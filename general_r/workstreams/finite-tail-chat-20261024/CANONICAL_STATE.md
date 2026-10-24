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
- gate SHA-256: `415191c88737a23e03df41c011b5d4fdb01537f4455985a2f26d0a30968e565d`;
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


## 11. Round 2 — parameter-exact theorem admission

Starting HEAD was verified as `3d27693d9f9d5bf2586e0f0178228563d96de22b`. All new and modified files remain inside this workstream directory.

Added `PARAMETER_ADMISSION_MATRIX.json` and `PARAMETER_ADMISSION_VERIFIER.py`.

- Explicit rows: r=4,...,100 (97 parameter rows), with a four-interval partition extending to every integer r>=4.
- Source records: eight immutable theorem/asset records, including source commit, source path/blob, exact parameter applicability, proof type, assumptions, and terminal contract.
- Matrix raw SHA-256: `037ebe8e26f0c72e135e3d6a560d4620f023cb52b0c4d8e87096c12e0a8828da`.
- Admission verifier SHA-256: `08d8e58ae6713cf8ab94b1e2dbb3715cd920f4255d21792b7a6d801be04dc326`.
- Theorem gate now calls the admission verifier before promotion and records the matrix/verifier fingerprints in its receipt.
- Unified entry point: `generate_parametric_certificate.py`, which reuses the existing endpoint-domain and d1 generators rather than reimplementing their arithmetic.

### Parameter status

| Parameter range | Admitted facts | Still open |
|---|---|---|
| 4<=r<=11 | no registered general residual-core reduction | r=4,5 are counterexamples only to the abstract M_r(2) cutoff contract; r=6..11 have low-order recurrence cutoff sublemmas, but no full original-graph reduction |
| r=12..16 | conditional q-ceiling source applies under RC; fixed r=12 recurrence arithmetic is replayed | RC/front extraction; broad ANCHOR_K8 below 68; recurrence bridge |
| r=17..67 | full core contract follows analytically once a legal 4r+1 residual has been extracted | global residual extraction; broad ANCHOR_K8 below 68; endpoint/design closure |
| r>=68 | broad near-anchor ANCHOR_K8 source applies | RC/front extraction and terminal closure; no unconditional all-large-r theorem |

The exact three-anchor K8 theorem is a separate source for r>=12, but only when three pairwise nonadjacent degree-r anchors are actually established. It is not substituted for the broader near-anchor ANCHOR_K8 assumption.

The scalar audit confirms that under q<=3r+2, the only medium-interval candidates are d=4 and d=r-3 at r=12,13,14; there are none for r>=15. This is a necessary-domain simplification under RC, not a graph-level theorem.

## 12. Parameterized certificate families and receipt contract

- `ENDPOINT_DOMAIN_LOWER_BOUND_V1`: one certificate per r/profile, with all d=0,...,r reconstructed by the independent verifier.
- `D1_SHELL_CLASS_BOUND_V1`: one certificate per r>=12, with N=0,...,6 checked exactly; N=6 exceeds the incidence cap by 2. Owner multiplicity remains unbounded by this lemma.
- `FINITE_TAIL_RECEIPT_SCHEMA.md` and `FINITE_TAIL_REPLAY_PROTOCOL.md` define the full theorem-receipt interface and promotion invariant.

Independent arithmetic audit performed in a Python harness:
- endpoint-domain arithmetic checked for r=12,...,100, 5,073 d-rows;
- D1 checked for r=12,...,100, 623 class-count rows;
- r=12,13,14 medium boundary candidates and r>=15 elimination matched the exact formulas;
- six d1 classes contradicted the cap by exactly 2 for every tested r.

## 13. Graph-level symmetry interface

Added `GRAPH_SYMMETRY_WITNESS_SCHEMA.md`, `GRAPH_SYMMETRY_VERIFIER.py`, and `GRAPH_SYMMETRY_TEST_VECTORS.json`.

The toy fixture has 8 fully enumerated edge-colorings of K3, one distinguished pivot and a two-vertex shell role; exhaustive role-preserving vertex swap and global color swap yield 3 orbits. The independent Python reconstruction checked all 8 witness mappings and matched the committed pre/post state-set hashes:
- pre-quotient: `1c10fd6173e748ff06f912ebae87d5bf4c6c2002a88ad54f8671a53a9fc0d18c`;
- post-quotient: `344254a1cfc131a437ced79dff954c6e79ca02c7a8ca7ff97556d7c770b752cf`.

The committed graph-verifier CLI has not yet been run directly in a repository execution environment. Therefore this is an independently cross-checked toy fixture/interface, not a claim that graph-level EG617 symmetry reduction is certified.

## 14. Round 2 promotion verdict

- Theorem-admission matrix: constructed; 97/97 committed rows matched an independent reconstruction.
- Parameterized certificate-family interface: constructed; source applicability is checked before generation and the promotion gate rechecks it.
- Graph-symmetry witness interface: constructed; bounded toy fixture cross-checked independently; committed CLI replay pending.
- New EG617(r) theorem: **NONE**.
- `ASYMPTOTIC_R0`: **NOT AVAILABLE**.
- `RC` and global extraction: **OPEN**.


Round-2 implementation fingerprints:
- theorem gate SHA-256: `7f3dfb534ecb6c6b81d129ee0c96a8a141277188f133d05fcf52f8206094ce84`
- unified family wrapper SHA-256: `8ab57ec8f005061fd1aa234b24e8e434d36bcbd77149e6caa9a1e5f7de9fc36a`
- graph symmetry verifier SHA-256: `6f6c484575772b72324ee0e4ad3495c93fb1b39ebb6f35e981fa54277a952f4c`
- graph symmetry test-vector file SHA-256: `72ed53eb8f05d1a1531595076f018a5e31c8f66388cf230dfff70a88bfbdc05a`


### Source-proof scope note

The admission registry freezes exact source commits, paths, and blob hashes and verifies their parameter statements/ranges. It does not claim that this finite-tail workstream independently reproved every upstream analytic theorem. Each source record has a `local_audit_status` distinguishing source-scope verification from proof reproduction; only the D1 integer consequence and toy symmetry fixture received separate local arithmetic/witness checks here.


### Front-recurrence source nuance

The matrix now records `FRONT_RECURRENCE_TERMINATION` and `LOW_ORDER_CUTOFF_THEOREMS` as additional source entries. The potential-function theorem is valid for r>3 conditional on a finite sound seed/cutoff package; M_r(2), M_r(3) cutoffs are proved for r>=6 inside the abstract recurrence contract. The r=4,5 examples refute extension of the abstract M_r(2) cutoff only, not EG617(r). The complete original-graph bridge, seed-floor package, and all-state outer-budget dominance remain OPEN.
