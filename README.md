# Kevros MCP Server

Governance primitives for autonomous agents. Verify actions against policy, record provenance, and bind intents — all cryptographically signed.

## Quick Start

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "kevros": {
      "type": "streamableHttp",
      "url": "https://governance.taskhawktech.com/mcp/",
      "headers": {
        "X-API-Key": "${KEVROS_API_KEY}"
      }
    }
  }
}
```

Set your API key (free tier: 100 calls/month, instant signup):

```bash
export KEVROS_API_KEY=kvrs_...
```

Or leave it unset — the server auto-provisions a free-tier key on first use.

## Tools

| Tool | Description |
|------|-------------|
| `governance_verify` | Check an action against policy bounds (ALLOW / CLAMP / DENY) |
| `governance_attest` | Record a completed action in a signed evidence ledger |
| `governance_bind` | Cryptographically bind a declared intent to a command |
| `governance_verify_outcome` | Verify an outcome against a prior attestation |
| `governance_bundle` | Retrieve a compliance evidence bundle |

## Pricing

| Tier | Calls/month | Price |
|------|------------|-------|
| Free | 100 | $0 |
| Scout | 5,000 | $29/mo |
| Sentinel | 50,000 | $149/mo |
| Sovereign | 500,000 | $499/mo |

## Links

- [Live Gateway](https://governance.taskhawktech.com)
- [Agent Card](https://governance.taskhawktech.com/.well-known/agent.json)
- [Python SDK](https://pypi.org/project/kevros/) (`pip install kevros`)
- [Website](https://taskhawktech.com)

## License

BSL-1.1
