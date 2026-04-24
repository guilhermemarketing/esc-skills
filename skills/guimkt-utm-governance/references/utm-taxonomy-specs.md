# UTM Taxonomy Specs — Reference

Especificações de governança para o agente consultar durante a criação de convenções UTM.

---

## 1. GA4 Default Channel Grouping — Regras de Matching

> **Regra fundamental:** GA4 é case-sensitive. `Email` ≠ `email`. Tudo lowercase.

### Canais e Regras de Medium/Source

| Canal GA4 | `utm_medium` deve conter | `utm_source` deve conter | Notas |
|-----------|--------------------------|--------------------------|-------|
| **Paid Search** | `cpc`, `ppc`, `paidsearch` | Source lista de search engines | Auto-tagging (gclid) resolve para Google |
| **Organic Search** | `organic` | Source lista de search engines | Não tagear — tráfego orgânico é automático |
| **Paid Social** | `paid-social`, `cpc`, `ppc`, `paidsocial` | Source lista de redes sociais | `cpc` funciona se source = social |
| **Organic Social** | `social`, `social-network`, `social-media` | Source lista de redes sociais | Sem medium = Referral |
| **Email** | `email` | Qualquer | Exatamente `email` — sem variações |
| **Affiliates** | `affiliate` | Qualquer | |
| **Referral** | `referral` | Qualquer | Tráfego sem UTM de outros sites |
| **Display** | `display`, `cpm`, `banner` | Qualquer | |
| **Video** | `video` | Qualquer | YouTube ads sem auto-tag |
| **Audio** | `audio` | Qualquer | Podcasts, Spotify ads |
| **SMS** | `sms` | Qualquer | |
| **Mobile Push** | `push`, `mobile`, `notification` | Qualquer | |
| **Direct** | (sem medium) | `(direct)` | Sem UTMs / tráfego direto |
| **(Unassigned)** | — | — | Não matcha nenhuma regra acima |

### Lista de Search Engines Reconhecidos

```
google, bing, yahoo, baidu, duckduckgo, yandex, ask, aol, dogpile,
ecosia, naver, sogou, seznam, qwant, brave
```

### Lista de Redes Sociais Reconhecidas

```
facebook, instagram, linkedin, twitter, x.com, tiktok, pinterest,
reddit, tumblr, snapchat, threads, youtube, quora, whatsapp,
telegram, discord, mastodon, bluesky
```

---

## 2. Parâmetros UTM Padrão gui.marketing

### Parâmetros Oficiais (5 padrão + 7 extended)

| # | Parâmetro | Tipo | Obrigatório | Descrição |
|---|-----------|:----:|:-----------:|-----------|
| 1 | `utm_source` | Padrão | ✅ | Plataforma de origem |
| 2 | `utm_medium` | Padrão | ✅ | Tipo de mídia/canal |
| 3 | `utm_campaign` | Padrão | ✅ | Nome da campanha |
| 4 | `utm_content` | Padrão | ⬜ | Variação criativa / ad name |
| 5 | `utm_term` | Padrão | ⬜ | Keyword / termo de busca |
| 6 | `utm_adset` | Extended | 🔶 | Conjunto de anúncios / ad group |
| 7 | `utm_adname` | Extended | 🔶 | Nome do anúncio individual |
| 8 | `utm_placement` | Extended | ⬜ | Posicionamento (feed, stories, search) |
| 9 | `keyword` | Extended | ⬜ | Keyword exata (Google Ads) |
| 10 | `matchtype` | Extended | ⬜ | Tipo de correspondência (exact, phrase, broad) |
| 11 | `device` | Extended | ⬜ | Dispositivo (mobile, desktop, tablet) |
| 12 | `location` | Extended | ⬜ | Geo-localização do clique |

### IDs de Atribuição (captura automática — NÃO tagear manualmente)

| ID | Plataforma | Como chega | Persistência |
|----|-----------|-----------|-------------|
| `gclid` | Google Ads | Auto-tagging | URL → 1st party cookie (90 dias) |
| `gbraid` | Google Ads (iOS ATT) | Auto-tagging | URL → 1st party cookie |
| `wbraid` | Google Ads (web-to-app) | Auto-tagging | URL param |
| `dclid` | DV360 | Auto-tagging | URL param |
| `fbclid` | Meta Ads | Auto-append | URL param |
| `fbc` | Meta | Cookie browser | 1st party `_fbc` |
| `fbp` | Meta | Cookie browser | 1st party `_fbp` |
| `ttclid` | TikTok Ads | Auto-append | URL param |
| `li_fat_id` | LinkedIn Ads | Auto-append | URL param |
| `epik` | Pinterest Ads | Auto-append | URL param |

---

## 3. Templates de UTM por Plataforma

### 3.1 Google Ads (Search)

```
URL Suffix (Account-level ou Campaign-level):
utm_source=google&utm_medium=cpc&utm_campaign={campaignname}&utm_adset={adgroupname}&utm_adname={creative}&utm_placement={network}&keyword={keyword}&matchtype={matchtype}&device={device}&location={loc_physical_ms}&utm_term={keyword}

Notas:
- Auto-tagging (gclid) deve estar ATIVO
- UTMs manuais complementam, não substituem gclid
- {network} = g (Google Search), d (Display), s (Search Partners)
- {creative} = ID do anúncio (não nome)
```

### Macros Dinâmicas Google Ads

| Macro | Valor | Uso |
|-------|-------|-----|
| `{campaignname}` | Nome da campanha | utm_campaign |
| `{adgroupname}` | Nome do ad group | utm_adset |
| `{creative}` | ID do criativo | utm_adname |
| `{keyword}` | Keyword que acionou | keyword, utm_term |
| `{matchtype}` | e, p, b (exact/phrase/broad) | matchtype |
| `{device}` | m, c, t (mobile/computer/tablet) | device |
| `{network}` | g, d, s | utm_placement |
| `{loc_physical_ms}` | ID da localização | location |
| `{targetid}` | ID do target | — |
| `{feeditemid}` | ID do asset/extension | — |

### 3.2 Meta Ads (Facebook / Instagram)

```
URL Parameters (Ad-level):
utm_source=meta&utm_medium=paid-social&utm_campaign={{campaign.name}}&utm_adset={{adset.name}}&utm_adname={{ad.name}}&utm_placement={{placement}}&utm_content={{ad.id}}

Notas:
- Meta auto-appends fbclid (NÃO desativar)
- {{placement}} = feed, stories, reels, right_column, etc.
- utm_source = "meta" (não "facebook") para consolidar FB + IG
```

### Macros Dinâmicas Meta Ads

| Macro | Valor | Uso |
|-------|-------|-----|
| `{{campaign.name}}` | Nome da campanha | utm_campaign |
| `{{campaign.id}}` | ID da campanha | utm_id |
| `{{adset.name}}` | Nome do conjunto | utm_adset |
| `{{adset.id}}` | ID do conjunto | — |
| `{{ad.name}}` | Nome do anúncio | utm_adname |
| `{{ad.id}}` | ID do anúncio | utm_content |
| `{{placement}}` | Posicionamento | utm_placement |
| `{{site_source_name}}` | fb, ig, an, msg | — |

### 3.3 LinkedIn Ads

```
URL Parameters:
utm_source=linkedin&utm_medium=paid-social&utm_campaign=%CAMPAIGNNAME%&utm_adset=%CAMPAIGNGROUPNAME%&utm_adname=%CREATIVEID%&utm_content=%CREATIVENAME%

Notas:
- LinkedIn auto-appends li_fat_id
- Macros limitados vs. Google/Meta
```

### Macros Dinâmicas LinkedIn

| Macro | Valor |
|-------|-------|
| `%CAMPAIGNNAME%` | Nome da campanha |
| `%CAMPAIGNGROUPNAME%` | Nome do grupo |
| `%CREATIVEID%` | ID do criativo |
| `%CREATIVENAME%` | Nome do criativo |

### 3.4 TikTok Ads

```
URL Parameters:
utm_source=tiktok&utm_medium=paid-social&utm_campaign=__CAMPAIGN_NAME__&utm_adset=__AID_NAME__&utm_adname=__CID_NAME__&utm_content=__CID__

Notas:
- TikTok auto-appends ttclid
```

### Macros Dinâmicas TikTok

| Macro | Valor |
|-------|-------|
| `__CAMPAIGN_NAME__` | Nome da campanha |
| `__CAMPAIGN_ID__` | ID da campanha |
| `__AID_NAME__` | Nome do ad group |
| `__CID_NAME__` | Nome do criativo |
| `__CID__` | ID do criativo |

### 3.5 Pinterest Ads

```
URL Parameters:
utm_source=pinterest&utm_medium=paid-social&utm_campaign={campaignname}&utm_content={adid}

Notas:
- Pinterest auto-appends epik
- Macros mais limitados
```

### 3.6 Email Marketing

```
utm_source={{plataforma}}&utm_medium=email&utm_campaign={{nome-campanha}}&utm_content={{variacao}}

Exemplos de source: mailchimp, rdstation, hubspot, activecampaign, brevo
```

### 3.7 Outros Canais

```
WhatsApp orgânico:
utm_source=whatsapp&utm_medium=social&utm_campaign={{campanha}}

Telegram:
utm_source=telegram&utm_medium=social&utm_campaign={{campanha}}

QR Code:
utm_source=qrcode&utm_medium=offline&utm_campaign={{campanha}}&utm_content={{local}}

Influencer:
utm_source={{nome-influencer}}&utm_medium=influencer&utm_campaign={{campanha}}
```

---

## 4. Naming Convention — Regras Obrigatórias

### Regras de Formatação

```
1. LOWERCASE SEMPRE         → google (não Google, GOOGLE)
2. SEM ESPAÇOS              → black-friday (não black friday → black%20friday)
3. HIFENS para separar      → campanha-nome (não campanha_nome)
4. SEM CARACTERES ESPECIAIS → sem acentos, ç, ñ, etc.
5. SEM UNDERSCORES em UTMs  → underscores reservados para parâmetros internos
6. DATAS no campaign name   → 2026-q2-produto-campanha
7. CONSISTÊNCIA CROSS-TEAM  → mesma taxonomia para todos os operadores
```

### Estrutura Recomendada para utm_campaign

```
{ano}-{trimestre}-{produto-servico}-{tipo-campanha}-{variante}

Exemplos:
- 2026-q2-consultoria-search-brand
- 2026-q2-erp-social-awareness
- 2026-q1-plano-pro-remarketing-carrinho
- 2026-q3-webinar-ia-lancamento
```

### Regras Especiais

```
- utm_source: SEMPRE o nome da plataforma, lowercase, sem abreviações
  ✅ google, meta, linkedin, tiktok, pinterest, mailchimp
  ❌ fb, li, gads, tt, pin, mc

- utm_medium: SEMPRE alinhado com GA4 Default Channel Grouping
  ✅ cpc, paid-social, email, referral, organic, display
  ❌ pago, social_pago, mail, ref, organico

- utm_content: usar para diferenciar criativos/variações
  ✅ rsa-headline-v1, carrossel-beneficios, video-depoimento
  ❌ ad1, teste, novo
```

---

## 5. Auditoria de UTMs — Checklist

### Red Flags (Problemas Críticos)

```
🔴 utm_source ou utm_medium em CamelCase ou UPPERCASE
🔴 Espaços em qualquer parâmetro UTM
🔴 utm_medium que não matcha GA4 channel groups (ex: "pago", "social_pago")
🔴 UTMs em links internos do site (overwrites session attribution)
🔴 fbclid / gclid sendo removidos por redirects ou URL cleaners
🔴 Hidden fields do formulário não capturando UTMs
🔴 CRM não recebendo campos de atribuição
🔴 Mesmo utm_campaign para campanhas diferentes em períodos diferentes
```

### Yellow Flags (Atenção)

```
🟡 utm_source inconsistente entre operadores (facebook vs meta vs fb)
🟡 utm_campaign sem data/trimestre (dificulta análise temporal)
🟡 utm_content vazio em campanhas com múltiplos criativos
🟡 utm_adset vazio em campanhas com múltiplos ad sets
🟡 Auto-tagging desativado no Google Ads
🟡 Tráfego "(Unassigned)" > 5% no GA4
🟡 Tráfego "Direct" inflado (possível UTM stripping)
```

### Green Flags (Boas Práticas)

```
🟢 Taxonomia documentada e compartilhada com todo o time
🟢 Templates de UTM por plataforma configurados
🟢 Macros dinâmicos ativos em todas as plataformas de ads
🟢 Script GTM capturando UTMs e persistindo em cookies
🟢 Hidden fields preenchidos e enviando ao CRM
🟢 Auto-tagging ativo em Google Ads
🟢 utm_medium alinhado com GA4 channel groups
🟢 Auditoria mensal do Traffic Acquisition report
```

---

## 6. CRM Integration — Campos de Atribuição

### Mapeamento LP → CRM

Todos os parâmetros abaixo devem existir como **custom fields** nos objetos do CRM:

```
Objeto: Lead / Contact
├── utm_source         (texto)
├── utm_medium         (texto)
├── utm_campaign       (texto)
├── utm_adset          (texto)
├── utm_adname         (texto)
├── utm_placement      (texto)
├── utm_content        (texto)
├── utm_term           (texto)
├── keyword            (texto)
├── matchtype          (texto)
├── device             (texto)
├── location           (texto)
├── gclid              (texto, max 255 chars)
├── fbclid             (texto, max 500 chars)
├── fbc                (texto)
├── fbp                (texto)
├── li_fat_id          (texto)
├── ttclid             (texto)
├── epik               (texto)
├── landing_page       (URL)
├── referrer           (URL)
└── first_touch_date   (datetime)

Objeto: Deal / Oportunidade
├── (herda todos os campos do Lead/Contact via automação)
├── deal_source        (cópia do utm_source no momento da criação)
├── deal_campaign      (cópia do utm_campaign)
└── attribution_model  (first-touch / last-touch / multi-touch)
```

### Regras de Persistência

```
1. FIRST-TOUCH preservado: nunca sobrescrever UTMs originais no Lead
2. LAST-TOUCH em campo separado: se Lead retorna com novos UTMs, registrar em campos "last_"
3. Automação CRM: ao criar Deal, copiar campos de atribuição do Lead automaticamente
4. Offline Conversions: usar gclid/fbclid do Lead para upload de conversões
5. Sem gclid = sem atribuição determinística no Google Ads offline
6. Sem fbclid/fbc/fbp = match rate muito baixo no Meta offline
```

---

## 7. Validação de URLs — Regras

### Regex de Validação

```regex
# UTM source: lowercase, sem espaços, sem caracteres especiais
utm_source=[a-z0-9][a-z0-9-]*[a-z0-9]

# UTM medium: deve ser um valor reconhecido pelo GA4
utm_medium=(cpc|paid-social|email|referral|organic|display|video|audio|sms|push|affiliate|influencer|offline)

# UTM campaign: lowercase, hifens, com data
utm_campaign=[0-9]{4}-q[1-4]-[a-z0-9-]+

# Sem espaços em nenhum parâmetro
utm_[a-z]+=.*\s.*  → FALHA
```

### Script de Validação (pseudo-código)

```
FUNCTION validateUTM(url):
  params = parseURLParams(url)
  errors = []
  
  IF params.utm_source != lowercase(params.utm_source):
    errors.push("utm_source deve ser lowercase")
  
  IF params.utm_medium NOT IN GA4_VALID_MEDIUMS:
    errors.push("utm_medium não reconhecido pelo GA4: " + params.utm_medium)
  
  IF params.utm_campaign AND NOT matches(/^[0-9]{4}-q[1-4]-/, params.utm_campaign):
    warnings.push("utm_campaign sem prefixo de data recomendado")
  
  IF containsSpaces(anyParam):
    errors.push("Parâmetro contém espaços: " + param)
  
  IF containsUppercase(anyParam):
    errors.push("Parâmetro contém uppercase: " + param)
  
  RETURN {valid: errors.length == 0, errors, warnings}
```

---

## 8. WhatsApp Tracking & Atribuição — Cenários Brasil

> **Contexto:** WhatsApp é o canal #1 de vendas (79%), marketing (54%) e atendimento (47%) no Brasil.
> É frequentemente o canal MENOS integrado ao CRM. As conversas mais valiosas da empresa estão presas no celular dos funcionários.
> Fonte: Panorama do Go-To-Market no Brasil 2026, HubSpot.
> Referência: https://gui.marketing/blog/whatsapp-tracking-conversoes/

### 8.1 Por que UTM e Pixel NÃO Funcionam em CTWA

```
CTWA (Click to WhatsApp Ads):
- NÃO existe URL editável para inserir UTMs
- O link é gerado e controlado pela Meta (back-end)
- O lead vai DIRETO do anúncio para o app WhatsApp
- NÃO há pageview, NÃO há formulário, NÃO há pixel
- O pixel registra apenas impressão e clique no anúncio
- O que acontece DENTRO do WhatsApp é caixa preta

Consequência fatal:
- O algoritmo da Meta aprende a gerar CONVERSAS, não CLIENTES
- Sem sinal de fechamento, o ML otimiza para o lead preguiçoso
- Volume cresce, custo por conversa cai, qualidade despenca
- "Lixo qualificado" — high volume, zero revenue
```

### 8.2 Três Cenários de WhatsApp Tracking

| Cenário | Fluxo | UTMs? | Pixel? | Atribuição |
|---------|-------|:-----:|:------:|-----------|
| **A: LP → WhatsApp** | Anúncio → Landing Page → Botão WA | ✅ Via URL da LP | ✅ Na LP | Script GTM captura UTMs antes do redirect + evento `whatsapp_click` |
| **B: CTWA Puro** | Anúncio → WhatsApp direto | ❌ Impossível | ❌ Impossível | Apenas via WABA: parâmetro `referral` + `BSUID` |
| **C: LP → WhatsApp com CRM** | Anúncio → LP → Form/WA → CRM | ✅ Via URL + hidden fields | ✅ Na LP | Melhor cenário: captura dados na LP, registra no CRM, fecha loop offline |

### 8.3 WABA — WhatsApp Business API

```
O que é:
- Versão profissional do WhatsApp da Meta para empresas
- Permite: múltiplos atendentes, automação, CRM integration, tracking
- NÃO é o WhatsApp Business App (Play Store) — são diferentes
- Acessada EXCLUSIVAMENTE via BSPs (Business Solution Providers)

Parâmetros de tracking únicos:

1. referral (parâmetro da WABA API)
   - Quando lead chega via CTWA e número está na WABA
   - A API passa automaticamente dados do anúncio de origem:
     * campaign_id, adset_id, ad_id (do Meta Ads)
   - ÚNICO elo que fecha rastreamento CTWA → conversa → venda
   - Disponível no webhook da WABA ao receber mensagem

2. BSUID (Business Scoped User ID)
   - Identificador que a Meta usa para conversas onde o usuário
     NÃO expõe o número de telefone (usernames do WhatsApp)
   - Campo "from" do webhook retorna BSUID ao invés de telefone
   - Se o sistema usa apenas telefone para match → conversas
     com BSUID ficam sem atribuição → CAC aparente sobe
   - CRM DEVE armazenar AMBOS: telefone E BSUID
   - Lógica de merge obrigatória quando dados se cruzam
   - Verificar se o BSP escolhido suporta BSUID em webhooks
```

### 8.4 BSPs no Brasil — Referência de Custo (2026)

```
Modelo de cobrança da Meta (desde Jul/2025):
- Conversas receptivas (lead inicia): GRATUITAS e ilimitadas
  → Relevante para CTWA: o lead inicia, custo Meta = zero
- Mensagens de Marketing (ativo): ~R$0,35 por template
- Mensagens de Utilidade: ~R$0,05 (gratuitas na janela 24h)
- Mensagens de Autenticação: ~R$0,02

Custo dos BSPs (plataforma):
- Tier 1 (PME): R$69–149/mês (Umbler Talk, Z-API, Wppconnect)
- Tier 2 (Médio porte): R$200–500/mês (Treble.ai, Whaticket)
- Tier 3 (Enterprise): R$1.000+/mês (Blip, Twilio, Infobip)
- Implementação: R$0–3.000 (Umbler cobra ~R$3.000 para setup)

Conta real para micro empresa (200 conv/mês, sem disparo ativo):
- Meta: R$0/mês (conversas receptivas)
- BSP: R$69–99/mês
- Setup: R$3.000 (uma vez)
- Ano 1: R$3.828–4.188 | Ano 2+: R$828–1.188
```

### 8.5 Decisão: Quando Vale Montar Estrutura WABA?

```
NÃO faz sentido se:
- Verba de mídia < R$3k/mês
- Menos de 200–300 conversas/mês via WhatsApp
- Um único atendente (sem multi-agente)
- Operação onde o dono atende pessoalmente
- Sem clareza sobre taxa de fechamento

FAZ sentido se:
- Volume impossibilita acompanhamento manual de origem
- Múltiplos atendentes no mesmo número
- Necessidade de disparo ativo (follow-up, nutrição)
- Integração com CRM para registro automático
- Quer parâmetro referral para fechar loop CTWA → venda
- Precisa treinar o algoritmo Meta com sinais de qualidade
```

### 8.6 Mínimo Viável Antes da WABA (Custo Zero)

```
Para operações entre os dois perfis (volume crescendo, sem BSP):

1. Pergunta padrão no início de toda conversa:
   "Como você nos encontrou? (Instagram / Google / indicação)"
   → Registrar em planilha semanal

2. Etiquetas no WhatsApp Business App:
   → Organizar conversas por campanha de origem manualmente

3. Pixel instalado se houver site:
   → Mesmo sem CTWA, ajuda em retargeting e lookalike

Resultado: ~70% da inteligência necessária, custo zero.
Os 30% restantes (automação) se pagam quando o volume justificar.
```

### 8.7 WhatsApp + CRM — Campos Obrigatórios

```
Campos adicionais no CRM para operações WhatsApp-first:

Objeto: Lead / Contact
├── whatsapp_number      (texto, E.164: +5516999999999)
├── whatsapp_bsuid       (texto, BSUID da Meta — coexiste com telefone)
├── whatsapp_source      (enum: ctwa, organic, lp-redirect, manual)
├── referral_campaign_id (texto, do parâmetro referral WABA)
├── referral_adset_id    (texto, do parâmetro referral WABA)
├── referral_ad_id       (texto, do parâmetro referral WABA)
├── first_message_date   (datetime, quando iniciou conversa)
├── conversation_status  (enum: new, in-progress, qualified, closed-won, closed-lost)
└── bsp_conversation_id  (texto, ID interno do BSP)

Regras de merge:
1. Se lead chega por CTWA (referral), popular referral_campaign/adset/ad_id
2. Se lead chega por LP → WA (cenário A/C), popular UTMs normais
3. Se BSUID presente, armazenar junto ao telefone
4. Mesmo contato pode ter telefone E BSUID em momentos diferentes
5. Lógica de dedup: telefone é chave primária, BSUID é chave secundária
```

### 8.8 WhatsApp + Offline Conversions — Fechando o Loop

```
Pipeline CTWA → Venda → Ads Platform:

1. Lead inicia conversa via CTWA
2. WABA webhook recebe mensagem com parâmetro referral
   → referral contém: source_url, source_id, source_type, headline, body
3. BSP registra no CRM com referral_campaign/adset/ad_id
4. Atendente qualifica lead (MQL → SQL → Venda)
5. CRM registra mudança de status + valor
6. Integração envia conversão offline para Meta:
   → CAPI offline event com email/phone hash + value + referral data
   → Meta faz match com a conversa original via BSUID ou phone
7. Algoritmo Meta recebe sinal de QUALIDADE (não apenas volume)
   → Otimização melhora: busca perfis semelhantes aos que COMPRARAM

Para Google Ads (se houver LP no meio):
→ Cenário C: LP captura gclid → CRM → Offline Conversion Import
→ Cenário B (CTWA puro): Google Ads NÃO tem visibilidade
   → Alternativa: Enhanced Conversions com email/phone do lead

Para LinkedIn Ads:
→ Conversions API com email hash + conversion rule
→ li_fat_id só existe se houver LP no caminho
```

### 8.9 Limitações Críticas — Disclaimer Obrigatório

```
⚠️ CTWA + Google Analytics = CEGO
- GA4 NÃO rastreia o que acontece dentro do WhatsApp
- Única forma: evento manual em thank you page (exige site no caminho)
- CTWA puro: GA4 não vê funil completo

⚠️ CAPI NÃO resolve CTWA
- CAPI resolve cookies bloqueados, NÃO tracking dentro do WhatsApp
- Para fechar loop CTWA → venda: usar WABA referral, não CAPI
- CAPI é complementar (para Enhanced Conversions), não substituto

⚠️ Migração de número interrompe atendimento
- Número DEVE ser desconectado do WA Business App antes de migrar para WABA
- Não dá para usar os dois simultaneamente
- Planejamento de transição obrigatório

⚠️ BSUID é o futuro — preparar agora
- Com usernames no WhatsApp, campo "from" muda de telefone para BSUID
- Sistemas que usam apenas telefone para match vão perder atribuição
- Consultar BSP sobre suporte a BSUID ANTES de implementar
```
