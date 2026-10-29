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

The scalar witness can be realized by a source-correct **Class-A** local mode, but not by the Class-B argument previously claimed. Take \(x_C\in O\), with all ten isolated K5s single-outside; let the special \(N_s\) be single-outside with H-part \(\{w,s_i,s_j,s_k\}\), \(w\in T_0\), and let \(N_t\) be double-outside with H-triangle \(\{y,t_j,t_k\}\), \(y\in T_i\), where \(i,j,k\) are distinct. Set \(A_0=\{w,s_j\}\). The actual nine-edge baseline is the K4 on \(\{w,s_i,s_j,s_k\}\) plus the K3 on \(\{y,t_j,t_k\}\); all three baseline T0 attachments go to the K4 triangle, so this is Class A. The two additional H-edges are \(yw\) and \(ys_j\), giving \(g_C=2,t_C=1\), with the T0 repeat on \(T_0T_i\) and the large-pair repeat on \(T_iT_j\). The seven-vertex residual graph has \(\alpha=2\). Thus shared-track placement is source-realizable in Class A. The earlier attempted counterexample incorrectly used \(yw\) as a baseline attachment and \(ws_i\) as an extra; in the actual source baseline \(ws_i\) is a K4 edge and \(yw\) is extra. It therefore does not refute the Class-B-specific complement law.

A corrected source-compatible aggregate witness chooses four patterns on \((T_1T_2,T_0T_1)\), three on \((T_1T_2,T_0T_2)\), and three on \((T_2T_3,T_0T_3)\). Its exact-color surplus is
\[
(7,0,3;4,3,3),
\]
and the remaining aggregate capacities are
\[
(1,9,6;0,1,0),
\]
giving \(g_D=17\). This respects an explicit source-realizable local mode and all scalar capacities, but still omits the actual endpoint labels in the common residual factors and is not a Q32 coloring.

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



### 3.1. Mode-sensitive pair-location laws at \((g_C,t_C)=(2,1)\)

**Class A source mode (shared track).** In the \(x_C\in O\), \(N_s\)-single, \(N_t\)-double placement described above, the true baseline is \(K_4(\{w,s_i,s_j,s_k\})\cup K_3(\{y,t_j,t_k\})\), not an arbitrary alternative matching baseline. The two extras are \(yw\) and \(ys_j\). Therefore the T0 repeat is on \(T_0T_i\), the large-pair repeat on \(T_iT_j\), and the two pairs share track \(i\).

**Class B source mode (complementary tracks).** For the seven-vertex Class-B baseline, the source placement forces \(x_C\in T_0\) and both special K5s double-outside; the \(x_C\in O\) and triple-special placements put all three baseline T0 attachments on the same large-track triangle and are Class A. In the double-double mode, if \(y\in O\), \(x_C\) together with the H-part of \(N_t\) forms a transversal K4 and again gives Class A. Thus Class B at \(g_C=2,t_C=1\) has \(y\in H\). Write \(i\) for the track of \(y\), \(j\) for the track of the unique H vertex in \(A_0\), and \(k\) for the remaining track. Pointwise saturation gives exactly one H vertex in \(A_0\), and balanced coloring forces \(i\ne j\). The source gadget then gives the unique T0 repeat on \(T_0T_k\) and the large-pair repeat \(yA_0\) on \(T_iT_j\). Hence these pairs are complementary.

The previous counterexample was a valid Class-A source graph, not a Class-B graph. The correct model must preserve both rules separately: **Class A permits shared-track placement; Class B forces complementary-track placement.** Neither local rule solves the common endpoint-label packing.

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


## 4.1 Vertex-labelled owner-only relaxation witness

verify_v47_z01_vertex_labelled_common_p_witness.py constructs a labelled **owner-only relaxation** in the E0=0 scalar state. The 36 large-track vertices are arranged into six disjoint 6-cycles, so each P_ij is a perfect matching and their union has degree two at every vertex. Ten distinct T0 vertices are assigned to ten individual source Class-A K4+K3 residual gadgets with (g_C,t_C)=(2,1) and alpha(J_C)=2. The H / exact-repeat / D-repeat edge counts are:
- large-pair H=(4,3,3), exact repeats=(7,0,3), D repeats=(1,9,6);
- T0 H edges=(7,7,8), T0 repeats=(4,4,3);
- ten individual exact gaps equal 2, and g_D=17.

The construction passes these local and aggregate checks, but it is **not a feasible common-P color-matching packing**: it assigns three exact colors to each of three residual 6-cycles and one color to a fourth. Colors sharing the same residual six vertices require the same six complementary baseline edges on those vertices, contradicting cross-color edge-disjointness. The verifier now reports nine colliding color pairs and 36 duplicate baseline-edge claims. This is an intentionally weakened owner-only witness, useful for exposing the missing constraint, not evidence that the full endpoint packing is feasible.

## 4.2 Pair-projection injectivity lemma

Let C be an exact color with a large-pair repeat edge e in S_ij. By the source contract, both endpoints of e lie in R_i(C) and R_j(C), so P_ij contains at least one edge inside the 2-by-2 bipartite block R_i(C) x R_j(C). There are exactly two perfect matchings on this block, and they partition its four edges. Therefore at most one of those perfect matchings is disjoint from P_ij. The restriction of M_C,ij to this block is consequently uniquely determined by the residual pair (R_i(C),R_j(C)) and P_ij.

If another exact color C' had the same two residual subsets on tracks i,j, its M_C',ij restriction would have to be the same matching, violating edge-disjointness. Hence:

\[
\boxed{\text{If C owns an }S_{ij}\text{ edge, then its residual pair }(R_i(C),R_j(C))\text{ is unique among exact colors.}}
\]

This is a valid cross-color constraint without assuming that a color's six residual vertices form a component of the common P graph. It is necessary but not by itself a contradiction.

The remaining bridge is to impose pair-projection injectivity, all cross-color matching edge-disjointness, and the complete triangle-factor / Type-I incidence constraints simultaneously. The owner-only witness is not a full source-realizable Q32 coloring.
## 5. Current proof frontier and audit gate

- Non-full-support rows \(v=45,46\), \(m=8,9,10\), are closed in this workstream under the source-correct multiplicity theorem, current nonexact degree floors, and the no-core-only degree-four lemma. The \(v=44,m=8,9\) branch belongs to the sibling workstream.
- For full support \(v=47\), the \(z=0,1\) small/outer partitions are aligned, the \(z=1\) \((3,2,1,1)\) profile is closed by a K13 contradiction, and the remaining \(z=0\) and \(z=1\) \((2,2,2,1)\) cells remain open.
- The common-factor CSP above is the next exact bridge from local Type-I shapes to a global contradiction. Until its vertex-labelled edge-packing constraints are solved or a source-realizable completion is exhibited, E408/Q32 remains **OPEN / NOT_CERTIFIED**.


### 4.3 Additional direct P_0i/baseline-overlap failure

A stricter audit of `verify_v47_z01_vertex_labelled_common_p_witness.py` finds a fatal flaw even before its residual-signature collisions: for each exact color C, the proposed P_0j and P_0k edges at its residual T0 vertex x_C are exactly the K4 baseline edges x_Cs_j and x_Cs_k of that same color. But P_0i is the complement of the eleven selected color matchings, so it cannot contain any such baseline edge. There are exactly 20 such overlaps across the ten colors. The script now asserts this count and labels itself a retraction audit; it no longer claims a feasible common-P witness. The already documented 9 residual-signature collision pairs and 36 duplicate baseline-edge claims are an additional, independent failure. The owner-only construction therefore supplies no feasible endpoint packing, and must not be used as evidence of Q32 feasibility.