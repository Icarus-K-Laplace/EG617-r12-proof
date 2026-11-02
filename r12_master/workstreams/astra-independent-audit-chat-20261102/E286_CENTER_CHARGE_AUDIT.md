# E286 center-charge derivations: formula (3), formula (4), and star support

Frozen theorem snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.

This note makes explicit the shared-center accounting used in E286 Sections6 and8. It is a derivation from the support/blocker setup, not a change to the frozen theorem.

## 1. Two mixed points on a K9 with two K9-completers

Let (X=K_0) have size9. Let (z,z') be mixed points supported on (K_0,K_2) and (K_0,K_3), respectively. Let
[
A=X\setminus N(z),\quad B=K_2\setminus N(z),\quad
A'=X\setminus N(z'),\quad B'=K_3\setminus N(z').
]
All four sets are nonempty; in particular (b'=|B'|\ge1), because a point cannot complete a K11. Suppose two further points (w_1,w_2) both complete (X).

For each (x\in A):
- it has 8 neighbors inside (X);
- it is adjacent to (w_1,w_2);
- it is adjacent to every vertex of (B), by the blocker-completeness lemma;
- if (x\notin A'), it is adjacent to (z');
- if (x\in A'), it is adjacent to every vertex of (B'), so it has at least one such neighbor.

Thus (d(x)\ge 8+2+b+1=11+b), and
[
\epsilon(x)\ge\max(0,b-1).
]
For each (y\in B), the internal K11 degree10 and the forced complete adjacency to A give (d(y)\ge10+a), hence
[
\epsilon(y)\ge\max(0,a-2).
]
Finally, (z) has at least (9-a+11-b=20-a-b) neighbors in (X\cup K_2), so
[
\epsilon(z)\ge\max(0,8-a-b).
]
The three charged sets ({z},A,B) are disjoint. Therefore
[
\epsilon(z)+\sum_{x\in A}\epsilon(x)+\sum_{y\in B}\epsilon(y)
\ge
\max(0,8-a-b)+a(b-1)+b\max(0,a-2).
]
The right side is at least5 by the scalar inequality (4). This explicitly justifies the h=5, 9/11 case when the two other 01 points complete K9.

## 2. Three mixed points on a K10 star

Let (X=K_0) have size10, and let (z_i) be supported on (K_0,K_i), (i=1,2,3), with distinct K11 leaves. For each i write (A_i=X\setminus N(z_i)), (B_i=K_i\setminus N(z_i)). Every (B_i) is nonempty.

For a vertex (x\in X) missing a subset (S\subseteq\{z_1,z_2,z_3\}), the blocker-completeness lemma forces x adjacent to every (B_i) for (i\in S). It is also adjacent to all (3-|S|) other star points. Hence
[
d(x)\ge9+(3-|S|)+\sum_{i\in S}|B_i|
=12+\sum_{i\in S}(|B_i|-1).
]
Consequently the K10-center excess dominates the sum of all three individual K10 terms ( |A_i|\max(0,|B_i|-3)). The opposite K11 charges lie in three distinct cliques, and the three point charges are distinct, so the three scalar charges can be added without double-counting.

If exactly one (A_i) is nonempty, the other two points complete K10. The scalar bound is
[
\max(0,9-a-b)+a(b-1)+b\max(0,a-2)\ge6.
]
The two K10-completing points are nonadjacent (otherwise they and K10 form K12), so their common neighborhood has size at least10. The common-neighbor bound gives their combined excess at least7. These charges are disjoint, for a total at least13.

If all three (A_i) are empty, all three points complete K10. They are pairwise nonadjacent, and each pair has combined excess at least7. Summing the three pair inequalities gives total point excess at least (\lceil21/2\rceil=11).

If at least two (A_i) are nonempty, each corresponding mixed blocker costs at least4. Under total budget (T\le8), exactly two could only occur at equality: both missing pairs must be ((a,b)=(2,3)), all eight excess units are concentrated on the two points, and all clique vertices have zero excess. The third point must complete K10 (it cannot complete its K11). But any vertex in either two-point K10 missing set then has internal degree9, is adjacent to the third point and the other mixed point if it is not missing it, and has three forced neighbors in its own K11 missing set. Its degree is at least14 if it is in only one missing set, or at least15 if in both. This contradicts zero clique excess. If all three (A_i) are nonempty, the three disjoint leaf/point charges already total at least12. Thus at most one (A_i) can be nonempty under (T\le8).

This supplies the equality detail behind the h=4 star support argument and makes the K10 center additivity explicit.

## 3. Audit conclusion

The two center-charge arguments used in the h=4 and h=5 support eliminations are valid under the stated blocker-completeness lemma and the nonempty missing-set condition for K11s. The center terms are pointwise additive; the opposite-leaf terms and point terms are disjoint. No counterexample was found in these cases.
