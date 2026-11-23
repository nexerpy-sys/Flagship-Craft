# Task Mode Adapter (Frontend Planner)

In **Gemini Task Mode**, you have an **offline Linux sandbox** to test state machines and lint generated HTML deterministically.

## Execution Rules
1. **State-Machine Unit Tests**: Test all 5 async states (`idle | loading | empty | error | success`) and stale-response cancellation with deterministic unit tests in the sandbox.
2. **Mandatory A11y Lint**: Run `python3 scripts/check_a11y.py <file.html>` on generated HTML and fix any missing `lang`, `<main>`, `alt`, or `<input>` label findings.
3. **Visual Handoff**: When paired with `frontend-design-craft`, verify keyboard focus order, empty/error states, and responsive breakpoints in rendered output.
