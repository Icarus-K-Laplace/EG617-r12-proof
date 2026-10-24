# Progress Log — Finite-Tail Certification

## 2026-10-24 — FT-001: solver-neutral certification boundary established

Status: **SUBSTANTIVE ADVANCE / FRAMEWORK_READY**.

### Repository isolation

Created and used only:

- branch `workstream/general-r-finite-tail-20261024`;
- directory `general_r/workstreams/finite-tail-chat-20261024/`.

Base/reference: `workstream/general-r-architecture-20261024`.

### Theory integrated

Read and separated the following interfaces:

1. general residual-core q ceiling and missing-degree collapse;
2. latest asymptotic sensitivity/small-r audit;
3. latest three-anchor integration status;
4. historical r=12 contextual recurrence certificate and its independent replay receipt.

The key scope correction is preserved: the r=12 machine certificate checks exact contextual arithmetic, while its bridge is still explicitly OPEN. It is not a graph-existence certificate.

### New machinery

Added:

- `generate_instance.py` — deterministic `generate_instance(r)` V1 CSP generator;
- `verify_instance.py` — independent tiny verifier, no generator import;
- `TEST_VECTORS.json` — frozen r=12..15, two-profile regression hashes;
- `verify_test_vectors.py` — independent replay of all frozen vectors;
- `ASSUMPTION_LEDGER.md` — analytic/machine theorem gate;
- `CERTIFICATE_SCHEMA.md` — universal certificate/replay interface;
- `CANONICAL_STATE.md` — support/search-space/readiness matrix;
- `README.md` — operator/replay documentation.

### Search-space result

For the first exact scalar pruning layer:

- `r=12,13,14`, baseline RC leaves 9 missing-degree values / 5 reflection reps;
- `r>=15`, baseline RC collapses to 7 values / 4 reflection reps;
- under `RC+ANCHOR_K8`, r=12..15 already have 7 values / 4 reflection reps.

Thus the future finite solver can select modules by parameter instead of replaying the complete r=12 tree.

### Current theorem status

No new fixed parameter is promoted to `PROVED` in this milestone.

Reasons:

- no certified global `r0` yet;
- RC/front extraction is still open in the general programme;
- residual endpoint and design-terminal bridges remain live;
- below r=12 a separate parameter-specific reduction is required.

### Immediate response if r0 lands

Freeze the sibling theorem commit, populate the finite interval, classify each r by available theorem modules, start from the high end, use endpoint-only solver modules for r>=15, and emit LRAT/DRAT or exact bounded-enumeration certificates with independent replay.


## 2026-10-24 — FT-002: theorem-aware endpoint module passes conditional promotion gate

Status: **CONDITIONAL_MODULE_CERTIFIED / NO NEW EG617(r) THEOREM**.

### New pipeline

Added:

- `generate_endpoint_domain.py`: deterministic exact-integer module certificate producer;
- `verify_endpoint_domain.py`: independent verifier with no generator import;
- `theorem_promotion_gate.py`: verifier replay + per-r assumption lookup; unknown assumption IDs fail closed;
- `THEOREM_PROMOTION_GATE.md`;
- `ENDPOINT_MODULE_SCHEMA.md`;
- `SYMMETRY_CERTIFICATION.md`;
- `GRAPH_CSP_ADAPTER.md`;
- `CERTIFICATE_REPLAY_REPORT.md`.

Added a machine-readable status snapshot to `ASSUMPTION_LEDGER.md`.

### First completed module

`ENDPOINT_DOMAIN_LOWER_BOUND_V1` derives the exact necessary missing-degree domain from the proved conditional ingredients

- `q_y >= d(r+1-d)`;
- `q <= 3r+2` under RC, or `q <= 3r-1` under RC + ANCHOR_K8.

It emits all d-rows from 0 through r, exact slack values, candidate degrees, scalar-reflection classes, and hashes. The independent verifier rebuilds these data from r/profile and rejects any altered row. The gate may promote the conditional lemma but explicitly blocks EG617(r).

### Committed replay example

- r=13, profile=residual-core;
- 14 complete rows; q_cap=41;
- candidate degrees: `[0,1,2,3,4,10,11,12,13]`;
- instance SHA-256: `0b6dce65ae4ac393e5170c6330f7e571800dc34c0fbcb990d57f3718675ddfef`;
- certificate SHA-256: `2b2526cd2281e44425ebe0dd3ef08fc04cf95c04f5003e918de3a0496f4976f4`;
- verifier SHA-256: `1a6ac72042fa7b3a95215c3e2854f661a6cd63c11b879d865af028a91962e6e4`;
- gate SHA-256: `d239d700ecb2f246c750af4b1acb76d6c38b1bdf5c42dadaeeb3adaac23ef7bc`;
- gate result: `PASS_CONDITIONAL_MODULE`;
- RC status: `OPEN`;
- EG617(13): **not proved**.

### Replay and adversarial checks

- Full CLI producer -> verifier -> gate: PASS for r=12,13,14,15,68 under both profiles (10 cases).
- Exact arithmetic sweep: r=4,...,100 under both profiles; all row lists complete and reflection classes partition candidate degrees.
- Boundary regression: baseline d=4 survives at r=12,13,14 and is excluded at r=15; the anchor ceiling excludes d=4 for r=12,...,15.
- Tampered admissibility bit: verifier rejected the certificate.
- Unknown assumption ID in the ledger: gate returned `BLOCKED_UNKNOWN_ASSUMPTION_ID`.
- r=11: schema generation succeeds, but theorem gate returns `SCHEMA_ONLY` / `BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE`.

The finite sweep is an implementation audit only, not an all-r proof. No graph-level CSP, SAT proof, LRAT/DRAT, exact ILP certificate, or new EG617(r) theorem was produced.

### Open interfaces

- RC/front extraction remains OPEN.
- ASYMPTOTIC_R0 remains unavailable.
- d0/d1/d2/d3 endpoint closure and high-endpoint kernel are not encoded as hard constraints.
- Graph-level color/vertex symmetry witnesses are specified but not implemented.
- Design-terminal classification/nonextension remains an external OPEN gate.
