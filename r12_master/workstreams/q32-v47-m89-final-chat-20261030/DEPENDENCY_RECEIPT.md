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
| `q32_fullsupport_m89_solver.py` | `272ed95ea147514c5cbacd7e2783721e8e55e736` |
| `verify_q32_fullsupport_candidate.py` | `cfd2321b8b191458680dfcb31b01f06274f34ae4` |
| `verify_m89_pivot_matching.py` | `59a2c4031785303a0efe37090e37118b2d35dcf0` |
| `V47_NEAR_TURAN_SOURCE_NORMAL_FORM.md` | `8e4f611ded8e0eeedfff445c270311ad204d054c` |

The 130-edge minimum-degree-four theorem is cited by the read-only Case-II canonical/dependency audit and is the basis for the m=9 floor sum 4+3=7. Its complete proof artifact was not located among the inspected files in this branch snapshot; this workstream therefore treats that result as an imported dependency, not as an independently re-proved theorem. The directly inspected 130-edge degree-three proof and 131-edge degree-three proof are weaker/parallel source records and do not replace the 130-edge degree-four dependency.


The 69/70 near-Turan partition CSP and independent verifier were subsequently extended from exact colors to all eleven non-target colors. This is valid because alpha(C[H])<=12 and omega(C[H])<=4 hold for every non-target color; the exact-source witness alignment check remains restricted to exact colors.

The latest all-color orthogonality checkpoint also updates the local solver/verifier blobs above; the pivot matching verifier blob remains unchanged.
