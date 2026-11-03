# Independent h13 q29/q30 COVER audit

Frozen theorem snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

Audit branch: `workstream/r12-astra-independent-audit-20261102`.

## Conclusion

The h13 q29/q30 argument is analytically coherent under the stated hereditary T61 contract. This pass found no concrete counterexample or fatal inequality defect. It did identify several compressed transitions in the q30 classification; the derivations are expanded below so the proof can be made easier to referee. The independent arithmetic checker passed, but it does not replace the graph-theoretic proof or Lean kernel verification.

## 1. q>=29 gate and q29 promotion

The energy-independent q>=29 result is the combination of:
- the embedded R(3,36) exclusion, giving every actual 47-core minimum degree at least11;
- the degree-11 vertices in each such core forming a clique;
- EDGE12 and the triangle/K4 row-union bounds;
- the 13-shell matching and triangle-free reductions;
- the q<=28 triangle channel exclusion;
- the complete q27/q28 bipartite row/decorations classification and the repeated-row/B1 contradictions.

The q27/q28 finite classification has already been independently reimplemented in this audit lineage: 19,448 row-count vectors per q, with canonical state counts 2 and8, and 81,920 direct subset identities checked. This pass did not rerun that larger enumerator.

For the E407/E408 promotion, a maximizing regular pivot p is essential. If q_p<=29 and e(C)<=288, the 47-core has delta>=12 and EDGE13. Assuming no regular shell vertex of missing degree3..10, put X={a:t_a>=11}. Three points in X force q>=30, so |X|<=2. Regular points outside X have missing degree at most2; EDGE13 prevents edges between two such regular points. The four X cases in Section9 then force a contradiction to z>=22. Hence some regular y has d_M(y) in [3,10], and formula (3) at beta=12 gives q_y>=d(13-d)>=30, contradicting maximality when Q<=29. This closes E407; for E408 it reduces Q<=30 to Q=30.

The beta=12 use in formula (3) requires only delta(C)>=12 for the old core. The new core's delta>=12 is invoked only after q_y>=29 or q_y=30 has bounded its edge count by288 or287, respectively.

## 2. q30 preliminary reductions

Assume E=408 and Q=30 at a maximizing pivot p. Its 47-core has287 edges, so the <=288 gate gives delta(C)>=12 and EDGE13.

### 2.1 K4-freeness

If M contains a K4, its four-point row sum is at least36. Equation (1), q=30 and e_M(K4)=6 force equality: row sum36 and zero outside charge. Each K4 weight is at most12, since the complementary triple has row sum at least24.

There are nine outside points. Because M is K4-free, each has at most2 neighbors in the K4. Since z>=22 and the K4 contributes only6 edges, some outside point y has missing degree2. Its two neighbors S form an M-edge. Equation (1) gives rho=31-t(S), and formula (3) at beta12 gives
[
q_y\ge22+\rho=53-t(S)\ge29.
]
Thus the new core has at most288 edges and minimum degree12. The two inserted vertices have new-core degrees (t_s-e_F(s,D_y)\ge12), so both weights are at least12. The other two K4 vertices have total weight at most12, contradicting EDGE13 on their M-edge. Hence M is K4-free.

### 2.2 The heavy set X

Let X={a:t_a>=11}. Since M is K4-free, equation (1) gives |X|<=3.

- **X empty.** A regular point has weight at most2. EDGE13 therefore forbids any edge incident to a regular point, so all M-edges lie on decorated vertices. There are at most G<=8 such vertices, and Turan gives at most ex(8,K4)=21 edges, below z>=22.
- **X={x}, t_x=11.** A regular outside point cannot meet x: degree1 violates EDGE13, while degree2 would need its other neighbor to have weight at least11, creating a second X point. Thus every edge lies on x and decorated vertices. If x is regular, its M-degree11 cannot be supported by at most8 decorated points. If x is decorated, at most8 decorated vertices support all edges, again giving z<=21.
- **X={x}, t_x>=12.** The other12-set contains a triangle or a 2-matching, since otherwise its matching number is at most1 and it is a star (independence11) or a triangle. A triangle with x gives q>=12+24-5=31. A 2-matching with x gives q>=12+26-8=30. Equality forces a five-set with8 edges and all other eight vertices independent and regular. Their weights are below11, so they can meet only x; each contributes at most one edge. Hence z<=8+8=16, contradiction.
- **|X|=3.** Equation (1) forces three weight-11 points forming a triangle, with the other ten points independent and regular. K4-freeness bounds each outside degree by2; degree1 violates EDGE13. A degree-2 outside point has two weight-11 neighbors, and formula (3) gives q_y>=22+9=31. Thus no outside point can be active, contradicting z>=22.
- **|X|=2.** The other11-set contains an edge uv. The four-set X union {u,v} has at most5 edges by K4-freeness and total weight at least22+13=35. Equality is forced: both X weights are11, (t_u+t_v=13), the four-set is K4 minus one edge, and the other nine vertices are independent and regular. This case is expanded next.

### 2.3 The |X|=2 K4-minus-edge case

Let the two weight-11 points be a,b and the other two be u,v. Since X has exactly two points, (t_u,t_v\le10). Each of u,v has internal missing degree at least2 in the K4-minus-edge, so neither can be a neighbor of a regular outside point of missing degree2: (10+2<13). The nine outside points are regular and, by the no-middle-degree assumption, have missing degree at most2. A degree-1 outside point is impossible because every four-set point has weight at most11. Thus every active outside point has degree2 and must meet both a,b.

If k outside points are active, then
[
z=5+2k\ge22,
]
so k=9. Each of a,b has at least2+9=11 missing neighbors, and its weight is11; hence its internal degree in the four-set is exactly2 and its decoration is zero. In a K4-minus-edge, the two degree-2 vertices are exactly the endpoints of the missing edge, so the missing edge is ab. The other two points u,v have internal degree3, no outside neighbors, and
[
g_u+g_v=t_u+t_v-6=7.
]
Neither decoration is zero, since that would make the corresponding point regular with missing degree3, excluded in this case. This is precisely Family II.

### 2.4 The d=10 regular-pivot branch

For a regular shell point y with d_M(y)=10, formula (3) at beta12 gives q_y>=30. Since Q=30, equality holds; rho=h12=kappa=b=0. Formula (4), with the new-core minimum degree12 now licensed by its 287-edge count, gives m=0. Thus S=N_M(y) is independent in M, the other three shell points B are independent and regular, and t(S)=30.

The new core contains S as a target clique of size10, with no S--D_y edges because b=0. Every s in S has new-core degree (t_s+9\ge12), so (t_s\ge3). Their weights sum to30, hence all ten have weight3. Any active point of B is regular and adjacent to a hub of weight3, so EDGE13 forces its missing degree to be at least10, hence exactly10. Since z>=22, all three B points are active. Therefore M is exactly K_{3,10}, with the ten low weights3 and the three hub weights10: the k=10 case of Family I.

This fills the compressed step in the source that invokes a weight-10 hub.

## 3. Family I elimination

In Family I, K={p} union the ten lows is a target K11. Each v in K has exactly three neighbors T_v outside K, and the q30 shell classification shows T_v is a triangle. The shell at v is bipartite between K minus {v} and T_v. Thus any other K point is adjacent to all or none of T_v, and distinct row triples are disjoint.

If a row class has multiplicity c, a vertex x in its triangle has degree (c+12): c neighbors in K, two in its triangle, and ten in the corresponding core. For a pivot w in another row class j, x lies in C_w and
[
d_{C_w}(x)=(c+12)-c-e_F(x,T_j)=12-e_F(x,T_j)\ge12.
]
Hence (e_F(x,T_j)=0). This explicitly verifies that distinct row triangles are target-anticomplete.

Their multiplicities satisfy (1\le c_i\le3), (sum c_i=11), so their number r is4 or5 (also r<=5 from alpha(F)<=5).

- If r=5, the 35 vertices outside K and the five triangles have total excess5. Each such vertex has no neighbor in K. If it failed to complete one of the five triangles, choosing one nonneighbor from each triangle would give an independent6-set. Thus it completes some triangle. In the corresponding q30 core, its degree is (d_F(x)-3\ge12), so (d_F(x)\ge15) and its excess is at least2. This would require at least70 excess, contradiction.
- If r=4, the 38 remaining vertices have total excess2, so at least36 are regular. Each regular remainder vertex has at most one neighbor in each row triangle, by the same core-degree inequality. Any two nonadjacent regular remainder vertices, together with one point from each of the four triangles avoiding both, form an independent6-set. Hence the at least36 regular remainder vertices form a clique, contradicting omega(F)<=11.

Family I is impossible.

## 4. Family II elimination

In Family II, let K consist of p and the nine ordinary lows; it is a target K10. The two globally decorated points u,v are adjacent to every K point but are nonadjacent to each other. Each v_i in K has exactly two further neighbors T_i.

For an ordinary low y, its two missing neighbors are the hubs of weight11, and the remaining shell has one uv edge plus total decoration7, so rho=8. Formula (3) at beta12 gives
[
q_y=22+8+h_{12}+\kappa+b\ge30.
]
Maximality forces equality; in particular kappa=0, so T_y is an edge, and its new core has minimum degree12. T_p is also the original hub edge. Every K point therefore has q=30, and the q30 classification applies at each one. Family I is already excluded, so each view is Family II. Since u,v are the only globally decorated points, they are the two exceptional lows in every view; the other nine K points are ordinary lows. Consequently T_i is the pair of regular hubs in the view at v_i.

Each x in T_i has degree13, is adjacent to v_i alone in K, and is nonadjacent to u,v. The pairs T_i are disjoint: otherwise a hub in the view at v_i would also be adjacent to another K point, contrary to the Family II shell form. For i≠j, x in T_i is nonadjacent to v_j and lies in the q30 core C_j. Its core degree is
[
d_{C_j}(x)=13-1-e_F(x,T_j)\ge12,
]
so e_F(x,T_j)=0. Thus the ten pairs are pairwise anticomplete. Choosing one vertex from each pair gives an independent10-set, contradicting alpha(F)<=5.

## 5. Independent finite arithmetic check

`RECHECK_H13_Q30_ARITHMETIC.py` passed:
- all six possible missing-edge placements in K4 minus one edge have degree pattern (2,2,3,3);
- the d=10 branch forces the K3,10 state;
- the |X|=2 branch forces nine active outside points, two regular hubs of missing degree11, and two exceptional lows with decorations summing7;
- the Family I row-class multiplicity partitions are exhausted for r=4,5;
- all four E=407/408 excess rows used in the Family I contradiction pass;
- ten disjoint pair classes yield an independent transversal of size10.

This script checks arithmetic and finite patterns only. It does not prove EDGE13, the shell classification, row-class compatibility, the core-degree gates, or the external AES theorem.

## 6. Audit disposition

No concrete counterexample was found in the h13 q29/q30 chain. The compressed d=10 and |X|=2 transitions now have explicit derivations, and the Family I cross-row core-degree calculation is stated with all removed K-neighbors accounted for. The finite checker is supplemental.

Still open as certification tasks:
- a complete clean-room execution of the root verifier and exact environment/hash receipt;
- exact theorem-ledger crosswalk for every external leaf;
- Lean kernel certification of the original K145 theorem;
- independent expert/referee review of the complete proof.

This audit does not claim all-r Erdős 617, nor proof-assistant certification.


## 7. Cross-reference correction in the 13-shell matching lemma

The separate h=13 matching lemma used by the frontend recurrence (COVER Section4) says a mixed König cover, with one vertex in the four matched endpoints and one in the unmatched nine-set, supports at most12 cross edges. The general upper bound is13: the two cover vertices can have disjoint incident-edge sets of sizes9 and4 if they are not adjacent. If they are adjacent, the bound is12.

This does not change the lemma. Adding all six possible edges among the four matched endpoints gives at most19<22, still contradicting z>=22. The other cover types remain bounded by8 (two unmatched points) or are the two matched endpoints, which is the only case that can support the required at least16 cross edges. The subsequent two-disjoint-cross-edges argument is unchanged. This is a harmless proof-text correction, not a counterexample to the h13 terminal theorem.


## 7.1 Correction: the original mixed König-cover bound of 12 is valid

The preceding subsection's claim that the source bound12 should be corrected to13 was itself an overcount and is withdrawn.

Let S be the four matched endpoints and I the nine unmatched vertices. If a vertex cover of the bipartite cross graph consists of s in S and i in I:
- if si is an edge, the union of edges incident to s or i has size at most 9+4-1=12;
- if si is not an edge, s has at most8 neighbors in I and i at most3 neighbors in S, giving at most11.

Thus the source's upper bound12 is correct. The earlier attempted bound13 incorrectly counted the absent si edge in both degrees. The proof remains valid as written: 12+6=18<22 (and the weaker bound13+6=19<22 would also suffice). No correction to the frozen COVER Section4 is required for this subcase.
