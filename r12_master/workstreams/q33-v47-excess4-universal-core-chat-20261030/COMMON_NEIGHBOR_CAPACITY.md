# Common-neighbor capacity

Status: **PROVED_CONDITIONAL** on Kang-Pikhurko Theorem 1, whose primary PDF was checked.

Assume the five core hypotheses and write epsilon(v)=d(v)-12, so sum epsilon=4.

## 1. No 25-set has independence number at most two

Suppose W is any 25-vertex subset with alpha(H[W])<=2.

Then the complement J=overline{H[W]} is triangle-free. It is also non-bipartite: if J were bipartite with parts X,Y, then H[W] would contain the two cliques X and Y. Since omega(H)<=11, both parts would have size at most 11, forcing |W|<=22.

Kang-Pikhurko, Theorem 1, states that for n>=r+3 and 2<=r<=(n-1)/2, the maximum number of edges in a K_{r+1}-free graph on n vertices which is not r-partite is

p_r(n)=t_r(n)-floor(n/r)+1.

At n=25,r=2 the hypotheses hold. The balanced complete bipartite graph has

t_2(25)=13*12=156,

so every non-bipartite triangle-free 25-vertex graph has at most

p_2(25)=156-12+1=145

edges.

Therefore

e(H[W]) >= binom(25,2)-145 = 155.

But

sum_{w in W} d_H(w)
=300+sum_{w in W}epsilon(w)
<=300+4=304,

and hence e(H[W])<=152. Contradiction.

Thus no 25-set W can have alpha(H[W])<=2.

Primary source:
M. Kang and O. Pikhurko, “Maximum K_{r+1}-free graphs which are not r-partite”, Matematychni Studii 24 (2005), 12–20, Theorem 1.
https://opikhurko.warwick.ac.uk/E/KangPikhurko05ms.pdf

## 2. Common-neighbor bound

Let uv be a nonedge and c=|N(u) intersect N(v)|. The common antineighborhood

R=V(H) minus ({u,v} union N(u) union N(v))

has size

|R|=45-d(u)-d(v)+c
=21+c-epsilon(u)-epsilon(v).

Since u,v are nonadjacent to every point of R and to each other, an independent triple in H[R] would extend with u,v to an independent five-set. Hence alpha(H[R])<=2.

By the previous section, |R|<=24. Consequently

**|N(u) intersect N(v)| <= 3+epsilon(u)+epsilon(v).**

## 3. K10 completion capacity

Let K be a clique of order 10. At most one external vertex can be complete to K.

If two external vertices x,y are both complete to K and xy is an edge, K union {x,y} is a K12, contrary to omega(H)<=11.

If xy is a nonedge, they have at least ten common neighbors. The common-neighbor bound gives at most

3+epsilon(x)+epsilon(y)<=7,

because the total excess is four. Contradiction.

This proves the K10 capacity statement, including the complete-to-K10 exception.
