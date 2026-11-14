---
name: Constraint-Driven Development
description: Discovers, declares, and strictly enforces hard technical constraints, invariants, resource budgets, and licensing boundaries.
category: development
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Constraint-Driven Development

## Overview

Software quality degrades when agents attempt unconstrained generation. Constraint-Driven Development explicitly surfaces, validates, and locks down the technical, operational, and licensing boundaries before code generation begins.

## Four Tiers of Constraints

1. **System & Runtime Invariants**: Supported Python/Node versions, memory limits, thread-safety requirements.
2. **Architecture & Dependency Boundaries**: Zero new third-party packages without explicit audit; local mock transports over network calls.
3. **Security & Data Invariants**: Zero hardcoded secrets, no unparameterized queries, zero unverified serialization.
4. **License & Attribution Integrity**: Permissive licensing compatibility (MIT/Apache 2.0), no code copy-pasting from restrictive licenses.

## Enforcement Mechanism

- Each task must define a `constraints` dictionary.
- Automated static checks and tests fail if any declared invariant is violated.
