---
name: nwn-nwscript-api
description: Use when writing, reviewing, or debugging NWScript (.nss) code for a Neverwinter Nights: Enhanced Edition (NWN:EE) multiplayer module — event handlers, conversation scripts, spell/item scripts, tag-based scripting. Not for non-script custom content (2DA/hakpack work — see the nwn-custom-content skill) or general C-family language questions unrelated to NWN's engine API.
---

# NWScript for NWN:EE

The authoritative, always-current function/event/constant reference is **NWN Lexicon** (https://nwnlexicon.com). This skill exists so an agent doesn't have to rediscover the lookup pattern every time and doesn't hallucinate function signatures.

## The one rule that matters most

**Never write a function call from memory alone if you're not certain of its exact name, parameter order, or default values.** NWScript has hundreds of engine functions, many with similar names (e.g. `GetFirstObjectInArea` vs `GetNearestObject` vs `GetObjectByTag`) and inconsistent parameter ordering between "similar" functions. A wrong signature usually won't produce a compile error you'd expect — it can compile with silently wrong defaults, or fail at runtime with no useful message. Before using an unfamiliar function, fetch its NWN Lexicon page.

## Looking up functions/events/constants

NWN Lexicon page URLs are the function/constant name directly off the root, e.g.:
- https://nwnlexicon.com/ApplyEffectToObject
- https://nwnlexicon.com/GetFirstObjectInArea
- https://nwnlexicon.com/DelayCommand

Category browse pages (useful when you know *what you want to do* but not the exact function name):
- All functions grouped by topic: https://nwnlexicon.com/Category:Functions (subcategories include Action on Object, Alignment, Combat, Conversation, Creature, Effect, Item, Object, Placeable, Sound, Visual Effect, and more)
- Constants: https://nwnlexicon.com/Category:Constants
- Events: https://nwnlexicon.com/Category:Events
- Data types: https://nwnlexicon.com/Category:Data_Types
- Tutorials/primers: https://nwnlexicon.com/Category:Tutorials and https://nwnlexicon.com/Category:Primers

If the project repo has a local copy of `nwscript.nss` (the base declarations file every module/toolset installation ships with), that is ground truth for exact signatures and is faster to check than fetching a page — prefer it when available. Check the repo root, a `nss/` or `scripts/` folder, or wherever the build tooling (e.g. Nasher, `nwn_script_comp`) expects source. If it's not in the repo, it can be pulled straight from the game data with neverwinter.nim's `nwn_resman_extract --pattern nwscript.nss` (see the nwn-custom-content skill's `reference/neverwinter-nim-cli.md` for the full CLI toolchain) rather than guessing at a copy found online.

## Language basics (things that trip up agents used to C/C++/Java)

- Case-sensitive, C-like syntax, but no pointers, no dynamic heap allocation, and (pre-EE) no user-defined structs — EE added `struct` support, don't assume it's absent, but check the target NWN version if the module isn't EE-only.
- No true recursion depth to rely on — the engine enforces stack/instruction limits per script execution; deep or unbounded recursion will fail at runtime with a script error, not a compile warning.
- Compiled scripts are capped at 64KB of bytecode. Very large single scripts (e.g. giant switch-based tag scripts) can hit this — split into included files (`#include`) with `main()`/handler dispatching if a script is getting close.
- Functions must be declared (prototyped) before use, or defined earlier in the file / an included header — no automatic forward resolution across separate compilation units besides `#include`.
- Object references (`object`), effects (`effect`), item properties (`itemproperty`), talents, locations, etc. are opaque engine handles, not structs you can introspect directly — you get/set their properties via specific Get/Set functions, not field access.
- `OBJECT_INVALID` / `GetIsObjectValid()` checks matter — many engine functions return the invalid object sentinel rather than erroring, and using an invalid object silently no-ops rather than crashing.

## Entry points / how scripts get wired up

NWScript files don't get "called" by name from other scripts automatically — they're wired in as event handlers via:
- Module properties (e.g. `OnModuleLoad`, `OnPlayerChat`, `OnClientEnter`) — set in the toolset's Module Properties → Events tab, referencing a script's filename (no extension).
- Object properties (creatures, placeables, triggers, areas each have their own event slots, e.g. `OnHeartbeat`, `OnUsed`, `OnDeath`).
- Conversation (`.dlg`) node scripts, which use `int StartingConditional()` for conditions and `void main()` for actions — the same script file can define either depending on the entry point the conversation calls, but a given file is one or the other.
- Spell/item scripts follow the same `void main()` pattern, invoked by the engine when the spell/item event fires.

For multiplayer/persistent-world modules specifically, tag-based scripting is the common convention: a small number of central scripts read `GetTag()` of the relevant object and dispatch to per-tag logic in a big `switch`/`if` chain (or an include-file-per-tag pattern once things get large), rather than writing a unique script file per placeable/creature/item. This keeps event-slot references stable even as content is added, at the cost of larger central files (watch the 64KB limit above).

## Common patterns worth getting exactly right

- **Effects**: create with the relevant `Effect*()` constructor function, then apply with `ApplyEffectToObject(nDurationType, eEffect, oTarget[, fDuration])` — `DURATION_TYPE_INSTANT`, `DURATION_TYPE_TEMPORARY`, or `DURATION_TYPE_PERMANENT`. Forgetting to apply a constructed effect is a common no-op bug.
- **Delays**: `DelayCommand(fSeconds, ActionOrFunctionCall())` and `AssignCommand(oTarget, ActionCall())` are how you schedule actions on an object or run an action as if a different object performed it — not real threads/callbacks, just deferred single calls.
- **Local variables**: `GetLocalInt/String/Object/Float` + `SetLocal*` on objects are the closest thing to per-object persistent state during a running server; there are no static/global variables that survive module save/load reliably without using a database or the object-local-variable system (or a persistent-storage solution like SQL if the module uses one).

## Compiling / verifying

**Prefer `nwn_script_comp`** from neverwinter.nim (https://github.com/niv/neverwinter.nim) for command-line compilation — it uses the same open-source compiler library as the official `nwnsc` binary, but ships cross-platform alongside the rest of that project's CLI tooling (2DA/ERF/GFF conversion, resource extraction, etc.), which makes it the more consistent choice when an agent is driving the whole workflow. `nwnsc` (Beamdog's own binary) and the toolset's in-app Build are equally valid fallbacks, e.g. if the project's existing Nasher config already points at one of them — don't fight an established build setup, but default to `nwn_script_comp` when setting one up fresh.

Compiling is how you catch syntax/type errors before considering a script done. A script that "looks right" but references a function with a wrong signature can still fail to compile with a possibly-confusing error pointing at the wrong argument — cross-check against the Lexicon page whenever a compile error is unclear. `nwn_asm` (also from neverwinter.nim) can inspect compiled bytecode directly if something needs debugging at that level.

## Reference files in this skill

- `reference/function-categories.md` — the full list of NWN Lexicon's function category pages, for browsing by topic instead of guessing exact names.

## Related skill

- `nwn-custom-content` covers the broader neverwinter.nim CLI toolchain (`reference/neverwinter-nim-cli.md`) for everything besides script compilation — 2DA edits, hakpacks, resource extraction.
