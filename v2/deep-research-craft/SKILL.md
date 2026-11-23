---
name: deep-research-craft
description: Multi-source research synthesis, primary-source hierarchy, contradiction resolution, and strict citation discipline. Use for market/technical research, competitive analysis, literature synthesis, and fact-checking. Do NOT trigger for building software, UI styling, or simple single-fact lookups.
---

# Deep Research Craft

Synthesize truth from messy sources without smoothing over gaps or contradictions.

## 1. Mode Detection

- **Chat Mode**: Load `references/chat-mode.md`. Use Web Search + explicit citation hygiene; note that Deep Research tool runs outside Skills.
- **Task Mode**: Load `references/task-mode.md`. Use parallel subagents for >=3 independent entities/sources and Python scripts for tabular synthesis.

## 2. Core Workflow

1. **Define the Research Question & Output Schema**: Lock exact comparison dimensions before searching.
2. **Source Hierarchy**: Load `references/source-hierarchy.md`. Prefer primary docs, official specs, and raw data over secondary blogs.
3. **Contradiction Hunt**: Actively look for conflicting numbers, dates, or specs across sources; resolve against the highest-authority primary source.
4. **Honest Gaps**: Missing data is reported as `NOT FOUND`—never interpolated.
