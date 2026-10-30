# E408 Q32 m=10, 3+7, z=3 — dual-fiber switch-cost and endpoint-saturation audit

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL local reduction + exact finite enumeration.** This does not close z=3, full-support Q32, or EG617(r=12).

## 1. Contract and scope

Work in the full-support m=10 disconnected 3+7 light-block cell. Let A,B,C be the small light triangle, D_1,...,D_7 the outer blocks, and R the seven residual vertices. The registered ledger is
\[
e(H[R])=6,\qquad \sum_{i=1}^7 y_i=2,\qquad d_R(r)+b_r=2,\qquad \Delta(H[R])\le2.
\]
Let F=(F_0,F_1,F_2,F_3) be the four clique fibers of the common small-triangle residual map, and G=(G_0,G_1,G_2,G_3) the four clique fibers of the globally aligned outer-K7-track assignment. Their sorted profiles belong to
\[
\mathcal P=\{(3,3,1,0),(3,2,2,0),(3,2,1,1),(2,2,2,1)\}.
\]
No equality of the two partitions is assumed.

This audit treats the no-double-track branch. The separate double-track branch remains governed by the existing double-track alpha/fiber filters: a double-track vertex has no R-neighbors, its global G-fiber is empty, and the z=3 residual type is restricted to 2C3+K1 or C3+P4. No double-track case is silently included in the theorem below.

## 2. Per-block incidence-slack inequality

For an outer block D with no double-track vertex, the registered 4,5,5 local normal form says that the four singleton common labels s(q), q in D, are either:
- an aligned permutation of 0,1,2,3; or
- a synchronized switch multiset with one label duplicated and one label omitted.

The four vertices q in D occupy four distinct outer tracks g(q). Define
\[
\eta_D=\sum_{q\in D}|F_{s(q)}\setminus G_{g(q)}|.
\]
Each q is adjacent to all of F_{s(q)} by its singleton common label and to all of G_{g(q)} by track completeness. Hence
\[
d_R(q)\ge |F_{s(q)}\cup G_{g(q)}|
=|G_{g(q)}|+|F_{s(q)}\setminus G_{g(q)}|.
\]
Summing over the four q in D uses every G-fiber once, so
\[
\sum_{q\in D}d_R(q)\ge 7+\eta_D.
\]
By the registered block ledger, \(\sum_{q\in D}d_R(q)=7+y_D\). Therefore
\[
\boxed{y_D\ge\eta_D.}\tag{2.1}
\]
This is the same exact incidence argument as the z=0,1 alignment audit, but it is now used without assuming F=G.

## 3. Exact finite partition-pair enumeration

For fixed labelled partitions F,G, define
\[
c(F,G)=\min_{\mathcal S,\pi}
\sum_{k=1}^4 |F_{s_k}\setminus G_{\pi(k)}|,
\]
where \(\pi\) ranges over all bijections from the four outer-track labels to the four positions, and \(\mathcal S=(s_1,\ldots,s_4)\) ranges over the 13 allowed multisets:
- the one aligned multiset (each small label once);
- the 12 switch multisets (choose a duplicated label s, choose a distinct omitted label j, and use s,s plus the other two labels).

The minimum is exact because all orders of the common labels and all assignments of the four distinct outer tracks are represented by these multisets and the 24 permutations \(\pi\). Every actual no-double-track outer block D satisfies \(\eta_D\ge c(F,G)\).

The verifier enumerates all \(4^7\) labelled maps for each of the six registered residual graphs, retaining exactly the maps whose four fibers are cliques and whose sorted profile belongs to \(\mathcal P\). It then checks every ordered pair (F,G), all 13 multisets, and all 24 outer-track assignments.

| Residual graph R | Labelled F maps | Ordered (F,G) pairs | Exact c(F,G) distribution | Zero-cost mismatches |
|---|---:|---:|---|---:|
| C6 + K1 | 48 | 2,304 | 0: 1,152; 3: 1,152 | 0 |
| 2C3 + K1 | 168 | 28,224 | 0: 7,488; 1: 10,368; 2: 10,368 | 3,456 |
| P7 | 96 | 9,216 | 0: 2,304; 1: 3,456; 2: 2,304; 3: 1,152 | 0 |
| C3 + P4 | 168 | 28,224 | 0: 6,912; 1: 9,792; 2: 9,792; 3: 1,728 | 2,880 |
| C4 + P3 | 96 | 9,216 | 0: 2,304; 1: 2,304; 2: 2,304; 3: 2,304 | 0 |
| C5 + P2 | 120 | 14,400 | 0: 2,880; 1: 5,760; 2: 5,760 | 0 |

Across the six residual types the verifier checks 91,584 ordered labelled partition pairs. There are 16,704 zero-cost pairs with the same unlabelled partition and 6,336 zero-cost pairs with different unlabelled partitions.

The only nontrivial zero-cost profile pairs are:

| R | Small-map profile F | Outer-track profile G | Exact split |
|---|---|---|---|
| 2C3 + K1 | (3,3,1,0) | (3,2,1,1) | one size-three F-fiber splits 2+1 |
| C3 + P4 | (3,2,2,0) | (3,2,1,1) | one size-two F-fiber splits 1+1 |
| C3 + P4 | (3,2,2,0) | (2,2,2,1) | one size-three F-fiber splits 2+1 |

In every nontrivial zero-cost pair:
1. F has exactly one empty fiber F_s;
2. the unique zero-cost local switch duplicates s and omits a single nonempty fiber F_j;
3. the other two nonempty F-fibers are exactly two G-fibers;
4. the two remaining G-fibers are disjoint and partition F_j.

If F has no empty fiber, a zero-cost switch is impossible because the duplicated F_s would have to be contained in two disjoint G-fibers. A zero-cost aligned pattern forces F=G. The finite enumeration verifies that the only different-partition exceptions are the three rows above.

## 4. Five-switch / two-aligned-endpoint theorem

Assume F and G are different and no double-track vertex exists.

For each outer block D, eta_D >= c(F,G)=0. Since F and G differ, an aligned block cannot have eta_D=0; every zero-eta_D block must be the unique synchronized switch described in Section 3: it duplicates the empty small-map fiber F_s and omits the split fiber F_j. Every other local pattern has eta_D>=1.

There are seven outer blocks and
\[
\sum_D y_D=2,\qquad y_D\ge\eta_D.
\]
Therefore at most two blocks can have positive eta_D, so at least five blocks must be zero-eta switches of the same type.

Now use the exact endpoint-load ledger on each small block A_i. Let n_h=|F_h| and let e_i(h) count extra endpoints at label h from A_i to the seven outer blocks. The established degree floor gives
\[
e_i(h)\ge 3-n_h,\qquad \sum_h e_i(h)=7.
\]
Writing u_i(h)=e_i(h)-(3-n_h), we have
\[
\sum_h u_i(h)=7-\sum_h(3-n_h)=7-(12-7)=2.
\]
In the mismatch normal form, F_s is empty, and each zero-cost synchronized switch contributes one extra endpoint at label s in each of the three small blocks. Thus five such switches give e_i(s)>=5. But
\[
e_i(s)\le 3-n_s+2=5.
\]
Consequently exactly five zero-cost switches occur, e_i(s)=5, and u_i(s)=2; all other endpoint-load surpluses vanish: u_i(h)=0 for h!=s.

The two remaining blocks must each have eta_D>=1. Their total incidence excess is at least two, so equality holds throughout:
\[
y_D=\eta_D=1
\]
for each of these two blocks, while the five switch blocks have y_D=0. They cannot be switches: a switch duplicating the empty fiber s would have zero eta, while a switch duplicating any nonempty fiber would require positive endpoint-load surplus at that label, but all surplus has already been consumed at s. Hence the two remaining blocks are aligned.

The outer weighted-heavy graph W has weighted degree 2-y_D at block D. Therefore the two aligned blocks have weighted degree one, and the five switch blocks have weighted degree two. By the exact seven-block heavy-graph catalog, the two degree-one vertices are the endpoints of the unique path component of W.

Each aligned endpoint has eta_D=1. It maps the split F_j to one of its two G-pieces and leaves exactly one vertex unmatched. For a 2+1 split it must map F_j to the size-two piece; for a 1+1 split either choice costs one. No claim is made that the two endpoints choose different pieces.

Conclusion: every no-double-track completion with F!=G has exactly five zero-cost synchronized switches, all duplicating the same empty F-fiber and omitting the same split F-fiber, plus exactly two aligned blocks with y_D=1 at the endpoints of the unique outer-heavy path.

## 5. What remains open

This theorem does not rule out the five-switch/two-endpoint normal form. It does not address the separate double-track branch, the F=G aligned branch, m=10's other light-block components, or full-support m=8,9. The next target is to combine the repeated same-transposition switch pattern with the light-edge matching holonomy and the exact endpoint-label allocation at the two path endpoints.

No retracted degree-nine claim, exceptional-vertex injectivity, Q33 identity, or E407 identity is used. The full-support Q32 terminal and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## 6. Supersession — pointwise partner-fiber blocker

The five-switch/two-aligned-endpoint normal form above is an intermediate necessary form, not the current open target. The new Q32_Z3_SWITCH_PARTNER_DEGREE_BLOCKER.md proves that the q-vertex receiving two extra small-component edges also sees the transposed partner fiber F_j. Its pointwise degree cap forces n_s+n_j<=1, excluding every nontrivial F/G mismatch mode. The no-double-track branch therefore reduces to aligned F=G profile (2,2,2,1). The double-track and aligned-2221 branches remain open.


## 7. Correction — valid residual-degree mismatch closure

The previous Section 6's proposed inference that q adjacent to A_j,B_j must be adjacent to every residual r in F_j is invalid: sharing neighbors does not imply adjacency. The resulting n_s+n_j<=1 mismatch inequality is withdrawn.

The valid replacement is Q32_Z3_MISMATCH_RESIDUAL_DEGREE_CLOSURE.md. It uses the five-switch/two-aligned-endpoint normal form and equality in the incidence-slack inequality to determine exact residual neighborhoods in all seven outer blocks. The 2+1 split forces a K3-fiber vertex to have d_R=0; the 1+1 split forces either d_R=0 in a K2 or an isolated K2 component in C3+P4. Therefore F!=G is impossible. The no-double-track z=3 branch reduces to aligned F=G profile (2,2,2,1). The double-track and aligned-2221 branches remain open.
