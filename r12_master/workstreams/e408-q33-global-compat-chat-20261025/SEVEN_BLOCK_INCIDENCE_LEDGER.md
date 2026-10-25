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

At least eight colors have \(s_C=0\), i.e. exact-129 restrictions to R. For every exact-129 color, the retained blocker theorem gives \(r_i(C)\ge1\) for each block i, so the baseline bound is
\[
R_C\ge7,\qquad P_C\le55. \tag{3}
\]
The former Sections 15–16 claimed \(R_C\ge15,\ P_C\le47\), but those outer-cap proofs are now **NOT CERTIFIED** because they use the invalid single-external-edge isolation inference. The only unconditional row-level bound used here is the baseline \(R_C\ge7,\ P_C\le55\); stronger outer caps must not be used until repaired.
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
2. \(e(L)=336+\delta\), \(S_0=\epsilon_U+2\delta\ge13\) in the general 31-point/56-witness boundary, and the degree identities in NON_FOUR_PARTITE_TERMINAL.md.
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


## 7. New low-slack blocker normal form (\(r_i(C)\le3\))

This subsection imports the pairwise blocker-compatibility theorem from the read-only ultimate-closure workstream and derives a sharper consequence for blocks with at most three repeated C-incidences.

Fix an exact-129 color C and an outer block \(B_i\). Write \(X_b=N_C(b)\cap R\) for \(b\in B_i\), and let \(n_i(C)\) be the number of size-five blockers. The exact blocker theorem gives:
- every \(X_b\) has size at least five;
- a size-five \(X_b\) is one of the ten isolated K5 components;
- any component fully contained in a row neighborhood contributes five repeated C-incidences if it is fully contained in two row neighborhoods, so this cannot happen when \(r_i(C)\le3\);
- at least nine of the twelve row neighborhoods contain a full K5 component (the gadget-incidence cap \(2|U_C|=22\) allows at most three rows with no full component).

**Theorem 7.1 (low-slack component coverage).** If \(r_i(C)\le3\), then:
1. no row neighborhood contains two full K5 components, because that row would contribute at least 10 edges and the other eleven rows at least 5 each, giving \(e_C(B_i,R)\ge65>61+r_i(C)\);
2. every K5 component is contained in exactly one row neighborhood;
3. exactly two row neighborhoods contain no full K5 component;
4. every component-containing row has size at most \(5+(r_i(C)-1)\le7\).

**Proof.** Item 1 follows from the edge budget. By the one-or-two rule, a component cannot be fully contained in two rows when \(r_i(C)\le3\), since all five of its vertices would then have C-degree two into \(B_i\). Therefore the at least nine component-containing rows from the blocker theorem represent distinct components. If only nine components were represented, three rows would contain no full component. Each such row has at least six neighbors in the exceptional gadget \(U_C\). Thus those three rows alone contribute at least 18 incidences from \(U_C\) into \(B_i\). But each of the 11 gadget vertices has C-degree one or two into \(B_i\), so the total gadget incidence into \(B_i\) is at most \(11+r_i(C)\le14\), a contradiction. Hence all ten components are represented exactly once, leaving exactly two rows with no full component. Their neighborhoods have size at least six, while the ten component-containing rows have size at least five. Since the total incidence is \(61+r_i(C)\), the total excess above \(10\cdot5+2\cdot6=62\) is \(r_i(C)-1\le2\). Thus each component-containing row has at most two extra vertices, proving item 4. \(\square\)

**Two exceptional-row refinement.** Let X and Y be the two row neighborhoods containing no full K5 component, and put \(Y_U=X\cap U_C\), \(Z_U=Y\cap U_C\). The total incidence budget above the baseline \(10\cdot5+2\cdot6=62\) is \(r_i(C)-1\le2\), so X and Y together contain at most two vertices outside \(U_C\). Their union therefore cannot cover a full isolated K5 component. Applying pairwise blocker compatibility with k=0 gives \(U_C\subseteq X\cup Y\), hence \(Y_U\cup Z_U=U_C\).

Let \(a=|Y_U\cap Z_U|\). Since both gadget portions have size at least six, \(1\le a\le r_i(C)\le3\). The complements \(A_C=U_C\setminus Y_U\) and \(B_C=U_C\setminus Z_U\) are disjoint cliques of C[U_C], each of size at most five, and
\[
|A_C|+|B_C|=11-a.
\]
Thus their size profiles are \(5+5\) if \(a=1\), \(5+4\) if \(a=2\), and either \(5+3\) or \(4+4\) if \(a=3\). If e is the number of gadget vertices additionally covered by component-containing rows and t the number of component vertices appearing outside their unique component row, then the exact repeated-incidence budget is
\[
r_i(C)=a+e+t,\qquad e+t\le2.
\]
This isolates the remaining local freedom to at most two extra incidences beyond the two complementary gadget blockers.

**Cross-block consequence.** Suppose \(r_i(C)\le3\) and \(r_j(C)\le3\) for two distinct outer blocks. For each isolated component \(K_\ell\), let \(x_i(\ell)\in B_i\) and \(x_j(\ell)\in B_j\) be its unique component-containing row representatives. Each row neighborhood contains \(K_\ell\) plus at most two extra vertices. Their union contains no second full component and covers at most four vertices of \(U_C\). Thus at least seven vertices of \(U_C\) remain outside the union; they cannot form a clique because \(\omega(C[U_C])=5\). Pairwise blocker compatibility therefore forces
\[
x_i(\ell)x_j(\ell)\in E(C).
\]
So for any two blocks with \(r_i(C),r_j(C)\le3\), the ten component labels induce ten forced, pairwise vertex-disjoint C-edges between those blocks. The edges are a matching and may be baseline edges; this does **not** by itself imply \(d_{ij}(C)>0\).

## 8. Consequence for the 56-witness support

For each of the eight selected exact-129 colors, at least six isolated components are B-labelled no-S components \(\{b\}\cup Q\), with \(Q\subset H\) an independent four-set in the 56-witness family. In any outer block with \(r_i(C)\le3\), Theorem 7.1 shows that every such selected component is contained in a unique row neighborhood.

For a fixed outer row \(x\), its C-neighborhoods \(N_C(x)\cap R\) across different colors are disjoint, since each edge \(xr\) has a unique color. Therefore the selected four-sets \(Q\) whose components are represented by the same outer row are pairwise disjoint. Each row can represent at most seven selected Q-sets (they are disjoint four-subsets of the 31-point support), and it cannot represent two components of the same color because its C-neighborhood has size at most seven in the low-slack block.

Hence every low-slack block induces a 12-row partition of the 56 selected witness labels into matching classes, with at least six labels from each of the eight selected colors represented in the partition. Across two low-slack blocks, the component-label matching edges above must be edge-disjoint across colors, since an outer-block pair has only one edge color.

This is a sharper, explicitly labelled finite compatibility problem. It is **not yet an impossibility proof**: the 56 labels give 56 component occurrences per block, while the crude row capacity is \(12\cdot7=84\), so the immediate capacity inequality remains feasible.


## 9. Duplicate-budget thresholds for low-slack blocks

For an exact-129 color C, \(R_C=62-P_C\) and every block has \(r_i(C)\ge1\). Let h be the number of blocks with \(r_i(C)\ge4\). Then
\[
R_C=\sum_i r_i(C)\ge4h+(7-h)=7+3h,
\]
so
\[
h\le\left\lfloor\frac{55-P_C}{3}\right\rfloor.
\]
Consequently the number \(k_C\) of blocks with \(r_i(C)\le3\) satisfies
\[
\boxed{k_C\ge\max\left(0,\,7-\left\lfloor\frac{55-P_C}{3}\right\rfloor\right).}
\]

Useful thresholds:
| Duplicate count P_C | Guaranteed blocks with r_i(C)<=3 |
|---:|---:|
| P_C >= 35 | at least 1 |
| P_C >= 38 | at least 2 |
| P_C >= 41 | at least 3 |
| P_C >= 44 | at least 4 |
| P_C >= 47 | at least 5 |
| P_C >= 50 | at least 6 |
| P_C >= 53 | all 7 |

For each such block, Theorem 7.1 and the two-exceptional-row refinement apply. This gives a precise way to turn a large per-color duplicate budget into forced component matchings across multiple block pairs. The aggregate lower bound \(\sum_{C:s_C=0}P_C\ge69\) alone does not force any one color to reach P_C>=35, so this threshold is a conditional branch filter rather than a global closure.


## 10. Extended low-duplicate blocker theorem (\(r_i(C)\le5\))

Theorem 10.1. Fix an exact-129 color C and a target block \(B_i\). If \(r:=r_i(C)\le5\), then the twelve neighborhoods \(X_b=N_C(b)\cap R\) have the following structure:

1. Exactly ten neighborhoods contain a full isolated K5 component, one for each of the ten components, with no component represented twice and no row containing two full components.
2. The other two neighborhoods contain no full K5 component. Their gadget portions \(X,Y\subset U_C\) satisfy \(X\cup Y=U_C\), \(|X|,|Y|\ge6\), and \(a:=|X\cap Y|\in\{1,\ldots,5\}\).
3. The complements \(U_C\setminus X\) and \(U_C\setminus Y\) are disjoint cliques in \(C[U_C]\), each of size at most five. Their unordered size profiles are:
   - \(a=1\): \((5,5)\);
   - \(a=2\): \((5,4)\);
   - \(a=3\): \((5,3)\) or \((4,4)\);
   - \(a=4\): \((5,2)\) or \((4,3)\);
   - \(a=5\): \((5,1)\), \((4,2)\), or \((3,3)\).
4. If \(e_i\) is the number of gadget-vertex incidences in the ten component-containing rows, beyond their ten mandatory K5s, and \(t_i\) is the number of component-vertex incidences beyond the one mandatory occurrence of each component vertex, then the exact identity is
\[
\boxed{r_i(C)=a+e_i+t_i.} \tag{10}
\]

**Proof.** Every vertex of R has C-degree one or two into \(B_i\), so the total incidence into \(U_C\) is \(11+r_U\le11+r\le16\). A row containing no full K5 component has at least six neighbors in \(U_C\). Hence there are at most two such rows.

There cannot be zero such rows: twelve full-component rows contribute at least 60 incidences, and all eleven gadget vertices must also occur in row neighborhoods, giving \(e_C(B_i,R)\ge71>61+r\).

There cannot be exactly one such row. In this case eleven rows contain a full component. No row can contain two full components: that would create at least twelve component-row occurrences across eleven rows, hence at least two repeated component labels (each component can occur in at most two rows by the one-or-two rule), forcing at least ten repeated component incidences and contradicting \(r\le5\). Thus each of the eleven full rows contains exactly one component. There are ten component labels. Since each repeated component contributes five vertices of degree two into the block, (r\le5) permits at most one repeated component; hence exactly one component is repeated and all ten components are represented. The two rows containing that repeated component cannot jointly contain a second full component in their union: every component is already represented, and covering a second one in the pair would add five more repeated incidences, exceeding \(r\le5\). Pairwise blocker compatibility therefore has \(k=1\) for this pair and forces their union to contain at least six gadget vertices. Those six gadget incidences are additional to the baseline \(11\cdot5+6=61\) row incidences (the eleven mandatory K5s and the no-component row), giving \(e_C(B_i,R)\ge67>61+r\).

So there are exactly two no-component rows and ten component-containing rows. No component-containing row can contain two full K5s, since that would give
\(e_C(B_i,R)\ge10+9\cdot5+2\cdot6=67>61+r\).
If a component were repeated among the ten rows, another component would be absent from their full-component occurrences. Its five vertices must still occur in some row, adding at least five incidences beyond the baseline \(10\cdot5+2\cdot6=62\), again giving at least 67. Hence each component occurs in exactly one row.

The two no-component rows cannot jointly cover a full K5 component: doing so adds five component-vertex incidences beyond the baseline 62, giving at least 67. Thus the pairwise blocker theorem applies with \(k=0\), forcing their gadget portions to cover all of \(U_C\). Each complement is a clique by the individual blocker lemma; the complements are disjoint because \(X\cup Y=U_C\). Since \(|X|,|Y|\ge6\), their overlap \(a\) is at least one; since \(a\le r\le5\), it is at most five. The listed profiles follow from \(|U_C\setminus X|+|U_C\setminus Y|=11-a\) and the clique-number cap five.

Finally, the ten mandatory component rows contribute 50 incidences, while the two gadget portions contribute \(|X|+|Y|=11+a\). All other row incidences are exactly \(e_i+t_i\). Therefore
\(e_C(B_i,R)=50+(11+a)+e_i+t_i=61+r_i(C)\), proving (10). \(\square\)

**Corollary 10.2 (forced component matching across blocks).** If \(r_i(C)+r_j(C)\le6\), then for every isolated K5 component \(K_\ell\) of \(C[R]\), its unique representatives \(x_i(\ell)\in B_i\), \(x_j(\ell)\in B_j\) are C-adjacent. The ten resulting edges form a matching between \(B_i\) and \(B_j\).

**Proof.** Both row counts are at most five, so Theorem 10.1 gives unique component representatives. The row \(X_{x_i(\ell)}\) contains \(K_\ell\) plus at most \(r_i(C)-1\) extra vertices, because the baseline total incidence is 62 and the total beyond it is \(r_i(C)-1\). Likewise on side j. Their union therefore contains at most
\[
(r_i(C)-1)+(r_j(C)-1)\le4
\]
vertices outside \(K_\ell\). It cannot contain a second K5 component, and it meets \(U_C\) in at most four vertices, leaving at least seven gadget vertices outside the union. If the representatives were C-nonadjacent, pairwise blocker compatibility with \(k=1\) would force the remaining gadget to have independence number at most one, hence to be a clique of size at most five. Contradiction. Distinct component labels have distinct representatives in each block, so the ten forced edges form a matching. \(\square\)

**Budget corollary.** Since \(R_C=62-P_C=\sum_i r_i(C)\), if \(P_C\ge36\), then \(R_C\le26\). A seven-tuple of positive integers with every pair-sum at least seven has sum at least 27 (its sorted minimum is \(3,4,4,4,4,4,4\)). Hence \(P_C\ge36\) guarantees at least one block pair \(i,j\) with \(r_i(C)+r_j(C)\le6\), and thus a forced ten-edge component matching. This is a conditional branch filter; the aggregate exact-color bound \(\sum_{C:s_C=0}P_C\ge69\) alone does not force any one color to reach 36.


## 11. Exact boundary classification at \(r_i(C)=6\)

Fix an exact-129 color \(C\) and target block \(B_i\), and assume \(r_i(C)=6\). For each \(K_\ell\), let \(m_\ell\) be the number of row neighborhoods \(X_b\) containing all of \(K_\ell\). Put
\[
m=\sum_{\ell=1}^{10}m_\ell,\qquad
k=\#\{\ell:m_\ell=2\}.
\]
Let \(d_K\) be the number of repeated incidences among the 50 vertices in the ten \(K_5\) components, and \(d_U\) the number of repeated incidences among the 11 vertices of the gadget \(U_C\). Thus \(d_K+d_U=6\). Let \(n\) be the number of rows containing no complete \(K_5\) component.

**Theorem 11.1 (six-duplicate boundary).** Exactly one of the following cases holds.

**Case A: \(n=1\).**
- \(k=1\), \(m=11\); every component-containing row contains exactly one full \(K_5\), all ten components are represented, and one component is represented twice.
- \(d_K=5\), \(d_U=1\).
- The no-component row has exactly six gadget vertices. The two rows representing the repeated component have disjoint gadget portions whose union has size six. That six-set and the no-component row's gadget six-set cover \(U_C\) and intersect in exactly one vertex.
- The complement of each of those two six-sets is a five-vertex clique in \(C[U_C]\); these two five-cliques are disjoint, and together with the unique common vertex of the six-sets they partition \(U_C\).
- Every other row has no gadget vertices, and no component vertex has any repeated incidence beyond the five vertices of the repeated \(K_5\).

**Case B: \(n=2\) and \(k=1\).**
- \(d_K=5\), \(d_U=1\).
- Each no-component row has exactly six gadget vertices, their gadget portions intersect in exactly one vertex, and no other row contains a gadget vertex.
- There are two possible full-component occurrence profiles:
  1. \(m=10\): each of the ten component-containing rows contains exactly one full component; one component is represented twice and one component is not fully contained in any row. The five vertices of the latter component each occur exactly once in the row family, but only as partial component incidences.
  2. \(m=11\): one component-containing row contains two full components, the other nine each contain one, all ten components are represented, and one component is represented twice. No component vertex occurs outside these full-component occurrences.

**Case C: \(n=2\) and \(k=0\).**
- \(m=10\): each of the ten component-containing rows contains exactly one distinct full component, and all ten components are represented once.
- \(1\le d_U\le6\), \(d_K=6-d_U\le5\). The five incidences above the baseline \(50+12=62\) split exactly as
\[
d_K+(d_U-1)=5.
\]
Here \(d_K\) counts partial appearances of component vertices beyond their unique full-component row, while \(d_U\) counts repeated gadget incidences.

**Proof.** Every no-component row has at least six gadget vertices. The gadget has exactly \(11+d_U\le17\) total row incidences, so \(n\le2\). Also \(m_\ell\le2\) for every component, and every repeated full component contributes five repeated component incidences; hence \(k\le1\) and \(m\le10+k\le11\). If \(n=0\), all twelve rows contain a full component, so \(m\ge12\), impossible. Thus \(n\in\{1,2\}\).

If \(n=1\), then \(m\ge11\), hence \(m=11\) and \(k=1\). The two rows containing the repeated component must have gadget union of size at least six by pairwise blocker compatibility. Together with the no-component row's six gadget incidences, this gives at least twelve gadget incidences, so \(d_U\ge1\). Since \(d_K\ge5\) and \(d_K+d_U=6\), equality holds: \(d_K=5,d_U=1\). Equality in the gadget-incidence lower bound gives the stated disjointness, six-set sizes, one-point intersection, and absence of gadget incidences in all other rows. The five repeated component incidences are exhausted by the repeated \(K_5\).

If \(n=2\), the two no-component rows give at least twelve gadget incidences, so \(d_U\ge1\) and \(d_K\le5\). If \(k=1\), then \(d_K\ge5\), so \(d_K=5,d_U=1\). Also \(10\le m\le11\). When \(m=10\), ten rows each contain one full component, with nine distinct labels; hence one label is repeated and one is absent from the full-component rows. Its five vertices must occur once each as partial component incidences. When \(m=11\), exactly one of the ten rows contains two full components, all ten labels are represented, and one label is repeated. In either subcase the twelve gadget incidences are exactly the two no-component rows' six each, with a one-point overlap; all other rows have no gadget vertices. The component-incidence budget \(d_K=5\) rules out any further repeated component vertices.

Finally, if \(k=0\), then \(m\le10\), while the ten component-containing rows give \(m\ge10\). Thus \(m=10\), with exactly one distinct full component in each such row. The identity \(d_K+d_U=6\) and \(d_U\ge1\) gives \(d_K\le5\), and the displayed excess identity follows. These cases exhaust all possibilities. \(\square\)

**Corollary 11.2 (cross-block matching at the \(6+1\) boundary).** If \(r_i(C)=6\) and \(r_j(C)=1\), then at least eight of the ten \(K_5\) component labels force \(C\)-colored edges between \(B_i\) and \(B_j\); these edges form a matching of size at least eight. In Cases A and C, all ten labels force such edges. In Case B with \(m=10\), nine labels force them. In Case B with \(m=11\), at least eight labels force them.

**Proof.** Since \(r_j(C)=1\), Theorem 10.1 gives a row in \(B_j\) whose neighborhood is exactly \(K_\ell\), for every label \(\ell\). Suppose \(x\in B_i\) is a row representative containing exactly one full \(K_\ell\) and at most five additional vertices, and let \(y\in B_j\) be the exact \(K_\ell\) representative. If \(xy\) were not \(C\)-colored, pairwise blocker compatibility would give
\[
\alpha\!\left(C[U_C\setminus(X_x\cup X_y)]\right)\le1,
\]
because the union contains exactly one complete \(K_5\). But \(X_x\cup X_y\) covers at most five gadget vertices, leaving at least six vertices of \(U_C\); this remaining graph cannot be a clique because \(\omega(C[U_C])=5\). Contradiction.

In Case A, every label has a single-component row with at most five extra vertices (for the repeated label, choose the smaller of its two disjoint gadget portions). In Case C, each component-containing row has at most five extra incidences because the total excess above the 62-incidence baseline is five, and no row contains two full components. In Case B with \(m=10\), the nine fully represented labels have such rows. In Case B with \(m=11\), at most two labels lack a single-component row, namely the components that occur only in the double-component row; if one of them is the repeated component, it also has a single-component representative elsewhere. The selected representatives are distinct on each side, so the forced edges form the claimed matching. \(\square\)

**Scope.** Theorem 11.1 classifies the exact \(r_i(C)=6\) boundary but does not by itself eliminate any of its cases. Corollary 11.2 extends the earlier ten-edge matching interface to a guaranteed eight-edge matching when the two block budgets are \(6\) and \(1\); the forced edges remain baseline edges unless a separate duplicate-incidence argument says otherwise.


**Corollary 11.3 (high-\(P_C\) boundary forces a packing of maximum cliques).** Suppose \(C\) is exact-129, \(P_C\in\{49,50\}\), and some block \(B_i\) has \(r_i(C)=6\). Then:
- if \(P_C=50\), \(C\) contains at least eight vertex-disjoint \(K_{12}\) cliques, each consisting of one \(K_\ell\) component and one representative from each of the seven outer blocks;
- if \(P_C=49\), \(C\) contains at least seven such vertex-disjoint \(K_{12}\) cliques.

**Proof.** Since \(R_C=62-P_C\), the six other block budgets sum to six when \(P_C=50\), so all six equal one. When \(P_C=49\), those six budgets sum to seven, so five equal one and the remaining one equals two.

For \(P_C=50\), Corollary 11.2 supplies at least eight component labels whose representatives in \(B_i\) are C-adjacent to the exact \(K_\ell\) representatives in all six \(r_j=1\) blocks. The representatives for a fixed \(K_\ell\) in the six low-slack blocks are pairwise C-adjacent by Corollary 10.2, and every representative is C-adjacent to all five vertices of \(K_\ell\). Each such label therefore gives a \(K_{12}\).

For \(P_C=49\), the \(r_j=2\) block has at least \(11-2=9\) distinct exact size-five blockers by (5). The \(r_i=6\) block has at least eight clean single-component labels by Corollary 11.2. Their label sets intersect in at least \(8+9-10=7\) components. For each common label, the representatives in the \(r_i=6\) and \(r_j=2\) blocks are C-adjacent by the same pairwise blocker argument as Corollary 11.2; representatives in the \(r_j=2\) and \(r=1\) blocks are C-adjacent by Corollary 10.2, as are representatives in any two \(r=1\) blocks. Thus each common label extends to a \(K_{12}\).

Distinct labels use disjoint residual \(K_5\) components and distinct outer representatives, so the resulting cliques are vertex-disjoint. \(\square\)

This is a packing consequence, not a contradiction: \(\omega(C)\le12\) permits disjoint maximum cliques, and the present ledger does not yet show that the forced packing is incompatible with the remaining 870-edge color budget.


## 12. Exact gadget normal form and two-clique packing

**Theorem 12.1 (exact 5-clique structure of the 11-point gadget).** Under the retained exact-129 Type-I factor contract, let \(A,B\subset U_C\) be the two distinguished disjoint \(K_5\)'s and let \(x\) be the remaining vertex. Then \(e(C[U_C])=29\), \(\alpha(C[U_C])=2\), and \(\omega(C[U_C])=5\) force the following normal form.

Let \(A_0=\{a\in A: ax\notin E(C)\}\), \(B_0=\{b\in B: bx\notin E(C)\}\), with sizes \(a,b\). The independence-number condition forces every edge between \(A_0\) and \(B_0\). Since the 20 edges internal to \(A\cup B\) leave exactly nine other edges,
\[
(5-a)+(5-b)+e_C(A,B)=9,\qquad e_C(A,B)\ge ab,
\]
so \((a-1)(b-1)\le0\). After swapping \(A,B\), take \(a=1\); then \(b\in\{1,2,3,4\}\) and the cross edges are exactly \(A_0\times B_0\).

Besides \(A,B\), the only possible \(K_5\)'s in \(U_C\) are
\[
A'=(A\setminus A_0)\cup\{x\},
\]
and, only at the endpoints, \(B'=(B\setminus B_0)\cup\{x\}\) when \(b=1\), or \(D'=A_0\cup B_0\) when \(b=4\). Consequently the possible unordered pairs of disjoint \(K_5\)'s are:
- \(b=1\): \(\{A,B\},\{A',B\},\{A,B'\}\);
- \(b=2,3\): \(\{A,B\},\{A',B\}\);
- \(b=4\): \(\{A,B\},\{A',B\},\{A',D'\}\).

In particular, there exist two fixed disjoint \(K_5\)'s \(D_1,D_2\) such that every possible disjoint \(K_5\)-pair \(\{E,F\}\) has one member disjoint from \(D_1\) and the other disjoint from \(D_2\). One can take \((D_1,D_2)=(A,B)\) for \(b\le3\), and \((D_1,D_2)=(A',B)\) for \(b=4\).

**Proof.** The counting argument above gives the cross-edge normal form. A clique containing \(x\) and vertices from \(A\) can use only \(A\setminus A_0\), so its only possible size-five instance is \(A'\); the analogous clique on the B side exists only when \(b=1\). A clique not containing \(x\) that meets both \(A\) and \(B\) must lie in \(A_0\cup B_0\), so it has size five only when \(b=4\). This lists all size-five cliques. Checking their disjoint pairs gives the displayed list and the fixed pair \(D_1,D_2\). \(\square\)

**Corollary 12.2 (gadget clique packing from low-slack blocks).** Let \(J\) be any set of \(m\) target blocks with \(r_i(C)\in\{1,2\}\), and suppose at most one of them has \(r_i(C)=2\). Then \(C\) contains two vertex-disjoint cliques of sizes at least \(m+5\) and \(m+5\) if all \(r_i=1\); if one block has \(r_i=2\), it contains vertex-disjoint cliques of sizes \(m+5\) and \(m+4\).

In particular:
- six blocks with \(r_i=1\) force two vertex-disjoint \(K_{11}\)'s in \(C\);
- five blocks with \(r_i=1\) plus one block with \(r_i=2\) force vertex-disjoint \(K_{11}\) and \(K_{10}\).

**Proof.** For every \(r_i=1\) block, Theorem 10.1 gives two no-component rows whose neighborhoods in \(U_C\) are complements of a disjoint \(K_5\)-pair. By Theorem 12.1, one row's neighborhood contains \(D_1\) and the other contains \(D_2\). The omitted five-sets for all \(D_1\)-rows are 5-subsets of the six-set \(U_C\setminus D_1\), so any two intersect in at least four vertices. If two such outer vertices were C-nonadjacent, the pairwise blocker theorem with \(k=0\) would require their neighborhoods to cover all of \(U_C\), equivalently their omitted five-sets to be disjoint. Contradiction. Thus the selected \(D_1\)-rows form a clique together with \(D_1\), and similarly for \(D_2\). The two cliques are disjoint because \(D_1,D_2\) are disjoint and no 5-set can be disjoint from both.

For \(r_i=2\), Theorem 10.1 permits overlap \(a=1\) or \(a=2\); the complement profile is respectively \((5,5)\) or \((5,4)\). Thus at least one no-component row has a five-clique complement \(E\). By Theorem 12.1, \(E\) is disjoint from one of \(D_1,D_2\), so that row extends the corresponding clique by one vertex. It cannot extend both, and the other clique remains at size \(m+4\). \(\square\)

**Corollary 12.3 (strengthened high-\(P_C\) packing).** In the setting of Corollary 11.3:
- \(P_C=50\) forces eight vertex-disjoint \(K_{12}\)'s and four additional vertex-disjoint \(K_{11}\)'s. These cliques cover 140 vertices and contain \(748\) internal C-edges.
- \(P_C=49\) forces seven vertex-disjoint \(K_{12}\)'s, four vertex-disjoint \(K_{11}\)'s, and one vertex-disjoint \(K_{10}\). These cliques cover 138 vertices and contain \(727\) internal C-edges.

For \(P_C=50\), the six \(r=1\) blocks supply ten label-based \(K_{11}\)'s, at least eight extended to \(K_{12}\) by Corollary 11.2; Corollary 12.2 supplies two disjoint gadget \(K_{11}\)'s. For \(P_C=49\), the five \(r=1\) blocks and the \(r=2\) block supply ten label-based \(K_{11}\)'s, at least seven extended to \(K_{12}\); Corollary 12.2 supplies one gadget \(K_{11}\) and one gadget \(K_{10}\).

**Scope.** These packing bounds are strictly stronger than Corollary 11.3 but still do not contradict the exact 870-edge budget: the packings leave respectively 122 and 143 C-edges outside their clique interiors. A separate argument must constrain those remaining edges or link the packings to the other colors.


## 13. Audit correction: external-star inference withdrawn

**Status correction (2026-10-25): Sections 13–16 of the earlier ledger are not certified.** The previous Lemma 13.1 claimed that every monochromatic \(K_{12}\) is an isolated component of its color. This is false: for any outside vertex \(z\), the twelve edges from \(z\) to the clique must use all eleven other colors at least once, which implies only
\[
d_C(z,K_{12})\le1,
\]
not \(d_C(z,K_{12})=0\). A single external \(C\)-edge is allowed.

Consequently, any branch whose only contradiction is “a monochromatic \(K_{12}\) has one external \(C\)-edge” is invalid. This affects the former claims \(P_C\le49\), \(P_C\le48\), and the former \(P_C=50,\ r_i(C)=6\) exclusion. The detailed drafts are preserved in \`ARCHIVE_UNCERTIFIED_OUTER_CAPS_20261025.md\`, \`P49_BOUNDARY_EXCLUSION.md\`, and \`P48_BOUNDARY_EXCLUSION.md\`; they must not be cited as proved results until every such step is repaired, for example by forcing at least two external \(C\)-edges from the same outside vertex or by an independent valid contradiction.

Sections 1–12 remain the current conditional outer-row and gadget-normal-form results, subject to their own contracts. The inner-core theorem \`R12_E408_Q33_S0_12_EXCLUSION.md\` is separate: its \(K_{12}\) contradictions are cliques inside \(H\) and use \(\omega(H)\le11\), not the withdrawn outer isolation claim.

The global E408 Q33 terminal and EG617(\(r=12\)) remain **OPEN / NOT_CERTIFIED**.