# Chat Mode Adapter (Deep Research)

In **Gemini Chat Mode**, you have iterative Web Search and `fetch_page`, but **no parallel background subagents** and **no Skills execution inside Gemini's Deep Research tool**.

## Execution Rules
1. **Sequential Search Discipline**: Run a broad landscape query first, then targeted Tier 1 primary-source queries.
2. **Inline Traceability**: Every pricing, limit, date, or benchmark claim must carry an inline URL and verification month/year.
3. **No-Sandbox Fallback**: Because you cannot run `scripts/check_citations.py` in Chat Mode, manually audit every numeric/pricing line before responding and mark any unverified gap as `NOT FOUND`.
4. **Deep Research Handoff**: If the user needs a 20+ source Deep Research report, prepare the exact research brief, comparison axes, and exclusion criteria in text so they can launch it cleanly in Gemini's Deep Research tool.
