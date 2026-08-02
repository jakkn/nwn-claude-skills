# Bundled Anvil services

Anvil ships a set of services you get by declaring them as constructor dependencies. Most
wrap engine function hooks, so using one is almost always better than writing the hook
yourself — read this before reaching for `HookService`.

```csharp
[ServiceBinding(typeof(MyService))]
public sealed class MyService
{
  public MyService(SchedulerService scheduler, ChatService chat) { ... }
}
```

## Contents

- [Scheduling and lifecycle](#scheduling-and-lifecycle)
- [Chat and feedback](#chat-and-feedback)
- [Scripts and events](#scripts-and-events)
- [Storage and resources](#storage-and-resources)
- [2DA tables](#2da-tables)
- [Rules and mechanics overrides](#rules-and-mechanics-overrides)
- [Player presentation](#player-presentation)
- [Character validation (ELC)](#character-validation-elc)
- [Targeting](#targeting)
- [Low-level](#low-level)

## Scheduling and lifecycle

**`SchedulerService`** — timed callbacks on the server thread. Both methods return a
`ScheduledTask` implementing `IDisposable`; dispose to cancel.

```csharp
IDisposable repeating = scheduler.ScheduleRepeating(Tick, TimeSpan.FromMinutes(10));
IDisposable once      = scheduler.Schedule(Later, TimeSpan.FromMinutes(20));
scheduler.Schedule(action, SchedulerService.NextUpdate);   // run on the next server loop
```

`ScheduledTask` also exposes `ExecutionCount`, `FailedExecutionCount`, `IsCancelled`,
`Cancel()`. Prefer this over `OnHeartbeat` for periodic work — heartbeats are locked to the
engine's 6-second tick and fire per object.

For per-tick work, implement `IUpdateable` and add `[ServiceBinding(typeof(IUpdateable))]`
— unlike `IInitializable`, this one is not bound implicitly, so a class that only implements
the interface is never called. `Time.DeltaTime` gives the frame delta. See
`patterns.md#logging-and-diagnostics` for the double-binding shape.

## Chat and feedback

**`ChatService`** — send and shape chat traffic.

```csharp
chat.SendServerMessage(ChatChannel.PlayerTalk, "hello", targetPlayer);
chat.SendMessage(ChatChannel.PlayerShout, "hello", senderCreature, targetPlayer);
chat.SetChatHearingDistance(ChatChannel.PlayerTalk, 30f);              // global
chat.SetPlayerChatHearingDistance(player, ChatChannel.PlayerTalk, 5f); // per player
chat.ClearPlayerChatHearingDistance(player);
```

`GetChatHearingDistance` / `GetPlayerChatHearingDistance` read the current values. To
intercept or rewrite messages, subscribe to `OnChatMessageSend` (skippable) rather than
using this service.

**`FeedbackService`** — hide combat log and feedback spam, globally or per player.

```csharp
feedback.AddFeedbackMessageFilter(FeedbackMessage.SkillCantUse, player);
feedback.AddCombatLogMessageFilter(CombatLogMessage.Feedback);
feedback.FeedbackMessageFilterMode = FilterMode.Whitelist;  // or Blacklist
```

Also `RemoveFeedbackMessageFilter`, `RemoveCombatMessageFilter`, `IsFeedbackMessageHidden`,
`IsCombatLogMessageHidden`, and `CombatMessageFilterMode`.

## Scripts and events

**`ScriptHandleFactory`** — register NWScript-named handlers at runtime, the dynamic
counterpart to the `[ScriptHandler("name")]` attribute.

```csharp
ScriptCallbackHandle handle = factory.RegisterScriptHandler("my_script", OnCalled);
ScriptCallbackHandle unique = factory.CreateUniqueHandler(OnCalled); // generated name
factory.UnregisterScriptHandler("my_script");
factory.IsScriptRegistered("my_script");
```

Callbacks take `CallInfo` (`ObjectSelf`, `ScriptName`, `ScriptType`, `ScriptParams`,
`TryGetEvent<T>`) and return `ScriptHandleResult` (`Handled`, `NotHandled`, `True`,
`False`). Script names are capped at 16 characters, same as the toolset.

`CreateUniqueHandler` is how you hand a callback to an engine API that wants a script
name — event scripts, item property callbacks, `EffectRunScript`.

**`EventService`** — the machinery behind `+=` on `Nw*` objects. The main reason to touch it
directly is bulk-unsubscribing:

```csharp
eventService.ClearObjectSubscriptions(someObject);
```

`EventCallbackType.After` exists, but only the native (hook-backed) events dispatch it.
`GameEventFactory`, which backs every toolset event (`ModuleEvents.*`, `AreaEvents.*`,
`CreatureEvents.*`, …), only ever raises `Before` — subscribing `After` to one of those
silently never fires.

## Storage and resources

**`ObjectStorageService`** — managed key/value storage attached to an object, with optional
persistence alongside the character or object.

```csharp
ObjectStorage storage = objectStorage.GetObjectStorage(creature);
storage.Set("myplugin", "score", 42, persist: true);
int? score = storage.GetInt("myplugin", "score");
storage.Remove("myplugin", "score");
```

`Set`/`GetInt`/`GetFloat`/`GetString`/`ContainsX`, plus `TryGetObjectStorage` and
`DestroyObjectStorage`. Prefer the strongly-typed wrappers over raw prefix/key calls:

```csharp
creature.GetObjectVariable<PersistentVariableInt>("score").Value = 42;
```

The concrete wrapper types are `PersistentVariableInt`, `PersistentVariableBool`,
`PersistentVariableFloat`, `PersistentVariableString`, `PersistentVariableGuid`,
`PersistentVariableEnum<T>`, `PersistentVariableStruct<T>`. The `ObjectStorageVariable*`
types they derive from are abstract — `GetObjectVariable<T>` requires a concrete `new()`
type, so naming the base directly won't compile.

**`PluginStorageService`** — `GetPluginStoragePath(Assembly)` returns the per-plugin
directory Anvil sets aside for your data files. Use it instead of writing next to the DLL.

**`ResourceManager`** — read and inject game resources at runtime.

```csharp
byte[]? data  = resources.GetResourceData("nw_rat001", ResRefType.UTC);
string? text  = resources.GetResourceText("mytable", ResRefType.TWODA);
resources.WriteTempResource("gen_item.uti", bytes);   // becomes loadable immediately
resources.CreateResourceDirectory("/path/to/dir");     // add a resource search path
bool exists   = resources.IsValidResource("nw_rat001", ResRefType.UTC);
```

`WriteTempResource` is the mechanism for generating blueprints or 2DAs at runtime.
`ResourceManager.MaxNameLength` is 16. `HomeStorage` exposes Anvil's own directories
(`Plugins`, `PluginData`, `ResourceTemp`, `NLogConfig`, `Paket`).

## 2DA tables

`NwGameTables` has typed properties for around 35 common tables — `AppearanceTable`,
`VisualEffectTable`, `ExpTable`, `PortraitTable`, `ItemPropertyTable`, the `Parts*` family
and so on. Check `api-index.md` under `Anvil.API.NwGameTables` for the full list and use
these in preference to loading the same table yourself.

For a custom or unwrapped 2DA, define an entry type:

```csharp
public sealed class FactionRankEntry : ITwoDimArrayEntry
{
  public int RowIndex { get; init; }        // populated for you — don't assign it
  public string Name { get; private set; } = string.Empty;
  public int MinReputation { get; private set; }

  public void InterpretEntry(TwoDimArrayEntry entry)
  {
    Name = entry.GetString("Name") ?? string.Empty;
    MinReputation = entry.GetInt("MinRep").GetValueOrDefault(0);
  }
}

TwoDimArray<FactionRankEntry> ranks = NwGameTables.GetTable<FactionRankEntry>("faction_ranks")!;
```

Tables loaded *by name* are cached, and the cache remembers the entry type — asking for one
of those with a different `T` throws `InvalidOperationException`. That affects the ten Anvil
loads by name: `exptable`, `damagelevels`, `effecticons`, `environment`, `loadscreens`,
`iprp_costtable`, `iprp_paramtable`, `placeableobjsnds`, `placeabletypes`, `progfx`. Use the
`NwGameTables` property for those, or pass `checkCacheType: false`. The rest of the wrapped
tables are loaded from native handles and aren't in the cache, so a custom entry type works.
`useCache: false` forces a re-read either way. The `.2da` suffix is optional.

`TwoDimArrayFactory.Get2DA<T>` still exists but is `[Obsolete]` — create
`Anvil.API.TwoDimArray` instances or use `NwGameTables.GetTable<T>` instead. With
`TreatWarningsAsErrors` on (Anvil's own default) using it will fail the build.

## Rules and mechanics overrides

Each of these hides a function hook behind a small API. Reach for the service before
writing your own hook.

**`WeaponService`** — extend weapon feats and rules to custom base items.

```csharp
weapons.AddWeaponFocusFeat(baseItem, feat);
weapons.AddEpicWeaponDevastatingCriticalFeat(baseItem, feat);
weapons.SetWeaponFinesseSize(baseItem, CreatureSize.Medium);
weapons.SetWeaponIsMonkWeapon(baseItem);
weapons.SetMaxRangedAttackDistanceOverride(baseItem, max, maxPassive, preferred);
weapons.OnDevastatingCriticalHit += data => data.Bypass = true;
```

Also `GreaterWeaponFocusAttackBonus`, `GreaterWeaponSpecializationDamageBonus`,
`EnableSlingGoodAimFeat`, and the `AddGreater*` / `AddEpic*` / `AddWeaponOfChoice*` family.

**Creature overrides**

| Service | What it does |
| --- | --- |
| `CreatureForceWalkService` | `Get/SetAlwaysWalk(creature, bool)` |
| `CreatureWalkRateCapService` | `Get/SetWalkRateCap(creature, float?)` |
| `InitiativeModifierService` | `Get/Set/ClearInitiativeModifier(creature, int)` |
| `DamageLevelOverrideService` | `Get/Set/ClearDamageLevelOverride(creature, DamageLevelEntry)` |
| `BypassLevelUpValidationService` | `DisableValidation` flag |
| `PlayerRestDurationOverrideService` | `Get/Set/ClearDurationOverride(creature, TimeSpan)` |
| `ItemMinEquipLevelOverrideService` | `Get/Set/ClearMinEquipLevelOverride(item, byte)` |

## Player presentation

**`PlayerNameOverrideService`** — show different names to different observers.

```csharp
// PlayerNameOverride(string characterName, string playerName = "Someone") — get-only props.
PlayerNameOverride nameOverride = new PlayerNameOverride("Hooded Figure", "???");

names.SetPlayerNameOverride(target, nameOverride);
names.SetPlayerNameOverride(target, nameOverride, observer);  // observer-specific
names.ClearPlayerNameOverride(target, clearAll: true);
```

Plus `GetPlayerNameOverride`, `GetOverridesForObserver`, and the `OverwriteDisplayName`,
`ShowOverridesToDM`, `PlayerListNameType` settings.

**`PlayerObjectNameOverrideService`** — `Get/Set/ClearObjectNameOverride(player, object, name)`
for renaming any game object per observer.

**`ObjectVisibilityService`** — hide objects globally or per player.

```csharp
visibility.SetPersonalOverride(player, target, VisibilityMode.Hidden);
visibility.SetGlobalOverride(target, VisibilityMode.Visible);
```

**`PlayerLoopingVisualEffectService`** —
`AddLoopingVisualEffect(player, gameObject, VisualEffectTableEntry)` (note the singular),
with `GetLoopingVisualEffects(player, gameObject)` and
`ClearLoopingVisualEffects(player, gameObject)`.

**`PlayerPossessionService`** — `PossessCreature(player, creature, mindImmunity, createQuickBar)`.

## Character validation (ELC)

**`EnforceLegalCharacterService`** replaces the stock ELC with hookable events:

```csharp
elc.OnValidationBefore  += e => { };
elc.OnValidationFailure += e => { /* e.Type, e.SubType, e.StrRef, ... */ };
elc.OnValidationSuccess += e => { };
elc.OnCustomCheck       += e => { };
elc.EnforceDefaultEventScripts = true;
elc.EnforceEmptyDialog = true;
```

Failure event types are specialised — `OnELCSkillValidationFailure`,
`OnELCFeatValidationFailure`, `OnELCSpellValidationFailure`, `OnELCItemValidationFailure`,
`OnELCLevelValidationFailure` — see `api-index.md`.

## Targeting

There is no injectable targeting service — `CursorTargetService` is `internal`. Use the
player API: `player.EnterTargetMode(handler, settings)` or `TryEnterTargetMode(...)`, which
take the callback directly. `TargetModeSettings` (`ValidTargets`, `CursorType`,
`BadCursorType`, `TargetingData`) shapes the cursor, and `TargetingData` (`Shape`, `Flags`,
`Spell`, `Feat`, `Size`, `Range`) draws spell-style targeting geometry. See
`patterns.md#cursor-targeting`.

## Low-level

**`HookService`** — install your own native function hooks. See `hooks.md`.

**`InjectionService`** — `Inject<T>(instance)` populates `[Inject]` properties on an object
you constructed yourself, for objects that live outside the container (pooled entities,
things deserialized from disk). Note that `ObjectVariable` subclasses are already injected
for you by `GetObjectVariable<T>`, so they don't need this.

**`EncodingService`** — the `Encoding` the server uses for strings, for correct handling of
non-ASCII text when crossing the native boundary.

**`DialogService`** — inspect and rewrite conversation nodes while a dialog script runs:
`CurrentNodeType`, `CurrentNodeId`, `CurrentNodeIndex`, `CurrentScriptType`,
`GetCurrentNodeText(language, gender)`, `SetCurrentNodeText(...)`.
