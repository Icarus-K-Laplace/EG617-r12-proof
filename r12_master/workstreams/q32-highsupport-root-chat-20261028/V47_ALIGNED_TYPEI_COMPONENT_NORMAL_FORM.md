# E408 Q32 — Type-I color components under the aligned 3+7 low-z normal form

Date: 2026-10-29  
Status: **PROVED_CONDITIONAL structural theorem.** This narrows the exact-color placement types in the aligned z=0,1 cell; it does not close that cell.

## 1. Frozen graph contract

Assume the m=10, disconnected 3+7 branch with z in {0,1}, after the registered track-alignment theorem and the K13 exclusion. The only remaining residual profile is
`(2,2,2,1)`, and the small-map fibers agree with the outer-track fibers.

For each of the three size-two fibers F_h, let X_h=T_h union F_h, where T_h is its aligned ten-vertex pivot track. Then X_1,X_2,X_3 are target-color K12 cliques. The singleton fiber together with its ten-vertex track is a target-color K11 clique X_0. These four cliques partition H.

Consequently, for every non-target color C:
- if v is in one of X_1,X_2,X_3, then C has at least one edge from v to each of the other two K12 cliques, so d_C(v,H)>=2;
- if v is in X_0, then C has at least one edge from v to each of the three K12 cliques, so d_C(v,H)>=3.

This uses only the frozen balanced-coloring premise: every 13-set contains all twelve colors.

## 2. Triple-outside Type-I placement is impossible

For an exact Type-I color C, its graph on H union O is the registered disjoint union of ten K5 components and an 11-vertex gadget G11. Distinct components have no C-edges between them.

In the registered triple placement, one K5 has three vertices in O and only two vertices in H. Each of those two H vertices has exactly one C-neighbor in H: the other H vertex of that K5. This contradicts the pointwise lower bound d_C(v,H)>=2 for every v in H from Section 1.

Therefore:

> **No exact color can use the triple-outside K5 placement in the aligned low-z 3+7 cell.**

A double-outside K5 has three H vertices and two O vertices. Each of its H vertices has exactly two C-neighbors in H, so none can lie in X_0, where d_C(v,H)>=3. Since H vertices in the same X_h are target-adjacent and hence cannot be joined by C-edges, the three H vertices of every double-outside K5 must be one vertex from each of X_1,X_2,X_3.

Every single-outside K5 has four H vertices. They form an independent four-set in the target graph H. Because H is partitioned into the four target cliques X_0,X_1,X_2,X_3, the K5 contains exactly one H vertex from each of these four parts.

Thus the only surviving exact-color placements are:
1. x_C in O, with one double-outside K5 and nine single-outside K5s;
2. x_C in H, with two double-outside K5s and eight single-outside K5s.

## 3. Exact gadget part sizes and edge accounting

The component counts force the H/O composition of G11.

### Case A: x_C in O

The nine single-outside K5s use nine H vertices from each X_h and one O vertex each. The unique double-outside K5 uses one H vertex from each of X_1,X_2,X_3 and two O vertices, and none from X_0.

Hence G11 contains:
- two H vertices from each of X_1,X_2,X_3;
- two H vertices from X_0;
- three O vertices.

Its H-H edge contribution from the ten K5 components is
`9 binom(4,2)+binom(3,2)=57`.
If `g_C=e_C(H)-69`, then
`e_C(H intersect G11)=12+g_C`.
The registered source-correct cap `g_C<=4` gives
`12 <= e_C(H intersect G11) <= 16`.

The lower bound 12 also follows pairwise from the color-cover condition: at least two G11 edges are needed between each pair of K12 parts, and at least two between X_0 and each K12 part.

### Case B: x_C in H, two-double placement

The eight single-outside K5s use eight H vertices from every X_h. The two double-outside K5s each use one H vertex from each of X_1,X_2,X_3 and none from X_0.

Hence G11 contains:
- two H vertices from each of X_1,X_2,X_3;
- three H vertices from X_0;
- two O vertices.

The ten K5 components contribute
`8 binom(4,2)+2 binom(3,2)=54`
H-H edges. Therefore
`e_C(H intersect G11)=15+g_C`.
The registered source-correct cap `g_C<=5` gives
`15 <= e_C(H intersect G11) <= 20`.

The lower bound 15 follows because the G11 H-edges must include at least two edges between each pair of K12 parts (six total) and at least three edges from X_0's three remaining vertices to each K12 part (nine total).

## 4. Consequence and boundary

For every exact color in this aligned low-z cell, the 11-point gadget's H-H edge count is now tied exactly to its near-Turan gap:
- x_C in O: `h_C=12+g_C`, with `g_C<=4`;
- x_C in H, two-double: `h_C=15+g_C`, with `g_C<=5`.

This eliminates the triple-placement row and gives a part-by-part interpretation of the remaining color gap. The two remaining placement types are not individually contradictory, and this theorem does not close z=0 or z=1. No retracted degree-nine premise is used; full-support Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
