# API, Data & Invariant Engineering

This playbook covers the engineering passes that separate code that compiles from code that holds up under bad input, retries, concurrency, and partial failure.

---

## Pass 1 — API Currency

Your recollection of an API can be older than the version installed in the project. Code written from stale memory compiles in your head and fails at runtime, or works while using a deprecated or insecure path.

Before using any library, SDK, framework feature, or CLI you have not already seen working in this repository:
1. **Find the installed version** from the lockfile, manifest (`package.json`, `pyproject.toml`, `requirements.txt`), or the package itself. Never assume latest.
2. **Check one source of truth for that exact version**, in order of preference:
   - The installed package's own source or type definitions.
   - Official documentation for that version.
   - The official changelog or migration guide.
3. **If you cannot check any of these**, write the code and log *"API usage for X not checked against version Y"* under **Not Verified (Level E)**.

Signals that must trigger a check even for familiar libraries:
- A major version you have not worked with.
- Authentication, payments, cryptography, file upload, or cloud provider SDKs.
- An import path, option name, or config key you are reconstructing rather than copying from working code in the repo.

Prefer the pattern already used in the repository over the one you remember, unless the repository's pattern is the bug.

---

## Pass 2 — Invariants & Where They Are Enforced

Spend care where mistakes are expensive to undo: the data model, public interfaces, and anything persisted or sent to another party.

For each invariant in your frame, enforce it at the **strongest** available layer:
1. **Unrepresentable in types or schema**: Enums, non-null columns, branded IDs, discriminated unions.
2. **Enforced by the datastore**: `UNIQUE`, `FOREIGN KEY`, `CHECK` constraints, atomic `UPDATE ... WHERE`, database transactions.
3. **Enforced at one choke point in code**: A single service/middleware boundary that every path must pass through.
4. **Enforced by convention in each caller**: Weakest—will be violated by the next engineer or endpoint. If you must use it, state it explicitly in the report.

### Universal System Invariants
- **Idempotency**: Any operation that can be retried (`POST /orders`, `POST /charges`, webhook handlers) must be safe to retry. Use an `Idempotency-Key` with a datastore `UNIQUE` constraint—never a `SELECT`-then-`INSERT` check, which races under concurrent retries.
- **Atomic State Transitions**: Never model lifecycle state with loose booleans (`is_paid`, `is_cancelled`). Use a single `status` enum and enforce legal transitions atomically (`UPDATE orders SET status = 'captured' WHERE id = :id AND status = 'authorized'`).
- **Money & Counts**: Represent money in integer minor units (`amount_cents: int`) or exact `Decimal`, paired with an ISO-4217 `currency` code. Never use binary `float`. Represent counts with integer types.
- **Time**: Persist instants in UTC (`TIMESTAMPTZ` / ISO-8601 `Z`). Retain an IANA timezone (`Asia/Kolkata`) separately only when future local civil-time schedules matter; convert only for display.
- **External Calls**: Every outbound HTTP/DB/RPC call has an explicit connect + read timeout. Every retry has a max count, exponential backoff + jitter, and a defined caller-visible failure state when retries exhaust.

---

## Pass 3 — Input & Timeline Walk

Do not list edge cases from imagination. Walk the input and the timeline systematically.

### Input Walk (Every Boundary Value)
- `null` / `None`, missing key, empty string `""`, whitespace-only `"   "`, empty list `[]`.
- `0`, `-1`, `NaN`, `Infinity`, integer overflow, and precision loss.
- Wrong type (string where integer expected, array where object expected).
- Duplicate keys, 10KB+ strings in name/title fields, Unicode, emojis, and RTL text.
- Boundary dates: leap years, DST transitions, epoch `0`, far-future dates.

### Timeline Walk (Every Failure Point)
- **Client disconnects mid-request**: Does partial state leak?
- **Step 2 of 3 fails**: Are earlier steps rolled back or explicitly recoverable?
- **Two identical requests arrive 5ms apart**: Does the datastore prevent double-spend or duplicate creation?
- **Downstream times out after 10s**: Is the DB connection/lock released, or does it stall the pool?

---

## Pass 4 — Transactions, Outbox & Pagination

- **Keep External Calls Outside DB Transactions**: Never hold a database transaction open while calling Stripe, an email API, or an LLM. Commit the local state (`pending`) first, then dispatch the external call (or use an outbox table + worker).
- **No N+1 Queries**: Batch-load relations (`WHERE id IN (...)`) or use explicit joins.
- **Pagination**: Use cursor-based pagination (`cursor`, `limit` capped at `<=100`) for live/mutable feeds; reserve offset pagination for small, static admin tables.

---

## Pass 5 — Contrastive Anchors (Naive vs. Flagship Backend)

1. **Double-Spend / Balance Deduction**:
   - *Naive*: Reads `balance = db.get(id).balance`, checks `if balance >= amount:` in Python, then updates `balance - amount`. Two concurrent requests both pass the check and overdraw the account.
   - *Flagship*: Executes `UPDATE accounts SET balance_cents = balance_cents - :amt WHERE id = :id AND balance_cents >= :amt RETURNING balance_cents` and returns `409 Conflict` if 0 rows updated.
2. **Webhook / Retry Handling**:
   - *Naive*: Processes the webhook payload directly and inserts a new ledger row on every delivery.
   - *Flagship*: Inserts `(provider, event_id)` into `processed_events` with a `UNIQUE` constraint inside the same transaction as the ledger update; duplicate deliveries hit the unique constraint and return `200 OK` idempotently.
