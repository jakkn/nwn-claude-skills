# Permissions

Toolbox ships a group/user permission system that server admins configure in
`groups.yml` and `users.yml`. From a plugin the usable surface is one class,
`PermissionsService` (`Jorteck.Toolbox.Features.Permissions`), plus the
`DMPermissionConstants` string constants. The config service, config types, and DM event
handlers are all internal. (`PermissionSet` is technically public, but the only thing that
returns one — `PermissionsConfigService.GetPermissionsForPlayer` — is internal, so you
can't obtain an instance.)

**The whole feature is disabled by default** (`PermissionsConfig.Enabled = false`) and many
servers never turn it on. Every call has to say what should happen in that case, which is
why `HasPermission` takes a default — and why getting that default wrong is the most
common way to ship a permission check that does nothing.

## Checking a permission

```csharp
[ServiceBinding(typeof(MyService))]
public sealed class MyService
{
  private readonly PermissionsService permissions;

  public MyService(PermissionsService permissions) => this.permissions = permissions;

  public void DoThing(NwPlayer player)
  {
    if (!permissions.HasPermission(player, "myplugin.dothing", defaultIfDisabled: player.IsDM))
    {
      // NB: Toolbox's own SendErrorMessage extension is internal — use Anvil's.
      player.SendServerMessage("You do not have permission to do that.", ColorConstants.Red);
      return;
    }
    // ...
  }
}
```

`defaultIfDisabled` defaults to `false` — i.e. omitting it means "deny everyone when the
permissions feature is off", which is almost never what you want. Pass `player.IsDM` for
DM tools, `true` for things everyone should have.

`permissions.IsEnabled` tells you whether the feature is on, if you need to branch on it
rather than supply a default.

## Key naming

Keys are free-form dotted strings. The conventions Toolbox itself follows, and which you
should match:

| Pattern | Used for |
| --- | --- |
| `command.{Command}` | Chat commands. Spaces in the command name become dots. `IChatCommand.PermissionKey`'s default. Case is **preserved** here. |
| `toolbox.window.list` | Seeing the toolbox button and window list at all. |
| `toolbox.window.use.{viewId}.{bindKey}` | An individual widget in a window, via `ApplyPermissionBindings`. Both segments **lowercased**. |
| `dm.*`, `playerdm.*`, `chat.*` | Built-in DM powers — see `DMPermissionConstants`. |
| `permissions.*` | The `perms …` commands' own keys. |

Namespace your own keys under your plugin (`myplugin.…`) so an admin can grant them with a
single wildcard. Don't invent keys under `toolbox.*`, `dm.*`, `playerdm.*`, `chat.*` or
`permissions.*`; those belong to Toolbox.

Note the casing inconsistency between the two mechanisms above — it's Toolbox's, not a
typo. Keep your own keys lowercase and it won't bite you.

`DMPermissionConstants` also has target suffixes — `TargetSelf`, `TargetCreature`,
`TargetPlayer`, `TargetItem`, `TargetPlaceable`, `TargetDoor`, `TargetStore`,
`TargetTrigger`, `TargetWaypoint`, `TargetEncounter` — which the DM handlers append to a
base key, e.g. `dm.spawn` + `.creature`. Follow that shape if your feature is
target-type-sensitive.

## How keys resolve

Worth understanding because it constrains how you should name things:

- A player's permission set is the union of their user entry's permissions and every group
  they're in, including inherited groups and the default group (`default`, or `dm` for
  DMs — which ships with `*`, so out of the box a DM has everything).
- An entry ending in `*` or `.*` becomes a **wildcard**, stored with the suffix stripped.
  Matching is a plain `StartsWith`, not a glob. So `dm.*` grants `dm.kill` — but note it
  also grants `dm-anything`, because the trailing dot was stripped along with the star.
- An entry starting with `-` removes that key from the set. Negations only remove what was
  already added, so a `-` must come after the grant it cancels — and the **user entry is
  parsed before any group entry**, so a `-foo` on a user can never cancel a `foo` granted
  by one of that user's groups. That surprises admins regularly; it's worth saying so in
  your own docs if you ship permission keys.
- Sets are resolved once per player and cached until the config is edited via the
  `/perms …` chat commands (the base name is server-configurable). A hand-edit of the YAML
  needs a reload.

## Gating a window

There is **no permission check on opening a window.** `WindowManager.OpenWindow` opens
whatever you ask it to, and a view with `ListInToolbox => true` is openable by anyone who
can see the toolbox list. If a whole window should be restricted, check
`HasPermission` yourself before calling `OpenWindow`.

`toolbox.window.list` — the key that gates the list itself — is evaluated **once, on client
enter**, defaulting to `player.IsDM`. A player promoted to DM mid-session never gets the
button until they reconnect.

What Toolbox does give you is widget-level gating inside a controller:

```csharp
ApplyPermissionBindings(View.ApplyEnabled, View.DeleteEnabled);
```

Each `NuiBind<bool>` is set to `HasPermission(player, $"toolbox.window.use.{View.Id}.{bind.Key}", true)`,
lowercased. Note the `true` — **widgets are enabled by default when the permissions
feature is off**, the opposite of the `HasPermission` default. Also note this only sets the
`Enabled` bind; it doesn't stop a crafted NUI event from reaching your handler, so
re-check server-side for anything destructive.

## Gating a chat command

Set `PermissionKey` (or accept the `command.{Command}` default) *and* `DMOnly`. Toolbox
picks between them: with permissions enabled it uses `PermissionKey`, with permissions
disabled it falls back to `!DMOnly || player.IsDM`. Setting only one leaves the other mode
wide open or fully closed.

## Known wart

`PermissionsService.GetGroups(player, includeDefault)` is unusable as of v8193.37.6. Its
early-return condition is inverted: it returns an empty sequence when the permissions
feature is *enabled*, and falls through to the config lookup when it's *disabled* — at
which point the group and user configs were never loaded from disk and the lookup throws a
`NullReferenceException`. Use `HasPermission`, which is correct. Worth reporting upstream
if you hit it.
