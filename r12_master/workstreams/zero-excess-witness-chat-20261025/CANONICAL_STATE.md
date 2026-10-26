# Canonical state — R12 zero-excess witness workstream

Date: 2026-10-25  
Repository: \`Icarus-K-Laplace/EG617-r12-proof\`  
Branch: \`workstream/r12-zero-excess-witness-20261025\`  
Scope: fixed \(r=12\) only. This line does not modify sibling workstreams.

## Headline

**EG617(r=12) remains OPEN / NOT_CERTIFIED.**

## New theorem

\`R12_ZERO_EXCESS_WITNESS_THEOREM.md\` proves analytically:

- For a 47-point core \(H\) with \(\alpha(H)\le4\), \(\delta(H)\ge12\), and \(e(H)=284\), let \(H_0\) be obtained by deleting all vertices with \(d_H>12\). Then \(\alpha(H_0-T)=4\) for every \(T\) of at most six vertices.
- For \(e(H)=285\), the same holds for every \(T\) of at most four vertices.
- Therefore each regular shell row with at most three core neighbours has an independent four-set witness entirely in \(H_0\), and in the 284-edge core every pair of such rows has a common witness.
- Under the retained exact-129 factor theorem, each exact-129 color in E407 Q32 and E408 Q33 has at least one no-S K5 component whose four core vertices all have degree 12 in \(H\). This yields at least seven such colored witnesses for E407 Q32 and at least eight for E408 Q33.

The graph lemma is **PROVED_ANALYTIC**. The exact-129 component corollary is **PROVED_CONDITIONAL** on the retained Kang–Pikhurko equality/factor theorem and the contextual color caps.

## Remaining blocker

This supplies necessary witness structure but does not eliminate any E407/E408 terminal. The open step is a joint labelled-overlap/capacity contradiction using the actual 284-edge core and unique color ownership. No sum of local costs may be taken over overlapping witnesses without an explicit multiplicity bound.

## Repository discipline

Only \`r12_master/workstreams/zero-excess-witness-chat-20261025/\` is modified by this branch. The sprint/master/ultimate-closure branches were read-only references.


## Round-2 overlap audit

Added \`R12_WITNESS_OVERLAP_CAPACITY.md\` with a pairwise crossing lemma and exact edge-load identity. For a linear family of \(m\) independent 4-sets, every pair requires at least three cross-edges, and the total crossing count is exactly \(\sum_{xy\in E(H)}r_xr_y\).

For \(m=5c\) selected K5 witnesses from \(c\) exact-129 colors, the current scalar cap gives only
\[
\sum_{xy\in E(H)}r_xr_y\le122c^2,
\]
versus lower bound \(3\binom{5c}{2}\). At \(c=7,8\) these are \(5978>1785\) and \(7808>2340\), so this route is insufficient. No contradiction is claimed.

- Pairwise witness crossing lemma: **PROVED_ANALYTIC**.
- Exact edge-load identity: **PROVED_ANALYTIC**.
- Scalar overlap contradiction: **OPEN / DISPROVED as a sufficient route**.
- Labelled shell-incidence overlap bound: **OPEN**.
- E407 Q32 and E408 Q32/Q33: **OPEN**.
- EG617(r=12): **OPEN / NOT_CERTIFIED**.


## Arithmetic audit asset

\`verify_zero_excess_arithmetic.py\` checks the complete finite integer table for the zero-excess theorem and the witness-overlap scalar comparison. It does not certify any graph completion or substitute for the analytic proof.


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


## Round 5 — E408 Q33 S0=13 exclusion and sibling refresh (2026-10-26)

Read-only sibling heads checked:
- E407 Q32 terminal: 79c1086efca893fad8933210a92a432457232410
- E408 Q33 global compatibility: 0cb2ff3968f005c9cb255958df7c02b220678701
- E408 Q32 excess-six: a0ba6db26c7e8b00a4217dcbcbf298895dff93ce
- unified witness capacity: 9935e0d2343fc08d9e65d51ff495cfb260d6de95
- emergency sprint: f4c3b06891d29238d4f9cca2588f442004b6dc97

Added R12_E408_Q33_S0_13_EXCLUSION.md and verify_e408_s0_13_profiles.py. The intended result is to exclude S0=13 in the 31-point / 56-witness minimum-support E408 Q33 boundary, conditional on the registered 47-core / 284-edge / alpha<=4 / omega<=11 contract, exact-129 factor, inherited universal S0>=12 lower bound, and the separate universal S0=12 exclusion. The finite profile enumerator has 60 labelled cases, bucketed m=10:6, m=9:24, m=8:22, m=7:8.

## Round 6 — independent proof audit and corrections (2026-10-26)

Before retaining the S0=13 exclusion, an independent audit found and repaired three issues in the written argument:

1. **Transversal complement:** a complement transversal is a mathematical object and need not itself occur as a W-neighborhood. The proof now explicitly distinguishes those claims and proves that clique consequences still apply to a partition by three mathematical transversals, with the missing W-group allowed to be empty.
2. **High-neighborhood incidence bound:** the correct pair-counting conclusion is \(|Y\cap S_i|\le q_y-7\), where \(Y=N_H(y)\cap R\) hits the \(7-b_y\) partitions missed by y. The previous displayed \(1+b_y\) bound was invalid. The q=10,b=1 case is now handled together with q=10,b=2 by the independent-five/W-degree contradiction.
3. **Two realized neighborhoods:** the previous special-incidence argument for m=8,7 was not valid. It is replaced by the multiplicity cap \(m_i\le4\): one realized set is impossible, and two realized sets have multiplicities (4,4) or (4,3), so a multiplicity-four clique contradiction follows using the complement transversal.

The universal S0=13 exclusion does not derive an upper bound on \(\delta+\epsilon_U\); the existing \(\delta+\epsilon_U\le17\) bound applies only in the separately proved four-partite subcase. The retained conditional conclusion is
\[
\boxed{S_0=\epsilon_U+2\delta\ge14,\qquad \delta\ge5.}
\]
The arithmetic/profile checks were replicated in-session and pass (60 cases; buckets 6/24/22/8). This is an arithmetic audit, not a graph-realization certificate. The analytic proof is now repaired under its stated contracts; the independent prior S0>=12 theorem remains an inherited conditional input.

### Current frontier

- E408 Q33 minimum support v=31: conditionally \(S_0\ge14\) without four-partiteness; the four-partite subcase has the stronger conditional \(S_0\ge22\). Profiles with \(S_0\ge14\) and larger support sizes remain open.
- E407 Q32 minimum support v=29: this line's bound is \(S=\epsilon_U+2\delta\ge9\), hence \(\delta\ge3\). Sibling work has closed some delta=14..16 subcases, but delta<=13 and shell-template compatibility remain open.
- E408 Q32 remains the separate 285-edge / excess-six core. Support reduction v>=44 leaves the v=44 terminal open.
- The unified labelled-witness route still has a label-transfer/component-realization gap.
- The original T61-to-K145 bridge and complete EG617(r=12) theorem remain OPEN / NOT_CERTIFIED.

No sibling branch was modified.
