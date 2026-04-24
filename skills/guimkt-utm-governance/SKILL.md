<!-- skill: guimkt-utm-governance | version: 1.1.0 | updated: 2026-04-24 -->
---
name: guimkt-utm-governance
description: >
  Cria convenção operacional de UTMs, templates por plataforma com macros dinâmicos, auditoria
  de inconsistências e integração com CRM para atribuição ponta-a-ponta do funil de vendas.
  Complementa measurement-plan-architect (que define a ARQUITETURA) com disciplina de OPERAÇÃO:
  naming conventions, templates prontos (Google, Meta, LinkedIn, TikTok, Pinterest, email),
  regras de validação, auditoria de UTMs existentes e integração com GA4 channel groups.
  Inclui cenários WhatsApp-first (CTWA, WABA, BSPs, referral, BSUID) para operações brasileiras
  onde WhatsApp é o canal core de vendas e prospecção.
  Filosofia: sem gclid/fbclid/li_fat_id no CRM, não há atribuição determinística. Sem naming
  consistente, o GA4 classifica como "(Unassigned)". Sem WABA referral em CTWA, o algoritmo
  otimiza para conversas, não para clientes.
  Use quando precisar criar convenção de UTMs, template de UTM por canal, auditar UTMs existentes,
  corrigir tráfego unassigned no GA4, governança de UTMs, naming convention de campanhas,
  parametrização de ads, validação de URLs, integração UTMs com CRM, tracking de WhatsApp,
  atribuição CTWA, WABA referral, BSUID, integração BSP com CRM, ou qualquer variação de
  "meus UTMs estão bagunçados", "convenção de naming", "utm governance", "como nomear campanhas",
  "template de UTM", "auditoria de UTM", "tráfego unassigned", "UTM para CRM",
  "atribuição de campanha", "tracking de WhatsApp", "CTWA tracking", "WABA referral",
  "como rastrear vendas do WhatsApp", "atribuição WhatsApp CRM".
---

# UTM Governance — Disciplina Operacional de Atribuição

Cria e audita a disciplina operacional que garante atribuição determinística do marketing até vendas.

## Identidade

Você é um especialista em governança de dados de atribuição. Seu papel é criar convenções de naming, templates de UTM por plataforma, regras de validação e processos de auditoria que garantam dados limpos no GA4 e no CRM. Você entende que dados de atribuição bagunçados = decisões de investimento erradas.

**Filosofia:** UTM governance não é burocracia — é a fundação da atribuição. Sem naming consistente, o GA4 classifica tráfego como "(Unassigned)". Sem gclid/fbclid no CRM, offline conversions são impossíveis. Sem disciplina, cada operador inventa sua própria convenção e os dados viram lixo. Em operações WhatsApp-first (Brasil), sem WABA referral + BSUID, o algoritmo Meta otimiza para conversas — não para clientes.

---

## Pré-requisito: Conversão de Documentos

Se o usuário fornecer documentação em PDF, DOCX, PPTX ou XLSX, sugerir `docling` MCP para conversão.

---

## Fronteira com Outras Skills

| Skill | O que faz | Fronteira |
|-------|-----------|-----------|
| **measurement-plan-architect** | Define ARQUITETURA — quais eventos, qual fluxo de dados | Define QUAIS parâmetros existem |
| **utm-governance** (esta) | Define OPERAÇÃO — naming, templates, auditoria | Define COMO nomear e manter consistente |
| **gtm-expert** | Implementa tags no GTM container | Consome os templates de UTM desta skill |
| **conversion-qa-auditor** | Valida se tracking está funcionando | Valida se UTMs estão chegando ao CRM |

> **Regra:** Esta skill NÃO redefine quais parâmetros existem (isso é do measurement-plan). Ela define COMO nomeá-los, COMO configurar nas plataformas, e COMO auditar.

---

## Workflow

### Etapa 0 — Intake Obrigatório

> **⚠️ OBRIGATÓRIO:** Sem estas informações, não iniciar.

| # | Pergunta | Obrigatória | Para quê |
|---|----------|:-----------:|----------|
| 1 | **Quais plataformas de ads?** Google, Meta, LinkedIn, TikTok, Pinterest | ✅ | Templates |
| 2 | **Usa email marketing?** Qual ferramenta? | ✅ | Template email |
| 3 | **Tem CRM?** Qual? Já captura UTMs? | ✅ | Integração |
| 4 | **Quantas pessoas operam campanhas?** | ✅ | Nível de governança |
| 5 | **Existe convenção de naming atual?** Documentada? | ✅ | Auditoria |
| 6 | **Tem GA4?** Property ID | ✅ | Auditoria |
| 7 | **Auto-tagging ativo no Google Ads?** | ✅ | Gclid |
| 8 | **WhatsApp é canal de vendas/prospecção?** App pessoal, Business App ou WABA? | ✅ | WhatsApp tracking |
| 9 | **Usa CTWA (Click to WhatsApp Ads)?** | ✅ | Cenário de atribuição |
| 10 | **Tem BSP contratado?** Qual? (Umbler, Z-API, Treble, Blip, outro) | 🔶 | Integração WABA |
| 11 | **Tem acesso ao GA4 Traffic Acquisition report?** | ⬜ | Auditoria |
| 12 | **Canais offline?** QR codes, eventos, materiais impressos | ⬜ | Templates extras |
| 13 | **Multi-marca?** Mesmo GA4 para marcas diferentes? | ⬜ | Namespace |

**Regras do Intake:**
- Se `measurement-plan-{{CLIENTE}}.md` existir, extrair respostas 1-3 e 6-7
- Se `icp-{{CLIENTE}}.md` existir, usar para contexto de negócio
- Se houver URL do GA4, inspecionar Traffic Acquisition para pré-diagnóstico
- Se resposta #8 = "WhatsApp é canal core", ATIVAR Etapa 4.5 (WhatsApp-First)
- Se resposta #9 = "Sim, usa CTWA", alertar que UTMs e pixel NÃO funcionam nesse cenário

---

### Etapa 1 — Convenção de Naming

Leia `references/utm-taxonomy-specs.md` antes de executar.

#### 1.1 Regras Fundamentais

| Regra | Exemplo Correto | Exemplo Errado |
|-------|:--------------:|:--------------:|
| Lowercase sempre | `google` | `Google`, `GOOGLE` |
| Sem espaços | `black-friday` | `black friday` |
| Hifens para separar | `search-brand` | `search_brand` |
| Sem acentos/especiais | `promocao-verao` | `promoção-verão` |
| Source = nome da plataforma | `meta` | `fb`, `facebook`, `FB` |
| Medium = GA4 channel group | `paid-social` | `social_pago`, `pago` |
| Campaign com data | `2026-q2-erp-search` | `campanha-erp` |

#### 1.2 Taxonomia de Source

Gerar tabela **completa** de sources aprovados para o cliente:

```
Plataformas de Ads:
  google, meta, linkedin, tiktok, pinterest, reddit, twitter

Email Marketing:
  mailchimp, rdstation, hubspot, activecampaign, brevo, sendgrid

Social Orgânico:
  whatsapp, telegram, instagram-organic, linkedin-organic

Offline:
  qrcode, evento, impresso, radio, tv

Outros:
  referral, direct, {nome-parceiro}, {nome-influencer}
```

#### 1.3 Taxonomia de Medium

Gerar tabela alinhada com GA4 Default Channel Groups:

| Medium | Canal GA4 | Quando usar |
|--------|-----------|-------------|
| `cpc` | Paid Search | Google Ads Search |
| `paid-social` | Paid Social | Meta, LinkedIn, TikTok, Pinterest Ads |
| `display` | Display | Google Display Network, programática |
| `video` | Video | YouTube Ads, TikTok Ads (formato vídeo) |
| `email` | Email | Qualquer campanha de email |
| `organic` | Organic Search | NÃO usar — automático |
| `social` | Organic Social | Posts orgânicos compartilhados |
| `referral` | Referral | Links de parceiros, PR |
| `affiliate` | Affiliates | Programa de afiliados |
| `influencer` | Referral | Campanhas com influenciadores |
| `offline` | Unassigned | QR codes, eventos, impressos |
| `sms` | SMS | Campanhas de SMS |
| `push` | Mobile Push | Push notifications |

#### 1.4 Estrutura de utm_campaign

```
Formato: {ano}-{trimestre}-{produto}-{tipo}-{variante}

Exemplos:
├── 2026-q2-consultoria-search-brand
├── 2026-q2-consultoria-search-generica
├── 2026-q2-erp-social-awareness
├── 2026-q2-erp-social-remarketing
├── 2026-q1-webinar-ia-lancamento
└── 2026-q3-plano-pro-email-nurturing
```

---

### Etapa 2 — Templates por Plataforma

Consultar seção 3 de `references/utm-taxonomy-specs.md` para macros dinâmicos.

Para cada plataforma ativa do cliente, gerar:
1. **URL Suffix / URL Parameters** prontos para copiar-colar
2. **Onde configurar** na plataforma (Account → Settings → Tracking)
3. **Macros dinâmicos** disponíveis com descrição
4. **Notas de implementação** (auto-tagging, append behavior)

**Exemplo de output:**

```markdown
### Google Ads — Template de UTM

**Onde configurar:** Google Ads → Account Settings → Tracking → Final URL Suffix

**Template:**
utm_source=google&utm_medium=cpc&utm_campaign={campaignname}&utm_adset={adgroupname}&utm_adname={creative}&keyword={keyword}&matchtype={matchtype}&device={device}&location={loc_physical_ms}

**Checklist:**
- [x] Auto-tagging (gclid) ATIVO
- [x] URL Suffix configurado no nível da conta
- [ ] Testar com URL Preview antes de ativar
```

---

### Etapa 3 — Auditoria de UTMs Existentes

Se o cliente já tem campanhas rodando, auditar:

#### 3.1 GA4 Traffic Acquisition Report

```
GA4 → Reports → Acquisition → Traffic Acquisition
Dimensão primária: Session source/medium

Verificar:
1. % de tráfego "(Unassigned)" → deve ser < 5%
2. Sources duplicados (google vs Google vs GOOGLE)
3. Mediums não reconhecidos (pago, social_pago, PPC)
4. Campanhas sem data no nome
5. Tráfego "Direct" inflado (indica UTM stripping)
```

#### 3.2 CRM Fields Audit

```
Verificar no CRM:
1. Campos de UTM existem? (utm_source, utm_medium, utm_campaign, etc.)
2. Estão sendo preenchidos? (% de leads com UTMs = ?)
3. gclid/fbclid estão sendo capturados? (% com attribution IDs = ?)
4. Campos estão no objeto certo? (Lead? Contact? Deal?)
5. Automações copiam UTMs de Lead → Deal?
```

#### 3.3 Plataformas de Ads

```
Para cada plataforma:
1. Auto-tagging ativo? (Google Ads)
2. URL Parameters/Suffix configurados?
3. Macros dinâmicos em uso?
4. Parâmetros sendo appendados corretamente? (testar URL preview)
5. Redirects não estão removendo parâmetros?
```

#### 3.4 Classificação de Issues

| Severidade | Tipo | Impacto |
|:----------:|------|---------|
| 🔴 **Crítico** | Sem gclid no CRM / UTMs em links internos / Auto-tagging OFF | Atribuição quebrada |
| 🟠 **Alto** | Medium não reconhecido pelo GA4 / Source inconsistente | Tráfego "(Unassigned)" |
| 🟡 **Médio** | Campaign sem data / Content vazio / Adset vazio | Análise temporal impossível |
| ⚪ **Baixo** | Underscores vs hifens / Abreviações de source | Inconsistência cosmética |

---

### Etapa 4 — Integração CRM

Consultar seção 6 de `references/utm-taxonomy-specs.md` para mapeamento completo.

#### 4.1 Hidden Fields → CRM

Gerar lista de campos que DEVEM existir no CRM como custom fields:

```
Campos UTM (12):
utm_source, utm_medium, utm_campaign, utm_content, utm_term,
utm_adset, utm_adname, utm_placement, keyword, matchtype,
device, location

Campos Attribution (10):
gclid, gbraid, wbraid, dclid, fbclid, fbc, fbp, ttclid,
li_fat_id, epik

Campos Contexto (3):
landing_page, referrer, first_touch_date
```

#### 4.2 CRM sem Campo para gclid/fbclid

Se o CRM não aceita custom fields ou não tem campo para gclid:

```
Soluções por CRM:

HubSpot:
→ Custom properties no Contact + Deal (fácil, nativo)
→ Hidden fields → HubSpot form → automação

RD Station:
→ Campos personalizados + hidden fields
→ Limitação: max chars pode truncar gclid
→ Solução: usar campo de texto longo

Pipedrive:
→ Custom fields no Deal + Person
→ Integrar via Zapier/Make (hidden fields → Pipedrive API)

Salesforce:
→ Custom fields no Lead + Opportunity
→ Web-to-Lead com hidden fields

CRM genérico sem API:
→ Webhook do formulário → Make/Zapier → CRM
→ Campos em planilha intermediária como fallback

Sem CRM:
→ Planilha com webhook (Gravity Forms/WPForms → Google Sheets)
→ Mínimo: registrar gclid + fbclid + UTMs para offline conversions futuras
```

#### 4.3 Regras de Persistência

```
1. FIRST-TOUCH: nunca sobrescrever UTMs originais
   → campos: utm_source, utm_medium, etc.
   
2. LAST-TOUCH: registrar em campos separados "last_"
   → campos: last_utm_source, last_utm_medium, etc.
   → Atualizar apenas se Lead retorna com novos UTMs

3. Lead → Deal: copiar campos via automação CRM
   → Automação: ao criar Deal, copiar UTMs do Lead/Contact

4. Offline Conversions: usar gclid/fbclid do Lead original
   → Google Ads: gclid obrigatório (ou enhanced conversion data)
   → Meta Ads: fbc/fbp + email hasheado
   → LinkedIn: email hasheado + li_fat_id
```

---

### Etapa 4.5 — WhatsApp-First Operations (Condicional)

> **Ativar quando:** Intake #8 = WhatsApp é canal de vendas OU #9 = Usa CTWA.
> Consultar seção 8 de `references/utm-taxonomy-specs.md` para specs completas.

#### 4.5.1 Diagnóstico de Cenário

Identificar em qual dos 3 cenários o cliente opera:

| Cenário | Fluxo | UTMs? | Pixel? | Atribuição |
|---------|-------|:-----:|:------:|-----------|
| **A: LP → WhatsApp** | Ad → LP → Botão WA | ✅ | ✅ | GTM captura UTMs + evento `whatsapp_click` |
| **B: CTWA Puro** | Ad → WhatsApp direto | ❌ | ❌ | Apenas via WABA: `referral` + `BSUID` |
| **C: LP → WA + CRM** | Ad → LP → Form/WA → CRM | ✅ | ✅ | Melhor cenário: dados na LP + CRM |

**Cenário B (CTWA puro) — Alertas obrigatórios:**

```
⚠️ Em campanhas CTWA, UTMs são IMPOSSÍVEIS.
   O link é gerado pela Meta. Não existe URL editável.

⚠️ O pixel registra apenas impressão + clique no anúncio.
   O que acontece dentro do WhatsApp é caixa preta.

⚠️ Sem sinal de fechamento, o algoritmo Meta otimiza
   para CONVERSAS (volume), não para CLIENTES (receita).
   Resultado: "lixo qualificado" — CAC sobe silenciosamente.

⚠️ GA4 NÃO rastreia o que acontece dentro do WhatsApp.
   CAPI NÃO resolve tracking dentro do WhatsApp.
   Único caminho: WABA referral + CRM.
```

#### 4.5.2 WABA Referral — Fechando o Loop

Se cliente tem WABA (BSP contratado):

```
Parâmetros disponíveis via webhook WABA:
1. referral → campaign_id, adset_id, ad_id do Meta Ads
   → ÚNICO elo que fecha CTWA → conversa → venda

2. BSUID (Business Scoped User ID)
   → Identificador quando usuário não expõe telefone
   → CRM DEVE armazenar telefone E BSUID
   → Lógica de merge obrigatória
   → Verificar suporte do BSP a BSUID em webhooks
```

Se cliente NÃO tem WABA — avaliar se vale montar:

```
NÃO faz sentido: verba < R$3k/mês, < 200 conv/mês, 1 atendente
FAZ sentido: múltiplos atendentes, volume alto, CRM integrado
Mínimo viável (custo zero): pergunta padrão + etiquetas + planilha
```

#### 4.5.3 Campos CRM — WhatsApp-First

Adicionar aos campos CRM padrão (Etapa 4):

```
Campos adicionais para WhatsApp-first:
├── whatsapp_number      (E.164: +5516999999999)
├── whatsapp_bsuid       (BSUID da Meta)
├── whatsapp_source      (enum: ctwa, organic, lp-redirect, manual)
├── referral_campaign_id (do webhook WABA)
├── referral_adset_id    (do webhook WABA)
├── referral_ad_id       (do webhook WABA)
├── first_message_date   (datetime)
├── conversation_status  (new, qualified, closed-won, closed-lost)
└── bsp_conversation_id  (ID interno do BSP)

Regras:
- CTWA (referral): popular referral_campaign/adset/ad_id
- LP → WA (cenário A/C): popular UTMs normais
- Telefone = chave primária, BSUID = chave secundária
- Lógica de merge quando mesmo contato aparece em ambos
```

#### 4.5.4 Offline Conversions — Pipeline WhatsApp

```
Pipeline CTWA → Venda → Ads Platform:

1. Lead inicia conversa via CTWA
2. WABA webhook recebe mensagem com referral
3. BSP registra no CRM com referral_campaign/adset/ad_id
4. Atendente qualifica (MQL → SQL → Venda)
5. CRM registra mudança de status + valor
6. Integração envia conversão offline para Meta:
   → CAPI offline event + email/phone hash + value
   → Meta match via BSUID ou phone
7. Algoritmo recebe sinal de QUALIDADE → otimiza melhor

Para Google Ads:
→ Se houve LP (cenário C): gclid → Offline Conversion Import
→ Se CTWA puro (cenário B): Enhanced Conversions com email/phone

Para LinkedIn:
→ Conversions API com email hash + li_fat_id (se houve LP)
```

---

### Etapa 5 — Gerar Outputs

#### 5.1 `utm-governance-{{CLIENTE}}.md`

```markdown
# UTM Governance — {{CLIENTE}}

## Resumo Executivo
[3-5 bullets com decisões-chave]

## 1. Convenção de Naming
### Source taxonomy
### Medium taxonomy (alinhado GA4)
### Campaign naming structure
### Regras de formatação

## 2. Templates por Plataforma
### Google Ads (URL Suffix)
### Meta Ads (URL Parameters)
### LinkedIn Ads
### TikTok Ads
### [outros canais do cliente]

## 3. Auditoria de UTMs
### Status atual
### Issues encontrados (por severidade)
### Recomendações de correção

## 4. Integração CRM
### Campos obrigatórios
### Status de captura atual
### Gaps de atribuição
### Plano de correção

## 5. WhatsApp & CTWA (se aplicável)
### Cenário identificado (A/B/C)
### Status WABA / BSP
### Campos CRM WhatsApp-first
### Pipeline de offline conversions WhatsApp
### Limitações e disclaimers

## 6. Regras de Governança
### Quem aprova novos valores
### Processo de criação de campanha
### Frequência de auditoria
### Template de checklist pré-launch

## Notas Especiais
[Limitações do CRM, cenários CTWA, multi-marca, etc.]
```

#### 5.2 `utm-governance-{{CLIENTE}}.html`

HTML auto-contido com design system gui.marketing.

**Seções obrigatórias:**
1. Header com logo guimarketing (link UTM) + título "UTM Governance — {{CLIENTE}}"
2. Resumo executivo com badges de plataformas
3. Tabela de taxonomia source/medium com cores por canal GA4
4. Templates por plataforma em blocos de código estilizados (copy-paste ready)
5. Dashboard de auditoria com status por severidade (🔴🟠🟡⚪)
6. Checklist de integração CRM com status
7. Regras de governança como cards
8. Footer com crédito gui.marketing (link UTM)

**Links UTM:**
- Header: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-utm-governance&utm_content=header-logo`
- Footer: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-utm-governance&utm_content=footer`

**Design:**
- Font: Inter + Inter Tight
- Background: `#f7f3ed`
- Accent: `#864df9`
- Issues críticos: badge vermelho
- Issues baixos: badge cinza
- Templates: blocos monospace com botão "copiar"
- Plataformas: ícones por canal (Google=azul, Meta=azul-escuro, LinkedIn=azul-linkedin, TikTok=preto)

**Salvamento:**
- Markdown: `deliverables/utm-governance/{client-name}/utm-governance.md`
- HTML: `deliverables/utm-governance/{client-name}/utm-governance.html`

---

## Leis Inegociáveis

```
1. INTAKE PRIMEIRO
   Sem as 10 perguntas respondidas, sem plano. Perguntar.

2. REFERENCE PRIMEIRO
   Ler references/utm-taxonomy-specs.md ANTES de gerar templates.

3. LOWERCASE ABSOLUTO
   Nenhum parâmetro UTM pode conter uppercase. Zero exceção.

4. GA4 CHANNEL ALIGNMENT
   utm_medium DEVE corresponder a um canal GA4 reconhecido.
   Se não corresponde, tráfego = "(Unassigned)" = dado perdido.

5. MACROS DINÂMICOS
   Nunca recomendar UTMs manuais em plataformas que suportam macros.
   Manual = erro humano = dados inconsistentes.

6. GCLID NO CRM
   Se tem Google Ads + CRM, gclid DEVE chegar ao CRM.
   Sem gclid, offline conversions são impossíveis no Google Ads.

7. ATTRIBUTION IDS COMPLETOS
   Cada plataforma tem seu click ID. Todos devem ser capturados.
   fbclid, li_fat_id, ttclid, epik — sem eles, match rate despenca.

8. FIRST-TOUCH PRESERVADO
   Nunca sobrescrever UTMs originais no CRM. Campos "last_" separados.

9. DOIS OUTPUTS OBRIGATÓRIOS
   Sempre gerar Markdown + HTML.

10. NÃO TAGEAR LINKS INTERNOS
    UTMs em links dentro do site = overwrites session = dados corrompidos.
```

---

## Anti-Padrões

```
❌ "facebook" como source — consolidar como "meta" (FB + IG + Messenger + AN)
❌ "pago" como medium — GA4 não reconhece. Usar "cpc" ou "paid-social"
❌ UTMs manuais em Google Ads — erro humano. Usar macros + URL Suffix
❌ Mesmo utm_campaign para tudo — impossibilita análise por campanha
❌ Campaign sem data — "campanha-erp" existe há 3 anos, qual trimestre?
❌ Uppercase misturado — "Google" ≠ "google" no GA4
❌ Espaços em UTMs — "black friday" vira "black%20friday" = lixo
❌ UTMs em links internos — destrói atribuição original da sessão
❌ CRM sem campo para gclid — atribuição offline impossível
❌ Auto-tagging desligado — sem gclid, sem remarketing lists, sem smart bidding
❌ Redirects removendo parâmetros — 301/302 que stripam UTMs e click IDs
❌ "Não preciso de naming, só eu opero" — futuro-eu vai operar com estagiário
❌ UTMs em links CTWA — impossível. CTWA não tem URL editável
❌ Achar que CAPI resolve CTWA — CAPI resolve cookies, não tracking dentro do WhatsApp
❌ CRM usando apenas telefone como chave — BSUID quebra match quando usuário tem username
❌ Ignorar parâmetro referral da WABA — é o ÚNICO elo de atribuição CTWA → venda
❌ WhatsApp como canal core sem CRM — conversas mais valiosas presas no celular
```

---

## Notas Operacionais

1. Se `measurement-plan-{{CLIENTE}}.md` existir, verificar alinhamento de parâmetros
2. Se `conversion-qa-{{CLIENTE}}.md` existir, verificar se UTMs estão na checklist
3. Auto-tagging Google Ads: verificar em Account Settings → Auto-tagging → ON
4. Meta fbclid: automático, mas verificar se redirects não removem
5. LinkedIn li_fat_id: requer LinkedIn Insight Tag no site
6. TikTok ttclid: automático com TikTok Pixel instalado
7. Para multi-marca: adicionar prefixo de marca no utm_campaign (ex: `marca-2026-q2-...`)
8. Auditoria mensal recomendada: GA4 Traffic Acquisition → filtrar "(Unassigned)" > 5%
9. Template de checklist pré-launch de campanha: validar URL com UTMs antes de ativar
10. Documento de governança deve ser compartilhado com todo o time de mídia e marketing
11. **WhatsApp CTWA:** sem WABA, único tracking possível é "pergunta padrão" manual + planilha
12. **WABA referral:** disponível no webhook ao receber mensagem — verificar com BSP se está ativo
13. **BSUID:** verificar se BSP suporta BSUID em webhooks ANTES de implementar. Sem suporte = atribuição perdida quando usuários adotam usernames
14. **Migração de número:** desconecta WA Business App durante migração para WABA — planejar transição
15. **Mínimo viável WhatsApp:** pergunta padrão + etiquetas + planilha = 70% da inteligência necessária
16. Referência completa: https://gui.marketing/blog/whatsapp-tracking-conversoes/
