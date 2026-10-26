# Progress log — R12 zero-excess witness workstream

## 2026-10-25 — Round 1: robust zero-excess witnesses

### Repository intake

Read-only intake from \`workstream/r12-emergency-sprint-20261024\` and \`workstream/r12-ultimate-closure-20261024\` confirmed the headline theorem remains OPEN / NOT_CERTIFIED. The live T61 front-end bottlenecks are E407 Q32 and E408 Q32/Q33; the shared interface identifies the 47-point, 284-edge core as the common case for E407 Q32 and E408 Q33, while E408 Q32 has 285 core edges. Existing witness-capacity files explicitly leave labelled witness packing open.

This workstream was isolated on branch \`workstream/r12-zero-excess-witness-20261025\`, based on the read-only sprint HEAD \`5258c5fe17af3bf17eb7a2bfb08315c9be9116cd\`. No sibling path was modified.

### New analytic result

Added \`R12_ZERO_EXCESS_WITNESS_THEOREM.md\`.

For \(H\) on 47 vertices with \(\alpha(H)\le4\), \(\delta(H)\ge12\), and \(e(H)\in\{284,285\}\), delete all vertices of positive degree excess to obtain \(H_0\). A Turán comparison proves:
- \(e(H)=284\): \(\alpha(H_0-T)=4\) for every \(|T|\le6\);
- \(e(H)=285\): \(\alpha(H_0-T)=4\) for every \(|T|\le4\).

The proof gives the exact upper bound
\[
e(H_0-T)\le282-\frac E2-12k+\binom{k}{2}-t(12-k)+\binom t2,
\]
where \(E=2e(H)-564\), \(k\) is the number of positive-excess vertices, \(t=|T|\), and \(n=47-k-t\). If \(\alpha(H_0-T)\le3\), Turán's theorem forces \(e(H_0-T)\ge p_3(n)\). The minimum endpoint gaps are 5 for the 284-edge case and 6 for the 285-edge case, so all allowed cases contradict.

The arithmetic table was exhaustively checked over all \(k,t\) in the stated finite ranges. The proof itself is analytic and does not rely on the table as a substitute for the Turán argument.

### Derived applications

1. Any shell row with \(t_b\le3\) has a target-independent four-set \(Q_b\subseteq H_0\) anticomplete to it.
2. In the 284-edge core, any two such regular rows have a common independent-four witness because the union of their core neighborhoods has size at most six.
3. Under the retained exact-129 factor theorem, the ten isolated K5 components in an exact-129 color include at least five components \(\{b\}\cup Q\) with \(b\in B\), \(Q\subseteq H\), and no \(S\)-vertex. Since the 284-edge core has at most four positive-excess vertices and the five components are disjoint within a color, at least one such \(Q\) has all four vertices of degree 12 in \(H\).
4. E407 has non-target residual excess four, hence at least seven exact-129 colors; E408 Q33 has excess three, hence at least eight. Conditional on the retained factor theorem, this gives at least seven/eight zero-excess colored witnesses, respectively.

### Audit boundaries

- **PROVED_ANALYTIC:** robust zero-excess independent-four theorem for 284/285 cores.
- **PROVED_ANALYTIC:** common zero-excess witness for any pair of \(t_b,t_c\le3\) rows in a 284-edge core.
- **PROVED_CONDITIONAL:** at least one zero-excess no-S K5 component per exact-129 color for the 284-edge E407 Q32 and E408 Q33 cases.
- **OPEN:** no E407 Q32 or E408 Q32/Q33 terminal is eliminated.
- **OPEN:** labelled overlap/capacity theorem; actual color-component witnesses cannot be replaced by arbitrary graph-theoretic witnesses without proof.
- **OPEN:** full EG617(r=12).

### Commit log

- \`R12_ZERO_EXCESS_WITNESS_THEOREM.md\`: \`e02fc41103d43e06edd040b93d39bb7dba783510\`.
- \`CANONICAL_STATE.md\`: \`2a3c4a604d7f66daf5fbe31af1fb9500ef56519b\`.


## 2026-10-25 — Round 2: witness-overlap edge-load audit

Added \`R12_WITNESS_OVERLAP_CAPACITY.md\`.

For any family \(\mathcal Q\) of independent 4-sets in \(H\) with pairwise intersections at most one, every pair \(Q,Q'\) has at least three H-edges between \(Q\setminus Q'\) and \(Q'\setminus Q\). If \(r_x\) is the number of selected witness sets containing \(x\), exact double-counting gives
\[
\sum_{\{Q,Q'\}\subseteq\mathcal Q}e_H(Q\setminus Q',Q'\setminus Q)
=\sum_{xy\in E(H)}r_xr_y
\ge3\binom{|\mathcal Q|}{2}.
\]

For five no-S K5 witnesses from each of \(c\) exact-129 colors, \(|\mathcal Q|=5c\), \(r_x\le c\), \(\sum_xr_x=20c\), and \(\sum_x\epsilon(x)=4\). The exact scalar upper bound is
\[
\sum_{xy\in E(H)}r_xr_y
\le\frac12\sum_x(12+\epsilon(x))r_x^2
\le122c^2.
\]
At \(c=7\), this is \(5978\) versus lower bound \(1785\); at \(c=8\), it is \(7808\) versus lower bound \(2340\). Thus the pairwise-crossing inequality does not close the terminals. The arithmetic was corrected and checked; no contradiction is claimed.

This records a valid reusable incidence identity and a clear failed scalar route. The remaining blocker is a labelled overlap bound that uses each witness's shell-row hit pattern and the actual 284-edge core, rather than only the total number of memberships and degree excess.

Commits:
- \`R12_WITNESS_OVERLAP_CAPACITY.md\` (initial): \`c49e9b83a4888ae8573e3657af90687f5e7c7459\`.
- \`R12_WITNESS_OVERLAP_CAPACITY.md\` (corrected arithmetic): \`21a11a95de35cba62f45c07409e58b3f88cbb482\`.



### Arithmetic replay asset

Added \`verify_zero_excess_arithmetic.py\`. It checks every \((E,k,t)\) integer row in the Turán comparison, verifies the gap decreases to the listed endpoint, and checks the exact scalar witness-overlap lower/upper bounds. It explicitly states that this is arithmetic verification only, not a graph-search certificate.

Commit: \`0cabc72f444ad64a215c1a4e30d99ff00bbeaae2\`.


### Status correction and final audit

The scalar edge-load route is now marked **DISPROVED as a sufficient route** (not as a theorem about the graph). The valid pairwise-crossing inequality remains proved; its scalar upper bound is too weak by the explicit numerical comparisons above. The actual terminal-exclusion problem remains OPEN.

Commit: \`adce64d75cee84b28e765392eb8c8bf5ebf24b19\`.


## Round 2 — cross-branch witness-packing synthesis and exact boundary kernel

New files:
- R12_HIGH_SUPPORT_COLOR_WITNESS.md (corrected six-label count; commit aba9b8126ed6a62e5ba15c7d6f0a1c989ab4c183).
- R12_WITNESS_PACKING_BOUNDARY_KERNEL.md (exact E407/E408 incidence ledgers and cross-branch audit; commit 82abaa158f32b2154fef1b80577017e3443072b8).
- verify_witness_boundary_arithmetic.py (integer audit only; commit 52ffcbc8bbf1e5ee49d4ce528de367c2b4f81d84).

The corrected high-support theorem uses the rigorously established six B-labelled no-S K5 components per exact-129 color. Since at least five B labels have k_b>=2 in every eligible shell contract, each exact-129 color has a labelled witness hitting at least two S rows. This closes the previous h=5 boundary; it does not require an exact-star reduction.

The latest sibling witness-packing branch yields at least seven independent four-sets in H per exact-129 color, pairwise linear across colors. The Turán support bounds are v>=29 for E407 Q32 and v>=31 for E408 Q33; if E407 has at least eight exact-129 colors, v>=31, and if E408 Q33 has at least nine, v>=32. The remaining color profiles are E407 129^7,130^4 and E408 Q33 129^8,130^3.

For the minimal-support boundaries, the exact ledgers are:
- E407 v=29: e(H[V_*])=112-g, x=124+epsilon_*+2g, e(H[W])=48-epsilon_*-g, with g+epsilon_*<=16 and epsilon_*+2g>=2.
- E408 Q33 v=31: e(H[V_*])=129-g, x=114+epsilon_*+2g, e(H[W])=41-epsilon_*-g, with g+epsilon_*<=17.
These retain the core degree/excess and alpha(H[W]) constraints without double counting edges.

A further extreme-corner reduction is proved for E407 g=16, epsilon_*=0: the selected 49 blocks form TD(4,7) on 28 active vertices plus one unused point, and H[W]=K5 union K5 union K4 union K4. The remaining labelled incidence system is still open.

Cross-branch audit:
- The sibling m=10 witness-star claim e(H[U])=135 or >=144 is not justified: the second-Turán theorem permits H[U]=3K10 plus 1..8 cross-part edges. This is a gap in that local dichotomy, not a full-core counterexample.
- The claim that a missing edge in M[S] automatically reduces the number of S-intersecting K5 components for every fixed color is not justified by that fact alone. The safe universal count remains seven total Q blocks and six B-labelled blocks unless an additional forcing lemma is supplied.

Headline status remains OPEN / NOT_CERTIFIED. The next target is to eliminate the two exact incidence kernels, not to add more scalar witness counts.


## Round 3 — live sibling refresh; exact four-partite E407 reduction

Latest sibling heads reread:
- ultimate closure: 0bdce893225af4273fa5f95d68815ff79c130446;
- witness packing: 5d0e3ceab7895be1a947e46853f92bb84477f4e5.

New result in R12_WITNESS_PACKING_BOUNDARY_KERNEL.md:
- In the E407 v=29 minimal-support branch, if L=bar(H[V_*]) is four-partite, then its parts are (7,7,7,8), the 49 Q-blocks form TD(4,7) on 28 active points plus one unused point z, and all extra L edges are incident to z.
- If delta=e(L)-294, then d_H[V_*](z)=28-delta. The core degree cap gives delta>=12; the exact budget then forces epsilon_*=epsilon_z=16-delta, z has no W-neighbours, and e(H[W])=32 with H[W]=K5 union K5 union K4 union K4.
- The group-label argument excludes delta=12 and delta=13: in those cases there are at most one positive-excess W vertex, so one K5 component is entirely zero-excess; its five vertices share one seven-point group as a common neighborhood, creating K12. Thus any four-partite E407 boundary must have delta in {14,15,16}.
- The delta=14/15 branches force at least one positive-excess vertex in each K5 component. The delta=16 case still has an exceptional branch where all four excess units lie in one K4 component; otherwise the group-label structure applies. The four-partite branch is reduced, not closed.

Latest sibling audits:
- The general transversal lower bound tau(Q)>=7 is usable.
- Do not infer non-four-partiteness by ruling out only the complete Turan graph; incomplete four-partite graphs remain possible.
- Do not use the new beta-sensitive component floors until a color-specific co-location theorem is proved. omega(M[S]) bounds the number of S-vertices in one K5 component, not the number of distinct components meeting S. The safe universal count remains seven S-avoiding Q sets, at least six B-labelled, and at least two zero-excess B-labelled witnesses per exact-129 color.

New commit sequence:
- boundary-kernel extension and live audit: a8f3afbfe3be135352d39d4229224ceca1af0ae6
- high-support sibling audit: 0f46dab0656cd3e07627cb8e6df8b0cc02cd3c54

The E407 non-four-partite boundary and the E408 Q33 v=31 boundary remain OPEN. E408 Q32 is still a separate 285-edge-core problem. EG617(r=12) remains OPEN / NOT_CERTIFIED.


## Round 4 — live sibling refresh; corrected four-partite boundary analysis (2026-10-25)

Live sibling heads reread:
- ultimate closure: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40;
- emergency sprint: ad56a91c644458cb16dd590b7a4ed0e800978a81;
- witness packing: 5d0e3ceab7895be1a947e46853f92bb84477f4e5;
- this workstream: 3dbc0349a678e1f8b668e940967699f3b3de527a.

### New result: E408 Q33 four-partite boundary S0 >= 11

In R12_WITNESS_PACKING_BOUNDARY_KERNEL.md, Section 13 gives an independent proof that the four-partite E408 Q33 minimum-support boundary must satisfy
\[
S_0=\epsilon_U+2\delta\ge11,\qquad \delta+\epsilon_U\le17.
\]
Key ingredients:
1. The 56 blocks force L's parts to be A,B,C (size 8) and D (size 7); each pair between D and a large part is used once, and unused pairs between large parts form perfect matchings.
2. Every outside vertex with exactly seven core neighbours has neighbourhood D. Such vertices form a clique: otherwise an independent triple from A,B,C plus two nonadjacent such vertices would violate alpha(H)<=4. Since D is a 7-clique and no counterexample can contain a monochromatic K13, their count k is at most 5.
3. This bound and the exact cross-edge budget exclude S0=8 and S0=9. At S0=10, only k=4 or5 is arithmetically possible; the size-8/9 transversal classification and a three-per-large-part capacity bound force at least ten full-large-part neighbourhoods, while only nine can occur. Hence S0>=11.

This proof does not rely on the selected-pair count in the sibling R12_E408_Q33_FOUR_PARTITE_S0_10_EXCLUSION.md. That sibling's s=1/s=2 pair-count step is invalid as written: a selected pair absent from all Q blocks may be an H-edge, not necessarily an extra L-edge. The theorem's conclusion is independently recovered by Section 13 under the actual counterexample constraint.

### Corrected E407 four-partite branch

Audit of the earlier Sections 6/9 found that the 49 witness blocks do not force the eighth point of the (7,7,7,8) partition to be unused. For a seven-by-eight pair type, the seven unused pairs have degree one on the seven-point side but can have nonuniform degrees on the eight-point side. The earlier TD(4,7)-plus-unused-point reduction, and all conclusions depending on a distinguished z (including delta>=12 and the K5∪K5∪K4∪K4 structure), are withdrawn.

The valid E407 v=29 / 49-block ledger remains
\[
\delta\ge2,\quad \delta+\epsilon_U\le16,\quad
\epsilon_U+2\delta\ge2,\quad 0\le\epsilon_U\le4.
\]
The four-partite branch is still open; no invalid distinguished-point assumption is retained.

Updated proof assets:
- R12_WITNESS_PACKING_BOUNDARY_KERNEL.md — Sections 6 and 9 corrected; Section 13 adds the independent E408 S0>=11 proof.
- verify_witness_boundary_arithmetic.py — arithmetic checks updated for the refined E408 degree windows.
- Latest commits: boundary proof df41618effb2ce5e025f20258ecffd357af2f258; E407 audit correction 49afd66a18850049c80e4b48c073582a9ecf3473; verifier cleanup 3dbc0349a678e1f8b668e940967699f3b3de527a.

Status firewall: E408 Q33 non-four-partite boundary remains OPEN; E407 Q32, E408 Q32 (285-edge core), other support sizes, and the original K145 bridge remain OPEN / NOT_CERTIFIED. No full EG617(r=12) proof is claimed.


## Round 5 — live sibling refresh and universal E408 Q33 S0>=14 result (2026-10-26)

Current sibling heads read-only checked:
- E407 Q32 terminal: 79c1086efca893fad8933210a92a432457232410
- E408 Q33 global compatibility: 0cb2ff3968f005c9cb255958df7c02b220678701
- E408 Q32 excess-six: a0ba6db26c7e8b00a4217dcbcbf298895dff93ce
- unified witness capacity: 9935e0d2343fc08d9e65d51ff495cfb260d6de95
- emergency sprint: f4c3b06891d29238d4f9cca2588f442004b6dc97
- this branch before the round: f3935770d0c2b4e41d164d734d6fd0f9de3e56a8

### New result

Added R12_E408_Q33_S0_13_EXCLUSION.md and verify_e408_s0_13_profiles.py. Under the registered 47-core / 284-edge / alpha<=4 / omega<=11 contract and the 31-point, 56-witness exact-129 boundary, the theorem excludes S0=13 without assuming L is four-partite. Combining with the separately audited universal S0>=12 theorem gives
\[
\boxed{S_0=\epsilon_U+2\delta\ge14,\qquad \delta\ge5.}
\]
The finite profile verifier enumerates 60 labelled degree/T-incidence parameter cases and checks the m=10/9/8/7 buckets. Arithmetic checks do not certify graph realization.

### Cross-branch status

- E408 Q33, minimum support v=31: universal S0>=14; four-partite branch has S0>=22. The non-four-partite branch for S0>=14 and larger support sizes remain open.
- E407 Q32, minimum support v=29: this line's universal bound is S=epsilon_U+2delta>=9 (hence delta>=3); the sibling terminal line has conditionally closed multiple delta=14..16 subcases but still has delta<=13 and shell-template compatibility gaps.
- E408 Q32 remains a separate 285-edge / excess-six core. Its support reduction v>=44 leaves the v=44 labelled triple terminal open.
- The unified labelled-witness route still has an unresolved label-transfer/component-realization gap.
- The original T61-to-K145 bridge and complete EG617(r=12) theorem remain OPEN / NOT_CERTIFIED.

No sibling branch was modified.


## Round 6 — proof audit corrections (2026-10-26)

The S0=13 exclusion was audited before retaining its conditional status. The theorem note and arithmetic verifier were repaired as follows:

- Proved distinct R-only eight-transversals are disjoint; two disjoint ones have a third complement transversal, while explicitly not assuming that complement is a realized W-neighborhood.
- Generalized the clique argument to any three mathematical transversals partitioning R, allowing the W-group for one part to be empty.
- Replaced the invalid high-neighborhood intersection bound \(1+b_y\) with the correct pair-counting bound \(|Y\cap S_i|\le q_y-7\), where \(Y=N_H(y)\cap R\). The q=10,b=1 case is covered by the same independent-five/W-degree contradiction as q=10,b=2.
- Removed the invalid special-incidence argument for the m=8,7 two-neighborhood cases. The multiplicity cap \(m_i\le4\) forces a multiplicity-four group if only one or two neighborhoods are realized; the complement transversal supplies the required partition for the clique contradiction.
- Removed the unsupported claim that the universal S0=13 exclusion itself implies \(\delta+\epsilon_U\le17\); that upper bound remains only in the separately proved four-partite subcase.

The arithmetic enumeration was replicated in-session: 60 labelled parameter cases, with m=10:6, m=9:24, m=8:22, m=7:8; all arithmetic assertions passed. This is not a graph-realization certificate. Under the stated core/exact-129 contracts, the inherited universal S0>=12 lower bound, and the separate universal S0=12 exclusion, the repaired conditional result is \(S_0\ge14\), hence \(\delta\ge5\), for the minimum-support E408 Q33 boundary only.

Full EG617(r=12) remains OPEN / NOT_CERTIFIED. No sibling branch was modified.


## Round 7 — S0=14 equality terminal narrowed (2026-10-26)

Created R12_E408_Q33_S0_14_NO_SEVEN_TRANSVERSAL.md and its arithmetic verifier. Under the retained core/exact-129/transversal contracts, S0=14 cannot have any seven-point transversal T: a realized q=7 witness forces a T, then the T-complete clique and T-incidence sum force at least 6-(k+a) high b=7 vertices, which join that clique to exceed omega(H)<=11. If T exists without a q=7 witness, the multiplicity cap and T-type clique force a K12. Therefore all q_w=8 and no seven-point transversal exists.

The remaining no-transversal all-q=8 system has an exact omission-set description. For each color c, X_c is its three omitted U-vertices, each W-neighborhood meets X_c in at most one point, sum_u rho_u=24 for rho_u=8-c_u, and
\[
\tau_w=\sum_{u\in N_U(w)}\rho_u,\qquad d_H(u,W)=6-3\rho_u+j_u+\epsilon_u.
\]
The arithmetic verifier passed 30 integer inequality states and the pairs (epsilon_U,delta)=(0,7),(2,6),(4,5). This is a structural reduction only; S0=14 remains OPEN.

Full EG617(r=12) remains OPEN / NOT_CERTIFIED. No sibling branch was modified.
