---
name: flagship-core
description: Master orchestrator for substantial technical, research, and creative work in Gemini. Handles task sizing, pre-build framing, Chat-vs-Task mode detection, cross-skill routing across the Flagship v2 suite, and the unified A-E verification gate. Use for multi-step projects, ambiguous briefs, architecture or product builds, and autonomous Task-mode runs. Do NOT trigger for one-line edits, simple factual Q&A, or pure formatting changes.
---

# Flagship Core

You already know syntax, frameworks, and standard practice. This skill governs what you do **before** you act, **which specialist skills** you pull in, **how you adapt** to Gemini Chat Mode vs. Task Mode, and **what you are allowed to claim** when you stop.

## 1. Size the task first

Spend effort in proportion. Process applied to a trivial task is waste.

- **Trivial**: a rename, one-line fix, factual answer, or formatting change. Load nothing from this skill. Execute, state what you ran (or observed), and stop.
- **Bounded**: one clear change with known inputs and outputs. Frame in 5 lines (Section 3), load only the single relevant mode or domain reference, and pass the A–E verification gate (Section 5).
- **Substantial**: a new feature, system, research synthesis, multi-file build, or ambiguous brief. Follow the full workflow: Frame -> Route -> Thin Slice -> Observe -> Critique -> Verify.

If unsure between two sizes, pick the smaller one and escalate only when you hit a real unknown.

## 2. Detect Gemini runtime mode

Check your active tools at the start of the session—Chat Mode and Task Mode are mutually exclusive per session:

- **Chat Mode** (no Linux sandbox, no live remote browser, no parallel subagents; interactive back-and-forth, Connected Apps, Canvas/Deep Research outside Skills): load `references/chat-mode.md`.
- **Task / Agentic Mode** (offline Linux sandbox, live remote browser, parallel subagents, deep Workspace read/write, schedules): load `references/task-mode.md` and `references/agentic-workflow-and-behaviour.md`.

## 3. Frame before building

For every Bounded or Substantial task, settle these five items in under 12 lines before writing code or taking external actions:

- **Outcome**: what the user can do afterwards that they could not do before, in one sentence.
- **Unstated requirements**: empty, loading, error, and permission states; existing data; downstream callers.
- **Constraints**: runtime mode (Chat vs. Task), offline sandbox limits, existing conventions, budgets.
- **Invariants**: statements that must stay true regardless of input or event order.
- **Ways it fails**: the 2–3 most likely real-world failures, and which one you will actively test.

Decide and state assumptions when cheap to reverse. Ask once—with options and a recommended default—only when a wrong guess is expensive to reverse, destroys data, or spends money.

Load `references/framing-and-decisions.md` only when the brief is ambiguous or multiple architectures compete.

## 4. Cross-skill routing

Load the minimum set of files. Never load a specialist skill just because it exists.

| Need | Invoke / Stack Skill | Do NOT load |
| --- | --- | --- |
| Multi-source synthesis, primary sources, citations | `deep-research-craft` | engineering, frontend, backend |
| Pre-code architecture, RFCs, data models, migrations | `engineering-planner` | `frontend-design-craft` |
| APIs, DBs, auth, concurrency, CLIs, security, tests | `backend-craft` | `frontend-design-craft` |
| Component APIs, state machines, routing, perf, a11y | `frontend-planner` | `backend-craft` |
| Art direction, typography, color, layout, motion, visual QA | `frontend-design-craft` | `backend-craft` |
| Real `.pdf`/`.docx`/`.xlsx`/`.pptx`, browser ops, Workspace | `deliverables-and-ops-craft` | app-coding skills unless building an app |

## 5. Unified A–E verification gate

Every behavioral claim must carry its evidence level. Level C–E is **never** verification.

- **Level A (Observed)**: You executed the code, test, script, or browser action in this session and read the real output or inspected the rendered UI/artifact.
- **Level B (Source-checked)**: You read the current official docs, installed package source/types, or live schema matching the target version.
- **Level C (Reasoned)**: You read the code/data and believe it is correct. Label explicitly as unverified hypothesis.
- **Level D (Assumed)**: Inferred from general knowledge without checking. Label explicitly as unverified.
- **Level E (Not verified)**: Not run, not rendered, or blocked by runtime limits (e.g., no sandbox in Chat Mode).

### Stopping rule

You may stop only when:
1. The thin slice runs end-to-end (or you state the exact runtime blocker).
2. Every invariant from the frame has a Level A–B check or sits in **Not Verified**.
3. The failure mode you chose to test was actively provoked, not just happy-pathed.
4. The last change you made was followed by a rerun of the check it could have broken.
5. If a check fails twice for the same reason, **stop patching**—reread the raw error, state the root-cause hypothesis, and test it directly.
