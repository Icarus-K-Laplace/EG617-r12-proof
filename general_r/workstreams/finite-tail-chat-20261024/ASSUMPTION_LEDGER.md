# Finite-Tail Assumption Ledger

This ledger is a hard interface between the analytic general-r workstreams and any finite computation in this directory.

**Certification rule.** A finite certificate for parameter `r` may be promoted to an EG617 theorem only when every assumption ID consumed by the generated instance is separately certified for the same `r`. A SAT/ILP/CSP `UNSAT` result never upgrades an `OPEN` analytic bridge.

## RC — residual-core contract

Consumed by profile: `residual-core` and `near-anchor`.

Contract:

- legal residual `F` has `|F|=4r+1`;
- a legal pivot has degree `r+1`;
- the associated core `H` has `|H|=3r-1`;
- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- `delta(H)>=r`;
- the inherited hereditary cap used by the general-r backend is valid;
- legal repivots used by the backend preserve the core contract (the backend closure interface remains conditional until its upstream gates are discharged).

Once RC is available, the proved symbolic backend gives

- `e(F)<=2r^2+4r+4`;
- `e(H)>=(r(3r-1)+2)/2`;
- `q<=3r+2`;
- every regular repivot with missing degree `d` obeys `q_y>=d(r+1-d)`.

Current status: **CONDITIONAL / front extraction not yet certified in general.** The source theorem is stated for `r>=12`; the all-r contextual extraction and especially `delta(H)>=r` remain a load-bearing front-end gap.

Primary source: `general_r/GENERAL_R_Q_CEILING_AND_MISSING_DEGREES.md` on the architecture line.

## ANCHOR_K8 — exact/near three-anchor excess floor

Consumed only by profile: `near-anchor`.

Contract:

`K_r = 2e(H)-r(3r-1) >= 8`.

Combined with RC this improves the right-edge ceiling to

`q<=3r-1`.

Current analytic status: the broad near-anchor source is applicable only for `r>=68`. For `12<=r<68`, this finite-tail workstream does **not** assume it silently; a parameter-specific proof/certificate is required before a `near-anchor` instance can use the broad `ANCHOR_K8` profile.

Pinned source used by the existing endpoint generator: branch `workstream/general-r-asymptotic-20261024`, commit `cd38647f85de9827a784288e69bad7a66d1e4e3a`, file `general_r/workstreams/asymptotic-chat-20261024/HYPOTHESIS_SENSITIVITY.md`.

Latest status sync: commit `aa7fbbda16ff0170c9bf7c440ca961a7a8aab3c0`, file `general_r/workstreams/asymptotic-chat-20261024/CANONICAL_STATE.md`; it preserves the same `r>=68` scope and records A_ext, C*, D as open.

Three-anchor sibling head: `a934c3ccc22b6991cca5ba82f49ac9f3400748f0`; its exact three-anchor theorem is separately registered and is not interchangeable with this broader profile.

## QCAP_BASE — baseline q ceiling

Derived assumption, not an independent hypothesis.

Dependencies: `RC`.

Conclusion: `q<=3r+2`.

## QCAP_ANCHOR — strengthened q ceiling

Derived assumption, not an independent hypothesis.

Dependencies: `RC + ANCHOR_K8`.

Conclusion: `q<=3r-1`.

## R12_FRONTEND_REC — historical r=12 contextual recurrence certificate

Scope: fixed `r=12` front-end arithmetic only.

Repository assets: `certificates/frontend_line_a_v1/`.

Recorded status:

- reduction status: `PROVED`;
- arithmetic status: `COMPUTATION_CERTIFIED`;
- independent replay: `PASS`;
- recurrence nodes: 1752;
- outer comparisons: 144;
- bridge status: **OPEN**.

Therefore this asset can be reused as a certified finite arithmetic sublemma, but it is **not** a graph-existence certificate, not generic `R(4,49)` emptiness, and not by itself a proof of EG617 for `r=12`.

## ASYMPTOTIC_R0 — eventual theorem threshold

Current status: **NOT AVAILABLE**.

The latest asymptotic integration has removed exact three-anchor as an asymptotic blocker above 68, but still lists the following as live bottlenecks:

1. front extraction/core certification (`H_A` / RC source);
2. residual endpoint terminal closure (`H_C*`);
3. robust design-terminal classification/nonextension (`H_D`).

When a sibling branch certifies a concrete `r0`, this ledger must record the exact theorem statement and immutable source commit before the finite range `4<=r<r0` is declared.

## r<12 policy

`generate_instance.py` accepts every integer `r>=4` so that the certificate format is universal, but the current general-r residual-core source theorem is only marked applicable from `r>=12`.

Thus for `4<=r<12` the generated payload is a **schema/encoding test only** unless a separate parameter-specific reduction theorem is attached. No computation in this directory may infer RC below 12 from the formula alone.

## Status vocabulary

- `PROVED_ANALYTIC`: complete analytic implication, no machine search required.
- `COMPUTATION_CERTIFIED`: exact finite implication independently replayed under its listed assumptions.
- `CONDITIONAL`: implication proved only after one or more explicit assumption IDs.
- `OPEN`: required implication not yet certified.
- `SCHEMA_ONLY`: deterministic instance/certificate plumbing exists, but no theorem claim follows.


## Machine-readable theorem-gate snapshot (2026-10-24)

The theorem-promotion gate reads these lines as the current explicit status interface. A range-limited theorem is considered applicable only when the requested r lies in its stated range.

- RC: OPEN
- ANCHOR_K8: PROVED_ANALYTIC for r>=68; OPEN for 12<=r<68
- ASYMPTOTIC_R0: OPEN
- R12_FRONTEND_REC: COMPUTATION_CERTIFIED_ARITHMETIC_ONLY; BRIDGE_OPEN


## Parameter-exact source reconciliation — 2026-10-24

The machine-readable registry distinguishes **source theorem applicability** from **discharge of the assumption needed by the original EG617 reduction**.

### RC_FROM_EXTRACTED_RESIDUAL

- Source: branch `workstream/general-r-residual-core-extraction-20261024`, commit `614a956a7e964f42c0818eca05e3ca9e26a6458a`, file `general_r/workstreams/residual-core-extraction-chat-20261024/RESIDUAL_BRANCH_CLOSURE.md`.
- Range: every `r>=17).
- Theorem: once an induced legal `4r+1` residual exists, the full residual/core contract follows analytically.
- Status: **PROVED ANALYTICALLY CONDITIONAL ON EXTRACTION**. The extraction/stopping dichotomy from the original counterexample remains OPEN, so this does not change the global RC status to PROVED.

### ANCHOR_K8 — broad near-anchor contract

- Broad theorem source: branch `workstream/general-r-asymptotic-20261024`, commit `aa7fbbda16ff0170c9bf7c440ca961a7a8aab3c0`, file `general_r/workstreams/asymptotic-chat-20261024/CANONICAL_STATE.md`.
- Range: `r>=68) only.
- Status: **PROVED_ANALYTIC_FOR_R_GE_68** in the stated broad near-anchor context; OPEN for `12<=r<68).
- Do not infer the broad theorem below 68 from the exact-anchor theorem below.

### EXACT_THREE_ANCHOR_K8 — specialized theorem, not a substitute for broad ANCHOR_K8

- Source: branch `workstream/general-r-three-anchor-20261024`, commit `a934c3ccc22b6991cca5ba82f49ac9f3400748f0`, file `general_r/workstreams/three-anchor-chat-20261024/PUBLICATION_VERSION.md`.
- Range: every `r>=12).
- Exact contract: `|V(H)|=3r-1), `alpha(H)<=3), `omega(H)<=r-1), `delta(H)>=r), and three pairwise nonadjacent vertices of degree exactly `r).
- Conclusion: `K=2e(H)-r(3r-1)>=8).
- Status: independently audited analytic proof under that exact three-anchor hypothesis. This does **not** discharge broad `ANCHOR_K8) when the three-anchor premise is not established.

### D1_SHELL_CLASS_BOUND source

- Source: branch `workstream/general-r-repivot-termination-20261024`, commit `35fec3eaaab70b31e10b41065634b35b02a28e6`, file `general_r/workstreams/repivot-termination-chat-20261024/ENDPOINT_CLASSIFICATION.md`.
- Range: `r>=12`, conditional on A+B / RC + broad ANCHOR_K8.
- Conclusion: at most five distinct d1 shell classes. This does not bound owner multiplicity within a class and does not close d1 nonextension.

### Additional source-premise IDs

- `EXTRACTED_4R_PLUS_1_RESIDUAL: OPEN` — a conditional input to the r>=17 residual/core theorem; global extraction remains open.
- `NEAR_ANCHOR_TERMINAL_CONTRACT: CONDITIONAL` — must be established by the active analytic branch for the exact object; it is not supplied by a scalar certificate.
- `CORE_CONTRACT: CONDITIONAL_ON_RC` — the exact core hypotheses required by the specialized three-anchor theorem.
- `THREE_PAIRWISE_NONADJACENT_DEGREE_R_ANCHORS: CONDITIONAL` — a premise, not a universally established configuration.
- `R12_CONTEXTUAL_RECURRENCE_BRIDGE: OPEN` — the historical r=12 arithmetic replay does not close the graph-level bridge.

The parameter-admission matrix explicitly keeps all of these distinctions. No source in this ledger currently certifies an unconditional asymptotic threshold `r0); `ASYMPTOTIC_R0=NOT_AVAILABLE`.


## Machine-readable source-premise status additions

- EXTRACTED_4R_PLUS_1_RESIDUAL: OPEN
- NEAR_ANCHOR_TERMINAL_CONTRACT: CONDITIONAL
- CORE_CONTRACT: CONDITIONAL_ON_RC
- THREE_PAIRWISE_NONADJACENT_DEGREE_R_ANCHORS: CONDITIONAL
- R12_CONTEXTUAL_RECURRENCE_BRIDGE: OPEN
