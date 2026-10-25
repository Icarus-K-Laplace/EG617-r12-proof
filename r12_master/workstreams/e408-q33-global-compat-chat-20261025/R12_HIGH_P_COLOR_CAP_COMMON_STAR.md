# Conditional colorwise cap \(P_C\le49\) from a common-star gadget certificate

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the registered exact-129 factor theorem, seven-block equality system, row-complement profile theorem for \(r_i(C)\le5\), pairwise-blocker lemma, and exact 11-point gadget normal form.  
Scope: establishes \(P_C\le49\) for each exact-129 color. It does **not** close the aggregate eleven-color ledger, E408 Q33, or the original \(K_{145}\) theorem.

## 1. Contract and notation

Fix an exact-129 color \(C\). Its residual graph is the disjoint union of ten isolated \(K_5\) components and an 11-vertex gadget \(U_C\). Under the exact-129 contract,
\[
\alpha(C[U_C])=2,\qquad \omega(C[U_C])=5.
\]
The seven target blocks have positive duplicate budgets \(r_1,\ldots,r_7\) satisfying
\[
P_C+\sum_{i=1}^7r_i=62.
\]
For a block with \(r_i\le5\), the row theorem gives two no-full-component rows. Let \(H_i,H_i'\) be the complements in \(U_C\) of their \(C\)-neighborhoods. They are disjoint cliques, and their allowed size profiles are
\[
\begin{array}{c|l}
r_i & (|H_i|,|H_i'|)\\ \hline
1 &(5,5)\\
2 &(5,5),(5,4)\\
3 &(5,5),(5,4),(5,3),(4,4)\\
4 &(5,5),(5,4),(5,3),(4,4),(5,2),(4,3)\\
5 &(5,5),(5,4),(5,3),(4,4),(5,2),(4,3),(5,1),(4,2),(3,3).
\end{array}
\]
The finite checker deliberately enumerates **every** pair of disjoint gadget cliques with one of these size profiles, including pairs that might not be realizable by an actual row system. This is an over-approximation and therefore a safe finite test.

## 2. Common-star gadget lemma

**Lemma 2.1 (common \((D,w)\) property).** Suppose \(1\le r_i\le5\) and \(\sum_i r_i\le12\). For every choice of one allowed complement pair \(\{H_i,H_i'\}\) for each of the seven blocks, there exist a \(C\)-colored \(K_5\), \(D\subset U_C\), and a vertex \(w\in U_C\setminus D\) such that, for every \(i\), one member \(G_i\in\{H_i,H_i'\}\) satisfies
\[
w\in G_i,\qquad G_i\cap D=\varnothing.
\]

**Finite proof certificate.** The exact gadget normal form has four representatives, indexed by \(b=1,2,3,4\). For each representative and each budget \(r=1,\ldots,5\), the verifier enumerates all disjoint clique pairs with the registered sizes. A pair contributes the candidate set of all \((D,w)\) for which at least one of its two cliques contains \(w\) and avoids \(D\). The dynamic program forms every possible intersection of these candidate sets over all seven blocks. The empty intersection is unreachable in all cases.

Reproducible checker: verify_high_p_common_star.py. It checks 18 nonincreasing seven-block profiles with total \(7\) through \(12\) and maximum at most \(5\), across all four gadget normal forms (72 profile/form pairs). It enumerates 2,405,684 DP transitions, with maximum 2,625 reachable intersection states; no empty state occurs. The enumerated row-pair counts for budgets \(1,\ldots,5\) are \((3,31,148,438,940)\) for \(b=1,4\) and \((2,22,112,352,794)\) for \(b=2,3\).

## 3. From a common star to a forbidden \(K_{12}\)

Select the rows whose complements are \(G_i\) from Lemma 2.1. Every \(G_i\) contains the same \(w\), so all pairs of selected complements intersect. Also, all \(G_i\) avoid \(D\), so every selected row is \(C\)-adjacent to all five vertices of \(D\).

Let \(p_i\) be the number of vertices from the ten isolated \(K_5\) components occurring in the selected no-component row of block \(i\). The exact row-incidence identity gives
\[
p_i\le r_i-a_i\le r_i-1,
\]
because the overlap parameter \(a_i=11-|H_i|-|H_i'|\) is at least one. If \(p_i+p_j\le4\), the two selected rows cannot jointly cover a full isolated \(K_5\). The pairwise-blocker lemma then says that two such rows can be \(C\)-nonadjacent only if their gadget complements are disjoint. Since both contain \(w\), they must be \(C\)-adjacent.

Consequently, whenever \(p_i+p_j\le4\) for every pair \(i\ne j\), the seven selected rows and \(D\) form a \(C\)-colored \(K_{12}\), call it \(Q\).

Now put \(V'=U_C\setminus D\), so \(|V'|=6\), and define \(O_i=V'\setminus G_i\). Since \(G_i\) is a clique in a gadget with \(\omega(C[U_C])=5\), each \(|G_i|\le5\), hence \(|O_i|\ge1\). Therefore
\[
\sum_{i=1}^7|O_i|\ge7>|V'|=6.
\]
By pigeonhole, some \(z\in V'\) belongs to at least two of the \(O_i\). Equivalently, \(z\notin G_i,G_j\) for two selected rows, so \(z\) is \(C\)-adjacent to at least two vertices of \(Q\).

But the balanced-coloring star-capacity lemma says every vertex outside a monochromatic \(K_{12}\) has at most one incident \(C\)-edge into that clique: its twelve edges to the clique must include each of the other eleven colors, or the clique plus that vertex is an independent 13-set in a missing color. Thus \(d_C(z,Q)\ge2\) is a contradiction.

## 4. Application to \(P_C\ge51\)

If \(P_C\ge51\), then \(\sum_i r_i=62-P_C\le11\). Since the seven budgets are positive, for any pair \(i,j\),
\[
r_i+r_j\le \sum_k r_k-5\le6.
\]
Hence
\[
p_i+p_j\le(r_i-1)+(r_j-1)\le4.
\]
Lemma 2.1 and Section 3 apply, excluding every \(P_C\ge51\) profile. Therefore \(P_C\le50\).

## 5. Application to \(P_C=50\)

Here \(\sum_i r_i=12\). The seven positive integer profiles, up to permutation, are exactly
\[
\begin{split}
&(6,1^6),\quad (5,2,1^5),\quad (4,3,1^5),\\
&(4,2,2,1^4),\quad (3,3,2,1^4),\\
&(3,2,2,2,1^3),\quad (2^5,1^2).
\end{split}
\]

The first three are excluded by the separate audited double-star results:
- \((6,1^6)\): R12_P50_R6_DOUBLE_STAR_EXCLUSION.md;
- \((5,2,1^5)\) and \((4,3,1^5)\): R12_P50_REMAINING_HIGH_PROFILES_EXCLUSION.md.

For the other four profiles, the two largest budgets sum to at most six. Thus \(r_i+r_j\le6\) for every pair, and the same \(p_i+p_j\le4\) argument applies. Lemma 2.1 excludes all four profiles.

Combining Sections 4–5 gives the conditional colorwise cap
\[
\boxed{P_C\le49\quad\text{for every exact-129 color }C.}
\]

## 6. Scope firewall

This repairs the earlier \(P_C\le49\) claim **without** using the false inference that a monochromatic \(K_{12}\) has no external edge of its color. The only external-edge input is the valid star-capacity bound \(d_C(z,Q)\le1\).

The stronger claim \(P_C\le48\) (excluding \(P_C=49\)) remains **NOT CERTIFIED**; the old P49/P48 drafts remain on audit hold. The new \(P_C\le49\) theorem is conditional on the upstream exact-129 factor, row-complement, pairwise-blocker, and seven-block contracts. It does not solve the aggregate eleven-color compatibility problem, E408 Q33, E407 Q32, E408 Q32, or EG617(\(r=12\)).
