# Architecture Patterns & Reversibility

## 1. Reversibility First

- Prefer **two-way doors** (modular interfaces, feature flags, additive schema changes) over **one-way doors** (destructive column drops, tight coupling, vendor lock-in).
- Every migration plan must include: **Forward step**, **Verification check**, and **Rollback step**.

## 2. Failure-Mode Checklist

- **Partial failure**: What happens if step 2 of 3 fails? (Idempotency keys, outbox pattern, compensating actions).
- **Concurrency**: What happens on double-submit or parallel workers? (Optimistic locking, unique constraints).
- **Scale & Bounds**: Unbounded lists, N+1 queries, missing timeouts, missing rate limits.
