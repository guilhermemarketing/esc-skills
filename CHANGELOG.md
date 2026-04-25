# Changelog

Todas as alterações notáveis no repositório ESC Skills são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/). Skills seguem [Semantic Versioning](https://semver.org/).

---

## [2.2.0] - 2026-04-25

### Q3 Sprint 1 — Pipeline v3 (11 etapas) + 2 Skills Estratégicas

- **Adicionado:** `guimkt-lead-scoring-architecture` — arquitetura completa de lead scoring e lifecycle stages (Lead → MQL → SAL → SQL → Opportunity → Customer → Evangelist) com scoring explícito (fit) + implícito (engagement) + intent signals, conversion value mapping para value-based bidding, routing rules, integration specs (HubSpot, Pipedrive, RD Station, Salesforce), e calibração periódica. Etapa 9 do pipeline `/esc-start` v3
- **Adicionado:** `guimkt-brandformance-planner` — planejamento estratégico de mix Branding vs. Performance com diagnóstico de maturidade de marca (1-5), mix awareness/consideration/conversion, cenários conservador/moderado/agressivo, KPIs por fase, brand signals map. Baseado em Les Binet & Peter Field, Byron Sharp, Ehrenberg-Bass + metodologia proprietária gui.marketing (Micro-Bolhas, Funil Invertido, Janelas de Impacto). Etapa 3.5 condicional do pipeline `/esc-report` v2
- **Atualizado:** Pipeline `/esc-start` — v2 → **v3** (10 → 11 etapas, Lead Scoring como Etapa 9, Etapa 5 como hub de ads com suporte futuro para LinkedIn/TikTok)
- **Atualizado:** Pipeline `/esc-report` — v1 → **v2** (nova Etapa 3.5 Brandformance Planning condicional, 5 skills orquestradas)
- **Atualizado:** `references/esc-start-output-formats.md` — v2 → **v3** (novo template Etapa 9 Lead Scoring)
- **Atualizado:** `manifest.json` — 83 → 85 skills
- **Tipo:** MINOR
- **Impacto em agentes:** Pipeline `/esc-start` agora tem 11 etapas. Agentes que referenciam "10 etapas" devem atualizar. `/esc-report` tem nova etapa condicional 3.5
- **Migração necessária:** Atualizar referências ao pipeline de 10 para 11 etapas

---

## [2.1.0] - 2026-04-24

### Sprint 2 — Skills Independentes (4 novas)

- **Adicionado:** `guimkt-executive-performance-report` — relatório executivo profit-first com Brandformance Flywheel, Unit Economics e vereditos por canal. Markdown + HTML premium
- **Adicionado:** `guimkt-consent-mode-audit` — auditoria LGPD + Consent Mode v2 + CMP com score system 0-100 em 4 áreas
- **Adicionado:** `guimkt-experimentation-engine` — codifica disciplina de CRO com FACT&ACT, ROAR gate, PIPE scoring, behavioral science, sample size calculation
- **Adicionado:** `guimkt-utm-governance` — governança operacional de UTMs, naming conventions, templates por canal, auditoria de inconsistências, integração CRM, cenários WhatsApp-first (CTWA, WABA)
- **Atualizado:** `manifest.json` — 79 → 83 skills
- **Atualizado:** `README.md` — contagens 74+ → 83+, pipeline 6 → 10 etapas, tabelas Featured e All Skills expandidas
- **Atualizado:** `CHANGELOG.md` — este arquivo
- **Tipo:** MINOR
- **Impacto em agentes:** 4 novas skills disponíveis para uso imediato. Independentes — não alteram pipeline existente
- **Migração necessária:** Não

---

## [2.0.0] - 2026-04-24

### Sprint 1 — Pipeline v2 (10 etapas) + 4 Skills Core

- **Adicionado:** `guimkt-offer-diagnosis` — guard-rail fundacional (Etapa 0 do pipeline). Diagnostica 8 dimensões da oferta antes de gerar ativos
- **Adicionado:** `guimkt-measurement-plan-architect` — plano completo de mensuração com tracking architecture, consent mode, lead quality schema, offline conversions, enhanced conversions, WhatsApp-first scenarios (Etapa 7)
- **Adicionado:** `guimkt-conversion-qa-auditor` — auditoria go/no-go em dois modos: Pre-Launch e Post-Implementation. 11 categorias de QA, 70+ checks (Etapa 8)
- **Adicionado:** `guimkt-sales-page-message-mining` — Voice of Customer e review mining. Etapa Pré (-1) opcional que alimenta todas as skills downstream
- **Atualizado:** Pipeline `/esc-start` — expandido de 6 para 10 etapas (Pré, 0, 1-8)
- **Atualizado:** `manifest.json` — 74 → 79 skills (4 novas + 1 outra)
- **Tipo:** MAJOR
- **Impacto em agentes:** Pipeline `/esc-start` agora tem 10 etapas. Agentes que referenciam "6 etapas" devem atualizar
- **Migração necessária:** Atualizar referências ao pipeline de 6 para 10 etapas. Skills existentes não mudaram

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
