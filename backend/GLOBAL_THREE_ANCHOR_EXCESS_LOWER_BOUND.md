# Global three-anchor excess lower bound

Status: **PROVED_ANALYTIC**.

This strengthens the CORE211 three-anchor closure to a parameterized low-excess theorem.

## Theorem

Let `H` be a graph on 35 vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`;
- three pairwise nonadjacent degree-12 vertices.

Define total degree excess above 12 by

`K = sum_v (d_H(v)-12) = 2e(H)-420`.

Then

> **K >= 4.**

Equivalently, every such graph has

`e(H)>=212`.

Thus CORE211 (`e=211`, `K=2`) is impossible, while `e=212`, `K=4` is the first possible equality boundary not excluded by this theorem.

The proof uses the three-anchor partition theorem and a common-nonneighbour capacity argument. It does not use E334 family labels.

---

## Preliminaries

By `GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`, the connector count is `c in {2,3,4}` and the block/signature patterns are:

- `c=2`: blocks `(10,10,10)`, two 3-anchor connectors;
- `c=3`: blocks `(10,10,9)`, one 3-anchor connector and two pair-connectors;
- `c=4`: either `(10,10,8)` or `(10,9,9)`, all connectors pair-connectors.

We argue by contradiction under `K<=3`.

We repeatedly use:

> If `u,v` are nonadjacent, their common nonneighbours form a clique, hence have size at most 11.

---

# 1. c=2

The proof of `GLOBAL_THREE_ANCHOR_C2_EXCESS_CLOSURE.md` only used that any forbidden small nonneighbour part would consume at least six units of excess. Therefore it remains valid a fortiori under `K<=3`.

For either connector `z`, assuming `kappa_z<=1` gives a block nonneighbour count `m in {20,21,22}` and, for each nonneighbour part `M_i`,

`kappa_x >= m-m_i-13` for every `x in M_i`.

If `m_i<=m-14`, that one part contributes at least `m-14>=6` units of excess, impossible under `K<=3`. Hence every `m_i>=m-13`, which forces `m<=19`, contradicting `m>=20`.

Thus both connectors satisfy `kappa>=2`, so `K>=4`.

Hence `c=2` is impossible under `K<=3`.

---

# 2. c=3

Write the blocks as `(10,10,9)`. There are two pair-connectors; each misses one of the two size-10 anchor blocks and both meet the size-9 anchor.

## 2.1 Any low pair-connector dominates the size-9 block

Let `z` be a pair-connector with `kappa_z<=1`, missing one size-10 anchor. Let `M_2` be its nonneighbours in the other size-10 block and `M_3` its nonneighbours in the size-9 block.

Because `z` and the missed anchor are nonadjacent, `M_2 union M_3` is a clique.

As in the CORE211 proof,

`m_2+m_3>=8`.

Every vertex of `M_2` contributes at least `m_3-2` excess, and every vertex of `M_3` contributes at least `m_2-3` excess.

If `m_3>=1`, then already the block excess is at least four:

- `m_3=1` gives `m_2>=7` and contribution at least4;
- larger `m_3` is worse.

This contradicts `K<=3`. Therefore `m_3=0`: every pair-connector with `kappa<=1` dominates the entire size-9 block.

## 2.2 One pair-connector must have kappa>=2

If both pair-connectors had `kappa<=1`, both would dominate the size-9 block and meet its anchor.

They cannot be adjacent, because the size-9 block plus its anchor and the two connectors would form a 12-clique.

But each low connector has eleven fixed neighbours (two anchors plus the size-9 block), hence at most two further neighbours. In the union of the two size-10 blocks they would have at least16 common nonneighbours, which would have to form a clique. Contradiction.

Thus one pair-connector has `kappa>=2`.

## 2.3 The high pair-connector also dominates the size-9 block

Under `K<=3`, that high connector has `kappa in {2,3}`.

Let `M_1` be its missed set in the adjacent size-10 block and `M_3` in the size-9 block. Their union is a clique.

The degree count gives

`m_1+m_3 >= 9-kappa+epsilon`,

so at least7 when `kappa=2` and at least6 when `kappa=3`.

The remaining excess outside the connector is at most `3-kappa`.

If `m_3>=1`, then:

- for `kappa=2`, the minimum block contribution occurs at `m_3=1,m_1=6` and is at least3, exceeding the remaining budget1;
- for `kappa=3`, the minimum positive contribution is at least2, exceeding the remaining budget0.

Hence `m_3=0`: the high pair-connector also dominates the size-9 block.

Now the high and low pair-connectors both dominate that block. If they are adjacent they form a 12-clique with the block and its anchor. If they are nonadjacent, the high connector has at most `1+kappa<=4` neighbours outside its fixed 11-neighbour base, while the low connector has at most2; hence in the other 20 block vertices they have at least14 common nonneighbours, again impossible.

Thus `c=3` is impossible under `K<=3`.

---

# 3. c=4, block pattern (10,10,8)

All connectors are pair-connectors and all meet the size-8 block anchor.

Call a connector *low* if `kappa<=1`.

If fewer than three connectors are low, two connectors have excess at least2 and already force `K>=4`. Thus under `K<=3` there are at least three low connectors.

For a low connector, let `M_{10}` and `M_8` be the missed sets in the two blocks whose anchors it meets. Their union is a clique.

If `M_8` is nonempty, the smallest possible total excess consumed by the connector plus these missed sets is three:

- for `kappa=0`, the missed-set sum is at least8 and the minimum is attained at `(m_{10},m_8)=(7,1)`, costing three block-excess units;
- for `kappa=1`, the missed-set sum is at least7 and the minimum `(6,1)` costs two block-excess units plus the connector's one.

Therefore either the low connector dominates the entire size-8 block, or it alone consumes the full possible budget `K=3`.

If one low connector consumes the full budget, all other connectors and block vertices have zero excess, so the other three connectors must dominate the size-8 block. If no connector consumes the full budget, the at least three low connectors themselves all dominate it.

Hence in every case there are three degree-at-most-13 connectors dominating the same size-8 block and meeting its anchor.

Any two such connectors must be adjacent: if not, each has at most three neighbours in the other 20 block vertices, leaving at least14 common nonneighbours, which would form a forbidden clique.

Thus the three connectors are pairwise adjacent. Together with the size-8 block and its anchor they form a 12-clique. Contradiction.

So this regime is impossible under `K<=3`.

---

# 4. c=4, block pattern (10,9,9)

Again all four connectors are pair-connectors. At least three are low under `K<=3`.

We claim every low connector completely dominates at least one of the two size-9 blocks.

- If the connector misses the size-10 anchor, its missed subsets in the two size-9 blocks form a clique. If both are nonempty, their total size is at least8 for `kappa=0` and at least7 for `kappa=1`, forcing at least four (respectively at least three plus the connector) excess units. Impossible under `K<=3`.
- If the connector misses one size-9 anchor, its missed sets in the size-10 block and the other size-9 block form a clique. If it misses even one vertex of that adjacent size-9 block, the degree lower bounds force more than three total excess units. Hence it dominates that size-9 block.

Thus each of the at least three low connectors dominates `X2` or `X3`. By pigeonhole, two low connectors dominate the same size-9 block.

If they are adjacent, the block, its anchor, and the two connectors form a 12-clique. If they are nonadjacent, each already has eleven fixed neighbours and hence at most two further neighbours; among the remaining 19 block vertices they have at least15 common nonneighbours, which would form a clique. Both cases are impossible.

Therefore this regime is also impossible under `K<=3`.

---

# 5. Conclusion and sharp boundary

All connector regimes are impossible when `K<=3`. Therefore

> **K>=4.**

Since `K=2e(H)-420`, this is equivalent to

> **e(H)>=212.**

This theorem explains the backend transition:

- CORE211 (`K=2`) is killed outright by three-anchor compatibility;
- CORE212 (`K=4`) is the first equality layer not excluded by the coarse excess inequality.

Thus the correct continuation is not to replay the E334 case tree at E335, but to classify the `K=4` equality geometries of this theorem and show which are compatible with the next-layer shell forcing.

That equality-rigidity problem is the natural reusable bridge toward E335 and possible later `r` values.