# Architecture Patterns, Boundaries & Trade-Offs

This playbook governs how you choose system boundaries, communication patterns, and data ownership before writing code. The goal is to prevent **premature distribution** (microservices/queues where a monolith belongs) and **accidental coupling** (shared mutable tables where explicit contracts belong).

---

## 1. Architecture Selection Matrix

| Workload Profile | Recommended Pattern | Avoid | Why |
| --- | --- | --- | --- |
| **<50 RPS, 1–5 engineers, fast iteration** | Modular monolith + single Postgres/SQLite | Microservices, Kafka, service mesh | Network hops add latency, distributed transactions, and ops overhead without solving any real bottleneck. |
| **Long-running or flaky external work** (PDFs, emails, webhooks, LLM calls) | Transactional Outbox + background worker | Calling external APIs inside HTTP request or DB transaction | Keeps HTTP p99 fast, prevents DB connection pool exhaustion, and guarantees at-least-once delivery. |
| **Read-heavy dashboard / analytics** | Materialized views or pre-aggregated summary tables | Live `GROUP BY` across 10M+ rows on every page load | Protects OLTP write latency and keeps dashboard p95 under 200ms. |
| **Multi-tenant SaaS** | Shared schema with mandatory `tenant_id` + row-level scoping | Separate DB per tenant (unless strict regulatory isolation) | Keeps migrations O(1) instead of O(N tenants). |

---

## 2. Boundary & Coupling Rules

1. **Depend on Interfaces, Own Your Data**:
   - Two modules may call each other through explicit service/function boundaries, but **never** reach into another module's private database tables.
2. **Sync vs. Async Decision Rule**:
   - Use **synchronous** calls only when the caller *must* have the result to render the immediate response (e.g., auth check, balance validation).
   - Use **asynchronous** queues/outbox for everything else (notifications, audit logs, webhook fan-out, search indexing).
3. **Failure Isolation (Bulkheads)**:
   - Isolate heavy/untrusted workloads (PDF rendering, CSV imports, third-party webhooks) into separate worker pools or timeouts so a spike in one cannot starve core user traffic.

---

## 3. Concrete Failure Modes & Verification

- **Failure Mode 1: Distributed Monolith**: Splitting into 4 services that all share one database and deploy in lockstep. *Check*: Can each module/service be tested and deployed without coordinating schema changes across 3 repos?
- **Failure Mode 2: Dual-Write Drift**: Writing to Postgres and then publishing to Redis/Kafka outside a transaction; the process crashes in between. *Check*: Use the **Transactional Outbox** pattern—write the event to an `outbox` table in the *same* DB transaction, then relay it asynchronously.
- **Failure Mode 3: Unbounded Fan-Out**: One user action triggers 500 synchronous downstream calls. *Check*: Cap batch sizes and move fan-out to a rate-limited worker.

---

## 4. Contrastive Anchors (Naive vs. Flagship Architecture)

1. **Order + Email + Analytics**:
   - *Naive*: Inside `POST /orders`, opens a DB transaction, inserts the order, calls SendGrid, calls Mixpanel, and commits. When SendGrid times out after 10s, the DB transaction rolls back and the user gets a 500 even though their card was charged.
   - *Flagship*: Inserts the order + an `order_created` outbox row in one 5ms DB transaction, returns `201 Created`, and lets a background worker deliver the email and analytics with retries.
2. **Internal Admin Tool**:
   - *Naive*: Proposes Kubernetes, RabbitMQ, Redis, and 3 FastAPI microservices for a 20-user internal ops dashboard.
   - *Flagship*: Proposes a single modular monolith + Postgres/SQLite with clean internal module boundaries, keeping deployment to 1 container and migrations to 1 command.
3. **File Processing Pipeline**:
   - *Naive*: Uploads a 50MB CSV, parses it synchronously in the web worker, and blocks the event loop for 12 seconds.
   - *Flagship*: Streams upload to object storage, enqueues a job with `status = 'pending'`, returns `202 Accepted` with a job ID, and processes in a bounded worker.
