---
name: guimkt-gtm-expert-template
description: >
  Customize the guimarketing GTM Leads 2025 template for new clients. Use when onboarding
  a new client that needs a GTM Web container with GA4, Meta Pixel, Google Ads, VisitorAPI
  geolocation, UTM tracking, and server-side transport (sGTM). Triggers on "new client GTM",
  "customize GTM template", "onboard GTM", "GTM template guimarketing", "setup GTM for client",
  "configurar GTM", "criar container GTM", "GTM para cliente", "GTM leadgen",
  "container de tracking", "setup GTM", "tags do GTM", "GTM web", "container GTM para leads".
  Esta skill é a FUNDAÇÃO de todo container GTM de lead generation no ecossistema gui.marketing.
---

# GTM Expert — Template guimarketing (Leads 2025)

Customize the pre-built guimarketing GTM Leads 2025 template for new clients. This template includes GA4 + cAPI, Meta Pixel + CAPI, Google Ads conversions, VisitorAPI geolocation, lead scoring, UTM first/last-click tracking, and enhanced conversions.

## Quick Start

```
Input:  Client name, GA4 ID, Meta Pixel ID, Google Ads ID, sGTM domain, client domain
Output: Ready-to-import GTM JSON file
```

Run: `python3 scripts/customize_template.py`

---

## ⚡ Quando esta skill é ativada automaticamente

> **Esta skill DEVE ser consultada por qualquer outra skill do ecossistema gui.marketing que envolva GTM para lead generation.**

| Skill que aciona | Contexto |
|-----------------|----------|
| `guimkt-gtm-expert` | Sempre que o cenário for leadgen (Regra de Ouro) |
| `guimkt-measurement-plan-architect` | Ao especificar plano GTM (Etapa 3.3) |
| `guimkt-conversion-qa-auditor` | Ao verificar conformidade do container (Etapa 1.5) |
| `guimkt-lead-scoring-architecture` | Ao definir variáveis GTM para conversion value mapping |

**Regra:** O template é a fundação. **Personalização é a regra. Criação do zero é a exceção.**

---

## Intake Ativo — Perguntas que o agente DEVE fazer

> **⚠️ OBRIGATÓRIO:** O agente deve solicitar TODOS os 5 IDs antes de iniciar a customização.

| # | ID Necessário | Formato | Exemplo | Obrigatório |
|---|--------------|---------|----------|:-----------:|
| 1 | **GA4 Measurement ID** | `G-XXXXXXXXXX` | `G-518CMPFCXK` | ✅ |
| 2 | **Meta Pixel ID** | Numérico (string) | `445192670100758` | ✅ |
| 3 | **Google Ads ID** | `AW-XXXXXXXXX` | `AW-410539258` | ✅ |
| 4 | **sGTM Transport URL** | `https://data.dominio.com.br` | `https://data.cliente.com.br` | ✅ |
| 5 | **Domínio do cliente** | `dominio.com.br` | `cliente.com.br` | ✅ |
| 6 | **Google Ads Conversion Label** | Alfanumérico | `AbC1dEfGhI` | ⬜ Opcional |
| 7 | **LinkedIn Insight Tag ID** | Numérico | `1234567` | ⬜ Opcional |
| 8 | **TikTok Pixel ID** | Alfanumérico | `CXXXXXXXXX` | ⬜ Opcional |
| 9 | **Bing UET Tag ID** | Numérico | `12345678` | ⬜ Opcional |

**Perguntas adicionais obrigatórias:**
- "O cliente já tem um container GTM existente? Se sim, importar e comparar com o template para identificar gaps."
- "Existe um `measurement-plan-{{CLIENTE}}.md`? Se sim, ler e extrair IDs automaticamente."
- "Quais plataformas além de Google e Meta? (LinkedIn, TikTok, Bing — para ativar tags do Standby)"

**Regra:** Se o usuário não fornecer os 5 IDs obrigatórios, **perguntar explicitamente**. Não usar os IDs de exemplo do template. Não inventar valores.

## Template Architecture

See [references/template_inventory.md](references/template_inventory.md) for the full inventory of tags, triggers, variables, and folders.

### Folder Structure (9 folders)

| Emoji | Folder | Purpose |
|---|---|---|
| 📊 | guimarketing data-stack | Core data collection, enhanced conversions, event_id, user cookies |
| 📍 | VisitorAPI | Geolocation via VisitorAPI (city, state, country, device) |
| 🔹 | Meta ADs | Facebook Pixel events (PageView, Lead, ViewContent) |
| 🛑 | APIs, IDs & Tokens | All client-specific constants (GA4, Pixel, Ads ID, domain, sGTM URL) |
| 🔸 | Google Analytics | GA4 tags (config, page_view, generate_lead, form events) |
| 🟢 | Google ADs | Google Ads conversion tracking + remarketing |
| 🔵 | Landingi Parameters | Landing page form scraping + lead scoring triggers |
| ⏸ | Standby | Paused tags (TikTok, Bing, LinkedIn — activate as needed) |
| 🔗 | UTM Tracking | First-click/last-click attribution + organic influence detection |

### Client-Specific Variables (must customize)

These 5 constant variables in the **🛑 APIs, IDs & Tokens** folder hold all client-specific values:

| Variable Name | Example Value | Notes |
|---|---|---|
| `GA4` | `G-XXXXXXXXXX` | GA4 Measurement ID |
| `Pixel Meta` | `445192670100758` | Meta Pixel ID (numeric string) |
| `Google ADs Tag guimarketing` | `AW-XXXXXXXXX` | Google Ads account ID |
| `URL de Transporte` | `https://data.client.com.br` | sGTM transport URL |
| `Constante - Domínio do Cliente` | `client.com.br` | Client domain |

### Container Metadata (must customize)

| Field | Location | Example |
|---|---|---|
| Container name | `containerVersion.container.name` | `"Client Name - Web"` |
| Public ID | `containerVersion.container.publicId` | `"GTM-XXXXXXXX"` |

## Customization Workflow

### 1. Gather Client Info

Ask for these **required** values:

```
- Client name (for container renaming)
- GA4 Measurement ID (G-XXXXXXXXXX)
- Meta Pixel ID (numeric)
- Google Ads ID (AW-XXXXXXXXX)
- Client domain (example.com.br)
- sGTM transport URL (https://data.example.com.br)
```

**Optional** (activate from Standby folder):

- Google Ads Conversion Label (for specific conversion actions)
- TikTok Pixel ID
- LinkedIn Insight Tag ID
- Bing UET Tag ID

### 2. Run Customization Script

```bash
python3 scripts/customize_template.py \
  --client-name "Acme Corp" \
  --ga4-id "G-XXXXXXXXXX" \
  --meta-pixel "1234567890" \
  --gads-id "AW-1234567890" \
  --domain "acme.com.br" \
  --sgtm-url "https://data.acme.com.br" \
  --output "GTM-Web_Acme_Corp.json"
```

### 3. Validate Output

```bash
python3 ../gtm-expert/scripts/validate_gtm.py GTM-Web_Acme_Corp.json
```

### 4. Manual Review Checklist

After customization, verify:

- [ ] Container name updated
- [ ] All 5 constant variables have correct client values
- [ ] `URL de Transporte` matches sGTM domain
- [ ] `Constante - Domínio do Cliente` matches client domain
- [ ] No leftover `DOMINIO_DO_CLIENTE` or `guimarketing` references in constants
- [ ] Standby tags remain paused unless explicitly activated
- [ ] Google Ads conversion labels updated (if provided)

## Activating Standby Tags

Tags in the **⏸ Standby** folder are `"paused": true`. To activate:

1. Set `"paused": false` (or remove the key)
2. Update the relevant ID constant
3. Verify trigger references are correct

Available standby tags:

- TikTok Pixel (PageView + Lead)
- Bing UET
- LinkedIn Insight Tag
- Additional Meta events

## Critical Rules

All rules from the `gtm-expert` skill apply:

1. **Encoding**: Always `ensure_ascii=True` when writing JSON
2. **ES5 Only**: No `const`, `let`, arrow functions, template literals in Custom HTML
3. **IDs are strings**: `"tagId": "23"` not `"tagId": 23`
4. **Variable refs**: `{{Variable Name}}` — don't break references during find/replace

## Conversion Label Customization

Google Ads conversion tags use `conversionLabel` which is unique per conversion action. The template has placeholder labels. When client provides their conversion labels:

```python
# Find the specific conversion tag
tag = next(t for t in tags if t['name'] == '01 | Google ADs - Leads [web]')
for p in tag['parameter']:
    if p['key'] == 'conversionLabel':
        p['value'] = 'CLIENT_CONVERSION_LABEL'
```

## UTM Tracking System

The template includes a comprehensive UTM tracking system in the **🔗 UTM Tracking** folder:

- **First-click (FC)** and **Last-click (LC)** attribution variables
- **Organic influence detection** (`organic_influenced_by_ad`)
- **Ad touch counting** (`total_ad_touches`)
- Custom event `utm_tracking_ready` fires after UTM data is processed
- Variables: `fc_source`, `fc_medium`, `fc_campaign`, `fc_content`, `fc_fbclid`, `fc_gclid` (and `lc_*` equivalents)

These are sent as GA4 event parameters automatically via the event settings variables.

---

## Output HTML (Apresentação ao Cliente)

Além do output em JSON (container GTM), **gerar versão HTML estilizada** quando solicitado para apresentação ao cliente:

### Regras do HTML:
1. Usar o design system gui.marketing (Inter Tight/Inter, bg `#f7f3ed`, accent `#864df9`)
2. Documentar tags, triggers e variables em tabelas com o layout brand
3. Header logo com link UTM: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-gtm-expert-template&utm_content=header-logo`
4. Footer com link UTM: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-gtm-expert-template&utm_content=footer`
5. Salvar como `gtm-template-{{CLIENTE}}.html`

> **IMPORTANTE:** O output principal continua sendo o JSON do container GTM. O HTML é um output adicional para documentação.
