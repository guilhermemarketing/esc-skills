# Tracking Architecture Specs — Reference

Especificações técnicas para o agente consultar durante a geração do plano de mensuração.

---

## 1. dataLayer Schema Padrão

```json
{
  "event": "generate_lead",
  "lead_type": "form_submit | whatsapp_click | phone_click | chat_start",
  "lead_source": "{{utm_source}}",
  "lead_medium": "{{utm_medium}}",
  "lead_campaign": "{{utm_campaign}}",
  "lead_adset": "{{utm_adset}}",
  "lead_adname": "{{utm_adname}}",
  "lead_placement": "{{utm_placement}}",
  "lead_device": "{{device}}",
  "lead_keyword": "{{keyword}}",
  "lead_matchtype": "{{matchtype}}",
  "lead_term": "{{term}}",
  "lead_position": "{{position}}",
  "lead_location": "{{location}}",
  "attribution_ids": {
    "gclid": "{{gclid}}",
    "gbraid": "{{gbraid}}",
    "wbraid": "{{wbraid}}",
    "dclid": "{{dclid}}",
    "fbclid": "{{fbclid}}",
    "fbc": "{{fbc}}",
    "fbp": "{{fbp}}",
    "ttclid": "{{ttclid}}",
    "li_fat_id": "{{li_fat_id}}",
    "epik": "{{epik}}"
  },
  "user_data": {
    "email_address": "{{hashed_email}}",
    "phone_number": "{{hashed_phone}}",
    "address": {
      "first_name": "{{hashed_fn}}",
      "last_name": "{{hashed_ln}}",
      "city": "{{city}}",
      "region": "{{region}}",
      "postal_code": "{{postal_code}}",
      "country": "{{country}}"
    }
  },
  "conversion_value": 0,
  "conversion_currency": "BRL",
  "page_location": "{{page_url}}",
  "page_title": "{{page_title}}",
  "consent_state": {
    "ad_storage": "granted | denied",
    "analytics_storage": "granted | denied",
    "ad_user_data": "granted | denied",
    "ad_personalization": "granted | denied"
  }
}
```

---

## 2. Parâmetros UTM + Atribuição

### UTMs (capturados da URL)
| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `utm_source` | Plataforma de origem | google, meta, linkedin |
| `utm_medium` | Tipo de mídia | cpc, cpm, social, email |
| `utm_campaign` | Nome da campanha | search-brand-2026 |
| `utm_adset` | Conjunto de anúncios | interesse-ceo-sp |
| `utm_adname` | Nome do anúncio | rsa-headline-teste-a |
| `utm_placement` | Posicionamento | feed, stories, search |
| `device` | Dispositivo | mobile, desktop |
| `keyword` | Palavra-chave (Google) | consultoria marketing |
| `matchtype` | Tipo de correspondência | exact, phrase, broad |
| `term` | Termo de busca real | como contratar marketing |
| `position` | Posição do anúncio | 1, 2, other |
| `location` | Localização geográfica | São Paulo |

### IDs de Atribuição (capturados automaticamente)
| ID | Plataforma | Persistência |
|----|-----------|-------------|
| `gclid` | Google Ads (padrão) | URL param → 1st party cookie |
| `gbraid` | Google Ads (iOS) | URL param → 1st party cookie |
| `wbraid` | Google Ads (web-to-app) | URL param |
| `dclid` | Display & Video 360 | URL param |
| `fbclid` | Meta Ads | URL param |
| `fbc` | Meta (click cookie) | 1st party cookie `_fbc` |
| `fbp` | Meta (browser cookie) | 1st party cookie `_fbp` |
| `ttclid` | TikTok Ads | URL param |
| `li_fat_id` | LinkedIn Ads | URL param |
| `epik` | Pinterest Ads | URL param |

---

## 3. GA4 Event Taxonomy

### Naming Convention
```
[ação]_[objeto]_[qualificador]

Exemplos:
- generate_lead
- form_submit_contact
- form_submit_material
- whatsapp_click_header
- whatsapp_click_footer
- phone_click
- scroll_depth_50
- scroll_depth_90
- cta_click_hero
- video_play_testimonial
- chat_start
- file_download_ebook
```

### Regras
1. Lowercase com underscores (snake_case)
2. Máximo 40 caracteres
3. Sem caracteres especiais ou acentos
4. Prefixo descritivo da ação (generate, form, click, scroll, view)
5. Sufixo descritivo do contexto quando necessário

### Eventos Recomendados (Recommended Events)
Priorizar eventos recomendados pelo Google sempre que possível:
- `generate_lead` — conversão primária de formulário
- `page_view` — pageview padrão
- `scroll` — scroll depth
- `click` — cliques em elementos externos
- `view_item` — visualização de produto/serviço
- `begin_checkout` — início de processo de compra
- `purchase` — compra finalizada

---

## 4. Enhanced Conversions — Specs por Plataforma

### Google Ads Enhanced Conversions
```
Dados aceitos (hasheados com SHA-256):
- email (normalizado: lowercase, trim, remove dots do gmail)
- phone_number (formato E.164: +55DDDNÚMERO)
- first_name (lowercase, trim)
- last_name (lowercase, trim)
- street_address
- city
- region
- postal_code
- country (ISO 3166-1 alpha-2: BR)
```

### Meta CAPI (Conversions API)
```
Endpoint: https://graph.facebook.com/v21.0/{pixel_id}/events
Dados aceitos (hasheados com SHA-256):
- em (email normalizado)
- ph (telefone E.164)
- fn (primeiro nome)
- ln (sobrenome)
- ct (cidade)
- st (estado)
- zp (CEP)
- country (país, lowercase: br)
- external_id (ID único do CRM)
- client_ip_address
- client_user_agent
- fbc (cookie _fbc)
- fbp (cookie _fbp)
- fbclid (click ID da URL)

Event names: Lead, CompleteRegistration, Contact, FindLocation, Schedule, SubmitApplication
```

### LinkedIn CAPI
```
Endpoint: LinkedIn Conversions API
Dados aceitos (hasheados com SHA-256):
- email
- linkedInFirstPartyId (li_fat_id do cookie)
- acct (Account URN)

Event names: Mapeados para conversion rules no Campaign Manager
```

### TikTok Events API
```
Endpoint: https://business-api.tiktok.com/open_api/v1.3/event/track/
Dados aceitos (hasheados com SHA-256):
- email
- phone_number
- external_id
- ttclid
- ttp (TikTok cookie)

Event names: SubmitForm, Contact, CompleteRegistration
```

---

## 5. Consent Mode v2 — Requisitos

### Sinais Obrigatórios
| Sinal | Descrição | Default Recomendado |
|-------|-----------|-------------------|
| `ad_storage` | Cookies de publicidade | denied |
| `analytics_storage` | Cookies de analytics | denied |
| `ad_user_data` | Envio de user data para ads | denied |
| `ad_personalization` | Remarketing/personalização | denied |
| `functionality_storage` | Cookies funcionais | granted |
| `security_storage` | Cookies de segurança | granted |
| `personalization_storage` | Cookies de personalização | denied |

### Comportamento por Estado de Consent

| Tag Type | Consent Denied | Consent Granted |
|----------|---------------|----------------|
| GA4 | Pings sem cookies (modelagem) | Tracking completo |
| Google Ads Conversion | Conversion modeling | Tracking completo + Enhanced |
| Meta Pixel | Nenhum disparo | Tracking completo |
| Meta CAPI (server) | Dispara SEM user_data | Dispara COM user_data |
| LinkedIn Insight | Nenhum disparo | Tracking completo |
| TikTok Pixel | Nenhum disparo | Tracking completo |

### dataLayer Consent Default (pré-CMP)
```javascript
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'analytics_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'functionality_storage': 'granted',
  'security_storage': 'granted',
  'wait_for_update': 500
});
```

### dataLayer Consent Update (pós-CMP)
```javascript
gtag('consent', 'update', {
  'ad_storage': 'granted',
  'analytics_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted'
});
```

---

## 6. Offline Conversions — Fluxo

### Google Ads Offline Conversion Import
```
Fluxo: CRM → Upload/API → Google Ads
Campos obrigatórios:
- gclid OU enhanced conversion data (email/phone)
- conversion_name (= nome da conversão no Google Ads)
- conversion_time (formato: yyyy-mm-dd hh:mm:ss+|-hh:mm)
- conversion_value
- conversion_currency (BRL)

API: Google Ads API → UploadConversionAdjustments
Frequência recomendada: diária ou a cada 6h
Latência máxima: 90 dias após o clique
```

### Meta Offline Conversions
```
Fluxo: CRM → CAPI ou Offline Events API → Meta Ads
Campos obrigatórios:
- event_name (Lead, Purchase, etc.)
- event_time (unix timestamp)
- user_data (email e/ou phone hasheados)
- custom_data.value
- custom_data.currency
- action_source: "system_generated"

Match keys: fbc, fbp, external_id, email, phone
Frequência recomendada: diária
Latência máxima: 7 dias para offline events
```

### LinkedIn Offline Conversions
```
Fluxo: CRM → LinkedIn Conversions API
Campos: email hasheado + conversion rule ID + timestamp
Frequência: diária
```

---

## 7. WhatsApp Tracking — Cenários

### Cenário A: LP → WhatsApp (botão no site)
- Rastreável com dataLayer event `whatsapp_click`
- UTMs preservados se script captura antes do redirecionamento
- Enhanced Conversions possível via server-side com dados do CRM

### Cenário B: CTWA (Click-to-WhatsApp Ad)
- Pixel/GTM NÃO dispara (não há pageview)
- Atribuição nativa do Meta via CTWA reporting
- WABA + BSP necessário para conversão offline
- Usar `referral` parameter da WABA API para vincular ad → conversa → conversão
- Sem sGTM/CAPI para CTWA puro

### Cenário C: LP → WhatsApp com CRM
- Melhor cenário: captura dados na LP, redireciona para WhatsApp
- CRM registra lead com UTMs e attribution IDs
- Offline Conversion fecha o loop com Google/Meta

> **Regra:** Sempre documentar qual cenário WhatsApp se aplica ao cliente. CTWA tem limitações fundamentais que afetam toda a arquitetura.

---

## 8. Server-Side Tagging — Arquitetura

### GTM Server-Side (Stape/Cloud Run)
```
Navegador → GTM Web → sGTM Container → Endpoints
                                        ├── GA4 (server)
                                        ├── Google Ads (server)
                                        ├── Meta CAPI
                                        ├── LinkedIn CAPI
                                        └── TikTok Events API

Benefícios:
- 1st party cookies (Cookie Keeper/Custom Loader)
- Maior match rate (IP, user agent preservados)
- Menor bloqueio por ad blockers
- Controle total sobre dados enviados
- Compliance: filtragem de PII antes do envio

Requisitos:
- Subdomínio first-party (data.dominio.com)
- Hosting: Stape, Cloud Run, ou equivalente
- SSL válido no subdomínio
- DNS CNAME ou A record apontando para o servidor
```

### Google Tag Gateway
```
Funcionalidades:
- Google-managed server-side
- Sem custom hosting necessário
- Limitado a tags Google (GA4, Google Ads)
- Não suporta Meta CAPI, LinkedIn CAPI, etc.
- Ideal para operações Google-only com baixo overhead técnico

Limitação principal: não serve endpoints de terceiros
```

### Decisão: GTM sGTM vs. Tag Gateway
| Critério | GTM Server-Side | Google Tag Gateway |
|----------|----------------|-------------------|
| Multi-plataforma (Meta, LinkedIn) | ✅ | ❌ |
| Customização total | ✅ | ❌ |
| Complexidade | Alta | Baixa |
| Custo | Hosting + manutenção | Gratuito |
| 1st party cookies | ✅ (Stape) | ✅ (nativo) |
| Recomendação | Operações multi-canal | Operações Google-only |

### GEO Headers (Stape / Server-Side)

O servidor sGTM (Stape ou equivalente) pode enriquecer requests com headers de geolocalização, permitindo preencher campos de localização para Enhanced Conversions sem depender de input do usuário.

```
Headers disponíveis:
- X-GEO-Country     → país (ISO 3166-1 alpha-2: BR)
- X-GEO-Region      → estado/região (ex: SP, RJ)
- X-GEO-City        → cidade (ex: São Paulo)
- X-GEO-PostalCode  → CEP (ex: 01310-100)
- X-GEO-Ipaddress   → IP do visitante

Uso em Enhanced Conversions:
- Google Ads: preencher city, region, postal_code, country
- Meta CAPI: preencher ct, st, zp, country
- LinkedIn CAPI: enriquecer match data

Documentação: https://stape.io/solutions/geo-headers
```

### Region-Specific Tags Behaviour

GA4, Google Ads Enhanced Conversions e demais tags podem ter comportamento condicional por região geográfica do visitante, útil para:

```
Casos de uso:
- Consent rules diferentes por país (LGPD vs. GDPR vs. CCPA)
- Pixels/tags específicos por mercado (ex: pixel Meta BR vs. Meta US)
- Conversion values diferenciados por região
- Idioma de eventos customizados por localização

Implementação:
- Usar variável sGTM com X-GEO-Country para criar triggers condicionais
- Ou usar Region-Specific Data Controls nativo do GA4

Documentação: https://stape.io/blog/region-specific-tags-behaviour-in-google-tag-manager
```
