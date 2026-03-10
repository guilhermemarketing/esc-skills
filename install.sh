#!/bin/bash
# ─────────────────────────────────────────────────
# esc-skills installer
# Instala todas as skills no projeto atual
# ─────────────────────────────────────────────────

set -e

REPO="https://github.com/guilhermemarketing/esc-skills.git"
TMP_DIR="/tmp/esc-skills-$$"
SKILLS_DIR=".agent/skills"

echo "🧠 esc-skills installer"
echo "──────────────────────────────────"

# Detectar diretório de skills do agente
if [ -d ".cursor/skills" ]; then
  SKILLS_DIR=".cursor/skills"
elif [ -d ".agent/skills" ]; then
  SKILLS_DIR=".agent/skills"
else
  mkdir -p "$SKILLS_DIR"
fi

echo "📁 Diretório de destino: $SKILLS_DIR"

# Clonar repositório
echo "📥 Baixando skills..."
git clone --depth 1 "$REPO" "$TMP_DIR" 2>/dev/null

# Copiar skills
COUNT=0
for skill in "$TMP_DIR"/skills/*/; do
  skill_name=$(basename "$skill")
  echo "  ✅ $skill_name"
  cp -r "$skill" "$SKILLS_DIR/"
  COUNT=$((COUNT + 1))
done

# Cleanup
rm -rf "$TMP_DIR"

echo "──────────────────────────────────"
echo "✅ $COUNT skills instaladas em $SKILLS_DIR/"
echo ""
echo "💡 Adicione ao .instructions do seu projeto:"
echo '   Custom skills em '"$SKILLS_DIR"'/ — carregar com view_file no SKILL.md'
