# Kevros MCP Server

Runtime intelligence for autonomous AI agents. Verify actions against policy, record hash-chained provenance, and bind intents cryptographically.

## Quick Start

**No installation required.** Connect directly to the hosted server:

```
https://governance.taskhawktech.com/mcp/
```

### Claude Desktop / Claude Code

Add to your MCP settings:

```json
{
  "mcpServers": {
    "kevros": {
      "url": "https://governance.taskhawktech.com/mcp/"
    }
  }
}
```

### Python SDK

```bash
pip install kevros
```

```python
from kevros import KevrosClient

client = KevrosClient()  # auto-provisions free API key
result = client.verify(action="deploy", context={"target": "production"})
print(result)  # {'decision': 'ALLOW', 'release_token': '...', 'epoch': 42}
```

## Tools (9)

| Tool | Description | Price |
|------|-------------|-------|
| `governance_verify` | Verify an action against policy | $0.01 |
| `governance_attest` | Record hash-chained provenance | $0.02 |
| `governance_bind` | Bind intent to command cryptographically | $0.02 |
| `governance_verify_outcome` | Verify measured outcome against intent | Free |
| `governance_bundle` | Generate compliance evidence bundle | $0.05 |
| `governance_health` | Health check | Free |
| `kevros_status` | API key status and usage | Free |
| `governance_check_peer` | Check peer agent reputation | Free |
| `governance_verify_token` | Verify a release token independently | Free |

## Resources (2)

- `kevros://agent-card` - A2A agent discovery card
- `kevros://trust-status` - Identity and trust status

## Prompts (2)

- `verify-before-act` - Pre-flight governance check template
- `governance-audit` - Compliance audit bundle generator

## Payment

Three payment protocols supported on all paid endpoints:

- **L402** (Lightning) - 16 sats per governance call (~$0.01)
- **x402** (USDC on Base) - $0.01 per call, 14 chain options
- **MPP** (Stripe/Tempo) - Card, bank, or stablecoin

**Free tier: 1,000 calls/month.** Auto-provisioned on first request. No signup, no credit card.

## Security

- Post-quantum signatures: ML-DSA-87 (FIPS 204) + SLH-DSA-SHA2-256f (FIPS 205)
- Hash-chained provenance ledger (append-only, independently verifiable)
- OFAC sanctions screening on every on-chain payment
- Fail-closed enforcement (deny on verification failure)

## Links

- [Live Gateway](https://governance.taskhawktech.com)
- [OpenAPI Spec](https://governance.taskhawktech.com/openapi.json)
- [Agent Card](https://governance.taskhawktech.com/.well-known/agent.json)
- [PyPI Package](https://pypi.org/project/kevros/)

## License

MIT

Built by [TaskHawk Systems](https://www.taskhawktech.com)
