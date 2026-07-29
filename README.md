# nwn-claude-skills

Backup and cross-machine distribution for the Claude Code skills used on NWN:EE module projects.

## Contents

- `skills/nwn-custom-content/` — 2DA edits, hakpacks, placeables/items/creatures, neverwinter.nim CLI reference
- `skills/nwn-nwscript-api/` — NWScript language notes + NWN Lexicon navigation

## Install on a machine

```
git clone <your-remote-url> ~/dev/nwn-claude-skills   # or wherever you keep repos
cd ~/dev/nwn-claude-skills
./install.sh
```

This symlinks each skill folder into `~/.claude/skills/`, so Claude Code — any editor, any project, on that machine — picks them up automatically. Use `./install.sh --copy` instead if you'd rather have independent copies per machine (e.g. planning to fork one machine's version).

## Updating

Edit the skill files in this repo (directly, or by asking Claude to), then:

```
git add -A && git commit -m "update skills"
git push
```

On every other machine where you ran `install.sh` in symlink mode:

```
git pull
```

The update takes effect immediately — no need to re-run `install.sh` unless a *new* skill folder was added to the repo.

## Project-scoped instead of global

To scope a skill to a single repo instead of installing it globally, copy (don't symlink) the relevant `skills/<name>/` folder into that repo's own `.claude/skills/<name>/`.

## Also available in Cowork

These same two skills are additionally saved directly to this Anthropic account's Cowork skill library (not file-based — no sync step needed there). This repo is specifically for Claude Code CLI sessions across machines/editors, where skills are read from the local filesystem rather than the account.

## First-time setup (push this to your own remote)

This repo starts with one local commit but no remote. Create an empty repo on GitHub/GitLab/etc. (don't initialize it with a README), then:

```
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```
