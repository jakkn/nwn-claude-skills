# Wiring a consuming project to this skill

The skill is installed globally (or symlinked into the project's `.claude/skills/`), but a
short note in the project's own `CLAUDE.md` makes the difference between an agent that
consults it and one that goes straight to reading `Jorteck.Toolbox` source. A project
consuming Toolbox is almost always an Anvil plugin too, so the block below assumes the
`anvil-api` skill is also installed and names both.

## Example

Adapt the versions and paths and drop it into the project's `CLAUDE.md`:

```markdown
## Anvil and NWN.Toolbox

This project is an NWN.Anvil plugin (`NWN.Anvil` <version>, net8.0) that consumes
`NWN.Toolbox` <version> as a package. Two skills cover these:

- `anvil-api` — the framework: `Nw*` types, events, effects, NUI primitives, the service
  container, `NwTask`.
- `nwn-toolbox-api` — what we consume from Toolbox: NUI window views/controllers, wizards
  and dialogs, `IChatCommand`, `PermissionsService`, blueprint sources.

Look things up there rather than reading either dependency's source:

- `nwn-toolbox-api/reference/api-index.md` — every **public** type and member in
  `Jorteck.Toolbox`. Grep it first. Toolbox is ~30% internal, and internal types are
  unreachable from this assembly — if a type isn't in the index, it isn't available to us,
  and the answer is "that's not part of the API" rather than "let me find it in the source".
- `nwn-toolbox-api/reference/nui-windows.md` — the view/controller pattern, which is how
  all our tool windows are written.
- `anvil-api/reference/api-index.md` — same idea for the framework underneath.

Reading Toolbox or Anvil sources directly is a last resort — if you do, say why, because it
usually means an index is stale and should be regenerated.

Local checkouts for that case: Anvil at `<path>`, NWN.Toolbox at `<path>`.
```

## Why this wording

- **Distinguish the two skills explicitly.** Without it, an agent asks Toolbox questions of
  the Anvil skill and vice versa. The one-line split — framework vs. what we consume on top
  — is enough to route correctly, and it stops "how do I make a NUI window" from being
  answered with raw `NuiWindow` when the project's convention is `WindowView<T>`.
- **Lead with the public/internal split.** This is the specific reason source-diving
  misfires for a *consumed package* rather than a checked-out framework: a large share of
  what an agent finds by grepping the source is uncallable. Saying so converts "the index is
  a convenience" into "the index is the definition of what exists".
- **Name the versions.** Each index is generated per version. An agent that knows what the
  project targets can spot divergence instead of trusting a stale entry.
- **Say "grep the index first", not just "the skill exists".** The failure mode isn't that
  agents don't know about the skill; it's that source-diving is the default reflex for a
  dependency whose code is on disk. Naming the specific first action displaces it.
- **Give source-reading an explicit escape hatch.** Forbidding it outright produces worse
  behaviour than making it a last resort that has to be justified — there are genuine cases
  (does this call check permissions? when does this fire?) where the source is the only
  answer, and an agent told "never" will bluff or stall.
- **Point at local checkouts if there are any.** Otherwise the escape hatch is unusable and
  the agent will guess.

## If several projects share this

Keep the block short and identical across projects so it stays easy to update. The details
that vary — the two package versions, checkout paths, project-specific conventions — belong
in that project's `CLAUDE.md`; everything else belongs in the skills, where it's versioned
once.
