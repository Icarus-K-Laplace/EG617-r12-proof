# E407 Q32 — delta=12 four-partite U exact support kernel

Date: 2026-10-27  
Status: **PROVED strict reduction** under the frozen 49-support/core contract. No external Didin input is used. This does not yet exclude the delta=12 four-partite branch.

## 1. Contract

Assume
\[
\delta=12,
\qquad e(L_U)=306,
\qquad L_U=\overline{H[U]}
\]
is four-partite.

The 49 selected support blocks are pairwise edge-disjoint K4s in L_U, seven per exact colour, with the seven blocks of a fixed colour vertex-disjoint.

Write the four part sizes in nondecreasing order
\[
a\le b\le c\le d,
\qquad a+b+c+d=29.
\]

Every K4 in a four-partite graph uses exactly one vertex from each part. Since the 49 support K4s are edge-disjoint, for every pair of parts their 49 induced support-pairs are distinct. Therefore
\[
ab,ac,ad,bc,bd,cd\ge49.
\tag{1.1}
\]

Also the complete four-partite graph on these parts must have at least 306 edges.

## 2. The part sizes are forced to (7,7,7,8)

The integer conditions
\[
a+b+c+d=29,
\qquad \min_{i<j}a_i a_j\ge49,
\qquad \sum_{i<j}a_i a_j\ge306
\]
have the unique solution
\[
\boxed{(a,b,c,d)=(7,7,7,8).}
\tag{2.1}
\]

The complete four-partite graph with these parts has
\[
3\cdot7\cdot7+3\cdot7\cdot8=315
\]
edges. Since L_U has 306 edges, exactly nine cross pairs are missing from L_U, equivalently H[U] has exactly nine target edges between distinct parts.

Let
\[
T_1,T_2,T_3,R
\]
be the parts, with `|T_i|=7` and `|R|=8`.

Inside H[U], each T_i is a K7 and R is a K8.

## 3. No target cross edge can join two T-parts

For any pair `T_i,T_j`, there are exactly
\[
|T_i||T_j|=49
\]
possible cross pairs. The 49 support K4s contribute 49 distinct `T_i-T_j` pairs, all of which are edges of L_U. Hence they exhaust the complete bipartite pair set.

Therefore
\[
\boxed{E_H(T_i,T_j)=\varnothing\quad(i\ne j).}
\tag{3.1}
\]

All nine target cross edges of H[U] lie between R and one of the T_i.

## 4. Every exact colour omits one R-point and no T-point

Fix one exact colour. Its seven selected support K4s are vertex-disjoint. Every support K4 uses one vertex from each of the four parts.

Seven disjoint blocks therefore use all seven vertices of each T_i, and exactly seven of the eight vertices of R. Thus the unique omitted U-point of that colour lies in R.

Consequently, with `r_u` denoting the number of exact colour classes omitting u,
\[
\boxed{r_u=0\quad\text{for all }u\in T_1\cup T_2\cup T_3,}
\tag{4.1}
\]
while
\[
\boxed{\sum_{r\in R}r_r=7.}
\tag{4.2}
\]
In particular at least one point `r0 in R` satisfies `r_{r0}=0`.

## 5. Three exact 7x8 leave graphs

Fix i in {1,2,3}. Across all 49 support K4s, the selected `T_i-R` pairs are distinct. Since there are 49 support blocks, they occupy 49 of the 56 pairs of `T_i x R`.

Thus exactly seven `T_i-R` pairs are not support pairs. Call these the leave graph `Lambda_i`.

Every vertex of T_i lies in all seven exact colours by (4.1), once in one block of each colour. Hence it is paired through support blocks with seven distinct R-points. Therefore every T_i vertex has exactly one leave neighbour:
\[
\boxed{d_{\Lambda_i}(t)=1\quad(t\in T_i).}
\tag{5.1}
\]

For r in R, it occurs in exactly `7-r_r` colour classes. Hence in each T_i it has exactly `7-r_r` support partners and therefore exactly r_r leave neighbours:
\[
\boxed{d_{\Lambda_i}(r)=r_r\quad(r\in R).}
\tag{5.2}
\]

So each `Lambda_i` is a seven-edge bipartite star forest with left degree sequence `1^7` and the same right degree sequence `(r_r)_{r in R}`. The three leave graphs may differ as edge sets, but share the same R-degree sequence.

Each leave pair is either
- one of the nine target H-edges between T_i and R, or
- one of the twelve additional non-support edges of L_U.

No other T_i-R pair can be a target edge or an additional L-edge: every pair outside the leave graph is already a support edge.

## 6. Pointwise leave identity

For u in U, let `x_u` be the number of non-support L_U edges incident with u, as in the frozen omission-degree identity
\[
d_H(u,W)=5+\epsilon_u-3r_u+x_u.
\]

For t in T_i, let `h_t=d_H(t,R)`. Since t has exactly one leave pair,
\[
\boxed{h_t+x_t=1.}
\tag{6.1}
\]
Thus `h_t in {0,1}` and the unique leave pair of t is target-coloured exactly when h_t=1.

For r in R, let
\[
h_r=d_H(r,T_1\cup T_2\cup T_3).
\]
Across the three leave graphs r has exactly `3r_r` leave incidences, so
\[
\boxed{h_r+x_r=3r_r.}
\tag{6.2}

Globally
\[
\sum_{t\in T_1\cup T_2\cup T_3} h_t
=\sum_{r\in R}h_r=9,
\]
\[
\sum_{t}x_t=21-9=12,
\qquad \sum_{r\in R}x_r=12,
\]
consistent with
\[
\sum_{u\in U}x_u=2\delta=24.
\]

## 7. Exact U-to-W degrees

The internal H[U] degrees are
\[
d_{H[U]}(t)=6+h_t\quad(t\in T_i),
\]
\[
d_{H[U]}(r)=7+h_r\quad(r\in R).
\]
Therefore
\[
\boxed{d_H(t,W)=6+\epsilon_t-h_t\in\{5+\epsilon_t,6+\epsilon_t\},}
\tag{7.1}
\]
\[
\boxed{d_H(r,W)=5+\epsilon_r-h_r.}
\tag{7.2}
\]

For the guaranteed point `r0 in R` with `r_{r0}=0`, equations (6.2) and nonnegativity give
\[
h_{r0}=x_{r0}=0,
\]
so
\[
\boxed{r_0\text{ is target-nonadjacent to every }T_i\text{ vertex and }d_H(r_0,W)=5+\epsilon_{r0}.}
\tag{7.3}
\]

This distinguished universal-support point is a natural anchor for the next common-nonneighbour attack.

## 8. W-side profiles

At delta=12,
\[
e(H[W])=36-\epsilon_U,
\qquad e(\overline{H[W]})=117+\epsilon_U.
\]
For epsilon_U>=2, Brouwer forces the W-complement to be four-partite. The exact W target-clique profiles are recorded in `DELTA12_AUGMENTATION_FRONTIER.md`.

The four-partite-U branch therefore reduces to:

- the exact `(7,7,7,8)` U clique kernel;
- nine target cross edges, all contained in the three seven-edge leave graphs `Lambda_i`;
- common R omission degrees summing to seven;
- the exact pointwise W-degree equations (7.1)-(7.3);
- the global four-unit degree-excess budget.

This is a finite-design/full-core compatibility problem, not a generic four-partite Turan problem.

No delta=12 closure is claimed yet.
