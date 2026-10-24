# E408 Q33 universal minimum-support bound: \(S_0\ge11\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained E408 Q33/d3 shell contract, exact-129 factor theorem, and 31-point/56-witness boundary. This removes the \(S_0=10\) boundary without assuming that the witness complement is four-partite.

## 1. Frozen boundary contract

Let \(H\) be the 47-vertex core with
\[
\alpha(H)\le4,\quad \omega(H)\le11,\quad d_H(x)=12+\epsilon_x,\quad
\epsilon_x\ge0,\quad \sum_{x\in H}\epsilon_x=4.
\]
Let \(U\subset V(H)\) be the 31-point union of 56 selected independent four-sets \(\mathcal Q\), chosen as seven sets from each of eight exact-129 colors. Within each color the seven sets are disjoint; across all colors any two distinct sets intersect in at most one point. Put \(W=V(H)\setminus U\), \(|W|=16\), and \(L=\overline{H[U]}\).

The 56 witness \(K_4\) edge sets are disjoint, so
\[
e(L)=336+\delta,\quad \delta\ge0.
\]
Write
\[
\epsilon_U=\sum_{u\in U}\epsilon_u,\qquad
S_0=\epsilon_U+2\delta.
\]
Since \(e(H[U])=129-\delta\), the exact core degree ledger gives
\[
e_H(U,W)=372+\epsilon_U-2(129-\delta)
=\boxed{114+S_0}.
\]
For \(w\in W\), let \(q_w=|N_H(w)\cap U|\). Every \(w\) must hit every \(Q\in\mathcal Q\), or \(Q\cup\{w\}\) would be an independent five-set in \(H\).

## 2. Every outside vertex has at least seven core neighbours in \(U\)

A transversal \(T\subset U\) of the witness family is a set meeting every \(Q\). No such \(T\) has size at most six.

For \(t=|T|\le5\), let \(n_1\) be the number of witness sets meeting \(T\) in exactly one point and \(n_2=56-n_1\) the number meeting it in at least two points. Linearity gives
\[
n_1\le t\left\lfloor\frac{31-t}{3}\right\rfloor,\qquad
n_2\le {t\choose2}.
\]
For \(t=0,1,2,3,4,5\), the upper bounds on \(n_1+n_2\) are \(0,10,19,30,42,50\), all below 56.

For \(t=6\), each point lies in at most \(\lfloor30/3\rfloor=10\) witness sets, so the total incidence \(I(T)=\sum_Q|Q\cap T|\le60\). But \(n_1\le6\lfloor25/3\rfloor=48\), hence
\[
I(T)\ge n_1+2n_2=56+n_2\ge112-n_1\ge64,
\]
a contradiction. Therefore \(\tau(\mathcal Q)\ge7\), and in particular
\[
\boxed{q_w\ge7\quad(w\in W)}.
\]

Let \(N_7=|\{w\in W:q_w=7\}|\). Since all other \(q_w\ge8\),
\[
114+S_0=\sum_{w\in W}q_w
\ge7N_7+8(16-N_7)=128-N_7.
\]
Thus
\[
\boxed{N_7\ge14-S_0}. \tag{1}
\]

## 3. A 7-transversal is unique, and can be the neighbourhood of at most four vertices of \(W\)

Suppose \(T\subset U\) is a seven-point transversal. In each color class, its seven disjoint witness sets are hit exactly once each. For any fixed \(t\in T\), the eight witness sets containing \(t\) have pairwise-disjoint triples \(Q\setminus\{t\}\); these eight triples partition \(R:=U\setminus T\), since \(|R|=24\). Every triple is independent in \(H\), and every pair \(t,r\) with \(t\in T,r\in R\) occurs together in one witness. Hence \(T\) is anticomplete to \(R\), and \(R\) contains an independent triple.

The set \(T\) must be a clique: otherwise an independent pair in \(T\), together with an independent triple in \(R\), would be an independent five-set in \(H\).

There cannot be two distinct seven-point transversals \(T,T'\). If \(s=|T\cap T'|\), then for each of the eight color classes the \(7-s\) blocks whose \(T\)-point lies in \(T\setminus T'\) yield \(7-s\) ordered pairs in \((T\setminus T')\times(T'\setminus T)\). Across colors these pairs cannot repeat, by linearity. Thus
\[
8(7-s)\le(7-s)^2,
\]
impossible for distinct \(T,T'\), since \(1\le7-s\le7\). So there is at most one seven-point transversal.

Now let \(X_T=\{w\in W:N_H(w)\cap U=T\}\). Every \(w\in X_T\) is adjacent to all of \(T\) and anticomplete to \(R\). If \(X_T\) contained an independent pair, that pair plus an independent triple in \(R\) would violate \(\alpha(H)\le4\). Hence \(X_T\) is a clique. Since \(T\) is a clique and is complete to \(X_T\), \(T\cup X_T\) is a clique. The core contract \(\omega(H)\le11\) gives
\[
|X_T|\le4.
\]
All vertices counted by \(N_7\) have seven-point transversal neighbourhoods, and that transversal is unique. Therefore
\[
\boxed{N_7\le4}.
\]
Together with (1), this proves \(S_0\ge10\).

## 4. Equality \(S_0=10\) forces a rigid incidence kernel

Assume \(S_0=10\). Then \(e_H(U,W)=124\), so (1) and \(N_7\le4\) force \(N_7=4\). All four degree-seven vertices have the same neighbourhood \(T\), and the other 12 vertices of \(W\) must all have \(q_w=8\), because
\[
124-4\cdot7=96=12\cdot8.
\]

For a size-eight neighbourhood \(N_H(w)\cap U\), either it contains all of \(T\), or it is contained in \(R=U\setminus T\). Indeed, if it misses \(t\in T\), then it must hit all eight disjoint triples in the partition of \(R\) given by the eight witness sets containing \(t\). It therefore needs eight neighbours in \(R\), so its size-eight neighbourhood lies wholly in \(R\).

Call the first type \(T\cup\{r\}\) a **T-type** neighbourhood, and let \(a\) be the number of these among the 12 size-eight neighbourhoods. Let
\[
\epsilon_T=\sum_{t\in T}\epsilon_t.
\]
Since \(T\) is a clique anticomplete to \(R\), every \(t\in T\) has \(6+\epsilon_t\) neighbours in \(W\). Summing over \(T\), the four degree-seven vertices contribute \(28\) incidences and each T-type vertex contributes \(7\), giving
\[
42+\epsilon_T=28+7a,\qquad \epsilon_T=7a-14.
\]
At least one \(t\in T\) has \(\epsilon_t=0\), since the total core excess is four. That vertex has exactly six neighbours in \(W\), four of which are the degree-seven vertices, so \(a\le2\). The displayed identity gives \(a\ge2\). Consequently
\[
\boxed{a=2,\quad \epsilon_T=0}.
\]
Thus the remaining ten size-eight neighbourhoods are eight-sets \(S_1,\ldots,S_{10}\subset R\), each hitting every witness \(Q\).

## 5. The ten \(R\)-type neighbourhoods have multiplicity pattern \(4,3,3\)

For \(r\in R\), let \(j_r\) be its degree in the leftover graph \(J\) of edges of \(L\) not covered by witness \(K_4\)s. Since each \(r\) occurs in exactly one witness with each \(t\in T\), it belongs to seven witness sets. Their edges contribute 21 distinct edges to \(L\) at \(r\), so
\[
d_L(r)=21+j_r,\qquad d_H(r,U)=9-j_r,\qquad
d_H(r,W)=3+\epsilon_r+j_r.
\]
Every leftover edge lies inside \(R\): all \(T\)-to-\(R\) pairs occur in witnesses, and \(T\) is a clique in \(H\). Hence \(\sum_{r\in R}j_r=2\delta\).

The two T-type vertices contribute exactly two \(R\)-to-\(W\) incidences. The ten \(R\)-type neighbourhoods contribute \(80\) incidences, and for each \(r\in R\) their multiplicity is
\[
s_r=3+\epsilon_r+j_r-a_r,
\]
where \(a_r\in\{0,1,2\}\) counts T-type vertices whose extra \(R\)-neighbour is \(r\). Since \(S_0=10\) and \(\epsilon_T=0\),
\[
\sum_{r\in R}(\epsilon_r+j_r)=\epsilon_U+2\delta=10,\qquad
\sum_{r\in R}s_r=80.
\]
Also every \(r\) occurs in at least one \(R\)-type neighbourhood, since \(d_H(r,W)=3+\epsilon_r+j_r\ge3\) and the two T-type vertices can account for at most two of those neighbours.

### 5.1 Distinct \(R\)-type neighbourhoods intersect in at most one point

Let \(S,S'\subset R\) be distinct \(R\)-type neighbourhoods with \(|S|=|S'|=8\), and put \(s=|S\cap S'|\). For each \(t\in T\), the eight triples \(Q\setminus\{t\}\) partition \(R\). Both \(S,S'\) meet every triple exactly once. The \(8-s\) points of \(S\setminus S'\) are therefore paired, in each such partition, with \(8-s\) distinct points of \(S'\setminus S\). Across the seven choices of \(t\), no pair can repeat, since that would make two witness sets share two vertices. Thus
\[
7(8-s)\le(8-s)^2.
\]
For distinct sets \(8-s\ge1\), so \(s\le1\).

### 5.2 Each distinct neighbourhood occurs at most four times

If a distinct set \(S\) occurs \(m\) times, its points receive at least \(8m\) incidences from those copies. But
\[
\sum_{r\in S}s_r
=24+\sum_{r\in S}(\epsilon_r+j_r-a_r)
\le24+\sum_{r\in R}(\epsilon_r+j_r)
=34.
\]
Therefore \(8m\le34\), so \(m\le4\).

### 5.3 Exactly three distinct sets partition \(R\)

Let \(t\) be the number of distinct \(R\)-type neighbourhoods. They cover \(R\), each has size eight, and distinct ones intersect in at most one point. For \(4\le t\le10\),
\[
\left|\bigcup_{i=1}^t S_i\right|
\ge8t-\binom t2>24,
\]
impossible because \(|R|=24\). Fewer than three sets cannot cover \(R\). Thus \(t=3\), and the three distinct sets are pairwise disjoint and partition \(R\).

Their multiplicities sum to ten and are each at most four, so the only possibilities are \((4,4,2)\) and \((4,3,3)\). The pattern \((4,4,2)\) is impossible: every point of the multiplicity-two set has \(s_r=2\), so \(s_r=3+\epsilon_r+j_r-a_r\) forces \(a_r\ge1\) at all eight points of that set. But only two T-type vertices exist, each with only one \(R\)-neighbour. Therefore the multiplicities must be
\[
\boxed{(4,3,3)}.
\]

## 6. The \(4,3,3\) kernel violates \(\omega(H)\le11\)

Let \(S_1,S_2,S_3\) be the three disjoint eight-sets in \(R\), with corresponding groups \(G_1,G_2,G_3\subset W\) of multiplicities \(4,3,3\). Each \(S_i\) is a transversal of every witness set. Since each witness contains one point of \(T\) and three points of \(R\), it contains exactly one point from each \(S_i\).

For \(i\ne j\), each vertex of \(S_i\) is paired in a witness with seven distinct vertices of \(S_j\), one for each \(t\in T\). These seven pairs are nonedges of \(H\); therefore every vertex of \(S_i\) has at most one \(H\)-neighbour in \(S_j\).

**Each \(S_i\) is a clique in \(H\).** If \(u,v\in S_i\) were nonadjacent, choose \(a\in S_j\) nonadjacent to both (at most two vertices of \(S_j\) are forbidden). Then choose \(b\in S_k\) nonadjacent to \(u,v,a\) (at most three vertices of \(S_k\) are forbidden). The set \(\{u,v,a,b\}\) is independent in \(R\); adjoining any \(t\in T\), which is anticomplete to \(R\), gives an independent five-set, contradiction.

**Each \(G_i\) is a clique.** If \(w,w'\in G_i\) were nonadjacent, choose nonadjacent \(a\in S_j,b\in S_k\). Both \(w,w'\) are anticomplete to \(S_j\cup S_k\) and to \(T\), since their \(U\)-neighbourhood is \(S_i\). Thus \(\{w,w',a,b,t\}\) would be an independent five-set for any \(t\in T\), contradiction.

Every vertex of \(G_1\) is adjacent to every vertex of \(S_1\) by the definition of its neighbourhood. Since \(S_1\) is a clique of size eight and \(G_1\) is a clique of size four, their union is a \(K_{12}\), contradicting \(\omega(H)\le11\).

Therefore \(S_0=10\) is impossible. Combining with \(S_0\ge10\) from Section 3 gives the universal boundary improvement
\[
\boxed{\epsilon_U+2\delta\ge11,\qquad \delta+\epsilon_U\le17.}
\]

## 7. Scope firewall

This excludes the \(S_0=10\) minimum-support kernel for E408 Q33 without assuming \(L\) is four-partite. It does **not** exclude the remaining \(S_0\ge11\) profiles, the non-minimum-support branches, E407 Q32, E408 Q32 (whose core has 285 edges/excess six), or the original \(K_{145}\) theorem. All upstream T61, exact-129 factor, and reduction dependencies remain explicit. EG617(\(r=12\)) remains OPEN / NOT_CERTIFIED.
