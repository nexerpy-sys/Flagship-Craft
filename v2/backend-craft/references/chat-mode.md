# Chat Mode Adapter (Backend Craft)

In **Gemini Chat Mode**, you have **no offline Linux sandbox**—you cannot execute code, run unit tests, or run `scripts/security_scan.py`.

## Execution Rules
1. **Self-Contained Output**: Deliver complete, idiomatic code with explicit input validation, timeouts, and a ready-to-run `unittest` / `pytest` block.
2. **Manual Security & Edge-Case Pass**: Because `security_scan.py` cannot run here, manually verify zero hardcoded secrets, parameterized SQL, `shell=False`, and explicit `limit` caps before responding.
3. **Honest Verification Label**: Never claim tests passed. Close with: *"Verified by inspection (Level C); runtime execution and tests not verified (Level E—no Linux sandbox in Chat Mode)."*
4. **Local Command**: Give the user the exact 1-line command to run locally (e.g., `pytest -q`).
