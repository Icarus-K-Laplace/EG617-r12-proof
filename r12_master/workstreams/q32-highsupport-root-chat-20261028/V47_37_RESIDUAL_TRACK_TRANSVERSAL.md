# E408 Q32 full support — residual vertices must contain a complete outer track in the 3+7 cell

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL structural theorem with exact integer regression.** No full-support Q32 closure claimed.

## 1. Contract

Work in the m=10 disconnected 3+7 cell. By `V47_37_OUTER_LIGHT_HOLONOMY.md`, the seven outer blocks are globally aligned into four tracks
`T_h={q_{i,h}: i in T}`, h=1,2,3,4, each inducing a K7. The only edges between distinct tracks are the additional cross-track edges, whose total number is
`x_T=3+z<=7`.

For every outer block i, the weighted internal-heavy degree is at most two. Hence every outer vertex q_{i,h} has at most two cross-track neighbors: the number of extra edges incident to block i is at most `t_i^T<=2`. Therefore the cross-track graph has maximum degree at most two.

For a residual vertex r in R, let
`b_r=sum_i (|N_H(r) intersect Q_i|-1)`.
The three small blocks have zero Q-R slack, and the degree ledger gives
`d_R(r)+b_r=2`.
Thus r has exactly one neighbor in each of the seven outer blocks plus b_r extra outer incidences, with `b_r<=2`. Its total number of neighbors in the 28 outer vertices is at most nine.

## 2. Independent-transversal lemma

Let four disjoint parts P_1,...,P_4 have sizes
`a_h in {1,...,7}`, with `sum_h a_h>=19`. Let X be a simple graph on their union such that:

- every edge of X joins different parts;
- `Delta(X)<=2`;
- `e(X)<=7`.

Then X has an independent transversal: one vertex from each part, with no X-edge among the four chosen vertices.

### Proof by a strict union bound

There are
`P=product_h a_h`
transversals. An edge between parts i,j forbids exactly
`product_{k not in {i,j}} a_k`
transversals. Thus the number of forbidden transversals is at most the sum of these weights over all edges.

Let x_ij count edges between parts i,j. The hypotheses imply the necessary integer constraints
`sum_{i<j} x_ij<=7`,
`sum_{j!=i} x_ij<=2a_i`,
and
`0<=x_ij<=min(a_i a_j,2a_i,2a_j,7)`.

For each sorted profile `7>=a_1>=a_2>=a_3>=a_4>=1` with sum at least 19, maximize
`B=sum_{i<j} x_ij product_{k not in {i,j}} a_k`
over this relaxed integer system. The relaxation can only overestimate the forbidden-transversal count, because it forgets vertex-level degree constraints beyond their part sums.

There are exactly 64 such sorted profiles. Exact integer enumeration gives
`B < P` for every profile; the minimum margin `P-B` is 63, attained at profile `(7,7,4,1)`, where `P=196` and `B=133`. Therefore fewer than P transversals are forbidden, so at least one independent transversal exists. QED.

## 3. Application to the 3+7 outer tracks

Fix r in R. For each track h, let
`A_h={q in T_h : qr is not an H-edge}`,
and put `a_h=|A_h|`.

If all four a_h were positive, then
`sum_h a_h = 28 - |N_H(r) intersect Q_T| >= 28-(7+b_r)>=19`.
The graph of additional cross-track edges induced on the A_h has maximum degree at most two and at most seven edges. The transversal lemma would give four pairwise nonadjacent vertices, one from each track, all nonadjacent to r. Together with r they form an independent 5-set, contradicting `alpha(H)<=4`.

Consequently at least one `a_h=0):

> **For every residual vertex r, there is an outer track T_h such that r is adjacent to all seven vertices of T_h.**

Equivalently, every residual vertex extends one of the four aligned outer K7 tracks to a K8.

Since r has at most two extra Q-R incidences, at least five of the seven outer blocks have exactly one r-neighbor, and that unique neighbor lies in the same track T_h. If `d_R(r)=2`, then `b_r=0` and all seven outer-block neighbors of r are exactly the vertices of T_h.

## 4. Exact integer verifier

The companion script `verify_v47_37_residual_track_transversal.py` enumerates all 64 sorted part-size profiles and every feasible relaxed six-variable edge-count allocation `(x_ij)` under the total-edge and per-part degree constraints. It checks that the maximum union-bound count is strictly smaller than `product(a_h)` for every profile.

Expected result:
- profiles checked: 64;
- minimum `P-B`: 63 at `(7,7,4,1)`;
- output: `V47_37_RESIDUAL_TRACK_TRANSVERSAL_OK`.

This verifies the finite integer inequality used in the proof. It does not enumerate the 47-vertex graph or prove global Q32 infeasibility.

## 5. Scope and next implication

This strengthens the 3+7 normal form: not only are the outer blocks four globally aligned K7 tracks, but every residual vertex must be complete to at least one whole track. The next step is to couple these track assignments with the common residual-neighbor map of the three small blocks, the 4,5,5 switch types, and the residual degree sequence.

The theorem does not yet rule out the 3+7 cell. Other m=10 cells and full-support m=8,9 remain open. EG617(r=12) remains **OPEN / NOT_CERTIFIED**.


## 6. Track assignment is a clique partition of R

The complete track in Section 3 is unique: a residual vertex has at most nine neighbors among the outer 28 vertices, so it cannot be adjacent to two disjoint K7 tracks. Let g(r) be its unique track label.

### Lemma 6.1 — vertices assigned to one track are adjacent

Suppose r,s are distinct residual vertices with g(r)=g(s)=h, but rs is a nonedge. Both are adjacent to all seven vertices of T_h. Outside T_h, each has at most two neighbors among the other three tracks, because its total outer-neighborhood has size at most nine. Therefore, in each of the other three tracks, at least
`7-2-2=3`
vertices are nonadjacent to both r and s.

We use a three-part transversal bound. If three parts have sizes a,b,c in {3,...,7}, there are abc transversals. Each of at most seven cross-track edges forbids at most max(a,b,c) transversals, while
`abc >= 9 max(a,b,c) > 7 max(a,b,c)`.
Thus at least one transversal avoids every cross-track edge. Choose such a vertex from each of the three tracks other than T_h, all nonadjacent to r,s. Together with r,s they form an independent 5-set, contradiction.

Hence every fiber `g^{-1}(h)` is a clique in H[R]. Since `Delta(H[R])<=2`, each fiber has size at most three. The seven residual vertices are partitioned into four clique fibers, whose sorted size profile is one of
`(3,3,1,0), (3,2,2,0), (3,2,1,1), (2,2,2,1)`.

These are the same four possible size profiles already obtained for the common small-block map f. The proof does **not** yet show `g=f` up to relabeling; that alignment is the next target.
