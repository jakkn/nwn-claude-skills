---
name: nwn-toolbox-api
description: Reference and working patterns for consuming NWN.Toolbox (the Jorteck.Toolbox NuGet package) from your own Anvil plugin. Use this whenever a task references Jorteck.Toolbox — adding a NUI window via WindowView/WindowController, a wizard or dialog popup, a chat command via IChatCommand, permission checks via PermissionsService, blueprint sources, or the Toolbox persistence store. Also use it for "how do I hook into the Toolbox" and for any C# file that has a `using Jorteck.Toolbox` in it. Consult this skill before reading NWN.Toolbox's own source — the answer is almost always in the bundled reference files. Not for the underlying Anvil framework itself (see the anvil-api skill), and not for NWScript or 2DA/hakpack work.
---

# NWN.Toolbox API

NWN.Toolbox is an Anvil plugin for Neverwinter Nights:EE servers — a DM toolset (NUI tool
windows, chat commands, a permission system, blueprint spawning) that also doubles as a
framework other plugins build on. Root namespace is `Jorteck.Toolbox`; the NuGet package
and assembly are both `NWN.Toolbox`.

**When you're consuming Toolbox rather than modifying it, treat it as a closed API.** Of
its 146 top-level types, 103 are usable public API; the rest are `internal` or generated
EF migration code. Internal here means genuinely unreachable, because your plugin is a
separate assembly — so reading Toolbox source to answer "how do I do X" mostly turns up
code you cannot call. Everything reachable is listed in `reference/api-index.md`.

## Finding an API

Work down this list and stop as soon as you have the answer:

1. **`reference/api-index.md`** — every public type and member in `Jorteck.Toolbox`, one
   type per `##` heading, members bulleted beneath, enum values inlined, defining source
   file noted in the heading. Grep it:
   `rg -A 40 '^## Jorteck\.Toolbox\.Core\.WindowController' reference/api-index.md`, or
   `rg 'ApplyPermissionBindings' reference/api-index.md` to find which type exposes a
   member. Fastest way to check whether something exists and what its signature is.
   **If a type isn't in the index, it's internal — it is not "somewhere in the source".**
2. **The topical references below** — for how the pieces fit together.
3. **Toolbox source** — only to confirm runtime behaviour the signature doesn't reveal
   (does this check permissions? when does this fire?). Say why you're doing it.

The index is generated from a specific Toolbox version, recorded in its own header. If a
member you expect is missing, compare that against the `NWN.Toolbox` version the project
references before concluding the API doesn't exist. Regenerate with:

```
python3 scripts/generate_api_index.py /path/to/NWN.Toolbox    # a NWN.Toolbox git checkout
```

| Reference | Read it when |
| --- | --- |
| `reference/api-index.md` | Looking up any type, member, or enum value |
| `reference/nui-windows.md` | Adding a NUI window, wizard, dialog popup, or object-selection list |
| `reference/chat-commands.md` | Adding a chat command, sub-commands, argument parsing, help text |
| `reference/permissions.md` | Permission keys, gating widgets and commands, the DM permission constants |
| `reference/extension-points.md` | Blueprint sources, the persistence store, NUI/object helper extensions |
| `reference/project-claude-md.md` | Setting a consuming project up to use this skill (`CLAUDE.md` snippet) |

## How your plugin plugs into Toolbox

Everything hangs off one fact: **Anvil registers every non-isolated plugin's services into
a single shared container.** Toolbox's services and yours live in the same
`AnvilServiceContainer`, so a class in your assembly annotated
`[ServiceBinding(typeof(IChatCommand))]` is collected by Toolbox's own command service with
no registration call, no manifest, no reference from Toolbox back to you. Every Toolbox
extension point is an interface used this way.

**The corollary: an isolated plugin cannot extend Toolbox at all.**
`AnvilServiceManager` only folds a plugin's types into the shared container when
`!plugin.PluginInfo.Isolated`. An isolated plugin still *injects* Toolbox services fine
from the parent container, so half the integration appears to work while every
`IChatCommand`, `IWindowView`, `IBlueprintSource` and `ILanguage` you register is silently
never seen. If an extension point isn't firing, check the isolation flag first.

There is no `IToolboxApi` entry point and no initialization step. You either implement one
of its interfaces and let the container find you, or you inject one of its public services
and call it.

```csharp
// Inject a Toolbox service like any other Anvil service.
[ServiceBinding(typeof(MyService))]
[ServiceBindingOptions(PluginDependencies = new[] { "NWN.Toolbox" })]
public sealed class MyService
{
  private readonly WindowManager windowManager;

  public MyService(WindowManager windowManager, PermissionsService permissions)
  {
    this.windowManager = windowManager;
  }
}
```

`PluginDependencies` takes plugin *assembly* names — `"NWN.Toolbox"`, not the namespace.
A service naming a missing plugin is skipped at startup rather than throwing, which is what
you want for optional integration; omit it if Toolbox is a hard requirement and you'd
rather fail loudly.

The public services worth knowing: `WindowManager` (open windows),
`PermissionsService` (permission checks), `BlueprintManager` (blueprint lookup),
`PersistenceStorageService` (Toolbox's per-player key/value store),
`WindowAutoCloseService`, `AreaShoutService`, `DiceRollService`, `LanguageService`,
`LanguageChatService`.

### The inherited `[ServiceBinding]` rule

`WindowView<TView>` is declared `[ServiceBinding(typeof(IWindowView))]`, and Anvil reads
attributes with `inherit: true`. **Your concrete view subclass is therefore registered
automatically — don't add `[ServiceBinding(typeof(IWindowView))]` yourself.** It's
redundant rather than harmful: registration is keyed by implementation type, so a second
identical binding overwrites the first rather than duplicating it. Adding
`[ServiceBinding(typeof(MyView))]` is a different thing and is fine — it additionally binds
the concrete type so you can inject the view directly.

The visible consequence is that a new `WindowView<T>` shows up in the DM toolbox window
list the moment it compiles, with no opt-in. Set `ListInToolbox => false` if it's meant to
be opened programmatically only.

### Project setup

Reference the package and exclude its runtime assets, the same way Toolbox itself
references Anvil — Toolbox is loaded as its own Anvil plugin at runtime, so shipping a
second copy of the DLL in your plugin folder is wrong:

```xml
<PackageReference Include="NWN.Anvil"   Version="8193.37.2" ExcludeAssets="runtime" PrivateAssets="all" />
<PackageReference Include="NWN.Toolbox" Version="8193.37.6" ExcludeAssets="runtime" PrivateAssets="all" />
```

Keep the `NWN.Anvil` version aligned with the one Toolbox was built against (check
Toolbox's own `.csproj` for the release you're on) — Anvil's API moves between builds.

## Common mistakes

- Registering an extension point from a plugin marked `Isolated`. Nothing fires and
  nothing logs.
- Assuming `WindowManager.OpenWindow` checks permissions. It does not. See
  `reference/permissions.md` — widget-level gating via `ApplyPermissionBindings` is
  opt-in and is the *only* thing Toolbox does for you.
- Assuming a feature is on. `ChatCommandConfig` defaults to enabled, but **permissions,
  languages, server restart and version check all default to disabled.** Anything you
  gate on `HasPermission` is ungated on a default install unless you pass a sane
  `defaultIfDisabled`.
- Trying to use `ConfigService`, `ChatCommandService`, `PermissionsConfigService`,
  `Database`, or the `*Config` feature classes. All internal — bar `LanguageConfig`, which
  is public but useless, since only the internal `ConfigService` hands out instances. Your
  plugin owns its own config; Toolbox's YAML config is not an extension point.
- Reaching for a Toolbox helper that turns out to be `internal` (`NwPlayerExtensions`,
  `UXConstants`, `DbContextExtensions`). Grep the index before writing the call.
- Giving a window a generic `Id` like `"settings"`. IDs are a flat global namespace shared
  with Toolbox's own windows and with the server admin's whitelist/blacklist config —
  prefix yours.
- Making a view's `Title` null. `ToolboxWindowController` silently filters those out of
  the list.
- Persisting state in a controller. Controllers are created per window-open and discarded
  on close; put durable state in a service or `PersistenceStorageService`.

## Related skills

- `anvil-api` — the framework underneath. Anything about `NwCreature`, `NuiWindow`,
  effects, events, the service container, or `NwTask` is an Anvil question, and Toolbox
  changes none of it. Read that skill for the model; read this one for the seams Toolbox
  adds on top.
- `nwn-nwscript-api` — `.nss` source in the same module.
- `nwn-custom-content` — 2DA edits, hakpacks, blueprints as toolset content.
