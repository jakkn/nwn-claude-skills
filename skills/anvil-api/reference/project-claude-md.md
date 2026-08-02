# Wiring a consuming project to this skill

The skill is installed globally (or symlinked into the project's `.claude/skills/`), but a
short note in the project's own `CLAUDE.md` makes the difference between an agent that
consults it and one that goes straight to reading Anvil's source. Two paragraphs is enough;
the value is in being concrete about *where* the answer lives.

## Example

Adapt the paths and drop it into the project's `CLAUDE.md`:

```markdown
## Anvil

This project is an NWN.Anvil plugin (`NWN.Anvil` <version>, net8.0). Anvil replaces
NWScript with a C# service model — see the `anvil-api` skill, which is the reference for
this framework.

Look things up there rather than reading Anvil's source:

- `reference/api-index.md` — every public type, member and enum value. Grep it first; one
  `rg` usually answers "does this method exist and what's its signature".
- `reference/events.md` — which `Nw*` type publishes which event, and which are skippable.
- `reference/services.md` — the services Anvil already ships. Check here before writing a
  function hook; most of the common ones are already wrapped.
- `reference/patterns.md`, `reference/hooks.md` — recipes and native hooking.

If the index doesn't have it, the generated docs at https://nwn-dotnet.github.io/Anvil/
are the next stop. Reading the Anvil sources directly is a last resort — if you do, say
why, because it usually means the index is stale and should be regenerated.

A local Anvil checkout is at `<path>` for that case.
```

## Why this wording

- **Name the version.** The index is generated per Anvil version. An agent that knows which
  version the project targets can notice when the index and the package have diverged
  instead of silently trusting a stale entry.
- **Say "grep the index first", not just "the skill exists".** The failure mode isn't that
  agents don't know about the skill; it's that source-diving is the default reflex for a
  dependency whose code is right there. Naming the specific first action displaces it.
- **Give source-reading an explicit escape hatch.** Forbidding it outright produces worse
  behaviour than making it a last resort that has to be justified — there are genuine cases
  (undocumented hook side effects, engine state) where the source is the only answer, and an
  agent that has been told "never" will either bluff or stall.
- **Point at a local checkout if there is one.** Otherwise the escape hatch is unusable and
  the agent will guess instead.

## If several projects share this

Keep the block short and identical across projects so it stays easy to update. The details
that vary — Anvil version, local checkout path, any project-specific conventions — belong in
that project's `CLAUDE.md`; everything else belongs in the skill, where it's versioned once.
