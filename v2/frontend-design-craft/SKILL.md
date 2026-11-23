---
name: frontend-design-craft
description: Visual craft and taste for user-facing interfaces including art direction, typography, color systems, layout rhythm, anti-slop kill-list, motion physics, and rendered screenshot critique. Use when designing or polishing UI/visuals. Do NOT trigger for state architecture, API/DB design, or non-visual refactors.
---

# Frontend Design Craft

Eliminate generic AI-slop aesthetics. Every surface needs deliberate art direction, typographic hierarchy, disciplined color, and purposeful motion.

## 1. Mode Detection

- **Chat Mode**: Load `references/chat-mode.md`. Deliver crisp, self-contained HTML/CSS/JS or design-token specs; note that visual rendering is **Level E (Not verified)**.
- **Task Mode**: Load `references/task-mode.md`. Render in the sandbox, run `scripts/check_contrast.py` on palette tokens, and inspect actual screenshots at 375px / 768px / 1440px.

## 2. Core Design Modules

- **Anti-Slop & Visual Taste**: Load `references/taste-and-kill-list.md` to ban generic gradients, card-soup, and timid hierarchy.
- **Motion Physics**: Respect `prefers-reduced-motion`; animate only `transform` and `opacity` for 60fps transitions.
