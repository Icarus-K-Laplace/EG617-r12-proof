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
