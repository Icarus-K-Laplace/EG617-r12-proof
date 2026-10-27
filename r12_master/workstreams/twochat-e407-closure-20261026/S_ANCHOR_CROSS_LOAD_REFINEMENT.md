# E407 Q32 — S-anchor / exact S-B cross-load tradeoff

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the frozen exact-129 residual factor and selected-anchor structure. Necessary structure only; E407 Q32 remains OPEN.**

## 1. Notation

For an exact-129 color c, let

\[
q_c:=|E_c(S,B)|
\]

be the number of shell S-B edges of color c. Let \(\sigma\) be the total number of selected S-anchor occurrences among the seven exact colors. Since every exact color has at most one selected S anchor,

\[
\sigma=\sum_{s\in S}m_s.
\]

Let \(\beta=e(M[S])\in\{0,1,2\}\). The previously proved shell-edge theorem gives the global bound

\[
\sum_c q_c\ge14-\beta.
\tag{1.1}
\]

This note adds a second lower bound depending on \(\sigma\).

## 2. Per-color S-B edge theorem

### Theorem 2.1

For every exact-129 color c,

\[
\boxed{q_c\ge1.}
\tag{2.1}
\]

If c has a selected S anchor, then

\[
\boxed{q_c\ge2.}
\tag{2.2}
\]

### Proof

The selected B-anchor theorem gives \(b_c\in\{5,6,7\}\).

#### Case A: \(b_c=5\)

This case is already sharp in `EXACT_COLOR_SHELL_CROSS_LOAD.md`: the selected anchors are \(\{p,s_c\}\cup B_c\), and each of the two residual hubs has a color-c edge to residual B. Hence \(q_c\ge2\).

#### Case B: \(b_c=6\) and an S anchor is selected

The unique selected non-B anchor is an S vertex, so p and the other two S hubs are residual. The residual B-placement is either

\[
(u_c,g_c)=(2,2)\quad\text{or}\quad(3,1),
\]

where u counts B vertices in the three unselected K5 components and g counts B vertices in the exceptional G11.

If p lies in an unselected K5, that component contains no shell vertex because every p-shell edge is target-colored. Therefore \(u_c\le2\), forcing \((u_c,g_c)=(2,2)\). The other two unselected K5 components each contain B. A residual hub in one of those K5s has a color-c edge to B. A residual hub in G11 also has a color-c edge to B: the two B vertices of G11 are color-c nonadjacent, so a hub nonadjacent to both would form a color-c independent triple with them, contradicting \(\alpha(G11)=2\).

If p lies in G11, the gadget cannot contain two B vertices: p together with two B vertices would be a color-c independent triple because p-B and B-B edges are target-colored. Hence \(g_c\le1\), forcing \((u_c,g_c)=(3,1)\). All three unselected K5s contain B. A residual hub in a K5 therefore sees B in color c; a residual hub in G11 must see its single B vertex, otherwise p, that B vertex, and the hub form an independent triple.

Thus each of the two residual hubs supplies a distinct S-B edge, proving \(q_c\ge2\).

#### Case C: \(b_c=6\) and p is selected

The residual outside-core labels are four B vertices and all three hubs. Suppose \(q_c=0\).

If \((u_c,g_c)=(2,2)\), the two B vertices in G11 forbid every S vertex from G11: with no S-B color-c edge, any such S together with the two B vertices would be an independent triple. The two B-containing K5s also contain no S. Hence all three hubs lie in the remaining B-free K5, forcing all three S-S edges to have color c.

If \((u_c,g_c)=(3,1)\), all three unselected K5s contain B and hence contain no S under \(q_c=0\). All three hubs lie in G11 with one B vertex. Since that B vertex is color-c nonadjacent to every hub, \(\alpha(G11)=2\) forces the three hubs to form a color-c triangle.

Both alternatives require all three S-S shell edges to have color c, impossible because every retained V12 template has \(\beta\le2\). Therefore \(q_c\ge1\).

#### Case D: \(b_c=7\)

All seven selected anchors lie in B. The residual outside-core labels are p, three B vertices, and all three hubs. Suppose \(q_c=0\).

If p lies in an unselected K5, that K5 contains no shell vertex, so \(u_c\le2\).

- If \((u_c,g_c)=(1,2)\), G11 contains two B vertices and therefore no S under \(q_c=0\). Of the other two K5s, one contains B; hence all three hubs must lie in the unique B-free K5 and form a color-c triangle.
- If \((u_c,g_c)=(2,1)\), both remaining K5s contain B and hence no S. All three hubs lie in G11 with one B vertex, and again \(\alpha(G11)=2\) forces the hubs to form a color-c triangle.

If p lies in G11, then g_c<=1 because p together with two B vertices would be an independent triple.

- For \((u_c,g_c)=(2,1)\), G11 contains p and one B and therefore no S when \(q_c=0\); all three hubs lie in the unique B-free K5 and form a color-c triangle.
- For \((u_c,g_c)=(3,0)\), all three K5s contain B and no S; all three hubs lie in G11 with p. Since p is color-c nonadjacent to every hub, \(\alpha(G11)=2\) again forces a color-c triangle on S.

The placement \((u_c,g_c)=(1,2)\) is impossible when p lies in G11 because p plus the two B vertices is already an independent triple.

Thus \(q_c=0\) always forces all three S-S edges to have color c, again impossible because \(\beta\le2\). Hence \(q_c\ge1\).

This completes the proof. QED.

## 3. Global S-anchor cross-load

A selected S anchor occurs exactly in the b=5 case or in the b=6 case where the unique non-B selected anchor is S. By Theorem 2.1, each such color contributes at least two S-B edges, while every other exact color contributes at least one. Therefore

\[
\boxed{\sum_c q_c\ge7+\sigma.}
\tag{3.1}
\]

Combining with (1.1),

\[
\boxed{|E_{\rm exact}(S,B)|\ge\max\{14-\beta,\,7+\sigma\}.}
\tag{3.2}
\]

In particular, the shell itself must satisfy

\[
\boxed{e_M(S,B)\ge\max\{14-\beta,\,7+\sigma\}.}
\tag{3.3}
\]

For template E, the old lower bound 12 is therefore strict whenever \(\sigma\ge6\): six selected S-anchor occurrences force at least 13 exact-colored S-B edges, and seven force at least 14.

## 4. Coupling to selected hub-complete support blocks

Let \(m_p\) be the selected pivot-anchor multiplicity. Since every selected anchor is in exactly one of B, S, or \(\{p\}\),

\[
B_{\rm sel}+\sigma+m_p=49.
\tag{4.1}
\]

In every shell branch with a full B row, `SELECTED_SUPPORT_HUB_COMPLETENESS.md` gives

\[
N_{\rm hub}^{\rm sel}\ge B_{\rm sel}-21=28-\sigma-m_p.
\tag{4.2}
\]

Together with (3.1),

\[
\boxed{N_{\rm hub}^{\rm sel}+|E_{\rm exact}(S,B)|\ge35-m_p\ge28.}
\tag{4.3}
\]

Equation (4.3) is a structural tradeoff, not an edge-count contradiction: its two summands are different resources. It is useful because minimizing selected hub-complete blocks forces high p/S-anchor multiplicity, which in turn forces exact shell cross-load or a 28-point repeated-pivot block packing.

## 5. Dependency audit

The proof uses:

- the exact residual factor \(3K5+G11\) and \(\alpha(G11)=2\);
- the selected-anchor classification \(b_c\in\{5,6,7\}\);
- B being a target clique and p being target-adjacent to all shell vertices;
- the retained V12 fact \(e(M[S])\le2\);
- edge-color uniqueness only for the global summation.

It does not use the Didin-dependent branch or any low-delta terminal classification.

The placement case split is finite and is replayed arithmetically in `verify_selected_support_global_forcing.py`; the verifier does not replace the graph-theoretic alpha-two arguments.

## 6. Remaining gap

The new inequality correlates the shell cross-load with the number of selected S anchors and, through (4.2), with the number of actual selected hub-complete support blocks. It still permits abstract incidence systems. The next terminal step must use the pointwise support multiplicities \(7-r_u\), anchor injectivity, and the U/W degree ledger to show that these two required structures cannot coexist on one 284-edge core.