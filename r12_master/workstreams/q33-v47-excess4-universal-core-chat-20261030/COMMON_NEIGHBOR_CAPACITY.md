# Common-neighbour capacity — source-complete version

Date: 2026-10-30  
Status: **PROVED** under the five Q33 core hypotheses and all inherited density caps.

Let H have 47 vertices, e(H)=284, delta(H)>=12, alpha(H)<=4, omega(H)<=11, and
\[
e(H[U])\le D(|U|),\qquad
D(n)=\binom n2-11p_{12}(n)
\]
for every U subset V(H), where p_12(n) is the balanced complete 12-partite edge count.

The earlier draft used Kang–Pikhurko at n=25 to show that no 25-set has alpha at most two. That input is unnecessary. The stronger internal seed R(2,24)=empty is already proved from D(24)=144 in MINDEG12_47_SOURCE_COMPLETE_AUDIT.md. We use it here, eliminating the external extremal-theorem dependency.

## 1. R(2,24) is empty

Suppose W is a 24-set with alpha(H[W])<=2. For every w in W, its non-neighbours in H[W] form a clique: two nonadjacent non-neighbours together with w would be an independent triple. Since omega(H)<=11, each vertex has at least 12 neighbours in H[W]. Thus
\[
e(H[W])\ge \frac{24\cdot12}{2}=144.
\]
But D(24)=144, so equality holds and H[W] is 12-regular.

Its complement L is therefore 11-regular and triangle-free. It is non-bipartite: a bipartition of 24 vertices has a side of size at least 12, which would be an independent set in L and hence a clique of size at least 12 in H[W].

Let C be a shortest odd cycle of L, of length 2k+1, k>=2. It is chordless. Every vertex outside C has at most k neighbours on C, since any k+1 vertices of an odd cycle contain an adjacent pair and would form a triangle with that outside vertex. Summing degrees on C gives
\[
11(2k+1)\le 2(2k+1)+k(23-2k),
\]
equivalently
\[
2k^2-5k+9\le0.
\]
The discriminant is 25-72<0, a contradiction. Hence R(2,24) is empty.

## 2. Common-neighbour bound

Let uv be a nonedge of H, let c=|N(u) intersect N(v)|, and write
\[
\epsilon(x)=d_H(x)-12,\qquad \sum_x\epsilon(x)=568-564=4.
\]
The common antineighbourhood
\[
R=V(H)\setminus(\{u,v\}\cup N(u)\cup N(v))
\]
has size
\[
|R|=45-d(u)-d(v)+c
=21+c-\epsilon(u)-\epsilon(v).
\]
An independent triple in H[R], together with u and v, would be an independent five-set. Thus alpha(H[R])<=2. If |R|>=24, any 24-subset would contradict R(2,24)=empty. Therefore |R|<=23 and
\[
\boxed{|N(u)\cap N(v)|\le 2+\epsilon(u)+\epsilon(v).}
\]

This improves the former 3+epsilon(u)+epsilon(v) estimate.

## 3. K10 completion capacity

Let K be a 10-clique. At most one external vertex can be complete to K.

If two external vertices x,y are both complete to K and xy is an edge, K union {x,y} is a K12, contrary to omega(H)<=11. If xy is a nonedge, they have at least ten common neighbours, whereas the preceding bound gives
\[
|N(x)\cap N(y)|\le2+\epsilon(x)+\epsilon(y)\le6,
\]
because the total excess is four. Contradiction.

Thus the K10 completion-capacity lemma is proved without Kang–Pikhurko.