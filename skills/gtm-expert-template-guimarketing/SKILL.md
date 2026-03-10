---
name: gtm-expert-template-guimarketing
description: Customize the guimarketing GTM Leads 2025 template for new clients. Use when onboarding a new client that needs a GTM Web container with GA4, Meta Pixel, Google Ads, VisitorAPI geolocation, UTM tracking, and server-side transport (sGTM). Triggers on "new client GTM", "customize GTM template", "onboard GTM", "GTM template guimarketing", or "setup GTM for client".
---

# GTM Expert — Template guimarketing (Leads 2025)

Customize the pre-built guimarketing GTM Leads 2025 template for new clients. This template includes GA4 + cAPI, Meta Pixel + CAPI, Google Ads conversions, VisitorAPI geolocation, lead scoring, UTM first/last-click tracking, and enhanced conversions.

## Quick Start

```
Input:  Client name, GA4 ID, Meta Pixel ID, Google Ads ID, sGTM domain, client domain
Output: Ready-to-import GTM JSON file
```

Run: `python3 scripts/customize_template.py`

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
