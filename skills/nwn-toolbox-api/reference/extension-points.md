# Extension points and utilities

The complete list of interfaces Toolbox collects from the shared Anvil container. Each is
implemented in your assembly, annotated `[ServiceBinding(typeof(TheInterface))]`, and
picked up with no further wiring.

| Interface | Namespace | Collected by | Covered in |
| --- | --- | --- | --- |
| `IWindowView` | `Jorteck.Toolbox.Core` | `WindowManager` | `nui-windows.md` — **inherited from `WindowView<T>`; don't add the attribute** |
| `IChatCommand` | `…Features.Chat` | `ChatCommandService` | `chat-commands.md` |
| `IBlueprintSource` | `…Features.Blueprints` | `BlueprintManager` | below |
| `ILanguage` | `…Features.Languages` | `LanguageService` | below |
| `IPersistenceStore` | `…Core.Persistence` | `PersistenceStorageService` | below — **registered by a call, not the container** |

`IWindowController`, `IWizardRootView`, `IWizardStepView`, `IWizardStepController<T>`, and
`IDialogView` are structural interfaces used inside the window system, not container
extension points — you implement them, but nothing collects them from the container.

None of this works from a plugin marked `Isolated`: Anvil keeps isolated plugins out of the
shared container, so Toolbox never sees your registrations, and there's no error.

## Blueprint sources

`BlueprintManager` merges results from every registered `IBlueprintSource`. Toolbox's own
source reads the module palette; add one to surface blueprints from a database, a generated
set, or another plugin's content in the DM spawn UI.

```csharp
[ServiceBinding(typeof(IBlueprintSource))]
public sealed class MyBlueprintSource : IBlueprintSource
{
  public IEnumerable<IBlueprint> GetBlueprints(
    BlueprintObjectType blueprintType, int start, string search, int count)
  {
    // start = offset, count = max to return, search = user's filter text (may be empty)
    return Array.Empty<IBlueprint>();
  }
}
```

`IBlueprint` requires `FullName`, `Name`, `Category`, `CR` (nullable float), `Faction`,
`ObjectType`, plus two creation methods — `NwObject Create(Location location)` for placing
in the world and `NwItem Create(NwGameObject owner)` for creating into an inventory.
Return null from whichever doesn't apply to your object type.

`BlueprintObjectType` is `Creature | Door | Encounter | Item | Placeable | Sound | Store |
Trigger | Waypoint`.

How `BlueprintManager.GetMatchingBlueprints(objectType, search, max)` queries you: first a
round of `GetBlueprints(type, 0, search, max / sourceCount)` from every source, then, if
that came up short, a second round at offset `max / sourceCount` for the remainder.
Results are merged and sorted by `FullName`. **Honour `start` and `count`** or the second
round will hand back duplicates.

## Languages

`ILanguage` adds an in-character language to the garbling system:

```csharp
[ServiceBinding(typeof(ILanguage))]
public sealed class LanguageMyTongue : ILanguage
{
  public string Id => "mytongue";                    // stable, used as the persisted key
  public string[] Aliases => new[] { "mt" };         // optional, defaults to null
  public string Name => "My Tongue";
  public Color ChatColor => new Color(51, 255, 153);
  public bool Enabled => true;

  public LanguageOutput Translate(string phrase, int proficiency)
  {
    const int seed = 1234;   // stable per language — same input garbles the same way
    return LanguageUtils.TranslateWithSeed(this, seed, phrase, proficiency);
  }
}
```

`proficiency` runs on the `LanguageProficiency` int scale — `Untrained` 0, `Beginner` 25,
`Intermediate` 50, `Advanced` 75, `Fluent` 100. DMs always get `Fluent`.

Return a `LanguageOutput`. **Its constructor is `(language, interpretation, output)` but
its fields are declared `Language, Output, Interpretation`** — easy to transpose. `Output`
is the garbled text everyone hears; `Interpretation` is what a listener who knows the
language reads. `LanguageUtils.TranslateUsingDictionary(...)` and
`TranslateWithSeed(...)` are the helpers Toolbox's own languages use, and give consistent
garbling for free.

`Enabled` is your call, but note the built-in languages gate it on
`ConfigService.Config.Languages.IsEnabled()`, and `ConfigService` is internal — so a
third-party language can't see the server's language feature flag. Returning `true`
unconditionally registers it even on servers with languages off; harmless, since
`LanguageChatService` won't route to it, but expect confusion.

`LanguageService` exposes `Languages`, `PlayerKnowsLanguage`, `GetLanguageProficiency`;
both of the latter need a `LanguageState`, obtained from
`LanguageService.GetStateForPlayer(player)`. `LanguageChatService` handles the chat
integration. Both services are public and injectable.

## Persistence store

`PersistenceStorageService` is Toolbox's per-player key/value store — it's what remembers a
player's dice-roll mode, language selection, and similar. It's public, so you can use it
for your own small per-player settings:

```csharp
persistenceStorageService.UpdateState(player, "myplugin.setting", myStruct);
MyType value = persistenceStorageService.GetState<MyType>(player, "myplugin.setting");
```

Namespace your keys — the store is flat and shared with Toolbox.

The default backend, `PersistentVariablePersistenceStore`, writes to
`PersistentVariableStruct<T>` on the player's **controlled** creature, so `T` must be
JSON-serialisable, and a DM possessing an NPC writes to the NPC.

**Both `GetState` and `UpdateState` throw `NullReferenceException` when the player has no
controlled creature** — `GetState`'s `?.` doesn't save you, because the result goes through
an implicit conversion that dereferences it. Guard on `player.ControlledCreature != null`
yourself. With a creature present but nothing stored, `GetState` returns `default(T)`.

You can replace the backend wholesale — implement `IPersistenceStore` and call
`SetActiveStore`. Unlike the other extension points this is **not** container-collected:
`[ServiceBinding(typeof(IPersistenceStore))]` does nothing, you have to call the setter.
Do it from an `IInitializable.Init()` in a service that depends on
`PersistenceStorageService`; the default store is only assigned on the first scheduler
update after startup, so an `Init()`-time call wins.

Make that registration re-runnable rather than one-shot: `PersistenceStorageService.Dispose()`
nulls the active store, so a custom store is discarded on Anvil reload — and any
`GetState`/`UpdateState` after container teardown NREs.

For anything larger than settings, use your own storage rather than this store — Anvil's
`PersistentVariable*` types and campaign database are the general-purpose options, and
Toolbox's own SQLite `Database` is internal.

## Utility extensions

Public, in the root `Jorteck.Toolbox` namespace:

- `NuiUtils` — `CreateComboForEnum<T>`, `.Assign(out …)`, `.Configure(…)`. See
  `nui-windows.md`.
- `ObjectExtensions` — `NwObject.GetTypeName()` returns a display string ("Player",
  "Placeable", "Area of Effect"); `NwObject.GetSelectionType()` maps an object to an
  `ObjectSelectionTypes` flag.
- `ChatExtensions` (in `ChatUtils.cs`) — `TalkVolume` ↔ `ChatVolume` conversion,
  `GetAreaShoutMessage(string)`.
- `CreatureSizeExtensions` — `CreatureSize.ACModifier()`.

`NwPlayerExtensions` (including `SendErrorMessage`), `DbContextExtensions`, and
`UXConstants` are **internal** despite looking like general-purpose helpers. Write your own
one-liner rather than trying to reach them.
