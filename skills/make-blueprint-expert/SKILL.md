---
name: make-blueprint-expert
description: Interpret, create, edit, validate, and optimize Make.com (formerly Integromat) scenario blueprint JSON files. Use when the user wants to create a Make scenario from scratch via blueprint, modify an existing blueprint JSON (fix field mappings, add modules, change body content, swap API endpoints), debug Make execution errors (InvalidConfigurationError, HTTP 400, field mapping issues), understand Make scenario structure, fix jsonStringBodyContent encoding issues, or generate correct Make expressions ({{module.field}}) inside JSON bodies. Also triggers for tasks involving Make HTTP modules, router/filter configuration, Facebook Lead Ads integration with CRM APIs, DataCrazy CRM integration, webhook configuration, variable modules (Set Variable, roleta/round-robin), or any Make.com automation troubleshooting. Use this skill whenever the user mentions "Make.com", "Make scenario", "blueprint JSON", "Make blueprint", "cenário Make", "módulo HTTP Make", "jsonStringBodyContent", "Make expressions", "InvalidConfigurationError Make", or any variation of creating, editing, debugging, or optimizing Make.com automations via blueprint files.
---

# Make.com Blueprint Expert

Create, edit, debug, and optimize Make.com scenario blueprints programmatically via JSON.

## Critical Rules

### 1. JSON Body Content: NEVER Use Quoted Strings Inside Make Expressions

The `jsonStringBodyContent` field is a **double-encoded JSON string** — a JSON string whose content is another JSON structure containing Make expressions `{{}}`. Make validates the body as JSON **before** evaluating expressions, so escaped quotes inside `{{}}` break the parser.

```json
// ❌ BREAKS — quotes inside {{}} terminate JSON string prematurely
{"name":"{{ifempty(1.field_name; \"fallback\")}}"}

// ✅ WORKS — direct value, no quoted fallback
{"name":"{{1.field_name}}"}

// ✅ WORKS — ifempty with another field reference (no quotes)
{"type":"{{ifempty(1.data.field_a[]; 1.data.field_b[])}}"}
```

If a string fallback is needed, set it in a **Set Variable** module before the HTTP module, then reference the variable.

### 2. Double-Encoding: Always Use Python json.dumps()

The `jsonStringBodyContent` blueprint value has two encoding layers:
- **Layer 1**: The body content itself is a JSON object (with Make expressions as values)
- **Layer 2**: That JSON is stored as a string value inside the blueprint JSON file

Always use Python's `json.dumps()` twice to generate correctly escaped values:

```python
import json

body_obj = {
    "name": "{{1.data.full_name}}",
    "email": "{{1.data.email}}",
    "config": {"id": "{{25.my_variable}}"}
}
# Double-encode: inner json.dumps creates the JSON string,
# outer json.dumps escapes it for the blueprint
blueprint_value = json.dumps(json.dumps(body_obj, separators=(',', ':')))
```

### 3. Array Indexing Is 1-Based

Make uses 1-based indexing for arrays. Empty brackets `[]` do NOT select a single item — they **flatten/iterate** arrays into strings.

```
// ❌ WRONG — does NOT select a single value
{{50.data.results[].id}}

// ✅ CORRECT — selects the first element (1-indexed)
{{50.data.results[1].id}}

// ✅ CORRECT — flattens array to comma-separated string (for display/concat)
{{1.data.tags[]}}
```

### 4. NEVER Edit Blueprints with Text-Based File Edit Tools

Blueprint JSON files have very long lines with complex multi-level escaping. Text-based find-and-replace tools (`multi_replace_file_content`, `replace_file_content`) will corrupt the file because:
- Special characters in target content don't match exactly
- Partial matches can replace schema definitions instead of actual body content
- Broken continuation lines get injected

**Always use Python** to read, modify, and write blueprint JSON:

```python
import json

with open('blueprint.json', 'r', encoding='utf-8') as f:
    bp = json.load(f)

# Navigate the structure programmatically
for item in bp['flow']:
    for route in item.get('routes', []):
        for module in route.get('flow', []):
            mapper = module.get('mapper', {})
            if 'jsonStringBodyContent' in mapper:
                body = json.loads(mapper['jsonStringBodyContent'])
                # Modify body fields as needed
                body['name'] = '{{1.data.full_name}}'
                mapper['jsonStringBodyContent'] = json.dumps(body, separators=(',', ':'))

with open('blueprint.json', 'w', encoding='utf-8') as f:
    json.dump(bp, f, indent=4, ensure_ascii=False)
```

## Blueprint Structure

### Top-Level Anatomy

```json
{
    "name": "Scenario Name",
    "flow": [
        { "id": 1, "module": "trigger-module:watch", ... },
        { "id": 2, "module": "google-sheets:addRow", ... },
        { "id": 25, "module": "util:SetVariable2", ... },
        { "id": 50, "module": "http:ActionSendData", ... },
        {
            "id": 60, "module": "builtin:BasicRouter",
            "routes": [
                {
                    "flow": [ { "id": 70, ... }, { "id": 71, ... } ],
                    "filter": { "conditions": [...] }
                },
                {
                    "flow": [ { "id": 80, ... }, { "id": 81, ... } ],
                    "filter": { "conditions": [...] }
                }
            ]
        }
    ],
    "metadata": { "instant": true, "version": 1 }
}
```

### Module Types Reference

| Module String | Type |
|---|---|
| `facebook-lead-ads:watchLeads` | Facebook Lead Ads Trigger |
| `google-sheets:addRow` | Google Sheets - Add Row |
| `http:ActionSendData` | HTTP - Make a Request (POST/PATCH/PUT) |
| `http:ActionGetData` | HTTP - Get Data (GET) |
| `util:SetVariable2` | Tools - Set Variable |
| `builtin:BasicRouter` | Router (with routes/filters) |
| `json:ParseJSON` | JSON - Parse |
| `builtin:BasicFeeder` | Iterator |
| `builtin:BasicAggregator` | Aggregator |
| `gateway:CustomWebHook` | Custom Webhook Trigger |
| `util:FunctionSleep` | Tools - Sleep |

### HTTP Module (`http:ActionSendData`) Mapper Fields

```json
{
    "mapper": {
        "url": "https://api.example.com/v1/resource",
        "method": "post",
        "headers": [
            {"name": "Authorization", "value": "Bearer {{token}}"},
            {"name": "Content-Type", "value": "application/json"}
        ],
        "contentType": "json",
        "inputMethod": "jsonString",
        "jsonStringBodyContent": "{...double-encoded JSON...}",
        "parseResponse": true,
        "stopOnHttpError": true,
        "allowRedirects": true,
        "shareCookies": false,
        "requestCompressedContent": true
    }
}
```

### Router Filter Conditions

Filters use nested arrays with operator objects:

```json
{
    "filter": {
        "name": "Route Name",
        "conditions": [
            [
                {
                    "a": "{{50.data.count}}",
                    "b": "0",
                    "o": "number:equal"
                }
            ]
        ]
    }
}
```

Common operators: `number:equal`, `number:notEqual`, `number:greater`, `number:less`, `text:equal`, `text:contain`, `text:startsWith`, `exist`, `notExist`.

### Set Variable Module — Roleta (Round-Robin Distribution)

A **roleta** is a common pattern for distributing incoming data (leads, tasks, tickets) among team members. It uses a `Set Variable` module with `random` to assign items probabilistically.

#### When to Create a Roleta
- The client needs to distribute leads/tasks equally among 2+ agents
- CRM APIs require an `attendantId` or `assigneeId` on creation
- The user mentions "roleta", "round-robin", "distribuição", or "distribuir leads"

#### Blueprint Structure

Place the Set Variable module **before** any HTTP module that needs the assigned value. The variable name should be descriptive (e.g., `roleta_crm`, `assigned_agent`, `responsavel`).

**2-way split (50/50):**
```json
{
    "id": 25,
    "module": "util:SetVariable2",
    "version": 1,
    "parameters": {},
    "mapper": {
        "name": "roleta_crm",
        "scope": "roundtrip",
        "value": "{{if(random > 0.5; \"UUID-AGENT-A\"; \"UUID-AGENT-B\")}}"
    }
}
```

**3-way split (33/33/33):**
```json
{
    "value": "{{if(random < 0.33; \"UUID-A\"; if(random < 0.66; \"UUID-B\"; \"UUID-C\"))}}"
}
```

**4-way split (25% each):**
```json
{
    "value": "{{if(random < 0.25; \"UUID-A\"; if(random < 0.5; \"UUID-B\"; if(random < 0.75; \"UUID-C\"; \"UUID-D\")))}}"
}
```

**Weighted split (70/30):**
```json
{
    "value": "{{if(random > 0.3; \"UUID-SENIOR\"; \"UUID-JUNIOR\")}}"
}
```

#### Wiring into HTTP Modules

Reference the variable in downstream modules using `{{<moduleId>.<variableName>}}`:

```json
// In the HTTP body content (as a plain dict before double-encoding):
{
    "assigneeId": "{{25.roleta_crm}}",
    "attendant": {"id": "{{25.roleta_crm}}"}
}
```

The same variable can be referenced in multiple modules (e.g., both "Create Lead" and "Create Deal" modules).

#### Python Generation Pattern

```python
def create_roleta_module(module_id, var_name, agents, position_x=900, position_y=0):
    """Generate a Set Variable module for round-robin distribution.
    
    Args:
        module_id: Unique module ID (int)
        var_name: Variable name (e.g., 'roleta_crm')
        agents: List of agent UUIDs to distribute among
        position_x, position_y: Canvas position
    """
    if len(agents) == 2:
        value = f'{{{{if(random > 0.5; "{agents[0]}"; "{agents[1]}")}}}}'
    else:
        # Build nested if() for N agents
        parts = []
        for i, agent in enumerate(agents[:-1]):
            threshold = round((i + 1) / len(agents), 2)
            parts.append(f'if(random < {threshold}; "{agent}"; ')
        value = '{{' + ''.join(parts) + f'"{agents[-1]}"' + ')' * (len(agents) - 1) + '}}'
    
    return {
        "id": module_id,
        "module": "util:SetVariable2",
        "version": 1,
        "parameters": {},
        "mapper": {
            "name": var_name,
            "scope": "roundtrip",
            "value": value
        },
        "metadata": {
            "designer": {"x": position_x, "y": position_y},
            "restore": {"expect": {"scope": {"label": "One cycle"}}}
        }
    }
```

## Facebook Lead Ads Field Mapping

Facebook Lead Ads fields are accessed via `<moduleId>.data.<internal_name>`. The internal names are defined during form creation and **may not be in English**.

### Discovering Field Names

Check the module's output interface in the blueprint JSON under `interface.output` → `data.spec`:

```json
{
    "name": "data",
    "type": "collection",
    "label": "Field data",
    "spec": [
        {"name": "full_name", "type": "text", "label": "Full name"},
        {"name": "email", "type": "text", "label": "Email"},
        {"name": "phone", "type": "text", "label": "Phone number"},
        {"name": "custom_field", "type": "array", "label": "Custom question label"}
    ]
}
```

The `name` field is what you use in expressions: `{{1.data.full_name}}`, NOT the `label`.

### Custom Fields (Arrays)

Custom fields from Facebook forms come as arrays. Use `[]` to flatten to a string:

```
{{1.data.custom_field[]}}
```

Fields with hyphens or special characters require backticks:

```
{{1.data.`field-with-hyphens`[]}}
```

### Other Trigger Data

Beyond form fields, the trigger also provides metadata:
- `{{1.leadgenId}}` — Lead ID
- `{{1.campaignName}}` — Campaign name
- `{{1.adsetName}}` — Ad set name
- `{{1.adName}}` — Ad name
- `{{1.platform}}` — Platform (e.g., fb, ig)
- `{{1.isOrganic}}` — Whether the lead is organic

## Debugging Common Make Errors

### InvalidConfigurationError: "JSON body content is not valid JSON"
**Cause**: Escaped quotes inside Make expressions in `jsonStringBodyContent` (e.g., `ifempty(val; "text")`).
**Fix**: Remove all `ifempty` / `if` calls that use string literals with quotes inside the body content. Use direct field references or pre-compute in a Set Variable module.

### HTTP 400: Required field is empty
**Cause**: Wrong field path (e.g., `1.data.full_name` when the internal name is `1.data.nome`) or wrong module ID prefix.
**Fix**: Check the trigger module's `interface.output` spec for correct internal field names.

### HTTP 400: Invalid field value (e.g., "email must be valid")
**Cause**: A fallback like `ifempty(field; "null")` sends literal string "null" as an email address.
**Fix**: Remove the fallback or use an empty string. Facebook Lead Ads forms with required fields always send values.

### Incomplete Executions / DLQ (Dead Letter Queue)
Make pauses sequential scenarios when errors accumulate. Items in the DLQ carry the **original request body** — retrying won't pick up new module mappings.
**Fix**: Delete DLQ items, fix the module, reactivate. Reprocess data from an earlier module (e.g., Google Sheets) if needed.

### Module Output Not Available
**Cause**: Referencing a module that hasn't run yet or is in a different router branch.
**Fix**: Only reference modules that are guaranteed to have executed in the current flow path. Modules in other router branches are not accessible.

## Workflow: Creating a New Blueprint

1. **Define the flow**: List all modules in order with their connections
2. **Build body objects** in Python as plain dicts with Make expressions as string values
3. **Generate the blueprint** structure programmatically using Python
4. **Double-encode** all `jsonStringBodyContent` values with `json.dumps(json.dumps(obj, separators=(',', ':')))`
5. **Validate** the final JSON with `json.load()` before delivering
6. **Test** by importing in Make and running with a sample trigger

## Workflow: Fixing an Existing Blueprint

1. **Load** the blueprint with `json.load()`
2. **Navigate** to the target module: `bp['flow']` → routes → flow → mapper
3. **Parse** existing body: `json.loads(mapper['jsonStringBodyContent'])`
4. **Fix** the body dict (field names, paths, remove broken expressions)
5. **Write back**: `mapper['jsonStringBodyContent'] = json.dumps(body, separators=(',', ':'))`
6. **Save**: `json.dump(bp, f, indent=4, ensure_ascii=False)`
7. **Validate**: Re-load the saved file with `json.load()` to confirm valid JSON
8. **Print** all module bodies for visual verification before delivering

## Validation Script Pattern

Always run this after editing any blueprint:

```python
import json

with open('blueprint.json', 'r') as f:
    bp = json.load(f)
print("✅ Blueprint is valid JSON")

for item in bp['flow']:
    for route in item.get('routes', []):
        for module in route.get('flow', []):
            mapper = module.get('mapper', {})
            body = mapper.get('jsonStringBodyContent', '')
            url = mapper.get('url', '')
            method = mapper.get('method', 'post')
            if body:
                body_json = json.loads(body)
                print(f"\nModule {module['id']} ({method.upper()} {url}):")
                for k, v in body_json.items():
                    print(f"  {k}: {v}")
```
