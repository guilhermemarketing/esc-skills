---
name: guimkt-gtm-expert
description: >
  Create, edit, validate, and manage Google Tag Manager container JSON files for import/export.
  Use when the user wants to create a GTM container from scratch, modify an existing GTM JSON
  (rename tags, add variables, inject scripts, swap IDs), bulk-edit tags/triggers/variables,
  templatize containers for multi-client use, or troubleshoot GTM import errors. Also triggers
  for tasks involving GTM Custom HTML tags, dataLayer variable setup, conversion tracking
  configuration (Google Ads, Meta Pixel, GA4), or server-side GTM transport configuration.
  Covers both GTM Web and sGTM container types. Para cenários de lead generation, SEMPRE
  consultar primeiro a skill guimkt-gtm-expert-template e o template
  GTM-Web_Modelo_Leads_2025_guimarketing.json como base. Triggers adicionais: "configurar GTM",
  "criar container GTM", "GTM para cliente", "GTM leadgen", "container de tracking",
  "setup GTM", "tags do GTM", "editar container GTM", "GTM web".
version: "1.1.0"
updated: "2026-04-25"
---

# GTM Expert

Create and manipulate Google Tag Manager container JSON files programmatically.

---

## ⚡ Regra de Ouro — Template First

> **ANTES de criar ou editar QUALQUER container GTM, verificar se o cenário é de lead generation.**
> Se sim, a PRIMEIRA ação é consultar a skill `guimkt-gtm-expert-template` e usar o template
> `GTM-Web_Modelo_Leads_2025_guimarketing.json` como base.

```
┌─────────────────────────────────────────────────────┐
│ O cenário envolve geração de leads (formulário,     │
│ WhatsApp, telefone, agendamento)?                   │
├──────────┬──────────────────────────────────────────┤
│ SIM      │ → Usar template guimarketing como base   │
│          │   1. Ler guimkt-gtm-expert-template       │
│          │   2. Rodar scripts/customize_template.py  │
│          │   3. Personalizar constantes + standby    │
│          │   4. Validar com scripts/validate_gtm.py  │
├──────────┼──────────────────────────────────────────┤
│ NÃO      │ → Criar container do zero com esta skill │
│ (e-comm, │   (seguir Workflow abaixo)                │
│  app,    │                                          │
│  outro)  │                                          │
└──────────┴──────────────────────────────────────────┘
```

**Links diretos:**
- Template JSON: `../guimkt-gtm-expert-template/templates/GTM-Web_Modelo_Leads_2025_guimarketing.json`
- Script de customização: `../guimkt-gtm-expert-template/scripts/customize_template.py`
- Inventário completo: `../guimkt-gtm-expert-template/references/template_inventory.md`

> **⚠️ NUNCA gerar um container leadgen do zero quando o template existe.**
> O template contém 6.493 linhas de configuração testada em produção — UTM tracking (FC/LC),
> VisitorAPI geolocation, enhanced conversions, lead scoring, dataLayer architecture, e cAPI.
> Recriar isso manualmente é erro garantido.

---

## Intake Obrigatório — 5 IDs Antes de Tudo

> **⚠️ OBRIGATÓRIO:** Sem estes 5 valores, NÃO iniciar manipulação de container.

| # | ID Necessário | Formato | Exemplo |
|---|--------------|---------|----------|
| 1 | **GA4 Measurement ID** | `G-XXXXXXXXXX` | `G-518CMPFCXK` |
| 2 | **Meta Pixel ID** | Numérico (string) | `445192670100758` |
| 3 | **Google Ads ID** | `AW-XXXXXXXXX` | `AW-410539258` |
| 4 | **sGTM Transport URL** | `https://data.dominio.com.br` | `https://data.cliente.com.br` |
| 5 | **Domínio do cliente** | `dominio.com.br` | `cliente.com.br` |

**Regras do Intake:**
- Se o usuário não fornecer os 5 IDs, **perguntar**. Não inventar. Não usar placeholders sem avisar.
- Se `measurement-plan-{{CLIENTE}}.md` existir, **ler e extrair IDs automaticamente**.
- Se o cliente não tem sGTM, aceitar "não tem" e desabilitar tags de transporte.
- Pergunta extra obrigatória: "Existe um measurement plan do cliente? Se sim, forneça o arquivo."
- IDs opcionais (perguntar se aplicável): Google Ads Conversion Label, LinkedIn Insight Tag ID, TikTok Pixel ID, Bing UET ID.


## Critical Rules

### Encoding: Always use `ensure_ascii=True`

GTM's import parser **rejects raw UTF-8 bytes** for non-ASCII characters (emojis, accented chars like ã, é, ç). Always serialize with:

```python
json.dump(data, f, ensure_ascii=True, indent=4)
```

This escapes all non-ASCII as `\uXXXX` sequences (e.g., 🔗 → `\ud83d\udd17`, ã → `\u00e3`). GTM renders them correctly after import.

### JavaScript: ES5 Only

GTM's JavaScript compiler runs in **ECMASCRIPT3/5 mode**. Any ES6+ feature in Custom HTML tags causes `"Erro do compilador JavaScript"`. Forbidden features and their ES5 equivalents:

| ES6+ Feature | ES5 Replacement |
|---|---|
| `const` / `let` | `var` |
| `() => {}` | `function() {}` |
| `` `template ${x}` `` | `'string ' + x` |
| `[...arr]` | manual array copy |
| `{a, b} = obj` | `var a = obj.a` |
| `obj?.prop` | `obj && obj.prop` |
| `Object.entries(o)` | `Object.keys(o)` + loop |
| `for (x of arr)` | `for (var i = 0; i < arr.length; i++)` |

After writing any Custom HTML script, run the ES5 verification script: `scripts/verify_es5.py`

### ID Management

Every object needs a unique numeric string ID within its type. When adding objects:

1. Scan existing: `max(int(t['tagId']) for t in cv['tag'])`
2. Increment from max
3. IDs are **strings**: `"tagId": "113"` not `"tagId": 113`

### Variable References

GTM interpolates with `{{Variable Name}}`. Works in tag parameters (including Custom HTML `<script>` blocks), trigger filters, and variable definitions.

## JSON Schema

See [references/schema.md](references/schema.md) for the complete structure with all object types, parameter formats, and templates for creating new objects.

## Workflow

### Reading/Modifying a Container

```python
import json

with open('container.json', 'r') as f:
    data = json.load(f)

cv = data['containerVersion']
tags = cv['tag']
triggers = cv['trigger']
variables = cv['variable']
folders = cv['folder']

# Find by name, ID, or type
tag = next(t for t in tags if t['name'] == 'My Tag')
html_tags = [t for t in tags if t['type'] == 'html']
ads_tags = [t for t in tags if t['type'] == 'awct']

# Modify parameter
for p in tag['parameter']:
    if p['key'] == 'conversionId':
        p['value'] = '{{My Variable}}'

# Save (ALWAYS ensure_ascii=True)
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=True, indent=4)
```

### Bulk Find & Replace

```python
text = json.dumps(data, ensure_ascii=False)
text = text.replace('old_brand', 'new_brand')
data = json.loads(text)  # validates JSON integrity
```

**Caution**: Verify replacements don't break `{{variable}}` references, parameter keys, or type identifiers.

### Validation Checklist

Run `scripts/validate_gtm.py` before delivering any JSON. It checks:
1. JSON validity
2. No raw non-ASCII bytes (encoding)
3. Unique IDs per object type
4. All trigger references from tags exist
5. All folder references exist
6. ES5 compliance in Custom HTML tags
7. Orphaned references

## Type Reference (Quick)

### Tag Types

| Code | Platform |
|---|---|
| `html` | Custom HTML |
| `gaawe` | GA4 Event |
| `googtag` | Google Tag (base) |
| `awct` | Google Ads Conversion |
| `gclidw` | Conversion Linker |
| `sp` | Google Ads Remarketing |
| `bzi` | Bing UET |
| `cvt_*` | Community Templates (Meta Pixel, etc.) |

### Variable Types

| Code | Kind |
|---|---|
| `v` | Data Layer Variable |
| `c` | Constant |
| `k` | 1st Party Cookie |
| `j` | JavaScript Variable |
| `jsm` | Custom JavaScript |
| `awec` | Google Ads Enhanced Conversions |
| `gtes` | Google Tag Event Settings |
| `gtcs` | Google Tag Config Settings |
| `remm` | Regex Table |

### Trigger Types

| Code | Kind |
|---|---|
| `PAGEVIEW` | Page View |
| `DOM_READY` | DOM Ready |
| `CUSTOM_EVENT` | Custom Event |
| `FORM_SUBMISSION` | Form Submission |
| `LINK_CLICK` | Link Click |

### Built-In Trigger IDs (Not Exported)

These exist implicitly and can be used in `firingTriggerId` without being defined:

| ID | Trigger |
|---|---|
| `2147479553` | All Pages |
| `2147479573` | Initialization - All Pages |
| `2147479572` | Consent Initialization - All Pages |

## Multi-Client Templatization

Parameterize all client-specific values into constant variables:

| Value | Variable Name Pattern |
|---|---|
| Domain | `Constante - Domínio do Cliente` |
| Google Ads ID | `Google ADs Tag [client]` → `AW-XXXXXXXXX` |
| GA4 ID | `GA4` → `G-XXXXXXXXX` |
| Meta Pixel | `Pixel Meta` → numeric string |
| sGTM URL | `URL de Transporte` → `https://data.domain.com` |

Replace **ALL** hardcoded usages with `{{Variable Name}}` — including inside Custom HTML strings and trigger filter values. The only place a raw value appears is in the constant definition itself.

---

## Validação Anti-Genérico

> **⚡ OBRIGATÓRIO antes de entregar qualquer container de lead generation.**

Todo container GTM para lead generation gerado pelo ecossistema gui.marketing DEVE conter os 8 componentes abaixo. Se algum estiver ausente, o container é considerado **genérico e incompleto** — voltar ao template.

### Checklist de Completude (8 componentes)

| # | Componente | Como verificar |
|---|-----------|----------------|
| 1 | **Script UTM Tracking** (first-click + last-click + organic influence) | Tag `UTM_Tracking_localStorage` + variáveis `fc_*` e `lc_*` |
| 2 | **Script LeadDataCollector** (scrape de formulário + enhanced conversions) | Tag `LeadDataCollector` no folder 📊 data-stack |
| 3 | **VisitorAPI geolocation** | Tags `VisitorAPI.io - Geolocation` + `VisitorAPI - Cookie Setup` |
| 4 | **5 variáveis constantes** (GA4, Pixel, GAds, sGTM, Domínio) | Folder 🛑 APIs, IDs & Tokens com 5 constants |
| 5 | **GA4 Event Settings com user_data + cAPI** | Variáveis `Parâmetros GA4 + cAPI` com email, phone, city, etc. |
| 6 | **Enhanced Conversions data layer variables** | Variáveis `enhanced_conversion_data.*` (email, phone, firstname, lastname) |
| 7 | **Conversion Linker tag** | Tag tipo `gclidw` ativa em All Pages |
| 8 | **9 folders organizacionais** | 📊, 📍, 🔹, 🛑, 🔸, 🟢, 🔵, ⏸, 🔗 |

**Regra:** Se o output não contém esses 8 componentes, **NÃO entregar**. Consultar o template e reconstruir.

---

## Output HTML (Apresentação ao Cliente)

Além do output em JSON (container GTM), **gerar versão HTML estilizada** quando solicitado para apresentação ao cliente:

### Regras do HTML:
1. Usar o design system gui.marketing (Inter Tight/Inter, bg `#f7f3ed`, accent `#864df9`)
2. Organizar tags/triggers/variables em tabelas com o layout brand
3. Header logo com link UTM: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-gtm-expert&utm_content=header-logo`
4. Footer com link UTM: `https://gui.marketing/?utm_source=esc-skills&utm_medium=deliverable&utm_campaign=guimkt-gtm-expert&utm_content=footer`
5. Salvar como `gtm-container-{{CLIENTE}}.html`

> **IMPORTANTE:** O output principal continua sendo o JSON do container GTM. O HTML é um output adicional para exibição/documentação.
