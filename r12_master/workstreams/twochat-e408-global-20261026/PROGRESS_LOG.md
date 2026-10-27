# Progress log — E408 global incidence / witness capacity

## 2026-10-26 — isolated branch and intake audit

- Created dedicated branch workstream/r12-twochat-e408-global-20261026 from main HEAD 3f42fcce5761ca2372140618adda56f95fcbe253.
- Checked actual HEADs of Q33, Q32, unified witness-capacity, witness packing, zero-excess witness, and ultimate-closure workstreams. All sibling branches remain read-only.
- Reconciled the stale Q33 profile ledger: the source Q33 branch already has a separate double-star theorem excluding (6,2,1^5), although its canonical summary still lists four profiles as open.
- Independently replayed the (6,2,1^5) gadget verifier: 452 Case-A checks plus 570,942 Case-B/C checks, total 571,394, zero failures.

## 2026-10-26 — new Q33 (7,1^6) closure

- Added verify_q33_p49_r7_double_star.py and independently executed its finite predicates in a separate Python runtime.
- Four gadget normal forms: K5 counts 4,3,3,4; universal-D sizes 2,3,3,2.
- Checked 48 low-pair/D tests and 27,380 high-pair alignment tests, zero failures.
- Proved the graph-level row split n=0, n=1, n>=2. The n>=2 branch uses the exact gadget alignment and seven-row double-star. The n=1 branch either gives the same double-star or forces a repeated full component, which yields five external C-edges into a constructed C-colored K12.
- Added Q33_P49_R7_DOUBLE_STAR_EXCLUSION.md. Status: PROVED_CONDITIONAL under the exact-129 factor, row-budget, row-blocker, and gadget-normal-form contracts.

## 2026-10-26 — Q33 frontier reconciliation and global ledger

- Updated Q33_P49_REMAINING_PROFILES.md: only the all-component-edge-present branches of (4,4,1^5) and (4,3,2,1^4) remain open on the P_C=49 screen.
- Added CONTRACT_FIREWALL.md, DEPENDENCY_AUDIT.md, Q33_SEVEN_BLOCK_GLOBAL_CONTRADICTION.md, and Q32_CORE285_TERMINAL.md.
- Audited the historical inference that ten disjoint C-colored K12s imply P_C<=42. This bound is not established by star capacity alone and is not used in this branch.
- Exact accounting for an all-component-edge-present exact-129 color: ten K12s account for 660 of 870 C-edges; the residual edge ledger is 29 internal gadget edges, 90 outer-to-R edges outside own components, and 91 outer-block edges outside the ten diagonal matchings. The counts are consistent and do not alone imply a contradiction.

## Current state

- Q33 P_C=49: profiles (6,2,1^5) and (7,1^6) excluded conditionally; two all-component-edge-present profiles remain OPEN.
- Q33 global witness/core/outer-incidence contradiction: OPEN.
- Q32 285-edge support floor |U|>=44 is a retained theorem; v=44 triple-pair terminal remains OPEN.
- Original EG617(r=12): OPEN / NOT_CERTIFIED.

## Commit trail

- 6e896507bee2d91701b173b52678788f3dfcc826 — exact gadget verifier for (7,1^6).
- d462fe568577e4ab9204ef155da18111000312f0 — (7,1^6) double-star theorem.
- d5285026a56a15ad2a78e7625248d39c87d03b84 — Q33 profile reconciliation.
- 0db5ca4bcdcff339165f6e6bbfc3151ed86038fa — canonical state.
- 67966feb11ce76c970e6e1377f59cf0e1b353554 — contract firewall.
- 67feab906085980e9f2d3e3aadc808540e43cda5 — dependency audit.
- 309b4194219e79600604b18b43da8a42d166edea — Q33 global ledger.
- 880a753684fa50f321ed3eb24e358cff64aa2ea1 — Q32 terminal.


## 2026-10-27 — Q33 exact-color count exclusion

- Derived a cross-layer capacity theorem using the 31-point support \(U\), its 16-point complement \(W\), the 56 selected witnesses, and the full ten-component witness family for each exact-129 color.
- Proved \(h\le4\), where \(h\) counts selected gadget witnesses, from \(e(\overline{H[W]})\le96\) and the unselected component K4s' edge-disjoint W-pairs.
- Excluded \(m=10\): the two exact colors outside the selected eight require at least 48 total incidences in \(U\), but their 20 component four-sets have pair-cost at most \(\delta+4h\le33\), allowing at most 46 incidences. The four-edge overlap cap per selected gadget witness follows from the triangle-free complement of its color graph on four vertices.
- Corollary: if \(m=9\), at least one selected witness must be a gadget witness; always \(h\le4\).
- Independent arithmetic replay: 20 variables/budget 33 -> max 46; 10 variables/budget 17 -> max 23; pointwise capacity inequality passes for \(k=0,\ldots,4\).
- New proof commit: 50e4f7c2299f1cb21a410779a27fdd9fd7795438. New verifier commit: 62462f04e76b33aa921249caa38d604fd6e6f95c.

## Current state after this advance

- Q33 exact-129 color count: \(m\in\{8,9\}\); \(m=10\) excluded conditionally.
- Selected gadget witnesses: \(h\le4\); if \(m=9\), \(h\ge1\).
- Q33 \(P_C=49\): \((6,2,1^5)\), \((7,1^6)\) conditionally excluded; \((4,4,1^5)\) and \((4,3,2,1^4)\) remain open in all-component-edge-present branches.
- Q33 global witness/core/outer-incidence contradiction: OPEN.
- Q32 285-edge support floor \(|U|\ge44\) retained; \(v=44\) triple-pair terminal OPEN.
- Original EG617(r=12): OPEN / NOT_CERTIFIED.


## 2026-10-27 — sharpened m=9 residual contract and audit repair

- Derived the lower pair-cost 18 needed for one unselected exact color's ten component sets to cover at least 24 points of the 31-point support. Hence \(\delta\ge18-4h\): \(\delta\ge14,10,6,5\) for \(h=1,2,3,4\).
- Proved the \(h=4\) endpoint is rigid: \(\overline{H[W]}=K_{4,4,4,4}\), with the selected component witnesses' W-parts giving an edge decomposition into four \(K_4\)'s and 24 triangles. This is a minimum residual contract, not a contradiction.
- Independently replayed arithmetic DP: minimum cost for 10 values \(k_i\in\{0,\ldots,4\}\) with sum at least 24 is 18; the previous maxima 46 and 23 remain verified.
- Refined proof commit: 1edb9efe781aa722c0ae2813f3efcca3d906273f. Refined verifier commit: 448fc7e717273d4f4cc8b9671897c2de37d2a490.
- Audited and corrected the R7 proof's pigeonhole wording so it correctly identifies a vertex adjacent to two selected rows, rather than saying it is “omitted” by them. Commit: f0743b0c5c65d883f9e533b2c5cd83c9987c3b77.



## 2026-10-27 — close the h=4 equality endpoint

- The h=4 lower bound saturates \(e(\overline{H[W]})\le96\), forcing \(H[W]=4K_4\) and \(\overline{H[W]}=K_{4,4,4,4}\).
- Equality forces the selected component witnesses' W-parts to edge-partition this complete four-partite graph into four \(K_4\)'s and 24 triangles.
- Vertex degree parity gives each vertex an even number of appearances among the four \(K_4\)'s. Each part therefore has two vertices of K4-incidence 2 and two of incidence 0; incidence 4 is impossible because it forces incidence 1 in other parts.
- The four K4s would yield four pairwise-orthogonal balanced binary columns, i.e. OA(4,4,2,2). Exhaustive verification over the six balanced binary columns finds maximum pairwise-orthogonal family size 3, contradiction.
- Result: \(h\le3\) globally. If \(m=9\), then \(h\in\{1,2,3\}\) and \(\delta\ge14,10,6\) respectively.
- Proof commit: 99d85042c32a87a27d56c321c025ec55a3f978f5. Independent OA verifier commit: 91050534c8c59106b119474b7e3a45f37c6d6f51.



## Latest canonical frontier — 2026-10-27

- Q33 exact-129 color count: \(m\in\{8,9\}\); \(m=10\) is PROVED_CONDITIONAL impossible.
- Selected gadget-witness count: \(h\le3\); if \(m=9\), \(h\in\{1,2,3\}\) and \(\delta\ge14,10,6\) respectively.
- \(h=4\) is closed by an orthogonal-array obstruction, not left as an open terminal.
- Q33 \(P_C=49\): two profiles conditionally excluded; the all-component-edge-present branches of \((4,4,1^5)\) and \((4,3,2,1^4)\) remain OPEN.
- Q33 global core/witness/outer incidence contradiction remains OPEN.
- Q32 285-edge \(v=44\) triple-pair terminal remains OPEN.
- Original EG617(r=12): OPEN / NOT_CERTIFIED.



## 2026-10-27 — joint U/W capacity refinement for m=9

- Added the complementary pair-cost \(c_W=\sum_\ell \binom{4-k_\ell}{2}\), bounded by the unused edge capacity of \(\overline{H[W]}\). This couples the 31-point support budget and the 16-point complement, rather than using the U-cost alone.
- Proved the m=9, h=3 case has \(\delta\ge11\), strengthening the previous \(\delta\ge6\). If \(\delta=11\), then \(\epsilon_U=4\) and the ninth color's ten components have exactly four \(k=2\) and six \(k=3\) sets; their four W-edges exhaust the remaining W-edge capacity.
- For h=2, \(\delta\ge10\); equality forces six \(k=2\) and four \(k=3\) sets, and \(\epsilon_U\ge1\). If \(\epsilon_U=1\), the W-edge capacity is exactly saturated.
- Independent finite enumeration over all 1001 count profiles of ten \(k_i\in\{0,1,2,3,4\}\) verified: cost \(\le18\), sum \(\ge24\) forces profile \((2^6,3^4)\); the h=3, \(\delta\le10\) joint U/W budgets have no profile; h=3, \(\delta=11\) forces \((2^4,3^6)\).
- Updated proof commit: 3d05879da362a9ce68c4836bc484d7e78b872d36. Updated arithmetic verifier: 2625ad01209eb3744edae2739b78af78325dfac9.

