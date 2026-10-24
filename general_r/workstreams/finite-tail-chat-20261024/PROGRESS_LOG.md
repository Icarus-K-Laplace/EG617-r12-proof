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
