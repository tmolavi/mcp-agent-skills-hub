# Molavi Agent Skills Evaluation Framework (Skill Evals)

This directory provides the automated, reproducible evaluation suite for all skills in `mcp-agent-skills-hub`.

Inspired by industry-standard skill evaluation practices (Anthropic skill-creator v2 & Addy Osmani Agent Skills), this suite provides two deterministic testing tiers:

## Evaluation Tiers

### Tier 1: Behavioral & Schema Verification
- Ensures every skill in `skills/` contains a valid `SKILL.md` with standard YAML frontmatter (`name`, `description`).
- Validates the presence of operational sections:
  - Overview / Problem definition
  - When to Use / When NOT to Use
  - Trigger conditions or required inputs
  - Verification checklist / Acceptance criteria

### Tier 2: Description Distinctness & Collision Detection
- Scans all skills in the catalog to detect description collisions, overlapping trigger phrases, or overly generic descriptions (e.g. "helps with coding").
- Measures description token efficiency to avoid bloating agent context windows.

### Rejected Decision Ledger (`skill-impact.md`)
- Append-only registry of proposed skill modifications, descriptions, or tools rejected due to evaluation regressions or quality failures.

## Running the Evals

Run the collision and schema suite locally:
```bash
python3 evals/check_collisions.py
python3 evals/eval_runner.py
```
