# Concurrency & Resilience

## 1. Race Conditions & Idempotency

- **Double-Submit / Retry**: Use `INSERT ... ON CONFLICT DO NOTHING` or unique idempotency keys rather than `SELECT` then `INSERT` (TOCTOU).
- **Optimistic Locking**: Use `version` or `updated_at` in `WHERE` clauses for concurrent updates; return `409 Conflict` on mismatch.

## 2. Contrastive Anchors (Naive vs. Flagship Backend)

- **Naive**: Checks `if balance >= amount:` in Python, sleeps or calls payment API inside the DB transaction, catches `Exception: pass`, and only tests the 200 OK path.
- **Flagship**: Uses atomic `UPDATE accounts SET balance = balance - :amt WHERE id = :id AND balance >= :amt`, keeps external calls outside the transaction with an outbox/idempotency key, and writes a test that provokes concurrent double-spend.
