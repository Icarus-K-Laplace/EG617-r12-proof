# E408 Q32 full support — global light-holonomy rigidity in the 3+7 cell

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL structural theorem.** It does not close the 3+7 cell or global Q32.

## 1. Frozen 3+7 contract

Use the ten pivot blocks for m=10. In the disconnected light-block component split 3+7, let S be the small light triangle and T the seven-block outer component. The registered reduction gives:

- every pair from S to T has exactly five H-edges;
- every pair inside S is light (exactly a perfect matching);
- for every i in T, its weighted internal-heavy degree is
  `t_i^T = sum_{j in T,j!=i} k_ij <= 2`, where `k_ij=e_H(Q_i,Q_j)-4`;
- `x_T=sum_{i<j in T} k_ij=3+z<=7`;
- the light graph L[T], with ij light iff `k_ij=0`, has minimum degree at least four.

Thus the heavy-pair graph on T has weighted maximum degree two, and every pair of outer blocks has at most six H-edges.

## 2. Triangle consistency

Every light pair is exactly a perfect matching. If A,B,C form a light triangle, the two-light matching-composition theorem forces the matching on A-C to be the composition of the matchings on A-B and B-C. Consequently every light triangle has identity holonomy.

For any four-cycle of light pairs, the two-light composition theorem forces both path matchings into each diagonal pair. Each diagonal has at most six edges. The union of two distinct perfect matchings has at least six edges, with equality only when their relative permutation is a transposition. Therefore four-cycle holonomy is either identity or a transposition; if it is a transposition, both diagonals have exactly six edges, so both have weight k=2.

But a k=2 pair saturates the internal-heavy degree budget at both endpoints. Hence if a four-cycle had transposition holonomy, each of its four vertices would be light-adjacent to every block outside the cycle. Choose any external block E in T. The four cycle edges and the four edges to E form four light triangles. Triangle consistency through E forces the cycle holonomy to be identity, contradiction.

Therefore **every light four-cycle has identity holonomy** in the 3+7 cell.

## 3. Every light cycle has identity holonomy

We prove this by induction on cycle length.

- Length 3: triangle consistency.
- Length 4: Section 2.
- Length 5: if there is a light chord, it splits the cycle into a triangle and a four-cycle, both with identity holonomy. If there is no light chord, each cycle vertex has two heavy neighbors among the other five cycle vertices. Those two heavy edges already use its full weighted-heavy degree budget two, so every pair from the cycle to either of the two outside vertices is light. Either outside vertex is then a common light hub; the five cycle-edge matchings all factor through that hub, giving identity holonomy.
- Length 6 or 7: a chord must exist, since a chordless cycle would give each vertex at least three or four heavy neighbors, exceeding the weighted-heavy degree cap two. A chord splits the cycle into shorter cycles; by induction both subcycles have identity holonomy, hence so does the original cycle.

Thus every cycle of L[T] has identity holonomy.

## 4. Global alignment and four K7 tracks

The light graph L[T] is connected because it has seven vertices and minimum degree at least four. Since every cycle has identity holonomy, one may relabel the four vertices in each outer block so that every light-edge matching is the identity matching.

Now take any heavy pair i,j in T. Since each of i,j has at least four light neighbors among the other six vertices, their light neighborhoods have at least
`4+4-5=3`
common vertices. Pick a common light neighbor k. The two-light composition theorem forces the composed matching along i-k-j into H[Q_i,Q_j]. Under the global alignment this is the identity matching. Hence every pair of outer blocks, light or heavy, contains the same aligned four-edge matching.

Therefore the 28 vertices in the seven outer blocks contain four vertex-disjoint cliques of size seven:
`T_h={q_{i,h}: i in T}`, for h=1,2,3,4.

All remaining Q-Q edges inside T are cross-track edges, and their total number is exactly the heavy slack
`x_T=3+z<=7`.

> **New normal form:** in the 3+7 cell, the induced graph on the 28 outer-block vertices contains four aligned K7 tracks, with at most seven additional cross-track edges.

## 5. Exact combinatorial regression

The companion verifier enumerates all weighted heavy graphs on seven labels with edge weights k in {0,1,2}, weighted degree at most two at every label, and total weight at most seven. It checks:
- every resulting light graph has minimum degree at least four;
- every chordless five-cycle has both outside vertices light-adjacent to all five cycle vertices;
- every six- or seven-cycle has a light chord;
- the saturation condition for any weight-two diagonal pair of a four-cycle.

The exact enumeration covers 22,054 weighted heavy graphs and checks 5,803,387 light cycles across lengths 3 through 7. The verifier returns `V47_37_LIGHT_GRAPH_CYCLE_DECOMPOSITION_OK`.

This regression checks the finite heavy-graph combinatorics used in the cycle-decomposition proof. The matching-holonomy steps are proved analytically in Sections 2–4 and rely on the registered two-light composition theorem.

## 6. Scope firewall

No external extremal theorem, retracted degree-nine premise, exceptional-vertex injectivity, Q33 identity, or E407 identity is used. The result applies only after entering the registered m=10 disconnected 3+7 cell.

It does not exclude that cell: four K7 tracks plus at most seven cross-track edges remain compatible with the scalar edge ledger. Full-support Q32 m=10 remains OPEN, as do m=8 and m=9. EG617(r=12) remains **OPEN / NOT_CERTIFIED**.
