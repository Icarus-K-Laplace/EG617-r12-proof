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

For every \(x\in U\), let \(t_x=|\{i:o_i=x\}|\), setting \(t_x=0\) for \(x\notin O\). Thus \(t_x\ge1\) on \(O\) and \(\sum_{x\in O}t_x=10\). Let \(r_x=d_R(x)\) and \(c_x=d_H(x,W)\). The \(10-t_x\) blocks containing \(x\) contribute \(3(10-t_x)\) distinct complement neighbors, hence
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
Using (1), the exact form is
\[
3t(S)\le 12+2s+\binom{s}{2}-e_W-c_S-\epsilon_{U\setminus S}.
\tag{3a}
\]
Since \(e_W\ge2\), this implies
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

Suppose \(e_W=2\). If \(e_R[A]=2\), use the sharper bound \(\sum_{x\in A}r_x\le e_R+2\). It gives \(c_A+\epsilon_{U\setminus A}\le0\), hence \(c_A=0\). The two edges of \(R[A]\) give an independent pair in \(H[A]\), and \(W\) has an independent triple; since \(c_A=0\), their union is an independent five-set.

If instead \(e_R[A]=3\), then (5) gives \(c_A\le1\), while \(A\) is an independent triple in \(H\). Let \(Z\subseteq W\) consist of vertices having no \(H\)-neighbor in \(A\). The set \(Z\) must be a clique in \(H[W]\), or an independent pair in \(Z\) together with \(A\) would be an independent five-set. Since \(e_W=2\), every clique in \(H[W]\) has size at most two, so at least four vertices of \(W\) have an \(H\)-neighbor in \(A\). This requires \(c_A\ge4\), contradicting \(c_A\le1\).

All cases with \(k=7\) are impossible. Hence \(k\ge8\). \(\square\)

## What this does and does not close

- **Closed conditionally:** the support-41 exact-component terminal cannot have only \(5,6,\) or \(7\) distinct omitted points among the ten exact colors.
- At this stage the surviving omission counts are \(k=8,9,10\). The endpoint lemmas below eliminate \(k=8,e_W=2,4\) and reduce \(k=8,e_W=3\) to a \(3K_2\) incidence kernel; \(k=9,10\) remain open.
- **Not proved:** \(|U_{\rm comp}|=41\) is impossible; the full exact-color ledger; E407/E408 terminal closure; the \(K_{145}\)-to-T61 bridge; or EG617(r=12).
- **Dependency firewall:** the result requires the exact-129 factor theorem and the 284-edge core contract. It does not use a claim that a monochromatic \(K_{12}\) has no single external edge of its own color.


## Further reduction of the \(k=8\) boundary

At \(k=8\), inequality (3) leaves only the multiplicity patterns
\[
(3,1^7)\quad\text{or}\quad(2,2,1^6).
\]
Let \(N=U\setminus O\), so \(|N|=33\). Then
\[
c=76-\epsilon_U-2e_W,\qquad
c_N=66+r_N+\epsilon_N,\qquad
c_O=10-2e_W-r_N-2\epsilon_N-\epsilon_O.
\]

### Lemma 14.1: \(e_W=5\) is impossible

If \(e_W=5\), the cross-edge floor \(c\ge66\) forces \(\epsilon_U=0\), \(c=66\), \(c_O=0\), and \(r_N=0\). Thus \(e_R=7\), and all \(R\)-edges lie inside \(O\).

- For pattern \((3,1^7)\), the triple-omitted point has \(R\)-degree 7, so it is \(R\)-adjacent to all seven other omitted points.
- For pattern \((2,2,1^6)\), the two double-omitted points each have \(R\)-degree 4, and the six other omitted points each have \(R\)-degree 1. The two degree-four points must be adjacent in \(R\): otherwise they would require eight incidences to six degree-one vertices.

Either case supplies an \(R\)-edge \(xy\) inside \(O\), hence an independent pair in \(H\), with no \(H\)-edges from \(O\) to \(W\). Since a six-vertex graph with five edges has an independent triple, \(x,y\) plus that triple form an independent five-set. Contradiction. Therefore \(e_W\le4\).

### Lemma 14.2: the \((3,1^7), e_W=4\) branch is a rigid star terminal

Let \(x\) be the triple-omitted point. The singleton subset inequality gives
\[
c_x+\epsilon_{U\setminus\{x\}}\le1.
\]
For this pattern, the exact cross-edge ledger is
\[
c_O=2-\epsilon_x-\epsilon_Y-2\epsilon_N-r_N,
\tag{14.2}
\]
where \(\epsilon_Y=\sum_{y\in Y}\epsilon_y\), \(\epsilon_N=\sum_{n\in N}\epsilon_n\), and \(r_N=\sum_{n\in N}r_n\). Indeed \(c=68-\epsilon_U\), while \(c_N=66+r_N+\epsilon_N\). In particular \(c_O\le2\).

If \(c_x=0\), the singleton inequality gives \(\epsilon_Y+\epsilon_N\le1\), and (14.2), with \(c_O\ge0\), gives \(\epsilon_x\le2\) and \(r_N\le2\). Thus \(r_x=7-\epsilon_x\ge5\), and at least three \(R\)-neighbors of \(x\) lie in \(Y\). At most two points of \(Y\) have a positive \(H\)-degree into \(W\), since \(c_O\le2\); therefore one of those \(R\)-neighbors \(y\) has \(c_y=0\). The pair \(x,y\), together with an independent triple in \(W\), contradicts \(\alpha(H)\le4\). Hence \(c_x=1\) and \(\epsilon_{U\setminus\{x\}}=0\).

Applying the exact bound (3a) to each pair \(\{x,y\}\), with \(t_x+t_y=4\), \(e_W=4\), \(c_x=1\), and \(\epsilon_{U\setminus\{x,y\}}=0\), forces \(c_y=0\). Now \(c_O=1\), \(\epsilon_Y=\epsilon_N=0\), and (14.2) gives \(\epsilon_x+r_N=1\). Thus \(\epsilon_x\in\{0,1\}\) and \(r_N=1-\epsilon_x\). It follows that \(e_R=8-\epsilon_x=r_x\), so every residual edge is incident to \(x\); \(x\) is \(R\)-adjacent to all seven other omitted points, and possibly one point of \(N\`.

Finally, each \(y\ne x\) is nonadjacent to \(x\) in \(H\) and has no \(H\)-neighbor in \(W\). Therefore every independent triple in \(W\) must contain the unique \(H\)-neighbor \(w\) of \(x\) in \(W\). It follows that \(w\) is isolated in \(H[W]\), and \(H[W\setminus\{w\}]\) has five vertices, four edges, and independence number at most two. The equality case of Mantel's theorem identifies it as \(K_3\cup K_2\). Hence
\[
H[W]\cong K_3\cup K_2\cup K_1.
\]

This is a rigid conditional terminal at this point in the reduction. Lemma 14.4 below excludes it; Lemmas 14.5–14.6 handle the remaining \(e_W=2,3\) endpoints.


### Lemma 14.3: the \((2,2,1^6), e_W=4\) branch is impossible

Let \(A=\{a,b\}\) be the two double-omitted points and \(Y=O\setminus A\) the six single-omitted points. We have \(c_O\le2\), and
\[
e_R[O]\ge r_O-e_R=6+c_O+\epsilon_N\ge6.
\]
Any \(R\)-edge inside \(O\) must meet \(T=\{x\in O:c_x>0\}\), because otherwise its endpoints are nonadjacent in \(H\), have no \(H\)-neighbors in \(W\), and together with an independent triple of \(W\) form an independent five-set. Since \(c_O\le2\), \(|T|\le2\).

The set T is nonempty because e_R[O] is at least 6 and every R-edge inside O must meet T. If |T|=1, then c_O is at least 1, so r_N + 2 epsilon_N + epsilon_O is at most 1. Thus r_N<=1 and epsilon_O<=1. Any double-omitted point a outside T then has r_a=4-epsilon_a>=3, but it can have at most one R-neighbor in O and at most r_N<=1 R-neighbors in N, giving r_a<=2, contradiction. Therefore |T|=2. With |T|=2, c_O=2 and the identity for c_O forces r_N=epsilon_N=epsilon_O=0. If T contained only one of the two double-omitted points, the other would have r=4 but could have R-neighbors only among the two points of T, impossible. Hence T consists of both double-omitted points.

It follows that \(c_a=c_b=1\), \(c_O=2\), and the identity for \(c_O\) forces \(\epsilon_O=\epsilon_N=r_N=0\). Hence \(r_a=r_b=5\), while each \(y\in Y\) has \(r_y=1\). Every \(R\)-edge in \(O\) meets \(A\), and the six degree-one vertices of \(Y\) each use one edge to \(A\). Therefore the degree sum of \(A\) in \(R\) is either \(6\) or \(8\), depending on whether \(ab\in R\). But \(r_a+r_b=10\), contradiction.

Consequently, among the \(k=8,e_W=4\) states, only the \((3,1^7)\) rigid star terminal of Lemma 14.2 remains.


### Lemma 14.4: the remaining \((3,1^7), e_W=4\) star terminal is impossible

Continue under Lemma 14.2. Write \(O=\{x\}\cup Y\), where \(|Y|=7\) and \(t_x=3\), \(t_y=1\) for \(y\in Y\). Write \(W=A\dot\cup B\dot\cup\{w\}\), with \(H[A]\cong K_3\), \(H[B]\cong K_2\), and \(w\) isolated in \(H[W]\). Let \(N=U\setminus O\), so \(|N|=33\). All vertices of \(U\setminus\{x\}\) have zero excess; \(\epsilon_x\in\{0,1\}\), and
\[
\epsilon_W=4-\epsilon_x.
\]
The residual complement graph \(R\) is a star centered at \(x\): its seven edges \(xy\), \(y\in Y\), are always present, and there is one additional edge \(xn_0\), \(n_0\in N\), exactly when \(\epsilon_x=0\).

First, \(H[Y]\cong K_7\). Indeed, \(x\) is nonadjacent in \(H\) to every \(y\in Y\), and both \(x\) and \(Y\) are anticomplete to \(W\setminus\{w\}\). If distinct \(y,z\in Y\) were nonadjacent in \(H\), then \(x,y,z\), one vertex of \(A\), and one vertex of \(B\) would be an independent five-set. Hence every pair in \(Y\) is an \(H\)-edge. Each \(y\in Y\) has degree 12, six neighbors in \(Y\), and no neighbors in \(\{x\}\cup W\); therefore
\[
|N_H(y)\cap N|=6\quad(y\in Y).
\]
Also,
\[
|N_H(x)\cap N|=d_H(x)-d_H(x,W)-d_H(x,Y)=11+\epsilon_x.
\]

For \(n\in N\), let \(S_n=N_H(n)\cap W\) and \(h_n=|N_H(n)\cap Y|\). The exact degree identity \(d_H(n,W)=2+r_n\), together with the star description of \(R\), says:
- if \(\epsilon_x=1\), every \(S_n\) has size 2;
- if \(\epsilon_x=0\), every \(S_n\) has size 2 except one \(S_{n_0}\) of size 3.

The independent-set condition forces a covering classification. For each \(a\in A,b\in B\), both \(\{x,y,a,b\}\) and \(\{y,w,a,b\}\) are independent four-sets for every \(y\in Y\). If \(h_n<7\), choose \(y\in Y\) nonadjacent to \(n\).
- If \(xn\notin E(H)\), then \(S_n\) must meet every pair \(\{a,b\}\), \(a\in A,b\in B\); equivalently \(A\subseteq S_n\) or \(B\subseteq S_n\).
- If \(xn\in E(H)\), then \(S_n\) must meet every triple \(\{w,a,b\}\); equivalently \(w\in S_n\), or \(A\subseteq S_n\), or \(B\subseteq S_n\).

Consequently every \(n\in N\) belongs to at least one of the following four sets:
\[
\begin{aligned}
X_w&=\{n:w\in S_n\},\\
X_{BB}&=\{n:B\subseteq S_n\},\\
X_{AAA}&=\{n:S_n=A\},\\
X_7&=\{n:h_n=7\}.
\end{aligned}
\tag{14.4}
\]
The set \(X_{AAA}\) has size at most one, since only \(n_0\) can have three neighbors in \(W\). The exact degree counts give
\[
|X_w|=11+\epsilon_w,\qquad
|X_{BB}|\le\left\lfloor\frac{22+\epsilon_B}{2}\right\rfloor,\qquad
|X_7|\le6.
\tag{14.5}
\]
Here \(\epsilon_w,\epsilon_B\) are the degree-excess sums on the isolated vertex and the \(K_2\), respectively; the last bound follows because each \(y\in Y\) has only six neighbors in \(N\).

If \(\epsilon_x=1\), then \(\epsilon_W=3\) and \(X_{AAA}=\varnothing\). Since \(\epsilon_B\le3-\epsilon_w\), (14.4)–(14.5) imply
\[
33\le |X_w|+|X_{BB}|+|X_7|
\le17+\epsilon_w+\left\lfloor\frac{25-\epsilon_w}{2}\right\rfloor
\le31,
\]
a contradiction.

If \(\epsilon_x=0\), then \(\epsilon_W=4\) and
\[
33\le |X_w|+|X_{BB}|+|X_{AAA}|+|X_7|
\le18+\epsilon_w+\left\lfloor\frac{26-\epsilon_w}{2}\right\rfloor.
\]
For \(\epsilon_w=0,1,2,3\), the final bound is \(31,31,32,32\), respectively, so necessarily \(\epsilon_w=4\). Then \(\epsilon_A=\epsilon_B=0\), and equality must hold in every set-size bound:
\[
|X_w|=15,\quad |X_{BB}|=11,\quad |X_{AAA}|=1,\quad |X_7|=6.
\]
As these four sets cover 33 vertices and their cardinalities sum to 33, they are pairwise disjoint. In particular, \(|X_{AAA}|=1\) means the unique degree-three vertex has \(S_{n_0}=A\), so no vertex of \(X_w\) has degree three into \(W\). Every \(n\in X_w\) therefore has \(h_n<7\) and \(S_n\) has size two, containing \(w\) but not all of \(A\) or all of \(B\). The first bullet above therefore forces \(xn\in E(H)\) for every \(n\in X_w\). This would give \(x\) at least 15 neighbors in \(N\), contradicting \(|N_H(x)\cap N|=11\).

Thus the rigid \((3,1^7),e_W=4\) terminal is impossible. Together with Lemma 14.3, **all \(k=8,e_W=4\) terminals are excluded**. Lemma 14.5 excludes \(e_W=2\); Lemma 14.6 reduces \(e_W=3\) to the \(3K_2\) incidence kernel. Hence only \(k=8,e_W=3\) remains at \(k=8\), while \(k\in\{9,10\}\) remain open. \(\square\)


### Lemma 14.5: \(e_W=2\) is impossible at support 41, \(k=8\)

Suppose \(e(H[W])=2\). Since \(\alpha(H[W])\le4\), the two edges of \(H[W]\) must be disjoint; otherwise \(H[W]\) contains a \(P_3\) and three isolated vertices, giving an independent five-set. Thus \(\alpha(H[W])=4\).

For every \(o\in O\), we must have \(c_o=d_H(o,W)\ge1\); otherwise \(o\) together with an independent four-set in \(W\) is an independent five-set. Hence \(c_O\ge|O|=8\). But the exact cross-edge ledger for \(|N|=33\) gives
\[
c_O=10-2e_W-\epsilon_O-2\epsilon_N-r_N
=6-\epsilon_O-2\epsilon_N-r_N\le6,
\]
a contradiction. Therefore \(e_W\ne2\).

### Lemma 14.6: \(e_W=3\) forces a three-edge matching

Suppose \(e_W=3\). The exact cross-edge ledger gives \(c_O\le4\). If \(\alpha(H[W])\ge4\), every \(o\in O\) must have \(c_o\ge1\), or else \(o\) plus an independent four-set in \(W\) is an independent five-set. This would give \(c_O\ge8\), impossible. Thus \(\alpha(H[W])\le3\).

Among six-vertex graphs with three edges, the nonmatching component types are \(K_3+3K_1\), \(P_4+2K_1\), \(K_{1,3}+2K_1\), and \(P_3+K_2+K_1\); each has independence number at least four. Thus
\[
H[W]\cong 3K_2.
\]
In particular, \(c_O\le4\), so at least four omitted points have \(c_o=0\).

There is also a useful incidence constraint. Let \(uv\in E(R[O])\), so \(u,v\) are nonadjacent in \(H\). If \(c_u=0\), then \(S_u=\varnothing\). The pair \(u,v\) can be extended by an independent transversal of the three matching edges unless \(S_v=N_H(v)\cap W\) contains both endpoints of at least one matching edge. Therefore every \(R[O]\)-edge incident to a zero-\(c\) omitted point must have its other endpoint with \(c_v\ge2\), and that endpoint's \(W\)-neighborhood contains a full matching edge. Since \(c_O\le4\), there are at most two such high-incidence omitted points.

This reduces the remaining \(k=8,e_W=3\) problem to a three-matching incidence kernel with at least four zero-\(c\) omitted points, at most two omitted points of \(W\)-degree at least two, and the exact residual-degree profile
\[
r_o=3t_o-2+c_o-\epsilon_o,\qquad
e_R=9-\epsilon_U,\qquad
e_R[O]\ge5+c_O+\epsilon_N.
\]
The kernel is not yet excluded. The remaining blocker is to show that the high-multiplicity omitted points cannot meet their required \(R\)-degrees through the at-most-two high-incidence points plus the bounded \(R\)-incidence into \(N\). \(\square\)


### Lemma 14.7: the \(e_W=3\) multiplicity patterns reduce to one star terminal

Assume the matching kernel of Lemma 14.6. For any \(uv\in E(R[O])\), the sets \(S_u\cup S_v\) must contain both endpoints of at least one of the three matching edges of \(H[W]\); otherwise an independent transversal of the matching avoids both neighborhoods and extends \(\{u,v\}\) to an independent five-set. Consequently:
- if \(c_u=0\), every \(R[O]\)-neighbor of \(u\) has \(c_v\ge2\);
- if \(c_u=1\), every \(R[O]\)-neighbor of \(u\) has \(c_v\ge1\).

The exact budget identity is
\[
c_O+r_N=4-\epsilon_O-2\epsilon_N\le4-\epsilon_o
\qquad(o\in O).
\tag{14.7}
\]

If \(t_o=2\) and \(c_o=0\), then \(r_o=4-\epsilon_o\). If \(c_O=0\), no edge of \(R[O]\) is possible, contradicting \(e_R[O]\ge5+c_O+\epsilon_N\ge5\). If \(c_O>0\), the first bullet bounds
\[
r_o\le\left\lfloor\frac{c_O}{2}\right\rfloor+r_N
=c_O+r_N-\left\lceil\frac{c_O}{2}\right\rceil
\le3-\epsilon_o,
\]
again a contradiction. If \(t_o=2,c_o=1\), the second bullet gives
\[
r_o\le c_O-1+r_N\le3-\epsilon_o,
\]
whereas the exact degree identity gives \(r_o=5-\epsilon_o\), impossible. Thus every multiplicity-two omitted point has \(c_o\ge2\).

For the profile \((2,2,1^6)\), both double-omitted points therefore have \(c_o\ge2\). Since \(c_O\le4\), they have \(c_o=2\) each and every singleton-omitted point has \(c_y=0\). The budget identity forces \(\epsilon_O=\epsilon_N=r_N=0\), so \(e_R=9\) and \(e_R[O]\ge9\); hence all residual edges lie in \(O\). Each of the six zero-\(c\) singleton points has \(r_y=1\) and must send its unique residual edge to one of the two double points. Those six edges contribute six to the degree sum of the double points, and the edge between the two double points contributes at most two more. But their required residual degree sum is \(r_a+r_b=6+6=12\), contradiction. Thus \((2,2,1^6)\) is impossible when \(e_W=3\).

For the profile \((3,1^7)\), let \(x\) be the triple-omitted point. The preceding argument excludes \(c_x=0\) by the same degree-cap calculation; if \(c_x=1\), then
\[
r_x=8-\epsilon_x\le c_O-1+r_N\le3-\epsilon_x,
\]
impossible. Hence \(c_x\ge2\). Since \(r_x=7+c_x-\epsilon_x\le e_R=9-\epsilon_x-\epsilon_Y-\epsilon_N\), we get
\[
c_x+\epsilon_Y+\epsilon_N\le2.
\]
Therefore \(c_x=2\), \(\epsilon_Y=\epsilon_N=0\), and \(r_x=e_R\); every residual edge is incident to \(x\). Every singleton point \(y\in Y\) has \(r_y=1+c_y\), but its residual degree is at most one because all residual edges are incident to \(x\). Hence \(c_y=0\) and \(r_y=1\) for all seven \(y\). Thus \(c_O=c_x=2\), and the budget identity gives \(r_N=2-\epsilon_x\), so \(\epsilon_x\in\{0,1,2\}\). The only surviving \(k=8,e_W=3\) profile is therefore the rigid star terminal
\[
c_x=2,\quad c_Y=0,\quad \epsilon_Y=\epsilon_N=0,\quad
R\text{ is a star at }x\text{ with leaves }Y
\text{ and }2-\epsilon_x\text{ additional leaves in }N.
\]
Moreover \(H[Y]\cong K_7\): if \(y,z\in Y\) were nonadjacent in \(H\), then \(y,z\) together with an independent transversal of the three matching edges in \(W\) would be an independent five-set. Since each \(y\in Y\) has degree 12, no H-neighbors at \(x\) or \(W\), and six neighbors in \(Y\), it has exactly six neighbors in \(N\).

This is a reduction, not yet a contradiction. The remaining blocker is to exclude this final \((3,1^7)\) star terminal under \(H[W]=3K_2\). \(\square\)
