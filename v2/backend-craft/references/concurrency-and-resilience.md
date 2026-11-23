# Concurrency, Idempotency & Resilience

Distributed systems and concurrent web backends fail in ways that never appear in single-threaded local tests: race conditions, double-submits, thundering herds, and cascading timeouts.

---

## 1. Concurrency & Race-Condition Patterns

| Problem | Broken Approach (TOCTOU) | Flagship Pattern |
| --- | --- | --- |
| **Duplicate creation / Double-submit** | `SELECT` to check if exists, then `INSERT` | `INSERT ... ON CONFLICT DO NOTHING` or `UNIQUE` constraint on `idempotency_key` |
| **Balance / Inventory deduction** | Read `balance` in app, `if balance >= amt: update` | Atomic `UPDATE accounts SET balance_cents = balance_cents - :amt WHERE id = :id AND balance_cents >= :amt` |
| **Concurrent record edits** | Last-write-wins blind `UPDATE` | **Optimistic locking**: `WHERE id = :id AND version = :expected_version`; return `409 Conflict` if 0 rows |
| **Job queue / Worker claiming** | `SELECT` pending jobs, then `UPDATE status = 'running'` | `UPDATE jobs SET status = 'running' WHERE id = (SELECT id FROM jobs WHERE status = 'pending' LIMIT 1 FOR UPDATE SKIP LOCKED) RETURNING *` |

---

## 2. Timeouts, Retries & Circuit Breakers

- **Explicit Timeouts Everywhere**: Never use default infinite timeouts on HTTP clients, DB queries, or Redis calls. Set distinct `connect_timeout` (e.g., `2s`) and `read_timeout` (e.g., `10s`).
- **Bounded Retries with Jitter**:
  - Retry **only** transient errors (`429`, `502`, `503`, `504`, network timeouts)—never retry `400`, `401`, `403`, or `404`.
  - Use exponential backoff + full jitter (`delay = random(0, base * 2^attempt)`) to prevent thundering herds.
  - Cap retries (e.g., `max_attempts = 3`) and define the exact fallback/error state when exhausted.
- **Idempotency Keys**: Every retried `POST` must carry an `Idempotency-Key` so retries never charge twice or create duplicate records.

---

## 3. Verification & Provoking Failures

Never stop at single-threaded happy-path tests:
- **Concurrency Test**: Spawn 5–10 parallel threads/coroutines hitting the same balance deduction or idempotency key simultaneously; assert that **exactly 1** succeeds (or total deducted equals `1 * amount`).
- **Timeout / Partial Failure Test**: Mock a downstream `TimeoutError` after step 1; assert that DB locks are released and state remains consistent.

---

## 4. Contrastive Anchors (Naive vs. Flagship Resilience)

1. **Coupon / Promo Redemption**:
   - *Naive*: Checks `if coupon.uses < coupon.max_uses:` in Python, then increments `uses += 1`. Two simultaneous requests both pass and exceed `max_uses`.
   - *Flagship*: Executes `UPDATE coupons SET uses = uses + 1 WHERE code = :code AND uses < max_uses` and rejects with `409 Conflict` when `rowcount == 0`.
2. **Webhook Retry Storm**:
   - *Naive*: Retries failed outbound webhooks in a tight `for i in range(5):` loop with `time.sleep(1)` inside the HTTP handler.
   - *Flagship*: Enqueues webhook delivery to a background worker with exponential backoff + jitter and a dead-letter state after 5 attempts.
