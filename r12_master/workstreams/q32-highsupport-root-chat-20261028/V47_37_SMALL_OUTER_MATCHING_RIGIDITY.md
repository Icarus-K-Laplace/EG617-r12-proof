# RETRACTED — E408 Q32 small-to-outer matching rigidity (invalid proof)

Date: 2026-10-28  
Status: **RETRACTED / INVALID PROOF (2026-10-29).** Do not use this file's former global-rigidity conclusion.

## 1. Frozen 3+7 cell

Use the disconnected m=10 light-block component split 3+7. Let A,B,C be the small light triangle and let T be the seven outer blocks. The registered reductions give:

- A,B,C are independent 4-sets with each pair exactly a perfect matching;
- every A-D, B-D, C-D pair for D in T has exactly five edges (one unique perfect matching plus one extra edge);
- the outer light graph L on T is connected with minimum degree at least four;
- the seven outer blocks are globally aligned into four K7 tracks;
- the common small-block residual map f:R->[4] has fibers F_s of sizes n_s, and at least three n_s are positive;
- for a small-block vertex A_s, `d_H(A_s)=9+e_A(s)+n_s`, where e_A(s) is the number of A-to-outer extra-edge endpoints at A_s;
- the small-block degree-excess sum is exactly two:
  `sum_s (e_A(s)+n_s-3)=2`.
  Hence `e_A(s)<=5-n_s`, in particular `e_A(s)<=4` whenever n_s>=1.

## 2. Seven-vertex cut-endpoint lemma

**Lemma 2.1.** If L is any graph on seven vertices with minimum degree at least four, every nontrivial vertex partition has at least five vertices incident to a crossing edge.

**Proof.** Let the smaller side have size k<=3.
- k=1: its vertex has at least four crossing neighbors, giving at least five endpoints.
- k=2: each of the two vertices has at most one neighbor inside its side, hence at least three crossing neighbors; the endpoint set has both vertices on that side and at least three on the other, so at least five.
- k=3: each vertex on the three-vertex side has at most two internal neighbors and hence a crossing neighbor; each vertex on the four-vertex side has at most three internal neighbors and degree at least four, hence also has a crossing neighbor. All seven vertices are endpoints. QED.

The exact regression in `verify_v47_37_matching_cut_bound.py` checks the six cut-size cases and the lower bounds above.

## 3. RETRACTION — switch endpoints are on different small labels

The former proof claimed that if the matching permutation from a fixed small block A to D changes across a light edge DE, then both extra edges in AD and AE are incident to the same small vertex A_s. This is false.

In the exact 4,5,5 switch lemma, for a transposition sigma=(0 1) and switch parameter s=0, the valid extra edges in the normalized three-block graph are A_0 C_1 and B_0 C_0. Assign A=D, B=E, C=the fixed small block. Then the extra edges are D_0 A_1 and E_0 A_0: they hit different small-block labels. The companion exact verifier certifies this as a valid alpha<=4 local configuration.

Therefore the previous cut-charging step is invalid: crossing endpoints cannot all be charged to one set S_s. The cut-endpoint lemma in Section 2 remains true, but it does not imply e_A(s)>=5.

## 4. Correct local implication retained

For a fixed small block A and a light outer edge DE, the switch theorem says either the two matching permutations agree, or they differ by a transposition. In the transposition case the two extra edges are incident to the two distinct moved small-side labels, one each.

The degree ledger itself remains valid:
- epsilon_s := e_A(s)+n_s-3 >= 0;
- sum_s epsilon_s=2;
- e_A(s)=3-n_s+epsilon_s;
- sum_s e_A(s)=7.

No global constancy of p_D follows from the old cut argument. The aligned-versus-single-transposition global dichotomy and the residual-profile exclusions formerly derived from that constancy are withdrawn.

## 5. Scope firewall

This file is retained as an audit trail only. The cut-size lemma is valid; the global small-to-outer matching theorem is not proved. The independent z=0,1 partition-alignment theorem must be audited separately and does not rely on this retracted argument. Full-support Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.

## 5. Scope firewall

This is a global matching normal form for the 3+7 cell, not a graph UNSAT certificate. The aligned regime and the two remaining low-fiber switch profiles still require compatibility with the residual track assignment, the outer heavy-edge budget `x_T=3+z<=7`, and the eleven-color edge partition. Full-support m=10 remains OPEN; m=8,9 and EG617(r=12) remain OPEN / NOT_CERTIFIED.
