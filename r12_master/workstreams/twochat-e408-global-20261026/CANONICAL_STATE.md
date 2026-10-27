# E408 global incidence / witness-capacity — canonical state

Updated: 2026-10-27  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Dedicated branch: workstream/r12-twochat-e408-global-20261026  
Allowed write scope: r12_master/workstreams/twochat-e408-global-20261026/

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED. E408 Q33: OPEN / NOT_CERTIFIED. E408 Q32: OPEN / NOT_CERTIFIED.**

The work in this branch is scoped to the user's E408 global incidence/witness-capacity task. It does not promote any result to an unconditional theorem about the original K145 problem.

## Branch isolation and source heads

This branch was created from main HEAD 3f42fcce5761ca2372140618adda56f95fcbe253. The following sibling workstreams were read-only and their actual HEADs were checked before the analysis:

| Workstream | HEAD checked |
|---|---|
| workstream/r12-e408-q33-global-compat-20261025 | 0cb2ff3968f005c9cb255958df7c02b220678701 |
| workstream/r12-e408-q32-excess6-20261025 | a0ba6db26c7e8b00a4217dcbcbf298895dff93ce |
| workstream/r12-unified-witness-capacity-20261025 | faa8183c150dd78b000d0957fa8a63cebd52e146 |
| workstream/r12-witness-packing-chat-20261025 | f5d3daa07403877ede9885e1bd5c2f46b16d81da |
| workstream/r12-zero-excess-witness-20261025 | c8c4833c7830370a703d228ee23e3b88484d6baa |
| workstream/r12-ultimate-closure-20261024 | 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 |

Only files under this branch's dedicated path are modified by this workstream.

## Contract firewall

### Q33 — 284-edge / excess-four

\[
|V(H)|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \delta(H)\ge12,\quad
\sum_{x\in H}(d_H(x)-12)=4.
\]

The seven-block equality system gives \(P_C+R_C+s_C=62\) for each non-target color \(C\), and \(\sum_Cs_C=3\). For an exact-129 color, \(s_C=0\), so \(P_C+R_C=62\). At \(P_C=49\), \(\sum_i r_i(C)=13\).

### Q32 — 285-edge / excess-six

\[
|V(H)|=47,\quad e(H)=285,\quad \alpha(H)\le4,\quad \delta(H)\ge12,\quad
\sum_{x\in H}(d_H(x)-12)=6.
\]

The Q32 shell contract is \(q=32\), equivalently \(e(M)+G_A=32\). Its exact-129 support-capacity proof is separate and must not import a 284-edge identity or a four-unit excess bound.

## Q33 Phase A — P_C=49 profile status

See Q33_P49_REMAINING_PROFILES.md.

- \((6,2,1^5)\): **PROVED_CONDITIONAL** under the retained row/gadget contracts. The 571,394-configuration verifier was independently replayed with zero failures.
- \((7,1^6)\): **PROVED_CONDITIONAL** in this branch by Q33_P49_R7_DOUBLE_STAR_EXCLUSION.md. Its standalone gadget verifier was independently replayed: 27,380 high-pair tests and 48 low-pair/\(D\) tests, zero failures.
- \((4,4,1^5)\): **OPEN** in the all-component-representative-edges-present branch.
- \((4,3,2,1^4)\): **OPEN** in the all-component-representative-edges-present branch.

For the last two profiles, the registered incidence-sensitive screen excludes a missing component-label edge in the exceptional high-budget block pair. The remaining branch has all ten component-label representatives C-adjacent across all seven blocks, hence ten disjoint C-colored K12s. That fact alone is not a contradiction.

A historical argument that a single external C-edge into a C-colored K12 is impossible is invalid. The valid star-capacity rule is \(d_C(z,Q)\le1\), so a contradiction requires at least two external C-edges from the same outside vertex. This branch only uses double-star contradictions.

## Q33 Phase B — global compatibility

**OPEN.** The exact-129 outer ledger currently yields
\[
M_C\ge15+P_C,\qquad
\sum_{s_C=0}P_C\ge62m-427,\qquad
\sum_{s_C=0}M_C\ge77m-427,
\]
where \(m\in\{8,9\}\) is now the certified remaining range for the number of exact-129 colors. The previous \(m=10\) branch is excluded by Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md, using the 31-point/56-witness support and all ten component four-sets per exact color. If \(m=9\), at least one selected witness must be a gadget witness; in all cases the gadget-witness count \(h\le3\). The remaining \(m\in\{8,9\}\) branches are still OPEN.


### New cross-layer capacity theorem (2026-10-27)

**PROVED_CONDITIONAL:** \(m=10\) is impossible under the Q33 284-edge contract. The proof separates the 56 selected witnesses from the full ten-component witness family, first bounds the selected gadget-witness count by \(h\le4\), then excludes \(h=4\) by an orthogonal-array obstruction. Thus \(h\le3\) globally. The two unselected exact colors in the \(m=10\) branch would need at least 48 incidences in \(U\), while their pair-cost budget \(\sum\binom{k}{2}\le\delta+4h\le33\) allows at most 46. If \(m=9\), at least one selected witness is a gadget witness; the joint \(U/W\) pair-cost audit further forces \(\delta\ge14,10,11\) for \(h=1,2,3\), respectively. If \(h=3,\delta=11\), then \(\epsilon_U=4\) and the ninth color's ten components have four \(k=2\) sets and six \(k=3\) sets. These are exact residual contracts, not a closure. This does not close \(m=8\) or \(m=9\), and does not close Q33.

The next target is to combine:
- the all-component-edge-present branch for the two remaining P49 profiles;
- the 56 labelled independent four-set witnesses in the 284-edge core;
- exact degree excess four and the support/omission ledger;
- cross-color witness linearity and outer-block component labels.

No scalar budget table will be promoted to a graph-level UNSAT result without an explicit realization theorem or complete certificate.

## Q32 Phase C — separate 285-edge terminal

The sibling Q32 workstream proves the strict support floor \(|U|\ge44\) under its own exact-129 contract. At \(|U|=44\), \(W=H\setminus U\) has three vertices and the two triple witnesses per exact color impose a pair-uniqueness terminal. This terminal remains OPEN. No Q33 284-edge theorem is imported into Q32.

## Current commit lineage

- Base main: 3f42fcce5761ca2372140618adda56f95fcbe253
- New R7 gadget verifier: 6e896507bee2d91701b173b52678788f3dfcc826
- R7 double-star theorem: d462fe568577e4ab9204ef155da18111000312f0
- Profile reconciliation: d5285026a56a15ad2a78e7625248d39c87d03b84
- Q33 m=10 exact-color capacity exclusion: 50e4f7c2299f1cb21a410779a27fdd9fd7795438
- Capacity arithmetic verifier: 62462f04e76b33aa921249caa38d604fd6e6f95c
- Refined (m=9) terminal proof: 1edb9efe781aa722c0ae2813f3efcca3d906273f
- Refined capacity verifier: 448fc7e717273d4f4cc8b9671897c2de37d2a490
- Exclude (h=4) by OA obstruction: 99d85042c32a87a27d56c321c025ec55a3f978f5
- OA obstruction verifier: 91050534c8c59106b119474b7e3a45f37c6d6f51
- Joint U/W capacity proof: 904e6709fdea0a4f0db8eaa3ed64bcda1756f49b
- Joint U/W capacity verifier: 2625ad01209eb3744edae2739b78af78325dfac9
- R7 pigeonhole wording audit correction: f0743b0c5c65d883f9e533b2c5cd83c9987c3b77

The latest branch HEAD may advance as additional files are committed. See PROGRESS_LOG.md for the chronological record.
