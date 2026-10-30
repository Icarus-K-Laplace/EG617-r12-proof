# V47 low-layer exclusion by a tight part and seven clean blocks

Date: 2026-10-30

## Theorem

Let H be a graph on 47 vertices with
\[
e(H)=285,\qquad \delta(H)\ge12,\qquad
\alpha(H)\le4,\qquad \omega(H)\le5.
\]
Then H has no partition into eleven independent 4-sets and one independent 3-set.

Equivalently, in the Q32 core, no non-target color C can satisfy \(e_C(H)\le70\), because the registered 69/70 near-Turán theorem supplies precisely such a partition whenever
\[
\alpha(C[H])\le12,\quad \omega(C[H])\le4,\quad e_C(H)\le70.
\]
The first two conditions are the established balanced-color and target-independence premises.

The proof actually gives a dichotomy: from any such partition and any choices of the Hall matchings below, either H has an independent 5-set or H has a K7.

## 1. Hall matching skeleton

Write the partition as
\[
H=P_1\sqcup\cdots\sqcup P_{11}\sqcup P_{12},
\quad |P_i|=4\ (i\le11),\quad |P_{12}|=3.
\]
Every part is independent in H.

For any two 4-parts A,B, the bipartite graph H[A,B] has a perfect matching. Otherwise Hall gives S subset A with |N_B(S)|<|S|, and then \(S\cup(B\setminus N_B(S))\) is an independent set of size at least five. The same argument for a 4-part A and the 3-part B gives a matching saturating B.

Choose these matchings independently for all part pairs and let M be their union. Then
\[
e(M)=4\binom{11}{2}+3\cdot11=220+33=253.
\]
Each 4-part has three vertices of M-degree 11 and one of M-degree 10. Each vertex of the 3-part has M-degree 11. Put \(F=H\setminus M\). Then
\[
e(F)=285-253=32.
\]

## 2. Five tight 4-parts

For each part define \(\rho_i=\sum_{v\in P_i}d_F(v)\). Since \(d_H(v)\ge12\):
- in each 4-part, the three M-degree-11 vertices have F-degree at least 1 and the M-degree-10 vertex has F-degree at least 2, so \(\rho_i\ge5\);
- in the 3-part, all three vertices have M-degree 11, so \(\rho_{12}\ge3\).

As \(\sum_i\rho_i=2e(F)=64\),
\[
\sum_{i=1}^{11}(\rho_i-5)+(\rho_{12}-3)=64-55-3=6.
\]
All terms are nonnegative integers. Therefore at most six of the eleven 4-parts have \(\rho_i>5\), and at least five 4-parts are tight:
\[
\rho_i=5.
\]

Fix one tight 4-part P. Equality in its degree lower bound forces its vertices to have F-degrees exactly
\[
(1,1,1,2).
\]
Call the three degree-one vertices \(u_1,u_2,u_3\). They are pairwise nonadjacent because P is independent in H, and each has exactly one F-neighbor.

## 3. Seven clean 4-parts

There are ten other 4-parts. Each of \(u_1,u_2,u_3\) has only one F-neighbor, so at most three of these ten parts contain an F-neighbor of one of the leaves. Hence at least seven other 4-parts are clean: no F-edge joins any \(u_\ell\) to such a part Q.

For a clean Q, the selected matching M[P,Q] is a perfect matching. It sends the three leaves \(u_1,u_2,u_3\) to three distinct vertices of Q. Because Q is clean, these are their only H-neighbors in Q. Let \(w_Q\) be the fourth vertex of Q. Then
\[
w_Q\not\sim_H u_1,u_2,u_3.
\]

Choose seven distinct clean parts \(Q_1,\ldots,Q_7\), and write \(w_i=w_{Q_i}\).

For every i≠j, if \(w_iw_j\notin E(H)\), then
\[
\{u_1,u_2,u_3,w_i,w_j\}
\]
is an independent 5-set. Therefore:
- if \(\alpha(H)\le4\), all \(w_iw_j\) must be edges, and \(\{w_1,\ldots,w_7\}\) is a K7;
- if \(\omega(H)\le5\), at least one pair \(w_i,w_j\) is a nonedge, giving an independent 5-set.

Thus every such partition forces
\[
\boxed{\alpha(H)\ge5\quad\text{or}\quad\omega(H)\ge7.}
\]
This contradicts the Q32 premises \(\alpha(H)\le4\) and \(\omega(H)\le5\).

## 4. Consequence for all eleven non-target colors

For each non-target color C, the established near-Turán theorem gives the 11K4+K3 partition if \(e_C(H)\le70\). The theorem above excludes that partition. Hence
\[
\boxed{e_C(H)\ge71\qquad(c=1,\ldots,11).}
\]

Together with the exact gap ledger,
\[
\sum_{c=1}^{11}(e_C(H)-69)=37,
\]
this gives the sharper nonnegative slack decomposition
\[
\boxed{\sum_{c=1}^{11}(e_C(H)-71)=15.}
\]
In particular every one of the eleven colors has at least two units of gap above the Turán baseline, and only 15 units remain to distribute.

This is a proven lower-bound strengthening. It does not by itself close m=8 or m=9; the remaining work must attack the 71+-edge layers and their source/gadget compatibility.

## Status and scope

**PROVED**, conditional only on the already registered 69/70 near-Turán theorem and the Q32 premises \(e(H)=285\), \(\delta(H)\ge12\), \(\alpha(H)\le4\), \(\omega(H)\le5\).

The proof does not use a solver result, does not assume any Type-I special-factor placement, and does not import m=10-only constraints.
