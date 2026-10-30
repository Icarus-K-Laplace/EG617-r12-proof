# Common-neighbour capacity — elementary source-complete proof

Date: 2026-10-30  
Status: **PROVED** under the five Q33 core hypotheses only; no hereditary density cap or external extremal theorem is needed.

Let H have 47 vertices, e(H)=284, delta(H)>=12, alpha(H)<=4 and omega(H)<=11. Put epsilon(v)=d_H(v)-12. Then
\[
\sum_v\epsilon(v)=2\cdot284-47\cdot12=4.
\]

## 1. No 25-set has independence number at most two

Suppose W is a 25-set with alpha(H[W])<=2. Let L be the complement of H[W]. Then L is triangle-free and
\[
\alpha(L)=\omega(H[W])\le11.
\]
L is non-bipartite, since a bipartition of 25 vertices has a side of size at least 13, which would be an independent set in L and hence a clique of size at least 13 in H[W].

Let C be a shortest odd cycle in L, of length 2k+1, k>=2. It is chordless. Each vertex outside C has at most k neighbours on C, since its C-neighbourhood is independent in the cycle. The remaining graph is triangle-free on 24-2k vertices, so Mantel's bound gives
\[
e(L)\le 2k+1+k(24-2k)+\left\lfloor\frac{(24-2k)^2}{4}\right\rfloor.
\]
For k=2,3,...,12, the right-hand side is respectively
145,142,137,130,121,110,97,82,65,46,25. Hence e(L)<=145 and
\[
e(H[W])\ge \binom{25}{2}-145=155.
\]
But
\[
e(H[W])\le\frac12\sum_{w\in W}d_H(w)
\le\frac12(25\cdot12+4)=152,
\]
a contradiction.

Mantel's inequality used here is elementary: for every edge xy in a triangle-free graph on m vertices, d(x)+d(y)<=m. Summing over edges and applying Cauchy gives e<=m^2/4.

Thus no 25-set W can have alpha(H[W])<=2.

## 2. Common-neighbour bound

Let uv be a nonedge of H, let c=|N(u) intersect N(v)|, and let
\[
R=V(H)\setminus(\{u,v\}\cup N(u)\cup N(v)).
\]
Then
\[
|R|=45-d(u)-d(v)+c=21+c-\epsilon(u)-\epsilon(v).
\]
An independent triple in H[R], together with u and v, would be an independent five-set. Thus alpha(H[R])<=2. The no-25-set result gives |R|<=24, whence
\[
\boxed{c\le3+\epsilon(u)+\epsilon(v).}
\]

For a core H that additionally inherits all density caps, the separate R(2,24)=empty lemma in MINDEG12_47_SOURCE_COMPLETE_AUDIT.md improves this to c<=2+epsilon(u)+epsilon(v). The Q33 universal nonexistence proof does not need that stronger capped version.

## 3. K10 completion capacity

At most one external vertex can be complete to a fixed K10. If two external vertices x,y both complete to K and xy is an edge, K union {x,y} is a K12. If xy is a nonedge, they have at least ten common neighbours, but
\[
|N(x)\cap N(y)|\le3+\epsilon(x)+\epsilon(y)\le7,
\]
since total excess is four. Contradiction.

This is the exact common-neighbour input required by the h=4, P and D support-template arguments. No Kang–Pikhurko theorem is used.