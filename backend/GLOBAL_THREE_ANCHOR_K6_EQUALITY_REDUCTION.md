# Global Three-Anchor K=6 Equality Reduction

Status: **PROVED_ANALYTIC** as a reduction theorem.  It does **not** assert that K=6 is empty.

This file synthesizes the first surviving equality frontier of the global three-anchor obstruction.

Dependencies:

- `GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`;
- `GLOBAL_THREE_ANCHOR_K6_C2_NORMAL_FORM.md`;
- `GLOBAL_THREE_ANCHOR_K6_C3_NORMAL_FORM.md`;
- `GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md`.

The point is to replace a new E-layer case tree by a finite list of graph-theoretic equality regimes.

---

## 1. Contract

Let H be a graph on 35 vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`;
- three pairwise nonadjacent degree-12 anchors.

Let

`K=sum_v(d_H(v)-12)`.

The global three-anchor theorem already proves `K>=6`.

Assume now the equality value

> `K=6`.                                                    (E1)

By the partition theorem the connector count is `c in {2,3,4}`.

---

# 2. c=2: three exact normal forms

The blocks are three K10's and the two connectors meet all three anchors.

`GLOBAL_THREE_ANCHOR_K6_C2_NORMAL_FORM.md` proves that all block vertices have degree exactly12 and, after relabelling connectors/blocks, exactly one of the following occurs.

### Type A

- connectors are adjacent;
- connector excesses `(3,3)`;
- each connector has block-nonneighbour profile `(7,6,6)`.

### Type B

- connectors are nonadjacent;
- excesses `(2,4)`;
- aligned profiles `(7,6,6)` and `(9,4,4)`;
- the 7- and 9-parts lie in the same K10;
- in each other K10 the 6- and 4-parts are complementary.

### Type C

- connectors are nonadjacent;
- excesses `(3,3)`;
- both profiles `(8,5,5)` with the 8-parts aligned;
- the 5-parts are complementary in each other K10.

The apparent `(2,2)` and `(2,3)` connector-excess allocations are impossible.

Thus c=2 is a genuinely finite equality classification.

---

# 3. c=3: one-defect normal form

The blocks are `(10,10,9)`.  There is one three-anchor connector and two pair-connectors, both incident with the anchor of the K9 block.

Call a pair-connector good if it dominates the K9 and bad otherwise.

`GLOBAL_THREE_ANCHOR_K6_C3_NORMAL_FORM.md` proves:

> exactly one pair-connector is good and exactly one is bad. (E2)

Moreover:

- the bad connector plus its forced missed-set witnesses consume at least five excess units;
- the good K9-dominator has excess at most one;
- the three-anchor connector has excess at most one;
- all excess outside the bad subsystem totals at most one.

Thus c=3 has the canonical shape

> **one high-cost local defect in an almost-regular background.**

This is the natural equality geometry predicted by the global charging theorem.

---

# 4. c=4, block pattern (10,10,8)

All four connectors are pair-connectors incident with the anchor of the K8 block.

Let a connector be good if it dominates K8.

`GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md` proves:

> at most two connectors dominate K8.                       (E3)

If exactly two do, then they are target-adjacent and

`K8 + its anchor + the two connectors`

is a saturated K11.

Every non-dominator is a positive-cost exceptional missed-set geometry; each costs at least three excess units under the retained local estimate.

Thus the `(10,10,8)` equality frontier is a bounded

> **K11-dominator / expensive-exception system.**

---

# 5. c=4, block pattern (10,9,9)

There are two K9 blocks.

For either K9, call a connector an anchor-compatible dominator if it meets that block's anchor and is adjacent to the whole block.

The K6 dominator-capacity theorem proves:

> **each K9 has at most one anchor-compatible dominator.**   (E4)

Indeed, two such dominators would need connector excess sum at least six; equality would use the entire global budget and force the two remaining zero-excess connectors to dominate a K9 as well, producing an immediate second contradiction.

Therefore the `(10,9,9)` regime is also reduced to a bounded set of dominators plus the positive-cost exceptional connector geometries from the K4 analysis.

---

# 6. Global equality theorem

Combining Sections2--5:

> **Three-Anchor K=6 Equality Reduction Theorem.**
>
> Every K=6 three-anchor residual core lies in one of only three structural mechanisms:
>
> 1. one of three exact c=2 connector normal forms (Types A/B/C);
> 2. a c=3 one-defect geometry consisting of one bad pair-connector plus an almost-regular K9-dominator/triple-connector background;
> 3. a c=4 dominator-capacity system in which the small clique blocks admit at most the dominators allowed by (E3)--(E4), and all remaining connectors are positive-cost exceptional missed-set states.

No unrestricted connector case tree remains at K=6.

---

# 7. Consequence for the backend architecture

The global three-anchor theorem currently gives

`K>=6`, equivalently `e(H)>=213`.

The present file explains exactly what equality means.  Therefore any later backend forcing theorem which produces three independent degree-12 anchors has only two possible outcomes:

1. `K>=8`, which strengthens the q-envelope automatically; or
2. `K=6`, in which case the core must realize one of the finite equality geometries in this file.

This is the correct reusable interface for E335--E340.  A future proof should not reopen E335-specific connector cases; it should show that the shell/support forcing is incompatible with Types A/B/C, the c=3 one-defect state, and the c=4 dominator-capacity states.

---

# 8. Next theorem target

The next high-value statement is an **Equality-Geometry Incompatibility Theorem**:

> no active support system satisfying the global support master contract can coexist with any K=6 three-anchor equality geometry above.

Such a theorem would either eliminate K=6 altogether (giving `K>=8`) or show that the support forcing itself automatically avoids the three-anchor equality branch.  Either outcome would strengthen E335--E340 simultaneously.