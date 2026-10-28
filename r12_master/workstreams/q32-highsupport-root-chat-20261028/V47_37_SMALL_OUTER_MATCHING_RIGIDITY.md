# E408 Q32 full support — global matching rigidity between the small triangle and outer blocks

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL structural theorem.** No Q32 closure claimed.

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

## 3. A fixed small block has the same matching permutation to every outer block

Fix A. For each D in T, let p_D be the unique perfect-matching permutation from the four labels of A to the globally aligned outer-track labels in D.

Take a light edge DE of L. The three-block switch theorem applies to the 5,5,4 triangle A-D-E. If p_D and p_E differ, they differ by a single transposition (ab), and the unique extra edges in A-D and A-E must both be incident to the same small-block label s in {a,b}. In particular, whenever p_D(s) != p_E(s) across a light edge, both endpoints D,E belong to
`S_s={D in T: the extra edge of A-D is incident to A_s}`.

If the value p_D(s) were nonconstant over T, connectedness of L would give a nontrivial partition of T by the values of p_D(s). Every vertex incident to a crossing edge would lie in S_s. Lemma 2.1 would imply |S_s|>=5, i.e. e_A(s)>=5.

But for every nonempty residual fiber n_s>=1, the degree ledger gives e_A(s)<=4. Thus p_D(s) is constant over T for every label s with n_s>=1. At most one fiber is empty, so at least three coordinates of the permutations p_D are constant. Since each p_D is a permutation, the fourth coordinate is forced too.

Therefore **p_D is one fixed permutation p_A, independent of D**.

The identical argument applies to B and C, because their residual maps have the same fibers F_s. Hence each of the three small blocks has a fixed matching permutation to the outer tracks, independent of which outer block is chosen.

## 4. Global matching-type dichotomy

Let the three fixed permutations be p_A,p_B,p_C. Applying the local 4,5,5 switch theorem to A,B,D, B,C,D, and A,C,D shows that every pair among p_A,p_B,p_C is either equal or differs by a transposition. Two distinct transpositions cannot compose to a transposition (their product is a 3-cycle or a double transposition), so there are at most two distinct permutations.

Thus the whole 3+7 cell has only two matching regimes:

1. **Aligned regime:** p_A=p_B=p_C.
2. **Single-transposition regime:** exactly one of the three permutations differs from the other two by one fixed transposition.

In the second regime, the local switch lemma forces the three extra-edge endpoints in every outer block D to share one small label s_D in the moved pair. The zero-slack transversal blocker further requires n_{s_D}<=1. If either moved label had fiber size at least two, no block could use it as s_D, forcing all seven extra endpoints to use the other label; that would give e_A(t)=7, contradicting e_A(t)<=5-n_t<=5. Hence both moved labels have residual fiber size at most one.

Therefore the single-transposition regime is possible only for residual fiber profiles
`(3,3,1,0)` or `(3,2,1,1)`.
The other profiles `(3,2,2,0)` and `(2,2,2,1)` are excluded from this regime.

## 5. Scope firewall

This is a global matching normal form for the 3+7 cell, not a graph UNSAT certificate. The aligned regime and the two remaining low-fiber switch profiles still require compatibility with the residual track assignment, the outer heavy-edge budget `x_T=3+z<=7`, and the eleven-color edge partition. Full-support m=10 remains OPEN; m=8,9 and EG617(r=12) remain OPEN / NOT_CERTIFIED.
