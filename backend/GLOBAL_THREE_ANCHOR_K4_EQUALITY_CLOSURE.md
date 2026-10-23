# Three-anchor K=4 equality closure

Status: **PROVED_ANALYTIC**.

This file strengthens `GLOBAL_THREE_ANCHOR_EXCESS_LOWER_BOUND.md` by eliminating the first equality layer `K=4`.

## Theorem

Under the 35-point three-anchor contract

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`;
- three pairwise nonadjacent degree-12 anchors;

one has

> `K=sum_v(d_H(v)-12) >= 6`,

and therefore

> `e(H)>=213`.

Since `K=2e(H)-420` is even, it suffices to exclude `K=4` after the previous theorem excluded `K<=3`.

The proof treats the three connector regimes. The only genuinely new equality geometry occurs for `c=2`.

---

# 1. c=2: exact K=4 geometry and contradiction

The partition theorem gives three `K10` blocks `X1,X2,X3` and two connectors `z,w`, both adjacent to all three anchors.

The previous nonneighbour-capacity proof shows that each connector has `kappa>=2`. Under total `K=4`, equality is therefore forced:

- `kappa_z=kappa_w=2`;
- every block vertex has zero excess and hence degree exactly12.

Let `epsilon=1` if `zw` is an edge.

For one connector, say `z`, its number of block nonneighbours is

`m=21-kappa_z+epsilon = 19+epsilon`.

For every block nonneighbour part `M_i`, zero block excess and the inequality

`kappa_x >= m-m_i-13`

force

`m_i>=m-13`.

If `epsilon=1`, then `m=20` and every `m_i>=7`, impossible because their sum is20. Hence

> `zw` is a nonedge.

Thus `m=19`, every `m_i>=6`, and the three part sizes sum to19. Therefore, for each connector, the multiset of block nonneighbour counts is exactly

> `(7,6,6)`.

Now let

`L = (block nonneighbours of z) intersect (block nonneighbours of w)`.

Both connectors have 19 block nonneighbours among 30 block vertices, so

`|L| >= 19+19-30 = 8`.

Because `z,w` are nonadjacent, the common-nonneighbour lemma says that `L` is a clique.

Write `L_i=L intersect X_i`, `ell_i=|L_i|`, and `ell=|L|`.

Take `x in L_i`. It already has ten neighbours in `X_i union {a_i}`. It is nonadjacent to both connectors. Since its degree is exactly12, it has at most two neighbours outside its own base clique.

But `L` is a clique, so `x` is adjacent to all `ell-ell_i` vertices of `L` lying in the other blocks. Hence

`ell-ell_i <=2`

for every nonempty `L_i`.

If `L` met two distinct blocks, each part would have size at most2, so `ell<=4`. If it met all three, the same inequalities give an even smaller bound. Since `ell>=8`, all of `L` must lie in a single block.

But each connector has at most seven nonneighbours in any one block, by the exact `(7,6,6)` equality pattern. Therefore their common nonneighbourhood inside one block has size at most7, contradicting `|L|>=8`.

Thus the `c=2`, `K=4` equality layer is impossible.

---

# 2. c=3 under K=4

The block pattern is `(10,10,9)` with two pair-connectors.

A pair-connector that fails to dominate the size-nine block has the following universal cost. If its connector excess is `k` and it misses at least one vertex of that block, then the common-nonneighbour clique with its missed anchor gives

`m_1+m_3 >= 9+epsilon-k`.

Taking the cheapest possibility `m_3=1` forces at least

`5+epsilon-k`

block-excess units; adding the connector's own `k` gives total cost at least

> `5+epsilon >=5`.

Hence under `K=4`, **every pair-connector dominates the entire size-nine block**.

The two pair-connectors therefore both dominate the same `K9` and meet its anchor.

- If they are adjacent, that `K9`, the anchor and the two connectors form a `K12`.
- If they are nonadjacent, connector `u` has at most `1+kappa_u` neighbours outside its fixed 11-neighbour base and connector `v` has at most `1+kappa_v`; since `kappa_u+kappa_v<=4`, in the other 20 block vertices they have at least

  `20-(1+kappa_u)-(1+kappa_v) >=14`

  common nonneighbours. These would form a clique, impossible.

Thus `c=3` is impossible for `K=4`.

---

# 3. c=4, block pattern (10,10,8), under K=4

A connector failing to dominate the size-eight block consumes at least three units of total excess (connector plus forced block excess), by the inequality already used in the `K<=3` proof.

Therefore at most one connector can fail to dominate the size-eight block. At least three connectors dominate it.

Take two such dominators `u,v`. Each has ten fixed neighbours (two anchors plus the `K8` block), so it has at most `2+kappa` further neighbours.

If `u,v` are nonadjacent, then in the other 20 block vertices they have at least

`20-(2+kappa_u)-(2+kappa_v) = 16-(kappa_u+kappa_v) >=12`

common nonneighbours, because the global excess budget is four. This exceeds the clique cap11.

Hence every pair among the three dominators is adjacent. The `K8` block, its anchor, and three pairwise adjacent connectors form a `K12`. Contradiction.

---

# 4. c=4, block pattern (10,9,9), under K=4

Connectors missing a size-nine anchor must dominate the other size-nine block: failing to do so costs at least five total excess units.

A connector missing the size-ten anchor either dominates one of the two size-nine blocks or, if it misses vertices in both, consumes at least four total excess units.

Thus there are two possibilities.

1. No connector uses the exceptional four-unit pattern. Then all four connectors dominate one of two size-nine blocks; two dominate the same block.
2. One connector uses the exceptional four-unit pattern. It consumes the entire excess budget. The other three connectors have zero excess and therefore each dominates one of the two size-nine blocks; again two dominate the same block.

Take two connectors `u,v` dominating the same size-nine block.

If `uv` is an edge, the block, its anchor and `u,v` form a `K12`.

If `uv` is a nonedge, each has eleven fixed neighbours, so among the other 19 block vertices they have at least

`19-(1+kappa_u)-(1+kappa_v) = 17-(kappa_u+kappa_v) >=13`

common nonneighbours. These would form a clique larger than11.

Contradiction.

---

# 5. Final sharpened theorem

No three-anchor core exists with `K<=4`. Since `K=2e(H)-420` is even,

> `K>=6`,

or equivalently

> `e(H)>=213`.

This is the current strongest analytic form of the global three-anchor compatibility theorem.

## Backend interpretation

- `e=211` / `K=2` is impossible;
- `e=212` / `K=4` is also impossible;
- `e=213` / `K=6` is the first remaining equality frontier for this mechanism.

Thus any E335 channel whose retained forcing produces three independent degree-12 anchors and a 211- or 212-edge core is closed immediately by the same theorem. The next reusable task is to classify the `K=6` equality geometries rather than revive the old E334 branch decomposition.