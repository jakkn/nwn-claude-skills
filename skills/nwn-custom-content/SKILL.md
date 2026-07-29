---
name: nwn-custom-content
description: Use when adding custom content to a Neverwinter Nights: Enhanced Edition (NWN:EE) multiplayer module — new placeables, items, creatures, appearances, portraits, sounds, hakpacks, 2DA edits, or TLK entries. Not for writing NWScript code (see the nwn-nwscript-api skill) or for general game-modding questions unrelated to NWN.
---

# NWN:EE Custom Content

This skill packages the workflow for adding non-script custom content to an NWN:EE module: 2DA edits, hakpacks, new appearances/items/placeables, and where to find the authoritative tutorials on nwn.wiki.

Primary sources (fetch live when the cached notes below aren't enough):
- Tutorial index: https://nwn.wiki/spaces/NWN1/pages/14618048/Tutorials
- 2DA file reference: https://nwn.wiki/spaces/NWN1/pages/38174875/2da+Files (individual files like placeables.2da, baseitems.2da etc. each have their own nwn.wiki page — search nwn.wiki for the filename)

Cached copies of the two core "how do I even start" tutorials are in `reference/`:
- `reference/adding-custom-content.md` — 2DA edits, adding a new placeable end to end
- `reference/hakpacks.md` — packaging content into a .hak file and attaching it to a module
- `reference/tutorial-index.md` — full categorized list of nwn.wiki tutorial pages (advanced, modeling, shaders, tools, etc.) with URLs
- `reference/neverwinter-nim-cli.md` — the command-line toolchain to use for all of this

## Tooling preference

**Prefer the neverwinter.nim CLI tools (https://github.com/niv/neverwinter.nim) over GUI/Windows-only tools whenever a task can be done from the command line.** `nwn_erf`, `nwn_twoda`, `nwn_resman_extract`, etc. are cross-platform, scriptable, and don't require WINE or a GUI session — a much better fit for an agent than driving `nwnexplorer.exe` or `nwhak.exe`. Full command reference in `reference/neverwinter-nim-cli.md`. Fall back to the GUI tools (nwnexplorer, nwhak.exe via the toolset/WINE) only if the CLI genuinely can't do something (e.g. visual model preview) or the user asks for the GUI workflow specifically.

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
| Visual effects | `visualeffects.2da` | — |
| Music soundtracks | `ambientmusic.2da` | — |
| Ambient background sound | `ambientsound.2da` | — |
| Tilesets | Own `.2da` + `.SET` file | Self-contained; may need a `doortypes.2da` entry |
| Races / classes / feats / domains / spells / skills | Multiple 2DAs + heavy TLK cross-referencing | Much higher complexity — treat as its own research task and fetch the specific nwn.wiki page for that system before starting |

## When this isn't enough

If the task involves a content type not covered in the cached reference files (e.g. custom races, item properties, poisons, weather types), fetch the matching page from the tutorial index (`reference/tutorial-index.md` has the categorized link list) before improvising — 2DA column semantics are easy to get subtly wrong and the failure mode is often a silent crash or content that doesn't load rather than a clear error.
