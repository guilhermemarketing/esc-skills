---
name: gtm-expert
description: Create, edit, validate, and manage Google Tag Manager container JSON files for import/export. Use when the user wants to create a GTM container from scratch, modify an existing GTM JSON (rename tags, add variables, inject scripts, swap IDs), bulk-edit tags/triggers/variables, templatize containers for multi-client use, or troubleshoot GTM import errors. Also triggers for tasks involving GTM Custom HTML tags, dataLayer variable setup, conversion tracking configuration (Google Ads, Meta Pixel, GA4), or server-side GTM transport configuration. Covers both GTM Web and sGTM container types.
---

# GTM Expert

Create and manipulate Google Tag Manager container JSON files programmatically.

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
