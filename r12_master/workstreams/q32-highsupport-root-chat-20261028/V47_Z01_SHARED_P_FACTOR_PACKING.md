# E408 Q32 — shared residual-factor packing model

Date: 2026-10-29  
Status: **Exact next-step formulation; not yet solved.** The aggregate relaxation is feasible, so this file identifies the vertex-level constraints needed for a genuine closure.

## 1. Why the scalar gap ledger is insufficient

`verify_v47_z01_aggregate_budget_witness.py` independently verifies an aggregate witness with
\[
E_0=0,\quad (E_1,E_2,E_3)=(2,2,2),\quad
(e_{12},e_{13},e_{23})=(4,3,3).
\]
The degree ledger then gives
\[
(y_1,y_2,y_3)=(7,7,8),\quad
(r_{12},r_{13},r_{23})=(8,9,9),\quad
(q_1,q_2,q_3)=(4,4,3),
\]
where \(r_{ij}=12-e_{ij}\) and \(q_i=11-y_i\).

A source-placement audit adds a complement law for the class-B, \(g_C=2,t_C=1\) pattern: an extra edge on \(T_0T_i\) must be paired with the large-pair extra on the complementary pair \(T_jT_k\), where \(\{i,j,k\}=\{1,2,3\}\). The corrected aggregate witness respects this law. Choose four patterns on \((T_2T_3,T_0T_1)\), four on \((T_1T_3,T_0T_2)\), and two on \((T_1T_2,T_0T_3)\). Their aggregate surplus is
\[
(2,4,4;4,4,2).
\]
The remaining aggregate capacities are
\[
(6,5,5;0,0,1),
\]
giving \(g_D=17\). Thus even after imposing this source-derived pair-location constraint, all scalar pair capacities, exact-color gap bounds, and the total 37-unit identity can hold simultaneously. The witness still omits the actual endpoint labels in the common residual factors and is not a Q32 coloring.

**This is not a Q32 coloring or an actual vertex-level completion.** It deliberately omits the shared endpoint labels of the common residual factors. It proves only that the aggregate budget inequalities and per-color pattern counts cannot by themselves close the branch.

## 2. Exact common-factor constraints on the three K12 pairs

For each \(1\le i<j\le3\), Hall's theorem supplies eleven edge-disjoint color-\(C\) perfect matchings \(M_{C,ij}\), one for each non-target color, whose complement \(P_{ij}\) is a perfect matching. The target matching \(H_{ij}\) is a subset of \(P_{ij}\). Define
\[
S_{ij}=P_{ij}\setminus H_{ij}.
\]
Then
\[
|S_{ij}|=12-e_H(T_i,T_j)=r_{ij},
\]
and the three \(S_{ij}\) together form a graph on \(T_1\cup T_2\cup T_3\) with
\[
d_{S_{12}\cup S_{13}\cup S_{23}}(v)=2-d_{H[T_1\cup T_2\cup T_3]}(v)\le2.
\]
Every edge of every \(S_{ij}\) is a repeated-color edge owned by exactly one non-target color. For an exact color \(C\), each such edge must be incident only with vertices in the residual set of its Type-I gadget; isolated K5 components cannot supply or receive an extra C-edge.

The decisive constraint missing from the aggregate witness is therefore not merely
\[
\sum_C |E_C^+\cap(T_i,T_j)|=r_{ij},
\]
but the **same actual edge set \(S_{ij}\)** must be partitioned among colors, with no endpoint conflicts and with each color's selected residual vertices containing all of its assigned edges.

## 2.1 Triangle-label signature for aligned single-outside colors

For a single-outside exact color whose large-track residual baseline is in class A or B, the three matchings \(M_{C,12},M_{C,13},M_{C,23}\) form twelve disjoint transversal triangles on the 36 large-track vertices: ten triangles belong to isolated K4 components, and the two residual triangles are the gadget's large-track baseline. Label these triangles by \(\tau_C\in\{1,\ldots,12\}\).

For each pair \(i<j\), the matching \(M_{C,ij}\) joins equal triangle labels. Since \(P_{ij}\) is edge-disjoint from \(M_{C,ij}\), every edge of \(P_{ij}\) joins **different** \(\tau_C\)-labels. If a non-H edge \(e\in S_{ij}\) is owned by color \(C\), both endpoints must be residual, so their labels must be exactly the two residual labels \(\{a_C,b_C\}\). Consequently every large-pair surplus edge owned by this color connects the same unordered label pair \(\{a_C,b_C\}\), even when the edges lie on different track pairs.

Equivalently, for each pair \(ij\), write \(P_{ij}\) in the triangle-label coordinates of \(M_C\) as a derangement permutation \(\pi_{C,ij}\) of the 12 labels. A surplus edge of C on that pair is possible only when
\[
\pi_{C,ij}(a_C)=b_C\quad\text{or}\quad \pi_{C,ij}(b_C)=a_C.
\]
Thus the complete set of large-pair surplus edges owned by an aligned exact color must lie on the at-most-six directed arcs between the same two residual triangle labels across the three pair types. This is stricter than checking only \(|E_C^+|\le3\).

If \(t_C=1\), the T0 surplus edge's large-track endpoint must also have triangle label \(a_C\) or \(b_C\). The T0 baseline edge from the same residual T0 vertex uses the other residual vertex in that track, so the baseline/extra pair at that track realizes both labels \(a_C,b_C\). This is the vertex-label condition to impose when matching T0 repeat edges to large-pair surplus edges.

This triangle-label signature applies only to aligned class-A/B single-outside colors. Class-C/D six-cycle holonomy and isolated-double colors must retain their separate residual models.

## 3. Color modes must remain separate

For each exact color \(C\), introduce a mode bit:

- **single-outside mode:** all ten isolated K5s meet H in transversal K4s. The residual gadget has profile \((2,2,2,1)\), baseline size 9, and \(e(J_C)=9+g_C\). Use the corrected seven-vertex catalog and holonomy table only in this mode.
- **isolated-double mode:** nine isolated K4s and one isolated K3 lie outside the gadget; the residual gadget has profile \((2,2,2,2)\), a two-transversal-K4 baseline of 12 edges, and \(e(J_C)=12+g_C\). Use the separate eight-vertex audit. Its present enumerator is only a necessary relaxation; the source star/incidence restrictions still have to be imposed.

Do not silently apply the seven-vertex theorem to a color in isolated-double mode.



### 3.1. Source complement law for class B with \((g_C,t_C)=(2,1)\)

Assume the all-isolated-single-outside mode and a class-B baseline. The T0 attachments split across the two large-track triangles. If \(x_C\in O\), or if the source placement is triple-outside, the residual T0 singleton belongs to the single-outside special \(K_5\), so all three baseline T0 attachments meet the same large-track triangle; that is class A, not B. Thus class B forces \(x_C\in T_0\) and the two-double placement, with both special \(K_5\) factors double-outside.

Let \(y\in N_t\). If \(y\in O\), the three H-vertices of \(N_t\setminus\{y\}\) already give \(x_C\) three H-neighbors, and \(t_C=1\) allows only one further H-neighbor; the source H-edge count then gives \(g_C=1\), not 2. Hence \(y\in H\). Write \(i\) for the large track containing \(y\), and \(j\) for the large track containing the unique H-vertex of \(A_0\). Since both special factors are double-outside, \(N_s\cap H\) and \(N_t\cap H\) are triangles, one vertex in each of \(T_1,T_2,T_3\).

The T0 point \(x_C\) is adjacent to the two H-vertices of \(N_t\setminus\{y\}\) and to the H-vertices of \(N_s\setminus A_0\). The condition \(t_C=1\) means \(d_C(x_C,H)=4\), so \(A_0\) contains exactly one H-vertex. If \(i=j\), neither of these two source neighborhoods contains a vertex in \(T_i\), violating the balanced-coloring requirement that every non-target color meet every large track from \(x_C\). Thus \(i\ne j\). The remaining large track \(T_k\) is the unique track in which \(x_C\) has two C-neighbors, so the T0 repeat edge lies on \(T_0T_k\). The only extra H-H gadget edge is \(y\)--the H-vertex of \(A_0\), which lies on \(T_iT_j\), the complementary large-track pair.

Therefore the source-correct pair-location law is
\[
\boxed{T_0T_k\text{ repeat}\ \Longrightarrow\ T_iT_j\text{ repeat},\quad \{i,j,k\}=\{1,2,3\}.}
\]
The companion aggregate verifier now uses only these three complementary location patterns. This is a necessary source-incidence constraint, not a global completion theorem.

## 4. Finite exact model to build

For each exact color \(C\):

1. Choose its mode and residual vertex sets \(R_i(C)\subseteq T_i\), with \(|R_i(C)|=2\) for \(i=1,2,3\), and \(|R_0(C)|=1\) or 2 according to the mode.
2. Choose the three pairwise perfect matchings \(M_{C,ij}\). In single-outside mode, the union of their edges on the 30 nonresidual vertices must be ten transversal triangles; the six residual large-track vertices have the audited two-triangle/six-cycle holonomy. In isolated-double mode, preserve the source-correct eight-vertex gadget and its two-K4 base.
3. For every edge \(e\in S_{ij}\), assign one owner color \(C\). If \(C\) is exact, require both endpoints of \(e\) to lie in \(R_i(C)\) and \(R_j(C)\), and include \(e\) in \(E_C^+\). Every \(S_{ij}\) edge must have exactly one owner.
4. Enforce \(J_C=B_C\cup E_C^+\), \(\alpha(J_C)\le2\), \(g_C=|E_C^+|\le3\), and \(t_C\le1\). The isolated-double mode must additionally obey the source-derived star incidence; the existing graph-count verifier alone is not sufficient.
5. For each \(T_0\)--\(T_i\) pair, choose the complement \(P_{0i}\) of the eleven color matchings saturating \(T_0\). It has exactly one edge at every T0 vertex but need not be a matching on \(T_i\). Its non-H edges are the T0 repeat edges; each exact color owns at most one such edge in total.
6. Enforce the exact H degree ledger, including \(E_0+\sum_iE_i=6\), \(y_i=e_{jk}+2+E_0+E_i\), \(\sum e_{ij}=10-E_0\), \(r_{ij}=12-e_{ij}\), and \(q_i=11-y_i\).
7. Enforce the global color budget \(7\le g_D\le19\), \(0\le g_C\le3\), and \(\sum_{C\text{ exact}}g_C=37-g_D\).

The model must preserve choice-dependence of each \(P_{ij}\): different selected Hall matchings can induce different complementary perfect matchings. No fixed residual factor may be assumed canonical.

## 5. Current proof frontier and audit gate

- Non-full-support rows \(v=45,46\), \(m=8,9,10\), are closed in this workstream under the source-correct multiplicity theorem, current nonexact degree floors, and the no-core-only degree-four lemma. The \(v=44,m=8,9\) branch belongs to the sibling workstream.
- For full support \(v=47\), the \(z=0,1\) small/outer partitions are aligned, the \(z=1\) \((3,2,1,1)\) profile is closed by a K13 contradiction, and the remaining \(z=0\) and \(z=1\) \((2,2,2,1)\) cells remain open.
- The common-factor CSP above is the next exact bridge from local Type-I shapes to a global contradiction. Until its vertex-labelled edge-packing constraints are solved or a source-realizable completion is exhibited, E408/Q32 remains **OPEN / NOT_CERTIFIED**.
