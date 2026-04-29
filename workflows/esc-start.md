---
description: Pipeline completo de marketing digital para novo cliente — Message Mining* → Offer Diagnosis → ICP → Google Ads → Wireframe LP → Landing Page Premium → Meta Ads (+LinkedIn* +TikTok*) → Criativos Clássicos → Measurement Plan → Conversion QA → Lead Scoring. Orquestra 11 skills em sequência com handoff de contexto via arquivos .md consolidados.
---

# /esc-start — Pipeline Completo de Marketing (v3)

Pipeline sequencial de 11 etapas para gerar todos os ativos de marketing digital de um novo cliente. Cada etapa produz um arquivo `.md` consolidado que alimenta a próxima.

```
[Pré] Message Mining* → [0] Offer Diagnosis** → [1] ICP → [2] Google Ads → [3] Wireframe →
[4] LP → [5] Meta Ads (+LinkedIn* +TikTok*) → [6] Criativos → [7] Measurement Plan →
[8] Conversion QA → [9] Lead Scoring

*  Etapas condicionais: dependem do canal/necessidade do cliente.
** Etapa 0: obrigatória, skip sob solicitação explícita do usuário.
```

> A Etapa 5 é um "hub de ads" — o agente escolhe quais sub-skills executar (Meta, LinkedIn, TikTok) baseado nos canais ativos do cliente.

Para formatos de output de cada etapa, consultar `references/esc-start-output-formats.md`.

## Princípio Central

> **Contexto Consolidado > Contexto Bruto**
>
> Nunca passar briefing bruto + ICP + outputs anteriores todos juntos para a próxima etapa.
> Cada etapa recebe **apenas** o `icp-consolidado-{{CLIENTE}}.md` + o output consolidado da etapa imediatamente anterior (quando aplicável).
> Isso evita alucinações, reduz tokens e mantém qualidade entre etapas.

---

## Pre-flight: Coletar Briefing

Antes de iniciar o pipeline, obter do usuário:

1. **Nome do cliente** (será usado como `{{CLIENTE}}` em todos os arquivos)
2. **Briefing completo** — pode ser texto livre, documento, URL do site, ou respostas estruturadas:

```yaml
briefing:
  empresa: [Nome da empresa/marca(s)]
  produto_servico: [O que está sendo vendido/oferecido]
  mercado: [B2B / B2C / ambos]
  publico: [Quem — demográfico e psicográfico]
  dor: [Problema real que o produto resolve]
  diferencial: [O que diferencia das alternativas]
  prova_social: [Dados, cases, certificações, depoimentos]
  tom_de_voz: [Como a marca fala]
  objetivo: [Tipo de conversão: SQL, MQL, agendamento, orçamento, etc.]
  site_url: [URL(s) do site]
  paleta_cores: [Cores da marca, se fornecidas]
  restricoes: [O que NÃO pode ser dito/mostrado]
```

Se o briefing for insuficiente, **PARAR e perguntar**. Não iniciar o pipeline com informações incompletas.

**Compilar** o briefing em um resumo de no máximo 80 linhas antes de avançar.

3. **Material de VoC disponível?** Perguntar se o cliente possui:
   - Reviews online (G2, Trustpilot, Clutch, Google)
   - Transcrições de calls de vendas/discovery
   - Pesquisas/surveys de clientes
   - Dados de CRM (motivos de perda, tags)
   - Comentários em redes sociais ou Reddit

Se **sim** → iniciar pela Etapa Pré (Message Mining).
Se **não** → pular para Etapa 0 (Offer Diagnosis).

---

## Etapa Pré — Message Mining (Opcional)

**Skill:** `guimkt-sales-page-message-mining`

**Condição:** Roda se o usuário tiver material de Voice of Customer. Se não → **pular para Etapa 0**.

**Input:** Material de VoC bruto fornecido pelo usuário
**Output:** `message-mining-{{CLIENTE}}.md`

Executar a skill integralmente (Fases 0-3). O output enriquece TODAS as etapas seguintes — especialmente Offer Diagnosis, ICP, Wireframe e Copy.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 0 — Offer Diagnosis (Obrigatória)

**Skill:** `guimkt-offer-diagnosis`

**Comportamento:** Obrigatória. Se o usuário disser "pular" ou "skip", registrar no output e avançar. Nunca bloquear o pipeline.

**Input:** Briefing compilado (+ `message-mining-{{CLIENTE}}.md` se disponível)
**Output:** `offer-diagnosis-{{CLIENTE}}.md`

Executar a skill integralmente. Se `message-mining-{{CLIENTE}}.md` existir, cruzar dados com o intake.

> ⚠️ Se veredicto = "oferta precisa ser reconstruída", recomendar fortemente ao usuário corrigir antes de continuar — mas **não bloquear** o pipeline.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 1 — ICP (Ideal Customer Profile)

**Skill:** `guimkt-icp-ideal-customer-profile`

**Input:** Briefing compilado (+ `offer-diagnosis-{{CLIENTE}}.md` + `message-mining-{{CLIENTE}}.md` se disponíveis)
**Output:** `icp-consolidado-{{CLIENTE}}.html` + `icp-consolidado-{{CLIENTE}}.md`

Executar a skill integralmente. Se offer-diagnosis e/ou message-mining existirem, usar para enriquecer dimensões de objeções, diferenciais, perfil psicográfico e linguagem.

> ⚠️ O `.md` é o **artefato-ponte universal** — será enviado para TODAS as etapas seguintes.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 2 — Google Ads (Keywords + Anúncios)

**Skill:** `guimkt-google-ads` → executar **Fases 2, 3 e 4** (Fase 1/ICP já foi feita na Etapa 1)

**Input:** `icp-consolidado-{{CLIENTE}}.md`
**Output:** `google-ads-consolidado-{{CLIENTE}}.md`

Pular Fase 1 (ICP) — já concluída na Etapa 1 com a skill dedicada. Executar Fase 2 (Keywords Positivas) → Fase 3 (Negativas) → Fase 4 (RSA), com aprovação entre fases.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 3 — Wireframe da Landing Page

**Skill:** `guimkt-wireframe-landing-page`

**Input:** `icp-consolidado-{{CLIENTE}}.md` (+ `message-mining-{{CLIENTE}}.md` se disponível)
**Output:** `wireframe-tabela-{{CLIENTE}}.md`

Executar a skill integralmente. Se message-mining existir, usar verbatims para headlines e copy das seções. Fase 2 (Wireframe-Sketch HTML) é opcional — executar se solicitado.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 4 — Landing Page Premium

**Skill:** `guimkt-landing-page` → executar **apenas Fase 2** (Wireframe-Tabela já existe da Etapa 3)

**Input:** `icp-consolidado-{{CLIENTE}}.md` + `wireframe-tabela-{{CLIENTE}}.md`
**Output:** `landing-page-{{CLIENTE}}.html` + `design-system-{{CLIENTE}}.md`

Pular Fase 1 — já concluída na Etapa 3. Executar Fase 2 (Design System → LP Premium → Acessibilidade → Quality Gate).

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 5 — Meta Ads (Conceitos Criativos de Performance)

**Skill:** `guimkt-meta-ads`

**Input:** `icp-consolidado-{{CLIENTE}}.md` + `design-system-{{CLIENTE}}.md` (da Etapa 4, se disponível) (+ `message-mining-{{CLIENTE}}.md` se disponível)
**Output:** `meta-ads-conceitos-{{CLIENTE}}.md` + `prompts-imagens-{{CLIENTE}}.md`

Executar a skill integralmente (Etapas 0-6). Se `design-system-{{CLIENTE}}.md` existir da Etapa 4, usar direto (pula extração). Se message-mining existir, usar verbatims para hooks e ângulos de copy.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 6 — Criativos Clássicos (Multi-Plataforma)

**Skill:** `guimkt-classic-advertising-creative`

**Input:** `icp-consolidado-{{CLIENTE}}.md` + `meta-ads-conceitos-{{CLIENTE}}.md`

> O arquivo de Meta Ads é enviado como **referência de conceitos já criados** — para que os criativos clássicos complementem (não repitam) os ângulos e hooks já usados.

**Output:** `criativos-classicos-{{CLIENTE}}.md`

Executar a skill integralmente. Usar conceitos de Meta Ads como referência para diversificar ângulos e formatos.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 7 — Measurement Plan (Plano de Mensuração)

**Skill:** `guimkt-measurement-plan-architect`

**Input:** `icp-consolidado-{{CLIENTE}}.md` + `landing-page-{{CLIENTE}}.html` (URL ou arquivo da LP)
**Output:** `measurement-plan-{{CLIENTE}}.md`

Executar a skill integralmente (Fases 1-8). Coletar informações do ambiente técnico (CRM, plataformas de ads, domínio, ferramentas existentes) no início.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 8 — Conversion QA (Auditoria de Tracking)

**Skill:** `guimkt-conversion-qa-auditor`

**Modo:** Pre-Launch (valida plano + LP antes de ligar tráfego) OU Post-Implementation (valida execução técnica real)

**Input:** `measurement-plan-{{CLIENTE}}.md` + `landing-page-{{CLIENTE}}.html` (URL ou arquivo)
**Output:** `conversion-qa-{{CLIENTE}}.md`

Executar a skill integralmente. Scoring: 90%+ launch / 70-89% ressalvas / <70% não lançar.

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 9 — Lead Scoring Architecture

**Skill:** `guimkt-lead-scoring-architecture`

**Input:** `icp-consolidado-{{CLIENTE}}.md` + `measurement-plan-{{CLIENTE}}.md`
**Output:** `lead-scoring-{{CLIENTE}}.md`

Executar a skill integralmente (Fases 1-8). Coletar ambiente CRM, plataformas de ads, ciclo de vendas, volume de leads no início.

> ✅ **Pipeline completo.** Após a Etapa 9, todos os ativos de marketing estão gerados, mensuração planejada, tracking auditado e scoring definido.

---

## Regras de Contexto (Inegociáveis)

1. **SEMPRE CONSOLIDAR** — Cada etapa produz um `.md` consolidado. Nunca passar output bruto.
2. **ICP É UNIVERSAL** — O `icp-consolidado-{{CLIENTE}}.md` vai para TODAS as etapas (1-9).
3. **MESSAGE MINING É ENRIQUECIMENTO** — Se existir, usado como input adicional nas etapas de copy (0, 1, 3, 5).
4. **MÍNIMO DE CONTEXTO** — Cada etapa recebe no máximo 3 arquivos: ICP + output anterior + message mining (se aplicável).
5. **CHECKPOINT OBRIGATÓRIO** — Apresentar output e aguardar aprovação antes de avançar.
6. **NÃO INVENTAR DADOS** — Se falta info, PARAR e perguntar ao usuário.
7. **NAMING CONSISTENTE** — Todos os arquivos seguem: `[tipo]-{{CLIENTE}}.md`
8. **SEQUÊNCIA RESPEITADA** — Executar sempre na ordem: Pré → 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
9. **ETAPAS OPCIONAIS** — Pré (Message Mining) é opcional. Etapa 0 (Offer Diagnosis) é obrigatória mas skipável sob solicitação explícita.
10. **LEAD SCORING COMPLEMENTA MEASUREMENT PLAN** — measurement-plan define *quais campos* capturar; lead-scoring define *o que fazer* com esses dados no CRM.

---

## Mapa de Dependências de Arquivos

```
message-mining-{{CLIENTE}}.md ──────┐ (opcional, enriquece 0, 1, 3, 5)
                                    ▼
offer-diagnosis-{{CLIENTE}}.md ─────┐ (enriquece 1)
                                    ▼
icp-consolidado-{{CLIENTE}}.md ─────┬──→ Etapa 2 (Google Ads)
        │                           ├──→ Etapa 3 (Wireframe)
        │                           ├──→ Etapa 4 (LP) + wireframe
        │                           ├──→ Etapa 5 (Meta Ads +LinkedIn* +TikTok*)
        │                           ├──→ Etapa 6 (Criativos) + meta-ads
        │                           ├──→ Etapa 7 (Measurement) + LP
        │                           ├──→ Etapa 8 (QA) + measurement-plan
        │                           └──→ Etapa 9 (Lead Scoring) + measurement-plan
        │
        └──→ [ARTEFATO-PONTE UNIVERSAL]
```

---

## Notas Operacionais

1. Se o pipeline for interrompido, pode ser retomado de qualquer etapa — basta ter os `.md` das etapas anteriores
2. Se o cliente tiver múltiplas marcas, processar uma marca por vez em cada etapa
3. O `icp-consolidado-{{CLIENTE}}.md` pode ser atualizado com feedback — nesse caso, considerar se etapas posteriores precisam ser refeitas
4. Este workflow funciona em qualquer agente que suporte as skills do repositório ESC Skills
5. As Etapas 7-9 (Measurement Plan + QA + Lead Scoring) podem ser executadas em paralelo com as Etapas 5-6 (Ads + Criativos) se o time tiver capacidade
6. Lead Scoring (Etapa 9) é altamente recomendada para clientes com CRM — sem ela, value-based bidding não tem fundação