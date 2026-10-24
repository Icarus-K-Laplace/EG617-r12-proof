# Three-Anchor K=6 / c=4 (10,10,8) Full Closure

Status: **PROVED_ANALYTIC**.

This theorem eliminates the entire `(10,10,8)` four-connector equality partition at `K=6`.

It combines the retained dominator-capacity theorem and the exactly-two-dominator closure with one new high-defect estimate: a same-signature pair of bad connectors costs at least four units, after which different signature groups add.

Dependencies:

- `GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md`;
- `GLOBAL_THREE_ANCHOR_K6_C4_TWO_DOMINATOR_FULL_CLOSURE.md`;
- hereditary cap `D(13)=67`;
- common-nonneighbour clique lemma;
- `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`.

---

## 1. Setup

Let the exclusive blocks have sizes `(10,10,8)` with anchors `a1,a2,a3`.
All four connectors are pair-connectors meeting `a3`:

- two have signature `{a1,a3}`;
- two have signature `{a2,a3}`.

For a bad connector of the first signature define

`P=X1\N(b)`, `Q=X3\N(b)`,

`p=|P|>=1`, `q=|Q|>=1`,

`k=kappa_b`.

Let `h in {0,1}` be the number of K8-dominators in the high-defect regimes considered below.
Every `x in Q` has the eight-neighbour base `X3 union {a3}`, plus the h dominators, and is adjacent to every point of P.  Every `y in P` has the ten-neighbour base `X1 union {a1}` and is adjacent to every point of Q.

Thus the explicit bad-subsystem excess lower bound is

> `C_h(b)=k + q(p-(4-h))_+ + p(q-2)_+`.                    (1)

The degree equation gives, with `epsilon` the number of connector neighbours of b,

> `p+q >= 8+epsilon-k`.                                    (2)

The same formulas hold symmetrically for the other signature with `X2` in place of `X1`.

Also, for any two same-signature connectors `b1,b2`, the saturated K11 `X1 union {a1}` gives by `D(13)=67`

> `p1+p2 >= 10+e`,                                         (3)

where `e=1` if `b1b2` is a target edge.

---

# 2. One-dominator regime: a same-signature bad pair costs at least four

Assume exactly one K8-dominator exists.  Then three connectors are bad, so by pigeonhole two bad connectors share one signature.

We prove that any such same-signature pair consumes at least four excess units.

Suppose instead their joint cost were at most three.  Since each individual explicit cost is nonnegative, in particular each connector must satisfy

`C_1(b)<=3`.

We claim this forces the unique local equality

> `(p,q,k,epsilon)=(3,2,3,0)`.                              (4)

Indeed:

- if `q=1`, then (2) and (1) give `C_1>=4`;
- if `p=1`, one gets an even larger bound;
- for `p,q>=2`, direct use of (2) shows that the only way to keep
  `k+q(p-3)_+ + p(q-2)_+ <=3`
  is `p=3,q=2,k=3,epsilon=0`.

Thus both connectors would have `p=3`, so

`p1+p2=6`,

contradicting the K11 cap (3), which requires at least ten.

Therefore

> **every same-signature bad pair in the one-dominator regime costs at least4.**   (5)

The third bad connector has the opposite signature.  Its explicit local cost from (1) is at least three.

The two signature groups have disjoint private blocks.  On their only possible shared charge block `X3`, actual charge is additive in the required sense: if a vertex is forced adjacent to private missed sets of sizes A and B, then

`(A+B-3)_+ >= (A-3)_+ +(B-3)_+`.

Hence the group costs add, giving

`K>=4+3=7`,

contradiction.

Thus exactly one dominator is impossible.

---

# 3. Zero-dominator regime: every same-signature bad pair costs at least four

Assume now there are no K8-dominators.  All four connectors are bad, two of each signature.

Fix a same-signature pair `b1,b2`.
Suppose its joint explicit cost were at most three.

For `h=0`, equations (1)--(2) show that any individual bad connector with explicit cost at most three must satisfy one of the finite low-cost rows

- `q=1`, `4<=p<=7`, `k=7-p`, `epsilon=0`; or
- `q=2`, `3<=p<=5`, with the minimal k from (2), again `epsilon=0`.

In every such row:

- the connector is nonadjacent to every other connector;
- it has no neighbours in the opposite size-ten block.

Therefore `b1,b2` are target-nonadjacent and the whole opposite K10 is contained in their common nonneighbourhood.

By the common-nonneighbour clique lemma this K10, together with any common missed vertices in `X1` or `X3`, must remain a clique of size at most11. Hence

> `|P1 intersect P2| + |Q1 intersect Q2| <=1`.               (6)

Consequently the two forced bicliques

`P1 x Q1`, `P2 x Q2`

have no edge overlap: their edge-set intersection has size

`|P1 intersect P2| |Q1 intersect Q2| =0`.

Moreover, if one vertex lies in the single possible shared side, the actual excess created by adjacency to the union of the two opposite missed sets dominates the sum of the two separate explicit charges.  Hence the explicit block-charge ledgers are additive.

For a bad connector satisfying (1)--(2) with h=0, the explicit cost is always at least two.  Therefore the same-signature pair has joint cost at least

> `2+2=4`,                                                   (7)

contradicting the assumed joint cost at most three.

Thus every same-signature bad pair costs at least four in the zero-dominator regime.

There are two signature groups, with disjoint private blocks.  Their X3 charges again add by

`(A+B-4)_+ >= (A-4)_+ +(B-4)_+`.

Therefore

`K>=4+4=8`,

contradicting `K=6`.

Hence the zero-dominator regime is impossible.

---

# 4. Complete closure of the partition

The retained dominator-capacity theorem already eliminates four and three dominators.
`GLOBAL_THREE_ANCHOR_K6_C4_TWO_DOMINATOR_FULL_CLOSURE.md` eliminates exactly two dominators.
Sections 2--3 above eliminate one and zero dominators.

Therefore

> **there is no three-anchor K=6 core in the `(10,10,8)` c=4 partition.**

The only remaining K=6 three-anchor partition, if any exists, is `(10,9,9)` with at most one K9 dominator.

---

## Reusable interpretation

The proof gives a general high-defect principle:

> once a saturated private K11 forces two same-signature connectors to carry large missed mass, either a dominator raises the local charge threshold enough to make the pair cost at least four, or—without a dominator—the common-nonneighbour clique prevents the two defect ledgers from sharing enough witnesses to reduce their joint cost below four.

This converts many exceptional connectors into a global excess contradiction without enumerating their connector graph.