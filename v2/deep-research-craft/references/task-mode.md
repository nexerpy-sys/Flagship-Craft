# Task Mode Adapter (Deep Research)

In **Gemini Task Mode**, you have **parallel background subagents**, `fetch_page`, live remote browser, and an **offline Linux sandbox** for deterministic synthesis.

## Execution Rules
1. **Parallel Subagent Fan-Out**: For >=3 entities, vendors, or independent topics, spawn parallel subagents with a strict JSON/Markdown schema and the rule: *"Return `NOT FOUND` for any missing field—never guess."*
2. **Live Browser Escalation**: Use `fetch_page` first; escalate to the live remote browser only for JS-rendered pricing calculators or dynamic tables.
3. **Deterministic Synthesis & Citation Lint**:
   - Persist extracted tables to disk (`data.csv` / `report.md`) in the sandbox.
   - Run `python3 scripts/check_citations.py <report.md>` and fix every flagged ungrounded numeric/pricing claim before delivery.
