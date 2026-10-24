# Certificate Replay Report — 2026-10-24

## Result

**PASS: first theorem-aware conditional endpoint module completed end to end.**

Module: `ENDPOINT_DOMAIN_LOWER_BOUND_V1` (`constraint_generation_version=endpoint-domain-generator-v1.0.0`)

This is a conditional exact-arithmetic lemma for the necessary missing-degree domain. It is not a graph-level CSP, not an endpoint closure theorem, and not an EG617(r) proof.

## Exact theorem interface

For the residual-core profile, under RC and the source theorem at immutable commit `a922c4d7646eb8d0087bde8547562c8aace02ee2`, the maximal-q ceiling is `q_cap=3r+2`. The regular-repivot lower bound is `q_y >= d(r+1-d)`. Since the selected state is maximal-q and lies under the ceiling, every legal missing degree must satisfy

`0 <= d <= r` and `d(r+1-d) <= 3r+2`.

The near-anchor profile uses `q_cap=3r-1` and adds `ANCHOR_K8`; the ledger records that premise as analytically proved only for r >= 68, while RC remains open.

## Replayed committed artifact

Certificate: `certificates/endpoint_domain_r13_residual_core.json`

Receipt: `certificates/endpoint_domain_r13_residual_core_receipt.json`

For r=13, residual-core:

- rows checked: 14 (every integer d=0,...,13);
- q ceiling: 41;
- admissible necessary-domain degrees: `[0,1,2,3,4,10,11,12,13]`;
- scalar reflection classes: 5, including d=0 retained as an unpaired boundary singleton;
- independent verifier: `PASS`;
- theorem-promotion gate: `PASS_CONDITIONAL_MODULE`;
- module status: `CONDITIONAL_LEMMA_CERTIFIED`;
- RC status: `OPEN`;
- EG617(13) promotion: **BLOCKED / NOT PROVED**.

Hashes:

- instance SHA-256: `65909c3589061e7463e807579bdde059ee7ae4d20f57f53158e5a612ae2d6c42`
- certificate SHA-256: `aa2123245e1bd6db9ab7056c3c2b0083f1d2f3828d39f40b54c731ba113b170a`
- generator SHA-256: `b29179be0386b44168450cab23fa3591c187222a32194ee086a05a5bca4d6758`
- independent verifier SHA-256: `c18a74703417faed2c453b588e0ea9a8b03244af04bfc0b5f4191ec8cc15de6a`
- theorem-promotion gate SHA-256: `415191c88737a23e03df41c011b5d4fdb01537f4455985a2f26d0a30968e565d`

## Commands

From the repository root:

```bash
cd general_r/workstreams/finite-tail-chat-20261024
python generate_endpoint_domain.py 13 --profile residual-core --output certificates/endpoint_domain_r13_residual_core.json
python verify_endpoint_domain.py certificates/endpoint_domain_r13_residual_core.json
python theorem_promotion_gate.py certificates/endpoint_domain_r13_residual_core.json --receipt certificates/endpoint_domain_r13_residual_core_receipt.json
```

The checked-in receipt binds the source assumption, hashes, verifier, gate, and the explicit non-promotion decision. The certificate's canonical hash is independent of pretty-print whitespace.

## Second endpoint module: D1_SHELL_CLASS_BOUND_V1

Certificate: `certificates/d1_shell_class_bound_r13.json`

Receipt: `certificates/d1_shell_class_bound_r13_receipt.json`

The sibling repivot endpoint theorem, source commit `35fec3eaaab70b31e10b41065634b35b02a28e6c`, proves conditionally under A+B and r>=12 that each distinct d1 missing-partner shell vertex contributes at least r to the shell-incidence sum, while the total is at most 6r-2. The exact arithmetic module checks N=0,...,6 and establishes that N=6 requires 6r incidences, exceeding the cap by exactly 2. Therefore the conditional shell-class bound is N<=5.

For r=13:

- incidence cap: 76;
- N=5 requires 65 incidences and has slack 11;
- N=6 requires 78 incidences and has deficit 2;
- rows checked: 7;
- independent verifier: `PASS`;
- theorem-promotion gate: `PASS_CONDITIONAL_MODULE`;
- RC and ANCHOR_K8 are both open for r=13;
- bounded-allowance d1 nonextension remains OPEN; EG617(13) is **NOT PROVED**.

Hashes:

- instance SHA-256: `e2606f6a45ce41d5de4a5a184e2a32026259bc2992a73fbe82ce0833a4ae8a5e`
- certificate SHA-256: `2b82b7c89b8afab0259728a21d6e28ea10ace8a97c7c46455511a381555b0bc8`
- generator SHA-256: `b0d85a0877953490c5d724365b17c15dfc3113390a578a6813a7ba7b9183d5b6`
- independent verifier SHA-256: `e05ff2311275143d7a3a1492141be42b40989c93361e32ec3c2e504a2e5d457a`
- theorem-promotion gate SHA-256: `415191c88737a23e03df41c011b5d4fdb01537f4455985a2f26d0a30968e565d`

Replay:

```bash
cd general_r/workstreams/finite-tail-chat-20261024
python generate_d1_shell_bound.py 13 --output certificates/d1_shell_class_bound_r13.json
python verify_d1_shell_bound.py certificates/d1_shell_class_bound_r13.json
python theorem_promotion_gate.py certificates/d1_shell_class_bound_r13.json --receipt certificates/d1_shell_class_bound_r13_receipt.json
```

The verifier checks the exact arithmetic consequence independently; it does not re-prove the sibling's graph-theoretic shell-incidence lemmas. The result is a useful conditional endpoint bound, not an absolute d1 closure theorem.

## Test matrix

The command-line generator -> verifier -> promotion gate completed successfully for both profiles at:

- r=12, 13, 14, 15;
- r=68.

The 10 scalar-profile runs returned `PASS` from the independent verifier and `PASS_CONDITIONAL_MODULE` from the module gate. The D1 shell-count module additionally passed end-to-end at r=12,13,68 (three more runs). All 13 matrix runs explicitly reported `eg617_r_proved=false`. After the final replay-command metadata update changed the gate hash, both committed r=13 sample certificates were rerun through the final gate and passed; both receipts bind the current gate hash.

Additional exact checks:

- an arithmetic sweep for every r=4,...,100 and both profiles verified complete ordered rows, exact integer bounds, and a disjoint complete partition of admissible degrees into scalar reflection classes;
- r=11 was accepted only as an encoding test and the gate returned `SCHEMA_ONLY / BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE`;
- a certificate with one altered admissibility bit was rejected by the independent verifier;
- a gate run with RC omitted from the machine-readable ledger returned `BLOCKED_UNKNOWN_ASSUMPTION_ID`;
- both module verifiers rejected tampered certificate rows;
- the D1 shell-count certificate at r=12,13,68 returned the same conditional maximum of five classes, with the exact six-class budget gap equal to 2;
- the d=4 boundary is retained by the residual-core ceiling at r=12,13,14 and excluded at r=15; the near-anchor ceiling excludes d=4 for r=12,...,15.

The r=4,...,100 sweep is a finite implementation audit, not a theorem for all r and not a graph-existence proof.

## Independence and scope audit

- The generator and verifier are separate files.
- The verifier does not import the generator and independently rebuilds the exact rows, candidate set, reflection classes, instance hash, and certificate hash. Its reflection-class partition uses a different visited-set algorithm from the producer's remaining-set algorithm.
- The promotion gate invokes the verifier as a subprocess, checks every assumption ID against the ledger, and fails closed for unknown IDs or unsupported r.
- The gate may promote conditional local endpoint lemmas, but never EG617(r), because neither module exhausts all legal graph states or proves a contradiction.
- Graph-level color/vertex symmetry, endpoint d0/d1/d2/d3 closure, high-endpoint kernel closure, LRAT/DRAT, and exact ILP proof checking remain unimplemented or gated by open analytic theorems.


## Round 2 — parameter admission and family audit

### Source/parameter admission

The branch started at the requested HEAD `3d27693d9f9d5bf2586e0f0178228563d96de22b`. The committed matrix has raw SHA-256 `bcdcfa098cee564b136f6fa00405fb34d46a9fa60342b8d4a46f8f77cb8053f7`; the admission verifier file hash is `114f1fd8441ad4e1b91c7ee4cad82e9abf3c21d6c4453502c2e5413ce4d51b35`.

A separate JS audit rebuilt the policy row for every r=4,...,100 and matched all 97 rows of the committed matrix. The independent admission-verifier logic was also exercised in a Python harness with queries for r=11, r=13 residual-core, r=13 near-anchor, r=68 near-anchor, and r=101 D1. It returned the expected blocked/conditional states; a tampered row was rejected. This harness was a separate logic replay, not a direct invocation of the committed CLI entry point.

Parameter conclusions:
- r=4,...,11: `BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE`;
- r=12,...,16: RC-dependent scalar module is conditional; broad ANCHOR_K8 remains open;
- r=17,...,67: the residual/core contract follows if a legal residual is extracted, but global extraction remains open;
- r>=68: broad ANCHOR_K8 source applies, but RC/front extraction and terminal closure remain open;
- the exact three-anchor K8 theorem is applicable for r>=12 only under its exact three-anchor hypothesis, and is not substituted for broad ANCHOR_K8.

### Parameterized exact-arithmetic audit

An independent Python arithmetic harness rechecked 5,073 endpoint-domain d rows for r=12,...,100 and 623 D1 class-count rows for the same parameter range. It confirmed:
- baseline q-cap medium candidates are d=4 and r-3 for r=12,13,14;
- no medium candidates remain for r>=15 under q<=3r+2;
- under q<=3r-1, d=4 and its reflection are excluded for all r>=12;
- for every tested r, six D1 classes require 6r incidences versus cap 6r-2 (gap exactly 2), so N<=5 under the cited conditional incidence lemmas.

### Graph symmetry fixture

The committed toy fixture exhausts all 8 colorings of K3 with two colors and has 3 orbit representatives under the role-preserving shell swap and color swap. A separate Python reconstruction verified all 8 explicit mappings and matched the committed digests:

- pre-quotient state-set SHA-256: `1c10fd6173e748ff06f912ebae87d5bf4c6c2002a88ad54f8671a53a9fc0d18c`;
- post-quotient orbit-set SHA-256: `344254a1cfc131a437ced79dff954c6e79ca02c7a8ca7ff97556d7c770b752cf`.

The committed `GRAPH_SYMMETRY_VERIFIER.py` CLI and unified certificate wrapper have **not** yet been executed directly in a repository runtime. The interface and test vectors are committed; do not claim the direct CLI replay passed.

### Promotion verdict

- Admission matrix: **constructed; 97/97 explicit rows independently matched**.
- Parametric certificate-family interface: **constructed; reuses existing generators/verifiers**.
- Graph symmetry witness interface: **constructed; toy fixture independently cross-checked, direct CLI replay pending**.
- New EG617(r) theorem: **NONE**.
- `ASYMPTOTIC_R0`: **NOT AVAILABLE**.
- RC/front extraction and remaining endpoint/design terminal closure: **OPEN**.
