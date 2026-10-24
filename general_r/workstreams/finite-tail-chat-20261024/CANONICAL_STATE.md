# EG617 General-r Finite-Tail — Canonical State

Date: 2026-10-24

Branch: `workstream/general-r-finite-tail-20261024`

Directory: `general_r/workstreams/finite-tail-chat-20261024/`

Headline status: **CONDITIONAL_MODULE_CERTIFIED / NO NEW EG617(r) THEOREM**.

The workstream now has a deterministic reduced-CSP generator, immutable hashes, an independent tiny verifier, an explicit analytic-assumption ledger, and a universal certificate interface. It does **not** claim an EG617 parameter is closed merely because the reduced scalar instance is generated or verified.

## 1. Currently supported r

| range | generator | current general reduction source | theorem closure in this workstream |
|---|---|---|---|
| `4<=r<12` | yes, schema test | not certified by current RC source | none |
| `r=12` | yes | conditional RC machinery exists; historical recurrence arithmetic certified but bridge open | none newly certified |
| `r=13,14` | yes | RC symbolic backend applicable conditionally | none |
| `r>=15` | yes | RC symbolic backend applicable conditionally; baseline medium-d collapse available | none |
| `r>=68` | yes | same RC caveat; sibling records ANCHOR_K8 analytically proved | none until RC/front + remaining terminal bridges close |

A future concrete `r0` will define the actual finite tail `4<=r<r0`.

## 2. Theoretical assumptions

See `ASSUMPTION_LEDGER.md`.

The V1 profiles are:

- `residual-core`: consumes `RC`, hence `q<=3r+2`;
- `near-anchor`: consumes `RC + ANCHOR_K8`, hence `q<=3r-1`.

The finite machine layer is forbidden to infer either assumption from a successful search.

## 3. Current reduced search space

The first solver-neutral CSP variable is the regular-repivot missing degree

`d in {0,...,r}`

subject to

`d(r+1-d)<=q_cap`.

This is the first exact pruning layer, not the final graph search.

Regression values:

| r | profile | raw d states | q-filter survivors | reflection orbit reps |
|---:|---|---:|---:|---:|
| 12 | residual-core | 13 | 9 | 5 |
| 12 | near-anchor | 13 | 7 | 4 |
| 13 | residual-core | 14 | 9 | 5 |
| 13 | near-anchor | 14 | 7 | 4 |
| 14 | residual-core | 15 | 9 | 5 |
| 14 | near-anchor | 15 | 7 | 4 |
| 15 | residual-core | 16 | 7 | 4 |
| 15 | near-anchor | 16 | 7 | 4 |

Consequences already visible from the symbolic theory:

- baseline RC retains the boundary `d=4` state at `r=12,13,14`;
- baseline RC removes all medium degrees from `r>=15`;
- under `ANCHOR_K8`, `d=4` is already removed for every `r>=12`;
- hence the finite solver for large tail parameters should not inherit the r=12 medium-support case tree.

## 4. Symmetry reduction

Implemented now:

- exact endpoint reflection `d <-> r+1-d` on the reduced scalar domain;
- deterministic orbit representatives.

Specified but **not yet implemented** at graph/SAT level:

- color permutation quotient;
- vertex permutation quotient;
- canonical colored-incidence labeling;
- degree/support invariant refinement;
- stabilizer-based orbit branching with verifier-checkable witnesses.

The graph-level quotient cannot be counted as a reduction until the witness checker exists.

## 5. Certificate format

Defined in `CERTIFICATE_SCHEMA.md`.

Priority:

1. analytic proof;
2. exact bounded enumeration;
3. SAT + LRAT/DRAT proof;
4. exact rational/integer ILP certificate;
5. Lean/Coq formal implication layer.

Every final parameter receipt must bind the theorem statement, analytic source commit, assumption IDs, instance hash, symmetry specification, certificate hash, verifier hash, replay command, finite result, bridge status, and theorem status.

## 6. Independently replayed / cross-checked cases

Historical repository asset:

- `r=12` contextual front-end recurrence: 1752 nodes and 144 outer comparisons have an independent replay receipt `PASS`;
- its bridge remains explicitly `OPEN` and it is not a graph-completion certificate.

New V1 harness regression vectors have been independently re-derived with the verifier formula at authoring time and frozen in `TEST_VECTORS.json` for `r=12,13,14,15`, both profiles. They certify deterministic encoding/hash behavior only.

Example hashes:

- `r=12`, residual-core: `5c5a0b373badd75a567e1022388489d1af96daa5b0fa31faa04fa7aac1d017d6`;
- `r=13`, residual-core: `cb981c74dbe6940cc9612dbb5b0509dd2dc08239fe2b71af7f6c43f059a1c551`;
- `r=13`, near-anchor: `cae385bd5e9fd8ddde967a7c04abad8419a2ac22c1f918916257a0756d679254`;
- `r=15`, residual-core: `8a633b97f0130b4b0f81489d143327da704d222b0e35fb55653854c0e270d2e6`.

## 7. Uncertified cases

At present this workstream has **no newly certified EG617(r) row**.

The following remain theorem-level blockers rather than solver failures:

- the general front extraction / RC source;
- residual endpoint terminal closure needed by the asymptotic synthesis;
- design-like terminal classification/nonextension interface;
- for finite `12<=r<68`, parameter-specific availability of ANCHOR_K8 whenever the near-anchor profile is used;
- for `4<=r<12`, a parameter-specific reduction replacing the current r>=12 RC source.

No global SAT instance has yet been emitted, because doing so before the analytic reduction is stable would certify the wrong search space.

## 8. If r0 appears today

Immediate solver admission policy:

1. ingest the sibling theorem statement and immutable source commit into `ASSUMPTION_LEDGER.md`;
2. partition `4<=r<r0` by which analytic reductions are certified for each `r`;
3. prioritize highest `r` first, because `r>=15` already has endpoint-only baseline missing-degree support and therefore a much smaller module set than r=12;
4. for `r>=68`, ANCHOR_K8 is already available from the sibling analytic result, subject still to RC/front compatibility;
5. treat `r=13,14` separately because baseline RC leaves the `d=4` boundary, while the strengthened anchor profile removes it;
6. treat `r=12` with its historical certified recurrence plus only the genuinely r=12-specific modules recorded by the asymptotic small-r audit;
7. only then descend toward `r<12`, where a separate reduction interface is needed.

This prevents wasting computation on parameters that analytic theory already collapses or on instances whose bridge is not yet proved.

## 9. Theorem-promotion milestones — 2026-10-24

A first real conditional endpoint module has completed the full producer -> certificate -> independent verifier -> theorem-promotion gate path:

- module: `ENDPOINT_DOMAIN_LOWER_BOUND_V1`;
- committed artifact: `certificates/endpoint_domain_r13_residual_core.json`;
- replay receipt: `certificates/endpoint_domain_r13_residual_core_receipt.json`;
- r=13 residual-core instance SHA-256: `65909c3589061e7463e807579bdde059ee7ae4d20f57f53158e5a612ae2d6c42`;
- certificate SHA-256: `aa2123245e1bd6db9ab7056c3c2b0083f1d2f3828d39f40b54c731ba113b170a`;
- verifier SHA-256: `c18a74703417faed2c453b588e0ea9a8b03244af04bfc0b5f4191ec8cc15de6a`;
- generator SHA-256: `b29179be0386b44168450cab23fa3591c187222a32194ee086a05a5bca4d6758`;
- verifier SHA-256: `c18a74703417faed2c453b588e0ea9a8b03244af04bfc0b5f4191ec8cc15de6a`;
- gate SHA-256: `da90253d941ceb184f5c74a603cda70c5dda466fd3936de484b82924783b032c`;
- gate: `PASS_CONDITIONAL_MODULE`; theorem status: `CONDITIONAL_LEMMA_CERTIFIED`;
- RC remains `OPEN`, so EG617(13) remains **NOT PROVED**.

A second, genuine endpoint-class module is now replayed:

- module: `D1_SHELL_CLASS_BOUND_V1`;
- committed artifact: `certificates/d1_shell_class_bound_r13.json`;
- receipt: `certificates/d1_shell_class_bound_r13_receipt.json`;
- source theorem: repivot endpoint classification, commit `35fec3eaaab70b31e10b41065634b35b02a28e6c`;
- r=13: shell incidence cap 76; five classes require 65, six require 78 and are impossible by gap 2;
- instance SHA-256: `e2606f6a45ce41d5de4a5a184e2a32026259bc2992a73fbe82ce0833a4ae8a5e`;
- certificate SHA-256: `2b82b7c89b8afab0259728a21d6e28ea10ace8a97c7c46455511a381555b0bc8`;
- generator SHA-256: `b0d85a0877953490c5d724365b17c15dfc3113390a578a6813a7ba7b9183d5b6`;
- verifier SHA-256: `e05ff2311275143d7a3a1492141be42b40989c93361e32ec3c2e504a2e5d457a`;
- gate: `PASS_CONDITIONAL_MODULE`; RC and ANCHOR_K8 remain open at r=13; bounded-allowance d1 nonextension remains OPEN.

The independent arithmetic verifier re-derives all seven class-count rows. Final CLI replay passed for the scalar profiles at r=12,13,14,15,68 and for the D1 shell module at r=12,13,68 (13 module/profile runs total). These are conditional local theorems only: neither module proves EG617(13), and neither closes all endpoint states. The r=4,...,100 audit is a finite implementation test, not an all-r theorem. Both module verifiers reject tampered rows, and unknown-ledger-ID tests fail closed as intended.

## 10. Next finite-tail implementation target

Once a sibling workstream supplies a stable terminal contract, build the graph/SAT adapter with:

- deterministic variable map;
- theorem-derived constraint modules selected by `r`;
- canonical colored-incidence labeling and stabilizer witnesses;
- CNF hash;
- LRAT proof production/checking;
- a tiny independent receipt verifier.

Until then, keep the V1 harness as the regression-tested theorem/instance boundary rather than expanding a speculative brute-force encoding.
