#!/bin/bash
# ─────────────────────────────────────────────────
# esc-skills installer & updater
# Install or update all skills in the current project or globally for Codex
#
# Usage:
#   curl -sL https://raw.githubusercontent.com/guilhermemarketing/esc-skills/main/install.sh | bash
#   bash install.sh              # Install in .agent/skills/ (first time)
#   bash install.sh update       # Update existing skills in .agent/skills/
#   bash install.sh check        # Check for updates (no changes)
#   bash install.sh --codex      # Install globally for Codex app (~/.codex/skills/)
#   bash install.sh --codex update  # Update Codex skills (per-skill rsync --delete)
#   bash install.sh --codex check   # Check for Codex skill updates
# ─────────────────────────────────────────────────

set -e

REPO="https://github.com/guilhermemarketing/esc-skills.git"
RAW_BASE="https://raw.githubusercontent.com/guilhermemarketing/esc-skills/main"
TMP_DIR="/tmp/esc-skills-$$"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# ─── Parse Arguments ─────────────────────────────────────────
CODEX_MODE=false
MODE="install"

for arg in "$@"; do
  case "$arg" in
    --codex) CODEX_MODE=true ;;
    install|update|check) MODE="$arg" ;;
  esac
done

# ─── Determine Skills Directory ──────────────────────────────
if [ "$CODEX_MODE" = true ]; then
  SKILLS_DIR="$HOME/.codex/skills"
elif [ -d ".cursor/skills" ]; then
  SKILLS_DIR=".cursor/skills"
elif [ -d ".agent/skills" ]; then
  SKILLS_DIR=".agent/skills"
else
  SKILLS_DIR=".agent/skills"
fi

echo ""
echo -e "${BOLD}🧠 esc-skills${NC} — AI Marketing Skills for Agents"
echo "──────────────────────────────────────────"
if [ "$CODEX_MODE" = true ]; then
  echo -e "🎯 Mode: ${CYAN}Codex (global)${NC}"
fi

# ─── Check Mode ──────────────────────────────────────────────

if [ "$MODE" = "check" ]; then
  echo -e "${CYAN}🔍 Checking for updates...${NC}"

  # Download remote manifest
  REMOTE_MANIFEST=$(curl -sL "$RAW_BASE/manifest.json" 2>/dev/null)
  if [ -z "$REMOTE_MANIFEST" ]; then
    echo -e "${RED}❌ Could not fetch remote manifest${NC}"
    exit 1
  fi

  # Find local manifest
  if [ "$CODEX_MODE" = true ]; then
    LOCAL_MANIFEST="$SKILLS_DIR/manifest.json"
  else
    LOCAL_MANIFEST="$SKILLS_DIR/../manifest.json"
  fi

  if [ ! -f "$LOCAL_MANIFEST" ]; then
    if [ -f "manifest.json" ]; then
      LOCAL_MANIFEST="manifest.json"
    else
      echo -e "${YELLOW}⚠️  No local manifest found. Run 'install' first.${NC}"
      exit 1
    fi
  fi

  # Compare versions using Python (available on most systems)
  python3 -c "
import json, sys

remote = json.loads('''$REMOTE_MANIFEST''')
local = json.load(open('$LOCAL_MANIFEST'))

outdated = []
new_skills = []

for name, info in remote['skills'].items():
    local_info = local.get('skills', {}).get(name)
    if not local_info:
        new_skills.append((name, info['version']))
    elif local_info['version'] != info['version']:
        outdated.append((name, local_info['version'], info['version']))

if not outdated and not new_skills:
    print('✅ All skills are up to date!')
    sys.exit(0)

if outdated:
    print(f'\n📦 {len(outdated)} skill(s) have updates:')
    for name, old_v, new_v in sorted(outdated):
        breaking = remote['skills'][name].get('breaking', False)
        flag = ' ⚠️  BREAKING' if breaking else ''
        print(f'  {name}: {old_v} → {new_v}{flag}')

if new_skills:
    print(f'\n🆕 {len(new_skills)} new skill(s) available:')
    for name, version in sorted(new_skills):
        print(f'  {name}: {version}')

print(f'\nRun \"bash install.sh update\" to update.')
" 2>/dev/null || echo -e "${RED}❌ Python3 required for version check${NC}"

  exit 0
fi

# ─── Install / Update Mode ───────────────────────────────────

echo -e "📁 Skills directory: ${CYAN}$SKILLS_DIR${NC}"
echo ""

# Clone repository
echo "📥 Downloading skills..."
git clone --depth 1 "$REPO" "$TMP_DIR" 2>/dev/null

INSTALLED=0
UPDATED=0
SKIPPED=0
NEW=0
BREAKING_LIST=""

if [ "$MODE" = "update" ] && [ -d "$SKILLS_DIR" ]; then
  echo -e "${CYAN}🔄 Update mode${NC} — comparing versions..."
  echo ""

  for skill in "$TMP_DIR"/skills/*/; do
    skill_name=$(basename "$skill")
    target="$SKILLS_DIR/$skill_name"

    if [ -d "$target" ]; then
      # Skill exists — check if SKILL.md changed
      if diff -q "$skill/SKILL.md" "$target/SKILL.md" > /dev/null 2>&1; then
        SKIPPED=$((SKIPPED + 1))
      else
        # Extract versions from YAML frontmatter
        OLD_VER=$(grep -m1 '^version:' "$target/SKILL.md" 2>/dev/null | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' || echo "?.?.?")
        NEW_VER=$(grep -m1 '^version:' "$skill/SKILL.md" 2>/dev/null | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' || echo "?.?.?")

        # Check for breaking change (major version bump)
        OLD_MAJOR=$(echo "$OLD_VER" | cut -d. -f1)
        NEW_MAJOR=$(echo "$NEW_VER" | cut -d. -f1)

        if [ "$OLD_MAJOR" != "$NEW_MAJOR" ] 2>/dev/null; then
          echo -e "  ${RED}⚠️  $skill_name: $OLD_VER → $NEW_VER (BREAKING)${NC}"
          BREAKING_LIST="$BREAKING_LIST\n    - $skill_name: $OLD_VER → $NEW_VER"
        else
          echo -e "  ${GREEN}↑${NC}  $skill_name: $OLD_VER → $NEW_VER"
        fi

        if [ "$CODEX_MODE" = true ]; then
          # Per-skill rsync with --delete to avoid 'references 2' etc.
          mkdir -p "$target"
          rsync -a --delete "$skill/" "$target/"
        else
          cp -r "$skill"/* "$target/"
        fi
        UPDATED=$((UPDATED + 1))
      fi
    else
      # New skill
      echo -e "  ${GREEN}+${NC}  $skill_name (new)"
      mkdir -p "$target"
      if [ "$CODEX_MODE" = true ]; then
        rsync -a --delete "$skill/" "$target/"
      else
        cp -r "$skill"/* "$target/"
      fi
      NEW=$((NEW + 1))
    fi
  done

  # Copy manifest
  if [ -f "$TMP_DIR/manifest.json" ]; then
    if [ "$CODEX_MODE" = true ]; then
      cp "$TMP_DIR/manifest.json" "$SKILLS_DIR/manifest.json"
    else
      cp "$TMP_DIR/manifest.json" "$SKILLS_DIR/../manifest.json" 2>/dev/null || \
      cp "$TMP_DIR/manifest.json" "manifest.json" 2>/dev/null || true
    fi
  fi

else
  # Fresh install
  mkdir -p "$SKILLS_DIR"

  for skill in "$TMP_DIR"/skills/*/; do
    skill_name=$(basename "$skill")
    target="$SKILLS_DIR/$skill_name"
    echo -e "  ${GREEN}✅${NC} $skill_name"

    if [ "$CODEX_MODE" = true ]; then
      mkdir -p "$target"
      rsync -a --delete "$skill/" "$target/"
    else
      cp -r "$skill" "$SKILLS_DIR/"
    fi
    INSTALLED=$((INSTALLED + 1))
  done

  # Copy manifest for future updates
  if [ -f "$TMP_DIR/manifest.json" ]; then
    if [ "$CODEX_MODE" = true ]; then
      cp "$TMP_DIR/manifest.json" "$SKILLS_DIR/manifest.json"
    else
      cp "$TMP_DIR/manifest.json" "$SKILLS_DIR/../manifest.json" 2>/dev/null || \
      cp "$TMP_DIR/manifest.json" "manifest.json" 2>/dev/null || true
    fi
  fi
fi

# Cleanup
rm -rf "$TMP_DIR"

# ─── Post-install Validation (Codex) ─────────────────────────

if [ "$CODEX_MODE" = true ]; then
  echo ""
  echo -e "${CYAN}🔍 Codex validation...${NC}"

  # Check for duplicate directories
  dupes=$(find "$SKILLS_DIR" -maxdepth 3 -type d \( -name 'references 2' -o -name 'scripts 2' -o -name 'assets 2' \) -print 2>/dev/null)
  if [ -n "$dupes" ]; then
    echo -e "  ${RED}⚠️  Duplicate directories found:${NC}"
    echo "$dupes" | while read -r d; do echo "    $d"; done
  else
    echo -e "  ${GREEN}✅${NC} No duplicate directories"
  fi

  # Check frontmatter validity
  invalid_fm=0
  for f in "$SKILLS_DIR"/*/SKILL.md; do
    [ -f "$f" ] || continue
    if [ "$(sed -n '1p' "$f")" != "---" ]; then
      echo -e "  ${RED}⚠️  Invalid frontmatter: $f${NC}"
      invalid_fm=$((invalid_fm + 1))
    fi
  done
  if [ $invalid_fm -eq 0 ]; then
    echo -e "  ${GREEN}✅${NC} All SKILL.md have valid frontmatter"
  fi
fi

# ─── Summary ─────────────────────────────────────────────────

echo ""
echo "──────────────────────────────────────────"

if [ "$MODE" = "update" ]; then
  TOTAL=$((UPDATED + NEW))
  echo -e "${BOLD}📊 Update summary:${NC}"
  [ $UPDATED -gt 0 ] && echo -e "  ${GREEN}↑${NC}  $UPDATED updated"
  [ $NEW -gt 0 ] && echo -e "  ${GREEN}+${NC}  $NEW new"
  [ $SKIPPED -gt 0 ] && echo "  ─  $SKIPPED unchanged"

  if [ -n "$BREAKING_LIST" ]; then
    echo ""
    echo -e "  ${RED}⚠️  Breaking changes detected:${NC}"
    echo -e "$BREAKING_LIST"
    echo -e "  ${YELLOW}Review CHANGELOG.md for migration instructions${NC}"
  fi

  if [ $TOTAL -eq 0 ]; then
    echo -e "  ${GREEN}✅ Already up to date!${NC}"
  fi
else
  echo -e "${GREEN}✅ $INSTALLED skills installed${NC} in $SKILLS_DIR/"
fi

echo ""
echo -e "💡 Tip: Run ${CYAN}bash install.sh check${NC} anytime to check for updates"
echo -e "📖 Docs: ${CYAN}https://gui.marketing/skills/${NC}"

if [ "$CODEX_MODE" = true ]; then
  echo ""
  echo -e "${YELLOW}⚡ Restart the Codex app to reload the skills menu.${NC}"
fi
