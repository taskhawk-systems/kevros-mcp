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

**Get an API key first (free, 1,000 calls/month):**

```bash
curl -X POST https://governance.taskhawktech.com/signup \
  -H "Content-Type: application/json" \
  -d '{"agent_id": "my-agent"}'
# Returns: {"api_key": "kvrs_...", "tier": "free", "monthly_limit": 1000}
```

```python
from kevros import KevrosClient

client = KevrosClient(api_key="kvrs_...")  # from signup above
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

- **L402** (Lightning) - 15 sats per governance call (~$0.01)
- **x402** (USDC on Base) - $0.01 per call, 13 chain options
- **MPP** (Stripe/Tempo) - Card, bank, or stablecoin

**Free tier: 1,000 calls/month.** Sign up at `POST /signup` with your agent ID. No credit card required.

## Security

- Post-quantum signatures: ML-DSA-87 (FIPS 204) + SLH-DSA-SHA2-256f (FIPS 205)
- Hash-chained provenance ledger (append-only, independently verifiable)
- OFAC sanctions screening on every on-chain payment
- Fail-closed enforcement (deny on verification failure)
- Formally verified: 1.94 billion states, 12 safety invariants, zero violations (TLA+)

## License

MIT
