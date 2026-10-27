# E407 Q32 — support-block transversal capacity on W

Date: 2026-10-27  
Status: **PROVED necessary-structure theorem under the frozen 49-block contract; terminal exclusion remains OPEN.**

## 1. Contract and notation

Let \(H\) be the 47-vertex E407 core with \(\alpha(H)\le4\), \(e(H)=284\), and the frozen split \(V(H)=U\dot\cup W\), where \(|U|=29\), \(|W|=18\). Let \(\mathcal Q\) be the 49 selected independent 4-sets on U, seven pairwise-disjoint blocks in each of seven exact-129 color classes. All 49 blocks are pairwise linear. For \(u\in U\), let \(r_u\) be the number of color classes omitting u; then
\[
m_u:=|\{Q\in\mathcal Q:u\in Q\}|=7-r_u,\qquad
\sum_{u\in U}r_u=7,\qquad 0\le m_u\le7.
\]
For \(w\in W\), write
\[
S_w=N_H(w)\cap U,\qquad d_U(w)=|S_w|,\qquad y_w=d_U(w)-7.
\]
The exact cross-edge ledger is
\[
e_H(U,W)=124+\epsilon_U+2\delta,
\]
where \(\epsilon_U=\sum_{u\in U}(d_H(u)-12)\) and \(\delta=e(\overline{H[U]})-294\). The retained contract gives \(\epsilon_U+2\delta\ge9\).

## 2. Theorem A — every W vertex is a block transversal

**Theorem A.** For every \(w\in W\), \(S_w\) intersects every \(Q\in\mathcal Q\). Consequently
\[
d_U(w)\ge7,\qquad y_w\in\mathbb Z_{\ge0},
\]
and
\[
\boxed{\sum_{w\in W}y_w=\epsilon_U+2\delta-2\ge7.}
\]

**Proof.** If \(S_w\cap Q=\varnothing\), then \(w\) is anticomplete to the independent 4-set Q, so \(Q\cup\{w\}\) is an independent 5-set in H, contradiction. Hence \(S_w\) hits all 49 blocks. Each u lies in at most seven blocks, so \(49\le\sum_{u\in S_w}m_u\le7|S_w|\), giving \(d_U(w)\ge7\). Summing \(d_U(w)\) over W gives \(e_H(U,W)=126+\sum_W y_w\), and the exact ledger gives the boxed identity. ∎

**Equality case.** If \(y_w=0\), then \(S_w\) is a 7-point transversal of \(\mathcal Q\): every point of \(S_w\) has \(r_u=0\), and every block meets \(S_w\) in exactly one point. Indeed, all 49 block incidences must be covered by seven points each occurring in at most seven blocks, so equality holds everywhere.

Let \(W_0=\{w:y_w=0\}\) and \(W_+=W\setminus W_0\). Since \(\sum_W y_w\ge7\), at most \(\sum_W y_w\) vertices lie in \(W_+\), and every independent 4-set in H[W] contains at least one vertex of \(W_+\), as shown next.

**Transversal-disjointness lemma.** Any two distinct 7-point transversals of \(\mathcal Q\) are disjoint. If transversals T and T' intersect but differ, choose \(t\in T\setminus T'\). The seven blocks containing t meet T' in seven distinct points (otherwise a pair \(\{t,v\}\) would repeat), so one such block contains a point \(u\in T\cap T'\). That block then contains both t and u from T, contradicting that T is a transversal.

Consequently there are at most four distinct zero-slack neighborhoods. If there are four, they are disjoint 7-sets covering 28 points, and the one remaining point has \(r_u=7\). The omission-degree identity then forces \(\epsilon_U+2\delta\ge16\). Therefore, whenever \(\epsilon_U+2\delta<16\), there are at most three distinct zero-slack U-neighborhoods.


## 3. Theorem B — positive-slack vertices cover every independent 4-set in W

**Theorem B.** For every independent 4-set \(I\subset W\),
\[
\boxed{\sum_{w\in I}y_w\ge1.}
\]
Equivalently, \(\alpha(H[W_0])\le3\).

**Proof.** Every \(u\in U\) must have a neighbor in I; otherwise \(I\cup\{u\}\) is an independent 5-set in H. Thus \(e_H(I,U)=\sum_{w\in I}d_U(w)\ge29\). But this sum is \(28+\sum_{w\in I}y_w\), proving the claim. ∎

**Exact boundary case.** If an independent 4-set \(I=\{w_1,w_2,w_3,w_4\}\subset W\) has \(\sum_I y_w=1\), then exactly three vertices have \(y=0\) and the fourth has \(y=1\). Moreover every u in U has exactly one neighbor in I, so the four sets \(S_{w_i}\) partition U into parts of sizes \(7,7,7,8\). Every support block has exactly one point in each part.

Proof: the 29 edges from I to U must cover every point of U at least once, and there are exactly 29 such edges. Each support block Q is hit by each \(w_i\); as each of its four points has exactly one neighbor in I, Q induces a perfect matching between Q and I. Hence the four neighborhoods partition U and each Q contains one point from each. The three 7-parts are zero-slack transversals and the 8-part carries all seven omission counts \(\sum r_u=7\). ∎

## 4. Theorem C — common-neighborhood capacity for nonadjacent W vertices

**Theorem C.** If \(w,w'\in W\) are nonadjacent in H, then
\[
\boxed{|S_w\cap S_{w'}|\le y_w+y_{w'}.}
\]

**Proof.** Every support block Q must meet \(S_w\cup S_{w'}\) in at least two points. If it met that union in exactly one point, its other three points would be independent and anticomplete to both w and w'; together with the nonadjacent pair \(\{w,w'\}\), they would form an independent 5-set. Summing block incidences gives
\[
98\le\sum_{u\in S_w\cup S_{w'}}m_u\le7|S_w\cup S_{w'}|.
\]
Thus \(|S_w\cup S_{w'}|\ge14\). Since \(|S_w|=7+y_w\) and \(|S_{w'}|=7+y_{w'}\), their intersection is at most \(y_w+y_{w'}\). ∎

Consequences:
- Two nonadjacent zero-slack vertices have disjoint 7-point U-neighborhoods.
- A zero-slack vertex and a \(y=1\) vertex can be nonadjacent only if their U-neighborhoods intersect in at most one point.
- More generally, each unit of combined U-degree slack permits at most one common U-neighbor for a nonadjacent W-pair.

## 5. A further rigidity lemma for the \(7,7,7,8\) boundary

Suppose an independent 4-set I with total slack one exists, and write
\[
U=T_1\dot\cup T_2\dot\cup T_3\dot\cup R,\quad
|T_i|=7,\quad |R|=8
\]
for the four neighborhoods in Theorem B.

1. **The three \(T_i\) are pairwise anticomplete in H.** For any pair of points \(u\in T_i,v\in T_j\), the seven blocks containing u meet \(T_j\) in seven distinct points; hence they cover all of \(T_j\). Thus every pair across \(T_i,T_j\) occurs in a support block and is a nonedge of H.
2. **Each \(T_i\) is a clique \(K_7\).** Since \(\sum_{u\in R}r_u=7\) and \(|R|=8\), choose \(s\in R\) with \(r_s=0\). The point s appears in all seven classes; its seven blocks pair it with all seven points of each \(T_i\), so s is anticomplete to every \(T_i\). If some \(T_i\) contained an independent pair, that pair, one point from each of the other two anticomplete \(T\)-parts, and s would form an independent 5-set. Hence each \(T_i\) is a clique.
3. **Every \(T_i\)-to-R edge is among exactly seven allowed pairs.** Each point \(u\in T_i\) lies in seven blocks and is paired with seven distinct R-points. It therefore has exactly one R-point with which it shares no block. All other \(T_i\)-R pairs are support-block pairs and hence H-nonedges. Thus \(H[T_i,R]\) is a subgraph of a bipartite graph with degree at most one on the \(T_i\) side; there are exactly seven potentially H-edge pairs for each i.
4. **The R-side omission rule.** For each \(s\in R\), at most \(r_s\) vertices of each \(T_i\) can be H-neighbors of s. If \(s,s'\in R\) are nonadjacent, then
\[
r_s+r_{s'}\ge7.
\]
Otherwise the two vertices have a common nonneighbor in each of the three \(T_i\), producing an independent 5-set. Consequently, if no point of R has \(r_s=7\), then \(H[R]\) is a clique except possibly for one edge: any nonedge must be a pair of positive omission weights summing to seven, and there can be at most one such pair.

Finally, if some \(s\in R\) has \(r_s=7\), the support omission-degree identity forces
\[
d_H(s,W)=\epsilon_s+x_s-16\ge0
\quad\Longrightarrow\quad
\epsilon_s+x_s\ge16
\quad\Longrightarrow\quad
\epsilon_U+2\delta\ge16.
\]
Therefore for every contract with \(\epsilon_U+2\delta<16\), the exceptional \(r_s=7\) case is impossible.

## 6. What this does and does not close

This theorem does **not** identify the 49 support blocks with the separate no-S exact-129 component witnesses. It does not by itself exclude any of the five shell templates.

It adds a common W-side contract:
- every W vertex has at least seven U-neighbors;
- the total excess over seven is exactly \(\epsilon_U+2\delta-2\);
- positive-slack W vertices hit every independent 4-set of W;
- nonadjacent W vertices have U-neighborhood intersection at most the sum of their slacks;
- any independent W-quadruple with total slack one forces a rigid \(7,7,7,8\) transversal design and three anticomplete \(K_7\) parts.

For the two minimum-slack profiles \((\delta,\epsilon_U)=(3,3)\) and \((4,1)\), the total W-side slack is exactly seven. Therefore at most seven W vertices have positive slack, at least eleven have \(y=0\), and \(H[W_0]\) has independence number at most three. **Do not infer that there are exactly seven positive-slack vertices or that each positive slack equals one**; a single vertex may carry more than one unit. Every independent W-quadruple contains a positive-slack vertex. If an independent quadruple with total slack one exists, the \(7,7,7,8\) structure above is forced; otherwise the residual is the strict incidence condition that every independent triple in \(W_0\) is hit by every compatible positive-slack vertex.

The global shell join, the non-four-partite low-\(\delta\) branches, and the original \(K_{145}\)-to-T61 bridge remain OPEN / NOT_CERTIFIED.
