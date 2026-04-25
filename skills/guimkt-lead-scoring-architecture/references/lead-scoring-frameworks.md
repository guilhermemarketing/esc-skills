# Lead Scoring & Lifecycle — Reference Frameworks

Especificações técnicas para o agente consultar durante a geração da arquitetura de lead scoring.

---

## 1. Modelos de Scoring

### 1.1 Scoring Explícito (Fit Score — Demográfico/Firmográfico)

Avalia o quão próximo o lead está do ICP. Baseado em dados **declarados** pelo lead ou enriquecidos por ferramentas.

```
Dimensões de Fit (pesos sugeridos para B2B):

| Dimensão          | Peso | Exemplos                              |
|-------------------|:----:|---------------------------------------|
| Cargo/Seniority   | 25%  | C-Level=100, Diretor=80, Gerente=60   |
| Porte da empresa  | 20%  | Enterprise=100, Mid=80, Small=40      |
| Setor/Indústria   | 20%  | Core=100, Adjacent=60, Off-target=10  |
| Região geográfica | 15%  | Atendível=100, Parcial=50, Fora=0    |
| Budget declarado   | 10%  | Alinhado=100, Abaixo=40, Não informou=20 |
| Email corporativo | 10%  | Corporativo=100, Pessoal=20           |
```

### 1.2 Scoring Implícito (Engagement Score — Comportamental)

Avalia o nível de engajamento e intenção do lead. Baseado em **ações rastreadas** (GA4, CRM, email).

```
Ações e Pontos (exemplo):

| Ação                          | Pontos | Decay? |
|-------------------------------|:------:|:------:|
| Visita à LP                   | +5     | 30d    |
| Scroll 90% da LP              | +10    | 30d    |
| Download de material          | +15    | 30d    |
| Assistir vídeo (>50%)         | +10    | 30d    |
| Abrir email de nurture        | +3     | 14d    |
| Clicar link no email          | +8     | 14d    |
| Visitar página de preços      | +20    | 14d    |
| Solicitar demo/reunião        | +50    | N/A    |
| Formulário de contato         | +40    | N/A    |
| WhatsApp click (LP)           | +35    | N/A    |
| Retorno ao site (>3 visitas)  | +15    | 30d    |
| Inatividade >30 dias          | -20    | N/A    |
| Inatividade >60 dias          | -40    | N/A    |
| Unsubscribe                   | -50    | N/A    |
| Bounce email                  | -30    | N/A    |
```

### 1.3 Scoring de Intent (Sinais de Compra)

Sinais de alta intenção que devem disparar alertas imediatos (não esperar acúmulo de score):

```
Sinais de Intent Imediato:
- Solicitação de proposta/orçamento
- Solicitação de demo/trial
- Menção de timeline ("precisamos para mês que vem")
- Menção de budget ("temos R$ X disponível")
- Pergunta sobre contrato/condições
- Comparação ativa com concorrente
- Visita repetida a página de preços (>3x em 7 dias)
```

---

## 2. Lifecycle Stages — Definições Padrão

### 2.1 Estágios Completos

```
┌─────────────────────────────────────────────────────────────────────┐
│ VISITOR                                                             │
│ Usuário anônimo. Sem dados. Apenas analytics.                       │
│ Critério de entrada: pageview                                       │
│ Critério de saída: preencher formulário ou iniciar conversa WA      │
├─────────────────────────────────────────────────────────────────────┤
│ LEAD                                                                │
│ Deu nome/email/telefone. Interesse declarado.                       │
│ Critério de entrada: form_submit OU whatsapp_click OU phone_click   │
│ Critério de saída: scoring atinge threshold MQL                     │
│ Ações: entrar em sequência de nurture, enriquecer dados             │
├─────────────────────────────────────────────────────────────────────┤
│ MQL (Marketing Qualified Lead)                                      │
│ Lead qualificado pelo marketing (fit + engagement acima do threshold)│
│ Critério de entrada: fit_score ≥ X AND engagement_score ≥ Y         │
│ Critério de saída: SDR aceita (→ SAL) ou rejeita (→ Lead/Recycled)  │
│ Ações: notificar SDR, pausar nurture genérico, iniciar nurture MQL  │
├─────────────────────────────────────────────────────────────────────┤
│ SAL (Sales Accepted Lead)                                           │
│ SDR aceitou o lead e iniciou contato.                               │
│ Critério de entrada: SDR marca como "aceito" no CRM                 │
│ Critério de saída: qualificação BANT/MEDDIC confirma oportunidade   │
│ SLA: contato em ≤ 24h após atribuição                               │
│ Ações: SDR faz discovery call                                       │
├─────────────────────────────────────────────────────────────────────┤
│ SQL (Sales Qualified Lead)                                          │
│ Oportunidade real confirmada pelo vendedor.                         │
│ Critério de entrada: BANT/MEDDIC confirmado pelo SDR/closer         │
│ Critério de saída: proposta enviada (→ Opportunity) ou descarte     │
│ Ações: criar deal/oportunidade no CRM                               │
├─────────────────────────────────────────────────────────────────────┤
│ OPPORTUNITY                                                         │
│ Proposta/orçamento enviado. Deal em pipeline.                       │
│ Critério de entrada: proposta enviada                               │
│ Critério de saída: closed-won (→ Customer) ou closed-lost           │
│ Ações: follow-up, negociação, revisão de proposta                   │
├─────────────────────────────────────────────────────────────────────┤
│ CUSTOMER                                                            │
│ Venda fechada. Cliente ativo.                                       │
│ Critério de entrada: contrato assinado / pagamento recebido         │
│ Critério de saída: churn (→ Churned) ou expansão (→ Evangelist)     │
│ Ações: onboarding, NPS, cross-sell/upsell                           │
├─────────────────────────────────────────────────────────────────────┤
│ EVANGELIST                                                          │
│ Cliente promotor. NPS 9-10 ou referral ativo.                       │
│ Critério de entrada: NPS ≥ 9 OU indicou ≥ 2 leads OU case publicado│
│ Ações: programa de referral, caso de sucesso, co-marketing          │
└─────────────────────────────────────────────────────────────────────┘

Estágios de descarte/reciclagem:
- DISQUALIFIED: Não atende critérios mínimos de fit. Nunca será MQL.
- RECYCLED: Foi MQL/SAL mas não evoluiu. Volta para nurture long-term.
- CHURNED: Era Customer mas cancelou/não renovou.
```

### 2.2 Estágios Simplificados (PME sem SDR)

Para operações menores sem SDR dedicado:

```
Lead → MQL → SQL/Opportunity → Customer → Evangelist

- Lead: formulário preenchido
- MQL: fit + engagement acima do threshold (automação ou revisão manual)
- SQL/Opportunity: vendedor confirma oportunidade e envia proposta
- Customer: venda fechada
- Evangelist: promotor ativo
```

---

## 3. Qualificação — Frameworks

### 3.1 BANT (Budget, Authority, Need, Timeline)

```
| Critério   | Pergunta-chave                          | Score |
|------------|------------------------------------------|:-----:|
| Budget     | Tem orçamento definido para isso?        | +25   |
| Authority  | É o decisor ou influenciador?            | +25   |
| Need       | Tem uma dor real que nossa solução resolve?| +25  |
| Timeline   | Tem prazo para implementar?              | +25   |
```

### 3.2 MEDDIC (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion)

```
Para vendas enterprise (ticket >R$ 50k):

| Critério          | Pergunta-chave                                |
|--------------------|-----------------------------------------------|
| Metrics           | Quais métricas de sucesso o cliente busca?     |
| Economic Buyer    | Quem assina o cheque?                          |
| Decision Criteria | Quais critérios de avaliação?                  |
| Decision Process  | Como é o processo de aprovação interno?        |
| Identify Pain     | Qual a dor específica e seu impacto financeiro?|
| Champion          | Quem internamente defende a solução?           |
```

### 3.3 CHAMP (Challenges, Authority, Money, Prioritization)

```
Para vendas consultivas:

| Critério        | Foco                                    |
|------------------|-----------------------------------------|
| Challenges      | Desafios antes do budget                 |
| Authority       | Mapeamento do comitê de decisão         |
| Money           | Budget e ROI esperado                    |
| Prioritization  | Onde isso fica na lista de prioridades?  |
```

---

## 4. Conversion Value Mapping — Para Value-Based Bidding

### 4.1 Fórmula Base

```
Conversion Value por estágio = Ticket Médio × Taxa de Conversão do Estágio

Exemplo B2B (ticket R$ 50.000, ciclo 90 dias):
- Lead (formulário)      → R$ 50.000 × 1/1000 = R$ 50
- MQL                    → R$ 50.000 × 1/100  = R$ 500
- SQL                    → R$ 50.000 × 1/20   = R$ 2.500
- Proposta enviada       → R$ 50.000 × 1/5    = R$ 10.000
- Venda fechada          → R$ 50.000 × 1/1    = R$ 50.000

Exemplo B2B PME (ticket R$ 5.000):
- Lead                   → R$ 5.000 × 3%   = R$ 150
- MQL                    → R$ 5.000 × 15%  = R$ 750
- SQL                    → R$ 5.000 × 40%  = R$ 2.000
- Venda                  → R$ 5.000 × 100% = R$ 5.000
```

### 4.2 Calibração

```
Regra de calibração (mensal):

1. Extrair do CRM: taxa de conversão real por estágio (últimos 90 dias)
2. Recalcular conversion values com taxas reais
3. Atualizar no Google Ads / Meta Ads
4. Comparar CAC por estágio vs. meta de CAC

Triggers de recalibração imediata:
- Taxa de MQL→SQL cai >20% em relação ao benchmark
- CAC sobe >30% sem aumento de volume
- Novo produto/serviço com ticket diferente
- Mudança significativa no ICP
```

---

## 5. CRM Integration Specs

### 5.1 HubSpot

```
Lifecycle Stages nativo:
subscriber → lead → marketing_qualified_lead → sales_qualified_lead → opportunity → customer → evangelist → other

Lead Scoring:
- HubSpot Score (padrão) — somar properties
- Predictive Lead Scoring (Enterprise) — ML nativo
- Custom Score Properties — até 25 scored properties

Automação:
- Workflows por lifecycle stage transition
- Deal pipeline linked a lifecycle
- Custom behavioral events (Marketing Hub Enterprise)

API:
- POST /crm/v3/objects/contacts — criar/atualizar
- PATCH /crm/v3/objects/contacts/{id} — update score
- POST /crm/v3/objects/deals — criar deal ao virar SQL
```

### 5.2 Pipedrive

```
Lifecycle via custom fields + pipeline stages:
Lead → Qualified → Contacted → Demo → Proposal → Negotiation → Won/Lost

Lead Scoring:
- Não nativo — usar campo customizado numérico
- Automação via Zapier/Make para calcular score
- LeadBooster add-on para scoring básico

Automação:
- Automations nativo para mover deals
- Webhooks para triggers externos
- Custom fields para scoring (fit + engagement)

API:
- POST /v1/persons — criar contato
- PUT /v1/persons/{id} — atualizar score
- POST /v1/deals — criar deal
- PUT /v1/deals/{id} — mover estágio
```

### 5.3 RD Station

```
Lifecycle via Lead Scoring nativo:
Lead → Qualified Lead → Client

Lead Scoring:
- Perfil (A/B/C/D) — fit score
- Interesse (1-4) — engagement score
- Critérios configuráveis na plataforma

Automação:
- Fluxos de automação por perfil×interesse
- Integração com CRM (Pipedrive, HubSpot, Salesforce)
- Segmentação por scoring para nurture

API:
- POST /platform/contacts — criar/atualizar
- PATCH /platform/contacts/{uuid} — update scoring
- Webhooks para lifecycle transitions
```

### 5.4 Salesforce

```
Lifecycle:
Lead Status → Opportunity Stage → Account

Lead Scoring:
- Einstein Lead Scoring (AI-native)
- Custom scoring via Process Builder/Flow
- Pardot (Marketing Cloud Account Engagement) — integração profunda

Automação:
- Flow Builder para lifecycle transitions
- Assignment Rules para routing
- Einstein Activity Capture para engagement auto

API:
- REST /services/data/v59.0/sobjects/Lead/ — criar
- REST /services/data/v59.0/sobjects/Opportunity/ — deal
- Bulk API para imports em massa
```

---

## 6. Routing Rules — Atribuição de Leads

### 6.1 Modelos de Routing

```
| Modelo         | Quando usar                         | Como funciona                    |
|----------------|--------------------------------------|----------------------------------|
| Round Robin    | Volume alto, equipe homogênea        | Distribui igualmente             |
| Territory      | Operação regional                    | Por região geográfica            |
| Skill-based    | Produtos diferentes, especialistas   | Por expertise do SDR             |
| Score-based    | Priorizar high-value leads           | Score alto → SDR sênior          |
| Hybrid         | Operações complexas                  | Combina território + score       |
```

### 6.2 SLA de Atribuição

```
Lead quente (score > threshold):
- Tempo máximo de atribuição: 5 minutos
- Tempo máximo para primeiro contato: 1 hora
- Alerta: email + Slack/Teams/WhatsApp para SDR

Lead morno (score médio):
- Tempo máximo de atribuição: 1 hora
- Tempo máximo para primeiro contato: 24 horas
- Alerta: email para SDR

Lead frio (score baixo):
- Entra em nurture automático
- Sem atribuição imediata a SDR
- Reavaliação após 30 dias ou novo engajamento
```

---

## 7. Decay & Recalibração

### 7.1 Score Decay (Perda de Pontos por Inatividade)

```
Regras padrão:
- Após 14 dias sem interação: -10% do engagement score
- Após 30 dias sem interação: -25% do engagement score
- Após 60 dias sem interação: -50% do engagement score
- Após 90 dias sem interação: mover para Recycled

Exceções:
- Fit score NUNCA decai (dados firmográficos não mudam)
- Intent signals não decaem (solicitou demo = flag permanente)
- Decay pausado durante feriados/períodos conhecidos de baixa atividade
```

### 7.2 Calibração Periódica

```
Frequência: mensal (mínimo) ou quinzenal (ideal)

Checklist de calibração:
□ Extrair do CRM: volume de leads por estágio nos últimos 30/60/90 dias
□ Calcular taxa de conversão real por transição (Lead→MQL, MQL→SQL, SQL→Won)
□ Comparar com taxas projetadas no scoring model
□ Ajustar thresholds se:
  - >60% dos leads viram MQL (threshold muito baixo)
  - <10% dos leads viram MQL (threshold muito alto)
  - >50% dos MQL são rejeitados pelo Sales (fit criteria precisa ajuste)
  - <20% dos SQL fecham (qualificação muito frouxa)
□ Recalcular conversion values para value-based bidding
□ Atualizar automações de routing se SLA não está sendo cumprido
□ Documentar mudanças e razões
□ Atualizar Conversion Actions no Google Ads com novos valores
□ Atualizar Custom Conversions no Meta Ads com novos valores
□ Validar que GTM Variables estão capturando valores corretos
```

---

## 8. GTM & Ads Platform Implementation Specs

### 8.1 dataLayer Schema — Eventos de Lifecycle

Cada transição de lifecycle deve gerar um push no dataLayer (client-side) ou um evento via API/webhook (server-side).

```javascript
// === CLIENT-SIDE (GTM Web) — Eventos na Landing Page ===

// Evento 1: Lead gerado (formulário submetido)
window.dataLayer.push({
  event: 'generate_lead',
  lead_type: 'form_submit',          // ou 'whatsapp_click', 'phone_click'
  conversion_value: 50,               // ← valor dinâmico do estágio
  conversion_currency: 'BRL',
  lead_source: 'google_ads',          // {{utm_source}}
  lead_medium: 'cpc',                 // {{utm_medium}}
  lead_campaign: 'search_brand',      // {{utm_campaign}}
  form_id: 'contact_form_hero',       // ID do formulário
  user_data: {                        // Para Enhanced Conversions
    email: '{{hashed_email}}',
    phone: '{{hashed_phone}}'
  }
});

// Evento 2: Lead WhatsApp (CTWA ou click direto)
window.dataLayer.push({
  event: 'generate_lead',
  lead_type: 'whatsapp_click',
  conversion_value: 35,               // ← WhatsApp geralmente tem valor menor (menos dados)
  conversion_currency: 'BRL',
  lead_source: '{{utm_source}}',
  lead_campaign: '{{utm_campaign}}'
});
```

```
// === SERVER-SIDE (Offline) — Eventos no CRM ===
// Estes NÃO passam pelo GTM Web. São enviados via:
// 1. Google Ads API (Offline Conversion Import)
// 2. Meta Conversions API (CAPI)
// 3. sGTM Webhook (se usando server-side GTM como hub)

// Evento MQL (CRM → Google Ads Offline Import)
{
  "gclid": "{{gclid_salvo_no_crm}}",
  "conversion_action": "MQL",
  "conversion_date_time": "2026-04-24T10:30:00-03:00",
  "conversion_value": 500,
  "currency_code": "BRL"
}

// Evento MQL (CRM → Meta CAPI)
{
  "event_name": "MQL",
  "event_time": 1745493000,
  "action_source": "system_generated",
  "user_data": {
    "em": ["{{sha256_email}}"],
    "ph": ["{{sha256_phone}}"],
    "fbc": "{{fbclid_cookie}}",
    "fbp": "{{fbp_cookie}}"
  },
  "custom_data": {
    "value": 500,
    "currency": "BRL",
    "lead_id": "{{crm_lead_id}}",
    "lifecycle_stage": "MQL"
  }
}

// Evento SQL (mesma estrutura, valor diferente)
{
  "event_name": "SQL",
  "conversion_value": 2500,
  // ... mesmos campos
}
```

### 8.2 Tags GTM Web — Configuração por Plataforma

```
=== Google Ads Conversion Tag ===

Tag: Google Ads Conversion Tracking
Trigger: Custom Event → generate_lead
Configuração:
  - Conversion ID: {{Google Ads Conversion ID}}
  - Conversion Label: {{Google Ads Conversion Label - Lead}}
  - Conversion Value: {{DLV - conversion_value}}     ← DINÂMICO
  - Currency Code: {{DLV - conversion_currency}}
  - Transaction ID: {{DLV - form_id}}_{{timestamp}}  ← dedup
  - Enhanced Conversions: ATIVO
    - Email: {{DLV - user_data.email}}
    - Phone: {{DLV - user_data.phone}}

⚠️ NUNCA usar valor fixo (hardcoded). Sempre referenciar variável de dataLayer.
⚠️ Cada estágio de lifecycle deve ter sua PRÓPRIA Conversion Action no Google Ads.

---

=== GA4 Event Tag ===

Tag: GA4 Event
Trigger: Custom Event → generate_lead
Configuração:
  - Event Name: generate_lead
  - Event Parameters:
    - value: {{DLV - conversion_value}}
    - currency: {{DLV - conversion_currency}}
    - lead_type: {{DLV - lead_type}}
    - lead_source: {{DLV - lead_source}}

---

=== Meta Pixel Tag ===

Tag: Custom HTML (Meta Pixel Event)
Trigger: Custom Event → generate_lead

fbq('track', 'Lead', {
  value: {{DLV - conversion_value}},
  currency: {{DLV - conversion_currency}},
  content_name: {{DLV - lead_type}}
});

⚠️ Para MQL/SQL, usar Meta CAPI (server-side), NÃO pixel client-side.
```

### 8.3 Variáveis GTM — Lista Completa

```
Data Layer Variables necessárias:

| Nome no GTM                    | DL Variable Name    | Tipo | Usado por                |
|--------------------------------|---------------------|------|--------------------------|
| {{DLV - conversion_value}}     | conversion_value    | DLV  | Todas as tags de conversão|
| {{DLV - conversion_currency}}  | conversion_currency | DLV  | Todas as tags de conversão|
| {{DLV - lead_type}}            | lead_type           | DLV  | GA4, Meta, relatórios    |
| {{DLV - lead_source}}          | lead_source         | DLV  | GA4, atribuição          |
| {{DLV - lead_medium}}          | lead_medium         | DLV  | GA4, atribuição          |
| {{DLV - lead_campaign}}        | lead_campaign       | DLV  | GA4, atribuição          |
| {{DLV - lifecycle_stage}}      | lifecycle_stage     | DLV  | Offline events           |
| {{DLV - scoring_grade}}        | scoring_grade       | DLV  | Segmentação por qualidade|
| {{DLV - form_id}}              | form_id             | DLV  | Dedup, tracking          |
| {{DLV - user_data.email}}      | user_data.email     | DLV  | Enhanced Conversions     |
| {{DLV - user_data.phone}}      | user_data.phone     | DLV  | Enhanced Conversions     |
```

### 8.4 Google Ads — Conversion Actions Setup

```
Conversion Actions a criar no Google Ads (por lifecycle stage):

| Nome                 | Action name          | Category         | Value    | Count | Primary? | Source          | Window |
|----------------------|----------------------|------------------|----------|:-----:|:--------:|-----------------|:------:|
| Lead - Formulário    | Lead_Form            | Submit lead form | Dynamic  | Every | ✅       | GTM Web Tag     | 90d    |
| Lead - WhatsApp      | Lead_WhatsApp        | Submit lead form | Dynamic  | Every | ✅       | GTM Web Tag     | 90d    |
| Lead - Telefone      | Lead_Phone           | Submit lead form | Dynamic  | Every | ✅       | GTM Web Tag     | 90d    |
| MQL                  | MQL                  | Submit lead form | Dynamic  | Every | ✅       | Offline Import  | 90d    |
| SQL                  | SQL                  | Submit lead form | Dynamic  | Every | ✅       | Offline Import  | 90d    |
| Proposta Enviada     | Proposal_Sent        | Purchase         | Dynamic  | Every | ❌       | Offline Import  | 90d    |
| Venda Fechada        | Purchase             | Purchase         | Dynamic  | Every | ✅       | Offline Import  | 90d    |

Configuração obrigatória:
- Value: "Use different values for each conversion" (NUNCA "Use the same value")
- Attribution model: Data-driven
- Include in "Conversions": YES para Primary, NO para Secondary
- Click-through window: 90 dias (B2B), 30 dias (B2C)
- Engaged-view window: 3 dias

Para Smart Bidding funcionar:
- Google Ads precisa de ~50 conversões/mês por Conversion Action (Primary)
- Se volume baixo, consolidar MQL+SQL em uma única Primary com valores diferentes
- Usar "Maximize conversion value" ou "Target ROAS" como bid strategy
```

### 8.5 Meta Ads — Custom Conversions Setup

```
Custom Conversions no Meta Events Manager:

| Event Name | Tipo            | Rule / Source    | Valor   | Otimizar? |
|------------|-----------------|------------------|---------|:---------:|
| Lead       | Standard Event  | Pixel + CAPI     | Dynamic | ✅        |
| MQL        | Custom Event    | CAPI Offline     | Dynamic | ✅        |
| SQL        | Custom Event    | CAPI Offline     | Dynamic | ✅        |
| Purchase   | Standard Event  | CAPI Offline     | Dynamic | ✅        |

Para otimizar campanhas para MQL/SQL:
1. Events Manager → Custom Conversions → Create
2. Selecionar "MQL" como custom event
3. Configurar valor padrão (fallback): R$ 500
4. Na campanha → Optimization goal → selecionar MQL ou SQL
5. Bid strategy: "Maximize value" ou "Target ROAS"

⚠️ Meta precisa de ~50 eventos/semana para sair do Learning Phase.
⚠️ Se volume baixo, otimizar para Lead (Pixel) e usar MQL como sinal secundário.
⚠️ Conversion window recomendado: 7-day click (testar 28-day para B2B longo).
```

### 8.6 sGTM — Webhook Hub Pattern

```
Se o cliente usa Server-Side GTM (sGTM via Stape ou GCP):

Fluxo: CRM → Webhook → sGTM → GA4 Server + Google Ads + Meta CAPI

1. CRM dispara webhook quando lifecycle muda:
   POST https://{{sgtm-server}}/webhook/lifecycle-event
   Body: {
     "event": "lifecycle_transition",
     "lifecycle_stage": "MQL",
     "conversion_value": 500,
     "currency": "BRL",
     "gclid": "{{gclid}}",
     "email": "{{email}}",
     "phone": "{{phone}}",
     "timestamp": "2026-04-24T10:30:00-03:00"
   }

2. sGTM Client → Custom Template recebe o webhook
3. sGTM Tags disparam em paralelo:
   - GA4 Server Tag → evento "lead_qualified_mql" com value
   - Google Ads Conversion Tag → offline conversion
   - Meta CAPI Tag → custom event "MQL"
   - (Opcional) LinkedIn CAPI, TikTok Events API

Vantagem do sGTM como hub:
- Um único webhook do CRM alimenta TODAS as plataformas
- Controle de consent no server-side
- Dedup e validação antes de enviar para plataformas
- Logs centralizados para debug
```

### 8.7 Pipeline de Automação CRM → Ads (sem sGTM)

```
Se o cliente NÃO usa sGTM, usar automação direta:

Opção A — Google Ads Offline Conversion Import (API)
1. CRM atualiza lifecycle stage
2. Zapier/Make/N8n captura webhook do CRM
3. Formata payload: {gclid, conversion_action, value, timestamp}
4. POST para Google Ads API: /v17/customers/{id}:uploadOfflineConversions
5. Google Ads recebe e treina Smart Bidding

Opção B — Google Ads Offline Conversion Import (Upload)
1. CRM exporta CSV com: gclid, conversion_action, value, timestamp
2. Upload manual ou via API no Google Ads
3. Frequência: diária (ideal) ou semanal (mínimo)

Opção C — Meta CAPI via Make/Zapier
1. CRM webhook → Make cenário
2. Make formata payload CAPI: {event_name, user_data, custom_data}
3. POST para Meta Graph API: /{pixel_id}/events
4. Meta recebe e treina ML

⚠️ Para Google Ads: GCLID é OBRIGATÓRIO. Sem gclid salvo no CRM, não há match.
⚠️ Para Meta: email_hash OU phone_hash é OBRIGATÓRIO. fbclid/fbc melhora match rate.
⚠️ Latência: enviar evento no MÁXIMO 24h após transição. Ideal: real-time via webhook.
```
