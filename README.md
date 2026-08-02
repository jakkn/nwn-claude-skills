# nwn-claude-skills

Claude Code skills for Neverwinter Nights: Enhanced Edition (NWN:EE) module development.

## Contents

- `skills/nwn-custom-content/` — 2DA edits, hakpacks, placeables/items/creatures, and the neverwinter.nim CLI reference
- `skills/nwn-nwscript-api/` — NWScript language notes and NWN Lexicon navigation
- `skills/anvil-api/` — NWN.Anvil (the C# framework for .NET-enabled servers): a generated index of the whole public API, the event catalogue, bundled services, working patterns, and native function hooking
- `skills/nwn-toolbox-api/` — NWN.Toolbox consumed as a package from your own Anvil plugin: a generated index of its public API, the NUI window view/controller pattern, chat commands, permissions, and the container extension points

## Regenerating the API indexes

`skills/anvil-api/reference/api-index.md` and `skills/nwn-toolbox-api/reference/api-index.md`
are generated from their respective sources and record the version they were built from in
their headers. After upgrading either package, refresh the index against a matching checkout
and commit the result:

```
python3 skills/anvil-api/scripts/generate_api_index.py /path/to/Anvil
python3 skills/nwn-toolbox-api/scripts/generate_api_index.py /path/to/NWN.Toolbox
```

The Toolbox index lists **public** types only — internal types are unreachable from a
consuming assembly, so their absence from the index is the answer, not a gap in it.

## Installation

```
git clone <repo-url> nwn-claude-skills
cd nwn-claude-skills
./install.sh
```

This symlinks each skill folder into `~/.claude/skills/`, so Claude Code picks them up automatically across every project and editor. Use `./install.sh --copy` instead for an independent, unlinked copy.

To scope a skill to a single project instead of installing it globally, copy (don't symlink) the relevant `skills/<name>/` folder into that project's own `.claude/skills/<name>/`.

## Updating

Edit or add skill files, then commit and push as usual:

```
git add -A && git commit -m "update skills"
git push
```

Anywhere the repo was installed in symlink mode, a `git pull` picks up the change immediately — no need to re-run `install.sh` unless a new skill folder was added.

## Adding a new skill

Create `skills/<new-skill-name>/SKILL.md` (plus a `reference/` folder if needed) and commit. `install.sh` picks up every folder under `skills/` automatically, no changes to the script required.

## License

Apache 2.0 — see [LICENSE](LICENSE).
