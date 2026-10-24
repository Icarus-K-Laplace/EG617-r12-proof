# E408 Q33 universal minimum-support bound: \(S_0\ge12\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained T61, exact-129 factor, and 31-point/56-witness Q33 boundary contracts. This strengthens R12_E408_Q33_UNIVERSAL_S0_11.md: the equality case \(S_0=11\) is also impossible, without assuming that the witness complement is four-partite.

## 1. Frozen notation and inherited lemmas

Use the notation of R12_E408_Q33_UNIVERSAL_S0_11.md. Thus \(U\) has 31 vertices, \(W\) has 16, \(\mathcal Q\) consists of 56 pairwise-linear independent four-sets in H, \(T\) is the unique possible seven-point transversal, and \(R=U\setminus T\), \(|R|=24\).

The preceding theorem established:
- every \(w\in W\) has \(q_w=|N_H(w)\cap U|\ge7\);
- there is at most one seven-point transversal T;
- \(T\) is a clique, anticomplete to R;
- \(N_7:=|\{w:q_w=7\}|\le4\), and every such w has \(U\)-neighbourhood T;
- for every \(t\in T\), the eight Q-blocks containing t partition R into eight triples;
- any two distinct 8-point R-only transversals of all Q intersect in at most one point.

Write \(\epsilon_x=d_H(x)-12\), so \(\epsilon_x\ge0\) and \(\sum_H\epsilon_x=4\). Let J be the graph of the \(\delta\) leftover edges of \(L=\overline{H[U]}\) not used by the 56 witness K4s; each \(j_r=d_J(r)\) for \(r\in R\). Then
\[
S_0=\epsilon_U+2\delta,\qquad
d_H(r,W)=3+\epsilon_r+j_r.
\]

For a W-vertex whose U-neighbourhood is not an R-only 8-set, call each of its neighbours in R a *special R-incidence*. If \(s_r\) counts the R-only 8-neighbourhoods containing r and \(a_r\) is the number of special R-incidences at r, then
\[
s_r=3+\epsilon_r+j_r-a_r. \tag{1}
\]
Under the contradiction hypothesis \(S_0=11\), if \(S\subset R\) is one distinct R-only 8-neighbourhood occurring m times, then
\[
8m\le\sum_{r\in S}s_r
\le24+\sum_{r\in R}(\epsilon_r+j_r)
=24+S_0-\epsilon_T\le35.
\]
Thus every distinct R-only 8-set has multiplicity at most four.

## 2. A three-set partition lemma

Suppose a family of 9 or 10 R-only 8-neighbourhoods has at most one uncovered point of R. Distinct sets intersect in at most one point. Its union therefore has size at least 23.

There are at least three distinct sets, since two 8-sets cover at most 16 points. There are at most three distinct sets, since for \(t=4,\ldots,10\),
\[
\left|\bigcup_{i=1}^t S_i\right|
\ge8t-\binom t2>24.
\]
Hence there are exactly three distinct sets \(S_1,S_2,S_3\). If their union had size 23, exactly one pair, say \(S_1,S_2\), would intersect at a point p, \(S_3\) would be disjoint from both, and one point r0 would lie outside their union. Every Q-block whose R-triple contains p must also contain r0 in order to hit all three S_i: the other two points cannot lie in S_1, S_2, or S_3 without hitting one of these transversals twice. But p belongs to seven distinct Q-blocks, one for each t in T. They would all contain both p and r0, violating linearity. Thus the union is all of R, and the three sets partition R.

For a partition \(R=S_1\dot\cup S_2\dot\cup S_3\) by three R-only 8-transversals, let \(G_i\subset W\) be the W-vertices whose U-neighbourhood is \(S_i\). Each S_i is a clique in H: if u,v in S_i were nonadjacent, choose a in S_j nonadjacent to both (each vertex has at most one H-neighbour in S_j), then b in S_k nonadjacent to u,v,a, and append any t in T to obtain an independent five-set. Each G_i is also a clique: if w,w' in G_i were nonadjacent, choose nonadjacent a in S_j and b in S_k, then \(\{w,w',a,b,t\}\) is independent for any t in T. Therefore, if \(|G_i|=4\), \(S_i\cup G_i\) is a K12, contradicting \(\omega(H)\le11\).


**Pair-counting extension.** Let \(S\subset R\) be an 8-point transversal of all seven partitions, and let \(Y\subset R\) be a \(q\)-point transversal of \(d\) of those partitions, where \(q\in\{8,9,10\}\). If \(s=|S\cap Y|<8\), then in each of the \(d\) partitions the \(8-s\) points of \(S\setminus Y\) pair with distinct points of \(Y\setminus S\). The same pair cannot recur in two partitions, by linearity. Hence
\[
d(8-s)\le(8-s)(q-s),
\]
so \(s\le q-d\). In particular:
- a distinct 8-point transversal of six partitions meets S in at most two points;
- a 9-point transversal of all seven partitions, unless it contains S, meets S in at most two points;
- a 10-point transversal of all seven partitions, unless it contains S, meets S in at most three points.

This is the pair-counting step used in the degree-nine cases below.

## 3. Assume \(S_0=11\)

The cross-edge count is
\[
e_H(U,W)=114+S_0=125.
\]
Since \(N_7\ge128-125=3\) and \(N_7\le4\), there are two cases.

### Case I: \(N_7=3\)

The remaining 13 W-vertices have \(q_w\ge8\) and total degree \(125-3\cdot7=104\), so all 13 have \(q_w=8\).

Let a be the number of these 8-neighbourhoods containing all of T. Summing degrees from T into W gives
\[
42+\epsilon_T=3\cdot7+7a,\qquad \epsilon_T=7a-21.
\]
At least one t in T has \(\epsilon_t=0\). Its W-degree is six, three of which are the N7 vertices, so a≤3. Nonnegativity of \(\epsilon_T\) gives a≥3. Thus a=3 and \(\epsilon_T=0\).

The remaining ten W-neighbourhoods are R-only 8-sets. They contribute 80 incidences, and \(\sum_R(\epsilon_r+j_r)=S_0-\epsilon_T=11\). By (1), at most one point of R can be uncovered: s_r=0 requires at least three special incidences, while there are only three special incidences in total. The three-set partition lemma applies. The ten copies have multiplicities summing to ten, each at most four, so the only patterns are (4,4,2) and (4,3,3). The (4,4,2) pattern is impossible because every point in the multiplicity-two set has s_r=2 and hence requires at least one special incidence, but there are only three special incidences for eight points. The (4,3,3) pattern gives a K12 by the clique lemma. Contradiction.

### Case II: \(N_7=4\)

The remaining 12 W-vertices have total U-degree \(125-4\cdot7=97\), so eleven have degree eight and one vertex y has degree nine.

For a degree-eight neighbourhood, its intersection with T is either 0 or 7. Let a be the number of T-type degree-eight neighbourhoods \(T\cup\{r\}\). Since y has degree nine and hits every Q, its T-intersection size b is in \(\{0,1,7\}\): if it misses any t in T, it must hit the eight disjoint R-triples in the partition induced by t, leaving room for at most one T-point.

Summing T-W incidences yields
\[
42+\epsilon_T=4\cdot7+7a+b,\qquad
\epsilon_T=7a+b-14. \tag{2}
\]
For a zero-excess t in T, the four degree-seven vertices already use four of its six W-neighbours, so \(a+\mathbf 1_{\{t\in N_U(y)\}}\le2\). Equation (2) leaves exactly three possibilities:

| b | a | \(\epsilon_T\) | R-only 8-sets | total special R-incidences | \(\sum_R(\epsilon_r+j_r)\) |
|---:|---:|---:|---:|---:|---:|
| 7 | 1 | 0 | 10 | 3 | 11 |
| 1 | 2 | 1 | 9 | 10 | 10 |
| 0 | 2 | 0 | 9 | 11 | 11 |

For b=7, y contains all T and two R points. The three special R-incidences are one from the T-type degree-eight vertex and two from y. No point has three special incidences, so all of R is covered. For b=1 or b=0, y contributes respectively eight or nine distinct R incidences and the two T-type vertices contribute one each. At most one point can be uncovered, because s_r=0 requires at least three special incidences and can occur only when both T-type extra points coincide with a point in y's R-neighbourhood. Thus the three-set partition lemma applies in all three rows.

#### Subcase II-a: b=7

There are ten R-only 8-sets, with multiplicities (4,4,2) or (4,3,3). The (4,4,2) pattern would require at least eight special incidences on the multiplicity-two set, but only three exist. Hence (4,3,3), which gives K12. Contradiction.

#### Subcase II-b: b=1

There are nine R-only 8-sets. Their multiplicities sum to nine and each is at most four, giving (4,4,1), (4,3,2), or (3,3,3). The (4,4,1) pattern requires at least 16 special incidences on the multiplicity-one set, but only ten exist. The (4,3,2) pattern contains a group of multiplicity four and gives K12.

In the (3,3,3) pattern, \(S_1,S_2,S_3\) partition R and the corresponding groups G_i each have size three. Let \(R_y=N_H(y)\cap R\), so \(|R_y|=8\). Since y has exactly one T-neighbour t0, \(R_y\) hits each of the six partitions induced by \(t\in T\setminus\{t_0\}\). If \(R_y\) differed from each S_i, the same pair-counting argument as in Section 2 would give \(|R_y\cap S_i|\le2\) for each i, impossible because the three S_i partition R and \(|R_y|=8\). Therefore \(R_y=S_i\) for some i.

If y missed a vertex w in G_i, choose a in S_j and b in S_k nonadjacent, and choose \(t\in T\setminus\{t_0\}\). The set \(\{y,w,a,b,t\}\) would be independent of size five. Hence y is adjacent to every vertex of G_i. Since S_i is a K8 and G_i is a K3, adding y creates a K12, contradiction.

#### Subcase II-c: b=0

There are nine R-only 8-sets and y's R-neighbourhood \(R_y\) is a nine-point transversal of all Q. Again the multiplicities are (4,4,1), (4,3,2), or (3,3,3). The first requires at least 16 special incidences, but only eleven exist. The second gives K12.

For (3,3,3), suppose \(R_y\) contained no S_i. Since \(R_y\) is a nine-point transversal of all seven partitions and S_i is an eight-point transversal, the pair-counting inequality gives \(|R_y\cap S_i|\le2\) for each i. This would imply \(|R_y|\le6\), impossible. Thus \(R_y\) contains some S_i. If y missed a vertex w in G_i, choose a in S_j and b in S_k outside \(R_y\) and nonadjacent; this is possible because y's nine-point set contains S_i plus only one additional point, while the bipartite H-degree between distinct S-parts is at most one. With any t in T, \(\{y,w,a,b,t\}\) would be an independent five-set. Hence y is adjacent to all of G_i, giving a K12 with S_i and G_i. Contradiction.

All cases under \(S_0=11\) are impossible. Combining with the already-proved \(S_0\ge10\) lower bound gives
\[
\boxed{S_0=\epsilon_U+2\delta\ge12}
\]
for the E408 Q33 31-point/56-witness minimum-support boundary, without any four-partiteness assumption.

## 4. Scope firewall

This closes only the \(S_0=11\) layer at the minimum-support boundary. It does not exclude \(S_0\ge12\), larger support sizes, E407 Q32, E408 Q32 (285-edge/excess-six), or the original \(K_{145}\) theorem. The T61 reduction and exact-129 factor inputs remain conditional contracts. EG617(r=12) remains OPEN / NOT_CERTIFIED.
