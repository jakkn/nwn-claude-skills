# nwn-claude-skills

Claude Code skills for Neverwinter Nights: Enhanced Edition (NWN:EE) module development.

## Contents

- `skills/nwn-custom-content/` — 2DA edits, hakpacks, placeables/items/creatures, and the neverwinter.nim CLI reference
- `skills/nwn-nwscript-api/` — NWScript language notes and NWN Lexicon navigation
- `skills/anvil-api/` — NWN.Anvil (the C# framework for .NET-enabled servers): a generated index of the whole public API, the event catalogue, bundled services, working patterns, and native function hooking

## Regenerating the Anvil API index

`skills/anvil-api/reference/api-index.md` is generated from Anvil's source and records the
version it was built from in its header. After upgrading the `NWN.Anvil` package, refresh it
against a matching Anvil checkout and commit the result:

```
python3 skills/anvil-api/scripts/generate_api_index.py /path/to/Anvil
```

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
