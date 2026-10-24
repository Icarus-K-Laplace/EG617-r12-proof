# High-multiplicity witness-star lemma

Date: 2026-10-25  
Status: **PROVED structural reduction; terminal exclusion OPEN.**

## 1. Setup

Let \(H\) be the 47-vertex core with
\[
\alpha(H)\le4,\quad \omega(H)\le11,\quad
d_H(v)=12+\varepsilon_v,\quad
\varepsilon_v\ge0,\quad \sum_{v\in H}\varepsilon_v=4.
\]
Let \(B\) be the ten-vertex target clique from an eligible E407 Q32 / E408 Q33-d3 shell-support contract. A labelled witness is an independent 4-set \(Q_b\subset H\) anticomplete to its label \(b\in B\), arising from a \(K_5\) component \(\{b\}\cup Q_b\) of a non-target color.

Different labelled witnesses from distinct color components intersect in at most one vertex. A single core vertex \(x\) can belong to at most ten witnesses, because the witness labels \(b\) must be distinct: if \(x\in Q_b\cap Q_{b'}\) and \(b=b'\) across two colors, edge \(xb\) would have two colors.

## 2. Common-vertex structure

**Lemma 2.1.** Suppose \(m\) distinct witnesses share a core vertex \(x\):
\[
Q_i=\{x\}\cup P_i,\qquad |P_i|=3.
\]
Then the \(P_i\) are pairwise disjoint independent triples, \(x\) is anticomplete to \(U:=\bigcup_iP_i\), and
\[
\alpha(H[U])\le3,\qquad
e(H[U])\ge 3\binom m2.
\]
Moreover, every \(y\in P_i\) has at least \(m-1\) neighbours in \(H[U]\).

**Proof.** The \(P_i\) are independent because each \(Q_i\) is independent. If two \(P_i,P_j\) shared a vertex, the corresponding witnesses would share that vertex and \(x\), contradicting the one-vertex intersection rule. Thus the triples are disjoint. The vertex \(x\) is nonadjacent to every \(P_i\). An independent 4-set in \(H[U]\), together with \(x\), would be an independent 5-set in \(H\), so \(\alpha(H[U])\le3\).

By Turán's theorem, the complement of \(H[U]\) is \(K_4\)-free and has at most \(t_3(3m)\) edges. Therefore
\[
e(H[U])\ge \binom{3m}{2}-t_3(3m)
=3\binom m2.
\]
Finally, if \(y\in P_i\) had no neighbour in some \(P_j\), then \(\{x,y\}\cup P_j\) would be an independent 5-set. So \(y\) has at least one neighbour in each of the other \(m-1\) triples. \(\square\)

## 3. The extreme \(m=10\) star

If \(m=10\), the ten witness labels exhaust \(B\), so \(x\) is anticomplete to all of \(B\), and \(|U|=30\). Lemma 2.1 gives
\[
e(H[U])\ge135.
\]
Also \(e(H[U])\le180+\varepsilon_U/2\le182\), since the 30 vertices of \(U\) have total core degree \(360+\varepsilon_U\).

A stronger near-equality classification follows from the second Turán theorem. Let \(L=\overline{H[U]}\). Then \(L\) is \(K_4\)-free and has
\[
e(L)=435-e(H[U]).
\]
If \(e(H[U])\le143\), then \(e(L)\ge292\). The second Turán bound for a non-tripartite \(K_4\)-free graph on 30 vertices is
\[
e(L)\le t_3(30)-10+1=291.
\]
So \(L\) must be complete tripartite. Each \(P_i\) is a triangle in \(L\), and the ten \(P_i\) are disjoint; hence each tripartition class has at least ten vertices. Since \(|U|=30\), all three classes have size ten. Therefore
\[
e(H[U])=135,\qquad H[U]=3K_{10}.
\]
Consequently the only possibilities are
\[
\boxed{e(H[U])=135\quad\text{or}\quad e(H[U])\ge144.}
\]

## 4. The \(135\)-edge equality case forces positive excess at \(x\)

**Lemma 4.1.** In the \(m=10\) star, if \(e(H[U])=135\), then \(\varepsilon_x\ge1\).

**Proof.** The previous section gives \(H[U]=K_{10}\dot\cup K_{10}\dot\cup K_{10}\). The vertex \(x\) is anticomplete to \(U\). If \(\varepsilon_x=0\), then \(d_H(x)=12\), so among the other 16 vertices of \(H\setminus(U\cup\{x\})\), exactly four are non-neighbours of \(x\). Call this set \(Y\).

For any \(y\in Y\), the set \(Y\) is not being used here as a whole; rather, \(y\) is nonadjacent to \(x\). To avoid an independent 5-set consisting of \(x,y\) and one vertex from each of the three \(K_{10}\) cliques, \(y\) must be adjacent to every vertex of at least one of those cliques. Otherwise choose a non-neighbour of \(y\) from each clique.

There are four vertices in \(Y\) and three \(K_{10}\) cliques, so two vertices \(y,z\in Y\) are complete to the same \(K_{10}\). They must be nonadjacent to each other, since otherwise that \(K_{10}\cup\{y,z\}\) is a \(K_{12}\), contradicting \(\omega(H)\le11\).

Each of \(y,z\) has at most \(2+\varepsilon_y\) and \(2+\varepsilon_z\) neighbours outside their common \(K_{10}\). Since \(\varepsilon_y+\varepsilon_z\le4\), their combined outside-neighbour sets have size at most eight. Thus in each of the other two \(K_{10}\) cliques there is a vertex \(u\), respectively \(v\), nonadjacent to both \(y,z\). The vertices \(u,v\) are nonadjacent because they lie in different cliques. Now \(x,y,z,u,v\) are pairwise nonadjacent, contradicting \(\alpha(H)\le4\).

Hence \(\varepsilon_x\ne0\). \(\square\)

## 5. What this reduction buys

A ten-witness star cannot be treated as an arbitrary overlap pattern. It forces one of two sharply separated core regimes:

- **dense-union regime:** \(e(H[U])\ge144\);
- **Turan-equality regime:** \(H[U]=3K_{10}\), but then the common vertex has \(\varepsilon_x\ge1\).

In the equality regime, each of the 30 vertices in \(U\) has nine core neighbours inside \(U\), and therefore at least \(3+\varepsilon_y\) neighbours outside \(U\). The remaining 17 core vertices must support all those cross-edges while \(x\) is anticomplete to \(U\).

This does not yet rule out either regime. The next step is to combine the \(3K_{10}\) equality structure or the \(e(H[U])\ge144\) bound with the shell-row incidence ledger and the five Q32 template labels.