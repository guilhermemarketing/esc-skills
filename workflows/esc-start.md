---
description: Pipeline completo de marketing digital para novo cliente — Message Mining* → Offer Diagnosis → ICP → Google Ads → Wireframe LP → Landing Page Premium → Meta Ads (+LinkedIn* +TikTok*) → Criativos Clássicos → Measurement Plan → Conversion QA → Lead Scoring. Orquestra 11 skills em sequência com handoff de contexto via arquivos .md consolidados.
---

# /esc-start — Pipeline Completo de Marketing (v3)

Pipeline sequencial de 11 etapas para gerar todos os ativos de marketing digital de um novo cliente. Cada etapa produz um arquivo `.md` consolidado que alimenta a próxima, garantindo consistência de contexto e eficiência de tokens.

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

**Condição:** Roda se o usuário tiver material de Voice of Customer (reviews, calls, transcrições, Reddit, CRM, pesquisas). Se não houver material, **pular para Etapa 0**.

**Input:** Material de VoC bruto fornecido pelo usuário

**Execução:**
1. Invocar a skill `guimkt-sales-page-message-mining`
2. Executar Fase 0 — Intake e Inventário de Fontes
3. Executar Fase 1 — Mineração e Extração (Review Mining, Transcrições, Surveys, Reddit)
4. Executar Fase 2 — Categorização e Priorização (6 mapas)
5. Executar Fase 3 — Gerar output consolidado
6. Apresentar ao usuário → aprovação

**Output:** `message-mining-{{CLIENTE}}.md`

> 💡 Este arquivo enriquece TODAS as etapas seguintes — especialmente Offer Diagnosis, ICP, Wireframe e Copy.

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 0.

---

## Etapa 0 — Offer Diagnosis (Obrigatória)

**Skill:** `guimkt-offer-diagnosis`

**Comportamento:** Obrigatória. Se o usuário disser "pular" ou "skip", registrar no output e avançar. Nunca bloquear o pipeline.

**Input:** Briefing compilado (+ `message-mining-{{CLIENTE}}.md` se disponível)

**Execução:**
1. Invocar a skill `guimkt-offer-diagnosis`
2. Executar Etapa 0 — Intake Obrigatório (10 perguntas)
3. Se `message-mining-{{CLIENTE}}.md` existir, cruzar dados com o intake
4. Executar Etapa 1 — Diagnóstico das 8 Dimensões
5. Executar Etapa 2 — Scoring e Veredicto
6. Executar Etapa 3 — Recomendações de Fortalecimento (se necessário)
7. Apresentar ao usuário → aprovação

**Output:** `offer-diagnosis-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

> ⚠️ Se veredicto = "oferta precisa ser reconstruída", recomendar fortemente ao usuário corrigir antes de continuar — mas **não bloquear** o pipeline.

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 1.

---

## Etapa 1 — ICP (Ideal Customer Profile)

**Skill:** `guimkt-icp-ideal-customer-profile`

**Input:** Briefing compilado (+ `offer-diagnosis-{{CLIENTE}}.md` + `message-mining-{{CLIENTE}}.md` se disponíveis)

**Execução:**
1. Invocar a skill `guimkt-icp-ideal-customer-profile`
2. Executar Etapa 1 — Coletar Contexto do Cliente
3. Se `offer-diagnosis-{{CLIENTE}}.md` existir, usar para enriquecer dimensões de objeções, diferenciais e ângulo
4. Se `message-mining-{{CLIENTE}}.md` existir, usar para enriquecer perfil psicográfico e linguagem
5. Executar Etapa 2 — Gerar ICP (9 Dimensões)
6. Executar Etapa 3 — Enriquecer com Análise Psicográfica (Psicográfico + ICP Real vs. Aspiracional + Modelos Mentais)
7. Executar Etapa 4 — Gerar Outputs (HTML + Markdown)
8. Apresentar ao usuário → aprovação

**Output:** `icp-consolidado-{{CLIENTE}}.html` + `icp-consolidado-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

> ⚠️ O `.md` é o **artefato-ponte universal** — será enviado para TODAS as etapas seguintes.

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 2.

---

## Etapa 2 — Google Ads (Keywords + Anúncios)

**Skill:** `guimkt-google-ads` → executar **Fases 2, 3 e 4** (Fase 1/ICP já foi feita na Etapa 1)

**Input:** `icp-consolidado-{{CLIENTE}}.md`

**Execução:**
1. Carregar no contexto **apenas** o `icp-consolidado-{{CLIENTE}}.md`
2. Pular Fase 1 (ICP) — já concluída na Etapa 1 com a skill dedicada
3. Executar Fase 2 — Keywords Positivas (30 por marca) → aprovação
4. Executar Fase 3 — Keywords Negativas → aprovação
5. Executar Fase 4 — Anúncios Responsivos (RSA) → aprovação

**Output:** `google-ads-consolidado-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 3.

---

## Etapa 3 — Wireframe da Landing Page

**Skill:** `guimkt-wireframe-landing-page`

**Input:** `icp-consolidado-{{CLIENTE}}.md` (+ `message-mining-{{CLIENTE}}.md` se disponível)

**Execução:**
1. Carregar no contexto **apenas** o `icp-consolidado-{{CLIENTE}}.md`
2. Se `message-mining-{{CLIENTE}}.md` existir, usar verbatims para headlines e copy das seções
3. Executar Etapa 1.0 — Espectro da Proposta de Valor
4. Executar Etapa 1.1 — Selecionar Framework de Copywriting
5. Executar Etapa 1.2 — Gerar Wireframe-Tabela
6. Executar Etapa 1.3 — Enriquecimento
7. Apresentar ao usuário → aprovação
8. (Opcional) Executar Fase 2 — Wireframe-Sketch (HTML de baixa fidelidade)

**Output:** `wireframe-tabela-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 4.

---

## Etapa 4 — Landing Page Premium

**Skill:** `guimkt-landing-page` → executar **apenas Fase 2** (Wireframe-Tabela já existe da Etapa 3)

**Input:** `icp-consolidado-{{CLIENTE}}.md` + `wireframe-tabela-{{CLIENTE}}.md`

**Execução:**
1. Carregar no contexto **apenas** os 2 arquivos acima (não recarregar briefing bruto)
2. Pular Fase 1 — já concluída na Etapa 3
3. Executar Etapa 2.1 — Definir Design System
4. Executar Etapa 2.2 — Gerar Landing Page Premium (HTML auto-contido)
5. Executar Etapa 2.3 — Acessibilidade
6. Validar Quality Gate (5 Dimensões de UX)
7. Apresentar ao usuário → aprovação

**Output:** `landing-page-{{CLIENTE}}.html` + `design-system-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 5.

---

## Etapa 5 — Meta Ads (Conceitos Criativos de Performance)

**Skill:** `guimkt-meta-ads`

**Input:** `icp-consolidado-{{CLIENTE}}.md` + `design-system-{{CLIENTE}}.md` (da Etapa 4, se disponível) (+ `message-mining-{{CLIENTE}}.md` se disponível)

**Execução:**
1. Carregar no contexto **apenas** o `icp-consolidado-{{CLIENTE}}.md`
2. Executar Etapa 0 — Design System: carregar `design-system-{{CLIENTE}}.md` (se existir da Etapa 4)
3. Executar Etapa 1 — Diagnóstico do Briefing + Customer Avatar Hooks (extrair why want / why not want / why watch do ICP)
4. Se `message-mining-{{CLIENTE}}.md` existir, usar verbatims para hooks e ângulos de copy
5. Executar Etapa 2 — Customer Journey Mapping (distribuir Creative Types por Cold/Warm/Hot)
6. Executar Etapa 3 — Gerar 10 Conceitos (mín. 6 Creative Types distintos, cobertura Cold/Warm/Hot)
7. Executar Etapa 4 — Desenvolver Cada Conceito (Hook → Hold → Offer + 3 variações A/B)
8. Executar Etapa 5 — Checklist de Validação (performance + compliance)
9. Executar Etapa 6 — Gerar arquivo de prompts de imagem consolidado
10. Apresentar ao usuário → aprovação

**Output:** `meta-ads-conceitos-{{CLIENTE}}.md` + `prompts-imagens-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 6.

---

## Etapa 6 — Criativos Clássicos (Multi-Plataforma)

**Skill:** `guimkt-classic-advertising-creative`

**Input:** `icp-consolidado-{{CLIENTE}}.md` + `meta-ads-conceitos-{{CLIENTE}}.md`

> O arquivo de Meta Ads é enviado como **referência de insights e clichês já descartados** — para que os criativos clássicos complementem (não repitam) os de Meta Ads.

**Execução:**
1. Carregar no contexto os 2 arquivos acima
2. Executar Etapa 0 — Diagnóstico do Briefing (reusar ICP)
3. Executar Etapa 1 — Anti-Clichê (considerar clichês já descartados em Meta Ads)
4. Executar Etapa 2 — Encontrar Insight (ângulos complementares)
5. Executar Etapa 3 — Gerar Conceitos (mínimo 3)
6. Executar Etapa 4 — Desenvolver (imagem estática, carrossel e/ou vídeo)
7. Executar Etapa 5 — Checklist de Qualidade
8. Apresentar ao usuário → aprovação

**Output:** `criativos-classicos-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 7.

---

## Etapa 7 — Measurement Plan (Plano de Mensuração)

**Skill:** `guimkt-measurement-plan-architect`

**Input:** `icp-consolidado-{{CLIENTE}}.md` + `landing-page-{{CLIENTE}}.html` (URL ou arquivo da LP)

**Execução:**
1. Invocar a skill `guimkt-measurement-plan-architect`
2. Executar Fase 1 — Intake: coletar informações do ambiente técnico (CRM, plataformas de ads, domínio, ferramentas existentes)
3. Executar Fase 2 — Funil & KPIs (mapa de KPIs, filosofia Brandformance/Funil Invertido)
4. Executar Fase 3 — Lead Quality & Conversion Value Schema (conversões primárias/secundárias, valor por evento, campos obrigatórios, hidden fields)
5. Executar Fase 4 — Tracking Architecture (taxonomia GA4, dataLayer schema, plano GTM web + server-side, UTMs + parâmetros de atribuição)
6. Executar Fase 5 — Offline Conversions & CRM Integration
7. Executar Fase 6 — Enhanced Conversions & Server-Side (Google Ads, Meta CAPI incl. fbclid, LinkedIn, TikTok + Stape GEO Headers)
8. Executar Fase 7 — Consent & Privacy Architecture (Consent Mode v2, CMP, region-specific behavior)
9. Executar Fase 8 — QA Checklist Preview (gerar checklist preliminar para Etapa 8)
10. Apresentar ao usuário → aprovação

**Output:** `measurement-plan-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 8.

---

## Etapa 8 — Conversion QA (Auditoria de Tracking)

**Skill:** `guimkt-conversion-qa-auditor`

**Modo:** Pre-Launch (valida plano + LP antes de ligar tráfego) OU Post-Implementation (valida execução técnica real)

**Input:** `measurement-plan-{{CLIENTE}}.md` + `landing-page-{{CLIENTE}}.html` (URL ou arquivo)

**Execução:**
1. Invocar a skill `guimkt-conversion-qa-auditor`
2. Executar Fase 1 — Carregar blueprint do measurement plan
3. Executar Fase 2 — Checklist QA por categoria (dataLayer, GA4, Google Ads, Meta Pixel, Meta CAPI, hidden fields, consent mode, sGTM, UTMs, offline conversions, cross-device)
4. Executar Fase 3 — Testes End-to-End (formulário com UTMs, WhatsApp click, consent denied)
5. Executar Fase 4 — Scoring e Veredicto (90%+ launch / 70-89% ressalvas / <70% não lançar)
6. Executar Fase 5 — Gerar relatório de QA com itens críticos e recomendações
7. Apresentar ao usuário → aprovação

**Output:** `conversion-qa-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

**Checkpoint:** Aguardar aprovação do usuário antes de avançar para Etapa 9.

---

## Etapa 9 — Lead Scoring Architecture

**Skill:** `guimkt-lead-scoring-architecture`

**Input:** `icp-consolidado-{{CLIENTE}}.md` + `measurement-plan-{{CLIENTE}}.md`

**Execução:**
1. Invocar a skill `guimkt-lead-scoring-architecture`
2. Executar Fase 1 — Intake: coletar ambiente CRM, plataformas de ads, ciclo de vendas, volume de leads
3. Executar Fase 2 — Lifecycle Stages (Lead → MQL → SAL → SQL → Opportunity → Customer → Evangelist)
4. Executar Fase 3 — Scoring Model (explícito: fit/firmográfico + implícito: engagement/comportamental + intent signals)
5. Executar Fase 4 — Conversion Value Mapping para value-based bidding (Google Ads, Meta Ads)
6. Executar Fase 5 — Routing Rules e automações (quando mover, quando alertar, quando descartar)
7. Executar Fase 6 — Integration Specs (HubSpot, Pipedrive, RD Station, Salesforce)
8. Executar Fase 7 — Calibração e revisão periódica (closed-won/lost ratio, decay rules)
9. Executar Fase 8 — Gerar Outputs (Markdown + HTML premium)
10. Apresentar ao usuário → aprovação

**Output:** `lead-scoring-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

> ✅ **Pipeline completo.** Após a Etapa 9, todos os ativos de marketing estão gerados, mensuração planejada, tracking auditado e scoring definido.

---

## Regras de Contexto (Inegociáveis)

1. **SEMPRE CONSOLIDAR** — Cada etapa produz um `.md` consolidado. Nunca passar output bruto.
2. **ICP É UNIVERSAL** — O `icp-consolidado-{{CLIENTE}}.md` vai para TODAS as etapas (1-9).
3. **MESSAGE MINING É ENRIQUECIMENTO** — Se existir, `message-mining-{{CLIENTE}}.md` é usado como input adicional nas etapas de copy (0, 1, 3, 5).
4. **OFFER DIAGNOSIS É CONTEXTO** — Se existir, `offer-diagnosis-{{CLIENTE}}.md` enriquece o ICP.
5. **MÍNIMO DE CONTEXTO** — Cada etapa recebe no máximo 3 arquivos: ICP + output anterior + message mining (se aplicável).
6. **CHECKPOINT OBRIGATÓRIO** — Apresentar output e aguardar aprovação antes de avançar.
7. **NÃO INVENTAR DADOS** — Se falta info, PARAR e perguntar ao usuário.
8. **NAMING CONSISTENTE** — Todos os arquivos seguem: `[tipo]-{{CLIENTE}}.md`
9. **SEQUÊNCIA RESPEITADA** — Executar sempre na ordem: Pré → 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
10. **ETAPAS OPCIONAIS** — Pré (Message Mining) é opcional. Etapa 0 (Offer Diagnosis) é obrigatória mas skipável sob solicitação explícita.
11. **LEAD SCORING COMPLEMENTA MEASUREMENT PLAN** — measurement-plan define *quais campos* capturar; lead-scoring define *o que fazer* com esses dados no CRM (scoring, routing, lifecycle transitions).

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