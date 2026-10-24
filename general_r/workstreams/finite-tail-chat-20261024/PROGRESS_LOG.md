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
- instance SHA-256: `65909c3589061e7463e807579bdde059ee7ae4d20f57f53158e5a612ae2d6c42`;
- certificate SHA-256: `aa2123245e1bd6db9ab7056c3c2b0083f1d2f3828d39f40b54c731ba113b170a`;
- verifier SHA-256: `c18a74703417faed2c453b588e0ea9a8b03244af04bfc0b5f4191ec8cc15de6a`;
- gate SHA-256: `415191c88737a23e03df41c011b5d4fdb01537f4455985a2f26d0a30968e565d`;
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


## 2026-10-24 — FT-003: first endpoint-class theorem module replayed

Status: **TWO CONDITIONAL MODULES CERTIFIED / NO EG617(r) PROMOTED**.

### New endpoint module

Added:

- `generate_d1_shell_bound.py`;
- `verify_d1_shell_bound.py`;
- `certificates/d1_shell_class_bound_r13.json`;
- `certificates/d1_shell_class_bound_r13_receipt.json`.

The source is sibling repivot endpoint classification commit `35fec3eaaab70b31e10b41065634b35b02a28e6c`, whose conditional theorem under A+B and r>=12 gives d1 partner incidence `t_s>=r` and total shell incidence `sum_A t_s<=6r-2`.

For r=13, the exact arithmetic verifier checks N=0,...,6. N=6 needs 78 incidences while the cap is 76, a contradiction by exactly 2; hence at most five d1 shell classes. This does **not** bound multiplicity within a class and does not close the d1 terminal.

Hashes:

- instance SHA-256: `e2606f6a45ce41d5de4a5a184e2a32026259bc2992a73fbe82ce0833a4ae8a5e`;
- certificate SHA-256: `2b82b7c89b8afab0259728a21d6e28ea10ace8a97c7c46455511a381555b0bc8`;
- generator SHA-256: `b0d85a0877953490c5d724365b17c15dfc3113390a578a6813a7ba7b9183d5b6`;
- verifier SHA-256: `e05ff2311275143d7a3a1492141be42b40989c93361e32ec3c2e504a2e5d457a`;
- final multi-module gate SHA-256: `415191c88737a23e03df41c011b5d4fdb01537f4455985a2f26d0a30968e565d`.

### Gate hardening

The promotion gate now dispatches by immutable module ID, binds both generator and verifier hashes, and uses the same status vocabulary for different local endpoint lemmas. Unknown module IDs/assumption IDs fail closed. The gate still always blocks EG617 promotion because these modules do not provide complete graph-state exhaustion or a contradiction.

The r=13 endpoint-domain receipt was refreshed to the final gate hash. Both sample receipts explicitly show `PASS_CONDITIONAL_MODULE`, `CONDITIONAL_LEMMA_CERTIFIED`, and `eg617_r_proved=false`.


### Final multi-module CLI replay

With the final module-dispatch gate, end-to-end CLI replay passed for 10 scalar-profile cases (r=12,13,14,15,68 × two profiles) and three D1 shell-bound cases (r=12,13,68). Both verifiers rejected tampered certificates. The gate returned `BLOCKED_UNKNOWN_ASSUMPTION_ID` when RC was omitted from the machine-readable ledger, and r=11 remained `SCHEMA_ONLY`. All 13 matrix runs left `eg617_r_proved=false`. After the final gate was extended to record generation, verifier, and gate replay commands, the two committed r=13 sample certificates were replayed again through that final gate and both passed.


## 2026-10-24 — FT-004: parameter-exact admission + replayable family interface

Status: **MATRIX BUILT / PARAMETRIC FAMILIES WIRED / TOY SYMMETRY INTERFACE BUILT / NO EG617(r) THEOREM**.

### 1. Admission matrix

Added `PARAMETER_ADMISSION_MATRIX.json` with:
- explicit rows r=4,...,100;
- four non-overlapping ranges covering all r>=4;
- six immutable source/asset records with commit, path, blob hash, quantifiers/range, proof type, assumptions, and terminal contract;
- per-module/per-profile admission and assumption state.

The independent matrix verifier reconstructs the row policy, checks source registry and range partition, and supports queries for arbitrary r>=4. A separate JS audit compared all 97 committed rows with independently reconstructed rows: **97/97 matched**. A separate Python harness exercised the verifier logic and rejected a tampered row.

### 2. Source-range reconciliation

The matrix explicitly distinguishes:
- RC q-ceiling source applicable for r>=12 only under RC;
- the full residual/core contract proved for r>=17 **once a legal 4r+1 residual exists**, while extraction remains open;
- broad near-anchor ANCHOR_K8 proved only for r>=68;
- exact-three-anchor K8 proved for r>=12 only under the exact three-anchor premise;
- the r=12 recurrence arithmetic receipt, whose graph-level bridge remains OPEN.

The exact three-anchor theorem is not used as a substitute for the broader near-anchor theorem.

### 3. Parameterized certificate family

Added `generate_parametric_certificate.py` and `PARAMETRIC_ENDPOINT_CERTIFICATES.md`. The wrapper checks source admission, then delegates to the existing module generators and promotion gate. It refuses r<12 for theorem-level family generation. The gate now records admission matrix and verifier hashes.

Exact arithmetic replay (independent Python harness):
- endpoint domain: 5,073 d-values checked for r=12,...,100;
- D1: 623 class-count rows checked for r=12,...,100;
- medium-degree boundary: r=12 -> {4,9}, r=13 -> {4,10}, r=14 -> {4,11}, r>=15 -> empty under baseline q-cap;
- D1 six-class deficit is exactly 2 for every tested r.

### 4. Receipt and symmetry interfaces

Added `FINITE_TAIL_RECEIPT_SCHEMA.md` and `FINITE_TAIL_REPLAY_PROTOCOL.md`.

Added `GRAPH_SYMMETRY_WITNESS_SCHEMA.md`, `GRAPH_SYMMETRY_VERIFIER.py`, and `GRAPH_SYMMETRY_TEST_VECTORS.json`. The toy K3/two-color fixture has 8 states, 3 orbits, and 8 explicit witnesses. An independent Python reconstruction matched both committed state-set digests and validated all 8 witness mappings.

Important execution caveat: the committed `PARAMETER_ADMISSION_VERIFIER.py`, `generate_parametric_certificate.py`, `theorem_promotion_gate.py`, and `GRAPH_SYMMETRY_VERIFIER.py` CLI commands have not been run directly against the remote branch in this session. The matrix, arithmetic, and toy symmetry logic received independent harness checks; the committed CLI replay remains an explicit next step.

### 5. Remaining blockers

- r=4,...,11: no applicable general residual-core reduction source registered.
- RC/front extraction: OPEN for all parameters.
- broad ANCHOR_K8: OPEN for 12<=r<68; source applies for r>=68.
- bounded-allowance d1 nonextension and d2 terminal closure: OPEN.
- robust design-terminal nonextension: OPEN.
- graph-level symmetry completeness for actual EG617 states: OPEN.
- unconditional asymptotic r0: NOT AVAILABLE.

No new EG617(r) theorem is claimed.


### Source-provenance precision

The admission matrix now binds both the endpoint generator's pinned broad ANCHOR_K8 source (`cd38647f85de9827a784288e69bad7a66d1e4e3a`) and the latest asymptotic status sync (`aa7fbbda16ff0170c9bf7c440ca961a7a8aab3c0`). The exact-three-anchor theorem remains a separate r>=12 source with its own premise. Every source record now carries `local_audit_status`, so upstream proof existence is not mislabeled as a proof rederived by this workstream.
