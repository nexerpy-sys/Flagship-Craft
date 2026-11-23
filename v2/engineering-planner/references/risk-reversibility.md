# Risk & Reversibility Analysis

## 1. Zero-Downtime Migration Pattern (Expand -> Migrate -> Contract)

Never rename or drop a live column/field in one step:
1. **Expand**: Add the new column/field (nullable or with default); write to both old and new.
2. **Migrate**: Backfill historical rows in bounded batches with progress checkpoints.
3. **Contract**: Switch reads to the new column, stop writing the old, then drop the old column in a later deploy.

## 2. Contrastive Anchors (Naive vs. Flagship Planning)

- **Naive**: "We'll use microservices with Kafka and Redis for this 2-user internal tool, and rename `user_name` to `full_name` directly in SQL."
- **Flagship**: "Start with a modular monolith + SQLite/Postgres; use Expand-Migrate-Contract for schema changes; define the 3 core invariants and a 1-command rollback."
