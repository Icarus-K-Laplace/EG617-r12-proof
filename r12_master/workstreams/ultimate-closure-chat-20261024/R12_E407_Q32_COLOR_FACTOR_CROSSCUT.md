# E407 Q32 — Exact-129 color-factor witness crosscut

Date: 2026-10-25  
Status: PROVED_CONDITIONAL on the retained E407 Q32 shell contract and the Kang–Pikhurko exact extremal classification for 129-edge non-target colors. This is a stronger necessary condition, not a closure of the five templates.

## 1. Contract

Let F be a hypothetical E407 Q32 residual: |V(F)|=61, e(F)=407, pivot p, shell A=S∪B with |S|=3, |B|=10, and core H with |H|=47, e(H)=284, alpha(H)<=4, delta(H)>=12, and total core excess sum_{v in H}(d_H(v)-12)=4. The retained parent contract also has alpha(F)<=5.

For the five V12 templates, M[B] is empty; every b in B is regular and its target-neighborhood into H has size k_b=d_M(b) in {0,1,2,3}. The exact color-factor argument below is applied only to templates A and C, whose row types have k_b in {0,1,3}.

Since the other 11 colors each have at least 129 edges on the 61 vertices,
\[
\sum_{j=1}^{11}(e(C_j)-129)=1830-407-11\cdot129=4.
\]
Thus at least seven non-target colors have exactly 129 edges.

For each such exact-129 color C, the hypothetical counterexample gives alpha(C)<=12, while alpha(F)<=5 gives omega(C)<=5. The retained Kang–Pikhurko Type-I equality classification therefore gives ten isolated K5 components and an 11-vertex exceptional gadget U. Every K5 component has all its edges in color C, hence is an independent set in the target graph F.

## 2. At least seven core independent 4-sets per exact-129 color

In template A, F[S] is a clique, so each K5 component contains at most one vertex of S. At most three of the ten components meet S, leaving at least seven components disjoint from S.

In template C, M[S] is a single edge. Only the two endpoints of that missing edge can coexist in a C-colored clique; the third hub is target-adjacent to both. Therefore the three vertices of S occupy at most two K5 components, leaving at least eight components disjoint from S.

Each component disjoint from S supplies an independent 4-set Q subset H: if the component contains a vertex of B or the pivot p, take its other four vertices; if it contains neither, take any four of its five core vertices. It cannot contain two vertices of B, since F[B] is a clique, and it cannot contain both p and a shell vertex, since p is target-adjacent to the shell.

Consequently each exact-129 color supplies at least seven pairwise-disjoint independent 4-sets in H for template A, and at least eight for template C.

## 3. Defect budget forces hub-complete witnesses

Call an independent 4-set Q subset H hub-complete if it has a target edge to each of the three hubs in S.

If Q misses a hub s in S, then it must hit every b in B with sb in M; otherwise Q∪{s,b} is an independent 6-set in F, contradicting alpha(F)<=5.

Let n0,n1,n3 be the counts of B-rows with k_b=0,1,3. For templates A and C, respectively,
\[
n_0+n_1+n_3=10,\qquad
3n_0+2n_1\le8\quad(A),\qquad
3n_0+2n_1\le9\quad(C).
\]
In both cases n3>=6 and n1<=4<n3. Every hub is missing from all n3 full rows. Hence a non-hub-complete Q hits at least n3 distinct B-rows and therefore accounts for at least n3 target edges between B and H.

Within one color, the Q sets selected from different K5 components are disjoint, so their B-H target edges are disjoint. The total B-H target-edge budget is
\[
c_S=\sum_{b\in B}k_b=3n_3+n_1<4n_3.
\]
Thus at most three of the no-S component witnesses can fail to be hub-complete.

**Conclusion.**
- Template A: each exact-129 color supplies at least 7-3=4 hub-complete independent 4-sets.
- Template C: each exact-129 color supplies at least 8-3=5 hub-complete independent 4-sets.

As there are at least seven exact-129 colors, the respective global lower bounds are 28 hub-complete sets for A and 35 for C.

## 4. Cross-color linearity and Hall matching

Any two selected Q subsets H from distinct exact-129 colors intersect in at most one vertex: otherwise the edge between two common vertices would be assigned two colors. Within one color, the selected sets are disjoint. Thus the full family is a linear 4-uniform set system.

More is true. If Q,Q' are independent 4-sets in a graph H with alpha(H)<=4 and |Q∩Q'|<=1, then the bipartite graph H[Q\\Q',Q'\\Q] has a perfect matching.

**Proof.** Put r=|Q∩Q'| in {0,1}; both exclusive parts have size 4-r. If Hall fails for X subset Q\\Q', then there are more than 4-r-|X| vertices Y subset Q'\\Q with no H-edge to X. Since each of Q,Q' is independent, X∪Y is independent. If r=1, the common vertex is also nonadjacent to all of X∪Y. In either case this constructs an independent set of size at least five, contradiction. Hall's theorem gives the perfect matching. QED.

Thus each pair of disjoint witness blocks forces at least four core edges between them; a pair intersecting once forces a perfect matching between the remaining triples, hence at least three core edges.

## 5. What this does and does not prove

This sharpens the earlier “hub-complete or high-B-degree” dichotomy: A/C cannot place more than three of the seven/eight available exact-color component witnesses in the high-B-degree branch. The surviving system must contain at least 28/35 hub-complete independent 4-sets with pairwise-linear intersections and pairwise Hall-matching constraints.

It does not yet contradict e(H)=284, the degree sequence with total excess four, or the 13-row shell capacities. Cross-pair edges can be reused by witness pairs from different colors; a valid next step must bound this reuse or classify the resulting incidence kernel. Templates B, D, and E are not covered by the hub-complete count above.

Dependencies: V12's finite E407 shell reduction; retained D(14)/template row contracts; Kang–Pikhurko Type-I exact-129 classification. No residual-core, three-anchor, or repivot theorem from sibling workstreams is used.
