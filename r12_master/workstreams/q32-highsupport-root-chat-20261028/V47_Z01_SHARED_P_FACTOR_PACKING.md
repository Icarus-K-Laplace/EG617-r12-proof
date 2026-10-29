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

Each of ten exact colors can take a locally admissible single-outside class-B pattern with \(g_C=2\), one large-pair surplus edge, and one T0-pair surplus edge. Choose four patterns on \((T_1T_2,T_0T_1)\), three on \((T_1T_3,T_0T_2)\), and three on \((T_2T_3,T_0T_3)\). Their aggregate surplus is
\[
(4,3,3;4,3,3).
\]
The nonexact color can then absorb the remaining aggregate capacities
\[
(4,6,6;0,1,0),
\]
giving \(g_D=17\). Thus all scalar pair capacities, exact-color gap bounds, and the total 37-unit identity can hold simultaneously.

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

## 3. Color modes must remain separate

For each exact color \(C\), introduce a mode bit:

- **single-outside mode:** all ten isolated K5s meet H in transversal K4s. The residual gadget has profile \((2,2,2,1)\), baseline size 9, and \(e(J_C)=9+g_C\). Use the corrected seven-vertex catalog and holonomy table only in this mode.
- **isolated-double mode:** nine isolated K4s and one isolated K3 lie outside the gadget; the residual gadget has profile \((2,2,2,2)\), a two-transversal-K4 baseline of 12 edges, and \(e(J_C)=12+g_C\). Use the separate eight-vertex audit. Its present enumerator is only a necessary relaxation; the source star/incidence restrictions still have to be imposed.

Do not silently apply the seven-vertex theorem to a color in isolated-double mode.

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
