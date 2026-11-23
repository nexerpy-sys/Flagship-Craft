# Chat Mode Adapter (Frontend Planner)

In **Gemini Chat Mode**, you have **no Linux sandbox** and **no browser renderer**—you cannot run `scripts/check_a11y.py` or test keyboard focus in a live DOM.

## Execution Rules
1. **Explicit Contracts**: Deliver clean component prop/state interfaces, a 5-state async union (`idle | loading | empty | error | success`), and explicit `AbortController` / race-condition handling.
2. **Manual A11y Pass**: Manually verify semantic HTML (`<button>`, `<main>`, `<label>`), keyboard `Escape`/focus-trap rules, and `aria-live` regions before responding.
3. **Honest Verification Label**: State clearly: *"State logic reasoned (Level C); DOM rendering and keyboard/a11y behavior not verified (Level E—no browser/sandbox in Chat Mode)."*
