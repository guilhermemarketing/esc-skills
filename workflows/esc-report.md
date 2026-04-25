---
description: Pipeline de Análise & Report (v2) — ciclo de accountability pós-campanha. UTM Governance → Coleta de Dados (gmp-cli) → Executive Performance Report → Brandformance Planning* → Consent Mode Audit* → Conversion QA (post-implementation)*. Orquestra 5 skills + gmp-cli para fechar o loop de accountability com dados reais e decisões executivas.
---

# /esc-report — Pipeline de Análise & Report (v2)

Pipeline de **accountability pós-campanha** para clientes com operação ativa. Coleta dados reais de todas as plataformas, gera relatório executivo profit-first, audita compliance de consent e valida integridade do tracking. Ciclo recorrente (mensal/quinzenal) que garante que cada real investido é rastreado, analisado e decidido.

```
┌───────────────────────────────────────────────────────────────────────┐
│                  /esc-report v2 — Ciclo de Report                     │
│                                                                       │
│   [1] UTM Governance ──→ [2] Coleta (gmp-cli) ──→ [3] Report         │
│        (1x ou audit)          (automática)           Executivo        │
│                                                        │             │
│                                                        ▼             │
│                                                [3.5] Brandformance*  │
│                                                        │             │
│                                                        ▼             │
│                         [5] Conversion QA* ◄── [4] Consent*          │
│                              (re-audit)          Audit                │
│                                                                       │
│   * Etapas 3.5, 4, 5 opcionais — dependem de necessidade do cliente  │
└───────────────────────────────────────────────────────────────────────┘
```

## Filosofia

> **Profit-First > Métricas de Vaidade**
>
> O relatório abre com Unit Economics (CAC, LTV, ROI), não com CPM e CTR.
> Métricas operacionais são diagnóstico, não headline.

> **Dados → Decisões → Ações**
>
> Cada canal recebe um veredito (Escalar / Manter / Otimizar / Pausar).
> "Performance boa" sem baseline não é análise. "Melhorar performance" não é próximo passo.

> **Brandformance Flywheel**
>
> Branding não é vaidade — é o sinal que os algoritmos aprendem.
> Marca fraca = sinal fraco = algoritmo confuso = CAC alto.

---

## Pré-requisitos

Antes de iniciar o `/esc-report`, o cliente DEVE ter:

| Requisito | Por quê | Verificação |
|-----------|---------|-------------|
| Campanhas ativas (≥ 1 plataforma) | Sem dados, sem relatório | Account IDs disponíveis |
| GA4 configurado com dados | Base analytics | Property ID + ≥ 14 dias de dados |
| Acesso às plataformas de ads | Coleta de dados | Tokens/credenciais configurados |
| ICP definido | Contexto de negócio | `icp-consolidado-{{CLIENTE}}.md` |

**Se o cliente passou pelo `/esc-start`:** os pré-requisitos já estão atendidos. Usar `measurement-plan-{{CLIENTE}}.md` como blueprint.

**Se NÃO passou pelo `/esc-start`:** verificar manualmente e coletar IDs no intake.

---

## Pre-flight: Intake do Ciclo

Antes de cada iteração do relatório, coletar:

```yaml
intake:
  cliente: [Nome/slug — será {{CLIENTE}}]
  periodo_analise: [Ex: Abril/2026, Semana 14-20 Abril]
  periodo_comparacao: [Ex: Março/2026, Semana anterior] # opcional → modo Snapshot se ausente
  plataformas_ativas:
    - google_ads: [Customer ID]
    - meta_ads: [Account ID + Access Token]
    - linkedin_ads: [Account ID] # opcional
    - tiktok_ads: [Business ID] # opcional
    - pinterest_ads: [Advertiser ID] # opcional
  ga4_property_id: [G-XXXXX ou Property ID numérico]
  gsc_site_url: [https://site.com/] # opcional
  objetivo_negocio: [Leads, vendas, agendamentos, demos]
  unit_economics:
    ticket_medio: [R$]     # obrigatório para modo Completo
    ciclo_vendas: [dias]   # obrigatório para modo Completo
    ltv: [R$]              # obrigatório para modo Completo
    meta_cac: [R$]         # obrigatório para modo Completo
  crm_dados: [SQLs, vendas, receita real] # opcional
  iteracao: [primeira? recorrente?]
  mudancas_recentes: [novo pixel, nova CMP, mudança de LP, novo canal] # determina etapas 4-5
```

**Regras do Intake:**
- Buscar client memory em `~/.mcp-credentials/clients/{client-slug}.json` para IDs
- Se campos de Unit Economics estiverem ausentes, **insistir uma vez**. Se não fornecidos, operar em Modo Tático
- Se `measurement-plan-{{CLIENTE}}.md` existir, extrair IDs automaticamente
- Se houver mudanças recentes de tracking/CMP → ativar Etapas 4 e 5

---

## Etapa 1 — UTM Governance (Setup ou Auditoria)

**Skill:** `guimkt-utm-governance`

**Comportamento:** Na **primeira iteração**, executar setup completo (Etapas 0-5 da skill). Em **iterações subsequentes**, executar apenas auditoria rápida (Etapa 3 da skill).

### Modo A: Primeira Iteração (Setup)

**Input:** Respostas do intake + `measurement-plan-{{CLIENTE}}.md` (se existir)

**Execução:**
1. Invocar a skill `guimkt-utm-governance`
2. Executar **Etapa 0 — Intake** (plataformas, CRM, naming atual, WhatsApp)
3. Executar **Etapa 1 — Convenção de Naming** (source, medium, campaign taxonomia)
4. Executar **Etapa 2 — Templates por Plataforma** (URL Suffix com macros dinâmicos)
5. Executar **Etapa 3 — Auditoria** (GA4 Traffic Acquisition, CRM fields, plataformas)
6. Executar **Etapa 4 — Integração CRM** (hidden fields, gclid/fbclid, persistência)
7. Se WhatsApp é canal → Executar **Etapa 4.5 — WhatsApp-First**
8. Executar **Etapa 5 — Gerar Outputs**
9. Apresentar ao usuário → aprovação

**Output:** `utm-governance-{{CLIENTE}}.md` + `utm-governance-{{CLIENTE}}.html`

### Modo B: Iteração Recorrente (Auditoria Rápida)

**Input:** `utm-governance-{{CLIENTE}}.md` (do setup anterior) + acesso GA4

**Execução:**
1. Abrir GA4 Traffic Acquisition report
2. Verificar % de tráfego "(Unassigned)" — deve ser < 5%
3. Verificar se sources/mediums estão consistentes com a convenção
4. Verificar se campaigns recentes seguem o naming
5. Se inconsistências → listar e recomendar correção
6. Se tudo OK → marcar como "✅ UTMs compliance" e avançar

**Output:** Seção "UTM Health Check" no relatório executivo (Etapa 3)

**Checkpoint:** Aguardar aprovação antes de avançar.

---

## Etapa 2 — Coleta de Dados (gmp-cli + APIs)

**Skill:** `guimkt-gmp-cli-mcp-skill` (ferramenta de coleta)

**Objetivo:** Coletar dados brutos de todas as plataformas de forma automatizada.

### 2.1 Verificar Autenticação

```bash
gmp auth status
```

Se falhar → guiar o usuário para autenticar (`gmp auth login`).

### 2.2 Coleta por Plataforma

**Google Ads:**
```bash
gmp ads campaigns -c CUSTOMER_ID -r LAST_30_DAYS --status ENABLED -f json
gmp ads keywords -c CUSTOMER_ID --campaign "{{CAMPAIGN}}" -l 30 -f json
gmp ads search-terms -c CUSTOMER_ID -f json
```

**GA4:**
```bash
gmp ga report -p PROPERTY_ID -m sessions,totalUsers,conversions,bounceRate -d sessionSource -r 30d -f json
gmp ga report -p PROPERTY_ID -m sessions,conversions -d landingPage -r 30d -f json
gmp ga report -p PROPERTY_ID -m sessions,conversions -d deviceCategory -r 30d -f json
```

**Search Console:**
```bash
gmp gsc report -s "https://site.com/" -d query -l 20 -f json
gmp gsc report -s "https://site.com/" -d page -l 20 -f json
```

**Meta Ads** (via Graph API):
```bash
curl -s "https://graph.facebook.com/v21.0/{ad_account_id}/insights?\
fields=spend,reach,impressions,frequency,clicks,cpm,ctr,actions,cost_per_action_type,\
outbound_clicks,cost_per_outbound_click&\
time_range={URL_ENCODED_RANGE}&\
access_token=$META_ACCESS_TOKEN"
```

**LinkedIn Ads:** Solicitar dados manuais (CSV export) se API não disponível.

**TikTok / Pinterest:** Solicitar dados manuais (CSV export).

### 2.3 Fallback Manual

Se `gmp auth status` falhar ou dados não estiverem disponíveis via API:
- Aceitar dados colados em texto, CSV, PDF ou exports de plataforma
- Usar `docling` MCP para conversão de documentos se necessário
- Extrair métricas manualmente e normalizar

**Output:** Dados brutos coletados (em memória / variáveis do contexto — não salvar como arquivo separado)

> ⚠️ Não apresentar dados brutos ao usuário. Avançar direto para a análise (Etapa 3).

---

## Etapa 3 — Executive Performance Report

**Skill:** `guimkt-executive-performance-report`

**Objetivo:** Transformar dados brutos em decisões executivas com visão profit-first.

**Input:**
- Dados coletados na Etapa 2
- `icp-consolidado-{{CLIENTE}}.md` (contexto de negócio)
- Dados de Unit Economics do intake (ticket, ciclo, LTV, meta CAC)
- Dados de CRM (se disponíveis — SQLs, vendas, receita real)
- `utm-governance-{{CLIENTE}}.md` (para contexto de UTM health)

**Execução:**
1. Invocar a skill `guimkt-executive-performance-report`
2. Determinar **modo de operação**:
   - 🟢 Completo (ticket + ciclo + LTV + meta CAC) → Unit Economics reais
   - 🟡 Parcial (apenas ticket) → ROI estimado
   - 🔴 Tático (sem dados de negócio) → CPL como proxy + disclaimer
3. Executar **Etapa 2 — Normalização Cross-Platform** (tabela padronizada, hierarquia de métricas)
4. Executar **Etapa 3.1 — Resumo Executivo** (3-5 bullets profit-first)
5. Executar **Etapa 3.2 — Unit Economics Dashboard** (CAC, LTV, ROI, Payback, Margem)
6. Executar **Etapa 3.3 — Análise por Plataforma** (performance + anomalias + veredito)
7. Executar **Etapa 3.4 — Análise Flywheel** (Atrair → Engajar → Encantar)
8. Executar **Etapa 3.5 — Desperdício** (campanhas com CPL > 2x, frequência > 5, keywords sem conversão)
9. Executar **Etapa 3.6 — Oportunidades** (CPL baixo + budget limitado, remarketing subutilizado)
10. Executar **Etapa 3.7 — Decisões** (Escalar / Manter / Otimizar / Pausar por canal/campanha)
11. Executar **Etapa 3.8 — Próximos Passos** (7 / 30 / 90 dias — concretos, não vagos)
12. Incluir **UTM Health Check** da Etapa 1 (se Modo B)
13. Executar **Etapa 4 — Gerar Outputs** (Markdown + HTML premium)
14. Apresentar ao usuário → aprovação

**Output:**
- `executive-report-{{CLIENTE}}-{{YYYY-MM-DD}}.md`
- `executive-report-{{CLIENTE}}-{{YYYY-MM-DD}}.html`

**Checkpoint:** Aguardar aprovação do usuário. Avaliar se Etapa 3.5 (Brandformance) é relevante.

---

## Etapa 3.5 — Brandformance Planning (Condicional)

**Skill:** `guimkt-brandformance-planner`

**Condição:** Rodar quando:
- O cliente precisa decidir **mix de investimento branding vs. performance**
- Há budget significativo (> R$ 15k/mês) e dúvida sobre alocação awareness vs. conversão
- O relatório executivo (Etapa 3) revelou **CAC crescente** ou **dependência excessiva de performance**
- É a **primeira iteração** e o cliente nunca fez planejamento de brandformance
- O cliente questionou "devo investir em marca?" ou "awareness é vaidade?"

Se nenhuma condição for atendida → **pular para Etapa 4** (ou finalizar).

**Input:**
- `executive-report-{{CLIENTE}}-{{YYYY-MM-DD}}.md` (dados de performance reais)
- `icp-consolidado-{{CLIENTE}}.md` (contexto de negócio)
- Dados de Unit Economics do intake (ticket, ciclo, LTV, meta CAC)
- Dados de branded search, direct traffic, SOV (se disponíveis)

**Execução:**
1. Invocar a skill `guimkt-brandformance-planner`
2. Executar **Fase 1 — Brand Maturity Diagnostic** (escala 1-5: mental availability, physical availability, brand assets, branded search, SOV)
3. Executar **Fase 2 — Mix Recommendation** (% awareness vs. consideration vs. conversion baseado na maturidade)
4. Executar **Fase 3 — Cadência e Budget** (alocação mensal por fase do funil, cenários conservador/moderado/agressivo)
5. Executar **Fase 4 — KPIs por Fase** (separar métricas de brand de métricas de performance — nunca misturar)
6. Executar **Fase 5 — Brand Signals Map** (sinais que indicam se investimento em marca está funcionando: search lift, direct traffic, branded queries, SOV)
7. Executar **Fase 6 — Gerar Outputs** (Markdown + HTML premium)
8. Apresentar ao usuário → aprovação

**Output:**
- `brandformance-plan-{{CLIENTE}}-{{YYYY-MM-DD}}.md`
- `brandformance-plan-{{CLIENTE}}-{{YYYY-MM-DD}}.html`

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 4 — Consent Mode Audit (Condicional)

**Skill:** `guimkt-consent-mode-audit`

**Condição:** Rodar quando:
- É a **primeira iteração** do `/esc-report` para este cliente
- Houve **mudança de CMP, GTM, ou adição de nova tag** desde a última auditoria
- O último consent audit tem **mais de 3 meses**
- O relatório executivo revelou **anomalias de dados** que podem indicar consent issues

Se nenhuma condição for atendida → **pular para Etapa 5** (ou finalizar se Etapa 5 também for skip).

**Input:**
- URL do site/LP
- GTM Container ID
- Lista de tags configuradas
- `measurement-plan-{{CLIENTE}}.md` (se existir)
- `consent-audit-{{CLIENTE}}-anterior.md` (se existir — comparar com auditoria anterior)

**Execução:**
1. Invocar a skill `guimkt-consent-mode-audit`
2. Executar **Etapa 0 — Intake** (CMP, GTM, tags, sGTM, região)
3. Executar **Etapa 1 — Consent Mode v2** (detectar status, verificar default/update, 3 cenários)
4. Executar **Etapa 2 — CMP Review** (presença, certificação Google Partner, dark patterns)
5. Executar **Etapa 3 — Tags por Estado de Consent** (matriz de compliance, teste de disparos)
6. Executar **Etapa 4 — LGPD Compliance** (requisitos, dark patterns proibidos)
7. Executar **Etapa 5 — Data Retention** (GA4, Google Ads settings)
8. Se sGTM → Executar **Etapa 6 — Server-Side** (consent signals repassados)
9. Executar **Etapa 7 — Gerar Outputs** (score 0-100, 4 áreas)
10. Apresentar ao usuário → aprovação

**Output:**
- `consent-audit-{{CLIENTE}}-{{YYYY-MM-DD}}.md`
- `consent-audit-{{CLIENTE}}-{{YYYY-MM-DD}}.html`

**Checkpoint:** Aguardar aprovação do usuário.

---

## Etapa 5 — Conversion QA Re-Audit (Condicional)

**Skill:** `guimkt-conversion-qa-auditor` → **Modo 2: Post-Implementation**

**Condição:** Rodar quando:
- É a **primeira iteração** e nunca houve QA
- Houve **mudança de tags, LP, formulário, ou CRM** desde o último QA
- O consent audit (Etapa 4) revelou **issues críticos** que afetam tracking
- O relatório executivo (Etapa 3) revelou **discrepâncias de dados** entre plataformas
- O último QA tem **mais de 3 meses**

Se nenhuma condição for atendida → **finalizar o ciclo**.

**Input:**
- URL da LP publicada
- `measurement-plan-{{CLIENTE}}.md`
- `consent-audit-{{CLIENTE}}-{{YYYY-MM-DD}}.md` (se Etapa 4 rodou)
- `utm-governance-{{CLIENTE}}.md`

**Execução:**
1. Invocar a skill `guimkt-conversion-qa-auditor` no **Modo Post-Implementation**
2. Executar **Etapa 1 — Carregar Blueprint** (measurement plan)
3. Executar **Etapa 2 — Checklist QA** (dataLayer, GA4, conversions, consent, sGTM, UTMs)
4. Executar **Etapa 3 — Testes End-to-End** (formulário com UTMs, WhatsApp, consent)
5. Verificar se **UTMs da governança** estão chegando ao CRM
6. Verificar se **offline conversions pipeline** está funcionando
7. Executar **Etapa 4 — Scoring e Veredicto**
8. Apresentar ao usuário → aprovação

**Output:**
- `conversion-qa-{{CLIENTE}}-{{YYYY-MM-DD}}.md`
- `conversion-qa-{{CLIENTE}}-{{YYYY-MM-DD}}.html`

> ✅ **Pipeline completo.** Após a Etapa 5 (ou após a Etapa 3 se Etapas 4-5 forem skip), o ciclo de report está concluído. Agendar próxima iteração.

---

## Regras de Contexto (Inegociáveis)

1. **UNIT ECONOMICS PRIMEIRO** — Se dados de negócio disponíveis, relatório abre com CAC, LTV, ROI. Se não, disclaimer claro.
2. **PROFIT-FIRST** — "Escalar" só aparece quando ROI é positivo. Sem ROI, escalar = acelerar prejuízo.
3. **DECISÃO EM CADA CANAL** — Todo canal recebe veredito: Escalar / Manter / Otimizar / Pausar.
4. **DADOS REAIS** — Nunca inventar números. Se dado não existe, declarar "não disponível".
5. **GMP-CLI PRIMEIRO** — Sempre tentar coleta automática antes de pedir dados manuais.
6. **CHECKPOINT OBRIGATÓRIO** — Apresentar output e aguardar aprovação antes de avançar.
7. **NAMING CONSISTENTE** — Todos os arquivos: `[tipo]-{{CLIENTE}}-{{YYYY-MM-DD}}.md`
8. **SEM MÉTRICAS DE VAIDADE** — "Alcance cresceu 200%" sem correlação com leads/vendas NÃO entra no resumo.
9. **ANOMALIAS EXPLICADAS** — Toda variação > 20% precisa de hipótese.
10. **PRÓXIMOS PASSOS CONCRETOS** — "Melhorar performance" NÃO é próximo passo. "Pausar campanha X e realocar R$500/dia para Y" é.

---

## Mapa de Dependências de Arquivos

```
icp-consolidado-{{CLIENTE}}.md ──────────────┐ (contexto de negócio)
                                              │
measurement-plan-{{CLIENTE}}.md ──────┐       │
                                      │       │
                                      ▼       ▼
Etapa 1: UTM Governance ──→ utm-governance-{{CLIENTE}}.md
                                      │
Etapa 2: Coleta (gmp-cli) ──→ [dados em memória]
                                      │       │
                                      ▼       ▼
Etapa 3: Executive Report ──→ executive-report-{{CLIENTE}}-{{DATA}}.md
                              └──→ executive-report-{{CLIENTE}}-{{DATA}}.html
                                      │
Etapa 3.5: Brandformance* ──→ brandformance-plan-{{CLIENTE}}-{{DATA}}.md (condicional)
                                      │
Etapa 4: Consent Audit* ──→ consent-audit-{{CLIENTE}}-{{DATA}}.md (condicional)
                                      │
Etapa 5: Conversion QA* ──→ conversion-qa-{{CLIENTE}}-{{DATA}}.md (condicional)
```

---

## Cadência Recomendada

| Volume de Investimento | Frequência do Report | Etapas 4-5 |
|:----------------------:|:-------------------:|:----------:|
| > R$ 30k/mês | **Quinzenal** | Trimestral |
| R$ 10-30k/mês | **Mensal** | Trimestral |
| R$ 3-10k/mês | **Mensal** | Semestral |
| < R$ 3k/mês | **Bimestral** | Anual ou sob demanda |

---

## Notas Operacionais

1. **gmp-cli primeiro:** Sempre verificar `gmp auth status` antes de pedir dados manuais
2. **Client memory:** Buscar IDs em `~/.mcp-credentials/clients/{client-slug}.json`
3. **Token Meta:** Expira frequentemente — validar com `curl https://graph.facebook.com/v21.0/me?access_token=$TOKEN`
4. **Modo Comparativo é padrão:** Sempre comparar com período anterior. Modo Snapshot apenas no primeiro report
5. **Relatório anterior como baseline:** Se `executive-report-{{CLIENTE}}-anterior.md` existir, comparar tendências
6. **UTM audit mensal:** Verificar GA4 Traffic Acquisition → "(Unassigned)" < 5% como rotina
7. **Consent re-audit:** Após mudança de CMP, GTM, ou adição de tag nova
8. **QA re-audit:** Após mudança de LP, formulário, CRM, ou pipeline de offline conversions
9. **Branding como investimento:** Campanhas de awareness não são "desperdício" — avaliar com nuance no Flywheel. Usar `guimkt-brandformance-planner` (Etapa 3.5) para decisão estruturada
10. **Integração com /esc-cro:** Se o relatório identificar problemas de conversão, recomendar ciclo de `/esc-cro`
11. **Brandformance é decisão estratégica:** Não rodar Etapa 3.5 em todo ciclo — apenas quando há decisão de alocação brand vs. performance pendente
