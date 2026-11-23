# Risk, Reversibility & Zero-Downtime Migrations

Every architectural decision has a **reversibility cost**. Spend 80% of your planning rigor on **one-way doors** (data models, public APIs, live migrations, auth/billing) and move fast on **two-way doors**.

---

## 1. Reversibility Classification

| Decision Type | Door Type | Required Rigor |
| --- | --- | --- |
| Internal helper naming, local CSS, test file layout | **Two-Way Door** | Decide immediately, state assumption, move on. |
| Adding a nullable column or additive API field | **Two-Way Door** | Safe if backward-compatible with old readers/writers. |
| Dropping/renaming a live column, changing primary keys | **One-Way Door** | Mandatory **Expand -> Migrate -> Contract** plan + rollback. |
| Public API breaking change, auth model, billing/ledger | **One-Way Door** | Versioning/deprecation window + explicit user approval. |

---

## 2. Zero-Downtime Migration Pattern (Expand -> Migrate -> Contract)

Never rename, split, or drop a live column/table in a single deploy—old application instances will crash mid-rollout.

1. **Expand**:
   - Add the new column/table (nullable or with a safe default).
   - Deploy app code that **dual-writes** to both old and new columns while still reading from the old column.
2. **Migrate**:
   - Backfill historical rows in **bounded batches** (e.g., 1,000 rows per transaction with `sleep(50ms)`) so you never lock the table or saturate replication lag.
   - Verify row counts and checksums between old and new columns.
3. **Contract**:
   - Deploy app code that reads from the new column (still dual-writing).
   - Once verified in production, stop writing to the old column, then drop it in a final, separate migration.

---

## 3. Blast-Radius & Rollback Checklist

Before executing any risky change or migration:
- **Feature Flag / Kill Switch**: Can we disable the new code path in `<30 seconds` without a full redeploy?
- **Rollback Verification**: If we roll back the app binary, will it still work against the current DB schema? (Additive-only migrations guarantee this).
- **Data Backup / Snapshot**: For destructive backfills or bulk updates, snapshot or export affected rows before running.

---

## 4. Contrastive Anchors (Naive vs. Flagship Risk Planning)

1. **Renaming a Live Column**:
   - *Naive*: Runs `ALTER TABLE users RENAME COLUMN name TO full_name;` and deploys new code simultaneously. Running pods throw `500 UndefinedColumn` for 3 minutes during rollout.
   - *Flagship*: Adds `full_name` (nullable), dual-writes, backfills in 1,000-row batches, switches reads, and drops `name` in a later deploy.
2. **Bulk Data Backfill**:
   - *Naive*: Runs `UPDATE orders SET currency = 'USD' WHERE currency IS NULL;` across 15 million rows in one transaction, locking the table and causing a site-wide outage.
   - *Flagship*: Loops `WHERE id > :last_id AND currency IS NULL LIMIT 1000` with brief pauses and progress logging.
3. **Third-Party Vendor Integration**:
   - *Naive*: Scatters raw Stripe/Twilio SDK types across 18 controllers.
   - *Flagship*: Wraps the vendor behind a narrow internal adapter interface (`PaymentGateway`), making provider swaps or mocking a two-way door.
