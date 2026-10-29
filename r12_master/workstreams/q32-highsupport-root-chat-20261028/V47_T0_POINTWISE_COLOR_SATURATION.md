# E408 Q32 — pointwise color-degree saturation on the K11 track

Date: 2026-10-29  
Status: **PROVED_CONDITIONAL exact degree ledger.** This adds a vertexwise constraint to the aligned z=0,1 cell; no Q32 closure is claimed.

> **Scope note (2026-10-29):** this degree-saturation theorem and the identity (g_C\ge t_C) do not assume all ten isolated K5 components are single-outside. The seven-vertex residual catalog is conditional; the isolated-double alternative is documented separately.

## 1. Contract

Use the aligned low-z profile (2,2,2,1): the target graph H is partitioned into target cliques
\(T_1,T_2,T_3\cong K_{12}\) and \(T_0\cong K_{11}\).
Let \(\mathcal C\) be the eleven non-target colors. The balanced-coloring premise says every 13-set contains every non-target color.

By Section 3 of `V47_Z01_BALANCED_COLORING_CROSS_TRACK_LEDGER.md`, the seven outer vertices and singleton residual vertex in T0 have epsilon=0, while each of the three small-block vertices has epsilon in {0,1}; thus E0 is in {0,1,2,3}. The existing cross-track ledger gives:
- every \(v\in T_0\) has target degree within H equal to \(12+\epsilon_v\);
- \(\epsilon_v\in\{0,1\}\), and the sum over \(T_0\) is \(E_0\in\{0,1,2,3\}\);
- every \(v\in T_0\) has exactly \(2+\epsilon_v\) H-neighbors outside T0.

## 2. Exact degree sum at each T0 vertex

Fix \(v\in T_0\). There are 36 vertices of H outside T0. Exactly \(2+\epsilon_v\) of those incident pairs are target-colored, so the number of non-target-colored H-edges from v to \(H\setminus T_0\) is

\[
36-(2+\epsilon_v)=34-\epsilon_v.
\]

For each \(i\in\{1,2,3\}\) and every non-target color C, the set \(T_i\cup\{v\}\) has 13 vertices. Since \(T_i\) is a target-color clique, C must appear on at least one edge from v to \(T_i\). Hence

\[
d_C(v,H\setminus T_0)\ge 3.
\]

Summing over all eleven non-target colors gives the exact saturation:

- If \(\epsilon_v=1\), the sum is 33, so **every non-target color has exactly three H-neighbors at v**.
- If \(\epsilon_v=0\), the sum is 34, so **exactly one non-target color has four H-neighbors at v and the other ten have exactly three**.

In particular, no non-target color can have H-degree at least five at a T0 vertex.

Let \(t_C\) be the number of vertices \(v\in T_0\) for which \(d_C(v,H)=4\). Then the vertexwise statement gives the exact identity

\[
\boxed{\sum_{C\in\mathcal C}t_C=11-E_0.}
\]

The sets of T0 vertices counted by the eleven \(t_C\) are pairwise disjoint and cover precisely the \(11-E_0\) vertices with \(\epsilon_v=0\).

## 3. Type-I restriction for each exact color

For an exact Type-I color C, every T0 vertex with \(d_C(v,H)=4\) must lie in its 11-vertex gadget \(G_{11}(C)\).

Indeed, a T0 vertex in an isolated single-outside K5 has exactly three C-neighbors in H. An isolated double-outside K5 cannot contain a T0 vertex, since it would give that vertex H-degree two, contradicting the degree floor three. An isolated triple-outside K5 has only one H-neighbor per H vertex and is likewise impossible at T0. Thus a degree-four T0 vertex must be in \(G_{11}(C)\).

Each of the two special K5s inside \(G_{11}(C)\) contains at most one T0 vertex, because its C-edges cannot lie inside the target clique T0. The special point \(x_C\) contributes at most one more T0 vertex. If \(x_C\in T_0\), it cannot be the triple placement (the eleven single-outside factors would require eleven other T0 vertices). In the two-double placement, the ten single-outside factors already use all ten T0 vertices other than \(x_C\), so neither double-outside factor can contain T0. Thus any special K5 that contains a T0 vertex must be single-outside; both special K5s cannot be single-outside, by the source-correct \(b_s+b_t=2\) exclusion. Consequently

\[
\boxed{t_C\le |G_{11}(C)\cap T_0|\le 2}
\]

for every exact color C.

This is a per-color capacity bound on who can own the degree-four T0 vertices. It is not, by itself, a contradiction: the nonexact color may own some or all of the \(11-E_0\) vertices.


There is also an exact surplus identity. Since each color C has at least one edge from every T0 vertex into each of the three K12 tracks, a degree-three T0 vertex contributes one edge to each T0--K12 pair, while a degree-four vertex contributes one extra edge on exactly one such pair. Hence
\[
\sum_{i=1}^3 \bigl(e_C(T_0,T_i)-11\bigr)=t_C.
\]
For each K12--K12 pair, Hall's theorem gives \(e_C(T_i,T_j)\ge12\). Therefore
\[
\boxed{g_C=e_C(H)-69
=t_C+\sum_{1\le i<j\le3}\bigl(e_C(T_i,T_j)-12\bigr)\ge t_C.}
\]
Combining the coarse source Type-I capacity with this identity gives \(t_C\le\min(2,g_C)\) for every exact color; Section 5 sharpens the global placement-aware bound to \(t_C\le1\). Summing over all eleven colors also recovers
\[
\sum_C(g_C-t_C)=37-(11-E_0)=26+E_0,
\]
the total surplus on the three K12--K12 pairs.

## 4. Finite aggregate consequences

Write \(t_D\) for the number of degree-four T0 vertices owned by the unique nonexact color D. Then

\[
t_D+\sum_{C\text{ exact}}t_C=11-E_0,\qquad 0\le t_C\le1.
\]

The ten exact colors can collectively own at most 10 such vertices. Thus if E0=0, the nonexact color D must own at least one of the 11 repeated-color T0 vertices; for E0>=1 this count alone gives no contradiction. The pointwise saturation is instead a hard local constraint for any future Type-I packing or SAT/ILP model: each T0 vertex is either **all eleven color-degrees equal 3**, or **one color-degree 4 and ten color-degrees 3**. No relaxed model may assign two repeat colors to the same T0 vertex or degree 5+ to any color there.

No retracted degree-nine assertion or exceptional-point injectivity is used. The aligned z=0,1 cells, full-support Q32, and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.


## 5. Global placement-sensitive bound: \(t_C\le1\)

The placement split sharpens the coarse bound in Section 3 to
\[
\boxed{t_C\le1\quad\text{for every exact Type-I color }C.}
\]
The proof separates the source-correct cases.

- **All ten isolated K5s single-outside.** Their ten transversal H-K4s use ten of the eleven T0 vertices, so only one T0 vertex remains in \(G_{11}\). Hence \(t_C\le1\). Equivalently, the seven-vertex residual singleton has three baseline C-edges, and pointwise saturation caps its C-degree at four, so at most one extra edge may occur across all three T0--Ti pairs combined.
- **Isolated-double, two-K4 subcases.** This covers \(x_C\in O\) with the double factor isolated, and \(x_C\in H\), two-double with one isolated double and \(y\in O\). The eight-vertex residual consists of two disjoint transversal K4s plus a star of extra edges centered at \(y\) or \(x_C\), with the other endpoints in one special K4. Only one of the two T0 residual vertices can be incident to that star: if the center is in T0, it is the only T0 endpoint that can receive an extra; if the center is in a large track, only the T0 vertex in the opposite special K4 can receive one. Thus \(t_C\le1\). If the star center lies in T0, the pointwise cap further forces \(g_C\le1\).
- **Exceptional isolated-double placement.** Here \(x_C\in H\), two-double, and \(y\in H\). The special double-outside clique \(N_s\) has an H-part \(K_3\), the special single-outside clique \(N_t\) has an H-part \(K_4\), and \(b_s+b_t=3\), so \(g_C=3\). The gadget contributes three edges from \(x_C\) to \(N_t\setminus\{y\}\), plus exactly one edge from \(x_C\) or \(y\) to each of the three H-vertices of \(N_s\).

  Neither \(x_C\) nor \(y\) can be in T0 alone: if \(x_C\in T_0\) but \(y\notin T_0\), the edge from \(x_C\) to the T0-vertex of \(N_t\) lies inside the target clique; if \(y\in T_0\) but \(x_C\notin T_0\), the edge from \(x_C\) to the \(N_t\)-vertex in \(x_C\)'s large track is forbidden. They cannot both lie in T0 either. If \(k=|A_0\cap N_s\cap H|\), then their H-degrees would be \(3+(3-k)\) and \(3+k\); both must be at most four, which would require \(k\ge2\) and \(k\le1\) simultaneously. Hence \(x_C,y\) both lie in large tracks.

  Since the residual track profile is (2,2,2,2), one T0 vertex lies in the \(N_s\) H-triangle and the other in the \(N_t\) H-\(K_4\). The former has exactly two C-neighbors inside the triangle and one gadget neighbor, so degree three. The latter has three C-neighbors inside the \(K_4\) and the extra edge from \(x_C\), so degree four. Thus this exceptional branch also has \(t_C=1\), not 2.

Consequently, every exact color has at most one degree-four T0 vertex, and the exact surplus identity strengthens to
\[
\boxed{\sum_{i=1}^3(e_C(T_0,T_i)-11)=t_C\le1.}
\]
Combining with \(g_C=t_C+\sum_{i<j}(e_C(T_i,T_j)-12)\) gives at least \(g_C-1\) surplus edges on the three large-track pairs. The global identity \(\sum_C t_C=11-E_0\) then implies \(t_D\ge\max(0,1-E_0)\) for the unique nonexact color D. This is a stronger source-correct constraint, not a contradiction.
