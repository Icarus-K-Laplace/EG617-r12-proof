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
- the inherited hereditary cap used by the general-r backend is valid.

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

Current analytic status: the asymptotic sibling records an analytic proof for every `r>=68`. For `12<=r<68`, this finite-tail workstream does **not** assume it silently; a parameter-specific proof/certificate is required before a `near-anchor` instance can be used in a theorem chain.

Integration references:

- asymptotic head observed: `cd38647f85de9827a784288e69bad7a66d1e4e3a`;
- three-anchor head observed: `a98ef900be419993e3fe63d37a0cf82fa104c455`.

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
