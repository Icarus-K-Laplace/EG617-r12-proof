# V12 independent replay

Date: 2026-10-30

## Execution

The original package verifier `verify_q32_certificate.py` was executed successfully from a clean copy of the recovered archive. It completed without assertion failure and reported the same per-kernel counts below.

A second verifier, `verify_v12_independent_replay.py`, was written independently. It imports none of `enumerate_q32_kernels.py`, `verify_q32_certificate.py`, or `screen_q32.py`. It uses:
- bit-mask adjacency and a fresh graph representation;
- bounded-composition enumeration of kernel weights;
- independent reconstruction of outside extension types;
- memoized multiplicity-count dynamic programming rather than the source verifier's sorted-sequence enumeration;
- a fresh 13-vertex shell checker for degree, charge, clique floors, repivot legality and `alpha(M)<=10`;
- a fresh screen classifier and five-template outside-row audit.

Reproduction command:

```bash
python -B verify_v12_independent_replay.py --archive T61_H13_V12.zip --output-dir replay_out
```

The original archive remains in Library at `/T61_H13_V12.zip`; copy it to the working directory before running the command. The script uses only the Python standard library.

## Exact counts

| Kernel | Weight vectors | Count states | Necessary shells |
|---|---:|---:|---:|
| I3 | 3,861 | 135 | 135 |
| T3 | 2,145 | 14,370 | 84 |
| K4 | 1,071 | 2,202 | 1,062 |
| W8 | 216 | 222 | 130 |
| W7_overlap | 294 | 167 | 28 |
| W7_separate | 322 | 364 | 328 |
| W6_pair | 342 | 67 | 37 |
| W6_same | 100 | 164 | 0 |
| W6_different | 326 | 266 | 180 |
| **TOTAL** | **8,677** | **17,957** | **1,984** |

## Independent screen replay

| Rule | Count |
|---|---:|
| OPEN | 554 |
| D3_RHO1 | 90 |
| NEAR_K12_CAPACITY | 1,192 |
| K9_PAIR_ROWS | 148 |
| **TOTAL** | **1,984** |

- Screen record mismatches: **0**.
- OPEN survivors mapped to exactly one template: **554/554**.
- Full outside-row template failures: **0**.
- Completed parent graphs: **0**.

The computation certifies the finite necessary-shell enumeration and the screen/mapping checks under the V12 input contract. It does not certify that any OPEN shell is realizable, and it does not prove the retained analytic input theorems or the 29-point parent-support bridge.

## Receipt hashes

- V12 archive SHA-256: `0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36`.
- V12 certificate SHA-256: `cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30`.
- Independent verifier SHA-256: `ac22350dca49f6ba5eb77f9c2cf5169bc226198a996c3a1b4c3699607ae7c26b`.
- Independent replay result SHA-256: `041dbef12b2e8738cb1cbb19c21e5587bcbfa562d527d9dd0d08f4dd773a90d6`.
- Survivor range-map SHA-256: `cab69a57a929e8b9280f9c70a41e75a3317321e064298d436b372fa3ed8fed50`.
