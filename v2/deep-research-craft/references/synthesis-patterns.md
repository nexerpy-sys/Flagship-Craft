# Synthesis Patterns, Subagent Fan-Out & Research Rigor

## 1. Lock the Research Brief Before Searching

Never start with a broad topic dump. Lock these three items first:
- **Decision**: What exact decision will this research inform? (e.g., *"Choose a vector DB for <10M embeddings under $200/mo"*).
- **Comparison Axes**: 4–6 exact columns (e.g., `Pricing Tier`, `Hard Limits`, `Latency/SLA`, `Lock-in`, `Last Verified`).
- **Exclusion Criteria**: What is explicitly out of scope?

## 2. Parallel Subagent Fan-Out (Task Mode)

When comparing >=3 entities or auditing >=3 independent sources:
- Give every subagent a **narrow entity**, an **exact JSON/Markdown schema**, and **strict anti-smoothing rules** (*"Return `NOT FOUND` for any missing field—never guess or average"*).
- Never parallelize sequentially dependent steps (e.g., don't fan out until the target entity list is locked).
- Run a **Reconciliation Pass** on all subagent outputs: hunt for mismatched units (monthly vs. annual pricing, GB vs. GiB, p50 vs. p99 latency) and resolve conflicts against Tier 1 sources.

## 3. Claim-to-Citation Traceability

- Every non-trivial number, date, limit, or price must carry an inline URL or `[source]` tag.
- Run `python3 scripts/check_citations.py <report.md>` in Task Mode to catch ungrounded numeric/pricing claims before delivery.
- Tag fast-moving facts (pricing, API limits, model specs) with the **month/year verified**.

## 4. Contrastive Anchors (Naive vs. Flagship Research)

1. **Vendor Pricing Comparison**:
   - *Naive*: Cites a 2024 blog post for Vendor A, guesses Vendor B's enterprise tier as *"around $500/mo,"* and mixes annual vs. monthly rates in the same column.
   - *Flagship*: Pulls Tier 1 pricing pages for both, normalizes all figures to monthly billing, marks Vendor B's Enterprise tier as `NOT FOUND (custom quote required)`, and dates every row.
2. **Technical Benchmark Synthesis**:
   - *Naive*: Repeats a vendor's marketing headline (*"10x faster than X"*) as settled fact.
   - *Flagship*: Notes the claim is vendor-authored (Tier 1 marketing), checks hardware/dataset conditions, and flags if independent Tier 2 benchmarks disagree.
3. **Regulatory / Policy Lookup**:
   - *Naive*: Summarizes an undated forum thread.
   - *Flagship*: Cites the official statute/documentation URL, effective date, and explicitly notes any jurisdiction or version caveats.
