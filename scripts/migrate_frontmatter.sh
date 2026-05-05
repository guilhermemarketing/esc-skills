#!/bin/bash
# ─────────────────────────────────────────────────
# ESC Skills — Frontmatter Migration Script
# Moves version/updated from HTML comment (line 1) into YAML frontmatter.
#
# BEFORE:
#   <!-- skill: name | version: 1.0.0 | updated: 2026-03-17 -->
#   ---
#   name: skill-name
#   description: ...
#   ---
#
# AFTER:
#   ---
#   name: skill-name
#   description: ...
#   version: "1.0.0"
#   updated: "2026-03-17"
#   ---
#
# Usage:
#   bash scripts/migrate_frontmatter.sh [directory]
#   Default directory: skills/
#
# Safe to run multiple times — skips already-migrated files.
# Compatible with macOS (BSD sed) and Linux (GNU sed).
# ─────────────────────────────────────────────────

set -e

TARGET_DIR="${1:-skills}"
MIGRATED=0
SKIPPED=0
ERRORS=0

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo ""
echo -e "🔄 Migrating SKILL.md frontmatter in ${TARGET_DIR}/"
echo "──────────────────────────────────────────"

for skillmd in "$TARGET_DIR"/*/SKILL.md; do
  [ -f "$skillmd" ] || continue
  skill_name=$(basename "$(dirname "$skillmd")")

  first_line=$(sed -n '1p' "$skillmd")

  # Already migrated — first line is ---
  if [ "$first_line" = "---" ]; then
    # Check if version: already exists inside frontmatter
    if sed -n '2,/^---$/p' "$skillmd" | grep -q '^version:'; then
      SKIPPED=$((SKIPPED + 1))
      continue
    fi
  fi

  # Extract version and updated from HTML comment (line 1)
  if echo "$first_line" | grep -qE '^[[:space:]]*<!--[[:space:]]*skill:'; then
    # Use grep + sed for portable extraction
    version=$(echo "$first_line" | grep -oE 'version: *[0-9]+\.[0-9]+\.[0-9]+' | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
    updated=$(echo "$first_line" | grep -oE 'updated: *[0-9]{4}-[0-9]{2}-[0-9]{2}' | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2}')

    if [ -z "$version" ]; then
      echo -e "  ${RED}❌ $skill_name — could not extract version from: $(echo "$first_line" | head -c 80)${NC}"
      ERRORS=$((ERRORS + 1))
      continue
    fi

    if [ -z "$updated" ]; then
      updated="2026-05-05"
    fi

    # Build the new file using Python for reliability across macOS/Linux
    python3 -c "
import sys

filepath = sys.argv[1]
version = sys.argv[2]
updated = sys.argv[3]

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove line 1 (HTML comment)
lines = lines[1:]

# Find the closing --- of the frontmatter
# lines[0] should be '---\n', find the next '---\n'
closing_idx = None
for i in range(1, len(lines)):
    if lines[i].strip() == '---':
        closing_idx = i
        break

if closing_idx is None:
    print(f'ERROR: could not find closing --- in {filepath}', file=sys.stderr)
    sys.exit(1)

# Insert version and updated before the closing ---
lines.insert(closing_idx, f'version: \"{version}\"\n')
lines.insert(closing_idx + 1, f'updated: \"{updated}\"\n')

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)
" "$skillmd" "$version" "$updated"

    echo -e "  ${GREEN}✅${NC} $skill_name: v${version} (${updated})"
    MIGRATED=$((MIGRATED + 1))

  elif [ "$first_line" = "---" ]; then
    # First line is ---, but no version: in frontmatter yet
    echo -e "  ${YELLOW}⚠️  $skill_name — starts with --- but no version: in frontmatter${NC}"
    SKIPPED=$((SKIPPED + 1))
  else
    echo -e "  ${RED}❌ $skill_name — unexpected first line: $(echo "$first_line" | head -c 60)${NC}"
    ERRORS=$((ERRORS + 1))
  fi
done

echo ""
echo "──────────────────────────────────────────"
echo -e "📊 Results: ${GREEN}${MIGRATED} migrated${NC} | ${YELLOW}${SKIPPED} skipped${NC} | ${RED}${ERRORS} errors${NC}"
echo ""

# Validation
echo "🔍 Validating all SKILL.md start with ---..."
fail_count=0
for f in "$TARGET_DIR"/*/SKILL.md; do
  [ -f "$f" ] || continue
  if [ "$(sed -n '1p' "$f")" != "---" ]; then
    echo -e "  ${RED}FAIL: $f${NC}"
    fail_count=$((fail_count + 1))
  fi
done

if [ $fail_count -eq 0 ]; then
  echo -e "  ${GREEN}✅ All SKILL.md files start with ---${NC}"
else
  echo -e "  ${RED}❌ $fail_count files still have invalid first line${NC}"
  exit 1
fi
