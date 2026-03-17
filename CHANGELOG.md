# Changelog

Todas as alterações notáveis no repositório ESC Skills são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/). Skills seguem [Semantic Versioning](https://semver.org/).

---

## [1.1.0] - 2026-03-17

### Infraestrutura de Distribuição

- **Adicionado:** `install.sh` reescrito com 3 modos: `install` (fresh), `update` (diff-based com version comparison e breaking change detection), `check` (verifica atualizações sem alterar)
- **Adicionado:** `.github/workflows/auto-release.yml` — cria GitHub Releases automaticamente quando skills mudam, com notificação Discord opcional para breaking changes
- **Atualizado:** `README.md` — seção Updates (EN + PT) com novos comandos `bash install.sh update` e `bash install.sh check`
- **Tipo:** MINOR
- **Impacto em agentes:** Nenhum — infraestrutura de distribuição para usuários finais
- **Migração necessária:** Não

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
