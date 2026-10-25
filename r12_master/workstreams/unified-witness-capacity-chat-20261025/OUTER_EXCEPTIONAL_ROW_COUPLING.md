# Outer exceptional-row coupling theorem

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the registered exact-129 Type-I factor theorem and seven-block equality system. This is a new cross-block duplicate lower bound, not a terminal contradiction.

## 1. Contract

Fix an exact-129 non-target color \(C\). Its residual graph \(C[R]\) consists of ten isolated \(K_5\) components \(K_1,\ldots,K_{10}\) and an 11-vertex exceptional gadget \(U_C\), with
\[
\alpha(C[U_C])=2,\qquad \omega(C[U_C])=5.
\]
For a target block \(B_i\), write \(X_i(b)=N_C(b)\cap R\). The exact blocker theorem gives \(|X_i(b)|\ge5\), with equality only when \(X_i(b)\) is one of the ten \(K_\ell\).

Assume \(r_i(C)\le3\). The low-slack blocker theorem then gives exactly ten component rows, one for each \(K_\ell\), and two exceptional rows \(x_i,y_i\) containing no full \(K_\ell\). The two exceptional neighborhoods each meet \(U_C\) in at least six vertices; their union covers \(U_C\); and their total number of vertices outside \(U_C\) is at most two.

Define the two complementary cliques
\[
A_i=U_C\setminus (N_C(x_i)\cap U_C),\qquad
B_i=U_C\setminus (N_C(y_i)\cap U_C).
\]
Then \(A_i,B_i\) are disjoint cliques of \(C[U_C]\), each of size between three and five, with possible size profiles
\[
(5,5),\ (5,4),\ (5,3),\ (4,4).
\]
These are the complements of the exceptional rows' gadget-neighborhoods, not the 31-point support \(U\) of the core witnesses.

## 2. A nonempty intersection forces an outer edge

Take two distinct blocks \(B_i,B_j\) with \(r_i(C),r_j(C)\le3\). For any choice \(D_i\in\{A_i,B_i\}\), \(D_j\in\{A_j,B_j\}\), if
\[
D_i\cap D_j\ne\varnothing,
\]
then the corresponding exceptional rows are necessarily adjacent in color \(C\).

**Proof.** Choose \(u\in D_i\cap D_j\). By definition, \(u\) lies outside both exceptional rows' \(C\)-neighborhoods. The union of those two neighborhoods contains at most four vertices outside \(U_C\), so it cannot cover any entire isolated \(K_5\) component. Choose one vertex outside the union from each of the ten components \(K_\ell\), and add \(u\). These eleven vertices form a \(C\)-independent 11-set in \(R\), anticomplete in color \(C\) to both exceptional rows. If the two rows were not \(C\)-adjacent, adding them would give a \(C\)-independent 13-set, contradicting the global coloring contract. \(\square\)

## 3. Forced-edge lower bound for a block pair

Let \(M_{ij}\) be the \(2\times2\) zero/nonzero intersection matrix for
\[
(A_i,B_i)\times(A_j,B_j).
\]
Let \(k\) be its number of nonzero cells, \(\ell\) its number of nonempty rows, and \(c\) its number of nonempty columns. Every nonzero cell forces a distinct \(C\)-edge between the corresponding exceptional rows.

The ten isolated-component representatives also force ten pairwise vertex-disjoint \(C\)-edges between \(B_i\) and \(B_j\), one for each \(K_\ell\). These ten edges are disjoint from the exceptional-row edges. Every one of the twelve vertices on each side must have at least one \(C\)-edge to the opposite block. After the ten component edges, the four exceptional rows therefore need an edge cover. In addition to the \(k\) forced exceptional edges, at least
\[
\max(2-\ell,\,2-c)
\]
further edges are needed to cover any still-uncovered exceptional rows.

Since the exact block-pair ledger is
\[
e_C(B_i,B_j)=12+d_{ij}(C),
\]
we obtain the explicit duplicate lower bound
\[
\boxed{
d_{ij}(C)\ \ge\
\eta(M_{ij})
:=k+\max(2-\ell,\,2-c)-2.
}
\]
The right side is always nonnegative for a nonempty \(2\times2\) matrix. Its complete mask classification is:

| Nonzero-cell pattern | \(k\) | \((\ell,c)\) | \(\eta\) |
|---|---:|---:|---:|
| one cell | 1 | (1,1) | 0 |
| two cells forming a matching | 2 | (2,2) | 0 |
| two cells sharing a row or column | 2 | (1,2) or (2,1) | 1 |
| three cells | 3 | (2,2) | 1 |
| four cells | 4 | (2,2) | 2 |

This bound distinguishes the exceptional-row *intersection pattern* from a mere count of forced edges: two forced edges that share an endpoint already require an additional edge to cover the fourth exceptional row.

## 4. Global duplicate budget consequence

Let \(\mathcal L_C=\{i:r_i(C)\le3\}\). Summing over low-slack block pairs gives
\[
\boxed{
P_C=\sum_{i<j}d_{ij}(C)
\ \ge\
\sum_{\{i,j\}\subseteq\mathcal L_C}\eta(M_{ij}).
}
\]
For each fixed block pair, the global near-Latin rule says \(\sum_C d_{ij}(C)=12\). Therefore the forced exceptional-row lower bounds across all exact colors must satisfy
\[
\boxed{
\sum_{C:\ i,j\in\mathcal L_C}\eta(M_{ij})\le12
\quad\text{for every }i<j.
}
\]
This is a genuinely cross-color condition: the exceptional-row patterns for different colors cannot collectively demand more than the twelve duplicate edges available in one block pair.

## 5. What this does and does not close

- If a low-slack block pair has two adjacent nonzero cells, three nonzero cells, or four nonzero cells in \(M_{ij}\), it consumes at least one (or two) units of \(C\)'s block-pair duplicate budget.
- If the nonzero cells form a matching, the current theorem gives no positive duplicate lower bound. In particular, identical complementary-clique pairs across all low-slack blocks yield \(\eta=0\) for every pair and are not excluded by this theorem.
- Thus the remaining mathematical task is to prove that the actual exact-129 gadget and the seven-block system force enough non-matching intersection patterns, or to couple these patterns to the core witness coordinates. No such global incompatibility is claimed yet.


## 6. The exceptional-row graph has independence number at most two

Let \(\mathcal E_C\) be the set of the two exceptional rows from each low-slack block \(B_i\), \(i\in\mathcal L_C\). Then
\[
\boxed{\alpha(C[\mathcal E_C])\le2.}
\]

**Proof.** Suppose \(x,y,z\in\mathcal E_C\) are pairwise nonadjacent in color C. Let \(A_x,A_y,A_z\subseteq U_C\) be their complementary gadget cliques. For two rows from the same block, their complements are disjoint by the two-exceptional-row theorem. For rows from different blocks, intersecting complements would force a C-edge by Section 2. Hence \(A_x,A_y,A_z\) are pairwise disjoint. Each has size at least three, so
\[
9\le |A_x|+|A_y|+|A_z|\le11.
\]
Their total gadget-neighborhood incidence is
\[
\sum_{v\in\{x,y,z\}}|N_C(v)\cap U_C|
=33-|A_x|-|A_y|-|A_z|\ge22.
\]

Each exceptional row has total neighborhood size at most eight: the two exceptional rows in its block have total size at most \(11+r_i(C)\le14\), while the other has size at least six. If x,y,z come from three different blocks, their total neighborhood incidence is at most \(3\cdot8=24\). If two come from the same block, their combined size is at most 14 and the third has size at most eight, so the total is at most 22. In either case, the number of incidences with the ten isolated \(K_5\) components is at most two.

Thus the union of the three neighborhoods misses at least one vertex of every isolated \(K_5\) component. Choose one such vertex from each of the ten components. They are pairwise C-nonadjacent and anticomplete to x,y,z. Together with the independent triple x,y,z, they form a C-independent 13-set, a contradiction. \(\square\)

### Consequences for the 2-by-2 exceptional edge pattern

For any pair of low-slack blocks, no exceptional row can be C-nonadjacent to both exceptional rows of the other block; otherwise those three rows would be an independent triple. Hence the C-nonedges among the four exceptional rows form a matching. Equivalently, the C-edges among them have minimum degree at least one, and there are at least two.

Let \(E_C^{\rm exc}\) be the graph induced by all exceptional rows in \(\mathcal E_C\). If \(k=|\mathcal L_C|\), then
\[
e(E_C^{\rm exc})\ge 2\binom{k}{2}=k(k-1).
\]
This matches the extremal lower bound for a graph on \(2k\) vertices with independence number at most two. If equality holds, Turán's theorem applied to the complement shows
\[
E_C^{\rm exc}=K_k\ \dot\cup\ K_k.
\]
The two cliques must choose opposite exceptional rows from each block, because the two rows within one target block are C-nonadjacent. Thus the zero-excess pattern is a globally consistent two-type split of the exceptional rows. Any departure from this two-clique structure requires additional C-edges among exceptional rows and consumes duplicate budget.

This theorem strengthens the local edge-cover argument: it rules out independent triples across all low-slack blocks, not just a particular pairwise intersection mask. It still permits the two-clique extremal pattern and therefore does not close Q33.


## 7. Near-complete labelled component matching for every low-row-budget pair

The exact-129 row theorem (Theorem 10.1 in the E408 Q33 sibling ledger) gives, whenever \(r_i(C)\le5\), ten distinct component-containing rows
\[
x_i(1),\ldots,x_i(10),\qquad
K_\ell\subseteq N_C(x_i(\ell))\cap R,
\]
one for each isolated \(K_5\) component \(K_\ell\) of \(C[R]\), and two exceptional rows. The total number of neighborhood incidences beyond the baseline \(10\cdot5+2\cdot6=62\) is exactly \(r_i(C)-1\). In particular, across the ten component rows, the sum of all extra incidences beyond their own \(K_\ell\) is at most \(r_i(C)-1\).

**Theorem 7.1 (at most one missing component diagonal).** If \(r_i(C),r_j(C)\le5\), then among the ten same-component pairs
\[
\{x_i(\ell),x_j(\ell)\},\qquad \ell=1,\ldots,10,
\]
at most one pair is nonadjacent in color C.

**Proof.** Fix a label \(\ell\) for which \(x_i(\ell)\) and \(x_j(\ell)\) are nonadjacent. Their neighborhoods contain the full component \(K_\ell\). Let \(E_i(\ell)\) and \(E_j(\ell)\) be the extra neighborhood incidences of these two rows outside \(K_\ell\). If their union does not cover another entire \(K_5\) component, one vertex can be chosen outside their union from each of the other nine components. If at least six gadget vertices of \(U_C\) also remain outside their union, those vertices contain an independent pair because \(\omega(C[U_C])=5\). The nine component vertices, that independent pair, and the two nonadjacent rows would form a C-independent 13-set.

Therefore a missing diagonal requires either (a) at least five extra incidences to cover all vertices of a second K5 component, or (b) at least six extra incidences into \(U_C\) to leave at most five gadget vertices. In either case,
\[
|E_i(\ell)|+|E_j(\ell)|\ge5.
\]
For distinct missing labels, the incidences belong to distinct component rows, so their extra-incidence charges are disjoint. Summing over all missing labels gives
\[
5m_{ij}\le (r_i(C)-1)+(r_j(C)-1)\le8,
\]
where \(m_{ij}\) is the number of missing component diagonals. Hence \(m_{ij}\le1\). \(\square\)

**Corollary 7.2.** Every pair of blocks with \(r_i(C),r_j(C)\le5\) has at least nine C-edges joining same-label component representatives. If \(r_i(C)+r_j(C)\le6\), the sharper sibling theorem gives all ten. If exactly one diagonal is missing and \(r_i(C)+r_j(C)=7\), the five extra-incidence units are fully exhausted by covering a second K5 component; no extra incidence can enter the gadget.

This is a labelled near-matching statement, not a claim that the entire block-pair graph is a matching. Cross-label edges and edges incident to exceptional rows remain possible and must be charged separately in \(d_{ij}(C)\).


## 8. A missing component diagonal must spend a block-pair duplicate

**Theorem 8.1 (label mismatch is charged to \(d_{ij}\)).** Under the hypotheses of Theorem 7.1,
\[
\boxed{m_{ij}(C)\le d_{ij}(C).}
\]
Consequently, for \(\mathcal I_C=\{i:r_i(C)\le5\}\),
\[
\boxed{
\sum_{\{i,j\}\subseteq\mathcal I_C}m_{ij}(C)
\le
\sum_{\{i,j\}\subseteq\mathcal I_C}d_{ij}(C)
\le P_C.
}
\]

**Proof.** Theorem 7.1 gives \(m_{ij}\in\{0,1\}\). It remains to show that \(m_{ij}=1\) forces \(d_{ij}\ge1\). Suppose instead \(m_{ij}=1\) and \(d_{ij}=0\). Then \(e_C(B_i,B_j)=12\); since every one of the 12 vertices on each side has C-degree at least one into the other block, the C-bipartite graph between the blocks is a perfect matching.

Nine component diagonals are present. The remaining three left rows and three right rows consist of the two exceptional rows and the unmatched component representative on each side. Since the missing same-label pair is not an edge, the perfect matching must pair each unmatched component representative to an exceptional row on the opposite side, and pair the two remaining exceptional rows to each other. Let \(x\) be the exceptional row on the left paired to the unmatched component row on the right, and let \(y,z\) be the two exceptional rows on the right. Then \(x,y,z\) are pairwise C-nonadjacent: \(y,z\) lie in the same target block, and the perfect matching gives x no edge to either of them.

The missing diagonal already consumes at least five of the combined extra-incidence budget \(r_i+r_j-2\le8\). At most three extra incidences remain across all other rows in the two blocks. Since an exceptional row's baseline neighborhood lies in \(U_C\), the union of \(N_C(x)\), \(N_C(y)\), and \(N_C(z)\) cannot cover an entire isolated K5 component: covering one would require five component-vertex incidences, but at most three remain. Choose one vertex outside this union from each of the ten isolated K5 components. Those ten vertices are pairwise C-nonadjacent and anticomplete to \(x,y,z\), producing a C-independent 13-set, contradiction. Thus \(d_{ij}\ge1\) whenever \(m_{ij}=1\), proving the claim. \(\square\)

This is the desired edge-ownership link: every missing same-component label alignment among low-budget blocks is paid for by at least one unit of the exact block-pair duplicate ledger. It does not charge a missing diagonal twice, and it does not claim that every duplicate edge creates a missing diagonal.


## 9. Duplicate-budget-to-\(K_{12}\)-packing theorem

For an exact-129 color C, let \(n_i(C)\) be the number of outer-block rows \(b\in B_i\) with
\[
|N_C(b)\cap R|=5.
\]
By the exact blocker theorem, each such neighborhood is one of the ten isolated K5 components, and no component can be used by two size-five blockers in the same block. Write \(\mathcal K_i(C)\subseteq\{1,\ldots,10\}\) for the set of component labels used in block \(B_i\).

The incidence ledger gives \(e_C(B_i,R)=61+r_i(C)\). Every other row is a blocker of size at least six, so
\[
5n_i(C)+6(12-n_i(C))\le61+r_i(C),
\qquad
n_i(C)\ge11-r_i(C).
\]
Consequently,
\[
\begin{aligned}
\left|\bigcap_{i=0}^6\mathcal K_i(C)\right|
&\ge10-\sum_{i=0}^6(10-n_i(C))\\
&\ge10-\sum_{i=0}^6(r_i(C)-1)\\
&=17-R_C=P_C-45.
\end{aligned}
\]

**Theorem 9.1 (duplicate budget forces disjoint maximum cliques).**
\[
\boxed{\nu_{12}(C)\ge \max\{0,P_C-45\},}
\]
where \(\nu_{12}(C)\) is the maximum number of vertex-disjoint monochromatic \(K_{12}\) cliques in color C.

**Proof.** Every label in \(\bigcap_i\mathcal K_i(C)\) gives one exact size-five blocker row \(x_i(\ell)\) in each of the seven outer blocks. If \(x_i(\ell)\) and \(x_j(\ell)\) were C-nonadjacent, their neighborhoods into R would both equal \(K_\ell\). One vertex from each of the other nine isolated K5 components, an independent pair in \(U_C\), and the two rows would form a C-independent 13-set. Thus the seven representatives are pairwise C-adjacent, and together with \(K_\ell\) form a monochromatic \(K_{12}\). Different labels use disjoint K5 components and distinct rows in every block, so the resulting \(K_{12}\) cliques are vertex-disjoint. \(\square\)

### Refined high-\(P_C\) branches

Combining Theorem 9.1 with the near-complete matching theorem and the sibling \(r_i(C)=6\) classification gives:

- If \(P_C\ge51\), then \(R_C\le11\), every pair satisfies \(r_i+r_j\le6\), and all ten components extend to ten vertex-disjoint \(K_{12}\) cliques.
- If \(P_C=50\), then there are at least eight such cliques. If all \(r_i\le5\), at most one block pair has sum \(r_i+r_j\ge7\), so at least nine component labels align globally. If one \(r_i=6\), the other six parameters are all one and the sibling \(6+1\) theorem gives at least eight.
- If \(P_C=49\), then at least four such cliques follow from Theorem 9.1. This improves to at least seven if one \(r_i=6\), and at least eight if every \(r_i\le5\).

This is a reusable branch certificate, not a contradiction: the original coloring contract permits disjoint monochromatic \(K_{12}\) cliques.
