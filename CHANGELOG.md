# Changelog

Todas as alterações notáveis no repositório ESC Skills são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/). Skills seguem [Semantic Versioning](https://semver.org/).

---

## [1.0.0] - 2026-03-17

### All Skills (74 skills)

- **Tipo:** MAJOR
- **O que mudou:** Inicialização do sistema de versionamento semântico — todas as 74 skills recebem versão 1.0.0, cabeçalho de versão no SKILL.md, e hash SHA-256 no manifest.json
- **Impacto em agentes:** Nenhum — baseline inicial, sem mudança de comportamento
- **Migração necessária:** Não

### Infraestrutura

- **Adicionado:** `manifest.json` — fonte de verdade com versão e hash de cada skill
- **Adicionado:** `scripts/update_manifest.py` — script de automação (init, verify, bump, add-headers)
- **Adicionado:** `.github/workflows/version-bump.yml` — CI para validação de integridade
- **Adicionado:** `CHANGELOG.md` — este arquivo
- **Atualizado:** `.gitignore` — exceções para novos arquivos de infraestrutura
