---
name: frontend-planner
description: Frontend structure and behavior including component APIs, state machines, routing, data fetching, rendering performance, and WCAG accessibility architecture. Use when architecting UI logic or complex client state. Do NOT trigger for visual aesthetics, color/typography taste, or backend logic.
---

# Frontend Planner

Separate **how the UI works** (state, data flow, accessibility, performance) from **how it looks** (`frontend-design-craft`).

## 1. Mode Detection

- **Chat Mode**: Load `references/chat-mode.md`. Focus on clean component contracts, state diagrams, and a11y requirements.
- **Task Mode**: Load `references/task-mode.md`. Verify state transitions, keyboard navigation, `python3 scripts/check_a11y.py <file.html>`, and bundle/render behavior in the sandbox.

## 2. Core Standards

- **Explicit State Machines**: Model `idle | loading | success | error | empty` explicitly—never derive loading/error from ambiguous booleans.
- **Accessibility Architecture**: Load `references/a11y-architecture.md` for keyboard, focus management, ARIA, and semantic HTML rules.
- **Performance Budgets**: Avoid unnecessary re-renders, layout thrashing, and unvirtualized large lists.
