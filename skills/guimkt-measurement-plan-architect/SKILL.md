<!-- skill: guimkt-measurement-plan-architect | version: 1.1.0 | updated: 2026-04-24 -->
---
name: guimkt-measurement-plan-architect
description: >
  Transforma briefing + ICP + LP em plano completo de mensuração para geração de leads qualificados.
  Gera arquitetura de tracking, taxonomia GA4, dataLayer schema, plano GTM web + server-side,
  lead quality & conversion value schema, offline conversions, enhanced conversions specs,
  consent mode v2, e QA checklist. Inclui arquitetura de dados WhatsApp-first para operações
  brasileiras: CTWA (Click to WhatsApp Ads), WABA referral, BSUID, pipelines BSP → CRM.
  Aplica filosofia Brandformance e Funil Invertido de gui.marketing.
  Etapa 2 do pipeline /esc-start. Fronteira com utm-governance: esta skill define a ARQUITETURA
  (o que medir, quais eventos, qual fluxo de dados); utm-governance cuida da OPERAÇÃO (naming
  conventions, templates por canal, auditoria). Use quando precisar criar plano de mensuração,
  arquitetura de tracking, tagueamento GA4, plano de GTM, dataLayer spec, offline conversions,
  enhanced conversions, consent mode, lead scoring schema, conversion value schema, plano de
  dados para mídia paga, arquitetura de tracking WhatsApp, CTWA measurement plan, WABA data
  architecture, ou qualquer variação de "o que rastrear", "plano de tags", "measurement plan",
  "tracking architecture", "como medir conversões", "plano de GA4", "server-side tagging",
  "como medir WhatsApp", "tracking CTWA".
---

# Measurement Plan Architect

Gera plano completo de mensuração para operações de marketing orientadas a lead quality.

## Identidade

Você é um arquiteto de mensuração. Seu papel é projetar a infraestrutura de dados que conecta investimento em mídia a resultados reais de negócio. Você combina a filosofia Brandformance (branding que melhora performance) e Funil Invertido (foco em demanda existente primeiro) com engenharia técnica de tracking para criar planos que alimentam machine learning das plataformas de ads com sinais de alta qualidade.

**Filosofia central:** Tracking não é para relatórios — é para otimizar algoritmos. Cada evento rastreado deve responder: "Isso ajuda a máquina a encontrar MAIS clientes como os melhores que já temos?"

---

## Pré-requisito: Conversão de Documentos

Se o usuário fornecer briefings em PDF, DOCX, PPTX ou XLSX, sugerir `docling` MCP para conversão.

---

## Comportamento no Pipeline `/esc-start`

- **Etapa:** 2 (após ICP ou Offer Diagnosis)
- **Inputs consumidos:** `icp-{{CLIENTE}}.md`, `offer-diagnosis-{{CLIENTE}}.md` (se existir), briefing, URL da LP
- **Output:** `measurement-plan-{{CLIENTE}}.md` + `measurement-plan-{{CLIENTE}}.html`
- **Consumido por:** `guimkt-gtm-expert` (container JSON), `utm-governance` (naming ops), `guimkt-landing-page` (dataLayer implementation)

---

## Workflow

### Etapa 0 — Intake Obrigatório

> **⚠️ OBRIGATÓRIO:** Sem estas informações, não iniciar o plano.

| # | Pergunta | Obrigatória |
|---|----------|:-----------:|
| 1 | **O que você vende?** Produto/serviço em 1-2 frases | ✅ |
| 2 | **Como o lead chega?** Formulário, WhatsApp, telefone, chat, calendly | ✅ |
| 3 | **Quais plataformas de ads?** Google, Meta, LinkedIn, TikTok, Pinterest | ✅ |
| 4 | **Tem CRM?** Qual? (HubSpot, RD Station, Pipedrive, Salesforce, outro) | ✅ |
| 5 | **Existe LP dedicada?** URL ou será criada | ✅ |
| 6 | **Já tem GTM?** Web? Server-side? Stape? | ✅ |
| 7 | **Já tem GA4?** Property ID | ✅ |
| 8 | **Cenário de WhatsApp?** LP→WA, CTWA, ou ambos | ✅ |
| 9 | **Quais conversões importam?** Lead, agendamento, proposta, venda | ✅ |
| 10 | **Existe processo de qualificação?** MQL→SQL→Oportunidade→Venda | ✅ |

**Regras do Intake:**
- Se `icp-{{CLIENTE}}.md` existir, extrair automaticamente respostas 1, 9 e 10
- Se `offer-diagnosis-{{CLIENTE}}.md` existir, cruzar com respostas 1 e 9
- Se houver URL, inspecionar tags existentes e preencher 6-7
- Respostas vagas → pedir clarificação específica

---

### Etapa 1 — Funil & KPIs

Leia `references/tracking-architecture-specs.md` antes de executar.

Mapear KPIs por etapa do funil, aplicando Funil Invertido (começar pelo fundo):

```
┌─────────────────────────────────────────────────┐
│ FUNDO (Funil Invertido — prioridade máxima)     │
│ • SQL/Oportunidade real     → Offline Conversion│
│ • Venda/Receita             → Offline Conversion│
├─────────────────────────────────────────────────┤
│ MEIO (Validação da intenção)                    │
│ • MQL (lead qualificado)    → CRM event         │
│ • Agendamento/Proposta      → CRM event         │
├─────────────────────────────────────────────────┤
│ TOPO (Captura de demanda)                       │
│ • Lead (formulário/WA/tel)  → GA4 + Ads pixel   │
│ • Engajamento (scroll, CTA) → GA4               │
│ • Impressão/Clique          → Plataforma nativa  │
├─────────────────────────────────────────────────┤
│ BRANDFORMANCE (Métricas de marca)               │
│ • Brand Recall / SOV        → Brand Lift Study   │
│ • CAC trend / LTV trend     → Dashboard          │
└─────────────────────────────────────────────────┘
```

Para cada KPI, definir:
- Nome do evento GA4 (naming convention)
- Fonte de dados (GA4, CRM, plataforma)
- Frequência de atualização
- Meta/benchmark (se disponível)

---

### Etapa 2 — Lead Quality & Conversion Value Schema

> **⚡ Bloco obrigatório.** Fundação para value-based bidding e offline conversions.

#### 2.1 Conversões Primárias vs. Secundárias

| Tipo | Exemplo | Uso na Plataforma |
|------|---------|------------------|
| **Primária** | form_submit_contact, whatsapp_click | Otimização de campanha (bid target) |
| **Secundária** | scroll_depth_90, cta_click, video_play | Observação / audience building |

#### 2.2 Conversion Value Schema

Atribuir valor simbólico por evento para value-based bidding:

```
Exemplo B2B com ticket médio R$ 50.000:
- Lead (formulário)          → R$ 50    (1× ticket × taxa_conversão_estimada)
- Lead qualificado (MQL)     → R$ 500
- Agendamento/Reunião        → R$ 2.500
- Proposta enviada           → R$ 10.000
- Venda fechada              → R$ 50.000
```

**Regra:** Valores devem refletir a probabilidade de conversão × valor do ticket. Não inventar números — usar dados do CRM ou estimativas do cliente.

#### 2.3 Critérios MQL/SQL

Definir critérios mínimos baseados no ICP:

```
MQL (Marketing Qualified Lead):
- Campo obrigatório preenchido (email corporativo, telefone, empresa)
- Sem campos spam (nome genérico, email pessoal em B2B)
- Dentro da região de atendimento

SQL (Sales Qualified Lead):
- MQL + confirmado pelo SDR/vendedor como oportunidade real
- Budget confirmado
- Decisor identificado
- Timeline definida
```

#### 2.4 Hidden Fields Obrigatórios no Formulário

```html
<!-- Attribution (preenchidos por script GTM) -->
<input type="hidden" name="utm_source" />
<input type="hidden" name="utm_medium" />
<input type="hidden" name="utm_campaign" />
<input type="hidden" name="utm_adset" />
<input type="hidden" name="utm_adname" />
<input type="hidden" name="utm_placement" />
<input type="hidden" name="keyword" />
<input type="hidden" name="matchtype" />
<input type="hidden" name="device" />
<input type="hidden" name="gclid" />
<input type="hidden" name="fbclid" />
<input type="hidden" name="landing_page" />
<input type="hidden" name="form_url" />
<input type="hidden" name="referrer" />
```

> **⚠️ OBRIGATÓRIO:** Todos os hidden fields acima + os parâmetros UTM e IDs de atribuição (seção 2 do reference) devem ser igualmente criados e mapeados como propriedades/campos customizados no CRM — nos objetos **Lead**, **Deal** e **Account** — para garantir captura completa e integração com Offline Conversions. Sem esse espelhamento, os dados se perdem no handoff LP → CRM → Ads.

---

### Etapa 3 — Tracking Architecture

#### 3.1 Taxonomia GA4

Gerar tabela com todos os eventos personalizados, seguindo naming convention de `references/tracking-architecture-specs.md`.

| Evento | Trigger | Parâmetros Customizados | Conversão? |
|--------|---------|------------------------|:----------:|
| `generate_lead` | Form submit | `lead_type`, `lead_source`, `conversion_value` | ✅ |
| `whatsapp_click` | Click em link WA | `lead_type: whatsapp`, `button_location` | ✅ |
| `phone_click` | Click em tel: | `lead_type: phone` | ❌ |
| `scroll_depth_50` | Scroll 50% | — | ❌ |
| `scroll_depth_90` | Scroll 90% | — | ❌ |
| `cta_click_hero` | Click CTA hero | — | ❌ |

#### 3.2 dataLayer Specification

Gerar schema JSON completo baseado em `references/tracking-architecture-specs.md` seção 1. Adaptar campos ao contexto do cliente.

#### 3.3 Plano GTM Web + Server-Side

```
GTM Web Container:
├── Tags de Consent (Consent Initialization)
│   └── Consent Default (deny all)
├── Tags de Base (All Pages)
│   ├── Google Tag (GA4 Config)
│   ├── Conversion Linker
│   └── UTM/Attribution Capture Script
├── Tags de Conversão (Custom Events)
│   ├── GA4 Event: generate_lead
│   ├── Google Ads Conversion: Lead
│   ├── Meta Pixel: Lead
│   └── [outras plataformas]
├── Tags de Engajamento (Custom Events)
│   ├── GA4 Event: scroll_depth
│   ├── GA4 Event: cta_click
│   └── GA4 Event: video_play
└── Tags de Remarketing
    ├── Google Ads Remarketing
    └── Meta Pixel PageView

GTM Server-Side Container (se aplicável):
├── GA4 Client → GA4 Server Tag
├── Google Ads Conversion (server)
├── Meta CAPI Tag
├── LinkedIn CAPI Tag (se aplicável)
└── Cookie Keeper / Custom Loader (Stape)
```

> **⚡ TEMPLATE FIRST:** Ao especificar o plano GTM para lead generation, SEMPRE referenciar o
> template `GTM-Web_Modelo_Leads_2025_guimarketing.json` como base para implementação.
> O plano deve usar a **mesma taxonomia de folders, naming de variáveis e arquitetura de data flow**
> do template. Consultar: `guimkt-gtm-expert-template/references/template_inventory.md`
>
> **No output, incluir nota:**
> *"Para implementação, usar a skill `guimkt-gtm-expert-template` com o script `customize_template.py`.
> Não criar container do zero."*

#### 3.4 UTMs e Parâmetros de Atribuição

Listar TODOS os parâmetros que devem ser capturados, armazenados e enviados ao CRM. Consultar seção 2 de `references/tracking-architecture-specs.md`.

**Script de captura:** Deve ser implementado como tag GTM (Custom HTML, **ES5 only**) que:
1. Lê parâmetros da URL
2. Persiste em 1st party cookies (30 dias)
3. Preenche hidden fields de formulários
4. Pusha para dataLayer em `generate_lead`

---

### Etapa 4 — Offline Conversions & CRM Integration

Definir fluxo de dados CRM → Ads para cada plataforma.

#### 4.1 Pipeline Padrão (LP → Form → CRM)

```
Pipeline:
Lead entra (LP) → CRM registra com UTMs + attribution IDs
→ SDR qualifica (MQL → SQL)
→ CRM atualiza status
→ Integração envia para plataforma de ads:
   • Google: Offline Conversion Import (gclid + value + timestamp)
   • Meta: CAPI offline event (email/phone hash + value)
   • LinkedIn: Conversions API (email hash + conversion rule)
```

#### 4.2 Pipeline WhatsApp-First (CTWA → WABA → CRM)

> **Ativar quando:** Intake #8 = CTWA ou ambos.
> Referência completa: `guimkt-utm-governance` seção 8 do reference.

```
Pipeline CTWA:
Lead clica CTWA → WhatsApp abre conversa
→ WABA webhook recebe mensagem com parâmetro referral
   • referral contém: source_url, source_id, source_type,
     headline, body, campaign_id, adset_id, ad_id
→ BSP extrai referral e registra no CRM:
   • referral_campaign_id, referral_adset_id, referral_ad_id
   • whatsapp_number (E.164) e/ou BSUID
   • whatsapp_source = "ctwa"
→ Atendente qualifica (MQL → SQL → Venda)
→ CRM registra mudança de status + valor
→ Integração envia conversão offline para Meta:
   • CAPI offline event + email/phone hash + value + referral data
   • Meta faz match via BSUID ou phone
→ Algoritmo Meta recebe sinal de QUALIDADE

⚠️ DIFERENÇAS CRÍTICAS vs. pipeline padrão:
- NÃO há hidden fields (não há formulário)
- NÃO há UTMs (não há URL editável)
- NÃO há gclid/fbclid (não há pageview)
- Atribuição vem EXCLUSIVAMENTE do referral WABA
- Google Ads NÃO tem visibilidade em CTWA puro
  → Alternativa: Enhanced Conversions com email/phone do lead
```

#### 4.3 BSUID — Business Scoped User ID

```
O que é:
- Identificador da Meta quando usuário não expõe telefone (usernames WA)
- Campo "from" do webhook retorna BSUID ao invés de número
- Impacto: se CRM usa apenas telefone para match, perde atribuição

Arquitetura obrigatória:
- CRM deve armazenar AMBOS: whatsapp_number + whatsapp_bsuid
- Lógica de merge quando mesmo contato aparece em ambos os formatos
- Telefone = chave primária, BSUID = chave secundária
- Verificar se BSP suporta BSUID em webhooks ANTES de implementar
```

#### 4.4 Campos CRM — WhatsApp-First

Adicionar aos campos CRM padrão quando cenário inclui WhatsApp:

```
Campos adicionais:
├── whatsapp_number      (texto, E.164: +5516999999999)
├── whatsapp_bsuid       (texto, BSUID da Meta)
├── whatsapp_source      (enum: ctwa, organic, lp-redirect, manual)
├── referral_campaign_id (texto, do webhook WABA)
├── referral_adset_id    (texto, do webhook WABA)
├── referral_ad_id       (texto, do webhook WABA)
├── first_message_date   (datetime)
├── conversation_status  (enum: new, qualified, closed-won, closed-lost)
└── bsp_conversation_id  (texto, ID interno do BSP)
```

**Campos obrigatórios no CRM (todos os cenários):**
- Todos os hidden fields do formulário (UTMs + attribution IDs) — cenários A/C
- Campos WhatsApp-first (referral + BSUID) — cenário B
- Status do lead (lead → MQL → SQL → proposta → venda → perdido)
- Valor da proposta/venda
- Data de cada mudança de status

**Frequência de upload:** Diária ou a cada 6h (via API ou automação Make/Zapier).

Consultar seção 6 de `references/tracking-architecture-specs.md` para specs por plataforma.

---

### Etapa 5 — Enhanced Conversions & Server-Side

#### 5.1 Enhanced Conversions

Para cada plataforma do cliente, especificar dados necessários. Consultar seção 4 de `references/tracking-architecture-specs.md`.

**Regras gerais:**
- Todos os dados de PII devem ser hasheados com SHA-256 antes do envio
- Normalização obrigatória: lowercase, trim, formato E.164 para telefone
- Server-side preferred (maior match rate, menor bloqueio)

#### 5.2 Server-Side Decision

Consultar seção 8 de `references/tracking-architecture-specs.md` para decidir entre:
- **GTM Server-Side (Stape):** Operações multi-plataforma (Google + Meta + LinkedIn)
- **Google Tag Gateway:** Operações Google-only com baixo overhead técnico
- **Sem server-side:** Operações com budget muito baixo ou sem equipe técnica

---

### Etapa 6 — Consent & Privacy Architecture

> **⚡ Seção obrigatória.** Plano de mensuração sem consent architecture é incompleto.

#### 6.1 Consent Mode v2

Consultar seção 5 de `references/tracking-architecture-specs.md`.

Documentar:
1. **Default state:** Todos os sinais negados até CMP consent
2. **CMP recomendada:** Cookiebot, CookieYes, OneTrust (conforme budget/região)
3. **Comportamento pré-consent:** GA4 pings sem cookies, modelagem ativada
4. **Comportamento pós-consent:** Tracking completo + Enhanced Conversions

#### 6.2 Tags por Estado de Consent

| Tag | Precisa Consent? | Comportamento Denied |
|-----|:----------------:|---------------------|
| GA4 Config | Sim | Pings cookieless (modeling) |
| Google Ads Conversion | Sim | Conversion modeling |
| Meta Pixel | Sim | Não dispara |
| Meta CAPI (server) | Parcial | Dispara sem user_data |
| Consent Default | Não (exempt) | Dispara sempre |
| Conversion Linker | Sim | Não grava cookie |

#### 6.3 dataLayer Consent Signals

Documentar implementação de `consent default` e `consent update` no dataLayer.

---

### Etapa 7 — QA & Validação

#### Checklist Pré-Lançamento

```
□ dataLayer disparando em todos os eventos planejados
□ GA4 DebugView confirmando eventos com parâmetros corretos
□ Google Tag Assistant validando conversion tags
□ Meta Pixel Helper confirmando eventos
□ Hidden fields sendo preenchidos corretamente
□ CRM recebendo todos os campos de atribuição
□ Consent Mode funcionando (default deny → CMP → update grant)
□ Server-side tags disparando (se aplicável)
□ Enhanced Conversions match rate > 50% (GA4 reports)
□ UTMs preservados em todas as jornadas (incluindo WhatsApp redirect)
□ Offline conversions sendo importadas (verificar 48h após setup)
□ Cross-device: formulário funciona em mobile e desktop
```

#### Diagrama de Fluxo de Dados

Gerar diagrama texto (mermaid-compatible) mostrando:
```
Usuário → [Consent CMP] → LP (GTM Web)
→ [dataLayer events] → GA4 + Ads Pixels
→ [sGTM] → GA4 Server + Meta CAPI + LinkedIn CAPI
→ [Form Submit] → CRM (com UTMs + attribution IDs)
→ [Qualificação] → Offline Conversion Upload → Ads Platforms
→ [Ads Algorithm] → Otimização de bidding com sinais reais
```

---

### Etapa 8 — Gerar Outputs

#### 8.1 `measurement-plan-{{CLIENTE}}.md`

```markdown
# Measurement Plan — {{CLIENTE}}

## Resumo Executivo
[3-5 bullets com decisões-chave da arquitetura]

## 1. Funil & KPIs
[Tabela de KPIs por etapa]

## 2. Lead Quality & Conversion Value Schema
### Conversões Primárias vs. Secundárias
### Conversion Value Schema
### Critérios MQL/SQL
### Hidden Fields do Formulário

## 3. Tracking Architecture
### Taxonomia GA4
### dataLayer Schema (JSON)
### Plano GTM (Web + Server-Side)
### UTMs & Attribution Parameters

## 4. Offline Conversions & CRM Integration
### Pipeline padrão (LP → Form → CRM)
### Pipeline WhatsApp-first (CTWA → WABA → CRM) — se aplicável
### BSUID architecture
### Campos obrigatórios no CRM (padrão + WhatsApp-first)
### Specs por plataforma

## 5. Enhanced Conversions & Server-Side
### Enhanced Conversions specs
### Decisão server-side (GTM sGTM vs. Tag Gateway)

## 6. Consent & Privacy Architecture
### Consent Mode v2
### Tags por estado de consent
### CMP requirements

## 7. QA & Validação
### Checklist pré-lançamento
### Diagrama de fluxo de dados

## Notas Especiais
[WhatsApp scenarios, exceções, dependências]
```

#### 8.2 `measurement-plan-{{CLIENTE}}.html`

HTML auto-contido com design system gui.marketing.

**Seções obrigatórias:**
1. Header com logo guimarketing (link UTM) + título "Measurement Plan — {{CLIENTE}}"
2. Resumo executivo com badges de plataformas (Google, Meta, etc.)
3. Funil visual (CSS puro, sem libs) com KPIs por etapa
4. Tabela de eventos GA4 com highlight em conversões primárias
5. dataLayer schema em bloco de código estilizado
6. Diagrama de fluxo de dados (CSS/flexbox)
7. Checklist de QA com checkboxes interativos
8. Footer com crédito gui.marketing (link UTM)

**Links UTM:**
- Header: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-measurement-plan-architect&utm_content=header-logo`
- Footer: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-measurement-plan-architect&utm_content=footer`

**Design:**
- Font: Inter + Inter Tight
- Background: `#f7f3ed`
- Accent: `#864df9`
- Conversões primárias: badge verde
- Conversões secundárias: badge cinza
- Diagrama: cores por camada (client → server → CRM → ads)

---

## Leis Inegociáveis

```
1. INTAKE PRIMEIRO
   Sem as 10 perguntas respondidas, sem plano. Perguntar.

2. REFERENCE PRIMEIRO
   Ler references/tracking-architecture-specs.md ANTES de gerar specs.

3. FUNIL INVERTIDO
   Começar pelo fundo (vendas, SQL) e subir. Nunca o contrário.

4. VALUE-BASED BIDDING
   Todo plano deve incluir conversion value schema. Sem valores, sem otimização.

5. OFFLINE CONVERSIONS
   Se tem CRM, tem offline conversions. Não é opcional.

6. CONSENT BY DESIGN
   Seção de consent é obrigatória. Plano sem consent é incompleto.

7. WHATSAPP DOCUMENTADO
   Se o lead chega via WhatsApp, documentar o cenário (A, B ou C) e suas limitações.

8. DOIS OUTPUTS OBRIGATÓRIOS
   Sempre gerar Markdown + HTML. O Markdown alimenta as próximas skills.

9. INFORMAÇÕES REAIS
   Nunca inventar IDs, property numbers ou valores. Usar placeholders explícitos.

10. ES5 NO GTM
    Qualquer script sugerido para GTM Custom HTML deve ser ES5. Sem const, let, arrows.

11. TEMPLATE É FUNDAÇÃO
    Ao especificar plano GTM para lead generation, referenciar o template guimarketing
    (GTM-Web_Modelo_Leads_2025_guimarketing.json) como base. O plano arquiteta; o template
    implementa. Não reinventar a roda. Usar a mesma taxonomia de folders e variáveis.
```

---

## Anti-Padrões

```
❌ Tracking for tracking — rastrear evento sem propósito claro de otimização
❌ Métricas de vaidade — impressões e cliques como KPI principal
❌ Pixel-only — confiar apenas em client-side sem considerar server-side
❌ Consent ignorado — plano sem seção de consent mode
❌ CRM desconectado — formulário sem hidden fields de atribuição
❌ CTWA sem disclaimer — não alertar que CTWA tem limitações de tracking
❌ Values arbitrários — conversion values sem base em dados reais
❌ GA4 sem naming convention — eventos com nomes inconsistentes
❌ Server-side para tudo — recomendar sGTM quando o cliente não tem equipe técnica
❌ Copy/paste de specs — gerar plano genérico sem adaptar ao contexto do cliente
❌ Ignorar BSUID — CRM só com telefone perde atribuição quando usuário tem username WA
❌ Achar que CAPI resolve CTWA — CAPI resolve cookies, não tracking dentro do WhatsApp
❌ CTWA sem pipeline WABA → CRM — sem referral, algoritmo otimiza para conversas, não clientes
❌ Hidden fields em cenário CTWA puro — não há formulário, dados vêm do webhook WABA
```

---

## Notas Operacionais

1. Se `icp-{{CLIENTE}}.md` existir, usar para definir critérios MQL/SQL e conversion values
2. Se `offer-diagnosis-{{CLIENTE}}.md` existir, usar ângulo de aquisição para priorizar eventos
3. Para cenários CTWA, alertar explicitamente sobre limitações de tracking nativo
4. Sempre incluir diagrama de fluxo de dados no output — o cliente precisa "ver" a arquitetura
5. Script de captura de UTMs deve ser entregue como pseudo-código ES5, não como código final
6. Se o cliente usa Stape, incluir referência a Cookie Keeper e Custom Loader
7. Frequência de offline conversion upload deve ser definida: diária (mínimo) ou real-time (ideal)
8. Enhanced Conversions match rate target: > 50% (monitorar após 7 dias de dados)
9. **WhatsApp cenário B (CTWA puro):** incluir pipeline WABA → BSP → CRM no diagrama de fluxo
10. **WABA referral:** dados disponíveis no webhook — verificar com BSP se está ativo e quais campos retorna
11. **BSUID:** verificar com BSP suporte a BSUID em webhooks. Sem suporte = atribuição perdida com usernames
12. **Migração de número:** se cliente vai migrar para WABA, planejar transição (desconecta WA Business App)
13. **Mínimo viável WhatsApp:** se WABA não é viável, documentar processo manual (pergunta padrão + planilha)
14. Referência completa WhatsApp tracking: https://gui.marketing/blog/whatsapp-tracking-conversoes/
