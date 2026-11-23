# Framing, Architecture Decisions & Premortems

Load this file when the brief is ambiguous, when several plausible architectures compete, or when the 12-line frame in `SKILL.md` is not enough.

---

## 1. The Decision Matrix (Reversibility x Blast Radius)

Every engineering or product decision falls into one of two categories:
- **Two-Way Door (Cheap to reverse + Low blast radius)**: Decide immediately, state the assumption in one line, and keep moving. Examples: internal helper naming, CSS spacing tweaks, local test structure, non-public module boundaries.
- **One-Way Door (Expensive to reverse OR High blast radius)**: Pause and present 2–3 concrete options with trade-offs and **one recommended default**. Examples: database schema migrations on live data, public API contracts, auth/permission models, billing/payment flows, irreversible deletions, external communications.

---

## 2. The Premortem Protocol

Before committing to an architecture or multi-step autonomous run, run a 60-second premortem:
*"It is 2 weeks later and this failed in production. What broke?"*

1. **Name the top 2–3 concrete failure modes**:
   - *Silent partial failure* (e.g., step 2 of 3 fails and leaves orphaned records).
   - *Concurrency / race* (e.g., double-submit or two workers processing the same job).
   - *Boundary / scale* (e.g., unbounded query, missing timeout, 10MB upload).
   - *Missing state* (e.g., empty state, expired token, permission denied).
2. **Pair each failure mode with**:
   - One **invariant** that prevents it.
   - One **active test** that provokes it (not just a happy-path check).

---

## 3. Scope Guard (Thin Slice vs. Speculative Abstraction)

- **Thin Slice First**: Build one complete vertical path (UI -> API -> DB -> Test) before adding breadth. Integration bugs hide until layers meet.
- **Zero Speculative Abstractions**: Do not build plugin systems, multi-provider factories, or generic event buses for a single concrete requirement. Three similar lines of code are better than a premature abstraction.

---

## 4. Contrastive Anchors (Naive vs. Flagship Framing)

- **Naive**: Reads *"Build an invoice tracker"*, immediately creates 14 files with a custom ORM wrapper, ignores currency precision and duplicate uploads, and asks 6 vague questions.
- **Flagship**: Locks a 5-line frame (Outcome, Unstated: empty/error states + duplicate-invoice idempotency, Invariant: `total_cents: int`, Failure mode: duplicate CSV import), decides cheap defaults, and builds the thin slice end-to-end.
