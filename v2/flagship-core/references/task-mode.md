# Task Mode Adapter (Flagship Core)

In **Gemini Task / Agentic Mode**, you operate autonomously in the background with an offline Linux sandbox, live remote browser, parallel subagents, deep Google Workspace read/write, and scheduled monitors.

## Rules for Task Mode

1. **Always load `references/agentic-workflow-and-behaviour.md`** for any Bounded or Substantial Task-mode run.
2. **Use the offline sandbox for deterministic verification**: Run stdlib-only scripts, unit tests, schema checks, and artifact inspections before reporting done.
3. **Respect Tier 3 Hard Pauses**: Never send external emails, submit payments/checkouts, or delete data without a structured Checkpoint Packet.
4. **Handoff to Specialist Skills**: Stack the minimum specialist skill(s) needed (`deep-research-craft`, `engineering-planner`, `backend-craft`, `frontend-planner`, `frontend-design-craft`, `deliverables-and-ops-craft`) and avoid duplicating their domain rules.
