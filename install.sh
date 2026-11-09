#!/usr/bin/env bash
# Install the skill into the agents on this machine.
# Usage: ./install.sh [antigravity|claude|agents|all]
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
src="$here/skills/mega-ui-ux"
target="${1:-antigravity}"

dest_for() {
  case "$1" in
    antigravity) echo "$HOME/.gemini/config/skills/mega-ui-ux" ;;
    claude)      echo "$HOME/.claude/skills/mega-ui-ux" ;;
    agents)      echo "$HOME/.agents/skills/mega-ui-ux" ;;
    *) echo "unknown target: $1" >&2; exit 1 ;;
  esac
}

if [ "$target" = "all" ]; then targets="antigravity claude agents"; else targets="$target"; fi
for t in $targets; do
  d="$(dest_for "$t")"
  rm -rf "$d"; mkdir -p "$(dirname "$d")"; cp -R "$src" "$d"
  echo "Installed to $d"
done
