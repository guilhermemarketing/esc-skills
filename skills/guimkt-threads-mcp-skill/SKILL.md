---
name: guimkt-threads-mcp-skill
description: Maintain and operate the Threads MCP Server installed at ~/mcp-servers/threads-mcp-server/. Covers token renewal (every 60 days via cloudflared + OAuth), troubleshooting, tool usage, and configuration across Antigravity and Claude Desktop. Use when the user mentions "Threads MCP", "renovar token Threads", "threads-mcp-server", "Threads API", "postar no Threads", "analytics Threads", "manutenção Threads MCP", or any operation involving the Threads social network MCP integration.
---

# Threads MCP Server — Maintenance & Operations

## Overview

MCP server for **Meta Threads API** with 15 tools. Installed globally at `~/mcp-servers/threads-mcp-server/`.

- **Repo**: [SvetimFM/threads-mcp-server](https://github.com/SvetimFM/threads-mcp-server)
- **Stack**: Node.js + TypeScript + MCP SDK (stdio transport)
- **Account**: @{{YOUR_THREADS_HANDLE}} (primary)
- **Meta App**: "{{YOUR_META_APP_NAME}}" (App ID: `{{YOUR_META_APP_ID}}`)
- **Threads App ID**: `{{YOUR_THREADS_APP_ID}}`

## Configuration Files

| File | Purpose |
|------|---------|
| `~/mcp-servers/threads-mcp-server/.env` | Credentials + tokens |
| `~/.gemini/settings.json` | Antigravity MCP registration |
| `~/Library/Application Support/Claude/claude_desktop_config.json` | Claude Desktop MCP registration |
| `~/mcp-servers/threads-mcp-server/dist/index.js` | Built server entry point |

## MCP Registration (both clients)

```json
{
  "command": "node",
  "args": ["{{ABSOLUTE_PATH_TO}}/threads-mcp-server/dist/index.js"],
  "timeout": 30000
}
```

## Token Renewal (every 60 days)

Token is a long-lived OAuth token. When it expires:

```bash
# Terminal 1: HTTPS tunnel (temporary, only during auth)
cloudflared tunnel --url http://localhost:3001

# Terminal 2: OAuth flow (opens browser for authorization)
cd ~/mcp-servers/threads-mcp-server && npm run auth:primary
```

**Steps:**
1. Start cloudflared → note the `*.trycloudflare.com` URL
2. Update `THREADS_REDIRECT_URI` in `.env` with the new URL + `/callback`
3. Update redirect URI in [Meta Developer App](https://developers.facebook.com/apps/{{YOUR_META_APP_ID}}/) → Threads API Settings (all 3 URL fields)
4. Run `npm run auth:primary` → authorize in browser
5. Token saved to `.env` automatically (valid 60 days)
6. Kill cloudflared (Ctrl+C)

## Available Tools

| Tool | Description |
|------|-------------|
| `threads_list_accounts` | List configured accounts |
| `threads_get_profile` | Profile info (username, bio, followers) |
| `threads_get_posts` | Recent posts |
| `threads_get_post_insights` | Post engagement metrics |
| `threads_batch_insights` | Batch engagement for recent posts |
| `threads_get_account_insights` | Account-level metrics (day/week/28d) |
| `threads_get_replies` | Replies to a post |
| `threads_get_my_replies` | Your replies to others |
| `threads_create_post` | Publish post (text, image, video) |
| `threads_create_thread` | Publish multi-post thread chain |
| `threads_schedule_post` | Schedule a post for future publishing |
| `threads_schedule_thread` | Schedule a multi-post reply chain |
| `threads_publish_scheduled` | Publish all due scheduled posts |
| `threads_list_scheduled` | List pending scheduled posts |
| `threads_cancel_scheduled` | Cancel a scheduled post by ID |
| `threads_publishing_limit` | Check 24h publish quota (250 max) |
| `threads_get_events` | Webhook events (mentions, replies) |
| `threads_setup_webhooks` | Register Meta webhooks |
| `threads_poll_account` | Poll for new posts since last check |
| `threads_daily_digest` | 24h aggregated digest for all accounts |

All tools accept optional `account` param: `"primary"` (default) or `"mirror"`.

## Scheduling Workflow

The Threads API has no native scheduling. This MCP implements client-side scheduling:

```
# Single post (container pre-created, supports reply_to)
threads_schedule_post(text, schedule_at, reply_to?)

# Thread/reply chain (texts stored, chain built at publish time)
threads_schedule_thread(posts[], schedule_at)

# Publish all due items
threads_publish_scheduled()
```

**Key**: Threads can't pre-create containers because each post needs the previous post's ID. Texts are stored and the chain is built at publish time.

**No background cron** — the agent must call `threads_publish_scheduled` when posts are due.

## Troubleshooting

### MCP not loading
- Verify `dist/index.js` exists: `ls ~/mcp-servers/threads-mcp-server/dist/index.js`
- Rebuild if needed: `cd ~/mcp-servers/threads-mcp-server && npm run build`
- Check `.env` has `THREADS_PRIMARY_ACCESS_TOKEN` and `THREADS_PRIMARY_USER_ID`

### Token expired
- Error: API returns `OAuthException` or `Invalid token`
- Fix: Follow "Token Renewal" section above

### OAuth redirect error
- Meta requires HTTPS for redirect URIs → use `cloudflared tunnel`
- All 3 URL fields in Meta app must be filled (redirect, deauthorize, data deletion)
- User must be added as **Testador do Threads** in Meta App → Funções do app

### Port 3002 conflict (webhook server)
- The MCP starts a webhook HTTP server on port 3002 (gracefully skipped if busy)
- This is optional and doesn't affect core functionality

## Dual Account Support

To add a mirror/secondary account:
```bash
cd ~/mcp-servers/threads-mcp-server && npm run auth:mirror
```
Uses `THREADS_MIRROR_ACCESS_TOKEN` and `THREADS_MIRROR_USER_ID` in `.env`.
