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

There cannot be zero such rows: then the twelve component-containing rows contribute at least 60 incidences, and the eleven gadget vertices require at least eleven additional incidences, giving \(e_C(B_i,R)\ge71>61+r\). There cannot be exactly one: eleven component-containing rows then give at least 55 incidences, and the lone no-component row contributes at least six gadget incidences. Among eleven full-component rows, some component repeats. Pairwise blocker compatibility for the two rows containing that component requires their union to contain at least six gadget vertices, adding at least six gadget incidences beyond the 55+6 baseline. Thus \(e_C(B_i,R)\ge67>61+r\).

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
