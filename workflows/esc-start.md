---
description: Pipeline completo de marketing digital para novo cliente — ICP → Google Ads → Wireframe LP → Landing Page Premium → Meta Ads → Criativos Clássicos. Orquestra 6 skills em sequência com handoff de contexto via arquivos .md consolidados.
---

# /esc-start — Pipeline Completo de Marketing

Pipeline sequencial de 6 etapas para gerar todos os ativos de marketing digital de um novo cliente. Cada etapa produz um arquivo `.md` consolidado que alimenta a próxima, garantindo consistência de contexto e eficiência de tokens.

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

---

## Etapa 1 — ICP (Ideal Customer Profile)

**Skill:** `guimkt-icp-ideal-customer-profile`

**Input:** Briefing compilado do cliente

**Execução:**
1. Invocar a skill `guimkt-icp-ideal-customer-profile`
2. Executar Etapa 1 — Coletar Contexto do Cliente
3. Executar Etapa 2 — Gerar ICP (9 Dimensões)
4. Executar Etapa 3 — Enriquecer com Análise Psicográfica (Psicográfico + ICP Real vs. Aspiracional + Modelos Mentais)
5. Executar Etapa 4 — Gerar Outputs (HTML + Markdown)
6. Apresentar ao usuário → aprovação

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

**Input:** `icp-consolidado-{{CLIENTE}}.md`

**Execução:**
1. Carregar no contexto **apenas** o `icp-consolidado-{{CLIENTE}}.md`
2. Executar Etapa 1.0 — Espectro da Proposta de Valor
3. Executar Etapa 1.1 — Selecionar Framework de Copywriting
4. Executar Etapa 1.2 — Gerar Wireframe-Tabela
5. Executar Etapa 1.3 — Enriquecimento
6. Apresentar ao usuário → aprovação
7. (Opcional) Executar Fase 2 — Wireframe-Sketch (HTML de baixa fidelidade)

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

## Etapa 5 — Meta Ads (Conceitos Criativos)

**Skill:** `guimkt-meta-ads`

**Input:** `icp-consolidado-{{CLIENTE}}.md`

**Execução:**
1. Carregar no contexto **apenas** o `icp-consolidado-{{CLIENTE}}.md`
2. Executar Etapa 1 — Diagnóstico do Briefing (usando dados do ICP consolidado)
3. Executar Etapa 2 — Anti-Clichê
4. Executar Etapa 3 — Encontrar Insight
5. Executar Etapa 4 — Gerar 6 Conceitos
6. Executar Etapa 5 — Desenvolver Cada Conceito
7. Executar Etapa 6 — Checklist de Validação
8. Apresentar ao usuário → aprovação

**Output:** `meta-ads-conceitos-{{CLIENTE}}.md` (ver formato em `references/esc-start-output-formats.md`)

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

---

## Regras de Contexto (Inegociáveis)

1. **SEMPRE CONSOLIDAR** — Cada etapa produz um `.md` consolidado. Nunca passar output bruto.
2. **ICP É UNIVERSAL** — O `icp-consolidado-{{CLIENTE}}.md` vai para TODAS as etapas.
3. **MÍNIMO DE CONTEXTO** — Cada etapa recebe no máximo 2 arquivos: ICP + output anterior relevante.
4. **CHECKPOINT OBRIGATÓRIO** — Apresentar output e aguardar aprovação antes de avançar.
5. **NÃO INVENTAR DADOS** — Se falta info, PARAR e perguntar ao usuário.
6. **NAMING CONSISTENTE** — Todos os arquivos seguem: `[tipo]-{{CLIENTE}}.md`
7. **SEQUÊNCIA RESPEITADA** — Executar sempre na ordem: 1 → 2 → 3 → 4 → 5 → 6.

---

## Notas Operacionais

1. Se o pipeline for interrompido, pode ser retomado de qualquer etapa — basta ter os `.md` das etapas anteriores
2. Se o cliente tiver múltiplas marcas, processar uma marca por vez em cada etapa
3. O `icp-consolidado-{{CLIENTE}}.md` pode ser atualizado com feedback — nesse caso, considerar se etapas posteriores precisam ser refeitas
4. Este workflow funciona em qualquer agente que suporte as skills do repositório ESC Skills
