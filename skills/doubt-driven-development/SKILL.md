---
name: Doubt-Driven Development
description: Subjects every non-trivial decision to an adversarial, fresh-context review before it stands. Biased to disprove assumptions while course correction is cheap.
category: development
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Doubt-Driven Development

## Overview

A confident agent response is not necessarily a correct one. Long context sessions quietly convert assumptions into false "facts". Doubt-Driven Development is the operational discipline of materializing an adversarial reviewer — biased to **disprove**, not approve — before any non-trivial design or code stands.

## When to Use

A decision is **non-trivial** when at least one condition is met:
- It introduces or alters branching logic or state machines.
- It touches authentication, security boundaries, or credential flows.
- It alters a database schema, public API contract, or serialized format.
- It introduces an architectural trade-off with irreversible consequences.

## Operational Protocol

1. **Isolate the Claim**: Extract the core assumption or proposed architecture into a concise claim.
2. **Fresh-Context Cross-Examination**: Evaluate the claim without accumulated session bias.
3. **Hunt for Failure Modes**:
   - Concurrency & Race Conditions: What happens under high load or network partition?
   - Input Edge Cases: Empty collections, Unicode extremes, malformed payloads.
   - Reversibility: Can this change be cleanly rolled back in production?
4. **Physical Evidence Gate**: Do not accept "this should work". Demand passing test outputs or reproduction scripts.

## Required Inputs
```json
{
  "proposed_change": "Unified diff or architecture proposal",
  "assumptions_made": ["Assumed SQLite handles concurrency here", "Assumed API key always present"]
}
```
