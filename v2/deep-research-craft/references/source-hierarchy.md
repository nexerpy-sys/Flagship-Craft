# Source Hierarchy & Contradiction Resolution

## 1. Authority Ladder (Highest to Lowest)

| Tier | Source Type | Examples | Rule |
| --- | --- | --- | --- |
| **Tier 1 (Primary)** | Official owner / raw artifact | Official docs, RFCs, SEC filings, peer-reviewed papers, vendor pricing/SLA pages, git changelogs | Gold standard. Always prefer over commentary. |
| **Tier 2 (Authoritative)** | Official registries & reproducible data | `pypi.org`, `npmjs.com`, government/census datasets, official benchmarks | Cite with exact version/date. |
| **Tier 3 (Secondary)** | Reputable engineering/industry analysis | Established engineering blogs, investigative journalism | Use for context; corroborate numbers against Tier 1–2. |
| **Tier 4 (Unverified)** | SEO listicles, forums, undated blogs | Reddit, Quora, AI-generated summaries, undated comparison sites | **Never** cite as settled fact. Treat as leads only. |

## 2. Contradiction Resolution Protocol

When two sources disagree on a number, date, capability, or price:
1. **Quote both** with their exact values, publication/update dates, and URLs.
2. **Trace provenance**: Check which source is closer to the Tier 1 origin and which is more recent.
3. **Resolve or Flag**: State the resolved truth and why—or, if neither is authoritative, mark the field `CONFLICTING` and present both sides.

## 3. Anti-Smoothing Rules

- Never average conflicting numbers.
- Never extrapolate a missing tier ("Enterprise is probably ~$500/mo")—write `NOT FOUND (custom/unpublished)`.
- Never strip dates from fast-moving claims (pricing, API limits, model specs).
