#!/usr/bin/env python3
"""Minimal example: verify an agent action via Kevros governance.

Uses the free tier (1,000 calls/month, no signup required).
"""

import httpx

GATEWAY = "https://governance.taskhawktech.com"

# Step 1: Get a free API key (auto-provisioned)
signup = httpx.post(f"{GATEWAY}/signup", json={"agent_id": "my-agent"})
api_key = signup.json()["api_key"]
print(f"API key: {api_key}")

# Step 2: Verify an action
resp = httpx.post(
    f"{GATEWAY}/governance/verify",
    headers={"X-API-Key": api_key, "Content-Type": "application/json"},
    json={
        "action_type": "deploy",
        "action_payload": {"target": "production", "service": "api"},
        "agent_id": "my-agent",
    },
)

result = resp.json()
print(f"Decision: {result['decision']}")        # ALLOW, CLAMP, or DENY
print(f"Release token: {result['release_token'][:40]}...")
print(f"Epoch: {result['epoch']}")
