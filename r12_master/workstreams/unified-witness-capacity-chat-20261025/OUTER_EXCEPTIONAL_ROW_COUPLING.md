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


## 10. Selected support family versus the full exact-component witness reservoir

### 10.1 The seven-witness minimum-support family

The seven graph-theoretic witnesses used in the E407/E408 minimum-support analysis are not automatically all isolated K5 components. However, all selected witnesses avoid \(S\), and the ten isolated K5 components also avoid \(S\). Hence \(S\subseteq U_C\) and \(|U_C\setminus S|=8\). Two selected gadget witnesses would have disjoint four-sets filling these eight non-S gadget vertices, leaving no room for the shell label of either witness. Thus at most one of the seven selected witnesses lies in the gadget and at least six are isolated-component witnesses.

For the original selected family \(\mathcal W_C\), the intersection with the all-block blocker set \(\mathcal K_C^*\) therefore satisfies
\[
|\mathcal W_C\cap\mathcal K_C^*|
\ge\max(0,6+(P_C-45)-10)
=\max(0,P_C-49).
\]
This gives a selected-witness extension threshold \(P_C\ge50\). It is a packing constraint, not a contradiction, and it applies specifically to the chosen seven-witness support family.

### 10.2 All ten exact components are shell witnesses

A stronger independent fact follows from the full shell contract. Each isolated K5 component avoids \(S\), and must meet \(V(R)\setminus H=\{p\}\cup S\cup B\) because \(\alpha(H)\le4\). Its outside-\(H\) vertices therefore lie in \(B\cup\{p\}\). But \(B\) is a clique in the target-color graph and \(p\) is target-adjacent to every vertex of \(B\), so a C-colored K5 component contains at most one vertex of \(B\cup\{p\}\). Consequently every isolated component has exactly one shell label and four core vertices:
\[
K_\ell=\{\lambda_\ell\}\cup Q_\ell,\qquad
\lambda_\ell\in B\cup\{p\},\quad Q_\ell\subseteq H,\quad |Q_\ell|=4.
\]
Thus the exact-129 factorization supplies ten component-backed shell witnesses per color. This does not imply that the seven witnesses minimizing support are all selected from these ten; their union is a different support problem.

### 10.3 A new high-support reduction when \(m=10\)

Let \(U_{\rm comp}\) be the union of all ten component four-sets from each of \(m\) exact-129 colors. Same-color sets are disjoint, and any two sets from different colors intersect in at most one vertex, so \(|U_{\rm comp}|\ge40\).

If \(m=10\) and \(|U_{\rm comp}|=40\), the 100 component K4s partition the 40-point support colorwise and contribute 600 distinct edges to \(\overline{H[U_{\rm comp}]}\). But \(W=H\setminus U_{\rm comp}\) has seven vertices and \(\alpha(H[W])\le4\), so \(e(H[W])\ge21-t_4(7)=3\). The exact degree ledger gives
\[
e(H[U_{\rm comp}])=480-284+\epsilon_U+e(H[W])
=196+\epsilon_U+e(H[W]),
\]
hence
\[
e(\overline{H[U_{\rm comp}]})
=584-\epsilon_U-e(H[W])\le581,
\]
a contradiction. Therefore \(m=10\) forces \(|U_{\rm comp}|\ge41\).

At \(|U_{\rm comp}|=41\), each of the ten colors omits exactly one point from its ten disjoint four-sets. Since \(|W|=6\) and \(e(H[W])\ge2\), the degree ledger gives
\[
e(\overline{H[U_{\rm comp}]})=612-\epsilon_U-e(H[W])\le610.
\]
The 100 component K4s already account for 600 distinct edges, leaving at most ten additional edges. This creates a separate near-decomposition / partial transversal-design terminal. The cases \(m=8,9\) with \(|U_{\rm comp}|\ge40\), and \(m=10\) with \(|U_{\rm comp}|\ge41\), remain OPEN.
## 11. E407/E408 top-cell-A interface: exact-color factorization across \(W\sqcup O\)

This section is conditional on the sibling theorem in front_end/T61_H13_FULL_COLOR_DEGREE_AND_ANTINEIGHBORHOOD.md, Sections 5–6: \(|W|=23\), \(|O|=38\), \(e_F(W)=132\), and every non-target color restricts to a near-perfect matching of 11 edges on \(W\). It is also conditional on front_end/E408_EXACT129_BLOCKER_DUPLICATE_THEOREM.md, which classifies every exact-129 color as ten isolated \(K_5\) components plus an 11-vertex gadget \(U\), with \(\alpha(U)=2\), \(\omega(U)=5\), and \(e(U)=29\).

### Theorem 11.1 (exact intersection pattern)

For every exact-129 color \(C\), its ten isolated \(K_5\) components meet \(W\) in one of exactly two ways:

- **Type A:** every component has two vertices in \(W\); \(U\cap W\) has three vertices and \(C[U\cap W]\) is one edge plus an isolated vertex.
- **Type B:** nine components have two vertices in \(W\), one component has one vertex in \(W\); \(U\cap W\) has four vertices and \(C[U\cap W]\) is a perfect matching of two edges.

In particular, every one of the ten \(K_5\) components meets \(W\), and at least nine of them contribute a component edge to the near-perfect matching \(C[W]\).

**Proof.** Since \(C[W]\) is a matching, each \(K_5\) component meets \(W\) in at most two vertices. The ten components therefore cover at most 20 vertices of \(W\), so \(|U\cap W|\ge3\). But \(C[U\cap W]\) is also a matching and \(\alpha(U)\le2\); a matching on at least five vertices has an independent set of size at least three. Thus \(|U\cap W|\le4\). Hence \(|U\cap W|\in\{3,4\}\), and the ten component intersections sum to 20 or 19. With ten summands each at most two, the only profiles are \(2^{10}\) and \(2^9,1\). The component edges account for 10 or 9 of the 11 edges in \(C[W]\), respectively; the remaining 1 or 2 edges lie in \(U\cap W\), giving the stated matching profiles. \(\square\)

### Theorem 11.2 (exact global cross-edge defect ledger)

Let
\[
\kappa_v=d_F(v)-13,\qquad K_W=\sum_{w\in W}\kappa_w,
\qquad t_C=e_C(O)-42.
\]
For every non-target color \(C\), \(t_C\ge0\): the 38-vertex graph \(C[O]\) has independence number at most 12, so Turán's bound gives \(e_C(O)\ge p_{12}(38)=42\).

Let \(s_C=e_C(V(F))-129\), with \(\sum_Cs_C=411-E\). Because \(e_C(W)=11\),
\[
e_C(W,O)=129+s_C-11-(42+t_C)=76+s_C-t_C.
\]
On the target side,
\[
e_F(W,O)=\sum_{w\in W}d_F(w)-2e_F(W)
=13\cdot23+K_W-264=35+K_W.
\]
Since \(W\times O\) has \(23\cdot38=874\) pairs, summing the non-target cross edges and equating the two ledgers yields
\[
\boxed{\sum_Ct_C=K_W+411-E-3.}
\]
Equivalently,
\[
\boxed{\sum_Ct_C=K_W\quad(E=408),\qquad
\sum_Ct_C=K_W+1\quad(E=407).}
\]

### Corollary 11.3 (exact-color defect cap and equality profile)

For an exact-129 color \(C\), the intersection types in Theorem 11.1 imply
\[
\boxed{0\le t_C\le6.}
\]
In Type A, the ten \(K_5\) components contribute 30 edges inside \(O\), while \(U\cap W\) has one edge and its three vertices each have degree at least four in \(U\); therefore at least ten \(U\)-edges cross from \(W\cap U\) to \(O\cap U\), so \(e_C(O)\le30+(29-1-10)=48\). In Type B, the components contribute \(9\binom32+\binom42=33\) edges inside \(O\); the four vertices of \(U\cap W\) each need at least three cross-neighbors, giving \(e_C(O)\le33+(29-2-12)=48\). Combine this with \(e_C(O)\ge42\).

If \(t_C=0\), equality in Turán's bound forces \(C[O]\) to be a disjoint union of ten \(K_3\)'s and two \(K_4\)'s. This is consistent with either Type A (ten component triangles plus two gadget \(K_4\)'s) or Type B (nine component triangles, one component \(K_4\), and a gadget \(K_4\cup K_3\)).

**Scope warning.** The defect identity is an exact global budget, not yet a contradiction. It says the total excess of the eleven induced graphs \(C[O]\) above their 42-edge Turán floor equals the target degree excess on \(W\) (plus one for E407). The next step must exploit the simultaneous edge-disjoint \(K_3/K_4\)-partition structure when many \(t_C=0\), or prove that the positive \(t_C\)'s cannot be distributed as the identity allows.


### Corollary 11.4 (rigidity of the Type-A gadget at zero defect)

Suppose \(C\) is exact-129, \(t_C=0\), and its W-intersection is Type A. Then \(U[O]\) is \(K_4\cup K_4\), while \(U[W]\) is \(K_2\cup K_1\). Write \(U[O]=A\cup B\), with \(A,B\) the two K4s, and \(U[W]=\{x,y,z\}\), with \(xy\in E(U)\) and z isolated in \(U[W]\).

After swapping A,B and x,y if needed, there is an integer \(a\in\{0,1,2,3\}\) such that:
- x is complete to A and has no neighbors in B;
- y is complete to B and has exactly a neighbors in A;
- z is complete to B and to exactly \(4-a\) vertices of A;
- the A-neighborhoods of y and z partition A;
- every vertex of \(A\cup B\) and x has degree 5 in U, while \(d_U(y)=5+a\) and \(d_U(z)=8-a\).

Thus the gadget degree multiset is either \(5^{10},8\) or \(5^9,6,7\). In particular, the unique W-vertex unmatched by \(C[W]\) in this Type-A case has \(C\)-degree at least five, rather than merely the generic exact-color floor four.

**Proof.** Since \(t_C=0\), \(U[O]\) is two disjoint K4s and \(U[W]\) is \(K_2\cup K_1\). The graph U has 29 edges, so exactly \(29-12-1=16\) edges cross between \(W\cap U\) and \(O\cap U\). Independence number at most two forces every W-vertex to be complete to at least one of A,B; otherwise a missed vertex from each K4 forms an independent triple with it. The adjacent vertices x,y must be complete to opposite K4s, since a common K4 plus x,y would be a K6. WLOG x is complete to A and y to B. Let A0 be the vertices of A missed by z. Since yz is a nonedge, y must be adjacent to every vertex of A0; otherwise one such vertex with y,z is an independent triple. The mandatory cross edges already total \(4+4+(8-|A_0|)+|A_0|=16\), so there are no additional cross edges: x has no B-neighbors, \(N(y)\cap A=A_0\), and \(N(z)\cap A=A\setminus A_0\). If \(|A_0|=4\), then x and y are both complete to A and create a K6; hence \(a=|A_0|\le3\). This gives the stated degree sequence. \(\square\)


### Corollary 11.5 (where the unique duplicate lies in a low-slack block)

Assume the hypotheses of Theorem 11.1 and let an outer block \(B_i\) have \(r_i(C)=1\). The exact row theorem (E408 Q33, Theorem 10.1) gives ten component rows and two exceptional rows; because the total incidence is \(61+r_i=62\), the component rows are exactly their ten \(K_5\)'s and the exceptional rows are six-vertex subsets \(U\setminus D_1,U\setminus D_2\), where \(D_1,D_2\) are disjoint \(K_5\)'s in \(U\).

The component rows contribute 20 W-incidences in Type A and 19 in Type B. Since \(D_1,D_2\) are disjoint and cover all but one gadget vertex, their total W-intersection size is 2 or 3 in Type A, and 3 or 4 in Type B. Hence the two exceptional rows contribute respectively 4 or 3 W-incidences in Type A, and 5 or 4 in Type B. Therefore
\[
\boxed{e_C(B_i,W)\in\{23,24\}.}
\]

For every \(w\in W\), the 12 edges from \(w\) to \(B_i\) must contain each of the eleven non-target colors at least once; otherwise \(B_i\cup\{w\}\) is an independent 13-set in a missing color. The target color has no edges between \(B_i\) and \(R\) under the seven-block equality ledger, so exactly one non-target color is repeated at each \((w,B_i)\). It follows that
\[
e_C(B_i,W)=23+r_i^W(C),
\]
where \(r_i^W(C)\in\{0,1\}\) records whether the unique repeated-C vertex in block \(i\) lies in \(W\). Thus the row-incidence calculation identifies the location of the unique duplicate:
- \(e_C(B_i,W)=23\): the duplicate lies in \(O=R\setminus W\);
- \(e_C(B_i,W)=24\): the duplicate lies in \(W\).

This links the exact-129 gadget clique-pair choice to the global duplicate ownership ledger. It is not a contradiction by itself; across seven blocks, the repeated vertices can still be distributed between W and O unless a further witness constraint rules out the aggregate pattern.


## 12. The \(P_C=49,\ r_i(C)=6\) corner: exact double-star audit

### Lemma 12.1 (external-star capacity)

Let \(Q\) be a \(C\)-colored \(K_{12}\) in a 12-coloring with no independent 13-set in any color, and let \(z\notin Q\). Every one of the eleven colors \(D\ne C\) must occur on the 12 edges from \(z\) to \(Q\); otherwise \(Q\cup\{z\}\) is a \(D\)-independent 13-set. Hence
\[
d_C(z,Q)\le1.
\]
A single external \(C\)-edge is allowed; the contradiction is \(d_C(z,Q)\ge2\). This is the correct star-capacity statement and does not use the invalid stronger assertion that every monochromatic \(K_{12}\) is \(C\)-isolated.

### Theorem 12.2 (conditional exclusion of \(P_C=49,\ r_i(C)=6\))

Assume the exact-129 factor theorem, the seven-block row-incidence contract, the exact 11-vertex gadget normal form, and the row classifications for \(r=1,2,6\). Then no exact-129 color \(C\) can satisfy
\[
P_C=49,\qquad r_i(C)=6.
\]

**Proof.** Since \(P_C+R_C=62\), \(R_C=13\). The six other positive row budgets sum to seven, so there are five \(r_j=1\) blocks and one \(r_k=2\) block. Each \(r=1\) block supplies a pair of disjoint \(K_5/K_5\) gadget complements. The \(r=2\) block supplies a disjoint \(K_5/K_5\) or \(K_5/K_4\) complement pair.

The \(r_i=6\) row theorem gives two types of high block:
- In Cases A/B, a gadget-only row has a \(K_5\) complement \(H\). In the \(m=10\) subcase of Case B, the five partial component incidences are distributed across the two gadget-only rows, so one of them has at most two; the finite check below verifies the alignment for every possible \(K_5\) complement. Cases A and B with no partial component incidences are included as well.
- In Case C, the two gadget-only rows have disjoint clique complements \(H_1,H_2\) with one of the exact profiles
\[
(5,5),(5,4),(5,3),(4,4),(5,2),(4,3),(5,1),(4,2),(3,3).
\]
Writing \(d_K\) for their total partial component incidence and \(d_U\) for repeated gadget incidence, the row identity gives \(d_K+d_U=6\), while \(d_U\ge a=11-|H_1|-|H_2|\). Therefore
\[
d_K\le |H_1|+|H_2|-5.
\]
For profiles \((5,5)\) and \((5,4)\), \(d_K\le5\) or \(4\), so one of the two high rows has at most two partial component incidences. The checker verifies alignment for each \(H_1\) and \(H_2\) separately. For every other profile \(d_K\le3\), so either high row has at most three partial component incidences and is safe for the construction below.

The exact verifier, verify_p49_r6_gadget_exclusion.py, checks the finite gadget selection. For the selected high complement \(H\), the \(r=2\) pair \(Q_1,Q_2\), and every nonempty set of \(r=1\) complement-pair types that can occur among the five low-budget blocks, it finds a \(K_5\) core \(D\), a selected \(Q\in\{Q_1,Q_2\}\), and a compatible omitted \(K_5\) set \(L\) for every low-pair type such that:
1. \(D\) is disjoint from \(H,Q,L\);
2. \(H\cap Q\ne\varnothing\) and \(H\cap L\ne\varnothing\);
3. some \(z\in U_C\setminus(D\cup H)\) is adjacent in color \(C\) to at least one vertex of \(D\), or is outside \(Q\), or is outside one selected \(L\).

The third condition gives \(z\) a \(C\)-edge to the high-block representative and at least one additional \(C\)-edge into the proposed clique. The \(r=1\) selected rows have no component-vertex incidences. The \(r=2\) selected row has at most one partial component incidence. The high row is chosen with at most two partial component incidences in the risky profiles, and at most three in the other profiles. Thus no pair of selected row-neighborhoods can cover all five vertices of an isolated \(K_5\) component.

All selected omitted sets lie in \(U_C\setminus D\). Their intersections are forced by conditions 2–3 and the fact that \(Q,L\) have size four or five inside this six-set. Consequently, for any two selected outer rows, a gadget vertex is missed by both. Since their neighborhoods do not cover a full isolated \(K_5\) component, one can choose one vertex from each of the ten isolated components and this common missed gadget vertex. If the two outer rows were not \(C\)-adjacent, these eleven residual vertices plus the two rows would be a \(C\)-independent 13-set. Hence all seven selected outer rows are pairwise \(C\)-adjacent. They also all see \(D\), so \(D\) and the seven rows form a \(C\)-colored \(K_{12}\).

The verifier supplies an external \(z\) with at least two \(C\)-edges into this \(K_{12}\), contradicting Lemma 12.1. \(\square\)

### Finite-verifier record and scope

The revised exact checker covers all four gadget normal forms, all disjoint \(r=1\) \(K_5/K_5\) pairs, all \(r=2\) \(K_5/K_5\) and \(K_5/K_4\) pairs, every nonempty subset of low-block pair types, and the exact Case-C complement-size profiles. The in-session replay of these predicates passed 2,132 Case-A/B configurations and 512,768 exact-profile Case-C configurations (514,900 total). For risky Case-C profiles \((5,5)\) and \((5,4)\), it checks both high-row choices; for the other profiles, it checks the existence of a safe high-row choice. No single-external-edge contradiction is used.

This theorem is conditional on the retained reduction, exact-129 factor theorem, gadget normal form, and row-incidence classifications. It excludes the \(P_C=49,r_i=6\) corner under those contracts; it does not establish \(P_C\le49\), close the aggregate eleven-color ledger, or prove the original \(K_{145}\) theorem.
