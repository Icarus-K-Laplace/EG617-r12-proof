# Global three-anchor partition theorem

Status: **PROVED_ANALYTIC**.

This theorem is independent of the E334 case labels. It isolates the graph-theoretic structure behind the source-reported V8 three-anchor closure and is intended as a reusable component of the global support-compatibility architecture.

## Theorem (three-anchor partition)

Let `H` be a graph on `n` vertices with

- `alpha(H) <= 3`,
- `omega(H) <= Omega`,
- three pairwise nonadjacent vertices `a1,a2,a3`, each of degree `delta`.

For every `v` outside `A={a1,a2,a3}`, put

`r(v)=|N_H(v) intersect A|`.

Let

- `X_i={v : N_H(v) intersect A={a_i}}`,
- `C={v : r(v)>=2}`,
- `c_j=|{v : r(v)=j}|` for `j=1,2,3`.

Then:

1. every outside vertex meets at least one anchor;
2. each `X_i` is a clique;
3. each `X_i union {a_i}` is a clique, hence `|X_i|<=Omega-1`;
4. with

   `sigma = 3 delta - (n-3)`,

   one has

   `c_2 + 2 c_3 = sigma`;

5. consequently

   `ceil(sigma/2) <= |C| <= sigma`;

6. independently, the clique cap gives

   `|C| >= n-3 Omega`.

Thus

`max(ceil(sigma/2), n-3 Omega) <= |C| <= sigma`.

## Proof

If a vertex `v` outside `A` were nonadjacent to all three anchors, then `A union {v}` would be an independent 4-set, contradicting `alpha(H)<=3`. Hence `r(v)>=1` for all outside vertices.

Fix `i`. If `x,y in X_i` were nonadjacent, then `x,y` are each nonadjacent to the other two anchors `a_j,a_k`, and the four vertices `{x,y,a_j,a_k}` would be independent. Therefore `X_i` is a clique. Since every vertex of `X_i` is adjacent to `a_i`, `X_i union {a_i}` is also a clique, so `|X_i|<=Omega-1`.

Now count anchor incidences in two ways. Because each anchor has degree `delta`,

`sum_{v notin A} r(v)=3 delta`.

Also there are `n-3` outside vertices, so

`sum_{v notin A}(r(v)-1)=3 delta-(n-3)=sigma`.

Only connectors contribute, and a 2-anchor connector contributes one while a 3-anchor connector contributes two. Hence

`c_2+2c_3=sigma`.

Since `|C|=c_2+c_3`, each connector contributes between one and two units to the last sum, giving

`ceil(sigma/2)<=|C|<=sigma`.

Finally

`n-3-|C| = |X_1|+|X_2|+|X_3| <= 3(Omega-1)`,

so `|C|>=n-3 Omega`.

This proves the theorem.

## Exact r=12 / CORE211 specialization

For the current 35-point residual-core contract,

`n=35`, `delta=12`, `Omega=11`.

Therefore

`sigma=36-32=4`

and

`2 <= |C| <= 4`.

Moreover the connector signatures and exclusive-clique sizes are forced exactly.

### `|C|=2`

`c_2+2c_3=4` and `c_2+c_3=2` give

`c_3=2, c_2=0`.

Both connectors meet all three anchors, and

`(|X_1|,|X_2|,|X_3|)=(10,10,10)`.

### `|C|=3`

One has

`c_3=1, c_2=2`,

and, up to permutation,

`(|X_1|,|X_2|,|X_3|)=(10,10,9)`.

### `|C|=4`

One has

`c_3=0, c_2=4`,

and, up to permutation,

`(|X_1|,|X_2|,|X_3|)` is either

`(10,10,8)` or `(10,9,9)`.

Equivalently, writing `d_i=10-|X_i|`,

`d_1+d_2+d_3=|C|-2`.

## Excess corollary

Suppose additionally `delta(H)>=12` and define the core excess

`K=sum_v (d_H(v)-12)`.

If an independent connector-capacity lemma shows that at least two vertices of `C` satisfy

`d_H(v)>=14`,

then automatically

`K>=4`.

Hence no such configuration can occur in a CORE211 equality core, where

`K=2*211-35*12=2`.

The user-delivered V8 source report states exactly such a connector-excess conclusion for its E334 three-anchor configuration. That V8-specific connector lemma is **not re-certified by this file**; this file proves the parameterized partition theorem and isolates the only additional local input needed for the CORE211 contradiction.

## Why this is reusable

The theorem does not depend on `E334`, support labels, or the numerical value 211. For any future residual-core problem with three equal-degree independent anchors, the entire core splits into three exclusive cliques plus a connector set whose size is controlled by

`3 delta-(n-3)`

and the clique cap. Therefore any local theorem forcing connector excess immediately becomes a global excess obstruction.

This is the intended abstraction for extending the V8 mechanism to later backend layers or related Ramsey residual-core problems.