---
name: anvil-api
description: Reference and working patterns for the NWN.Anvil C# framework (Neverwinter Nights:EE server plugins). Use this whenever a task touches Anvil — writing or reviewing a service, subscribing to game events, working with NwCreature/NwPlayer/NwItem/NwModule or any Nw* type, effects and item properties, NUI windows, 2DA tables, local/persistent variables, function hooks, or NWScript-replacement script handlers. Also use it for "how do I do X in Anvil", plugin project setup, and any C# file that references Anvil.API or Anvil.Services. Consult this skill before reading Anvil's own source — the answer is almost always in the bundled reference files. Not for NWScript (.nss) code — see the nwn-nwscript-api skill — or for 2DA/hakpack authoring, which is the nwn-custom-content skill.
---

# Anvil API

Anvil is a C# framework that replaces NWScript for Neverwinter Nights: Enhanced Edition
servers. Plugins are .NET class libraries that Anvil loads at server start; the framework
wraps the engine in a managed object model (`Anvil.API`) and a dependency-injected service
container (`Anvil.Services`).

Anvil is consumed as the `NWN.Anvil` NuGet package. Its source is ~63k lines across 800+
files, so crawling it to answer a question is slow and usually unnecessary. Everything you
need is here.

## Finding an API

Work down this list and stop as soon as you have the answer:

1. **`reference/api-index.md`** — every public type and member in `Anvil.API` and
   `Anvil.Services`, one type per `##` heading, members bulleted beneath, enum values
   inlined. Grep it: `rg -A 60 '^## Anvil\.API\.NwCreature ' reference/api-index.md`, or
   `rg 'ApplyEffect' reference/api-index.md` to find which types expose a member. This is
   the fastest way to check whether a method exists and what its signature is.
2. **The topical references below** — for how pieces fit together rather than what exists.
3. **`https://nwn-dotnet.github.io/Anvil/`** — the official generated API docs, with the
   XML doc comments (parameter meanings, remarks, caveats) that the index omits.
4. **Anvil source** — only when behaviour is genuinely ambiguous, e.g. you need to know
   what a hook actually does to engine state. Say why you're doing it.

The index is generated from a specific Anvil version, recorded in its own header. If a
member you expect is missing, compare that against the `NWN.Anvil` version the project
references before concluding the API doesn't exist — and if they've diverged, say so rather
than working around a stale index. Regenerate with:

```
python3 scripts/generate_api_index.py /path/to/Anvil     # an Anvil git checkout
```

| Reference | Read it when |
| --- | --- |
| `reference/api-index.md` | Looking up any type, member, or enum value |
| `reference/events.md` | Subscribing to game events; which object exposes which event; skipping events |
| `reference/services.md` | Using a bundled Anvil service (scheduler, chat, feedback, ELC, weapon rules, visibility…) |
| `reference/patterns.md` | Recipes: script handlers, chat commands, 2DA tables, variables, NUI, targeting, async |
| `reference/hooks.md` | Hooking native engine functions; C++→C# type mapping |
| `reference/project-claude-md.md` | Setting a consuming project up to use this skill (`CLAUDE.md` snippet) |

## The service model

A plugin is a collection of services. A class annotated with `[ServiceBinding(typeof(T))]`
is constructed by Anvil at server start and registered in the container as `T`. There is no
`Main()`; construction *is* the entry point.

```csharp
using Anvil.API;
using Anvil.API.Events;
using Anvil.Services;
using NLog;

[ServiceBinding(typeof(WelcomeService))]
public sealed class WelcomeService
{
  private static readonly Logger Log = LogManager.GetCurrentClassLogger();

  private readonly SchedulerService scheduler;

  // Constructor parameters are dependencies. Anvil resolves and constructs them first,
  // so ordering between services is expressed by asking for what you need.
  public WelcomeService(SchedulerService scheduler)
  {
    this.scheduler = scheduler;
    NwModule.Instance.OnClientEnter += OnClientEnter;
  }

  private void OnClientEnter(ModuleEvents.OnClientEnter eventData)
  {
    eventData.Player.SendServerMessage("Welcome!", ColorConstants.Lime);
  }
}
```

Things worth knowing:

- **Never reach for `static` to share state between services.** Static access hides the
  initialization order problem rather than solving it, and it's the single most common
  structural mistake in Anvil plugins. Declare the dependency in the constructor instead.
- **Bind to an interface to get a collection.** Several classes can each declare
  `[ServiceBinding(typeof(IChatCommand))]`; a consumer then takes
  `IEnumerable<IChatCommand>` in its constructor and receives all of them. This is the
  idiomatic plugin-extension point.
- **Property injection** via `[Inject]` is available and equivalent to constructor
  injection, but the property is only populated *after* construction — pair it with
  `IInitializable.Init()`, not the constructor body.
- **Lifecycle interfaces.** `IInitializable.Init()` runs after construction and injection,
  and `ILateDisposable`/`IDisposable` are wired up, just by implementing them.
  `IUpdateable.Update()` (every server loop tick) is the exception — it needs an explicit
  `[ServiceBinding(typeof(IUpdateable))]` alongside your own binding, or it silently never
  runs. Put cleanup in `IDisposable.Dispose()`, which fires just before shutdown;
  `ILateDisposable.LateDispose()` runs *after* the server instance is destroyed, when no
  APIs are usable, and is skipped on hot reload — it's for releasing function hooks only.
- **`[ServiceBindingOptions]`** sets `BindingPriority` (higher loads first, and wins when
  several candidates satisfy one dependency), `Lazy = true` (construct only if something
  depends on it), and `PluginDependencies` (skip the service unless the named plugins are
  present).
- Log with NLog: `private static readonly Logger Log = LogManager.GetCurrentClassLogger();`.
  Output lands in `logs.0/anvil.log`.

## Events

Anvil exposes engine events as ordinary C# events on the object they concern, typed to an
event-data class:

```csharp
NwModule.Instance.OnClientEnter += eventData => { /* module-wide */ };
someArea.OnEnter               += eventData => { /* just this area */ };
somePlayer.OnPlayerChat        += eventData => { /* just this player */ };
```

Subscribing on `NwModule.Instance` is global; subscribing on a specific object filters to
that object. Both are backed by `EventService` — you rarely call it directly.

Handlers are `Action<TEvent>`, so they're synchronous. To do something asynchronous, kick
off a task and discard it: `NwModule.Instance.OnClientEnter += e => _ = HandleAsync(e);`.

Events whose data class implements `IEventSkippable` can suppress the default engine
behaviour by setting `eventData.Skip = true`. Many "before" events also expose mutable
properties (damage amounts, prevent-flags) that change the outcome without skipping.

Unsubscribe with `-=` when the subscriber's lifetime is shorter than the object's;
`EventService.ClearObjectSubscriptions(obj)` drops everything registered against an object.

`reference/events.md` has the full catalogue of which events each `Nw*` type exposes.

## The object model

```
NwObject ─┬─ NwModule
          ├─ NwArea
          └─ NwGameObject ─┬─ NwCreature
                           ├─ NwItem
                           ├─ NwStore
                           ├─ NwSound
                           ├─ NwWaypoint
                           ├─ NwAreaOfEffect
                           ├─ NwEncounter
                           └─ NwTrappable ─┬─ NwTrigger
                                           └─ NwStationary ─┬─ NwDoor
                                                            └─ NwPlaceable
```

`NwPlayer` is deliberately **not** an `NwObject` — it represents the client connection.
Its `ControlledCreature` (currently possessed) and `LoginCreature` (the character they
logged in with) are the `NwCreature` handles, and both are nullable.

Getting hold of objects:

- `NwModule.Instance` — always valid, the root of everything.
- `NwObject.FindObjectsWithTag<NwPlaceable>("my_tag")`, `NwObject.FindObjectsOfType<T>()`.
- `NwModule.Instance.Players`, `.Areas`, and area/creature collection properties.
- `someUint.ToNwObject<NwCreature>()` and `someUint.ToNwPlayer()` when interoperating with
  raw NWScript object IDs.
- `obj.IsPlayerControlled(out NwPlayer? player)` to narrow an object to a player.

Nullability is enabled throughout Anvil, so the compiler tells you what can be null —
trust the annotations rather than defensively null-checking everything. Beyond null,
objects can be *destroyed*: check `obj.IsValid` before using a handle you've been holding
across time (a field, a closure, a scheduled callback). Members that reach the native
object throw `InvalidOperationException` on a destroyed handle; the NWScript-backed
majority quietly no-op or return defaults, which is the more dangerous failure because it
looks like the code ran.

`ObjectId` is a session-scoped handle and must not be persisted. Use `obj.UUID` for an
identifier that survives restarts.

## Script context and threading

This is where subtle bugs come from, so it's worth internalising.

The engine runs on one thread and has a notion of "the object currently running a script"
(`OBJECT_SELF`). Some APIs read it implicitly — most importantly, effects created with
`Effect.*` record whoever is in context as the effect's creator, which determines caster
level, dispel behaviour, and combat attribution.

- To create something in a specific object's context: `await obj.WaitForObjectContext();`
  then build the effect. This is the async equivalent of NWScript's `AssignCommand`.
- Never touch Anvil APIs from a thread-pool thread. `Task.Run` work is fine for pure
  computation, but come back with `await NwTask.SwitchToMainThread();` before touching
  anything game-related.
- `NwTask.Run(...)` runs the whole lambda on the server thread, so game APIs are safe
  inside it. Plain `Task.Run(...)` does not.
- Delays: `await NwTask.Delay(TimeSpan)` or `NwTask.Delay(NwTimeSpan.FromRounds(2))`
  (`NwTimeSpan` also has `FromTurns`, `FromHours`) — the replacement for `DelayCommand`.
  `NwTask.NextFrame()`, `DelayFrame(n)`, `WaitUntil(predicate)`, and
  `WaitUntilValueChanged(selector)` cover the rest.
- For recurring or fire-once work that isn't naturally async, prefer `SchedulerService`:
  `scheduler.ScheduleRepeating(action, TimeSpan.FromMinutes(10))` returns a disposable —
  dispose it to cancel.

An object can be destroyed while a task is suspended, so re-check `IsValid` after any
`await` if you captured an object beforehand.

## Storing data

Four options, in increasing order of persistence:

- **Plain C# fields on your service** — best default. If the data doesn't need to be read
  by NWScript or survive a restart, don't put it in the game database.
- **`ObjectStorageService`** / the `PersistentVariable*` wrappers — int, float and string
  values keyed to an object, optionally persisted with the character or object (richer
  types via `PersistentVariableStruct<T>`, which serialises to JSON). Reach for this when a
  plain field can't work because the lifetime is tied to a specific object.
- **Local variables** — `obj.GetObjectVariable<LocalVariableInt>("name").Value`. These are
  the NWScript locals, so they're the interop surface with legacy scripts. Typed variants
  exist for int/float/string/bool/object/location/guid/enum/struct/Cassowary, and you can
  subclass `LocalVariable<T>` for a custom serialization.
- **Campaign variables** — `CampaignVariable*` types, backed by the campaign database,
  survive restarts independently of any object.

## Common mistakes

- Making a service member `static` to avoid injecting the service.
- Assuming an `NwObject` field is still alive — check `IsValid`, especially after `await`.
- Creating an `Effect` without first entering the intended creator's context.
- Calling game APIs from `Task.Run` instead of `NwTask.Run` / `SwitchToMainThread`.
- Persisting `ObjectId` instead of `UUID`.
- Reimplementing something Anvil already ships — skim `reference/services.md` before
  writing a hook or a bespoke system.
- Script handler names must be ≤ 16 characters, same limit as the toolset.

## Related skills

- `nwn-nwscript-api` — for `.nss` source. An Anvil server usually still has NWScript in the
  module; when a task spans both, Anvil's `[ScriptHandler]` and `CallInfo` are the seam.
- `nwn-custom-content` — for 2DA edits, hakpacks, and new blueprints. Anvil reads 2DAs
  (`NwGameTables`) but doesn't author them; content added there is what Anvil then reads.
