# Invariants, Data Modeling & API Contracts

This playbook governs pre-code engineering design. Its purpose is to catch the decisions that are **expensive to reverse**—data models, public APIs, state transitions, and concurrency boundaries—before implementation begins.

---

## 1. System Invariants & Enforcement Hierarchy

An invariant is a statement that must remain true under **all** inputs, retries, partial failures, and concurrent executions.

For every invariant, enforce it at the **strongest** available layer:
1. **Unrepresentable in types or schema**: Use enums, non-null columns, and distinct types so invalid states cannot be constructed.
2. **Enforced by the datastore**: Use `UNIQUE`, `FOREIGN KEY`, `CHECK` constraints, and atomic `UPDATE ... WHERE` clauses.
3. **Enforced at one choke point**: A single service/middleware boundary that every caller must pass through.
4. **Enforced by convention in callers**: Weakest—will be violated by the next engineer or endpoint.

### Non-Negotiable Invariants
- **Idempotency**: Any mutating operation that can be retried (`POST /orders`, `POST /charges`, webhook handlers) must accept an `Idempotency-Key` backed by a datastore `UNIQUE` constraint—never a `SELECT`-then-`INSERT` check, which races under concurrent retries.
- **Money & Precision**: Represent currency in integer minor units (e.g., `amount_cents: int`) or exact `Decimal`, paired with an explicit ISO-4217 `currency` code. Never use binary `float`.
- **Time**: Persist instants in UTC (`TIMESTAMPTZ` / ISO-8601 `Z`). Store an IANA timezone (`Asia/Kolkata`) separately only when future local civil-time schedules matter.
- **Tenant Isolation**: Every multi-tenant table carries `tenant_id` (or `owner_id`), and every query scopes by it from the verified session—never from a client-supplied body field.

---

## 2. State-Machine Design

Never model lifecycle state with loose booleans (`is_paid`, `is_cancelled`, `is_refunded`)—they permit impossible combinations (`is_paid=true` AND `is_cancelled=true`).

1. **Explicit Enum**: Define a single `status` column (`pending | authorized | captured | failed | refunded`).
2. **Transition Table**: Define legal `(from_state, event) -> to_state` transitions explicitly. Reject illegal transitions with `409 Conflict`.
3. **Terminal States**: `refunded`, `cancelled`, and `completed` must never transition back to `pending`.

---

## 3. API Contract Standards

Lock these before writing handler code:
- **Consistent Error Envelope**:
  ```json
  {
    "error": {
      "code": "INSUFFICIENT_FUNDS",
      "message": "Account balance is below the requested transfer amount.",
      "retryable": false,
      "request_id": "req_01J9..."
    }
  }
  ```
- **Status Codes**: `400` malformed syntax, `401` unauthenticated, `403` unauthorized, `404` not found, `409` state/uniqueness conflict, `422` semantic validation failure, `429` rate limited (with `Retry-After`), `500` unexpected (never leak stack traces).
- **Pagination**: Cursor-based pagination (`cursor`, `limit` capped at `<=100`) for live/mutable feeds; offset pagination only for static admin tables.

---

## 4. Contrastive Anchors (Naive vs. Flagship Planning)

1. **Payment / Order Creation**:
   - *Naive*: `POST /orders` checks `if not db.exists(order_id): db.insert(...)`, stores `total: float`, and calls Stripe inside the DB transaction.
   - *Flagship*: `POST /orders` requires `Idempotency-Key` with a `UNIQUE` DB constraint, stores `total_cents: int` + `currency`, commits the `pending` order first, and dispatches the Stripe call outside the transaction via an outbox/worker.
2. **Schema Evolution**:
   - *Naive*: Renames `user_name` to `full_name` in a single `ALTER TABLE` migration, breaking running app instances mid-deploy.
   - *Flagship*: Uses **Expand -> Migrate -> Contract**: adds `full_name` (nullable), dual-writes, backfills in bounded batches, switches reads, then drops `user_name` in a later deploy.
