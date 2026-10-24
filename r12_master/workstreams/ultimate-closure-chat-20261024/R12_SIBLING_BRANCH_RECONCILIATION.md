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

The component decomposition permits a no-S K5 component of the form {p}∪Q. There can be at most one such component, but it is not a B-labelled witness: Q is not known to be anticomplete to any B-row. Therefore the safe count is:

| Shell type | No-S components | B-labelled components |
|---|---:|---:|
| A/B, M[S] empty | at least 7 | at least 6 |
| C/D/E, at most two components can meet S | at least 8 | at least 7 |

This distinction matters when counting hub-complete witnesses. If n_3≥1, every B-labelled component witness that misses any hub must hit a fixed full B-row's three-element core neighborhood. Since the component witnesses are disjoint within one color, at most three can miss a hub. The safe consequences are 3 hub-complete B-labelled witnesses per exact-129 color for A/B and 4 for C/D/E, not 4/5 from counting all no-S components without a B-label.

For E with n_3=0, the row constraints force all ten B-rows to miss the two endpoints of the P3. At least seven B-labelled no-S components remain per exact-129 color, and each Q hits both endpoints. Thus at least 49 endpoint-complete labelled witnesses occur globally over the seven guaranteed exact-129 colors.

This audit does not invalidate the 7/8 total independent-four packing theorem or its |V_*| support bounds: the Q from a pivot-containing component is still an independent four-set in H. It only blocks using that Q in a proof that requires an associated B-row.

## 4. Current headline status

- E407 Q32: five shell templates; finite state coverage replayed; common 284-edge core completion OPEN.
- E408 Q32: 285-edge / excess-six core; threshold-29 finite coverage and completion OPEN.
- E408 Q33: exact-129 factor and seven-block constraints sharpened; joint compatibility OPEN.
- General-r: sibling symbolic progress is conditional on stated extremal inputs; no unconditional r_0 certified.

The full theorem remains **OPEN / NOT_CERTIFIED**. No conditional shell theorem, count bound, or computational coverage result is promoted to a proof for K145.


## 5. Later live refresh — 2026-10-25

After the first reconciliation commit, the witness-packing branch advanced to [2bb0982ea89f87eaf0e7aec3ec87590e53bd297b](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/2bb0982ea89f87eaf0e7aec3ec87590e53bd297b), and the zero-excess branch advanced to [f3c9ef6b3a4bfadad4f70a16bb0e7c6434bb0777](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/f3c9ef6b3a4bfadad4f70a16bb0e7c6434bb0777). The former adds a stronger zero-excess component-witness count and the star-lemma audit; the latter adds an arithmetic verifier for the high-support label dichotomy.

The current ultimate-closure branch also acquired [R12_WITNESS_TRANSVERSAL_BOUNDARY_THEOREM.md](https://github.com/Icarus-K-Laplace/EG617-r12-proof/blob/workstream/r12-ultimate-closure-20261024/r12_master/workstreams/ultimate-closure-chat-20261024/R12_WITNESS_TRANSVERSAL_BOUNDARY_THEOREM.md) and a corrected verifier at [commit 78c30e86b0f432464ca5375695da97a27b230878](https://github.com/Icarus-K-Laplace/EG617-r12-proof/commit/78c30e86b0f432464ca5375695da97a27b230878). We independently replayed its arithmetic checks. It proves the transversal floor tau(Q)>=7 at the E407 (v,m)=(29,49) and E408 Q33 (31,56) support boundaries, hence every outside core vertex has at least seven neighbors into the selected witness union. The exact boundary windows are:
- E407: delta+epsilon_U<=16, epsilon_U+2delta>=2, and delta<=15;
- E408 Q33: delta+epsilon_U<=17.
These are stronger necessary constraints but still compatible with the remaining induced-subgraph lower bounds.

The beta-sensitive component count is recorded in R12_BETA_SENSITIVE_ZERO_EXCESS_PACKING.md. The emergency star lemma's basic incidence facts are retained, but its asserted e(H[U])=135 or >=144 dichotomy is not used: the second-Turan step proves tripartiteness, not completeness.
