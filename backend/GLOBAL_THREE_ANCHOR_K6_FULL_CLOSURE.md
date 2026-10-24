# Global Three-Anchor K=6 Full Closure

Status: **PROVED_ANALYTIC**.

This theorem closes the complete first equality layer of the global three-anchor obstruction.  It is a synthesis theorem: the connector partition is exhaustive, and every connector regime has now been eliminated analytically.

No E-layer label and no solver are used.

## Contract

Let `H` be a graph on 35 vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`;
- there exist three pairwise target-nonadjacent degree-12 vertices.

Define

`K = sum_v (d_H(v)-12) = 2e(H)-420`.

The previously proved three-anchor theorem gives `K>=6`.  Assume for contradiction that

> `K=6`.

By `GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`, the connector count is exactly one of `c=2,3,4`, and the exclusive clique-block sizes are forced as follows:

- `c=2`: `(10,10,10)`;
- `c=3`: `(10,10,9)`;
- `c=4`: `(10,10,8)` or `(10,9,9)`.

These cases are exhaustive.

---

## 1. Two connectors

`GLOBAL_THREE_ANCHOR_K6_C2_FULL_CLOSURE.md` eliminates every `c=2` equality state by a transversal-cover edge count.

The proof first classifies the exact K=6 normal forms and then compares:

- the cross-block edge supply forced by exact degree 12 of the block vertices; and
- the cross-block edge demand required to cover every triple of connector nonneighbours, since otherwise one obtains an independent 4-set.

All three exact c=2 normal forms violate this inequality.

Therefore

> `c=2` is impossible at `K=6`.

---

## 2. Three connectors

`GLOBAL_THREE_ANCHOR_K6_C3_FULL_CLOSURE.md` eliminates the complete `c=3` equality state.

The K=6 normal form has exactly one bad pair-connector and one K9-dominator.  For the bad connector, with missed sets `P,Q` of sizes `p,q`, connector excess `k`, and connector-adjacency count `epsilon`, the exact local ledger gives

`p+q >= 9+epsilon-k`

and

`L = k + q(p-2)_+ + p(q-2)_+ <=6`.

The arithmetic leaves only saturated or one-unit-slack cells.  In every surviving cell, the common-nonneighbour clique of the bad connector with another nonadjacent connector forces at least one additional target edge beyond the local excess ledger, contradicting `K=6`.

Therefore

> `c=3` is impossible at `K=6`.

---

## 3. Four connectors, block pattern (10,10,8)

`GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md` first proves that the K8 block has at most two compatible dominators.

The remaining occupancies are eliminated as follows.

- Exactly two dominators are excluded by `GLOBAL_THREE_ANCHOR_K6_C4_TWO_DOMINATOR_FULL_CLOSURE.md`.  Two saturated K11 bases force large missed mass in orthogonal block directions, while the local bad-connector capacity cannot carry that mass inside total excess six.
- One and zero dominators are excluded by `GLOBAL_THREE_ANCHOR_K6_C4_10108_FULL_CLOSURE.md`.  Same-signature bad pairs have joint defect cost at least four; different signature groups have additively compatible defect ledgers.  Thus one dominator forces total excess at least seven, while zero dominators force at least eight.
- Three and four dominators were already excluded by the dominator-capacity theorem.

Hence

> the `(10,10,8)` partition is impossible at `K=6`.

---

## 4. Four connectors, block pattern (10,9,9)

`GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md` proves that each K9 block has at most one anchor-compatible dominator.

- The exactly-two-dominator regime is excluded by `GLOBAL_THREE_ANCHOR_K6_C4_TWO_K9_DOMINATOR_FULL_CLOSURE.md`: the two saturated K11 bases force missed-mass inequalities on both K9 blocks, and the only apparent crossed equality pattern already consumes at least ten units of excess.
- Zero and one dominator are excluded by `GLOBAL_THREE_ANCHOR_K6_C4_1099_FULL_CLOSURE.md`.  A bad connector missing a K9 anchor has explicit defect cost at least four.  A non-dominating connector missing the K10 anchor, in the presence of one natural K9 dominator, has explicit cost at least three.  Different missed-anchor defects are additive on their shared block.  Thus zero dominators force at least eight excess units, and one dominator forces at least seven.

Hence

> the `(10,9,9)` partition is impossible at `K=6`.

---

# 5. Global theorem

All connector counts and block partitions allowed by the three-anchor partition theorem have been eliminated under `K=6`.

Therefore no three-anchor core satisfying the stated contract can have `K=6`.

The earlier theorem gives `K>=6`, and

`K=2e(H)-420`

is even.  Hence the next possible value is eight:

> **Global Three-Anchor Excess Theorem.**
>
> `K >= 8`.

Equivalently,

> **`e(H)>=214`.**

This is independent of the historical backend layer labels.

---

# 6. Strengthened backend envelope

For every high-backend state,

`E = 91 + q + e(H)`.

Therefore every state which produces three pairwise nonadjacent degree-12 anchors satisfies

`E >= 91 + q + 214 = q+305`,

or equivalently

> **`q <= E-305`.**

For the active high-backend layers:

| layer E | three-anchor upper bound on q |
|---:|---:|
|334|29|
|335|30|
|336|31|
|337|32|
|338|33|
|339|34|
|340|35|

This is one full unit stronger than the previous `q<=E-304` envelope.

---

# 7. Interpretation for the global-support programme

The theorem should not be read as an E334-specific closure.  Its reusable content is:

> **three sufficiently separated zero-charge signatures cannot live in a low-excess 35-point residual core unless the core pays at least eight units of degree excess.**

Combined with `GLOBAL_ZERO_SIGNATURE_ANCHOR_ALIGNMENT_THEOREM.md` and `GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md`, every support system in the three-signature branch now enters the sharper envelope `q<=E-305`.

The remaining backend problem is therefore not a new K=6 connector classification.  It is the forcing bridge:

> prove that every surviving maximal-pivot shell either produces the three-anchor branch, enters the collapsed-signature support master contract, or descends to one of those regimes through a controlled higher-slack equality layer.

The historical E335--E340 layers remain OPEN until that bridge is exhaustive.

---

# 8. Generalization

The partition step is parameterized by `(n,delta,Omega)`, while the closures use only:

- an independence-number-three transversal requirement;
- clique caps;
- minimum-degree excess ledgers;
- dense-base hereditary caps;
- additivity of missed-set defect charges.

Thus the proof architecture is not intrinsically tied to the layer labels or to E334.  For larger-r residual problems, the constants and connector partition change, but the same programme—partition, local defect cost, equality classification, and global additivity—remains applicable.