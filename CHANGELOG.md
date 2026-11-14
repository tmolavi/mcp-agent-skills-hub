# Changelog

All notable changes to the **Molavi Agent Skills** project will be documented in this file.

## [1.1.0] - 2026-11-14

### Added
- **Skill Evaluation Framework (Skill Evals):** Automated verification suite with Tier 1 Behavioral Schema Checker (`evals/eval_runner.py`) and Tier 2 Description Collision Auditor (`evals/check_collisions.py`).
- **Rejected Changes Ledger:** Added `evals/skill-impact.md` recording rejected proposals, rationales, and evaluation evidence to prevent repeated dead ends.
- **High-Rigor Engineering Skills:** Added `spec-driven-development`, `doubt-driven-development`, `constraint-driven-development`, and `anti-rationalization-rules` expanding catalog to 281 production skills.
- **Collision Resolution:** Disambiguated and fine-tuned AlloyDB and Cloud SQL PostgreSQL skill descriptions for routing accuracy.

## [Unreleased]

### Added
- Added `SECURITY.md` and `CONTRIBUTING.md` trust-signal files.
- Added explicit read-only database credential instructions in `docs/agent-installation.md`.
- Integrated token consumption and context management guidelines into `docs/token-optimization.md` as directional estimates.
- Integrated [molavi.pro](https://molavi.pro) links across README and documentation.

<!-- Future tagged releases will be listed here once published on GitHub. -->
