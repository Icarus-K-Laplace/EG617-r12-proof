# Exact-component support-41 omission floor

Date: 2026-10-26  
Status: **PROVED_CONDITIONAL** under the exact-129 component factorization and the 284-edge core contract. This is a structural reduction, not a complete EG617(r=12) proof.

## Theorem

Let \(H\) be a graph on 47 vertices with
\[
e(H)=284,\qquad \delta(H)\ge12,\qquad \alpha(H)\le4.
\]
Let \(U\subseteq V(H)\) have \(|U|=41\), and write \(W=V(H)\setminus U\), so \(|W|=6\). Suppose ten exact colors each supply ten four-sets
\[
\mathcal Q_i=\{Q_{i1},\ldots,Q_{i,10}\}\subseteq \binom U4
\]
such that, for each \(i\), the ten sets partition \(U\setminus\{o_i\}\) for a unique omitted point \(o_i\), and all 100 four-sets are pairwise edge-disjoint cliques in \(\overline{H[U]}\). Let
\[
O=\{o_i:1\le i\le10\},\qquad k=|O|.
\]
Then
\[
\boxed{k\ge8.}
\]
In particular, support size 41 cannot have only five, six, or seven distinct omitted points.

The theorem uses the **full ten-component family per exact color**, not the seven-witness minimum-support family. The two support notions must not be conflated.

## Exact budget identities

For \(X\subseteq V(H)\), put
\[
\epsilon_X=\sum_{x\in X}(d_H(x)-12)\ge0,
\]
so \(\epsilon_U+\epsilon_W=4\). Write \(e_W=e(H[W])\) and \(c=e_H(U,W)\). Since \(\alpha(H[W])\le4\), a six-vertex \(W\) must have \(e_W\ge2\). The degree and edge ledgers give
\[
c=76-\epsilon_U-2e_W,
\qquad
e(H[U])=208+\epsilon_U+e_W.
\]
Thus
\[
e(\overline{H[U]})=612-\epsilon_U-e_W.
\]

The 100 edge-disjoint \(K_4\)'s use 600 distinct complement edges. Let \(R\) be the set of remaining complement edges on \(U\), and let \(e_R=|R|\). Then
\[
\boxed{e_R=12-\epsilon_U-e_W.}\tag{1}
\]

For \(x\in O\), let \(t_x=|\{i:o_i=x\}|\), so \(t_x\ge1\) and \(\sum_{x\in O}t_x=10\). Let \(r_x=d_R(x)\) and \(c_x=d_H(x,W)\). The \(10-t_x\) blocks containing \(x\) contribute \(3(10-t_x)\) distinct complement neighbors, hence
\[
d_{H[U]}(x)=10+3t_x-r_x.
\]
Writing \(\epsilon_x=d_H(x)-12\), we obtain the exact identity
\[
\boxed{r_x=3t_x-2+c_x-\epsilon_x.}\tag{2}
\]

For any \(S\subseteq O\), set \(s=|S|\), \(t(S)=\sum_{x\in S}t_x\), \(c_S=\sum_{x\in S}c_x\), and \(\epsilon_S=\sum_{x\in S}\epsilon_x\). Every edge of \(R\) contributes at most once to the degree sum on \(S\), except an edge internal to \(S\), which contributes twice. Therefore
\[
\sum_{x\in S}r_x
=3t(S)-2s+c_S-\epsilon_S
\le e_R+\binom{s}{2}.
\]
Using (1) and \(e_W\ge2\),
\[
\boxed{3t(S)\le 10+2s+\binom{s}{2}-c_S-\epsilon_{U\setminus S}.}\tag{3}
\]
In particular:
\[
t_x\le4,\qquad t_x+t_y\le5,\qquad
t_x+t_y+t_z\le6.\tag{4}
\]
The only nondecreasing positive multiplicity patterns for \(k=5,6,7\) consistent with (4) are respectively
\[
(2^5),\qquad (1^2,2^4),\qquad
(1^6,4),\ (1^5,2,3),\ (1^4,2^3).
\]
These are integer consequences of (3), not graph-search claims.

## Excluding \(k=5\)

The pattern is \(t_x=2\) for all five \(x\in O\), and \(|U\setminus O|=36\). Every \(x\in U\setminus O\) has \(t_x=0\), so (2) gives \(d_H(x,W)=2+r_x+\epsilon_x\ge2\). Hence
\[
c\ge72.
\]
But \(c=76-\epsilon_U-2e_W\le72\), forcing \(e_W=2\), \(\epsilon_U=0\), and \(c=72\). Thus \(c_O=0\), every \(x\in U\setminus O\) has \(r_x=0\), and all ten edges of \(R\) lie inside \(O\). Equation (2) gives \(r_x=4\) for each of the five omitted points. Consequently \(R[O]=K_5\), so \(O\) is an independent five-set in \(H\), contradicting \(\alpha(H)\le4\).

## Excluding \(k=6\)

By (4), the multiplicity pattern is \(t=2\) on a four-set \(A\subset O\) and \(t=1\) on the other two points. Since \(|U\setminus O|=35\), the non-omitted points contribute at least 70 cross edges, so
\[
\epsilon_U+2e_W\le6.
\]
For the four-set \(A\), equation (2) gives
\[
\sum_{x\in A}r_x=16+c_A-\epsilon_A.
\]
On the other hand,
\[
\sum_{x\in A}r_x\le e_R+e_R[A]
\le (12-e_W-\epsilon_U)+6.
\]
Combining these and using \(\epsilon_U-\epsilon_A=\epsilon_{U\setminus A}\ge0\) yields
\[
e_W+c_A+\epsilon_{U\setminus A}\le2.
\]
Since \(e_W\ge2\), equality is forced throughout: \(e_W=2\), \(c_A=0\), and \(e_R[A]=6\). Thus \(A\) is a \(K_4\) in \(\overline H\), hence an independent four-set in \(H\), and no vertex of \(A\) has an \(H\)-edge to \(W\). Any \(w\in W\) extends \(A\) to an independent five-set, contradiction.

## Excluding \(k=7\)

The three patterns in (4) are handled separately.

### Case 1: \(t_x=4\) for one \(x\in O\)

Apply (3) with \(S=\{x\}\). Equality in \(12\le14-e_W-c_x-\epsilon_{U\setminus\{x\}}\) forces \(e_W=2\) and \(c_x=0\). A six-vertex graph with only two edges has an independent set of size at least four. Such a four-set in \(W\), together with \(x\), is independent in \(H\), contradiction.

### Case 2: multiplicities \(3,2,1,1,1,1,1\)

Let \(x,y\) have multiplicities 3 and 2. Apply (3) to \(S=\{x,y\}\). Since \(t(S)=5\), equality forces \(e_W=2\), \(c_x+c_y=0\), and \(\epsilon_{U\setminus\{x,y\}}=0\). Equation (2) gives
\[
r_x+r_y=11-\epsilon_U=e_R+1.
\]
The sum of the \(R\)-degrees of two vertices can exceed \(e_R\) only if those vertices are adjacent in \(R\); hence \(xy\in E(R)\). Thus \(x,y\) are nonadjacent in \(H\), and neither has an \(H\)-edge to \(W\). Since \(e_W=2\), \(W\) has an independent triple. Together these five vertices form an independent five-set, contradiction.

### Case 3: multiplicities \(2,2,2,1,1,1,1\)

Let \(A\) be the three points of multiplicity 2. From (2),
\[
\sum_{x\in A}r_x=12+c_A-\epsilon_A
\le e_R+e_R[A]
\le 15-e_W-\epsilon_U.
\]
Consequently
\[
\boxed{e_W+c_A+\epsilon_{U\setminus A}\le3.}\tag{5}
\]
So \(e_W\in\{2,3\}\).

If \(e_W=3\), (5) forces \(c_A=0\), \(\epsilon_{U\setminus A}=0\), and \(e_R[A]=3\). Thus \(A\) is an independent triple in \(H\), with no \(H\)-edges to \(W\). The graph \(H[W]\) has only three edges and therefore contains an independent pair; adjoining that pair to \(A\) contradicts \(\alpha(H)\le4\).

Suppose \(e_W=2\). If \(e_R[A]=2\), (5) forces \(c_A=0\). The two edges of \(R[A]\) give an independent pair in \(H[A]\), and \(W\) has an independent triple; because \(c_A=0\), their union is an independent five-set. If instead \(e_R[A]=3\), then (5) gives \(c_A\le1\), while \(A\) is an independent triple in \(H\). Let \(Z\subseteq W\) consist of vertices having no \(H\)-neighbor in \(A\). The set \(Z\) must be a clique in \(H[W]\), or an independent pair in \(Z\) together with \(A\) would be an independent five-set. Since \(e_W=2\), every clique in \(H[W]\) has size at most two, so at least four vertices of \(W\) have an \(H\)-neighbor in \(A\). This requires \(c_A\ge4\), contradicting \(c_A\le1\).

All cases with \(k=7\) are impossible. Hence \(k\ge8\). \(\square\)

## What this does and does not close

- **Closed conditionally:** the support-41 exact-component terminal cannot have only \(5,6,\) or \(7\) distinct omitted points among the ten exact colors.
- **Surviving omission patterns:** \(k=8,9,10\). Their multiplicity patterns still need separate analysis.
- **Not proved:** \(|U_{\rm comp}|=41\) is impossible; the full exact-color ledger; E407/E408 terminal closure; the \(K_{145}\)-to-T61 bridge; or EG617(r=12).
- **Dependency firewall:** the result requires the exact-129 factor theorem and the 284-edge core contract. It does not use a claim that a monochromatic \(K_{12}\) has no single external edge of its own color.
