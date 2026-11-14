---
name: Anti-Rationalization Rules
description: Prevents AI agents from inventing justifications for test failures, unexpected behaviors, or unmet specifications. Enforces physical evidence verification.
category: development
version: 1.0.0
author: Taqi Molavi
license: MIT
---

# Anti-Rationalization Rules & Verification Protocol

## Overview

AI models often rationalize failures: claiming a test failed "due to a pre-existing issue", "because the environment lacks X", or "this warning is harmless". Anti-Rationalization Rules strictly prohibit speculative excuses and enforce empirical, physical verification.

## Forbidden Rationalizations

- ❌ *"The test failed because the environment is different, so the code is actually correct."*
- ❌ *"This error is just a deprecation warning and won't affect production."*
- ❌ *"The mock failed, but in a real system it would definitely pass."*
- ❌ *"I didn't run the tests because the change was minor and trivial."*

## The Golden Rule of Verification

> **"It is strictly forbidden to guess. Either physical evidence confirms the change, or the task is NOT complete."**

## Verification Checklist

1. **Reproduction Script**: For any bug fix, write a test that fails before the fix.
2. **Deterministic Green**: Run the test suite and verify 100% pass rate.
3. **Diff Minimization**: Verify zero accidental edits to unrelated files.
4. **Physical Output**: Capture exit codes and terminal logs as permanent evidence.
