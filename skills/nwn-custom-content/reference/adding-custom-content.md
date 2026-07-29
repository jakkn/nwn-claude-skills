# Introduction to Adding Custom Content to a Module

Source: https://nwn.wiki/spaces/NWN1/pages/53670537/Introduction+to+Adding+Custom+Content+to+a+Module

## What can be added

A module's tilesets, creatures, placeables, sounds, music, VFX, classes, spells, and feats can all be replaced, tweaked, or extended. Doing so is two steps:

1. Update the relevant 2DA file(s).
2. Add the 2DA(s) and associated files (models, textures, etc.) to a hakpack.

Curate what you add — keep haks lean. Large all-in-one content packs (e.g. CEP) are easy to add but very hard to edit or remove later since they modify many base 2DAs.

## Basics

- Filenames the game loads: max 16 characters, lowercase preferred (OS compatibility, avoids duplicate-name collisions in a hak).
- Hakpacks: max 2GB each, can hold millions of files.
- Module content (scripts, blueprints, areas) no longer needs to go in a hak — modules can hold millions of resources directly.
- Only one TLK file per module; multiple custom-content sources needing their own TLK must be merged into one.

## Worked example: adding a new placeable (a statue)

1. **Get a clean base 2DA.** Use `nwn_resman_extract` from neverwinter.nim (https://github.com/niv/neverwinter.nim — see `neverwinter-nim-cli.md`) to pull the current `placeables.2da` straight out of the game's resource data — don't hand-write from scratch, and this also lets you find/edit existing models later. (The Windows-only `nwnexplorer` GUI does the same thing if you specifically need to browse visually, but the CLI is preferred for anything scriptable.)
2. **Get the model files.** For a placeable: `<name>.tga` (texture), `<name>100.mdl` (model), `<name>100.pwk` (walkmesh).
3. **Edit the 2DA.** Either edit the plain-text `.2da` directly (use an editor that preserves line endings — Notepad++ is fine on Windows), or convert to CSV with `nwn_twoda -i placeables.2da -o placeables.csv` for easier bulk/scripted edits, then convert back with `nwn_twoda -i placeables.csv -o placeables.2da`. Add a new row on an ID well past the reserved/base-game range (example used line `1000`). Relevant columns for a placeable:
   - `ID` — leftmost numbered column
   - `Label` — toolset display name (convention: prefix with something like `CC:` to mark it as custom content)
   - `ModelName` — the `.mdl` filename without extension
   - `SoundAppType` — index into `placeableobjsnds.2da` for the impact/interaction sound
   - `ShadowSize` — e.g. `1` for a medium shadow in fast-shadow mode
   - `BodyBag` — `0` for none
   - `Static` — `1` if it should be usable as a non-selectable static/terrain-like object
   - All other columns: leave as `****`
   - Columns are whitespace-separated (any width), one whitespace between them; quote values containing spaces (e.g. the Label).
4. **Test without a hak first.** Drop the edited 2DA and model files into `Documents/Neverwinter Nights/override`. This overrides the base game 2DA for fast iteration.
5. In the toolset, open/create a module, go to the Placeable palette tab → Custom, create a blueprint, and set **Appearance Type** to your new row. If it doesn't appear, the 2DA didn't load — recheck the override folder and the 2DA syntax.
6. Place it in an area, save, and press F9 to test in-game.
7. Once confirmed, move the files into a hakpack instead of the override folder (see the hakpacks reference) — override is for testing, not distribution.

## Gotchas

- Changing a 2DA row's ID *after* placing blueprints/instances that reference it breaks those instances (they silently stop loading the appearance). Treat an ID as fixed once anything depends on it.
- Removing files from override breaks anything referencing them the same way removing them from a hak would — override is not more "safe," just faster to iterate on.

## Other content types (same 2DA-edit pattern)

| Content type | Target 2DA | Notes |
|---|---|---|
| Creature appearances | `appearance.2da` | Many columns; most creature appearances ship with an example row to copy |
| Item appearances | (auto) | Usually just needs correctly named/numbered files in a contiguous block |
| New item base types | `baseitems.2da` | Will likely need new TLK entries |
| Portraits | `portraits.2da` | |
| Load screens | `loadscreens.2da` | |
| Soundsets | `soundset.2da` | |
| Visual effects | `visualeffects.2da` | |
| Music soundtracks | `ambientmusic.2da` | |
| Ambient background sound | `ambientsound.2da` | |
| Tilesets | own 2DA + `.SET` file | May need a `doortypes.2da` entry |
| Races / classes / feats / domains / spells / skills | multiple 2DAs + heavy TLK cross-referencing | High complexity — needs a dedicated tutorial per system, IDs are hard to change later |

Always: save often, keep backups of prior hak/module versions, test after every change.

See `neverwinter-nim-cli.md` for the full cross-platform CLI toolchain (extraction, 2DA/GFF/TLK conversion, hak packing) to use instead of the Windows-only GUI tools referenced in the original tutorial.
