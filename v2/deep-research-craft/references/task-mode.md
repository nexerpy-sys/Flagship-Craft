# Task Mode Adapter (Deep Research)

- Fan out **parallel subagents** when comparing >=3 entities, vendors, or independent topics.
- Give every subagent a strict JSON/Markdown schema and instruct it to return `NOT FOUND` rather than guessing.
- Use `fetch_page` / live browser only when Web Search snippets lack the primary table, pricing, or spec.
- Persist extracted comparison tables to disk in the sandbox and run deterministic checks (totals, dates, unit normalization) with Python before writing the final synthesis.
