# Four private cliques and the exceptional set

Status: **PROVED**

Let I={s1,s2,s3,s4} be the independent four-set from INDEPENDENT_FOUR_SET_LEMMA.md. Each si has degree 12.

For v outside I, define its I-support by N(v) intersect I. Since alpha(H)<=4, this support is nonempty: otherwise I union {v} is an independent five-set.

Let

P_i={v outside I : N(v) intersect I = {s_i}},

Z={v outside I : |N(v) intersect I|>=2}.

The sets P_1,...,P_4,Z partition V(H) minus I.

## 1. The private cliques

Define K_i={s_i} union P_i.

Each P_i is a clique. Indeed, if x,y in P_i were nonadjacent, then x,y together with I minus {s_i} would be an independent five-set. Since s_i is adjacent to every point of P_i, K_i is a clique.

The four K_i are pairwise disjoint.

Define d_i=|N(s_i) intersect Z|. Since s_i has degree 12 and I is independent,

|P_i|=12-d_i,
|K_i|=13-d_i.

Because omega(H)<=11,

d_i>=2.

## 2. The exact overlap identity

There are 43 vertices outside I, so

sum_i |P_i| + |Z| = 43.

The four distinguished vertices have total degree 48, and all their neighbors lie outside I. Counting I-to-outside incidences gives

sum_i |P_i| + sum_{z in Z}|N(z) intersect I| = 48.

Subtracting,

sum_{z in Z} (|N(z) intersect I|-1)=5.

Equivalently,

sum_i d_i = sum_{z in Z}|N(z) intersect I| = |Z|+5.

Every z in Z has support size 2, 3, or 4. Hence |Z|<=5. Also sum_i d_i>=8, so |Z|+5>=8 and |Z|>=3.

Thus

3<=|Z|<=5.

## 3. Exhaustive clique-size and support-size patterns

Write h=|Z|. Since each support contributes between 1 and 3 to the overlap surplus five, the following are the only possibilities.

| h | support sizes of Z | sorted (d_1,d_2,d_3,d_4) | clique orders |
|---:|---|---|---|
| 3 | (4,2,2) or (3,3,2) | (2,2,2,2) | (11,11,11,11) |
| 4 | (3,2,2,2) | (3,2,2,2) | (10,11,11,11) |
| 5 | (2,2,2,2,2) | (4,2,2,2) or (3,3,2,2) | (9,11,11,11) or (10,10,11,11) |

The support multigraph interpretation in the last row allows repeated support pairs, corresponding to distinct vertices of Z.

This classification is derived solely from the five core hypotheses. It does not import a Q32 partition.
