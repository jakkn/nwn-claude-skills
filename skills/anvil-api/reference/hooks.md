# Function hooking

Hooking intercepts a native engine function so you can observe it, change its inputs and
outputs, or replace it outright. It is the most powerful thing Anvil can do and the easiest
to crash a server with.

**Check `services.md` first.** Anvil already wraps dozens of hooks behind ordinary service
APIs (weapon feats, rest duration, visibility, initiative, name overrides, min-equip level,
walk rate, damage level, ELC). If one of those covers the need, use it — a bundled service
is tested, ordered correctly against Anvil's own hooks, and won't corrupt the stack.

**Check the event catalogue second.** Many "I need a hook" problems are really "I need a
skippable event" — `OnCreatureDamage`, `OnItemValidateEquip`, `OnSpellAction`,
`OnServerCharacterSave` and friends already exist, complete with mutable data and `Skip`.

Only when neither covers it should you write a hook.

## The overriding risk

A delegate whose signature doesn't match the C++ function **exactly** corrupts the stack.
Sometimes the server crashes immediately; sometimes it becomes a zombie and dies later in
an unrelated place, which is far worse to debug. Getting the signature right is the whole
job — take the type map below literally.

The mangled symbol names come from `nm -g` (Linux/macOS) and `dumpbin /exports` (Windows)
on the base game binaries. Verify a name by demangling it at https://demangler.com/ before
trusting it.

## Delegate marshalling

The general-purpose approach, and what you want for services.

```csharp
[ServiceBinding(typeof(RestDurationService))]
internal sealed unsafe class RestDurationService
{
  // C++: uint32_t CNWSCreature::AIActionRest(CNWSObjectActionNode* pNode)
  // First parameter is always the "this" pointer of the owning class.
  [NativeFunction(
    "_ZN12CNWSCreature12AIActionRestEP20CNWSObjectActionNode",  // gcc / linux
    "?AIActionRest@CNWSCreature@@QEAAIPEAVCNWSObjectActionNode@@@Z")]  // msvc / windows
  private delegate uint AIActionRestHook(void* pCreature, void* pNode);

  private readonly FunctionHook<AIActionRestHook> hook;

  public RestDurationService(HookService hookService)
  {
    hook = hookService.RequestHook<AIActionRestHook>(OnAIActionRest, HookOrder.Late);
  }

  private uint OnAIActionRest(void* pCreature, void* pNode)
  {
    CNWSCreature creature = CNWSCreature.FromPointer(pCreature);
    NwCreature? nwCreature = creature.ToNwObject<NwCreature>();

    // ... do work ...

    return hook.CallOriginal(pCreature, pNode);   // omit to replace the function entirely
  }
}
```

`FunctionHook<T>` is `IDisposable`; disposing removes the hook. Anvil disposes services'
hooks at shutdown, but if you install one outside a service lifetime, own the disposal.

## Function pointers

More performant, needed for very hot paths. Requires a `static` `[UnmanagedCallersOnly]`
method, which sits awkwardly with the service pattern — `HookEventFactory` exists to manage
that lifecycle. This is how Anvil implements its own native events.

```csharp
public sealed class OnServerCharacterSave : IEvent
{
  public NwPlayer Player { get; private init; }
  public bool PreventSave { get; set; }

  NwObject IEvent.Context => Player.ControlledCreature;

  // No [ServiceBinding] — HookEventFactory already declares it.
  internal sealed unsafe class Factory : HookEventFactory
  {
    // The [NativeFunction] attribute is required here too — RequestHook reads it off the
    // delegate type and throws without it.
    [NativeFunction("_ZN10CNWSPlayer19SaveServerCharacterEi",
      "?SaveServerCharacter@CNWSPlayer@@QEAAHH@Z")]
    private delegate int SaveServerCharacterHook(void* pPlayer, int bBackupPlayer);

    private static FunctionHook<SaveServerCharacterHook> Hook { get; set; }

    protected override IDisposable[] RequestHooks()
    {
      delegate* unmanaged<void*, int, int> pHook = &OnSaveServerCharacter;
      Hook = HookService.RequestHook<SaveServerCharacterHook>(pHook, HookOrder.Early);
      return new IDisposable[] { Hook };   // returned so they're disposed at shutdown
    }

    [UnmanagedCallersOnly]
    private static int OnSaveServerCharacter(void* pPlayer, int bBackupPlayer)
    {
      // ProcessEvent(EventCallbackType, eventData) dispatches to subscribers inside a
      // safe script context. Raise Before, call the original, then raise After.
      OnServerCharacterSave? eventData = ProcessEvent(EventCallbackType.Before,
        new OnServerCharacterSave
        {
          Player = CNWSPlayer.FromPointer(pPlayer).ToNwPlayer(),
        });

      int result = eventData!.PreventSave ? 0 : Hook.CallOriginal(pPlayer, bBackupPlayer);
      ProcessEvent(EventCallbackType.After, eventData);
      return result;
    }
  }
}
```

The type arguments on `delegate* unmanaged<void*, int, int>` are the parameters followed by
the return type.

Anvil's own `docs/development/function-hooks.md` shows a single-argument `ProcessEvent` and
omits the attribute on the pointer delegate — both are stale. Copy the shape from a real
event under `NWN.Anvil/src/main/API/Events/Native/`, not from that page.

Anvil keeps a catalogue of pre-declared, correctly-mangled delegates in
`Anvil.Native.Functions.*` (e.g. `Functions.CNWSPlayer.SaveServerCharacter`) and uses those
in its own events. The class is `internal`, so plugins can't reference it — but it is the
best place to *read* a known-good signature and its mangled names before writing your own
delegate.

`IEvent.Context` is what makes per-object subscription filtering work — return the object
the event is "about", or `null` if there isn't one.

## Hook order

`RequestHook`'s second argument decides where your hook sits relative to others. Anvil's own
hooks use the same scale, so picking sensibly keeps you composable with them.

| Constant | Value | Use for |
| --- | --- | --- |
| `HookOrder.Earliest` | -3000000 | Pure notification; never alters behaviour |
| `HookOrder.VeryEarly` | -2000000 | |
| `HookOrder.Early` | -1000000 | Skippable events; before/after state changes |
| `HookOrder.Default` | 0 | |
| `HookOrder.Late` | 1000000 | Conditional alternative implementations |
| `HookOrder.VeryLate` | 2000000 | |
| `HookOrder.Latest` | 3000000 | Almost never calls the original |
| `HookOrder.Final` | int.MaxValue | Full reimplementation |
| `HookOrder.SharedHook` | int.MinValue | Anvil-internal shared dispatch |

## C++ → C# type map

| C++ | C# | Notes |
| --- | --- | --- |
| `bool`, `BOOL` | `int` | |
| `uint8_t`, `char` | `byte` | |
| `uint8_t*`, `char*` | `byte*` | Convert char arrays via `StringHelper` to avoid code-page issues |
| `int32_t` / `uint32_t` | `int` / `uint` | |
| `int64_t` / `uint64_t` | `long` / `ulong` | |
| `float` | `float` | |
| `void`, `void*` | `void`, `void*` | |
| `RESTYPE` | `ushort` | |
| `ObjectID`, `OBJECT_ID`, `STRREF`, `PlayerID` | `uint` | |
| pointer/reference to class or struct | `void*` | Resolve with `XXX.FromPointer(void*)` |
| class/struct **by value** | matching C# struct | Harder — needs a C# struct with identical layout. Anvil's `CExoLocStringData` (used by `FeedbackService`) is the reference example; it's `internal`, so read it, don't reference it |

Pointer types follow the same mapping with `*` appended (`int32_t*` → `int*`).

## Crossing between native and managed

- `CNWSCreature.FromPointer(ptr)` and friends wrap a raw pointer as a native class.
- `.ToNwObject<NwCreature>()` / `.ToNwPlayer()` lift a native object to the Anvil API.
- `"text".ToExoString()` converts to `CExoString`; cache these in static readonly fields
  rather than converting per call.
- `NWNXLib.Rules()`, `.AppManager()` etc. reach the engine's global singletons.

Native types live in `NWN.Native.API`. They're visible without any special project setting,
but the pointer code you need to use them requires `<AllowUnsafeBlocks>true</AllowUnsafeBlocks>`
in the csproj and `unsafe` on the class or method.
