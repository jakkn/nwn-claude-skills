# Chat commands

Toolbox owns the `OnPlayerChat` hook, prefix detection, argument tokenisation, permission
checks, arg-count validation, and help generation. You supply an `IChatCommand`.

Types live in `Jorteck.Toolbox.Features.Chat`.

## Adding a command

```csharp
using System;
using System.Collections.Generic;
using Anvil.API;
using Anvil.Services;
using Jorteck.Toolbox.Features.Chat;

[ServiceBinding(typeof(IChatCommand))]
public sealed class TeleportCommand : IChatCommand
{
  [Inject]
  private SomeService SomeService { get; init; }

  public string Command => "teleport";
  public string[] Aliases => new[] { "tp" };    // optional; not shown in help
  public bool DMOnly => true;
  public Range ArgCount => 1..2;
  public string Description => "Teleport to a waypoint.";

  public CommandUsage[] Usages { get; } =
  {
    new CommandUsage("<waypoint tag>", "Teleport yourself to the waypoint."),
    new CommandUsage("<waypoint tag> <player>", "Teleport another player to the waypoint."),
  };

  public void ProcessCommand(NwPlayer caller, IReadOnlyList<string> args)
  {
    // args excludes the command word itself. Arg count is already validated.
  }
}
```

The `[ServiceBinding(typeof(IChatCommand))]` is all the registration there is — Toolbox's
command service takes `IChatCommand[]` from the shared container and finds yours.

Unlike `WindowView<T>`, `IChatCommand` is an interface with no base class, so here you
*must* write the attribute yourself.

## What the interface members do

| Member | Notes |
| --- | --- |
| `Command` | The primary name, without prefix. Shown in help. |
| `Aliases` | Defaulted to `null`. Alternate names, hidden from help. |
| `DMOnly` | Only consulted when the permissions feature is **disabled**. |
| `PermissionKey` | Defaults to `"command.{Command}"` with spaces → dots. Only consulted when permissions are **enabled**. |
| `ArgCount` | A `Range`. `1..1` exactly one, `2..` two or more, `..2` at most two, `1..3` one to three, `..` any. |
| `Description` | One-line summary in the help list. |
| `Usages` | `CommandUsage(subCommand, description)` or `CommandUsage(description)` when the command takes no sub-command. |
| `IsAvailable` | Defaults to `true`. For hard runtime requirements (a missing dependency, a disabled feature) — *not* permissions. A false value produces `Command "x" is unavailable at this time.` |
| `ProcessCommand` | Called only after availability, permission, and arg-count checks pass. |

`Aliases`, `PermissionKey`, and `IsAvailable` have default interface implementations, so
omit them unless you need them.

## Dispatch rules worth knowing

- Prefix is server config, `/` by default, and there can be several. `//` is ignored by
  default so players can escape.
- Matching runs in two passes over the command list sorted alphabetically by `Command`:
  first an exact match of the whole message against `Command` or an alias (zero args), then
  a `StartsWith(Command + " ")` match.
- Multi-word `Command` values dispatch correctly through both passes, and Toolbox uses them
  itself — the permission commands are named `perms user addgroup` and similar (and
  override `PermissionKey` rather than relying on the space-to-dot default).
- **But a shorter command name shadows a longer one.** If `"give"` and `"give item"` both
  exist, `/give item gold` is dispatched to `"give"` with `args = ["item", "gold"]`,
  because `"give"` sorts first. So either keep the shared prefix out of any single
  command's name, or model sub-commands as arguments with an `args[0]` switch — which is
  what most built-ins do.
- Argument tokenisation splits on spaces but respects double quotes, and `""` inside a
  quoted string is an escaped quote. So `/say "hello ""world"""` yields one arg.
- A wrong arg count doesn't error — it silently runs the help command for your command
  instead. Test with the right count.
- An unrecognised command produces "Unknown command. Type /help for help."
- Your command's own args-based validation should fall back to
  `HelpCommand.ShowCommandHelpToPlayer(caller, this)`. Inject `HelpCommand`; it's public.

## Permissions

With the permissions feature enabled, use is gated on `PermissionKey`, defaulting to
`command.teleport` for a command named `teleport`. With it disabled, the gate falls back to
`DMOnly` — so set both. See `permissions.md`.

## Related public services

- `HelpCommand` — `ShowAvailableCommandsToPlayer(player)`,
  `ShowCommandHelpToPlayer(player, command)`, `GetCommandHelp(command)`.
- `AreaShoutService` — `SendMessage(NwCreature sender, string message)` and
  `GetFormattedAreaMessage(string)` for area-wide chat.
- `ChatExtensions` (static, namespace `Jorteck.Toolbox`, defined in `ChatUtils.cs`) —
  `TalkVolume.ToChatVolume()` / `ChatVolume.ToTalkVolume()` conversions and
  `ChatExtensions.GetAreaShoutMessage(string)`.
- `DiceRollService` (namespace `Jorteck.Toolbox.Features`, note: not `.DiceRolls`) — dice
  rolls with the same broadcast/visibility rules the built-in roll commands use.
- `LanguageService` / `LanguageChatService` (`Jorteck.Toolbox.Features.Languages`) — the
  in-character language garbling system. `LanguageService` exposes `Languages`,
  `PlayerKnowsLanguage`, `GetLanguageProficiency` and friends. Add a language by
  implementing `ILanguage` and annotating it `[ServiceBinding(typeof(ILanguage))]` — see
  `extension-points.md`.

`ChatCommandService` and `ChatShortcutService` themselves are internal — you can't call
into the dispatcher or trigger a command programmatically. Call the underlying service
your command wraps instead.
