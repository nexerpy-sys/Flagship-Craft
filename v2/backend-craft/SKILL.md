---
name: backend-craft
description: Implementing and debugging APIs, databases, auth, concurrency, data pipelines, CLIs, security passes, and automated tests. Use when writing or fixing server-side or CLI code. Do NOT trigger for UI layout, visual taste, or high-level product research.
---

# Backend Craft

Build reliable, secure, testable backend systems with explicit error handling and real verification.

## 1. Mode Detection

- **Chat Mode**: Load `references/chat-mode.md`. Provide self-contained, production-grade code + test cases, explicitly marked **Level C / Level E** since no sandbox ran them.
- **Task Mode**: Load `references/task-mode.md`. Run unit/integration tests and `python3 scripts/security_scan.py <path>` in the offline Linux sandbox.

## 2. Core Standards

- **Input & Boundary Validation**: Validate all external inputs at the boundary; fail closed with structured errors.
- **Data & Concurrency**: Load `references/security-and-testing.md` for auth, injection, race-condition, and test-isolation rules.
- **No Silent Swallowing**: Never catch and ignore errors; log context or propagate typed failures.
