#!/bin/bash
# ─────────────────────────────────────────────────
# esc-skills installer & updater
# Install or update all skills in the current project
#
# Usage:
#   curl -sL https://raw.githubusercontent.com/guilhermemarketing/esc-skills/main/install.sh | bash
#   bash install.sh              # Install (first time)
#   bash install.sh update       # Update existing skills
#   bash install.sh check        # Check for updates (no changes)
# ─────────────────────────────────────────────────

set -e

REPO="https://github.com/guilhermemarketing/esc-skills.git"
RAW_BASE="https://raw.githubusercontent.com/guilhermemarketing/esc-skills/main"
TMP_DIR="/tmp/esc-skills-$$"
SKILLS_DIR=".agent/skills"
MODE="${1:-install}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo ""
echo -e "${BOLD}🧠 esc-skills${NC} — AI Marketing Skills for Agents"
echo "──────────────────────────────────────────"

# Detect agent skills directory
if [ -d ".cursor/skills" ]; then
  SKILLS_DIR=".cursor/skills"
elif [ -d ".agent/skills" ]; then
  SKILLS_DIR=".agent/skills"
fi

# ─── Check Mode ──────────────────────────────────────────

if [ "$MODE" = "check" ]; then
  echo -e "${CYAN}🔍 Checking for updates...${NC}"

  # Download remote manifest
  REMOTE_MANIFEST=$(curl -sL "$RAW_BASE/manifest.json" 2>/dev/null)
  if [ -z "$REMOTE_MANIFEST" ]; then
    echo -e "${RED}❌ Could not fetch remote manifest${NC}"
    exit 1
  fi

  LOCAL_MANIFEST="$SKILLS_DIR/../manifest.json"
  if [ ! -f "$LOCAL_MANIFEST" ]; then
    # Try skills dir parent or check current manifest
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

# ─── Install / Update Mode ───────────────────────────────

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
        # Extract versions from headers
        OLD_VER=$(head -1 "$target/SKILL.md" 2>/dev/null | grep -oP 'version:\s*\K[0-9]+\.[0-9]+\.[0-9]+' || echo "?.?.?")
        NEW_VER=$(head -1 "$skill/SKILL.md" 2>/dev/null | grep -oP 'version:\s*\K[0-9]+\.[0-9]+\.[0-9]+' || echo "?.?.?")

        # Check for breaking change (major version bump)
        OLD_MAJOR=$(echo "$OLD_VER" | cut -d. -f1)
        NEW_MAJOR=$(echo "$NEW_VER" | cut -d. -f1)

        if [ "$OLD_MAJOR" != "$NEW_MAJOR" ] 2>/dev/null; then
          echo -e "  ${RED}⚠️  $skill_name: $OLD_VER → $NEW_VER (BREAKING)${NC}"
          BREAKING_LIST="$BREAKING_LIST\n    - $skill_name: $OLD_VER → $NEW_VER"
        else
          echo -e "  ${GREEN}↑${NC}  $skill_name: $OLD_VER → $NEW_VER"
        fi

        cp -r "$skill"/* "$target/"
        UPDATED=$((UPDATED + 1))
      fi
    else
      # New skill
      echo -e "  ${GREEN}+${NC}  $skill_name (new)"
      mkdir -p "$target"
      cp -r "$skill"/* "$target/"
      NEW=$((NEW + 1))
    fi
  done

  # Copy manifest
  if [ -f "$TMP_DIR/manifest.json" ]; then
    cp "$TMP_DIR/manifest.json" "$SKILLS_DIR/../manifest.json" 2>/dev/null || \
    cp "$TMP_DIR/manifest.json" "manifest.json" 2>/dev/null || true
  fi

else
  # Fresh install
  mkdir -p "$SKILLS_DIR"

  for skill in "$TMP_DIR"/skills/*/; do
    skill_name=$(basename "$skill")
    echo -e "  ${GREEN}✅${NC} $skill_name"
    cp -r "$skill" "$SKILLS_DIR/"
    INSTALLED=$((INSTALLED + 1))
  done

  # Copy manifest for future updates
  if [ -f "$TMP_DIR/manifest.json" ]; then
    cp "$TMP_DIR/manifest.json" "$SKILLS_DIR/../manifest.json" 2>/dev/null || \
    cp "$TMP_DIR/manifest.json" "manifest.json" 2>/dev/null || true
  fi
fi

# Cleanup
rm -rf "$TMP_DIR"

# Summary
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
