---
name: engineering-planner
description: Pre-code system architecture, RFCs, data modeling, API contracts, migration plans, and reversibility analysis. Use before building complex systems or refactoring core architecture. Do NOT trigger for writing production code, visual styling, or pure research.
---

# Engineering Planner

Make the expensive decisions explicit before a single line of production code is written.

## 1. Mode Detection

- **Chat Mode**: Load `references/chat-mode.md`. Focus on concise RFCs, trade-off tables, and clarifying irreversible choices.
- **Task Mode**: Load `references/task-mode.md`. Inspect existing repo schemas/configs in the sandbox before proposing architecture.

## 2. Core Workflow

1. **Invariants & Boundaries**: Define what must never break (e.g., idempotency, tenant isolation, zero-downtime migration).
2. **Data & API Contracts**: Lock schemas, state transitions, and error contracts before implementation.
3. **Reversibility & Migration**: Load `references/architecture-patterns.md` for trade-off matrices and rollback plans.
4. **Thin-Slice Plan**: Sequence implementation into verifiable vertical slices.
