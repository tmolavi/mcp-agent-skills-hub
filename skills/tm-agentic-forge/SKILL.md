---
name: tm-agentic-forge
version: 0.1.0
description: Provider-independent agent engineering skill for vetting external skills/plugins (7-gate security), linting orchestrator tool-scopes, running 8-suite evaluations, and exporting runtime adapters for Antigravity, Hermes Core, and Hermes Personal Desktop.
permission_level: L0_READ_ONLY
license: MIT
targets: [antigravity, hermes-core, hermes-personal-desktop]
---

# TM-Agentic-Forge Skill

Use this skill when vetting external skills/plugins, enforcing least-privilege orchestrator tool scopes, running reproducible agent benchmarks, or exporting skills across **Antigravity**, **Hermes Core (Finland Linux)**, and **Hermes Personal Desktop (Mac Local)**.

## Core Rules
1. **Never auto-install untrusted skills or unpinned package tags / remote git MCP dependencies.** Always run `python3 -m tm_forge vet-skill <path>` first.
2. **Never conflate Mac Local (`hermes-personal-desktop`) and Finland Linux (`hermes-core`).** Verify with `python3 -m tm_forge check-env --target <target>`.
3. **Orchestrator Least Privilege:** Orchestrators (`is_orchestrator=True`) must emit `HandoffRequest` and must not hold `write`, `bash`, or `mcp_*` tools directly.
4. **Memory Isolation:** Delegate persistent memory to `tm-second-brain` via `SecondBrainBridge` namespaces (`antigravity`, `main-hermes`, `desktop-hermes`).

## Quick Commands
```bash
# Run 8-suite evaluation benchmark
python3 -m tm_forge eval

# Vet a SKILL.md before registration
python3 -m tm_forge vet-skill path/to/SKILL.md --license MIT --source local

# Verify runtime adapter host isolation
python3 -m tm_forge check-env --target antigravity
python3 -m tm_forge check-env --target hermes-core --host linux
python3 -m tm_forge check-env --target hermes-desktop --host macos
```
