# Security, Edge-Case & Testing Pass

Competent backend code handles the happy path. Flagship backend code assumes hostile inputs, flaky networks, concurrent requests, and partial failures.

## 1. Security Pass (Fail Closed)

- **Injection Prevention**:
  - *SQL*: Parameterized queries or prepared statements only. Never f-string or concatenate user input into SQL.
  - *Shell*: Never pass `shell=True` with user-controlled strings; pass argument arrays (`subprocess.run(["cmd", arg], shell=False)`).
  - *Path Traversal*: Resolve paths with `Path.resolve()` and verify `resolved.is_relative_to(base_dir)` before reading or writing user-supplied filenames.
- **AuthN vs. AuthZ (IDOR Prevention)**:
  - Authentication ("who are you?") is not Authorization ("do you own this record?").
  - Every `GET /items/:id`, `PATCH`, `DELETE`, or action endpoint must scope queries by `tenant_id` / `owner_id` from the verified session—never trust a `user_id` in the request body.
- **Secrets & Logs**:
  - Never hardcode API keys, JWT secrets, or DB passwords.
  - Never log `Authorization` headers, cookies, passwords, or full PII payloads.
- **Resource & DoS Bounds**:
  - Enforce explicit `timeout` on every outbound HTTP/DB/RPC call.
  - Enforce `max_bytes` on request bodies and file uploads.
  - Enforce `limit` caps (e.g., `1 <= limit <= 100`) on all paginated endpoints.

## 2. Edge-Case & Boundary Checklist

Test or explicitly handle every one of these:
- `null` / `None`, empty string `""`, whitespace-only `"   "`, and empty list `[]`.
- Negative numbers, `0`, `NaN`, `Infinity`, and integer overflow.
- Unicode, emojis, RTL text, and 10KB+ strings in name/title fields.
- Duplicate submissions (same idempotency key or rapid double-click).
- Clock skew, timezone boundaries (always store/compare UTC), and expired tokens.

## 3. Testing Discipline

- **Test Invariants, Not Implementation**: Assert on observable outputs, DB state, and HTTP status codes—not private helper calls.
- **Provoke the Failure Mode**: Every non-trivial endpoint or pipeline must have at least one test that actively provokes its primary failure mode (e.g., concurrent double-spend, malformed payload, downstream timeout, unauthorized tenant access).
- **Deterministic Isolation**: Each test must own its state (fresh temp DB / rolled-back transaction) so tests pass in any order.
