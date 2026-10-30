# Dependency receipt

## Branches inspected

| Branch | HEAD | Use |
|---|---|---|
| `workstream/r12-q32-highsupport-root-20261028` | `1de8a37556ba98ccbb8651f39a5192629453f0f1` | Mathematical base and source-labelled full-support model |
| `workstream/r12-q32-caseII-v44-final-20261028` | `9afd7c1a59056052974f9dc78933010d10e88bba` | Sibling v44 closure/dependency boundary only; not reworked |
| `workstream/r12-twochat-e408-global-20261026` | `b0459807acd4b7e386148056ddf77d7998918893` | latest root DAG, core 285 terminal, and root promotion interface |
| `main` | `278639de8572ffab12fe859d36f776fbb88fc4f0` | Staleness comparison only |

The new branch `workstream/r12-q32-v47-m89-final-20261030` was created from the high-support HEAD, not from the stale main branch.

## Source files and inspected blob SHAs

The latest root global branch HEAD is `b0459807acd4b7e386148056ddf77d7998918893` (replaces the older root SHA in the first receipt). The read-only root canonical/dependency summaries still contain `L_9=6`; the Case-II canonical/dependency audit explicitly supersedes it with `L_9=7` from the 130-edge degree-four and 131-edge degree-three theorems. The isolated model uses 7.

| File | Blob SHA |
|---|---|
| `q32-highsupport-root-chat-20261028/ROOT_DEPENDENCY_DAG.md` | `37a1dd404a179fe8a97fea1ce572dccf48fef36a` |
| `q32-highsupport-root-chat-20261028/CANONICAL_STATE.md` | `afa72318cb0626a0e5fa2ca526eba4bd5984f506` |
| `q32-highsupport-root-chat-20261028/Q32_FULLSUPPORT_VERTEX_LABELLED_CSP.md` | `25714d9f9af244aa1af7eb4392cdea5e82b8220c` |
| `q32-highsupport-root-chat-20261028/q32_fullsupport_vertex_labelled_csp.py` | `aba51326e4585594e7d87bc2bb0ff6b2a3d7730d` |
| `q32-highsupport-root-chat-20261028/verify_q32_fullsupport_candidate.py` | `bc29a5fe2b4031ccf6aa3e9eb262ca7318c40343` |
| `q32-highsupport-root-chat-20261028/V47_PIVOT_NEIGHBORHOOD_PACKING.md` | `10fb644df30419304482dffed89a577be8fc1710` |
| `q32-highsupport-root-chat-20261028/V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md` | `2e36e057e934b86d5f5e2baa25f65bac7b3bfcf5` |
| `q32-highsupport-root-chat-20261028/V47_T0_POINTWISE_COLOR_SATURATION.md` | `fdf1e9b00381bdbfd38011185d7170f4577c4bd2` |
| `q32-highsupport-root-chat-20261028/V47_Z01_SHARED_P_FACTOR_PACKING.md` | `f622f8870a6e533433d3c377041ac64cb2436483` |
| `q32-highsupport-root-chat-20261028/HIGH_SUPPORT_NEAR_TURAN.md` | `5dc6e156939b73e909b707a6cb41e540c3d8d657` |
| `twochat-e408-global-20261026/Q32_CORE285_TERMINAL.md` | `42f3644191bc5e3fe99ae6bbc6e25a8c7b6dd6f4` |
| `twochat-e408-global-20261026/ROOT_DEPENDENCY_DAG.md` | `09b4d5505d8b80839f2868aca1d427263158eab7` |
| `twochat-e408-global-20261026/CANONICAL_STATE.md` | `21bb902d9972557d1d3ece5208a74ac33b1b378d` |
| `twochat-e408-global-20261026/DEPENDENCY_AUDIT.md` | `725b6839c954a09ea46bee84e5ad4d2212c41a23` |
| `twochat-e408-global-20261026/Q32_131_MINDEG3_V46_M9_CLOSURE.md` | `c88aa8730669ca319bf9c82f53648c79d481747e` |
| `twochat-e408-global-20261026/Q32_U_COLOR_RESERVE.md` | `bb7ed1c7e11db73f9456e4ee3892715294182beb` |
| `q32-caseII-v44-final-chat-20261028/Q32_130_MINDEG3.md` | `6ab6a3fb890f31cf8b18171a240ce548957a629a` |
| `q32-caseII-v44-final-chat-20261028/CANONICAL_STATE.md` | `98eac1c7bba8f7e9dd921104b96ffd03dccc5335` |
| `q32-caseII-v44-final-chat-20261028/DEPENDENCY_AUDIT.md` | `2adcded87ae5918eac73d29b9b443e2664887313` |

All blob SHAs in this table were fetched from the stated branch refs during this workstream's audit.


## Local workstream artifact blobs at audit checkpoint

| Local artifact | Blob SHA |
|---|---|
| `q32_fullsupport_m89_solver.py` | `6170c347dc6b6ff0ab356c742cb3535922448151` |
| `verify_q32_fullsupport_candidate.py` | `ad47039f4c5f85880308e532a7599ef675abd4f8` |
| `verify_m89_pivot_matching.py` | `59a2c4031785303a0efe37090e37118b2d35dcf0` |
| `V47_NEAR_TURAN_SOURCE_NORMAL_FORM.md` | `8e4f611ded8e0eeedfff445c270311ad204d054c` |
| `V47_SOURCE_NEAR_TURAN_SPECIAL_GADGET_LOCALIZATION.md` | `4a93e1d79cbf3142763192cfcf2a400ef07088a6` |

The 130-edge minimum-degree-four theorem is cited by the read-only Case-II canonical/dependency audit and is the basis for the m=9 floor sum 4+3=7. Its complete proof artifact was not located among the inspected files in this branch snapshot; this workstream therefore treats that result as an imported dependency, not as an independently re-proved theorem. The directly inspected 130-edge degree-three proof and 131-edge degree-three proof are weaker/parallel source records and do not replace the 130-edge degree-four dependency.


The 69/70 near-Turan partition CSP and independent verifier were subsequently extended from exact colors to all eleven non-target colors. This is valid because alpha(C[H])<=12 and omega(C[H])<=4 hold for every non-target color; the exact-source witness alignment check remains restricted to exact colors.

The latest all-color orthogonality checkpoint also updates the local solver/verifier blobs above; the pivot matching verifier blob remains unchanged.


## 2026-10-30 low-layer source-localization checkpoint

| Local artifact | Blob SHA |
|---|---|
| `q32_fullsupport_m89_solver.py` | `6170c347dc6b6ff0ab356c742cb3535922448151` |
| `verify_q32_fullsupport_candidate.py` | `ad47039f4c5f85880308e532a7599ef675abd4f8` |
| `V47_SOURCE_NEAR_TURAN_SPECIAL_GADGET_LOCALIZATION.md` | `4a93e1d79cbf3142763192cfcf2a400ef07088a6` |
| `MATH_PROOF.md` | `e1d0956d096134ccdabaaa72ee92a2e6429f7ec2` |
| `RUN_LOG.md` | `20f78de0efc93788f3da677db584fd93d46b8b0b` |
| `CANONICAL_STATE.md` | `ebc8f0ef088afbbb0d55794076e92189f653536a` |

The new source-localization constraints are conditional on the 69/70 layer and alpha(H)<=4 / alpha(C)<=12. The solver and verifier blobs above include them. The 253-edge matching-skeleton theorem is analytic and is not yet encoded with explicit matching-choice variables. No full CSP run or SAT/UNSAT result exists.

| `OPEN_CASES.md` | `9a5835555ad233192bc6fea6cfd1bfd651f97f15` |

The latest mathematical append is MATH_PROOF.md §9.6, giving the exact leaf-core identity (e(F[W])=q+t-4). The matching skeleton remains analytic only; the solver was not executed.


## 2026-10-30 final Type-I partition obstruction checkpoint

Parent dependencies rechecked read-only:
- high-support source interface branch HEAD: `1de8a37556ba98ccbb8651f39a5192629453f0f1`;
- global E408/Q32 root branch HEAD: `b0459807acd4b7e386148056ddf77d7998918893`;
- sibling v44 Case-II branch HEAD: `9afd7c1a59056052974f9dc78933010d10e88bba`.

The final theorem depends on the registered Type-I exact-129 factorization in the high-support source interface and the Q32 H-core contract in the global root terminal. It does not modify or overwrite any sibling branch. The proof establishes that every exact color induces one of three forbidden independent-part partitions of H, so m=8 and m=9 full-support Q32 are analytically impossible. This is a conditional analytic proof promotion candidate; no full SMT execution, SAT result, UNSAT result, or solver proof log is claimed.

| Local artifact | Blob SHA | Size |
|---|---|---|
| `V47_TYPEI_PARTITION_OBSTRUCTION.md` | `4ff2d881748a917d25902dba5e21d41ef9ba9ef5` | 122 lines |
| `q32_fullsupport_m89_solver.py` | `1dae5a9acb1f20d6719c6a389fab3e7145560d50` | 658 lines |
| `verify_q32_fullsupport_candidate.py` | `1313fe8d559a214f7b187dd7438942c48be931dc` | 1060 lines |
| `MATH_PROOF.md` | `b2435e5303f8b427f4c83e0fba344813083ef405` | 374 lines |
| `CANONICAL_STATE.md` | `851bae8ac181d10599d18ade4fdf4d6d93d2d3e7` | 63 lines |
| `OPEN_CASES.md` | `1e638e246900296d80932a016bc7221160a9e58a` | 92 lines |
| `FULL_SUPPORT_CSP_SPEC.md` | `a531d2de85775d1bbcd7d7e82091c250750bed6d` | 127 lines |
| `MODEL_VALIDATION.md` | `0b3baaef9c1f2e7b59256b73e16aef40a5547fff` | 123 lines |
| `RUN_LOG.md` | `2b02eb56ec8532e9345764b0c179ab50778926d3` | 91 lines |

The independent verifier now reconstructs the source partition for each exact color and replays Hall matchings/tight-part obstruction using augmenting paths. Its synthetic self-test covers all three occupancy shapes. The solver is explicitly archival by default; legacy SMT execution requires the opt-in `--legacy-smt` flag.
