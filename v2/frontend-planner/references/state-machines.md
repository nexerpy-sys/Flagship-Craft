# UI State Machines, Data Flow & Async Resilience

Never represent async UI with loose booleans (`{ isLoading, isError, data }`)—they permit impossible states (`isLoading: true` AND `isError: true`). Model explicit discriminated unions.

---

## 1. The 5-State Async Union

Every async surface (page, table, modal, form) must explicitly handle all five states:
1. **`idle`**: Initial state before the first trigger.
2. **`loading`**: Request in flight. Show a skeleton matching the final layout (to prevent CLS) or a spinner; disable duplicate form submission.
3. **`empty`**: Request succeeded with `0` items. Show a clear explanation and a primary CTA (e.g., *"No invoices yet — Create your first invoice"*).
4. **`error`**: Request failed. Show an actionable error message, a **Retry** button, and **preserve all user-entered form input**.
5. **`success`**: Data present and rendered.

---

## 2. Stale Responses & Race Conditions

- **Abort / Sequence Guard**: When a user types rapidly into a search/filter input, cancel in-flight requests (`AbortController`) or tag each request with a monotonic `requestId` and ignore out-of-order responses.
- **Optimistic Updates**: Use optimistic UI *only* for high-frequency, low-risk actions (likes, toggles, reordering). Always snapshot previous state and roll back cleanly with a visible error toast if the server rejects.

---

## 3. Contrastive Anchors (Naive vs. Flagship Frontend State)

1. **Search-as-You-Type**:
   - *Naive*: Fires `fetch()` on every keystroke without `AbortController`; slow response #1 overwrites fast response #2.
   - *Flagship*: Debounces input (200ms), aborts prior in-flight requests via `AbortController`, and models `loading | empty | error | success` explicitly.
2. **Form Submission**:
   - *Naive*: Allows double-click submission, clears all form fields on 500 error, and shows *"Something went wrong."*
   - *Flagship*: Disables submit while `loading`, preserves all field values on `error`, and displays the server's actionable error message.
