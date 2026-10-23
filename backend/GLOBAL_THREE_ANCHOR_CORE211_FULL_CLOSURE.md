# Global three-anchor CORE211 full obstruction

Status: **PROVED_ANALYTIC**.

This theorem completes, independently of the delivered V8 archive replay, the graph-theoretic three-anchor obstruction underlying the source-reported E334 closure.

It uses only:

- `|H|=35`;
- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`;
- `e(H)=211`, hence total degree excess `K=2`;
- three pairwise nonadjacent degree-12 anchors.

No E334 shell-family label is used in the proof.

The partition theorem `GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md` reduces the connector count to `c in {2,3,4}`. The `c=2` case is proved in `GLOBAL_THREE_ANCHOR_C2_EXCESS_CLOSURE.md`. This file closes `c=3,4` and records the global corollary.

---

## Common nonneighbour lemma

If `u,v` are nonadjacent in `H`, then their common nonneighbours form a clique.

Indeed, if two common nonneighbours `x,y` were themselves nonadjacent, then `{u,v,x,y}` would be an independent four-set, contradicting `alpha(H)<=3`.

Therefore every common-nonneighbour set has size at most 11.

This elementary observation is the global compatibility engine below.

---

# 1. The three-connector regime

By the partition theorem, up to relabelling:

- `|X1|=|X2|=10`, `|X3|=9`;
- there is one connector adjacent to all three anchors;
- there are two pair-connectors, one missing `a1` and one missing `a2`;
- both pair-connectors are adjacent to `a3`.

Call the two pair-connectors `u,v`.

## 1.1 Low pair-connectors dominate the 9-clique block

Consider `v`, missing `a1`, and suppose `kappa_v<=1`.

Let `M2 subset X2` and `M3 subset X3` be the vertices nonadjacent to `v`, with sizes `m2,m3`.

Because `v` and `a1` are nonadjacent, `M2 union M3` is a clique by the common-nonneighbour lemma.

The total number of block nonneighbours of `v` is

`m = 19 + epsilon - kappa_v`,

where `epsilon` is the number of other connectors adjacent to `v`. Since `X1` has size10,

`m2+m3 >= m-10 >= 8`.

For `x in M2`, the clique `M2 union M3` gives at least `m3` extra neighbours on top of the ten neighbours already supplied by `X2 union {a2}`. Hence

`kappa_x >= m3-2`.

For `y in M3`, its base degree from `X3 union {a3}` is nine, so

`kappa_y >= m2-3`.

If `m3>=1`, then `m2+m3>=8` forces at least four units of excess on `M2 union M3`:

- if `m3=1`, then `m2>=7` and the `M3` contribution is at least `m2-3>=4`;
- if `m3=2`, the contribution is at least `2(m2-3)>=6`;
- larger `m3` is only worse.

This exceeds the total CORE211 excess two. Therefore

> every pair-connector with `kappa<=1` is adjacent to all nine vertices of `X3`.

## 1.2 The two pair-connectors cannot both be low

Suppose `kappa_u,kappa_v<=1`.

Both dominate `X3` and are adjacent to `a3`.

If `uv` were an edge, then

`X3 union {a3,u,v}`

would be a 12-clique, impossible. Hence `u,v` are nonadjacent.

Each already has eleven fixed neighbours: two anchors and all nine vertices of `X3`. Since its degree is at most13, each has at most two neighbours in

`R=X1 union X2`,

which has 20 vertices.

Thus `u,v` have at least

`20-2-2=16`

common nonneighbours in `R`. By the common-nonneighbour lemma these 16 vertices must form a clique, contradicting `omega(H)<=11`.

Therefore at least one pair-connector has `kappa>=2`.

## 1.3 A unique excess-two pair-connector is impossible

Because the total core excess is exactly two, the only remaining possibility would be:

- one pair-connector, say `u`, has `kappa_u=2`;
- every other vertex of `H` has zero excess.

Assume `u` misses `a2`. Let `M1 subset X1` and `M3 subset X3` be its nonneighbours in the two blocks whose anchors it meets.

Again `u` and `a2` are nonadjacent, so `M1 union M3` is a clique.

Since every block vertex has zero excess:

- a vertex of `M1` already has ten base neighbours and all `m3` vertices of `M3`, hence `m3<=2`;
- a vertex of `M3` already has nine base neighbours and all `m1` vertices of `M1`, hence `m1<=3`.

Therefore

`m1+m3<=5`.

But `u` has degree14. If `epsilon` is its number of connector neighbours, then it has

`12-epsilon`

block neighbours and hence

`17+epsilon`

block nonneighbours. The missed block `X2` has size10, so

`m1+m3 >= 7+epsilon >=7`,

contradiction.

Hence the three-connector regime is empty.

---

# 2. Four connectors: block pattern (10,10,8)

The partition theorem gives four pair-connectors; two miss `a1`, two miss `a2`, and every connector is adjacent to `a3`.

Let `X3` be the size-eight block.

## 2.1 Every low connector dominates X3

Take a connector `z` with `kappa_z<=1`, missing (say) `a1` and adjacent to `a2,a3`.

Let `M2 subset X2` and `M3 subset X3` be its nonneighbours in those adjacent-anchor blocks.

Because `z,a1` are nonadjacent, `M2 union M3` is a clique.

The total block nonneighbour count is

`18+epsilon-kappa_z`.

Since the missed block `X1` has size10,

`m2+m3 >= 8+epsilon-kappa_z`.

For `x in M2`,

`kappa_x >= m3-2`;

for `y in M3`, whose base clique has size8,

`kappa_y >= m2-4`.

If `m3>=1`:

- for `kappa_z=0`, the sum `m2+m3>=8` makes the block excess at least3;
- for `kappa_z=1`, the sum `m2+m3>=7` makes the block excess at least2, and adding `kappa_z=1` gives total excess at least3.

Both violate `K=2`.

Therefore `m3=0`: every connector with `kappa<=1` is adjacent to all eight vertices of `X3`.

## 2.2 Three low connectors force a contradiction

With four connectors and total excess two, at least three connectors have `kappa<=1`.

All three dominate `X3` and meet `a3`.

Each has ten fixed neighbours (`a_i,a3` plus the eight vertices of `X3`) and degree at most13, hence at most three neighbours in `X1 union X2`.

If two low connectors were nonadjacent, they would have at least

`20-3-3=14`

common nonneighbours in `X1 union X2`, which would form a clique of size14. Impossible.

Thus the three low connectors are pairwise adjacent. But then

`X3 union {a3}`

is a 9-clique, and adjoining the three pairwise adjacent low connectors produces a 12-clique. Contradiction.

So the `(10,10,8)` regime is empty.

---

# 3. Four connectors: block pattern (10,9,9)

Write `|X1|=10`, `|X2|=|X3|=9`.

The connector signatures are:

- two connectors miss `a1`;
- one misses `a2`;
- one misses `a3`.

We prove that every connector with `kappa<=1` completely dominates at least one of the two size-nine blocks `X2,X3`.

## 3.1 Low connector missing a1

Such a connector is adjacent to `a2,a3`. Let `M2,M3` be its nonneighbours in `X2,X3`.

`M2 union M3` is a clique, and

`m2+m3 >= 8+epsilon-kappa_z`.

Each vertex in either size-nine block has base degree nine, so

`kappa_x >= m3-3` for `x in M2`,

and

`kappa_y >= m2-3` for `y in M3`.

If both `m2,m3` were positive, then:

- for `kappa_z=0`, `m2+m3>=8` forces at least four units of block excess;
- for `kappa_z=1`, `m2+m3>=7` forces at least three units before or together with the connector excess.

Thus one of `m2,m3` is zero. The connector dominates `X2` or `X3`.

## 3.2 Low connector missing a2 or a3

Suppose `z` misses `a2`. It is adjacent to `a1,a3`, so consider its missed subsets `M1 subset X1`, `M3 subset X3`.

They form a clique. Since the omitted block `X2` has size9,

`m1+m3 >= 9+epsilon-kappa_z`.

For `x in M1`,

`kappa_x >= m3-2`;

for `y in M3`,

`kappa_y >= m1-3`.

If `m3>=1`, the lower bound above forces more than the available two total excess units (and still more after including a possible `kappa_z=1`). Therefore `m3=0`.

Hence every low connector missing `a2` dominates `X3`. Symmetrically, every low connector missing `a3` dominates `X2`.

Thus every connector with `kappa<=1` dominates at least one of the two size-nine blocks.

## 3.3 Pigeonhole contradiction

Total excess two implies that at least three of the four connectors have `kappa<=1`.

There are only two size-nine blocks. Hence two low connectors `u,v` dominate the same block, say `X2`.

Both are adjacent to `a2`.

If `uv` is an edge, then

`X2 union {a2,u,v}`

is a 12-clique.

If `uv` is not an edge, each connector already has eleven fixed neighbours (two anchors plus all nine vertices of `X2`), so each has at most two neighbours among the remaining 19 block vertices. They therefore have at least

`19-2-2=15`

common nonneighbours there. The common-nonneighbour lemma would make those 15 vertices a clique, again impossible.

Thus the `(10,9,9)` regime is empty.

---

# 4. Global theorem

Combining:

- `GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`;
- `GLOBAL_THREE_ANCHOR_C2_EXCESS_CLOSURE.md`;
- the `c=3` proof above;
- the two `c=4` proofs above;

we obtain:

## Global Three-Anchor CORE211 Obstruction

There is no graph `H` satisfying

- `|H|=35`;
- `e(H)=211`;
- `delta(H)>=12`;
- `alpha(H)<=3`;
- `omega(H)<=11`;

that contains three pairwise nonadjacent degree-12 vertices.

This theorem is independent of the historical labels `d3`, `r2/A2`, and `r1/A3`.

Therefore any backend forcing theorem that produces three independent degree-12 anchors in a CORE211 equality core immediately gives a contradiction.

## E334 evidence boundary

The delivered V8 source report states that all three surviving E334 residual mechanisms produce precisely this three-anchor configuration, hence source-reports `E334=EMPTY` relative to the retained backend/V7 forcing.

The graph-theoretic obstruction itself is now independently proved here. What remains pending in this assistant session is only independent replay of the V7/V8 package-level forcing bridge from the E334 shell families to the three anchors.

## Generalization target

The proof exhibits two reusable principles:

1. **partition rigidity:** independent minimum-degree anchors create near-maximal clique blocks plus few connectors;
2. **low-excess connector rigidity:** a connector with small degree excess has a huge nonneighbourhood, while `alpha<=3` forces common nonneighbours to be cliques; the clique cap then converts this into excess consumption.

A natural parameterized extension replaces `(35,12,11,K=2)` by `(n,delta,Omega,K)` and seeks the largest `K` for which the same nonneighbour-capacity inequalities still force contradiction. That is the appropriate route for E335 and for possible `r>=13` applications.