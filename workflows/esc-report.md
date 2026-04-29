---
description: Pipeline de Análise & Report (v2) — ciclo de accountability pós-campanha. UTM Governance → Coleta de Dados (gmp-cli) → Executive Performance Report → Brandformance Planning* → Consent Mode Audit* → Conversion QA (post-implementation)*. Orquestra 5 skills + gmp-cli para fechar o loop de accountability com dados reais e decisões executivas.
---

# /esc-report — Pipeline de Análise & Report (v2)

Pipeline de **accountability pós-campanha** para clientes com operação ativa. Coleta dados reais, gera relatório executivo profit-first, audita compliance e valida tracking. Ciclo recorrente (mensal/quinzenal).

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

| Requisito | Por quê | Verificação |
|-----------|---------|-------------|
| Campanhas ativas (≥ 1 plataforma) | Sem dados, sem relatório | Account IDs disponíveis |
| GA4 configurado com dados | Base analytics | Property ID + ≥ 14 dias de dados |
| Acesso às plataformas de ads | Coleta de dados | Tokens/credenciais configurados |
| ICP definido | Contexto de negócio | `icp-consolidado-{{CLIENTE}}.md` |

**Se o cliente passou pelo `/esc-start`:** os pré-requisitos já estão atendidos. Usar `measurement-plan-{{CLIENTE}}.md` como blueprint.

---

## Pre-flight: Intake do Ciclo

Antes de cada iteração, coletar:

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

**Comportamento dual:**
- **Primeira iteração → Modo Setup:** Executar skill integralmente (Etapas 0-5). Output: `utm-governance-{{CLIENTE}}.md` + `.html`
- **Iterações seguintes → Auditoria Rápida:** Verificar GA4 Traffic Acquisition — "(Unassigned)" < 5%, sources/mediums consistentes, campaigns recentes conforme naming. Output: seção "UTM Health Check" no relatório.

**Checkpoint:** Aguardar aprovação.

---

## Etapa 2 — Coleta de Dados (gmp-cli + APIs)

**Skill:** `guimkt-gmp-cli-mcp-skill` (ferramenta de coleta)

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

**LinkedIn / TikTok / Pinterest:** Solicitar dados manuais (CSV export) se API não disponível.

### 2.3 Fallback Manual

Se `gmp auth status` falhar ou dados indisponíveis via API:
- Aceitar dados colados em texto, CSV, PDF ou exports de plataforma
- Extrair métricas manualmente e normalizar

**Output:** Dados em memória — não salvar como arquivo separado. Não apresentar dados brutos ao usuário.

---

## Etapa 3 — Executive Performance Report

**Skill:** `guimkt-executive-performance-report`

**Input:** Dados coletados (Etapa 2) + `icp-consolidado-{{CLIENTE}}.md` + Unit Economics do intake + CRM (se disponível) + `utm-governance-{{CLIENTE}}.md`
**Output:** `executive-report-{{CLIENTE}}-{{YYYY-MM-DD}}.md` + `.html`

Executar a skill integralmente. Determinar modo de operação automaticamente:
- 🟢 Completo (ticket + ciclo + LTV + meta CAC) → Unit Economics reais
- 🟡 Parcial (apenas ticket) → ROI estimado
- 🔴 Tático (sem dados de negócio) → CPL como proxy + disclaimer

**Checkpoint:** Aguardar aprovação. Avaliar se Etapa 3.5 (Brandformance) é relevante.

---

## Etapa 3.5 — Brandformance Planning (Condicional)

**Skill:** `guimkt-brandformance-planner`

**Condição — rodar quando:**
- Budget significativo (> R$ 15k/mês) e dúvida sobre alocação awareness vs. conversão
- Relatório executivo revelou **CAC crescente** ou **dependência excessiva de performance**
- Primeira iteração e cliente nunca fez planejamento de brandformance
- Cliente questionou "devo investir em marca?" ou "awareness é vaidade?"

Se nenhuma condição → **pular para Etapa 4** (ou finalizar).

**Input:** `executive-report-{{CLIENTE}}-{{YYYY-MM-DD}}.md` + `icp-consolidado-{{CLIENTE}}.md` + Unit Economics + branded search/SOV (se disponíveis)
**Output:** `brandformance-plan-{{CLIENTE}}-{{YYYY-MM-DD}}.md` + `.html`

Executar a skill integralmente (Fases 1-6).

**Checkpoint:** Aguardar aprovação.

---

## Etapa 4 — Consent Mode Audit (Condicional)

**Skill:** `guimkt-consent-mode-audit`

**Condição — rodar quando:**
- Primeira iteração do `/esc-report` para este cliente
- Mudança de CMP, GTM, ou adição de nova tag desde a última auditoria
- Último consent audit tem mais de 3 meses
- Relatório executivo revelou anomalias que podem indicar consent issues

Se nenhuma condição → **pular para Etapa 5** (ou finalizar).

**Input:** URL do site/LP + GTM Container ID + lista de tags + `measurement-plan-{{CLIENTE}}.md` (se existir)
**Output:** `consent-audit-{{CLIENTE}}-{{YYYY-MM-DD}}.md` + `.html`

Executar a skill integralmente (Etapas 0-7). Score 0-100 em 4 áreas.

**Checkpoint:** Aguardar aprovação.

---

## Etapa 5 — Conversion QA Re-Audit (Condicional)

**Skill:** `guimkt-conversion-qa-auditor` → **Modo Post-Implementation**

**Condição — rodar quando:**
- Primeira iteração e nunca houve QA
- Mudança de tags, LP, formulário, ou CRM desde o último QA
- Consent audit (Etapa 4) revelou issues críticos
- Relatório executivo revelou discrepâncias de dados entre plataformas
- Último QA tem mais de 3 meses

Se nenhuma condição → **finalizar o ciclo**.

**Input:** URL da LP + `measurement-plan-{{CLIENTE}}.md` + consent audit (se Etapa 4 rodou) + `utm-governance-{{CLIENTE}}.md`
**Output:** `conversion-qa-{{CLIENTE}}-{{YYYY-MM-DD}}.md` + `.html`

Executar a skill integralmente no Modo Post-Implementation. Verificar UTMs da governança no CRM e pipeline de offline conversions.

> ✅ **Pipeline completo.** Após a Etapa 5 (ou Etapa 3 se Etapas 4-5 forem skip), o ciclo de report está concluído. Agendar próxima iteração.

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
6. **Consent re-audit:** Após mudança de CMP, GTM, ou adição de tag nova
7. **QA re-audit:** Após mudança de LP, formulário, CRM, ou pipeline de offline conversions
8. **Branding como investimento:** Campanhas de awareness não são "desperdício" — avaliar com nuance. Usar Etapa 3.5 para decisão estruturada
9. **Integração com /esc-cro:** Se o relatório identificar problemas de conversão, recomendar ciclo de `/esc-cro`
10. **Brandformance é decisão estratégica:** Não rodar Etapa 3.5 em todo ciclo — apenas quando há decisão de alocação brand vs. performance pendente
