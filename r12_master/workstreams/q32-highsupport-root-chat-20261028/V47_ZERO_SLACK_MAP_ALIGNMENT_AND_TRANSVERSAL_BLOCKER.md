# E408 Q32 full support — zero-slack map alignment and three-block transversal blocker

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL structural theorem; no full-support closure claimed.**

## 1. Scope: the disconnected m=10 cells

Use the ten pivot blocks Q_1,...,Q_10 and residual R, |R|=7. In the disconnected light-block graph, the 2+8 and 3+7 component cells have already been reduced to

- every cross pair from the small component S to an outer block has exactly five H-edges;
- every pair within S is light, hence has exactly four H-edges and is a perfect matching;
- y_i=0 for every i in S, so each r in R has exactly one neighbor in each small block;
- Delta(H[R])<=2 and d_H(r)=12 for every r in R.

The last two facts imply each residual vertex has a unique label in each small block, and its fiber over a label is a clique in H[R].

## 2. Zero-slack map alignment lemma

### Lemma 2.1

Let A,B be two disjoint independent 4-sets with H[A,B] exactly a perfect matching. Suppose every r in R has exactly one neighbor f_A(r) in A and exactly one neighbor f_B(r) in B. Assume |R|=7 and Delta(H[R])<=2, while alpha(H)<=4. Label A and B along their matching. Then

> **f_A(r)=f_B(r) for every r in R.**

### Proof

For any independent pair r,s in H[R], zero-slack and alpha(H)<=4 imply f_A(r) != f_A(s) and f_B(r) != f_B(s).

We claim
[
{f_A(r),f_A(s)}={f_B(r),f_B(s)}.
]
If not, choose a label b in the first pair but not the second. The two A-vertices whose labels are outside {f_A(r),f_A(s)}, together with r,s and B_b, form an independent 5-set: the chosen A-vertices miss r,s; B_b misses both r,s; and B_b is matched only to an A-label outside the chosen two A-vertices. Contradiction.

Now fix r. Among the at least four nonneighbors of r in R, there are two vertices s,t that are nonadjacent to each other: otherwise those nonneighbors would contain a clique of size at least four, impossible under Delta(H[R])<=2. Hence f_A(s) and f_A(t) are distinct, and both differ from f_A(r). Applying the unordered-pair identity to (r,s) and (r,t) gives
[
f_B(r)in{f_A(r),f_A(s)}cap{f_A(r),f_A(t)}={f_A(r)}.
]
Thus f_B(r)=f_A(r). QED.

### Corollary 2.2

- In the 2+8 cell, the two small blocks A,B have the same residual-neighbor map after matching alignment.
- In the 3+7 cell, the three small blocks A,B,C have the same residual-neighbor map. Indeed, every pair is a light perfect matching, and triangle matching consistency aligns the three matchings.

Write the common map as f:R->[4], with fibers F_h=f^{-1}(h) and n_h=|F_h|. Every F_h is a clique in H[R], and the small-block neighbors of r form the matched pair/triple with label f(r).

## 3. Three-block transversal theorem in the 3+7 cell

Fix an outer block D. The pair graphs A-D, B-D, C-D each have five edges: a unique perfect matching plus one extra edge. The exact 4,5,5 switch lemma, applied to every pair of small blocks and D, gives the following local normal form after relabeling:

- either all three base matchings are aligned and the three extra edges are arbitrary nonmatching edges;
- or one base matching differs by a transposition, and the three extra edges have the synchronized switch endpoints.

For q in D, let S_A(q), S_B(q), S_C(q) be the sets of labels in A,B,C adjacent to q. Each has size one or two.

### Lemma 3.1 — common-track blocker

For every q in D, the intersection
[
I(q)=S_A(q)cap S_B(q)cap S_C(q)
]
is nonempty and has size at most two.

If I(q)={h}, there exists an independent transversal
[
T_h={A_a,B_b,C_c},qquad {a,b,c}=[4]\setminus{h},
]
that is nonadjacent to q.

If I(q)={h,j} has size two, every transversal using the three distinct labels [4]\setminus{i} meets N(q), for every i in [4].

### Proof

In the aligned normal form, the base matching label is common to all three sets. In the switch normal form, the synchronized endpoints likewise give a common label for each q. Since each S-block has size at most two, the intersection has size at most two.

If I(q)={h}, each allowed label set [4]\setminus{h} after deleting S_A(q), S_B(q), or S_C(q) has size at least two. Hall's condition holds for one or two coordinates automatically; the union of all three allowed sets can fail to have size three only if all three S-sets contain the same second label, which would make |I(q)|=2. Thus a system of distinct representatives exists, giving T_h.

If I(q)={h,j}, any transversal whose labels are the three labels other than i must use at least one of h,j, whether i equals h, j, or neither. q is adjacent to both labels in all three blocks, so the transversal meets N(q). QED.

## 4. Degree-cap consequence for each outer-block vertex

Every q in an outer block has degree exactly 12 in the 3+7 cell, because that block has zero total degree excess. It has one base neighbor in each of the other nine pivot blocks. Write e_Q(q) for its number of extra Q-Q incidences beyond those nine base neighbors, and d_R(q) for its number of neighbors in R. Then
[
e_Q(q)+d_R(q)=3.
]
Let k(q) be the number of the three mandatory extra edges from D to A,B,C that are incident with q. Then k(q)<=e_Q(q).

### Case A: |I(q)|=1

Write I(q)={h}. For every r in F_h, the vertex r is nonadjacent to all three vertices of T_h. If qr were also a nonedge, T_h union {r,q} would be an independent 5-set. Hence q is adjacent to every r in F_h:
[
d_R(q)ge n_h.
]
Consequently
[
oxed{k(q)le e_Q(q)le 3-n_h.}
]
In particular, if n_h=3 then k(q)=0; if n_h=2 then k(q)<=1; and if n_h=1 then k(q)<=2.

### Case B: |I(q)|=2

Then q has both common-track neighbors in each of A,B,C. It must be incident with the extra edge in each of the three pairs, so k(q)=3. Since e_Q(q)+d_R(q)=3, it follows that
[
oxed{k(q)=3,quad d_R(q)=0,quad e_Q(q)=3.}
]
Thus q has no R-neighbor and no extra Q-Q incidence outside the three edges to the small component.

There is a further fiber-size restriction. If r in F_h and s in F_j were nonadjacent for h != j, choose the two labels a,b outside {h,j}; then q,r,s,A_a,B_b would be an independent 5-set. Hence every cross-pair between F_h and F_j must be an H-edge. Since Delta(H[R])<=2, this forces
`n_h+n_j<=3`
whenever both fibers are nonempty; if one is empty the inequality is automatic. Thus a 3+7 double-track vertex can only use a pair of tracks whose fiber sizes sum to at most three.

### Block-level ledger

Each outer block D has exactly one extra edge to each of A,B,C, hence
[
oxed{sum_{qin D} k(q)=3.}
]
Therefore its four vertices must realize one of the two patterns above, with all endpoint multiplicities respecting the fiber-size caps. This is strictly stronger than the previous scalar condition t_i^T+y_i=2.

## 5. What this closes and what it does not

New exact restrictions for the 3+7 cell:

1. the three zero-slack residual-neighbor maps coincide;
2. each outer vertex has a common track across all three small blocks;
3. a singleton common track h forces adjacency to the entire residual fiber F_h and imposes k(q)<=3-n_h;
4. a two-track vertex consumes all three small-component extra edges and has no residual neighbors;
5. the three extra endpoints per outer block sum to exactly three.

These constraints are ready to combine with the 18 residual path/cycle types in `verify_v47_m10_residual_path_cycle_types.py`, the six-unit degree ledger, and the internal heavy-edge graph on the seven outer blocks. They do **not** yet eliminate the 2+8 or 3+7 cells and are not a graph UNSAT certificate.

No retracted degree-nine claim, exceptional-vertex injectivity, Q33 identity, or E407 identity is used. EG617(r=12) remains **OPEN / NOT_CERTIFIED**.


## 6. Exact endpoint-load ledger on the small component

For a small block Q_i and label h, let e_i(h) be the number of extra edges from Q_i to outer blocks whose endpoint in Q_i has label h. In the 2+8 cell, there are eight outer blocks and one extra edge per Q_i--D pair, so `sum_h e_i(h)=8). In the 3+7 cell, `sum_h e_i(h)=7`.

Because the small block has nine other pivot blocks, each q_h has one base neighbor in each of them. Its R-neighborhood is exactly F_h. Therefore in either cell
[
d_H(q_h)=9+e_i(h)+n_h.
]
The minimum-degree contract gives
[
e_i(h)ge 3-n_h.
]
Writing `u_i(h)=e_i(h)-(3-n_h)`, we obtain the exact per-small-block slack totals
[
oxed{sum_h u_i(h)=
egin{cases}
3,&2+8,\
2,&3+7.
end{cases}}
]
Indeed, `sum_h n_h=7`, and the endpoint totals are eight or seven, respectively.

Thus in the 3+7 cell every small block has only two endpoint-load units beyond the mandatory profile `(3-n_h)_{h=1}^4`; in the 2+8 cell it has only three. The fiber-size partitions compatible with seven vertices and four clique fibers are
[
(3,3,1,0), (3,2,2,0), (3,2,1,1), (2,2,2,1).
]
This is the next exact integer ledger to combine with the outer-vertex cap `k(q)<=3-n_h`. In a 3+7 synchronized switch block, the three extra-edge endpoints all have the same small-block label s; the duplicated common track is s and necessarily has `n_s<=1`. If `n_s=1`, the unique vertex of F_s has two neighbors in that outer block, spending one of its `b_r=2-d_R(r)` extra-incidence units, so the number of switch blocks using s is at most `2-d_R(r)`.
