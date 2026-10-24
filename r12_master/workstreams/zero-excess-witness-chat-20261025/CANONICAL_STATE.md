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
