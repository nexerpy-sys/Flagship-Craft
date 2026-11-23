---
name: deliverables-and-ops-craft
description: Building real downloadable deliverables (.pdf, .docx, .xlsx, .pptx, HTML reports), live remote browser workflows with confirmation gates, and Google Workspace automation. Use for document/deck/spreadsheet generation or operational workflows. Do NOT trigger for app coding or pure research.
---

# Deliverables and Ops Craft

Produce executive-grade files and execute live Workspace/browser operations safely without silent failures.

## 1. Mode Detection

- **Chat Mode**: Load `references/chat-mode.md`. Draft content, outlines, or formulas in text; note that binary `.pdf`/`.xlsx`/`.pptx` builds and live browser actions require Task Mode.
- **Task Mode**: Load `references/task-mode.md`. Build real files in the offline sandbox, inspect rendered pages/sheets, and enforce Tier 3 confirmation gates on external actions.

## 2. Core Standards

- **Mandatory Artifact Inspection**: Never deliver a `.pdf`, `.docx`, `.xlsx`, or `.pptx` without verifying non-empty data, formula results, and clean layout/page breaks.
- **Read-Before-Write**: Always inspect existing Workspace/browser state before mutating.
