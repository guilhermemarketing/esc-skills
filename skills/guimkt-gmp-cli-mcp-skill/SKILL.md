<!-- skill: guimkt-gmp-cli-mcp-skill | version: 1.0.0 | updated: 2026-03-17 -->
---
name: guimkt-gmp-cli-mcp-skill
description: Operate the gmp-cli (Google Marketing Platform CLI) installed at ~/mcp-servers/gmp-cli/. Covers GA4 analytics, Google Search Console, Google Ads, and Google Tag Manager via terminal commands. Includes authentication setup, GAQL queries, report generation, output formatting, and agent best practices. Use when the user mentions "gmp-cli", "gmp ga", "gmp gsc", "gmp ads", "gmp gtm", "Google Marketing Platform CLI", "relatório GA4 via CLI", "search console report", "Google Ads CLI", "campaign performance", "keyword report", "search terms", "GTM tags", "GAQL query", or any operation involving the gmp command-line tool.
---

# GMP-CLI — Google Marketing Platform CLI

## Overview

CLI for **GA4, Search Console, Google Ads, and Tag Manager**. Installed globally at `~/mcp-servers/gmp-cli/`.

- **Repo**: [lucianfialho/gmp-cli](https://github.com/lucianfialho/gmp-cli)
- **Stack**: Node.js + TypeScript (Commander.js)
- **Global command**: `gmp`
- **Tokens**: `~/.config/gmp-cli/tokens.json` (auto-refresh)

## Authentication

### First-time setup

1. [Google Cloud Console](https://console.cloud.google.com) → Enable APIs: GA4 Data API, GA4 Admin API, Search Console API, Google Ads API
2. OAuth consent screen → External → add test user email
3. Credentials → OAuth Client ID → Desktop app → redirect URI: `http://localhost:3847/callback`
4. Configure and login:

```bash
gmp auth set-credentials --client-id CLIENT_ID --client-secret CLIENT_SECRET
gmp auth login          # opens browser
gmp auth status         # verify
```

### Google Ads (extra)

```bash
# Developer token from ads.google.com/aw/apicenter
gmp auth set-developer-token DEV_TOKEN

# If using MCC (Manager Account)
gmp auth set-login-customer-id 1234567890
```

## Output Formats

All commands support `-f` / `--format`:

| Flag | Format | Best for |
|------|--------|----------|
| `-f json` | JSON (default) | Agent parsing, piping to `jq` |
| `-f table` | ASCII table | Human-readable terminal display |
| `-f csv` | CSV | Export to spreadsheets, `> file.csv` |

**Agent best practice**: Use `-f json` for parsing data programmatically. Use `-f table` when displaying results to users.

## Google Analytics (GA4)

### Discovery

```bash
gmp ga accounts                       # list all accounts
gmp ga properties -a ACCOUNT_ID       # list properties for account
gmp ga metadata -p PROPERTY_ID        # available metrics/dimensions
gmp ga check -p PROPERTY_ID -m sessions,bounceRate -d pagePath  # compatibility check
```

### Reports

```bash
# Sessions + bounce rate by page, last 30 days
gmp ga report -p PROPERTY_ID -m sessions,bounceRate -d pagePath -r 30d

# With filter
gmp ga report -p PROPERTY_ID -m sessions -d pagePath --filter "pagePath==/product"

# Custom date range
gmp ga report -p PROPERTY_ID -m sessions -r 2024-01-01..2024-01-31

# Export CSV
gmp ga report -p PROPERTY_ID -m sessions -d pagePath -f csv > report.csv
```

### Realtime

```bash
gmp ga realtime -p PROPERTY_ID -m activeUsers -d country -f table
```

**Key options**: `-p` property ID, `-m` metrics (comma-separated), `-d` dimensions, `-r` date range, `-l` limit, `--filter` dimension filter.

## Google Search Console

```bash
gmp gsc sites                         # list verified sites

# Top queries (last 28 days)
gmp gsc report -s "https://example.com/" -d query -l 10 -f table

# Pages with most clicks
gmp gsc report -s "https://example.com/" -d page -l 10 -f table

# Filter by query or page
gmp gsc report -s "https://example.com/" -d query --query "keyword" -f table
gmp gsc report -s "https://example.com/" -d query --page "/blog" -f table

# Custom date range
gmp gsc report -s "https://example.com/" -d query -r 2024-01-01..2024-01-31

# URL indexation check
gmp gsc inspect -u "https://example.com/page" -s "https://example.com/"

# Sitemaps
gmp gsc sitemaps -s "https://example.com/"
```

**Key options**: `-s` site URL (required, with trailing `/`), `-d` dimensions (query, page, date, device, country), `-l` limit, `-r` date range.

## Google Ads

### Discovery

```bash
gmp ads accounts                    # simple list (no MCC needed)
gmp ads accounts -c MCC_ID -f table # detailed list via MCC
```

### Performance reports

```bash
# Campaigns (last 30 days, only enabled)
gmp ads campaigns -c CUSTOMER_ID -r LAST_30_DAYS --status ENABLED -f table

# Ad groups (filtered by campaign name)
gmp ads adgroups -c CUSTOMER_ID --campaign "Brand" -f table

# Keywords with quality score
gmp ads keywords -c CUSTOMER_ID --campaign "Brand" -l 20 -f table

# Search terms (actual queries that triggered ads)
gmp ads search-terms -c CUSTOMER_ID -f table
```

### Raw GAQL query

```bash
gmp ads query -c CUSTOMER_ID -q "SELECT campaign.name, metrics.clicks FROM campaign WHERE segments.date DURING LAST_7_DAYS"
```

**Key options**: `-c` customer ID (required), `-r` date range (`LAST_7_DAYS`, `LAST_30_DAYS`, `THIS_MONTH`, `LAST_MONTH`), `--status` filter, `--campaign` name filter (contains), `-l` limit.

**Note**: Cost values are returned in micros (divide by 1,000,000). The CLI auto-converts in formatted reports, but raw GAQL returns raw micros.

## Google Tag Manager

```bash
gmp gtm accounts                                 # list accounts
gmp gtm containers -a ACCOUNT_ID                  # list containers

# Tags, triggers, variables (default workspace)
gmp gtm tags -p accounts/X/containers/Y -f table
gmp gtm triggers -p accounts/X/containers/Y -f table
gmp gtm variables -p accounts/X/containers/Y -f table

# Specific workspace
gmp gtm tags -p accounts/X/containers/Y -w 3 -f table

# Published versions
gmp gtm versions -p accounts/X/containers/Y -f table
```

**Key options**: `-p` container path (format: `accounts/X/containers/Y`), `-w` workspace number.

## Agent Best Practices

### Workflow pattern

1. **Always check auth first**: `gmp auth status`
2. **Discover resources**: List accounts/properties before running reports
3. **Use JSON format** for parsing: `-f json` (default, pipe to `jq` for extraction)
4. **Use table format** for user-facing output: `-f table`
5. **Check metric compatibility** before GA4 reports: `gmp ga check -p ID -m metrics -d dimensions`

### Common agent workflows

**Full GA4 audit**:
```bash
gmp ga accounts                          # find account
gmp ga properties -a ACCOUNT_ID          # find property
gmp ga metadata -p PROPERTY_ID           # available metrics
gmp ga report -p PROPERTY_ID -m sessions,totalUsers,bounceRate -d pagePath -r 30d -f json
```

**Google Ads performance review**:
```bash
gmp ads accounts                         # find customer ID
gmp ads campaigns -c CID -r LAST_30_DAYS -f json   # overview
gmp ads keywords -c CID --campaign "Brand" -f json  # keyword drill-down
gmp ads search-terms -c CID -f json                 # actual search queries
```

**SEO snapshot** (Search Console):
```bash
gmp gsc sites                            # find site URL
gmp gsc report -s "https://site.com/" -d query -l 20 -f json     # top queries
gmp gsc report -s "https://site.com/" -d page -l 20 -f json      # top pages
gmp gsc inspect -u "https://site.com/page" -s "https://site.com/" # indexation
```

### Error handling

| Error | Cause | Fix |
|-------|-------|-----|
| `Failed to get access token` | Token expired or missing | `gmp auth login` |
| `developer token not set` | Google Ads needs extra auth | `gmp auth set-developer-token TOKEN` |
| `API error (403)` | Missing API enablement or permissions | Enable API in Google Cloud Console |
| `API error (400)` | Invalid GAQL or incompatible metrics | Use `gmp ga check` to validate combinations |

## Troubleshooting

### CLI not found
```bash
# Verify installation
which gmp
# Rebuild + relink if needed
cd ~/mcp-servers/gmp-cli && npm run build && npm link
```

### Token issues
- Tokens auto-refresh but may expire if credentials change
- Delete `~/.config/gmp-cli/tokens.json` and re-login for a clean start

## Updating

```bash
cd ~/mcp-servers/gmp-cli && git pull && npm install && npm run build
```
