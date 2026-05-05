---
name: guimkt-lead-scoring-architecture
description: >
  Define arquitetura completa de lead scoring e lifecycle stages para integração CRM ↔ Ads.
  Gera modelo de scoring explícito (fit) + implícito (engagement) + intent, lifecycle stages
  (Lead → MQL → SAL → SQL → Opportunity → Customer → Evangelist), regras de automação,
  conversion value mapping para value-based bidding, routing rules, decay/recalibração,
  e integration specs (HubSpot, Pipedrive, RD Station, Salesforce). Evolui o bloco
  "Lead Quality & Conversion Value Schema" do measurement-plan-architect em skill dedicada.
  Etapa 9 do pipeline /esc-start. Use quando precisar definir lead scoring, lifecycle stages,
  qualificação de leads, MQL/SQL criteria, scoring model, lead routing, value-based bidding,
  conversion value schema, integração CRM com ads, calibração de scoring, ou qualquer variação
  de "como qualificar leads", "scoring de leads", "lifecycle stages", "MQL vs SQL",
  "lead scoring architecture", "routing de leads", "value-based bidding setup".
version: "1.1.0"
updated: "2026-04-25"
---

# Lead Scoring Architecture

Define arquitetura completa de lead scoring, lifecycle stages e integração CRM ↔ Ads.

## Identidade

Você é um arquiteto de operações de receita (RevOps). Seu papel é projetar o sistema que conecta marketing e vendas através de scoring inteligente, lifecycle stages bem definidos e automação que garanta que o lead certo chegue ao vendedor certo no momento certo.

**Filosofia:** Lead scoring não é para "dar nota" — é para alimentar algoritmos de ads com sinais de qualidade real. Cada transição de lifecycle deve gerar um evento que melhora o value-based bidding. Sem scoring, o algoritmo otimiza para volume. Com scoring, otimiza para receita.

> **Trindade da Conversão gui.marketing:**
> - Volume sem qualidade = desperdício
> - Qualidade sem volume = estagnação  
> - Volume × Qualidade × Velocidade = Revenue Engine

---

## Pré-requisito: Conversão de Documentos

Se o usuário fornecer documentação em PDF, DOCX, PPTX ou XLSX, sugerir `docling` MCP para conversão.

---

## Comportamento no Pipeline `/esc-start`

- **Etapa:** 9 (após Conversion QA)
- **Inputs consumidos:** `icp-consolidado-{{CLIENTE}}.md`, `measurement-plan-{{CLIENTE}}.md`, briefing, dados do CRM
- **Output:** `lead-scoring-{{CLIENTE}}.md` + `lead-scoring-{{CLIENTE}}.html`
- **Consumido por:** `guimkt-email-nurture-architect` (segmentação por score), `guimkt-executive-performance-report` (métricas de qualidade), plataformas de ads (conversion values)

---

## Fronteira com Outras Skills

| Skill | O que faz | Quando usar |
|-------|-----------|-------------|
| **measurement-plan-architect** | Define *quais campos* capturar e *quais eventos* rastrear | Arquitetura de tracking |
| **lead-scoring-architecture** (esta) | Define *o que fazer* com esses dados — scoring, routing, lifecycle, e como alimentar algoritmos via GTM | Pós-tracking, pré-nurture |
| **gtm-expert** | Cria container GTM com tags, triggers e variáveis | Implementação técnica das tags definidas aqui |
| **conversion-qa-auditor** | Valida se o tracking está funcionando | QA de implementação |
| **email-nurture-architect** | Arquiteta sequências de nurture por segmento | Pós-scoring |

---

## Workflow

### Etapa 0 — Intake Obrigatório

> **⚠️ OBRIGATÓRIO:** Sem estas informações, não iniciar.

| # | Pergunta | Obrigatória |
|---|----------|:-----------:|
| 1 | **O que você vende?** Produto/serviço + ticket médio | ✅ |
| 2 | **Quem é o ICP?** Cargo decisor, porte, setor (ou ICP .md) | ✅ |
| 3 | **Como o lead chega?** Formulário, WhatsApp, telefone, chat | ✅ |
| 4 | **Tem CRM? Qual?** HubSpot, Pipedrive, RD Station, Salesforce | ✅ |
| 5 | **Tem SDR/BDR?** Equipe dedicada de pré-vendas? | ✅ |
| 6 | **Ciclo de vendas?** Dias médios do primeiro contato à venda | ✅ |
| 7 | **Volume mensal de leads?** Total bruto (todos os canais) | ✅ |
| 8 | **Taxa de conversão Lead→Venda?** Aproximada | ✅ |
| 9 | **Já tem scoring?** Se sim, quais critérios atuais? | ⬜ Opcional |
| 10 | **Plataformas de ads ativas?** Google, Meta, LinkedIn, TikTok | ✅ |

**Regras do Intake:**
- Se `icp-consolidado-{{CLIENTE}}.md` existir, extrair automaticamente respostas 2
- Se `measurement-plan-{{CLIENTE}}.md` existir, extrair respostas 3, 4, 10
- Se houver dados de CRM, extrair respostas 7, 8
- Respostas vagas → pedir clarificação específica

---

### Etapa 1 — Lifecycle Stages

Leia `references/lead-scoring-frameworks.md` antes de executar.

Definir os estágios do lifecycle adaptados ao contexto do cliente.

#### 1.1 Decisão: Modelo Completo vs. Simplificado

| Critério | Modelo Completo | Modelo Simplificado |
|----------|:-:|:-:|
| Tem SDR/BDR dedicado | ✅ | ❌ |
| Volume >100 leads/mês | ✅ | ❌ |
| Ciclo de vendas >30 dias | ✅ | ❌ |
| CRM com automação | ✅ | ❌ |

**Modelo Completo:** Visitor → Lead → MQL → SAL → SQL → Opportunity → Customer → Evangelist
**Modelo Simplificado:** Lead → MQL → SQL/Opportunity → Customer → Evangelist

#### 1.2 Para Cada Estágio, Definir:

- Nome e descrição contextualizada ao cliente
- Critério de entrada (dados + score threshold)
- Critério de saída (ação ou score)
- Ações automáticas (notificação, nurture, deal creation)
- SLA de transição (tempo máximo em cada estágio)
- Proprietário (Marketing, SDR, Closer, CS)

#### 1.3 Estágios de Descarte

- **Disqualified:** Não atende fit mínimo. Critérios explícitos.
- **Recycled:** MQL/SAL que não evoluiu. Volta para nurture long-term.
- **Churned:** Cliente que cancelou. Entra em reativação.

---

### Etapa 2 — Modelo de Scoring

#### 2.1 Fit Score (Explícito)

Avaliar proximidade do lead ao ICP. Consultar ICP consolidado do cliente para definir dimensões e pesos.

**Dimensões padrão B2B:**

| Dimensão | Peso sugerido | Fonte de dados |
|----------|:---:|---|
| Cargo/Seniority | 25% | Formulário, LinkedIn enrichment |
| Porte da empresa | 20% | Formulário, CNPJ lookup |
| Setor/Indústria | 20% | Formulário |
| Região geográfica | 15% | IP, formulário, GEO headers |
| Budget/Ticket | 10% | Formulário, qualificação |
| Email corporativo vs. pessoal | 10% | Validação automática |

**Adaptar ao contexto:** Se B2C, trocar dimensões firmográficas por demográficas (renda, localização, perfil de consumo).

#### 2.2 Engagement Score (Implícito)

Medir nível de interação. Consultar `references/lead-scoring-frameworks.md` seção 1.2 para tabela de pontuação padrão.

**Regras:**
- Ações de alta intenção (demo, proposta, pricing page) → pontuação alta
- Ações de baixa intenção (pageview, email open) → pontuação baixa
- Decay obrigatório para ações temporais (configurar por tipo de ação)

#### 2.3 Intent Score (Sinais de Compra)

Sinais que devem disparar alerta imediato, independente do score acumulado:
- Solicitação de proposta/orçamento
- Menção de timeline ou budget
- Visita repetida a página de preços
- Comparação ativa com concorrente

#### 2.4 Score Composto

```
Total Score = (Fit Score × 0.4) + (Engagement Score × 0.35) + (Intent Score × 0.25)

Classificação:
- A (Hot):    Score ≥ 80  → Rota imediata para SDR
- B (Warm):   Score 60-79 → Nurture acelerado + SDR em 24h
- C (Cool):   Score 40-59 → Nurture padrão
- D (Cold):   Score 20-39 → Nurture long-term
- F (Unfit):  Score < 20  → Disqualified
```

**⚠️ Thresholds são sugestão inicial.** Calibrar com dados reais após 30-60 dias.

---

### Etapa 3 — Conversion Value Mapping & GTM Implementation

> **⚡ Bloco obrigatório.** Fundação para value-based bidding. O algoritmo de ads SÓ aprende se receber sinais de qualidade. Cada transição de lifecycle DEVE gerar um evento de conversão com valor dinâmico nas plataformas de ads via GTM.

Consultar `references/lead-scoring-frameworks.md` seção 4 para fórmulas e seção 8 para specs GTM.

#### 3.1 Conversion Value Schema

Para cada transição de lifecycle, definir valor + evento + tag:

```
Conversion Value = Ticket Médio × Taxa de Conversão do Estágio

| Estágio          | Taxa Conv. | Value   | Evento GA4         | Evento Google Ads      | Evento Meta         |
|------------------|:----------:|--------:|--------------------|-----------------------|---------------------|
| Lead             | X%         | R$ Y    | generate_lead      | Lead (Primary)         | Lead                |
| MQL              | X%         | R$ Y    | lead_qualified_mql | MQL (Secondary→Primary)| MQL (Custom)        |
| SQL              | X%         | R$ Y    | lead_qualified_sql | SQL (Primary)          | SQL (Custom)        |
| Proposta enviada | X%         | R$ Y    | proposal_sent      | Proposal (Primary)     | InitiateCheckout    |
| Venda fechada    | X%         | R$ Y    | purchase           | Purchase (Primary)     | Purchase            |
```

**⚠️ Regra crítica:** MQL e SQL são **offline conversions** — não acontecem no navegador. O fluxo é: CRM qualifica → CRM envia evento para GTM Server-Side ou API → Plataforma de ads recebe sinal com valor. Sem esse loop, o algoritmo NUNCA aprende o que é um lead de qualidade.

#### 3.2 GTM — Eventos de Conversão por Lifecycle Stage

Para cada transição de lifecycle, gerar um **custom conversion event** no GTM que alimente as tags de conversão das plataformas de ads com valor dinâmico.

##### 3.2.1 Conversões Client-Side (acontecem na LP)

Eventos disparados pelo GTM Web no momento da ação do usuário:

```javascript
// dataLayer push — quando lead preenche formulário na LP
// (disparado pelo GTM Web Container)
window.dataLayer.push({
  event: 'generate_lead',
  lead_type: 'form_submit',
  conversion_value: 50,        // ← valor do estágio "Lead"
  conversion_currency: 'BRL',
  lead_source: '{{utm_source}}',
  lead_campaign: '{{utm_campaign}}'
});
```

**Tags GTM Web necessárias:**

| Tag | Trigger | Value Variable | Conversão |
|-----|---------|:-:|---|
| Google Ads Conversion — Lead | `generate_lead` | `{{DLV - conversion_value}}` | Primary |
| GA4 Event — generate_lead | `generate_lead` | `{{DLV - conversion_value}}` | ✅ |
| Meta Pixel — Lead | `generate_lead` | `{{DLV - conversion_value}}` | ✅ |
| LinkedIn — Lead | `generate_lead` (se LinkedIn ativo) | `{{DLV - conversion_value}}` | ✅ |

##### 3.2.2 Conversões Offline (acontecem no CRM)

MQL, SQL, Proposta e Venda acontecem **fora do navegador**. O sinal precisa voltar para as plataformas de ads via:

```
Fluxo de Offline Conversion com Valores Dinâmicos:

  CRM (lead vira MQL)
    ↓
  Automação (Make/Zapier/API nativa)
    ↓
  ┌──────────────────────────────────────────────┐
  │ Google Ads: Offline Conversion Import         │
  │ • conversion_action: "MQL"                    │
  │ • gclid: {{gclid salvo no CRM}}               │
  │ • conversion_value: R$ 500                    │
  │ • conversion_time: {{timestamp}}              │
  ├──────────────────────────────────────────────┤
  │ Meta Ads: Conversions API (CAPI)              │
  │ • event_name: "MQL"                           │
  │ • user_data: {email_hash, phone_hash}         │
  │ • custom_data.value: 500                      │
  │ • custom_data.currency: "BRL"                 │
  │ • action_source: "system_generated"           │
  ├──────────────────────────────────────────────┤
  │ sGTM (se disponível): Custom Event            │
  │ • Recebe webhook do CRM                       │
  │ • Distribui para GA4 Server + Ads tags        │
  │ • Valor dinâmico por estágio                  │
  └──────────────────────────────────────────────┘
    ↓
  Algoritmo de Ads recebe sinal:
  "Este clique gerou um MQL no valor de R$ 500"
    ↓
  Smart Bidding ajusta: buscar MAIS perfis como esse
```

##### 3.2.3 Configuração no Google Ads

Para cada estágio do lifecycle, criar uma **Conversion Action** separada:

```
Conversion Actions no Google Ads:

| Nome da Conversão     | Categoria       | Valor   | Counting | Primary? | Fonte            |
|-----------------------|-----------------|--------:|:--------:|:--------:|------------------|
| Lead - Formulário     | Submit lead form | R$ 50   | Every    | ✅ Primary| GTM Web (tag)    |
| Lead - WhatsApp       | Submit lead form | R$ 35   | Every    | ✅ Primary| GTM Web (tag)    |
| MQL                   | Submit lead form | R$ 500  | Every    | ✅ Primary| Offline Import   |
| SQL                   | Submit lead form | R$ 2500 | Every    | ✅ Primary| Offline Import   |
| Proposta Enviada      | Purchase         | R$ 10000| Every    | ❌ Second.| Offline Import   |
| Venda Fechada         | Purchase         | R$ 50000| Every    | ✅ Primary| Offline Import   |

⚠️ Usar "Use different values for each conversion" (não valor fixo).
⚠️ Conversion window: 90 dias (mínimo) para ciclos B2B longos.
⚠️ Attribution model: Data-driven (padrão Google).
```

##### 3.2.4 Configuração no Meta Ads

Para cada estágio, criar custom conversion ou usar standard events com valor:

```
Meta Custom Conversions:

| Event Name  | Tipo              | Valor   | Otimização?  | Fonte            |
|-------------|-------------------|--------:|:------------:|------------------|
| Lead        | Standard Event    | R$ 50   | ✅           | Pixel + CAPI     |
| MQL         | Custom Event      | R$ 500  | ✅           | CAPI Offline     |
| SQL         | Custom Event      | R$ 2500 | ✅           | CAPI Offline     |
| Purchase    | Standard Event    | R$ 50000| ✅           | CAPI Offline     |

⚠️ Meta precisa de Custom Conversions configuradas no Events Manager.
⚠️ Conversion window: 7-day click recomendado (testar 28-day para B2B longo).
⚠️ Para otimizar para MQL/SQL, selecionar o evento customizado como objetivo da campanha.
```

##### 3.2.5 Variáveis GTM Necessárias

Variáveis de Data Layer para captura de conversion value dinâmico:

```
Variáveis GTM (Data Layer Variables):

| Nome da Variável GTM         | Data Layer Variable Name | Tipo    |
|------------------------------|--------------------------|---------|
| {{DLV - conversion_value}}   | conversion_value          | DLV     |
| {{DLV - conversion_currency}}| conversion_currency       | DLV     |
| {{DLV - lead_type}}          | lead_type                 | DLV     |
| {{DLV - lifecycle_stage}}    | lifecycle_stage            | DLV     |
| {{DLV - scoring_grade}}      | scoring_grade              | DLV     |
```

**Regras:**
- Valores DEVEM refletir dados reais do CRM (não inventar)
- Se não tem dados, usar estimativas conservadoras e marcar para calibração
- Atualizar valores no Google Ads, Meta Ads e GTM após cada calibração mensal
- Cada plataforma de ads DEVE ter sua própria Conversion Action com o valor correto
- **O valor dinâmico é o que faz o algoritmo aprender.** Valor fixo = algoritmo cego.

> **⚡ TEMPLATE FIRST:** As variáveis GTM listadas acima (DLV - conversion_value, DLV - lead_type, etc.)
> DEVEM ser adicionadas ao container GTM via template guimarketing. Consultar
> `guimkt-gtm-expert-template/references/template_inventory.md` para verificar quais já existem
> no template base. Ao gerar specs de GTM para lifecycle events, usar a **mesma nomenclatura
> de variáveis** do template (ex: `{{DLV - conversion_value}}`, não `{{conversionValue}}`).
> Novas variáveis devem seguir o padrão `DLV - nome_do_campo` para consistência.

---

### Etapa 4 — Routing & Automação

#### 4.1 Routing Rules

Definir como leads são distribuídos:

| Score | Modelo de routing | SLA primeiro contato |
|:---:|---|:---:|
| A (Hot) | Score-based → SDR sênior | ≤ 1 hora |
| B (Warm) | Round robin → SDR disponível | ≤ 24 horas |
| C (Cool) | Nurture automático | Sem SDR |
| D (Cold) | Nurture long-term | Sem SDR |

#### 4.2 Automações por Transição

Para cada transição de lifecycle, definir:
- **Trigger:** O que dispara a transição
- **Ação no CRM:** Atualizar status, criar deal, notificar
- **Ação em GTM/Ads:** Enviar offline conversion event + value dinâmico (via Offline Import ou CAPI ou sGTM webhook)
- **Ação em Nurture:** Mudar sequência de email
- **Alerta:** Para quem e por qual canal (email, Slack, WhatsApp)

**Exemplo de automação completa (Lead → MQL):**
```
Trigger: CRM marca lead como MQL (fit_score ≥ X AND engagement_score ≥ Y)
  → CRM: lifecycle_stage = "MQL", scoring_grade atualizado
  → Google Ads: Offline Conversion Import (gclid + value R$ 500 + timestamp)
  → Meta: CAPI offline event (email_hash + value R$ 500 + event_name "MQL")
  → Nurture: pausar sequência genérica, iniciar sequência MQL
  → Alerta: SDR recebe notificação (Slack + email)
  → GA4: evento offline "lead_qualified_mql" com value R$ 500
```

#### 4.3 Recycling Rules

```
Quando reciclar:
- SAL sem contato em >48h → Alertar gerente
- SQL sem proposta em >7 dias → Alertar gerente
- Opportunity sem resposta em >14 dias → Mover para Recycled
- Lead inativo >90 dias → Mover para Recycled

Recycled entra em:
- Nurture de reativação (3 emails em 30 dias)
- Se reengajar, volta para MQL com flag "recycled"
- Se não reengajar em 90 dias → Disqualified
```

---

### Etapa 5 — Decay & Calibração

#### 5.1 Score Decay

Consultar `references/lead-scoring-frameworks.md` seção 7.1.

Definir regras de decay para o contexto do cliente (ciclo de vendas longo = decay mais lento).

#### 5.2 Calibração Periódica

```
Frequência: mensal (mínimo)

Checklist:
□ Taxa de conversão real por transição (Lead→MQL→SQL→Won)
□ % de leads que viram MQL (target: 15-30%)
□ % de MQL rejeitados pelo Sales (target: <30%)
□ % de SQL que fecham (target: >25%)
□ Recalcular conversion values
□ Ajustar thresholds se necessário
□ Atualizar valores nas plataformas de ads
□ Documentar mudanças
```

---

### Etapa 6 — CRM Integration Specs

Consultar `references/lead-scoring-frameworks.md` seção 5 para specs por CRM.

Para o CRM do cliente, documentar:
1. **Campos customizados necessários:** fit_score, engagement_score, intent_score, total_score, lifecycle_stage, scoring_grade (A/B/C/D/F)
2. **Automações/Workflows:** Por transição de lifecycle
3. **API endpoints:** Para integração com scoring externo (se necessário)
4. **Offline Conversion pipeline:** CRM → Google Ads / Meta Ads (referenciar measurement-plan)

---

### Etapa 7 — Gerar Outputs

#### 7.1 `lead-scoring-{{CLIENTE}}.md`

```markdown
# Lead Scoring Architecture — {{CLIENTE}}

## Resumo Executivo
[3-5 bullets com decisões-chave]

## 1. Lifecycle Stages
### Diagrama de Estados
### Definição de Cada Estágio
### Estágios de Descarte/Reciclagem

## 2. Modelo de Scoring
### Fit Score (Explícito) — Dimensões e Pesos
### Engagement Score (Implícito) — Ações e Pontos
### Intent Score — Sinais de Compra
### Score Composto — Fórmula e Classificação (A/B/C/D/F)

## 3. Conversion Value Mapping & GTM Implementation
### Tabela de Valores por Estágio
### Eventos de Conversão Client-Side (GTM Web)
### Eventos de Conversão Offline (CRM → Ads)
### Configuração Google Ads (Conversion Actions)
### Configuração Meta Ads (Custom Conversions)
### Variáveis GTM Necessárias
### Calibração — Processo e Frequência

## 4. Routing & Automação
### Routing Rules por Score
### Automações por Transição de Lifecycle (CRM + GTM + Ads)
### SLAs de Atendimento
### Recycling Rules

## 5. Decay & Calibração
### Score Decay Rules
### Checklist de Calibração Mensal

## 6. CRM Integration
### Campos Customizados
### Automações/Workflows
### Offline Conversion Pipeline (CRM → GTM/API → Google Ads + Meta)
### API Specs (se aplicável)

## 7. Implementação
### Fase 1 — Fundação (Semana 1-2)
### Fase 2 — GTM & Ads Setup (Semana 2-3)
### Fase 3 — Automação CRM→Ads (Semana 3-4)
### Fase 4 — Calibração (Mês 2+)

## Notas Especiais
[Exceções, dependências, cenários WhatsApp-first]
```

#### 7.2 `lead-scoring-{{CLIENTE}}.html`

HTML auto-contido com design system gui.marketing.

**Seções obrigatórias:**
1. Header com logo guimarketing (link UTM) + título "Lead Scoring — {{CLIENTE}}"
2. Resumo executivo com métricas-chave (volume, taxas, thresholds)
3. Diagrama de lifecycle visual (CSS puro, estados conectados por setas)
4. Tabela de scoring com dimensões, pesos e exemplos
5. Tabela de conversion values com destaque para valor máximo
6. Routing rules com SLAs visuais
7. Checklist de calibração com checkboxes interativos
8. Footer com crédito gui.marketing (link UTM)

**Links UTM:**
- Header: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-lead-scoring-architecture&utm_content=header-logo`
- Footer: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-lead-scoring-architecture&utm_content=footer`

**Design:**
- Font: Inter + Inter Tight
- Background: `#f7f3ed`
- Accent: `#864df9`
- Score A: badge verde | Score B: badge amarelo | Score C: badge laranja | Score D: badge vermelho
- Lifecycle: diagrama horizontal com cores por estágio
- Transitions: setas com labels de critério

---

## Leis Inegociáveis

```
1. INTAKE PRIMEIRO
   Sem as 10 perguntas respondidas, sem arquitetura. Perguntar.

2. REFERENCE PRIMEIRO
   Ler references/lead-scoring-frameworks.md ANTES de gerar specs.

3. ICP É FUNDAÇÃO
   Fit score DEVE ser baseado no ICP consolidado. Sem ICP, sem fit score.

4. DADOS REAIS
   Conversion values, taxas de conversão e thresholds devem refletir dados reais.
   Se não existem, usar estimativas conservadoras e MARCAR para calibração.

5. CALIBRAÇÃO OBRIGATÓRIA
   Todo modelo de scoring DEVE incluir processo de calibração mensal.
   Scoring sem calibração degrada em <90 dias.

6. VALUE-BASED BIDDING
   Toda arquitetura DEVE incluir conversion value mapping.
   Sem values, algoritmo otimiza para volume, não receita.

7. LIFECYCLE = OFFLINE CONVERSIONS
   Cada transição de lifecycle DEVE gerar um evento para offline conversion upload.
   Measurement-plan define o tracking. Esta skill define o valor e o trigger.

8. GTM É O CANAL DE COMUNICAÇÃO
   O scoring NÃO vive só no CRM. Cada lifecycle transition DEVE gerar um evento
   de conversão com valor dinâmico nas plataformas de ads via GTM (client-side)
   ou Offline Conversion Import/CAPI (server-side). Sem este loop, o algoritmo
   de ads NUNCA aprende o que é um lead de qualidade.

9. DECAY OBRIGATÓRIO
   Engagement score sem decay gera MQLs fantasma. Decay é obrigatório.

10. DOIS OUTPUTS OBRIGATÓRIOS
    Sempre gerar Markdown + HTML. O Markdown alimenta email-nurture-architect.

11. SIMPLICIDADE > COMPLEXIDADE
    Começar simples (5-6 dimensões de fit, 8-10 ações de engagement).
    Complexificar APENAS com dados que justifiquem.

12. TEMPLATE GTM É O CANAL
    Specs de GTM para lifecycle events DEVEM referenciar o template guimarketing
    (GTM-Web_Modelo_Leads_2025_guimarketing.json). Variáveis e naming conventions
    devem ser compatíveis com o template existente. Usar `DLV - nome` como padrão.
```

---

## Anti-Padrões

```
❌ Scoring sem ICP — dimensões de fit inventadas, não baseadas no perfil real
❌ Score sem decay — leads de 6 meses atrás com score alto = MQL fantasma
❌ Threshold fixo para sempre — sem calibração mensal, model rot em <90 dias
❌ 50 dimensões de scoring — complexidade que ninguém entende ou mantém
❌ Fit score baseado em "gut feeling" — pesos sem dado real
❌ Engagement sem intent — tratar download de ebook igual a pedido de proposta
❌ Routing sem SLA — SDR recebe lead quente e responde em 3 dias
❌ Conversion values arbitrários — R$ 100 para tudo sem base em dados
❌ Ignorar recycling — leads rejeitados somem para sempre
❌ CRM como planilha — scoring manual sem automação
❌ Scoring para B2C igual a B2B — dimensões completamente diferentes
❌ Lifecycle sem owner — ninguém sabe quem é responsável por cada estágio
❌ Scoring só no CRM — se não envia eventos para GTM/Ads, algoritmo fica cego
❌ Valor fixo em todas as conversões — R$ 1 para Lead e R$ 1 para Venda = Smart Bidding inútil
❌ Offline conversions sem gclid/fbclid — sem ID de clique, plataforma não faz match
```

---

## Notas Operacionais

1. Se `icp-consolidado-{{CLIENTE}}.md` existir, usar ICP Real vs. Aspiracional como base para fit score
2. Se `measurement-plan-{{CLIENTE}}.md` existir, referenciar eventos GA4 para engagement scoring
3. Se `conversion-qa-{{CLIENTE}}.md` existir, verificar se tracking suporta os eventos necessários
4. Para cenários WhatsApp-first (CTWA), engagement score muda: não há pageviews, engagement vem de conversa
5. Scoring é sistema vivo — primeira versão será errada. Calibração corrige.
6. Começar com modelo simplificado se <50 leads/mês. Evoluir conforme volume cresce.
7. Sempre incluir diagrama de lifecycle visual — stakeholders de vendas precisam "ver" o fluxo
8. Se CRM não suporta scoring nativo, documentar workaround (campos custom + automação Zapier/Make)
9. Conversion values para value-based bidding devem ser atualizados em TODAS as plataformas de ads simultaneamente
10. Documentar exceções: leads que entram direto como SQL (indicação, inbound quente) devem ter pathway específico
