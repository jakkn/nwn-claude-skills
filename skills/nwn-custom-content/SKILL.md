---
name: nwn-custom-content
description: Use when adding custom content to a Neverwinter Nights: Enhanced Edition (NWN:EE) multiplayer module — new placeables, items, creatures, appearances, portraits, sounds, hakpacks, 2DA edits, or TLK entries. Not for writing NWScript code (see the nwn-nwscript-api skill) or for general game-modding questions unrelated to NWN.
---

# NWN:EE Custom Content

This skill packages the workflow for adding non-script custom content to an NWN:EE module: 2DA edits, hakpacks, new appearances/items/placeables, and where to find the authoritative tutorials on nwn.wiki.

**This skill is a navigation aid, not an authority.** nwn.wiki is canonical. The notes here are a compressed snapshot (last reviewed 2026-08) that exists to get you to the right page and to warn you off the known traps — it is *not* complete coverage of any topic it touches, and a section that reads as authoritative may still be out of date. Where this skill and the wiki disagree, the wiki wins.

Primary sources:
- Tutorial index: https://nwn.wiki/spaces/NWN1/pages/14618048/Tutorials
- 2DA file reference: https://nwn.wiki/spaces/NWN1/pages/38174875/2da+Files (individual files like placeables.2da, baseitems.2da etc. each have their own nwn.wiki page — search nwn.wiki for the filename)
- Models and model formats: https://nwn.wiki/display/NWN1/Models · https://nwn.wiki/spaces/NWN1/pages/12027273/MDL+ASCII

Reference files in `reference/`. Each one opens with its own explicit "not covered here" list — **read that list before starting work in that area**, since it names the gaps you can't otherwise infer from a document that looks finished:
- `reference/adding-custom-content.md` — 2DA edits, adding a new placeable end to end
- `reference/hakpacks.md` — packaging content into a .hak file and attaching it to a module
- `reference/tutorial-index.md` — full categorized list of nwn.wiki tutorial pages (advanced, modeling, shaders, tools, etc.) with URLs
- `reference/neverwinter-nim-cli.md` — the command-line toolchain to use for all of this
- `reference/spells.md` — custom spells: spells.2da columns, the UserType mechanics fork, targeting/projectile/casting-economy variations, custom spellcasting classes via classes.2da, and ways to grant a spell outside the class system
- `reference/vfx.md` — custom VFX: visualeffects.2da + progfx.2da (all 13 types), what progfx can and cannot recolor, recoloring an existing particle VFX via ASCII model edits, node-attached accessories (progfx Type 12), and the blend/alpha trap. Uses **[wiki]** / **[tested]** / **[unverified]** markers to separate documented behaviour from hands-on findings.

## Tooling

**Default toolchain: the neverwinter.nim CLI (https://github.com/niv/neverwinter.nim).** `nwn_erf`, `nwn_twoda`, `nwn_resman_extract` and friends are cross-platform, scriptable, and need no GUI session. Full command reference in `reference/neverwinter-nim-cli.md`. Everything in the core workflow below is doable with it.

### Tool-resolution rule (read this before naming any other tool)

**Never recommend, invoke, or plan around a tool you recalled from memory. Every tool named outside the neverwinter.nim set must come from a page fetched during this session.**

This is not a style preference — it is the same anti-hallucination rule the `nwn-nwscript-api` skill applies to function signatures, extended to tooling, and for the same reason. NWN tooling has twenty-plus years of accumulated forum history, so the tool a model recalls most readily is reliably *the oldest one*, not the current one. Several long-established NWN tools are now only partially updated for EE and will silently drop EE-specific data. A confident recollection here is a strong signal you are about to name something obsolete.

When the default toolchain can't do something:

1. Fetch the relevant nwn.wiki page for that task class (see the tool-and-format index in `reference/tutorial-index.md`) and use whatever it currently recommends.
2. Prefer a CLI-capable option. An agent cannot run a GUI, and cannot run the game client.
3. If nothing usable is available in this environment, **stop and tell the user what's needed** — hand back the part you can do and name the missing capability. Do not improvise an installation, a platform workaround, or a substitute check.

Do not document environment setup, install locations, or filesystem paths in this skill. It is read by people on different operating systems with different install layouts; a recipe that works on one machine is a trap on the others.

### Known capability gaps in the default toolchain

- **No model compiler or decompiler.** Stock `.mdl` files ship compiled. Getting to editable ASCII needs an external decompiler resolved per the rule above. Note the engine loads ASCII `.mdl` directly, so *producing* content never requires a compiler — see `reference/vfx.md`.
- **No running game client.** Anything gated on launching NWN — in-game console commands, model hot-reload, visual confirmation — is a user handoff, not an agent step.

## Core workflow

1. **Identify the 2DA(s) that control the content type.** See the table below. Get a clean copy of the base game's 2DA with `nwn_resman_extract` (pointed at the game's key/install files) rather than guessing column meanings — see `reference/neverwinter-nim-cli.md`.
2. **Edit the 2DA.** Either edit the `.2da` text directly, or round-trip it to CSV with `nwn_twoda` for easier scripted/spreadsheet editing, then convert back. Add a new row using an ID number well outside the base game's reserved range (e.g. start custom rows at 1000+). Only fill in the columns that matter for that content type; leave the rest as `****`. Columns are whitespace-separated; quote any value containing a space.
3. **Test locally** by dropping the edited 2DA + associated files (models, textures, etc.) into the user's override folder (`Documents/Neverwinter Nights/override`) before packaging anything — this is the fast iteration loop.
4. **Package into a hakpack** once it works, using `nwn_erf -c` (see `reference/neverwinter-nim-cli.md`) or a build tool like Nasher (https://github.com/squattingmonk/nasher) for automated/CI builds. Remove the override copy once the hak is attached and confirmed working.
5. **Attach the hak** to the module via Module Properties → Custom Content, and rebuild.

## Hard rules (get these wrong and things silently break)

- Filenames the game loads: max 16 characters, lowercase preferred (case-sensitivity issues across OSes, and prevents accidental duplicate-name collisions in a hak).
- Only **one** TLK file per module. If merging content from multiple sources that each want their own TLK, the strings must be merged into a single custom TLK.
- Hakpacks: max 2GB each, but a module can reference multiple haks; load order matters (top of the list = highest precedence when two haks contain a file with the same name).
- **Don't put module-level content in hakpacks**: scripts, dialogs (.dlg), areas, and blueprints belong in the module itself, not the hak — haks are for models, textures, 2DA files, sounds, music, and tileset files. Modules can hold millions of resources now, so there's no size reason to hak scripts/blueprints anymore.
- Changing a 2DA row's ID after you've already placed instances that reference it breaks those instances. Treat the row ID as fixed once anything in the module depends on it.
- Removing a hakpack later is risky — anything referencing content from it will break with vague errors. Prefer adding curated, minimal haks over huge all-in-one packs (like CEP) that are hard to remove or diff against later. Nasher can decompile a module to JSON to help find dangling references before removing content.

## Content type → 2DA quick reference

| Content type | 2DA file | Notes |
|---|---|---|
| Placeables | `placeables.2da` | Needs model + texture + walkmesh (.pwk); simplest custom content to start with |
| Creature appearances | `appearance.2da` | Many more columns; copy an existing similar row as a starting template |
| Item base types | `baseitems.2da` | Usually needs new TLK string entries too |
| Item appearances | Often auto-detected | Just needs correctly-named/numbered model files in a contiguous block |
| Portraits | `portraits.2da` | — |
| Load screens | `loadscreens.2da` | — |
| Soundsets | `soundset.2da` | — |
| Visual effects | `visualeffects.2da` + `progfx.2da` | See `reference/vfx.md` — color, node attachment, and scale/position are mostly progfx.2da params or script-time `EffectVisualEffect()` args, not model edits |
| Music soundtracks | `ambientmusic.2da` | — |
| Ambient background sound | `ambientsound.2da` | — |
| Tilesets | Own `.2da` + `.SET` file | Self-contained; may need a `doortypes.2da` entry |
| Spells | `spells.2da` | See `reference/spells.md` — covers the row itself, the UserType mechanics fork, and custom spellcasting classes |
| Races / classes / feats / domains / skills | Multiple 2DAs + heavy TLK cross-referencing | Much higher complexity — treat as its own research task and fetch the specific nwn.wiki page for that system before starting |

## Related skills

- `nwn-nwscript-api` — writing the `.nss` scripts that drive the content added here.
- `anvil-api` — NWN.Anvil, the C# framework used on .NET-enabled servers. Anvil reads 2DAs at runtime via `NwGameTables` and can write resources at runtime via its `ResourceManager`, so a custom 2DA authored with this skill is often consumed from C# rather than NWScript.

## Fetch before acting — named triggers

"When this isn't enough" is not a judgement you can make from the inside; a compressed summary looks complete precisely where it's thinnest. So these are stated as triggers rather than left to discretion. **Fetch the relevant page before writing anything if the task involves:**

- **A content type with no reference file above** — custom races, classes, feats, domains, item properties, poisons, weather, tilesets. Start from `reference/tutorial-index.md` and fetch the specific page.
- **Any 2DA column not documented above.** Column semantics are easy to get subtly wrong and the failure mode is a silent crash or content that won't load, not an error message. Fetch that 2DA's own wiki page.
- **Any tool outside the neverwinter.nim set** — see the tool-resolution rule.
- **Binary model manipulation**, or any `.mdl` work beyond editing existing ASCII.
- **Anything you'd be relying on recall for.** If you can't point at where a claim came from, treat it as unverified.

## Reporting honestly

Most failure modes in NWN custom content are silent — content that doesn't load, a VFX that renders nothing, a spell that skips a mechanic. Almost none of it can be verified without launching the game, which an agent cannot do.

Do not manufacture a substitute for verification, and do not describe unverified work as working. Say what was changed, name the specific things most likely to be wrong, and hand over test steps for the user to run. If a task needed a capability that wasn't available, report that rather than routing around it — a plainly-flagged gap is far cheaper for the user than a confident wrong answer.
