---
name: Spec-Driven Development
description: Creates structured specifications before coding. Decomposes ambiguous requirements into a Capability Map, non-goals, and measurable acceptance criteria.
category: development
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Spec-Driven Development

## Overview

Spec-Driven Development enforces writing a structured specification before generating any code. The specification serves as the shared single source of truth between the human engineer and the AI agent. Code without a spec is guessing.

## When to Use

- Starting a new feature, project, or subsystem.
- Requirements are ambiguous, incomplete, or span multiple modules.
- Introducing a new API route, schema modification, or architecture pattern.
- Any change anticipated to touch more than 2 files or take over 20 minutes.

**When NOT to use:** Single-line typo corrections, trivial dependency version bumps, or direct scratch experimentation.

## Core Rules

1. **No Code Before Spec**: Never generate implementation code or modify core files until the spec is approved.
2. **Capability Decomposition**: Break the requirement into a Capability Map of independently testable units.
3. **Explicit Non-Goals**: Enforce boundaries by documenting what this change will *not* do.
4. **Acceptance Criteria & Test Matrix**: Define the exact observable assertions that verify completion.

## Required Inputs
```json
{
  "requirement": "Description of the feature or architectural need",
  "context": "Current system architecture and existing components"
}
```

## Spec Template
```markdown
# [Feature Name] Technical Specification

## 1. Problem & Context
## 2. Goals & Measurable Outcomes
## 3. Explicit Non-Goals & Boundaries
## 4. Capability Map & Components
## 5. Interface & Schema Contracts
## 6. Verification & Acceptance Criteria
```
