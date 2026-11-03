# Independent K145-to-T61 frontend interface audit

Date: 2026-11-03  
Frozen source: `K145_TO_T61_FRONTEND_AUDIT.md`, `RECURRENCE_PROOF.md`, and `FINAL_GLOBAL_PROOF.md` at integration snapshot `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

## Verdict

**NO LOAD-BEARING INTERFACE GAP FOUND.** The original coloring hypothesis is carried through the contextual R(4,49) contradiction, the maximal K12 extraction, the exact edge ledger, and the recurrence without exporting a contextual statement as a generic Ramsey theorem. The unique recurrence survivor has exactly the contract needed by the h12/h13 terminal theorems.

## 1. Original coloring to the least-color graph

For each of the 12 color graphs, every 13-set contains an edge, so its independence number is at most12. Turan applied to its complement gives at least (p_{12}(n)) edges of that color on every n-set. For a least-edge color graph G:
- (e(G)le {145\choose2}/12=870);
- (alpha(G)le12);
- (omega(G)le12);
- every induced set obeys (e(G[U])le D(|U|)).

If (delta(G)ge12), the average-degree bound forces G to be 12-regular. Brooks applies componentwise: (Delta=12), and no component is (K_{13}) because (omega(G)le12). Thus (chi(G)le12), giving an independent color class of size at least (lceil145/12ceil=13), contradiction. Therefore a minimum-degree vertex has degree (dle11). No stronger coloring assumption is inserted.

## 2. Contextual R(4,49) is impossible

Here the contextual class is an induced 49-set F of this same original target graph, with (alpha(F)le4), (omega(F)le11), and all inherited D-caps.

A vertex of degree at most11 leaves at least37 nonneighbors; any such 37-set lies in R(3,37), because an independent 4-set there plus the vertex would give an independent 5-set in F. This is impossible by M5.

If a vertex v has degree12, its 36-point nonneighborhood H lies in R(3,36). M5 gives (e(H)ge234), while (D(36)=234), so equality holds. The 12-neighborhood A cannot be a clique K12, so choose a missing pair a,b in A. If their two H-rows had union at most12, at least24 points of H would be anticomplete to a,b; that 24-set would have independence at most2, contradicting M1. Thus the row union is at least13, and
[
e(F[H\cup\{a,b\}])=e(H)+t_a+t_bge234+13=247>D(38)=241.
]
This contradiction rules out degree12. Hence (delta(F)ge13), and (e(F)gelceil49\cdot13/2\rceil=319).

For each of the other eleven color graphs C on the same 49-set, the original coloring gives (alpha(C)le12). Also (omega(C)le4), since a C-clique of size5 would be an independent 5-set in F. Its complement L is K13-free and not 12-partite: a 12-partition of L would partition C into twelve cliques of size at most4, covering at most48 vertices. Kang–Pikhurko Theorem 1 at (n,r)=(49,12) therefore gives (e(L)le1097), hence (e(C)ge79). The eleven other colors consume at least869 of the 1176 edges, so (e(F)le307<319). This is a contradiction in the original coloring. It proves absence of a contextual R(4,49) only; no generic uncolored R(4,49) assertion is used.

## 3. Maximal K12 extraction and edge ledger

For the minimum-degree vertex v, put A=N(v) and U=V(G)\N[v]. Take a maximal packing of j disjoint target K12s in G[U]. The D(13)=67 cap means a vertex outside a target K12 has at most one neighbor in it: two would give68 edges on13 points. Hence cross edges between any two packed blocks form a matching.

If j were at least12, choose one independent representative from each of twelve blocks greedily; at stage k, at most k-1 vertices in the current block are forbidden by prior representatives. Together with v this is an independent13-set. Thus j≤11. Maximality gives (omega(R)le11) in the residual R. If R had an independent set of size12-j, every block would retain at least j points avoiding it; choose j pairwise nonadjacent block representatives greedily, again obtaining an independent13-set with v. Thus (alpha(R)le11-j), including the j=0 and j=11 boundary cases. All inherited caps remain valid.

The exact partition of edges is also consistent. With (sigma=870-e(G)), (z={d\choose2}-e(G[A])), (g=sum_{a\in A}(d_G(a)-d)), and x,y the block-block and block-residual edge counts, respectively, the degree sum on A gives (e(A,U)=2z+g). Therefore
[
e(R)=870-{d+1\choose2}-66j-(\sigma+z+g+x+y).
]
Every subtracted term is nonnegative. The initial neighborhood is not silently assumed to be a clique.

## 4. Recurrence rules and matching guarantee

For a minimum-degree h pivot in a contextual R(a,n), the missing graph M on its h-neighborhood satisfies (alpha(M)le10). The closed-shell cap gives the charge floors (z=e(M)ge11,22,33) at h=12,13,14, respectively. The matching guarantee
[

u(M)ge max\left(\left\lceil\frac{h-10}{2}\right\rceil,,1+[h\ge12]+[h\ge13]\right)
]
is valid:
- h=11: (alpha(M)le10) forces an edge;
- h=12: a matching-number-one graph is a star or triangle; the star has an independent 11-set and the triangle has only3 edges, contradicting z≥11;
- h=13: if (
u=2), take four matched endpoints S and the unmatched independent 9-set I. The cross graph is bipartite with matching number at most2, so König gives a vertex cover of size2. A cover using one S and one I vertex supports at most12 cross edges; two I vertices support at most8. Thus the cover must be two S vertices. Since z≥22 and e(M[S])≤6, there are at least16 cross edges, yielding two disjoint cross edges on those two S vertices. The other two S vertices cannot be adjacent (that would make a 3-matching), and together with I they form an independent11-set, contradiction. König is used only on this bipartite cross graph, not on M itself;
- h=14: if (
ule2), four matched endpoints and ten unmatched independent vertices remain. The bipartite cross graph has a cover of size2 and hence at most20 edges; adding at most6 endpoint edges gives z≤26<33;
- h≥15: the elementary unmatched-vertex bound (
ugelceil(h-10)/2ceil) already gives at least3.

For t disjoint matching edges, their 2t endpoints give (qge t\beta-{2t\choose2}+p_a(2t)). If M is triangle-free, Mantel gives (qge t\beta-t^2). If M contains a triangle, its three rows give the separate (gamma-3) channel. The two channels are exhaustive; the recurrence takes the minimum of the valid channel bounds, and discards a channel only when its induced-set cap contradicts it. Core terms have smaller a; deletion averaging has smaller n. Thus the induction is acyclic and does not assume the desired terminal theorem.

## 5. Terminal interface

The third integer replay agrees with the stored recurrence at all 1,752 nodes and 144 outer stops. The unique survivor is ((d,j,a,n)=(11,6,5,61)), with (397le e(F)le408), (alpha(F)le5), (omega(F)le11), and all hereditary caps.

A degree at most11 in F would leave a contextual R(4,49) in its nonneighborhood. A minimum degree at least14 would force (e(F)ge427). Therefore (delta(F)in\{12,13\}), exactly the two branches handled by the independent h12 and h13 terminal packages. The proof does not replace “minimum degree13” by “there exists a degree13 vertex”; in the h13 branch all vertices have degree at least13 and the regular pivots are exactly the degree13 vertices.

## Audit boundary

No new mathematical interface gap was identified. This audit is a re-derivation of the analytic interfaces plus a check against the already independently replayed recurrence; it is not a fresh execution of the entire root verifier, a Lean kernel proof, or external peer review. The full EG617(r=12) certification status remains separate.
