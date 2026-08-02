# Anvil patterns

Working recipes for the things plugins do most. Each is a shape to adapt, not a snippet to
paste — check exact signatures in `api-index.md`.

## Contents

- [Plugin project setup](#plugin-project-setup)
- [Replacing an NWScript script](#replacing-an-nwscript-script)
- [Chat commands via interface binding](#chat-commands-via-interface-binding)
- [Effects and object context](#effects-and-object-context)
- [Item properties](#item-properties)
- [Variables and persistence](#variables-and-persistence)
- [2DA tables](#2da-tables)
- [Async and timing](#async-and-timing)
- [Cursor targeting](#cursor-targeting)
- [NUI windows](#nui-windows)
- [Logging and diagnostics](#logging-and-diagnostics)

## Plugin project setup

A plugin is a .NET class library targeting the framework Anvil is built against (net8.0 as
of the 8193.36 line — check the `NWN.Anvil` package's target before assuming).

```
dotnet new install NWN.Templates
dotnet new anvilplugin
dotnet build
```

The build output folder is copied whole into `<nwn home>/anvil/Plugins/<PluginName>/` —
the `.dll`, `.deps.json` and `.pdb` all matter. Anvil discovers `[ServiceBinding]` types by
scanning the loaded assembly, so there's nothing to register.

Look for `[ServiceBindingOptions(PluginDependencies = new[] { "OtherPlugin" })]` when a
service should only load if a sibling plugin is present.

## Replacing an NWScript script

`[ScriptHandler("name")]` on a method in a bound service makes Anvil run that method
whenever the engine would have run the script of that name — from a toolset event slot, a
conversation, an item property, or another script.

```csharp
[ServiceBinding(typeof(ScriptHandlers))]
public sealed class ScriptHandlers
{
  // Name must be <= 16 characters, same as the toolset.
  [ScriptHandler("open_gate")]
  private void OnOpenGate(CallInfo callInfo)
  {
    NwObject? self = callInfo.ObjectSelf;
  }

  // Return bool for a conditional (StartingConditional) script.
  [ScriptHandler("gate_is_open")]
  private bool GateIsOpen(CallInfo callInfo) => true;
}
```

The method may take no parameters, or a single `CallInfo` giving `ObjectSelf`,
`ScriptName`, `ScriptType`, `ScriptParams`, and `TryGetEvent<TEvent>(out …)` when the
script slot corresponds to a known event. Returning `ScriptHandleResult.NotHandled` lets
the original script run; anything else consumes it.

For handlers created at runtime — or where you need to hand a script *name* to an engine
API — use `ScriptHandleFactory.CreateUniqueHandler(callback)` and pass the returned
handle's script name.

**The handler method must be an instance method, never `static`.** Anvil registers it via
`Delegate.CreateDelegate(delegateType, serviceInstance, methodInfo)`, which always supplies
the service instance as the delegate target — for a `static` method .NET binds that target
to the method's *first parameter* instead, the signature no longer matches, and the binder
throws `ArgumentException: Cannot bind to the target method because its signature is not
compatible with that of the delegate type`.

Note this happens at server start, while `ScriptHandlerAttributeDispatchService` walks the
plugin's methods — it scans `BindingFlags.Static` as well as `Instance`, so a static handler
isn't quietly skipped, it takes the server down. This is easy to trip over because the
method often genuinely doesn't touch instance state, so an IDE will offer to make it
`static`; don't accept that for anything carrying `[ScriptHandler]`.

## Chat commands via interface binding

The idiomatic extension-point pattern: many implementations, one consumer.

```csharp
public interface IChatCommand
{
  string Command { get; }
  void ExecuteCommand(NwPlayer caller);
}

[ServiceBinding(typeof(IChatCommand))]           // bind to the INTERFACE, not the class
public sealed class GpCommand : IChatCommand
{
  public string Command => "!gp";
  public void ExecuteCommand(NwPlayer caller) => caller.ControlledCreature?.GiveGold(10000);
}

[ServiceBinding(typeof(ChatHandler))]
public sealed class ChatHandler
{
  private readonly List<IChatCommand> commands;

  public ChatHandler(IEnumerable<IChatCommand> commands)   // receives every binding
  {
    this.commands = commands.ToList();
    NwModule.Instance.OnPlayerChat += OnChat;
  }

  private void OnChat(ModuleEvents.OnPlayerChat eventData)
  {
    IChatCommand? match = commands.FirstOrDefault(c => c.Command == eventData.Message);
    match?.ExecuteCommand(eventData.Sender);
  }
}
```

Set `eventData.Message = ""` in an `OnPlayerChat` handler to swallow the message so it
isn't broadcast.

## Effects and object context

`Effect.*` static factories build effects; `ApplyEffect` puts them on an object or location.

```csharp
Effect blindness = Effect.Blindness();
blindness.SubType = EffectSubType.Supernatural;

target.ApplyEffect(EffectDuration.Temporary, blindness, TimeSpan.FromSeconds(5));
target.ApplyEffect(EffectDuration.Instant, Effect.VisualEffect(VfxType.ComBloodCrtRed));
```

`Effect` is a mutable, `IDisposable` wrapper over unmanaged engine memory — `SubType`,
`Tag`, `DurationType`, `Creator`, `CasterLevel`, `Spell` and `ShowIcon` are all settable
after construction. Applying an effect copies it onto the target, so building one once and
keeping it in a `readonly` field to apply repeatedly is idiomatic and cheaper than
recreating it. Just don't mutate a shared instance from more than one place.

**The context trap.** Some effects record the object that created them (summons, damage
attribution, caster level, dispel checks). The creator is whoever holds the current script
context at the moment `Effect.X()` runs, which inside an event handler is often not who you
mean. Enter the intended creator's context first:

```csharp
await eventData.Player.ControlledCreature!.WaitForObjectContext();

// SummonCreature(resRef, summonVfx, delay, appearType, unsummonVfx) — the second
// argument is the *appearance* effect; the unsummon effect is the fifth.
Effect summon = Effect.SummonCreature("nw_rat001", VfxType.ImpUnsummon,
  unsummonVfx: VfxType.ImpUnsummon);

NwModule.Instance.StartingLocation.ApplyEffect(EffectDuration.Temporary, summon, TimeSpan.FromMinutes(5));
```

Removing effects means iterating the live set — but `ActiveEffects` is a lazy iterator over
the engine's stateful effect cursor, so removing while enumerating corrupts the walk.
Snapshot first:

```csharp
foreach (Effect effect in creature.ActiveEffects.ToList())
{
  if (effect.EffectType == EffectType.Blindness)
  {
    creature.RemoveEffect(effect);
  }
}
```

(Removing a single effect and immediately `break`ing is also safe.)

`Effect.Tag` is the practical way to find your own effects later — set it when you create
them rather than matching on type.

**Persistent area-of-effect auras.** `Effect.AreaOfEffect(vfxType, onEnterHandle,
heartbeatHandle, onExitHandle)` spawns an `NwAreaOfEffect` — the `AOE_MOB_*`/`AOE_PER_*`
persistent VFX types. Any handle left `null` becomes an empty string passed to the native
`EffectAreaOfEffect`, and an empty script name does **not** mean "no script" — the engine
falls back to whatever script is baked into `vfx_persistent.2da`'s `ONENTER`/`ONEXIT`/
`HEARTBEAT` column for that VFX row.

That fallback is the default, not the exception: of the 47 rows in the stock
`vfx_persistent.2da`, 37 ship an `ONENTER`, 20 a `HEARTBEAT` and 18 an `ONEXIT`, and only 5
have no script at all. They're real vanilla gameplay effects, not no-ops — row 18
(`AOE_MOB_UNEARTHLY`, i.e. `PersistentVfxType.MobUnearthly`) has `ONENTER = NW_S1_AuraUnEaA`,
a Will-save-or-die. Pick a row for its shape and radius and you inherit its scripts.

So supply a handle for **every** slot, including the ones you don't want, using a no-op
handler to positively suppress the 2DA default:

```csharp
// Held in fields, not locals: ScriptCallbackHandle is IDisposable and disposing it
// unregisters the script name, so the handles must outlive every AoE that references them.
private readonly ScriptCallbackHandle onEnter;
private readonly ScriptCallbackHandle noOp;

public AuraService(ScriptHandleFactory scriptHandleFactory)
{
  onEnter = scriptHandleFactory.CreateUniqueHandler(HandleAuraEnter);
  noOp = scriptHandleFactory.CreateUniqueHandler(_ => ScriptHandleResult.Handled);
}

// Every slot named — leaving heartbeatHandle out here would inherit the 2DA's.
Effect aura = Effect.AreaOfEffect(PersistentVfxType.MobUnearthly, onEnter, noOp, noOp);
```

Create the handles once per plugin, not once per AoE. Each `CreateUniqueHandler` call
registers a fresh generated script name that stays registered until disposed, so
per-instance handles leak registrations.

If the handlers are fixed for the life of the plugin, a `[ScriptHandler]` pair with constant
names is simpler than managing handles at all — see "Replacing an NWScript script" above.
There's no `Effect.AreaOfEffect` overload taking plain script names, so pairing it with
`[ScriptHandler]` means calling the native function yourself:

```csharp
Effect aura = NWScript.EffectAreaOfEffect(
  ((PersistentVfxTableEntry)PersistentVfxType.MobUnearthly).RowIndex,
  "aura_enter", "aura_hb", "aura_exit")!;
```

Declare the result as `Effect` rather than `var` — the conversion from the native handle is
implicit, and `var` leaves you with the raw type. The tradeoff is that you skip the
`AssertValid()` check `Effect.AreaOfEffect` performs on each handle, so a typo in a script
name fails silently at runtime instead of throwing at creation.

## Item properties

Same shape as effects, but scoped to an item.

```csharp
private readonly ItemProperty haste = ItemProperty.Haste();

item.AddItemProperty(haste, EffectDuration.Temporary, NwTimeSpan.FromRounds(5));

foreach (ItemProperty property in item.ItemProperties)
{
  if (property.Tag == "special_temp")
  {
    item.RemoveItemProperty(property);
  }
}
```

`AddItemProperty` takes an `AddPropPolicy` plus `ignoreDuration` / `ignoreSubType` /
`ignoreTag` flags controlling how it reconciles with a matching existing property — worth
setting deliberately rather than accepting the default when you re-apply on every equip.

## Variables and persistence

```csharp
// NWScript-visible locals — the interop surface with legacy scripts.
creature.GetObjectVariable<LocalVariableInt>("quest_stage").Value = 3;
bool done = creature.GetObjectVariable<LocalVariableBool>("quest_done").Value;
creature.GetObjectVariable<LocalVariableString>("note").Delete();

// Managed storage on an object, persisted with the character/object.
// Concrete types are PersistentVariable{Int,Bool,Float,String,Guid,Enum<T>,Struct<T>} —
// the ObjectStorageVariable* base types are abstract and won't satisfy the new() constraint.
creature.GetObjectVariable<PersistentVariableInt>("internal_score").Value = 10;

// Campaign database, independent of any object. Obtained from the module or a player,
// never constructed directly.
CampaignVariableInt tally = NwModule.Instance.GetCampaignVariable<CampaignVariableInt>("mydb", "tally");
CampaignVariableInt mine  = player.GetCampaignVariable<CampaignVariableInt>("mydb", "tally");
```

All of these expose `Value`, `Delete()`, and implicitly convert to their value type.
`HasValue`/`HasNothing` are on the `ObjectVariable` family only — `CampaignVariable` has
`Campaign`, `Name` and `Player` instead.

The typed variants differ per family: `LocalVariable*` is the widest (int, float, string,
bool, object, location, guid, enum, struct, `Cassowary`), `PersistentVariable*` covers
int/bool/float/string/guid/enum/struct, and `CampaignVariable*` covers
int/bool/float/string/guid/enum/object/location/vector.

Custom serialization is a subclass:

```csharp
public sealed class DateTimeLocalVariable : LocalVariable<DateTime>
{
  public override DateTime Value
  {
    get => DateTime.UnixEpoch + TimeSpan.FromSeconds(NWScript.GetLocalInt(Object, Name));
    set => NWScript.SetLocalInt(Object, Name, (int)(value.ToUniversalTime() - DateTime.UnixEpoch).TotalSeconds);
  }

  public override void Delete() => NWScript.DeleteLocalInt(Object, Name);
}
```

Choosing between them: plain service fields for anything that doesn't need to outlive the
session or be seen by NWScript; `PersistentVariable*` when the lifetime is genuinely tied
to an object and must survive; `LocalVariable*` when legacy scripts must read it;
`CampaignVariable*` for cross-restart global state.

## 2DA tables

```csharp
public sealed class FactionRankEntry : ITwoDimArrayEntry
{
  public int RowIndex { get; init; }
  public string Name { get; private set; } = string.Empty;
  public int MinReputation { get; private set; }

  public void InterpretEntry(TwoDimArrayEntry entry)
  {
    Name = entry.GetString("Name") ?? string.Empty;
    MinReputation = entry.GetInt("MinRep").GetValueOrDefault(0);
  }
}

private readonly TwoDimArray<FactionRankEntry> ranks =
  NwGameTables.GetTable<FactionRankEntry>("faction_ranks")!;

FactionRankEntry top = ranks[^1];
foreach (FactionRankEntry row in ranks.Rows) { }
```

`RowIndex` is populated by the framework — don't assign it in `InterpretEntry`.

Around 35 standard tables already have typed accessors on `NwGameTables`
(`NwGameTables.ExpTable`, `.AppearanceTable`, `.VisualEffectTable`, …). Use those. Calling
`GetTable<MyEntry>("exptable")` with your own entry type throws, because Anvil has already
cached that table under its own type — the cache is keyed by name and checks the type.

## Async and timing

```csharp
await NwTask.Delay(TimeSpan.FromSeconds(30));      // DelayCommand replacement
await NwTask.Delay(NwTimeSpan.FromRounds(2));      // also FromTurns, FromHours
await NwTask.NextFrame();
await NwTask.DelayFrame(100);
await NwTask.WaitUntil(() => NwModule.Instance.Players.Count() > 5);
await NwTask.WaitUntilValueChanged(() => creature.HP);

// Heavy pure computation off-thread, then back to safety.
await Task.Run(() => Crunch());
await NwTask.SwitchToMainThread();

// A task whose body may touch game APIs.
Task t = NwTask.Run(async () =>
{
  await NwTask.Delay(NwTimeSpan.FromRounds(5));
  NwModule.Instance.SendMessageToAllDMs("done");
});

await NwTask.WhenAny(t1, t2);   // and WhenAll
```

All of these accept an optional `CancellationToken`; a `CancellationTokenSource` is the
clean way to abandon a set of waits when one of them wins.

Because handlers are synchronous, async work from an event starts with a discard:
`NwModule.Instance.OnClientEnter += e => _ = HandleAsync(e);`. Anything captured before an
`await` may have been destroyed by the time you resume — re-check `IsValid`.

## Cursor targeting

```csharp
player.EnterTargetMode(OnTargetSelected, new TargetModeSettings
{
  ValidTargets = ObjectTypes.Creature | ObjectTypes.Placeable,
  CursorType = MouseCursor.Magic,
  BadCursorType = MouseCursor.NoMagic,
});

private void OnTargetSelected(ModuleEvents.OnPlayerTarget eventData)
{
  if (eventData.IsCancelled) return;             // true when TargetObject is null

  NwObject? target = eventData.TargetObject;     // the area, if a bare position was picked
  Vector3 position = eventData.TargetPosition;
}
```

`EnterTargetMode` silently cancels any targeting already in progress and installs your
handler. `TryEnterTargetMode` instead returns `false` when the player is already in cursor
target mode, leaving the existing handler alone — use it when you don't want to stomp on
another system's prompt.

Add `TargetingData` to the settings to draw spell-style shapes (`Shape`, `Size`, `Range`,
`Flags`, `Spell`, `Feat`).

## NUI windows

Build a layout tree, open it for a player, keep the token.

```csharp
NuiBind<string> nameBind = new NuiBind<string>("player_name");

NuiWindow window = new NuiWindow(new NuiColumn
{
  Children =
  {
    new NuiLabel(nameBind),
    new NuiRow { Children = { new NuiButton("Accept") { Id = "accept" } } },
  },
}, "My Window")
{
  Geometry = new NuiRect(-1, -1, 400, 300),   // -1 centres on that axis
  Closable = true,
};

if (player.TryCreateNuiWindow(window, out NuiWindowToken token))
{
  token.SetBindValue(nameBind, player.PlayerName);
  token.SetBindWatch(nameBind, true);   // notify on client-side changes
}
```

Handle interaction through `OnNuiEvent`:

```csharp
NwModule.Instance.OnNuiEvent += eventData =>
{
  if (eventData.EventType == NuiEventType.Click && eventData.ElementId == "accept")
  {
    string? name = eventData.Token.GetBindValue(nameBind);
    eventData.Token.Close();
  }
};
```

`eventData.ArrayIndex` identifies the row when the event comes from a `NuiList` (the engine
reports a sentinel when the event isn't from an array). `NuiWindowToken` also carries
`SetUserData<T>`/`GetUserData<T>` for hanging per-window state off the token instead of a
dictionary keyed by player.

Widgets live in `Anvil.API` — `NuiButton`, `NuiButtonImage`, `NuiButtonSelect`, `NuiCheck`,
`NuiCombo`, `NuiChart`, `NuiColorPicker`, `NuiImage`, `NuiLabel`, `NuiOptions`,
`NuiProgress`, `NuiSlider`, `NuiSliderFloat`, `NuiSpacer`, `NuiText`, `NuiTextEdit`,
`NuiToggles`, `NuiList` — with `NuiColumn`, `NuiRow`, `NuiGroup` for layout.

## Logging and diagnostics

```csharp
private static readonly Logger Log = LogManager.GetCurrentClassLogger();
Log.Info("message");
```

NLog is configured by `anvil/nlog.config`; output goes to the console and
`logs.0/anvil.log`. The logger name is the class name, so per-class loggers make filtering
work.

For per-tick instrumentation, implement `IUpdateable` and read `Time.DeltaTime`:

```csharp
[ServiceBinding(typeof(IUpdateable))]
[ServiceBinding(typeof(PerfService))]
public sealed class PerfService : IUpdateable
{
  public void Update() => Log.Info($"tick rate: {1 / Time.DeltaTime.TotalSeconds}");
}
```

Note the double binding: one registers it in the update loop, the other makes it injectable
by its own type.
