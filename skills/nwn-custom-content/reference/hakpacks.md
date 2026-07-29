# Introduction to Hakpacks

Source: https://nwn.wiki/spaces/NWN1/pages/60981970/Introduction+to+Hakpacks

Follows on from `adding-custom-content.md` — understand the 2DA/file model before this.

## Three ways to load custom content into a module

1. **Override folder** (`Documents/Neverwinter Nights/override`) — highest priority, good for fast local testing, not for distribution.
2. **Development folder** — similar, for iterating on textures/models/scripts.
3. **Hakpacks (`.hak`)** — how custom content is actually shipped to players, or fed into nwsync for server distribution. This file covers hakpacks.

## What belongs in a hakpack

Models, textures, 2DA files, sounds, music, tileset files.

**Do not** put scripts, dialogs, areas, or blueprints in a hakpack — those belong in the module itself (haks load at higher priority than module content, which causes confusing conflicts) and modules can already store huge numbers of these directly.

## Limits

- 2GB max per hak file (a module can have multiple haks attached).
- Effectively no meaningful file-count limit anymore (was once a concern, now in the millions).
- If working with very large numbers of small files, consider Nasher (https://github.com/squattingmonk/nasher) or similar tooling instead of manual hak editing.

## Creating a hak

**Preferred: `nwn_erf` from neverwinter.nim** (https://github.com/niv/neverwinter.nim — cross-platform, scriptable, no GUI/WINE needed; see `neverwinter-nim-cli.md` for full syntax):

1. Gather the files to add outside the game's own folders in one directory. **All filenames lowercase** — mixed case risks accidentally adding two "different" files that are really the same resource.
2. Build the hak: `nwn_erf -c -f statue_torm.hak <directory-or-file-list>`. `.hak` is auto-detected as the ERF type from the filename extension.
3. Hakpacks are stored uncompressed; zip (7-Zip, or plain `zip`/`gzip` on Linux) before distributing.

**GUI alternative:** `nwhak.exe` from `<install>/Neverwinter Nights/bin/win32` (runs under WINE on non-Windows) does the same thing via drag-and-drop / Resource → Add, and must be saved with a filename ≤16 characters (excluding extension). Close it after saving — it locks the file open while running. Use this only if a GUI is specifically wanted; `nwn_erf` is otherwise the better default for agent-driven or CI workflows.

## Attaching a hak to a module

1. In the toolset: Edit → Module Properties → Custom Content tab.
2. Add the hak via the dropdown (if you have many haks installed, temporarily hiding unrelated ones can make the dropdown usable).
3. Save and rebuild the module when prompted; the build should show no errors.
4. Remove the override-folder test copies once the hak version is confirmed working — otherwise you can't tell which one is actually loading.

## Multiple hakpacks / load order

- Haks load top-to-bottom in the module's list; **higher in the list = higher precedence** for same-named files.
- 2DA files are the most common source of unintentional overrides — if two haks each ship a `placeables.2da`, only the top one's rows apply, meaning the other hak's placeable rows silently vanish from the toolset/game.
- The toolset's **Check for Conflicts** button lists both cross-hak file collisions and base-game overrides. Since intentionally overriding base 2DAs is common, focus on the "conflicts" panel (same file present in more than one hak) rather than the "overrides base game" warnings.

## Removing a hakpack (risky — read fully before doing this)

1. Back up the module and all haks first (zip together).
2. Remove every reference to that hak's content from the module (blueprints, placed instances, etc.). Decompiling the module to JSON with Nasher makes searching for references practical. The in-game "log missing resources" option can help but is noisy even on a clean base install.
3. Build and save the module — check for new errors, make a second save as a checkpoint.
4. Remove the hak in the Custom Content panel; build again (this may surface more dead references, but isn't exhaustive).
5. Save and test thoroughly.

This is why large all-in-one packs like CEP are usually a one-way door — plan for that before adding one.

## Editing an existing hak later

- **Preferred (CLI):** unpack with `nwn_erf -x -f old.hak` into a scratch directory, edit/add files there, then rebuild cleanly with `nwn_erf -c -f new.hak <directory>`. Since this always rebuilds from a full unpack, there's no risk of a silent partial overwrite — it's inherently safer than editing in place, and scriptable/repeatable in CI.
- **Riskier (GUI):** open the existing hak in `nwhak.exe` and drag new files on top — any name clash is overwritten irrevocably.

## Merging hakpacks

- **Preferred (CLI):** `nwn_erf -x -f a.hak` and `nwn_erf -x -f b.hak` into the same (or then-combined) directory, resolve any filename clashes by hand, then `nwn_erf -c -f merged.hak <directory>`.
- **Riskier (GUI):** `nwhak.exe` File → Merge — clashing files are overwritten irrevocably.
- 2DA files almost always need manual merging line-by-line when combining haks that both touch the same 2DA — round-trip through `nwn_twoda` to CSV if that makes the diff/merge easier to do by hand or with a script.

Always back up module + haks externally (cloud storage at minimum; source control / Nasher for anything beyond a small project) before hak surgery.

See `neverwinter-nim-cli.md` for the full `nwn_erf` command reference.
