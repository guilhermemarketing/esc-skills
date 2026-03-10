# GTM Container JSON Schema Reference

## Table of Contents

1. [Top-Level Structure](#top-level-structure)
2. [Container Version Object](#container-version-object)
3. [Tag Object](#tag-object)
4. [Trigger Object](#trigger-object)
5. [Variable Object](#variable-object)
6. [Folder Object](#folder-object)
7. [Built-In Variable Object](#built-in-variable-object)
8. [Parameter Types](#parameter-types)
9. [Templates: Creating New Objects](#templates)
10. [Google Ads Conversion Tag](#google-ads-conversion-tag)
11. [GA4 Event Tag](#ga4-event-tag)
12. [Custom HTML Tag](#custom-html-tag)
13. [DataLayer Variable](#datalayer-variable)
14. [Constant Variable](#constant-variable)
15. [Custom Event Trigger](#custom-event-trigger)
16. [Pageview Trigger with Filter](#pageview-trigger-with-filter)

---

## Top-Level Structure

```json
{
    "exportFormatVersion": 2,
    "exportTime": "2025-01-10 17:33:59",
    "containerVersion": { ... }
}
```

- `exportFormatVersion`: Always `2` for current GTM exports
- `exportTime`: ISO-ish datetime string (space-separated, not T)
- `containerVersion`: The container payload

## Container Version Object

```json
{
    "path": "accounts/{accountId}/containers/{containerId}/versions/0",
    "accountId": "6255658874",
    "containerId": "198792810",
    "containerVersionId": "0",
    "container": {
        "path": "accounts/{accountId}/containers/{containerId}",
        "accountId": "6255658874",
        "containerId": "198792810",
        "name": "Container Name",
        "publicId": "GTM-XXXXXXXX",
        "usageContext": ["WEB"],
        "fingerprint": "1730140466267",
        "tagManagerUrl": "https://tagmanager.google.com/#/container/...",
        "features": { ... },
        "tagIds": ["GTM-XXXXXXXX"]
    },
    "tag": [ ... ],
    "trigger": [ ... ],
    "variable": [ ... ],
    "folder": [ ... ],
    "builtInVariable": [ ... ],
    "customTemplate": [ ... ],
    "fingerprint": "1736530439361",
    "tagManagerUrl": "https://tagmanager.google.com/#/versions/..."
}
```

Key fields:
- `accountId` and `containerId`: Reused in every child object — copy from existing container
- `usageContext`: `["WEB"]` for web containers, `["SERVER"]` for sGTM
- `fingerprint`: Timestamp-based string, use `str(int(time.time() * 1000))` for new objects
- `customTemplate`: Community template definitions (Meta Pixel, etc.) — preserve as-is

## Tag Object

```json
{
    "accountId": "6255658874",
    "containerId": "198792810",
    "tagId": "23",
    "name": "01 | Facebook Pixel ViewContent [web]",
    "type": "cvt_198792810_8",
    "parameter": [ ... ],
    "fingerprint": "1730140625524",
    "firingTriggerId": ["19"],
    "blockingTriggerId": ["5"],
    "parentFolderId": "13",
    "tagFiringOption": "ONCE_PER_EVENT",
    "monitoringMetadata": {"type": "MAP"},
    "consentSettings": {"consentStatus": "NOT_SET"}
}
```

Required fields: `accountId`, `containerId`, `tagId`, `name`, `type`, `parameter`, `firingTriggerId`

Optional fields:
- `blockingTriggerId`: Triggers that prevent firing
- `parentFolderId`: Folder organization
- `tagFiringOption`: `ONCE_PER_EVENT` (default), `ONCE_PER_LOAD`, `UNLIMITED`
- `priority`: Tag firing priority (higher = fires first), as `{"type": "TEMPLATE", "key": "priority", "value": "100"}`
- `monitoringMetadata`: Usually `{"type": "MAP"}`
- `consentSettings`: `{"consentStatus": "NOT_SET"}` or consent-specific config
- `setupTag` / `teardownTag`: For tag sequencing

## Trigger Object

```json
{
    "accountId": "6255658874",
    "containerId": "198792810",
    "triggerId": "19",
    "name": "📋 Formulário",
    "type": "FORM_SUBMISSION",
    "filter": [
        {
            "type": "CONTAINS",
            "parameter": [
                {"type": "TEMPLATE", "key": "arg0", "value": "{{Page Hostname}}"},
                {"type": "TEMPLATE", "key": "arg1", "value": "{{Constante - Domínio do Cliente}}"}
            ]
        }
    ],
    "fingerprint": "1732376276413",
    "parentFolderId": "3"
}
```

Filter operators: `CONTAINS`, `EQUALS`, `STARTS_WITH`, `ENDS_WITH`, `MATCH_REGEX`, `DOES_NOT_CONTAIN`, `DOES_NOT_EQUAL`, `CSS_SELECTOR`

For CUSTOM_EVENT triggers, add:
```json
"customEventFilter": [
    {
        "type": "EQUALS",
        "parameter": [
            {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
            {"type": "TEMPLATE", "key": "arg1", "value": "my_event_name"}
        ]
    }
]
```

For PAGEVIEW with conditions (Some Pages), use `filter` array. For All Pages, omit `filter`.

### GTM Built-In Trigger IDs

These triggers are NOT exported in the JSON but can be referenced in `firingTriggerId`:

| ID | Trigger |
|---|---|
| `2147479553` | All Pages |
| `2147479573` | Initialization - All Pages |
| `2147479572` | Consent Initialization - All Pages |

Use these IDs directly in `firingTriggerId` arrays. Do NOT create custom triggers to replicate them.

## Variable Object

```json
{
    "accountId": "6255658874",
    "containerId": "198792810",
    "variableId": "15",
    "name": "Pixel Meta",
    "type": "c",
    "parameter": [
        {"type": "TEMPLATE", "key": "value", "value": "445192670100758"}
    ],
    "fingerprint": "1730140971090",
    "parentFolderId": "14",
    "formatValue": {}
}
```

`formatValue`: Usually empty `{}`. Can contain case conversion or other formatting rules.

## Folder Object

```json
{
    "accountId": "6255658874",
    "containerId": "198792810",
    "folderId": "58",
    "name": "🔗 UTM Tracking",
    "fingerprint": "1738000000000"
}
```

Folders are organizational only — they don't affect behavior.

## Built-In Variable Object

```json
{
    "accountId": "6255658874",
    "containerId": "198792810",
    "type": "PAGE_URL",
    "name": "Page URL"
}
```

Common built-in types: `PAGE_URL`, `PAGE_HOSTNAME`, `PAGE_PATH`, `REFERRER`, `EVENT`, `CLICK_URL`, `CLICK_TEXT`, `FORM_ID`, `FORM_CLASSES`

These must be enabled in the container to be available. Add to `builtInVariable` array if needed.

## Parameter Types

Parameters are the value system for tags, triggers, and variables:

| Type | Usage |
|---|---|
| `TEMPLATE` | String value (most common). Supports `{{Variable}}` interpolation |
| `BOOLEAN` | `"true"` or `"false"` as strings |
| `INTEGER` | Numeric value as string: `"2"` |
| `LIST` | Array of MAP objects (for repeated parameters) |
| `MAP` | Key-value pair object |

LIST of MAPs example (GA4 event parameters):
```json
{
    "type": "LIST",
    "key": "eventParameters",
    "list": [
        {
            "type": "MAP",
            "map": [
                {"type": "TEMPLATE", "key": "name", "value": "page_location"},
                {"type": "TEMPLATE", "key": "value", "value": "{{Page URL}}"}
            ]
        }
    ]
}
```

---

## Templates

### Google Ads Conversion Tag

```json
{
    "accountId": "ACCOUNT_ID",
    "containerId": "CONTAINER_ID",
    "tagId": "NEW_ID",
    "name": "01 | Google Ads - Leads (form_submit) [web]",
    "type": "awct",
    "parameter": [
        {"type": "BOOLEAN", "key": "enableConversionLinkerAutoLinking", "value": "false"},
        {"type": "TEMPLATE", "key": "conversionCookiePrefix", "value": "_gcl"},
        {"type": "BOOLEAN", "key": "enableProductReportingCheckbox", "value": "false"},
        {"type": "BOOLEAN", "key": "enableNewCustomerReportingCheckbox", "value": "false"},
        {"type": "BOOLEAN", "key": "enableEnhancedConversionsCheckbox", "value": "false"},
        {"type": "BOOLEAN", "key": "enableRdpCheckbox", "value": "false"},
        {"type": "BOOLEAN", "key": "sendPageViewWithOtherData", "value": "false"},
        {"type": "TEMPLATE", "key": "conversionId", "value": "{{Google ADs Tag client}}"},
        {"type": "TEMPLATE", "key": "currencyCode", "value": "BRL"},
        {"type": "TEMPLATE", "key": "conversionLabel", "value": "XXXXXXXXXXXXXX"},
        {"type": "TEMPLATE", "key": "conversionValue", "value": "0"},
        {"type": "TEMPLATE", "key": "orderId", "value": ""}
    ],
    "fingerprint": "TIMESTAMP",
    "firingTriggerId": ["TRIGGER_ID"],
    "parentFolderId": "FOLDER_ID",
    "tagFiringOption": "ONCE_PER_EVENT",
    "monitoringMetadata": {"type": "MAP"},
    "consentSettings": {"consentStatus": "NOT_SET"}
}
```

**IMPORTANT**: `conversionId` must reference a variable, NEVER a hardcoded ID. The `conversionLabel` is unique per conversion action and IS hardcoded.

### GA4 Event Tag

```json
{
    "accountId": "ACCOUNT_ID",
    "containerId": "CONTAINER_ID",
    "tagId": "NEW_ID",
    "name": "02 | GA4 | Evento form_submit [web]",
    "type": "gaawe",
    "parameter": [
        {"type": "BOOLEAN", "key": "sendEcommerceData", "value": "false"},
        {"type": "TEMPLATE", "key": "eventName", "value": "generate_lead"},
        {
            "type": "LIST",
            "key": "eventParameters",
            "list": [
                {
                    "type": "MAP",
                    "map": [
                        {"type": "TEMPLATE", "key": "name", "value": "method"},
                        {"type": "TEMPLATE", "key": "value", "value": "form"}
                    ]
                }
            ]
        },
        {"type": "TEMPLATE", "key": "measurementIdOverride", "value": ""},
        {"type": "TAG_REFERENCE", "key": "eventSettingsTable", "value": "GA4 Event Settings Variable"}
    ],
    "fingerprint": "TIMESTAMP",
    "firingTriggerId": ["TRIGGER_ID"],
    "parentFolderId": "FOLDER_ID",
    "tagFiringOption": "ONCE_PER_EVENT",
    "monitoringMetadata": {"type": "MAP"},
    "consentSettings": {"consentStatus": "NOT_SET"}
}
```

### Custom HTML Tag

```json
{
    "accountId": "ACCOUNT_ID",
    "containerId": "CONTAINER_ID",
    "tagId": "NEW_ID",
    "name": "UTM_Tracking_localStorage [web]",
    "type": "html",
    "parameter": [
        {"type": "TEMPLATE", "key": "html", "value": "<script>\n(function() {\n  // ES5 ONLY CODE HERE\n  var x = 1;\n})();\n</script>"},
        {"type": "BOOLEAN", "key": "supportDocumentWrite", "value": "false"}
    ],
    "fingerprint": "TIMESTAMP",
    "firingTriggerId": ["2"],
    "parentFolderId": "FOLDER_ID",
    "tagFiringOption": "ONCE_PER_EVENT",
    "monitoringMetadata": {"type": "MAP"},
    "consentSettings": {"consentStatus": "NOT_SET"}
}
```

For Custom HTML with priority:
```json
"priority": {"type": "TEMPLATE", "key": "priority", "value": "100"}
```

Note: The `html` parameter value contains newlines as literal `\n` in the JSON string. When building in Python, use multiline strings naturally — `json.dump` handles the escaping.

### DataLayer Variable

```json
{
    "accountId": "ACCOUNT_ID",
    "containerId": "CONTAINER_ID",
    "variableId": "NEW_ID",
    "name": "dlv - my_key",
    "type": "v",
    "parameter": [
        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
        {"type": "TEMPLATE", "key": "name", "value": "my_key"}
    ],
    "fingerprint": "TIMESTAMP",
    "parentFolderId": "FOLDER_ID",
    "formatValue": {}
}
```

The `name` parameter value must exactly match the key used in `dataLayer.push({event: 'x', my_key: 'value'})`.

### Constant Variable

```json
{
    "accountId": "ACCOUNT_ID",
    "containerId": "CONTAINER_ID",
    "variableId": "NEW_ID",
    "name": "Constante - Domínio do Cliente",
    "type": "c",
    "parameter": [
        {"type": "TEMPLATE", "key": "value", "value": "PLACEHOLDER.com.br"}
    ],
    "fingerprint": "TIMESTAMP",
    "parentFolderId": "FOLDER_ID",
    "formatValue": {}
}
```

### Custom Event Trigger

```json
{
    "accountId": "ACCOUNT_ID",
    "containerId": "CONTAINER_ID",
    "triggerId": "NEW_ID",
    "name": "🔗 utm_tracking_ready",
    "type": "CUSTOM_EVENT",
    "customEventFilter": [
        {
            "type": "EQUALS",
            "parameter": [
                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                {"type": "TEMPLATE", "key": "arg1", "value": "utm_tracking_ready"}
            ]
        }
    ],
    "fingerprint": "TIMESTAMP",
    "parentFolderId": "FOLDER_ID"
}
```

### Pageview Trigger with Filter

```json
{
    "accountId": "ACCOUNT_ID",
    "containerId": "CONTAINER_ID",
    "triggerId": "NEW_ID",
    "name": "Pageview - Specific Domain",
    "type": "PAGEVIEW",
    "filter": [
        {
            "type": "CONTAINS",
            "parameter": [
                {"type": "TEMPLATE", "key": "arg0", "value": "{{Page Hostname}}"},
                {"type": "TEMPLATE", "key": "arg1", "value": "{{Constante - Domínio do Cliente}}"}
            ]
        }
    ],
    "fingerprint": "TIMESTAMP",
    "parentFolderId": "FOLDER_ID"
}
```

### 1st Party Cookie Variable

```json
{
    "accountId": "ACCOUNT_ID",
    "containerId": "CONTAINER_ID",
    "variableId": "NEW_ID",
    "name": "cookie myprefix_email",
    "type": "k",
    "parameter": [
        {"type": "BOOLEAN", "key": "decodeCookie", "value": "false"},
        {"type": "TEMPLATE", "key": "name", "value": "myprefix_email"}
    ],
    "fingerprint": "TIMESTAMP",
    "parentFolderId": "FOLDER_ID",
    "formatValue": {}
}
```
