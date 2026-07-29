#!/usr/bin/env bash
# Installs/updates the NWN:EE Claude Code skills from this repo into
# the global Claude Code skills directory (~/.claude/skills), via symlinks.
#
# Usage:
#   ./install.sh            # symlink (recommended — stays in sync with `git pull`)
#   ./install.sh --copy     # copy instead of symlink (independent per-machine copy)

set -euo pipefail
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${HOME}/.claude/skills"
MODE="${1:-}"

mkdir -p "$TARGET_DIR"

for skill in "$REPO_DIR"/skills/*/; do
  name="$(basename "$skill")"
  dest="$TARGET_DIR/$name"

  if [ -e "$dest" ] || [ -L "$dest" ]; then
    echo "Removing existing $dest"
    rm -rf "$dest"
  fi

  if [ "$MODE" = "--copy" ]; then
    cp -r "$skill" "$dest"
    echo "Copied $name -> $dest"
  else
    ln -s "$skill" "$dest"
    echo "Symlinked $name -> $dest"
  fi
done

echo "Done. Run 'git pull' in this repo later to update all machines that symlinked it."
