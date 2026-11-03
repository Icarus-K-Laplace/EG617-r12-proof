# COVER q<=28 triangle-channel: independent analytic re-derivation

Date: 2026-11-03
Frozen source: `r12_master/workstreams/astra-global-root-integration-chat-20261031/frozen/cover/COVER_THEOREM.md`, Sections 1, 3, 5.
Audit branch: `workstream/r12-astra-independent-audit-20261102`.
Frozen integration: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

## Verdict

**NO FATAL GAP FOUND.** The triangle-channel exclusion in COVER Section 5 is valid under the stated shell contract. This note expands the single-edge and star subcases using a direct total-weight inequality. In particular, the conclusion does not need the source's compressed exact hub-weight assertion in those subcases.

## 1. Setup and edge equality

Let (M) be the 13-vertex missing graph of a regular pivot, with (q\le28), (z=e(M)\ge22), (alpha(M)\le10), and (M) K4-free. Let (T=\{x,y,w\}) be an M-triangle and (B=V(M)\setminus T), so (|B|=10). Put (u=e(M[B])), (G_B=\sum_{b\in B}g_b), and (t_a=d_M(a)+g_a).

The exact subset identity gives
[
u+G_B=q+3-t(T)\le q-21\le7,
]
because (t(T)\ge24).

For any edge (ab\in E(M[B])), K4-freeness gives
[
|N_M(a)\cap T|,|N_M(b)\cap T|\le2,
]
and
[
d_{M[B]}(a)+d_{M[B]}(b)\le u+1.
]
Therefore
[
t_a+t_b\le4+(u+1)+G_B\le12.
]
EDGE12 gives the reverse inequality, so equality holds throughout:
- (q=28), (t(T)=24), and (u+G_B=7);
- both (a,b) have exactly two T-neighbors;
- (d_{M[B]}(a)+d_{M[B]}(b)=u+1), so every B-edge meets ({a,b});
- all B-decoration is supported on the endpoints of every B-edge.

Thus (M[B]) has matching number at most one. Its nontrivial part is a star or a triangle.

## 2. B contains a triangle

If (M[B]) contains a triangle, every B-edge forces all B-decoration onto its two endpoints. Intersecting the endpoint pairs of the three triangle edges gives the empty set, hence (G_B=0). But then (u=3), contradicting (u+G_B=7).

## 3. B contains exactly one edge

Write the unique edge as (ab). The two T-neighborhoods of (a,b) each have size two and intersect in exactly one hub (w); they cannot be equal, since that would create a K4. Write them as ({w,x}) and ({w,y}).

The equality above gives (g_a+g_b=6), so
[
t_a+t_b=(3+g_a)+(3+g_b)=12.
]
All other eight B-vertices are regular. Each of the three hubs has missing degree at least three: two edges inside T and at least one edge to (a) or (b). Since (t(T)=24), every pair of hub weights has sum at most 21.

An outside regular B-vertex cannot have two T-neighbors: those two hubs are adjacent in T, so its INS11 inequality would require their weights to sum to at least 22:
[
t_i+t_j-2\ge2(12-2)=20.
]
It therefore has at most one T-neighbor. If it has one, EDGE12 requires that hub to have weight at least 11. At most one hub can have weight at least 11, because the other two have weight at least three and the three hub weights sum to 24. Thus all such attachments use the same hub.

The eight remaining B-vertices contribute at most eight T-edges. Consequently
[
z\le 3+1+4+8=16,
]
where the terms count the T-triangle, edge (ab), the four T-edges from (a,b), and the remaining eight vertices. This contradicts (z\ge22).

This argument avoids needing to assert exact values for the three hub weights.

## 4. B is a star with at least two edges

Let (a) be its center and (b_i) its leaves. Equality gives
[
g_a=7-k,qquad t_a=9,qquad t_{b_i}=3.
]
The two-element T-neighborhood of each leaf intersects the two-element T-neighborhood of (a) in exactly one hub; equality of the two neighborhoods would create a K4.

All leaves must share the same common hub (w). Otherwise two leaves with different common hubs force all three T-hubs to have weight at least nine, contradicting (t(T)=24). Let (y) be the third hub and (x) the other T-neighbor of (a). Then every leaf has missing neighborhood
[
S=\{a,w,y\}.
]
The induced missing graph on S has exactly two edges, (aw) and (wy), while (ay) is absent. Also (t_x\ge3), since (x) has its two T-edges and the edge to (a). Hence
[
t_w+t_y=24-t_x\le21.
]
For a regular leaf, INS11 requires
[
t(S)-2e_M(S)\ge3(12-3)=27.
]
But
[
t(S)-2e_M(S)
=9+t_w+t_y-4
\le9+21-4=26,
]
a contradiction.

Again, the proof needs only the sum bound (t_w+t_y\le21), not an exact assignment of the individual hub weights.

## 5. B is independent

Here (z=3+e_M(T,B)), so
[
19\le e_M(T,B)\le20.
]
K4-freeness gives each B-vertex at most two T-neighbors. Thus every B-vertex has T-degree one or two, and at most one has degree one.

Every hub must meet a regular degree-two B-vertex:

- A hub with no B-neighbor would join the independent 10-set B to make an independent 11-set.
- If it has a regular degree-one neighbor, that point is unique. All its other B-neighbors must be decorated, so (c_i\le G_B+1) and
  [
  t_i=2+c_i+g_i\le3+G\le9,
  ]
  contradicting EDGE12 on the degree-one edge.
- Otherwise all its B-neighbors are decorated. Choose one such neighbor (b). Then (c_i\le G_B-g_b+1), and
  [
  t_i+t_b\le(2+c_i+g_i)+(2+g_b)
  \le5+G_B+g_i\le5+G\le11,
  ]
  again contradicting EDGE12.

Therefore each hub has an edge to a regular degree-two B-point, forcing each hub weight to be at least ten. Since
[
t(T)=q+3-G_B\le31,
]
the sum of any two hub weights is at most 21. But a regular degree-two B-point has two adjacent hubs as its missing neighborhood, and INS11 requires their weight sum to be at least 22. Contradiction.

## 6. Audit conclusion

All four possibilities for (M[B]) are excluded:
1. a triangle;
2. exactly one edge;
3. a star with at least two edges;
4. no edges.

Thus the q<=28 triangle channel is impossible. The q27/q28 finite bipartite classification is therefore reached only after a valid analytic exclusion of the triangle channel.

This is a focused independent derivation, not a clean-room execution of the entire COVER verifier, Lean certification, or external referee report. No frozen source or sibling workstream is modified.
