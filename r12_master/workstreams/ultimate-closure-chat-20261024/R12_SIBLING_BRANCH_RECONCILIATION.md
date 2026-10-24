# Sibling R12 branch reconciliation and claim audit

Date: 2026-10-25  
Workstream: ultimate closure, branch workstream/r12-ultimate-closure-20261024

## 1. Sibling heads read

The following branch heads and newest commits were inspected before this reconciliation:

- [Emergency sprint](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/87a58429070cffbd90991045e0375102fcc4ec0d): corrected exact-129 component count and expanded E407 template coverage.
- [Emergency sprint 2026-10-25](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/5258c5fe17af3bf17eb7a2bfb08315c9be9116cd): added template-specific hub-capacity reduction to the proof DAG.
- [Witness packing](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/38b5dcec008903cdc3487941e7c6fa078637fbc5): labelled witness-packing support lower bound.
- [Zero-excess witness](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/8addc645223d7907982ad2ac5230c37266e23581): robust independent-four theorem and witness-overlap analysis.
- [General-r architecture](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/a922c4d7646eb8d0087bde8547562c8aace02ee2): contextual (k,s)-cap plane, conditional on the cited Second-Turán input.
- [General-r asymptotic](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/fa6a5f2b8b5d2a0fe821d50a4421884a69dc5366): forced-hub interface; the unconditional r_0 remains open.
- [General-r adversarial audit](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/7ea44fc180fcaef20283f788a2234e2a14aa78e2): validates delta(H)≥r−1 as stated, does not promote delta(H)≥r, and rejects naive affine edge-stability uniqueness.
- The r12 master-closure branch's newest head records E335 q30 core-214 equality reduction; no direct E407/E408 terminal closure was imported from that branch.

All sibling workstreams remain separate. No sibling files were overwritten or merged into this branch.

## 2. Compatible results now incorporated

1. The 284-edge core contract has alpha(H)≤4, delta(H)≥12, and total core excess four; E408 Q32 is the separate 285-edge / excess-six case.
2. The zero-excess theorem guarantees an independent four-set after deleting any at most six vertices of H_0 for the 284-edge case. We independently recomputed all ten endpoint gaps; they are 5, 6, 14, 15, 22, 23, 30, 31, 38, 44 in ascending order, all positive.
3. Every pair of regular B-rows in E407 Q32 has a common zero-excess independent-four witness; in E408 Q33 this holds for every pair of undecorated rows.
4. If the two rows' missing-hub sets cover S, that common witness must hit all three hubs.
5. The exact-129 witness-packing support bounds remain valid: at least 49 linear independent-four sets for E407 Q32 and at least 56 for E408 Q33. The support theorem proves |V_*|≥29 and |V_*|≥31, respectively, but neither is a contradiction.
6. The zero-excess sibling's overlap-capacity note explicitly shows that scalar degree/excess bounds do not close the terminal.

## 3. Corrected B-labelled witness counts

The universally valid count is:
- At least seven K5 components avoid S, because |S|=3 and the ten components are disjoint.
- At most one of those components contains pivot p.
- Each remaining component avoiding both S and p must be {b}∪Q with b∈B and Q⊂H, because B is a target clique and alpha(H)≤4.

Hence every exact-129 color has at least six B-labelled components, regardless of beta. It is invalid to infer seven/eight B-labelled components merely because a pair/triple of S vertices is allowed to share a non-target K5; allowed co-location is not forced co-location.

Since at most four core vertices have positive excess, at least two of the six disjoint B-labelled Q sets per exact-129 color are zero-excess. This gives global floors 14 in E407 and 16 in E408 Q33.

If a full row exists, at most three B-labelled Q sets per color can fail hub-completeness, because every such Q must hit the full row's three-element support and the Q sets are disjoint within the color. Therefore the safe floor is three hub-complete labelled witnesses per exact-129 color (21 globally in E407). If E has no full row, all B rows miss both P3 endpoints, so six witnesses per color hit both endpoints (42 globally).

## 4. Current headline status

- E407 Q32: five shell templates; finite state coverage replayed; common 284-edge core completion OPEN.
- E408 Q32: 285-edge / excess-six core; threshold-29 finite coverage and completion OPEN.
- E408 Q33: exact-129 factor and seven-block constraints sharpened; joint compatibility OPEN.
- General-r: sibling symbolic progress is conditional on stated extremal inputs; no unconditional r_0 certified.

The full theorem remains **OPEN / NOT_CERTIFIED**. No conditional shell theorem, count bound, or computational coverage result is promoted to a proof for K145.


## 5. Live refresh — latest sibling heads checked 2026-10-25

- Witness-packing branch latest read: [5d0e3ce](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/5d0e3ceab7895be1a947e46853f92bb84477f4e5). Its shell-incidence union lemma proves full-row support union at least 11 in template A and at least 10 in C. Its transversal audit correctly treats the E407 bound delta<=15 as conditional on non-four-partiteness.
- Zero-excess branch latest read: [2b433e2](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/2b433e2f1580e28dfd17db0006e6cc664b4be991). It derives the E407 g=16, epsilon_U=0 four-partite corner, but its “unused eighth point” and subsequent full-group hitting-set inference are not justified by pairwise linearity alone; see R12_E407_G16_EPS0_CORNER_AUDIT.md.
- The current ultimate-closure branch includes the witness-transversal boundary theorem. Its tau(Q)>=7 proof is valid, but the claimed unconditional non-four-partiteness is not. The correct E407 window is delta<=16; if delta=16, Brouwer's bound forces L to be four-partite, not non-four-partite. The E408 Q33 four-partite branch also remains open.
- The beta-sensitive component-count draft in R12_BETA_SENSITIVE_ZERO_EXCESS_PACKING.md has been withdrawn. Its corrected replacement is R12_EXACT129_ZERO_EXCESS_COMPONENT_PACKING.md.
- Added R12_FULL_ROW_SUPPORT_UNION.md and R12_E407_G16_EPS0_CORNER_AUDIT.md. The local TD(4,7) construction shows the eighth point can be used in one block, and an 8-point transversal can hit all 49 blocks without containing a whole part. This audits the local incidence inference only; it is not a full-core counterexample.

All sibling workstreams remain separate; this branch only adds its own reconciliation and proof-audit artifacts. EG617(r=12) remains OPEN / NOT_CERTIFIED.
