# Template Inventory — guimarketing GTM Leads 2025

Complete inventory of the base template `GTM-Web_Modelo_Leads_2025_guimarketing.json`.

## Folders (9)

| ID | Name | Purpose |
|---|---|---|
| 3 | 📊 guimarketing data-stack | Core data: enhanced conversions, cookies, event_id, GA4 event settings |
| 5 | 📍 VisitorAPI | Geolocation via VisitorAPI.io — city, state, country, device info |
| 13 | 🔹 Meta ADs | Meta Pixel events: PageView, ViewContent, Lead, CompleteRegistration |
| 14 | 🛑 APIs, IDs & Tokens | Client-specific constants: GA4 ID, Pixel ID, Ads ID, domain, sGTM |
| 30 | 🔸 Google Analytics | GA4 configuration + event tags |
| 36 | 🟢 Google ADs | Google Ads conversion + remarketing tags |
| 48 | 🔵 Landingi Parameters | Form scraping (email, phone), lead scoring regex tables |
| 57 | ⏸ Standby | Paused tags ready to activate (TikTok, Bing, LinkedIn, etc.) |
| 58 | 🔗 UTM Tracking | First-click/last-click attribution + organic influence |

## Tags Summary

### Active Tags

| Tag Name | Type | Folder | Trigger | Description |
|---|---|---|---|---|
| 00 \| Tag do Google (Config) | googtag | 🔸 GA | All Pages | GA4 base config w/ setup variable |
| 01 \| Facebook Pixel ViewContent | cvt_* | 🔹 Meta | Page view w/ domain | FB Pixel ViewContent |
| 01 \| GA4 - page_view | gaawe | 🔸 GA | All Pages | GA4 page_view event |
| 01 \| Google ADs - Remarketing | sp | 🟢 GADs | All Pages | Remarketing tag |
| 02 \| Facebook Pixel Lead | cvt_* | 🔹 Meta | Form submission | FB Lead event + user data |
| 02 \| GA4 - generate_lead | gaawe | 🔸 GA | Form submission | GA4 lead event |
| 02 \| Google ADs - Leads | awct | 🟢 GADs | Form submission | Ads conversion |
| Conversion Linker | gclidw | 🟢 GADs | All Pages | Links click IDs for attribution |
| VisitorAPI.io - Geolocation | html | 📍 Visitor | Initialization | Fetches geo data + stores in cookies/DL |
| VisitorAPI - Cookie Setup | html | 📍 Visitor | visitor-api-success | Stores geo in cookies for persistence |
| UTM_Tracking_localStorage | html | 🔗 UTM | Initialization | First/last click UTM capture |
| UTM_DataLayer_Push | html | 🔗 UTM | DOM Ready | Pushes UTM data to dataLayer |
| GA4 - page_view w/ UTM | gaawe | 🔗 UTM | utm_tracking_ready | Enhanced page_view with UTM params |
| LeadDataCollector | html | 📊 Data | Form submission | Scrapes form fields + populates enhanced conversions DL |

### Standby (Paused) Tags

| Tag Name | Type | Notes |
|---|---|---|
| Facebook Pixel PageView (standby) | cvt_* | Alternate Pixel PageView |
| Facebook Pixel Lead (standby) | cvt_* | Alternate Lead config |
| TikTok Pixel | html | Activate when client uses TikTok Ads |
| Bing UET | bzi | Activate when client uses Microsoft Ads |
| LinkedIn Insight | html | Activate when client uses LinkedIn Ads |

## Variables Summary

### Constants (🛑 APIs, IDs & Tokens)

| Name | Type | Default Value | Purpose |
|---|---|---|---|
| GA4 | Constant (c) | G-518CMPFCXK | GA4 Measurement ID |
| Pixel Meta | Constant (c) | 445192670100758 | Meta Pixel ID |
| Google ADs Tag guimarketing | Constant (c) | AW-410539258 | Google Ads account ID |
| URL de Transporte | Constant (c) | <https://data.DOMINIO_DO_CLIENTE.com.br> | sGTM transport URL |
| Constante - Domínio do Cliente | Constant (c) | DOMINIO_DO_CLIENTE.com.br | Client domain |
| Tag do Google - Setup Padrão | Config Settings (gtcs) | — | GA4 config w/ send_page_view + user_id |

### Enhanced Conversions Data (📊 data-stack)

| Name | Type | DL/Cookie Key |
|---|---|---|
| enhanced_conversion_data.email | JS Variable (j) | enhanced_conversion_data.email |
| enhanced_conversion_data.phone_number | JS Variable (j) | enhanced_conversion_data.phone_number |
| enhanced_conversion_data.firstname | JS Variable (j) | enhanced_conversion_data.firstname |
| enhanced_conversion_data.lastname | JS Variable (j) | enhanced_conversion_data.lastname |
| enhanced_conversion_data.tamanhoempresa | JS Variable (j) | enhanced_conversion_data.tamanhoempresa |
| enhanced_conversion_data.consumo | JS Variable (j) | enhanced_conversion_data.consumo |

### User Data Cookies (📊 data-stack)

| Name | Type | Cookie Key |
|---|---|---|
| cookie guimarketing_email | Cookie (k) | guimarketing_email |
| cookie guimarketing_firstname | Cookie (k) | guimarketing_firstname |
| cookie guimarketing_lastname | Cookie (k) | guimarketing_lastname |
| cookie guimarketing_phone | Cookie (k) | guimarketing_phone |
| Cookie _ga | Cookie (k) | _ga |
| Cookie _fbp | Cookie (k) | _fbp |
| Cookie _fbc | Cookie (k) | _fbc |

### GA4 Event Settings Variables (📊 data-stack)

| Name | Description |
|---|---|
| Parâmetros GA4 + cAPI (Padrão) | Event settings w/o transport (direct) |
| Parâmetros GA4 + cAPI (Padrão_Transporte) | Event settings w/ sGTM transport URL |

Both send: event_id, first_party_collection, user_data (email, first_name, last_name, phone, city, region, country), FB cookies (fbp, fbc), external_id, user_id

### VisitorAPI Variables (📍 VisitorAPI)

| Name | Type | DL/Cookie Key |
|---|---|---|
| Cookie visitorapi.pais | Cookie (k) | visitorapi.pais |
| Cookie visitorapi.city | Cookie (k) | visitorapi.city |
| Cookie visitorapi.estado | Cookie (k) | visitorapi.estado |
| dlv - visitorApiEstado | DL Variable (v) | visitorApiRegion |
| dlv - visitorApiCity | DL Variable (v) | visitorApiCity |
| dlv - visitorApiCountryCode | DL Variable (v) | visitorApiCountryCode |
| dlv - visitorApiCountryName | DL Variable (v) | visitorApiCountryName |
| dlv - visitorApiDeviceBrand | DL Variable (v) | visitorApiDeviceBrand |
| dlv - visitorApiDeviceModel | DL Variable (v) | visitorApiDeviceModel |
| jsc - visitorApiCity cookiedlv | Custom JS (jsm) | DL with cookie fallback |
| jsc - visitorApiEstado cookiedlv | Custom JS (jsm) | DL with cookie fallback |
| jsc - visitorApiCountryCode cookiedlv | Custom JS (jsm) | DL with cookie fallback |

### UTM Tracking Variables (🔗 UTM Tracking)

| Name | Type | DL Key |
|---|---|---|
| UTM - FC Source | DL Variable (v) | fc_source |
| UTM - FC Medium | DL Variable (v) | fc_medium |
| UTM - FC Campaign | DL Variable (v) | fc_campaign |
| UTM - FC Content | DL Variable (v) | fc_content |
| UTM - FC FBCLID | DL Variable (v) | fc_fbclid |
| UTM - FC GCLID | DL Variable (v) | fc_gclid |
| UTM - LC Source | DL Variable (v) | lc_source |
| UTM - LC Medium | DL Variable (v) | lc_medium |
| UTM - LC Campaign | DL Variable (v) | lc_campaign |
| UTM - LC Content | DL Variable (v) | lc_content |
| UTM - LC FBCLID | DL Variable (v) | lc_fbclid |
| UTM - LC GCLID | DL Variable (v) | lc_gclid |
| UTM - Organic Influenced | DL Variable (v) | organic_influenced_by_ad |
| UTM - Ad Touches | DL Variable (v) | total_ad_touches |

### Landingi Variables (🔵 Landingi Parameters)

| Name | Type | Purpose |
|---|---|---|
| landingi form - email | Custom JS (jsm) | Scrapes email from form inputs |
| landingi form - telefone | Custom JS (jsm) | Scrapes phone from form inputs |
| landingi-form-data | Enhanced Conversions (awec) | Wraps form email + phone |
| guimarketing_tamanho_empresa | Cookie (k) | Company size from form |
| guimarketing_consumo | Cookie (k) | Energy consumption from form |
| JS - Consumo | Custom JS (jsm) | Reads select[name="consumo"] value |
| Regex LP Table - Pontuação Consumo | Regex Table (remm) | Lead scoring by consumption tier |

## Triggers Summary

### Core Triggers

| Name | Type | Condition |
|---|---|---|
| 📋 Formulário | FORM_SUBMISSION | Page hostname contains client domain |
| 📋 Page view [thank-you] | PAGEVIEW | URL contains "send" + "hash" |
| visitor-api-success | CUSTOM_EVENT | Event = "visitor-api-success" |
| page_view visitorApi_intertravamento | CUSTOM_EVENT | visitor-api-success OR gtm.js + city cookie present |
| 🔗 utm_tracking_ready | CUSTOM_EVENT | Event = "utm_tracking_ready" |

### Lead Scoring Triggers (🔵 Landingi)

| Name | Type | Filters |
|---|---|---|
| 🤝 Send Lead Abaixo 500 | PAGEVIEW | URL send+hash, consumo matches "Abaixo" |
| 🤝 Send Lead 500-1000 | PAGEVIEW | URL send+hash, consumo matches "500 até" |
| 🤝 Send Lead 3.000 | PAGEVIEW | URL send+hash, consumo matches "3.000" |
| 🤝 Send Lead 20.000+ | PAGEVIEW | URL send+hash, consumo matches "20.000" |
| 🤝 Send Lead 51-100 | PAGEVIEW | URL send+hash, tamanho_empresa matches "100" |
| 🤝 Send Lead 501+ | PAGEVIEW | URL send+hash, tamanho_empresa matches "501" |
| 🤝 Send Lead 6-15 | PAGEVIEW | URL send+hash, tamanho_empresa matches "15" |

## Data Flow

```
User visits page
  → UTM_Tracking_localStorage captures UTMs (Initialization)
  → VisitorAPI.io fetches geolocation (Initialization)
  → visitor-api-success → cookies set
  → UTM_DataLayer_Push (DOM Ready) → utm_tracking_ready event
  → GA4 page_view + UTM params fire
  → Pixel ViewContent fires

User submits form
  → LeadDataCollector scrapes form → cookies + enhanced_conversion_data
  → 📋 Formulário trigger fires
  → GA4 generate_lead + Meta Lead + Google Ads Conversion fire
  → All send user_data via cAPI event settings
```
