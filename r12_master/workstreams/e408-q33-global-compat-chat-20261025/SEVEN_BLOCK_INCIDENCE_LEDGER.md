# Seven-block incidence ledger for E408 Q33

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL ledger; global terminal exclusion OPEN.**

This file keeps the outer K12-block system, the exact-129 color factors, and the inner 56-witness support attached by labels. It does not identify unrelated local witnesses with exact-129 components.

## 1. Outer seven-block system

Under the retained E408 equality embedding, the target graph is the disjoint union
\[
G=B_0\dot\cup B_1\dot\cup\cdots\dot\cup B_6\dot\cup R,
\]
where each \(B_i\cong K_{12}\), \(|R|=61\), \(e_G(R)=408\), and there are no target edges between distinct pieces. Since
\[
\binom{145}{2}=10440=12\cdot870,
\]
every one of the twelve colors has exactly 870 edges globally.

Fix a non-target color C. For every outside vertex x and target block \(B_i\), each of the eleven non-target colors must occur at least once on the twelve edges from x to \(B_i\); otherwise \(B_i\cup\{x\}\) would be a C-independent 13-set. Thus exactly one color occurs twice and each other color occurs once.

Define:
- \(d_{ij}(C)\): the number of vertices in either block whose repeated color toward the other block is C;
- \(P_C=\sum_{0\le i<j\le6}d_{ij}(C)\);
- \(r_i(C)\): the number of vertices \(x\in R\) whose repeated color toward \(B_i\) is C;
- \(R_C=\sum_{i=0}^6r_i(C)\);
- \(e_C(R)=129+s_C\), with \(s_C\ge0\).

The exact counts are
\[
e_C\Bigl(\bigcup_iB_i\Bigr)=252+P_C,\quad
e_C\Bigl((\bigcup_iB_i),R\Bigr)=427+R_C,
\]
and the global 870-edge count gives
\[
\boxed{P_C+R_C+s_C=62.} \tag{1}
\]
Summing over the eleven non-target colors,
\[
\sum_C P_C=252,\qquad
\sum_C R_C=427,\qquad
\sum_C s_C=3. \tag{2}
\]
For every block i, \(\sum_Cr_i(C)=61\).

At least eight colors have \(s_C=0\), i.e. exact-129 restrictions to R. For every exact-129 color, the retained blocker theorem gives \(r_i(C)\ge1\) for each block i, so
\[
R_C\ge7,\qquad P_C\le55. \tag{3}
\]
The three nonexact colors have \(\sum s_C=3\) and \(\sum P_C\le183\). Therefore
\[
\sum_{C:s_C=0}P_C\ge252-183=69. \tag{4}
\]

## 2. Exact-129 blocker structure

Fix an exact-129 color C. The retained constrained factor theorem says C[R] consists of ten isolated K5 components \(K_1,\ldots,K_{10}\) and an 11-vertex exceptional gadget \(U_C\) with \(\alpha(C[U_C])=2\).

For a vertex \(b\in B_i\), let
\[
X_b=N_C(b)\cap R.
\]
Because \(B_i\) is independent in C and \(\alpha(C)\le12\), \(X_b\) must meet every maximum independent 12-set of C[R]. A maximum independent 12-set is formed by choosing one vertex from each K5 component and an independent pair from \(U_C\).

**Blocker lemma.**
- If \(X_b\) contains no whole K5 component, then \(|X_b\cap U_C|\ge6\). Otherwise an independent pair remains in \(U_C\), and one can choose a vertex outside \(X_b\) from every K5 component to obtain an unblocked independent 12-set.
- Each vertex of R has C-degree one or two into \(B_i\), so the total incidence of \(U_C\) into \(B_i\) is at most \(2|U_C|=22\). Hence at most three of the twelve row-neighborhoods \(X_b\) can contain no whole K5 component.
- A fixed K5 component can be contained in at most two row-neighborhoods in one block: if it were contained in three, each of its five vertices would have C-degree at least three into that block, violating the one-or-two rule.

Consequently, in every outer block at least nine row-neighborhoods contain a full K5 component. There are only four components outside the six selected B-labelled no-S components from the inner shell witness family; those four components can account for at most eight rows. Thus:

> **Cross-layer conclusion 2.1.** For every exact-129 color C and every outer block \(B_i\), at least one row-neighborhood contains one of the six selected B-labelled no-S K5 components.

This statement concerns *containment of a full component*, not necessarily an exact size-five blocker.

## 3. Exact size-five blockers and component labels

Let \(n_i(C)\) be the number of rows b in block \(B_i\) for which \(X_b\) has size exactly five. Every such \(X_b\) equals one of the ten K5 components. From the edge count
\[
e_C(B_i,R)=61+r_i(C)
\]
and the fact that every non-size-five blocker has size at least six,
\[
5n_i(C)+6(12-n_i(C))\le61+r_i(C),
\]
so
\[
\boxed{n_i(C)\ge11-r_i(C).} \tag{5}
\]
A component repeated as two exact size-five neighborhoods contributes five duplicate incidences. Thus when \(r_i(C)\le2\), the size-five neighborhoods are distinct components.

The total number \(M_C=\sum_i n_i(C)\) of exact size-five blocker occurrences obeys
\[
M_C\ge77-R_C=15+P_C. \tag{6}
\]
Combining (4) and (6),
\[
\boxed{\sum_{C:s_C=0}M_C\ge8\cdot15+69=189.} \tag{7}
\]
If there are more than eight exact-129 colors, the lower bound is stronger.

Now attach the high-k shell label. Each exact-129 color has at least six B-labelled no-S K5 components. Under the retained Q33/d3 row contract:
- if \(\beta=0\) or \(1\), at least two of these selected components have a label b with \(k_b\ge2\);
- if \(\beta=2\) or \(3\), at least one does.

If \(r_i(C)=1\), (5) gives ten distinct exact size-five blockers, so every K5 component, including a high-k component, is represented exactly in block i. If \(r_i(C)=2\), there are at least nine distinct exact blockers; hence a color with at least two high-k selected components has at least one high-k component represented exactly in that block.

More generally, because \(R_C=62-P_C\), if k blocks have \(r_i(C)\ge3\), then
\[
R_C\ge3k+(7-k)=7+2k,
\]
so the number of blocks with \(r_i(C)\le2\) is at least
\[
\boxed{\max\!\left(0,7-\left\lfloor\frac{55-P_C}{2}\right\rfloor\right).} \tag{8}
\]
For \(\beta\in\{0,1\}\), every such block has an exact blocker for at least one high-k selected component.

The number of blocks with \(r_i(C)=1\) is at least
\[
\boxed{\max(0,P_C-48),} \tag{9}
\]
because if t blocks have duplicate count one, then \(R_C\ge t+2(7-t)=14-t\). Equation (9) therefore gives a high-k exact blocker in at least \(P_C-48\) blocks for all beta regimes whenever \(P_C\ge49\).

## 4. Block-block edges forced by a repeated component label

Suppose the same K5 component K_j is an exact size-five blocker in blocks \(B_i\) and \(B_j\), with representatives \(b_i\) and \(b_j\). Then \(b_i\) and \(b_j\) must be C-adjacent.

Indeed, if they were nonadjacent in C, choose one vertex from each of the other nine K5 components and an independent pair from the exceptional gadget. These eleven vertices form a C-independent 11-set disjoint from both neighborhoods \(X_{b_i}=X_{b_j}=K_j\). Adding \(b_i,b_j\) would give a C-independent 13-set, contradiction.

Thus each repeated component label gives a C-colored edge between the corresponding outer-block representatives. For a fixed block pair, these edges form a partial matching indexed by common exact component labels.

**Important accounting rule.** A forced component-representative edge is not automatically a duplicate counted in \(d_{ij}(C)\) or \(P_C\). It may be the unique baseline C-edge from each endpoint into the opposite block. Only an independently proved repeated C-incidence contributes to the duplicate budget.

## 5. Coupling to the 56-witness core support

For E408 Q33 at the minimum-support boundary, the inner family has 56 labeled K4s in L, seven per selected exact-129 color. Each color supplies at least six B-labelled no-S K5 components and at least one high-k selected component. Across colors the selected four-sets are linear: two different colors cannot share two core vertices because their common edge would have two colors.

The global and local systems therefore have to satisfy all of the following at once:

1. 56 edge-disjoint witness K4s in L, union U of size31.
2. \(e(L)=336+\delta\), \(S_0=\epsilon_U+2\delta\ge12\), and the degree identities in NON_FOUR_PARTITE_TERMINAL.md.
3. The exact-129 component labels and high-k shell labels in Sections 2–3.
4. The outer duplicate budgets (1)–(4) and occurrence lower bounds (6)–(9).
5. For any repeated exact component label across outer blocks, the corresponding block representatives are joined by a C-colored edge.

Under the four-partite branch, the stronger local result \(S_0\ge22\) additionally forces \(\delta\ge9\) and at least seven of the 24 unused large-part pair slots to be absent from L. These pair slots are the only possible leftover edges in L under that branch.

## 6. Status and remaining gap

The ledger is exact, but no incompatibility between all of these conditions has yet been proved. In particular:
- \(M_C\ge15+P_C\) is a necessary occurrence count, not an UNSAT certificate.
- The inner K4 support is not interchangeable with the outer component-block incidence matrix.
- A component representative edge cannot be charged to \(P_C\) unless the repeated incidence is explicitly established.
- The non-four-partite L branch remains within the K5-free second-Turán edge interval.
- The four-partite branch remains open for \(S_0\ge22\).

The remaining task is an explicit labeled incidence contradiction or an independently replayable finite certificate for the contract above. Until then E408 Q33 remains OPEN / NOT_CERTIFIED.
