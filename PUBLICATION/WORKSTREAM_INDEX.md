# EG617(r=12) — branch and workstream index

Inventory captured from GitHub on 2026-10-31. The repository had **44 remote branches** at the time of inventory, including the publication-preparation branch. All branches are preserved; no historical branch was renamed or deleted.

## Canonical fixed-r12 publication path

| Role | Branch / commit | What to read |
|---|---|---|
| Integrated proof | [`workstream/r12-astra-global-root-integration-20261031`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/tree/workstream/r12-astra-global-root-integration-20261031), commit [`c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2) | [FINAL_GLOBAL_PROOF.md](https://github.com/Icarus-K-Laplace/EG617-r12-proof/blob/c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2/r12_master/workstreams/astra-global-root-integration-chat-20261031/FINAL_GLOBAL_PROOF.md), proof DAG, theorem ledger, frozen dependencies |
| Independent certification | [`workstream/r12-final-certification-chat-20261031`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/tree/workstream/r12-final-certification-chat-20261031), commit [`09a88cc4fe1e2cf1f3a87475d6484f681910b23e`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/09a88cc4fe1e2cf1f3a87475d6484f681910b23e) | [FINAL_CERTIFICATION_REPORT.md](https://github.com/Icarus-K-Laplace/EG617-r12-proof/blob/09a88cc4fe1e2cf1f3a87475d6484f681910b23e/r12_master/workstreams/r12-final-certification-chat-20261031/FINAL_CERTIFICATION_REPORT.md), 58-row obligation matrix, replay code/results |
| Certification review | [PR #1](https://github.com/Icarus-K-Laplace/EG617-r12-proof/pull/1) | Open draft PR; not merged; AI-assisted informal audit, not human peer review |
| Q30 adversarial review | [`workstream/r12-final-two-bottleneck-review-20261031`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/tree/workstream/r12-final-two-bottleneck-review-20261031), commit [`a0f922ad09af99575bae581864b673aa4d41f00d`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/a0f922ad09af99575bae581864b673aa4d41f00d) | [Q30_INDEPENDENT_REFEREE_REPORT.md](https://github.com/Icarus-K-Laplace/EG617-r12-proof/blob/a0f922ad09af99575bae581864b673aa4d41f00d/r12_master/workstreams/r12-final-two-bottleneck-review-chat-20261031/Q30_INDEPENDENT_REFEREE_REPORT.md) |
| 286-edge equality | [`workstream/r12-astra-286-edge-parent-equality-20261030`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/tree/workstream/r12-astra-286-edge-parent-equality-20261030), commit [`c3d07b2ca5912b1b0c1c6998303c19c3c2911340`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/c3d07b2ca5912b1b0c1c6998303c19c3c2911340) | `286_EDGE_EQUALITY_CLASSIFICATION.md`, verifier and incidence audit |
| COVER theorem | [`workstream/r12-astra-cover-independent-closure-20261031`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/tree/workstream/r12-astra-cover-independent-closure-20261031), commit [`531e41c79e08dd2bb3892ca9ba8a491a56678565`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/531e41c79e08dd2bb3892ca9ba8a491a56678565) | `COVER_THEOREM.md`, case matrix, dependency audit and verifier |
| 47-point low-edge theorem | [`workstream/r12-astra-low-edge-universal-augmentation-20261030`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/tree/workstream/r12-astra-low-edge-universal-augmentation-20261030), commit [`783c72090205d4bd1a6eefce1dec09e15f78e319`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/783c72090205d4bd1a6eefce1dec09e15f78e319) | Direct proof, common-neighborhood capacity, minimum-degree gate |
| Exact Q32 / 285-edge source | [`workstream/r12-astra-q32-v47-universal-attack-20261030`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/tree/workstream/r12-astra-q32-v47-universal-attack-20261030), commit [`f56cc9eba646e71d63c4b55f468a2340bcdd64c2`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/f56cc9eba646e71d63c4b55f468a2340bcdd64c2) | Separate Q32 theorem/audit; do not conflate with Q33 |
| Original global root | [`workstream/r12-twochat-e408-global-20261026`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/tree/workstream/r12-twochat-e408-global-20261026), commit [`b0459807acd4b7e386148056ddf77d7998918893`](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/b0459807acd4b7e386148056ddf77d7998918893) | Historical root snapshot; its old OPEN ledger is superseded for the fixed-r12 proof by the integrated proof above |

## Complete remote branch snapshot

The following is an inventory of names and immutable HEADs, not a claim that every historical workstream is part of the final proof dependency graph.

| Branch | HEAD | Category | Reading guidance |
|---|---|---|---|
| `main` | `278639de8572ffab12fe859d36f776fbb88fc4f0` | Legacy default branch | Historical base; publication docs are being brought into sync. |
| `workstream/astra-aext-near-anchor-20261024` | `ad6e4ebe152e3918b9c5fe67f461ba402b1445d8` | Near-anchor analysis | Supporting/historical local analysis. |
| `workstream/astra-dlow-terminal-20261024` | `c71b29d3c5b661cdcf00404e545933893c44598b` | Low-degree terminal | Supporting/historical terminal analysis. |
| `workstream/general-r-adversarial-audit-20261024` | `7ea44fc180fcaef20283f788a2234e2a14aa78e2` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-architecture-20261024` | `a922c4d7646eb8d0087bde8547562c8aace02ee2` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-asymptotic-20261024` | `fa6a5f2b8b5d2a0fe821d50a4421884a69dc5366` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-design-terminal-20261024` | `c3f6aa87344008fa1955e9e48075735c5f4c46da` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-extremal-stability-20261024` | `e3e8849a1b0ea618e950f56554d2a61bb1853071` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-finite-geometry-20261024` | `8d8ed298530ce49409aca4079c8489bc1ae01e0a` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-finite-tail-20261024` | `f8f1221e53aa132fc712c15661a891300eda08b2` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-front-recurrence-20261024` | `f5fd2b931049a0426cdbfadeeee6a4be740a4290` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-induction-compression-20261024` | `658247cd7fbcab7057a0931e1f2b91c8c215b008` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-multicolor-global-20261024` | `41f1efdf52755c67adb16d01dd2c5b103884b155` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-repivot-termination-20261024` | `ac492a8465aa236056f2be2dd86e946a8f0b7429` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-residual-core-extraction-20261024` | `beea9470669fc473f0bff17fd850ef49753d118d` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/general-r-three-anchor-20261024` | `5d9bf4dda3ae917e2edeacf0cc873ca710a32af2` | General-r research | Separate general-parameter programme; not needed for the fixed r=12 proof. |
| `workstream/r12-astra-286-edge-parent-equality-20261030` | `c3d07b2ca5912b1b0c1c6998303c19c3c2911340` | 286-edge equality | 47-point equality classification source used by integration. |
| `workstream/r12-astra-cover-independent-closure-20261031` | `531e41c79e08dd2bb3892ca9ba8a491a56678565` | COVER theorem | Independent COVER source and finite classification assets used by integration. |
| `workstream/r12-astra-global-root-integration-20261031` | `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2` | Integrated fixed-r12 proof | Frozen integrated proof snapshot; final K145 theorem stated PROVED. |
| `workstream/r12-astra-independent-structural-attack-20261029` | `99f60126fdd9c72c450475e7fd75c6c499d69df7` | Structural attack | Supporting/historical structural analysis. |
| `workstream/r12-astra-low-edge-universal-augmentation-20261030` | `783c72090205d4bd1a6eefce1dec09e15f78e319` | 47-point low-edge theorem | Universal low-edge obstruction and safe augmentation source. |
| `workstream/r12-astra-q32-v47-universal-attack-20261030` | `f56cc9eba646e71d63c4b55f468a2340bcdd64c2` | Q32 / 285-edge theorem | Independent exact 285-edge source/audit; separate from Q33. |
| `workstream/r12-e407-q32-terminal-20261025` | `79c1086efca893fad8933210a92a432457232410` | Q32 support / 285-edge | Historical Q32-specific workstream; separate theorem and not to be conflated with Q33. |
| `workstream/r12-e407-v12-root-promotion-20261030` | `0b48d1f768e3d3c1d3137e0c3ec12f1ff618bb91` | E407 terminal | Historical E407 terminal workstream; retain as provenance. |
| `workstream/r12-e408-q32-excess6-20261025` | `a0ba6db26c7e8b00a4217dcbcbf298895dff93ce` | Q32 support / 285-edge | Historical Q32-specific workstream; separate theorem and not to be conflated with Q33. |
| `workstream/r12-e408-q33-global-compat-20261025` | `0cb2ff3968f005c9cb255958df7c02b220678701` | Q33 support / 284-edge | Historical Q33-specific workstream; separate theorem and not to be conflated with Q32. |
| `workstream/r12-emergency-sprint-20261024` | `f4c3b06891d29238d4f9cca2588f442004b6dc97` | Emergency sprint | Historical coordination/sprint workstream. |
| `workstream/r12-emergency-sprint-chat-20261025` | `5258c5fe17af3bf17eb7a2bfb08315c9be9116cd` | Emergency sprint | Historical coordination/sprint workstream. |
| `workstream/r12-final-certification-chat-20261031` | `09a88cc4fe1e2cf1f3a87475d6484f681910b23e` | Independent certification | AI-assisted informal audit; PASS for pinned c5 snapshot; PR #1 remains draft. |
| `workstream/r12-final-two-bottleneck-review-20261031` | `a0f922ad09af99575bae581864b673aa4d41f00d` | Adversarial review | Independent Q30 report; Q30 PROVED under the exact E408 parent contract. |
| `workstream/r12-master-closure-20261024` | `e46da35aedce7bbaaf11756b50192bd157956239` | Master closure | Historical integration/closure workstream. |
| `workstream/r12-publication-release-20261031` | `278639de8572ffab12fe859d36f776fbb88fc4f0` | Publication / repository organization | This branch: public-facing status, workstream index and release documentation. |
| `workstream/r12-q32-caseII-v44-final-20261028` | `9afd7c1a59056052974f9dc78933010d10e88bba` | Q32 support / 285-edge | Historical Q32-specific workstream; separate theorem and not to be conflated with Q33. |
| `workstream/r12-q32-highsupport-root-20261028` | `1de8a37556ba98ccbb8651f39a5192629453f0f1` | Q32 support / 285-edge | Historical Q32-specific workstream; separate theorem and not to be conflated with Q33. |
| `workstream/r12-q32-v47-m10-residual-final-20261030` | `b6bfa0d2c85e22b5d480fbe6d2a5e2727192cd4f` | Q32 support / 285-edge | Historical Q32-specific workstream; separate theorem and not to be conflated with Q33. |
| `workstream/r12-q32-v47-m89-final-20261030` | `f78ac022d70647e9c87580bbc595c2306cfda26c` | Q32 support / 285-edge | Historical Q32-specific workstream; separate theorem and not to be conflated with Q33. |
| `workstream/r12-q33-support-promotion-20261030` | `ca088347124f4ea7706a63129d7ed63d4e4090d7` | Q33 support / 284-edge | Historical Q33-specific workstream; separate theorem and not to be conflated with Q32. |
| `workstream/r12-q33-v47-excess4-universal-core-attack-20261030` | `bdc2046ea08f12455a37fd412fe2e19514118ada` | Q33 support / 284-edge | Historical Q33-specific workstream; separate theorem and not to be conflated with Q32. |
| `workstream/r12-twochat-e407-closure-20261026` | `0192807d1f3b2193aa65c25b9f671b36821aaded` | E407 closure | Historical terminal workstream; retain as provenance. |
| `workstream/r12-twochat-e408-global-20261026` | `b0459807acd4b7e386148056ddf77d7998918893` | Historical global root | Earlier canonical root; superseded for the fixed-r12 proof by the pinned integration snapshot. |
| `workstream/r12-ultimate-closure-20261024` | `1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40` | Master closure | Historical integration/closure workstream. |
| `workstream/r12-unified-witness-capacity-20261025` | `faa8183c150dd78b000d0957fa8a63cebd52e146` | Witness / capacity | Historical witness-packing and capacity workstream. |
| `workstream/r12-witness-packing-chat-20261025` | `f5d3daa07403877ede9885e1bd5c2f46b16d81da` | Witness / capacity | Historical witness-packing and capacity workstream. |
| `workstream/r12-zero-excess-witness-20261025` | `c8c4833c7830370a703d228ee23e3b88484d6baa` | Witness / capacity | Historical witness-packing and capacity workstream. |

## Naming and archival policy

1. Branch names are immutable historical identifiers. Do not rename or delete them merely to make the repository look tidy.
2. The **fixed-r12 proof path** is the integrated proof commit plus its independent certification commit, with exact provenance recorded above.
3. Q32 (285-edge) and Q33 (284-edge) are distinct mathematical contracts. Their workstreams remain separate.
4. E407/E408, support-promotion, witness-packing and emergency-sprint branches are retained as research provenance. Their historical local labels do not override the final proof DAG.
5. The `general-r-*` branches concern the broader parameterized programme. They are not evidence that the general conjecture has been solved.
6. Branch presence does not mean a branch has been merged into `main`; inspect the commit and PR state.
7. No branch or file has been deleted by this publication-preparation work.

## Current publication branch

This index is being prepared on `workstream/r12-publication-release-20261031`. The repository visibility remains unchanged. The publication branch is intended to be reviewed through a documentation-only PR to `main`.
