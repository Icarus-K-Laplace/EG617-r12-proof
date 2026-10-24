# Three-Anchor K=6 / (10,9,9) Exactly-Two-Dominator Full Closure

Status: **PROVED_ANALYTIC**.

This theorem eliminates every exactly-two-dominator equality state in the `(10,9,9)` four-connector partition.

Together with `GLOBAL_THREE_ANCHOR_K6_C4_TWO_DOMINATOR_FULL_CLOSURE.md`, it implies that any surviving `c=4,K=6` three-anchor core has at most one small-block dominator.

Dependencies:

- `GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md`;
- hereditary cap `D(13)=67`;
- the retained local costs from `GLOBAL_THREE_ANCHOR_K4_EQUALITY_CLOSURE.md`;
- `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`.

---

## 1. Connector signatures and dominator slots

Let the blocks have sizes

`|X1|=10`, `|X2|=|X3|=9`,

with anchors `a1,a2,a3`.

The four pair-connectors have signature multiset

- two connectors of type A, missing `a1`;
- one connector B, missing `a2`;
- one connector C, missing `a3`.

The retained K=6 dominator theorem gives:

> each K9 block admits at most one anchor-compatible dominator.

Thus an exactly-two-dominator state has one dominator for `X2` and one for `X3`.

We split according to whether the natural connectors B,C occupy those two slots.

---

## 2. If a type-A connector occupies a dominator slot, the remaining defects have different missed anchors

Suppose at least one type-A connector is one of the two dominators.

Because there is only one dominator slot per K9, the two remaining non-dominating connectors cannot both be the two type-A connectors.  Hence among the non-dominators there is a connector missing `a2` or `a3` together with a connector of a different missed-anchor type.

The retained local costs are:

- a type-A connector which misses vertices in both K9 blocks is an exceptional four-unit state;
- B or C, if it fails to dominate its opposite K9 block, costs at least five units.

For defects with different missed anchors the private missed blocks are disjoint and the only possible overlap of the local excess ledgers occurs in one shared block.  At a shared witness, adjacency to the union of the two private missed sets forces an excess at least the sum of the two separate local charges (the same convexity/additivity mechanism used in the c=3 and `(10,10,8)` dense-base reductions).

Therefore the two local costs are additive.

Hence the global excess is at least

`4+5=9`

(or `5+5=10`), contradicting `K=6`.

Thus in any exactly-two-dominator survivor, the dominators must be precisely the natural connectors B and C.

---

## 3. Natural dominators create two saturated K11 bases

Assume therefore:

- B dominates `X3`;
- C dominates `X2`.

Then

`B2=X2 union {a2,C}`

and

`B3=X3 union {a3,B}`

are both saturated K11s.

The two type-A connectors `u1,u2` are non-dominating and hence exceptional: each misses at least one vertex in each of `X2,X3`.

Write

`Pi=X2\N(ui)`, `Qi=X3\N(ui)`,

`pi=|Pi|>=1`, `qi=|Qi|>=1`,

`ki=kappa_ui`.

Let `e=1` if `u1u2` is a target edge.  Let `ri` be the indicator that `ui` is adjacent to C and `si` the indicator that it is adjacent to B.

---

## 4. The two K11 caps force large missed mass on both sides

Apply `D(13)=67` to `B2 union {u1,u2}`.

Connector `ui` has

`1 +(9-pi)+ri =10-pi+ri`

edges into `B2`.
Thus

`55 +(10-p1+r1)+(10-p2+r2)+e <=67`,

hence

> `p1+p2 >= 8+r1+r2+e >=8`.                                (P)

Likewise from `B3 union {u1,u2}`,

> `q1+q2 >= 8+s1+s2+e >=8`.                                (Q)

So the two exceptional connectors jointly miss at least eight vertices on each K9 side.

---

## 5. Single-exception capacity under the two saturated bases

For one exceptional connector `ui`, let `ni` be its number of neighbours in `X1`.
Its degree equation is

`ni = ki+pi+qi-8-epsilon_i`,

where `epsilon_i` is its number of connector neighbours among the other three connectors.  Hence

> `pi+qi >=8+epsilon_i-ki`.                                 (D)

Since `ui` and `a1` are nonadjacent, `Pi union Qi` is a target clique.
Every vertex of `Pi` already has the ten-neighbour base `X2 union {a2,C}`, and every vertex of `Qi` has the ten-neighbour base `X3 union {a3,B}`.
Therefore

> `Li = ki + pi(qi-2)_+ + qi(pi-2)_+`                       (L)

is a lower bound on the excess consumed by the `ui` missed-set subsystem.
Since `K=6`, necessarily `Li<=6`.

Exactly as in the `(10,10,8)` two-dominator argument, this implies:

1. if `pi,qi>=2`, then
   > `pi+qi<=6`;                                             (S1)
2. if `min(pi,qi)=1`, then
   > `max(pi,qi)<=8`.                                       (S2)

---

## 6. The two-side missed-mass bounds force a crossed pattern

If both exceptional connectors had `pi,qi>=2`, then by (S1)

`(p1+q1)+(p2+q2)<=12`,

while (P)+(Q) gives at least16.  Impossible.

Thus one connector has a side of size one.

Suppose `q1=1`.  Then (Q) gives `q2>=7`.
If `p2>=2`, then `p2,q2>=2`, so (S1) gives `p2+q2<=6`, impossible.
Therefore `p2=1`.

By (P), `p1>=7`.

Thus every possible survivor has the crossed form

> `(p1,q1)=(p,1)`, `(p2,q2)=(1,q)` with `p,q>=7`.            (X)

---

## 7. Crossed patterns already consume at least ten excess units

For the first connector, its singleton `Q1` vertex lies in `X3` and is adjacent to all `p>=7` vertices of `P1`.
It already has the ten-neighbour saturated base `B3`, so

`kappa(Q1) >= p-2 >=5`.

For the second connector, its singleton `P2` vertex lies in `X2` and is adjacent to all `q>=7` vertices of `Q2`.
It already has the ten-neighbour saturated base `B2`, so

`kappa(P2) >= q-2 >=5`.

These two witnesses lie in different blocks and their excesses are disjoint.
Therefore

`K>=5+5=10`,

contradicting `K=6`.

---

# 8. Conclusion

There is no `(10,9,9)`, `K=6` three-anchor core with exactly two K9 dominators.

Combining this theorem with the `(10,10,8)` two-dominator closure and the retained c=4 dominator-capacity theorem:

> **every surviving `c=4,K=6` three-anchor equality state has at most one small-block dominator.**

Thus the entire remaining K=6 equality frontier is a high-defect regime with at least three exceptional connectors.

---

## Reusable interpretation

Two saturated K11 bases impose orthogonal missed-mass lower bounds.  A single exceptional connector has a strict local missed-mass capacity, so two exceptions can only survive in a crossed one-small-side pattern; the crossed pattern then forces disjoint high-excess witnesses.  This mechanism is independent of the historical E-layer labels.