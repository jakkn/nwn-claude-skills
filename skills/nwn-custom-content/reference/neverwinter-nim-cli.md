# neverwinter.nim CLI toolchain

Source: https://github.com/niv/neverwinter.nim (MIT licensed, binary releases on the GitHub Releases page — no separate runtime install needed).

**Default to these tools over GUI/Windows-only equivalents** (`nwnexplorer.exe`, `nwhak.exe`) whenever the task can be scripted — they're cross-platform (no WINE), work over stdin/stdout, and are far easier for an agent to drive reliably and repeatably (e.g. rebuild-from-scratch instead of drag-and-drop edits).

All tools support `--help` for full usage and `--verbose`/`--quiet` for logging. **Confirm exact flags with `--help` before running an unfamiliar command** — don't guess flag names, especially the resman-selection flags (which key/hak/module files a tool reads from), since these can change between releases.

## Resource extraction / inspection (`resman` tools)

These operate on a "resman view" — the combined set of resources visible from whatever key files, haks, and module you point them at (base game data, a specific hak, a module, etc.) rather than one file format at a time.

- `nwn_resman_stats` — statistics on what's in a resman view.
- `nwn_resman_grep` — search a resman view for data.
- `nwn_resman_extract` — pull matching files out into a directory. Match by exact name (`<file>...`), `--pattern SUBSTRING`, `--binary SUBSTRING`, or `--all`; output directory via `-d` (default `.`).
  Example: `nwn_resman_extract --pattern placeables.2da -d ./work` (point it at the game's key files per `--help`, e.g. a `--key`/`--root`-style flag; check `--help` for the exact current flag name).
- `nwn_resman_cat` — pull file(s) from a resman view straight to stdout (good for quick inspection/piping).
- `nwn_resman_diff` — diff two resman views (e.g. checking language/localization differences).
- `nwn_resman_pkgsrv` — repackage a resman view for container/docker-style deployment.
- `nwn_key_pack` / `nwn_key_unpack` — un/pack a `.key` keyfile into/from a directory structure.
- `nwn_key_shadows` — report on file shadowing across a list of key files (i.e. which file wins when the same name appears in multiple keys).
- `nwn_key_transparent` — report on file duplication across a list of key files.

## Format conversion

- `nwn_twoda` — convert 2DA files to/from CSV (and other supported formats). `-i INPUT -o OUTPUT` with `-l`/`-k` to force input/output format if autodetection is wrong; `--minify` for compact 2DA output; `--write-id-column` to include row IDs in CSV export (discarded again on re-import — 2DA row order determines ID, not the column). This is the main tool for scripted or bulk 2DA edits, and for making a 2DA diffable/reviewable as CSV.
  Example: `nwn_twoda -i placeables.2da -o placeables.csv` then edit, then `nwn_twoda -i placeables.csv -o placeables.2da`.
- `nwn_gff` — convert GFF-family files (blueprints `.utc`/`.uti`/`.utp`/etc., modules' `.ifo`, and others) to/from readable formats (e.g. JSON), and extract/embed SQLite data blobs. Useful for inspecting or bulk-editing blueprints without opening the toolset.
- `nwn_tlk` — convert TLK string tables to/from other formats — useful when merging TLK entries from multiple custom-content sources (remember: only one TLK per module, so merges have to happen here).
- `nwn_erf` — un/pack ERF-family files, which includes `.hak`, `.mod`, `.erf`, `.nwm`. Core hakpack tool — see usage below.
- `nwn_erf_tlkify` — refactor hardcoded strings inside an ERF into an existing or new TLK (useful when converting content that has inline strings into properly localizable TLK references).
- `nwn_ssf` — convert SSF (soundset) files to/from CSV.
- `nwn_compressedbuf` — de/compress `NWCompressedBuf` payloads (used internally by some GFF fields).
- `nwn_net` — network helpers, e.g. querying live NWN servers.

### `nwn_erf` usage (the hakpack tool)

```
nwn_erf -c -f out.hak <file-or-directory>...   # create/pack — auto-detects ERF type (hak/mod/erf) from the -f extension
nwn_erf -x -f in.hak [<file>...]               # extract all, or only the named files, into the current directory
nwn_erf -t -f in.hak                           # list contents
```
Add `-v` to echo filenames as they're processed. `-r N` controls how many directory levels are recursed into when packing from a directory (default 1 — bump this if your source folder has subdirectories). Because `-x` then `-c` fully rebuilds a hak from a clean directory, this create/extract round-trip is the safe way to edit or merge haks — no in-place overwrite risk the way dragging files onto `nwhak.exe` has.

## Script compiler

- `nwn_script_comp` — NWScript compiler using the same open-source compiler library the official `nwnsc` binary uses; prefer this for CLI/CI workflows (e.g. driven by Nasher) since it ships as part of the same cross-platform toolchain as the rest of these tools.
- `nwn_asm` — utility for working with compiled NWScript bytecode directly.

## NWSync (server-side content distribution)

- `nwn_nwsync_write` — generate a serverside NWSync manifest from a set of haks/content.
- `nwn_nwsync_prune` — trim a serverside NWSync repository of data no longer referenced by any manifest.
- `nwn_nwsync_print` — print manifest contents in a human-readable form.
- `nwn_nwsync_fetch` — sync a manifest server-to-server (uses `aria2c`).

These are the official tools for maintaining a NWSync repo (relevant if the module is a persistent-world server distributing haks to players over NWSync instead of requiring a manual download).
