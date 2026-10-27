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
