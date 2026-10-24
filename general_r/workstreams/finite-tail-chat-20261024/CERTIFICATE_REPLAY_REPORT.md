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
- theorem-promotion gate SHA-256: `d239d700ecb2f246c750af4b1acb76d6c38b1bdf5c42dadaeeb3adaac23ef7bc`

## Commands

From the repository root:

```bash
cd general_r/workstreams/finite-tail-chat-20261024
python generate_endpoint_domain.py 13 --profile residual-core --output certificates/endpoint_domain_r13_residual_core.json
python verify_endpoint_domain.py certificates/endpoint_domain_r13_residual_core.json
python theorem_promotion_gate.py certificates/endpoint_domain_r13_residual_core.json --receipt certificates/endpoint_domain_r13_residual_core_receipt.json
```

The checked-in receipt binds the source assumption, hashes, verifier, gate, and the explicit non-promotion decision. The certificate's canonical hash is independent of pretty-print whitespace.

## Test matrix

The command-line generator -> verifier -> promotion gate completed successfully for both profiles at:

- r=12, 13, 14, 15;
- r=68.

All 10 runs returned `PASS` from the independent verifier and `PASS_CONDITIONAL_MODULE` from the module gate. Every run explicitly reported `eg617_r_proved=false`.

Additional exact checks:

- an arithmetic sweep for every r=4,...,100 and both profiles verified complete ordered rows, exact integer bounds, and a disjoint complete partition of admissible degrees into scalar reflection classes;
- r=11 was accepted only as an encoding test and the gate returned `SCHEMA_ONLY / BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE`;
- a certificate with one altered admissibility bit was rejected by the independent verifier;
- a gate run with RC omitted from the machine-readable ledger returned `BLOCKED_UNKNOWN_ASSUMPTION_ID`;
- the d=4 boundary is retained by the residual-core ceiling at r=12,13,14 and excluded at r=15; the near-anchor ceiling excludes d=4 for r=12,...,15.

The r=4,...,100 sweep is a finite implementation audit, not a theorem for all r and not a graph-existence proof.

## Independence and scope audit

- The generator and verifier are separate files.
- The verifier does not import the generator and independently rebuilds the exact rows, candidate set, reflection classes, instance hash, and certificate hash.
- The promotion gate invokes the verifier as a subprocess, checks every assumption ID against the ledger, and fails closed for unknown IDs or unsupported r.
- The gate may promote the conditional arithmetic lemma, but never EG617(r), because this module only gives a necessary scalar domain.
- Graph-level color/vertex symmetry, endpoint d0/d1/d2/d3 closure, high-endpoint kernel closure, LRAT/DRAT, and exact ILP proof checking remain unimplemented or gated by open analytic theorems.
