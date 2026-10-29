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
Combining the source Type-I capacity with this identity gives \(t_C\le\min(2,g_C)\) for every exact color. Summing over all eleven colors also recovers
\[
\sum_C(g_C-t_C)=37-(11-E_0)=26+E_0,
\]
the total surplus on the three K12--K12 pairs.

## 4. Finite aggregate consequences

Write \(t_D\) for the number of degree-four T0 vertices owned by the unique nonexact color D. Then

\[
t_D+\sum_{C\text{ exact}}t_C=11-E_0,\qquad 0\le t_C\le2.
\]

The exact colors can collectively own at most 20 such vertices, so this capacity alone does not close any E0 case. The pointwise saturation is instead a hard local constraint for any future Type-I packing or SAT/ILP model: each T0 vertex is either **all eleven color-degrees equal 3**, or **one color-degree 4 and ten color-degrees 3**. No relaxed model may assign two repeat colors to the same T0 vertex or degree 5+ to any color there.

No retracted degree-nine assertion or exceptional-point injectivity is used. The aligned z=0,1 cells, full-support Q32, and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
