# Three-anchor two-connector excess closure

Status: **PROVED_ANALYTIC**.

This file independently proves the `|C|=2` regime of the connector-excess mechanism behind the source-reported V8 E334 closure. It uses only the retained CORE211 graph contract and the already-proved three-anchor partition theorem.

## Contract

Let `H` satisfy

- `|H|=35`;
- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`;
- `e(H)=211`, hence total degree excess

  `K=sum_v (d_H(v)-12)=2`;

- `a1,a2,a3` are pairwise nonadjacent degree-12 vertices.

Assume the three-anchor partition has exactly two connectors.

By `GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`, the exclusive blocks are three cliques

`X1,X2,X3`, each of size 10,

and both connectors are adjacent to all three anchors.

## Theorem

Each of the two connectors has degree at least 14. Consequently the regime is impossible because the two connectors alone consume at least four units of degree excess, while CORE211 has total excess two.

## Proof

Fix one connector `z`, and let the other connector be `w`.

Write

`kappa_z=d_H(z)-12`

and let

`epsilon=1` if `zw` is a target edge, otherwise `epsilon=0`.

Suppose for contradiction that `kappa_z<=1`.

Since `z` is adjacent to all three anchors, the number of its neighbours in the 30 block vertices is

`p = 12+kappa_z-3-epsilon = 9+kappa_z-epsilon`.

Therefore the number of block vertices nonadjacent to `z` is

`m = 30-p = 21-kappa_z+epsilon`.

Under `kappa_z<=1` and `epsilon in {0,1}`,

`m in {20,21,22}`.

For each `i`, define

`M_i = X_i \ N_H(z)`,

and put `m_i=|M_i|`, so

`m_1+m_2+m_3=m`.

### Local nonneighbour-capacity inequality

Fix `x in M_i`, and let `j,k` be the other two block indices.

Consider the vertices in `M_j union M_k` that are nonadjacent to `x`. If two of them, say `y,y'`, were nonadjacent to one another, then

`{z,x,y,y'}`

would be an independent four-set: all three of `x,y,y'` are nonadjacent to `z`, and `x` is nonadjacent to `y,y'` by choice.

Hence the nonneighbours of `x` inside `M_j union M_k` form a clique. Since `omega(H)<=11`, there are at most 11 of them.

Thus `x` is adjacent to at least

`m-m_i-11`

vertices of `M_j union M_k`.

But `x in X_i`. Inside `X_i union {a_i}`, it already has exactly 10 neighbours: the other nine vertices of `X_i` and the anchor `a_i`. Therefore all neighbours outside that base clique number exactly

`d_H(x)-10 = 2+kappa_x`.

The preceding cross-block neighbours are among these, so

`m-m_i-11 <= 2+kappa_x`,

or

> `kappa_x >= m-m_i-13`.  (1)

### A small block would exhaust the entire CORE211 excess budget

Suppose some `m_i<=m-14`. Then the right side of (1) is positive for every `x in M_i`, and summing (1) over the whole part gives

`sum_{x in M_i} kappa_x >= m_i (m-m_i-13)`.

For `m in {20,21,22}` and `1<=m_i<=m-14`, the concave quadratic

`r(m-r-13)`

has its minimum at an endpoint of this interval, where it equals `m-14`. Hence

`m_i(m-m_i-13) >= m-14 >= 6`.

This is impossible because the total excess of the entire 35-point core is only two.

Therefore every part satisfies

`m_i >= m-13`.

Summing over the three blocks,

`m = m_1+m_2+m_3 >= 3(m-13)`.

Thus

`2m <=39`,

so `m<=19`, contradicting `m>=20`.

The assumption `kappa_z<=1` is impossible. Therefore

`kappa_z>=2`.

The argument applies symmetrically to the other connector `w`, so

`kappa_z+kappa_w>=4`.

But CORE211 has total excess `K=2`. Contradiction.

Hence the two-connector three-anchor regime is empty.

## Reusable form

The proof uses a general mechanism:

1. a large clique block gives every block vertex a small external-degree budget;
2. a low-degree connector has a very large block nonneighbourhood;
3. `alpha<=3` forces the cross-nonneighbours of every block vertex inside that connector nonneighbourhood to be a clique;
4. the clique cap turns this into a lower bound on local degree excess;
5. a low-excess global budget makes the three nonneighbour parts simultaneously too large.

This `nonneighbour-capacity` mechanism is the natural candidate for extending the V8 connector-excess lemma to the `|C|=3,4` regimes and to later low-excess backend cores.