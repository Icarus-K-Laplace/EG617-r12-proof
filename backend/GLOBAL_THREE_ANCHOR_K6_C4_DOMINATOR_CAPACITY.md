# Three-Anchor K=6 / Four-Connector Dominator Capacity

Status: **PROVED_ANALYTIC**.

This theorem gives the K=6 equality rigidity for the two `c=4` partition patterns.  It does not enumerate all connector signatures.  Instead it bounds how many connectors can dominate the small exclusive clique blocks.

Dependencies:

- `GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`;
- the local connector-cost estimates established in `GLOBAL_THREE_ANCHOR_K4_EQUALITY_CLOSURE.md`;
- the common-nonneighbour clique lemma;
- `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`.

No solver and no E-layer label are used.

---

# 1. Pattern (10,10,8)

Let the blocks be `X1,X2,X3` with sizes `(10,10,8)`, and let a3 be the anchor of X3.

All four connectors are pair-connectors and all four meet a3.

Call a connector an **X3-dominator** if it is adjacent to every point of X3.  Such a connector has the fixed target-neighbour base

`X3 union {a3, its other anchor}`,

of size ten.

The K4 equality proof established the following local fact:

> any connector which fails to dominate X3 consumes at least three units of total excess (its own excess plus the block excess forced by its missed-set clique).   (D1)

We use only this retained local estimate.

## 1.1 A nonadjacent dominator pair is expensive

Let u,v be two X3-dominators which are target-nonadjacent.

Each has ten fixed neighbours, so u has at most `2+kappa_u` further neighbours in `X1 union X2`, and v has at most `2+kappa_v`.

Therefore among the twenty vertices of `X1 union X2` they have at least

`20-(2+kappa_u)-(2+kappa_v)=16-(kappa_u+kappa_v)`

common nonneighbours.

These form a clique because u,v are nonadjacent.  The clique cap11 therefore forces

> **`kappa_u+kappa_v>=5`.**                                 (D2)

## 1.2 Four dominators are impossible

If all four connectors dominated X3, then their induced graph could not contain a triangle: a connector triangle together with `X3 union {a3}` (a K9) would form a K12.

Thus the four-connector graph would be triangle-free.

For every nonedge pair, (D2) requires endpoint excess-sum at least5.

Let the four connector excesses be ordered

`r1<=r2<=r3<=r4`,

with total at most `K=6`.

Then `r2+r3<=4`: if `r2+r3>=5`, integrality and `r3<=r4` would already force total greater than6.

Hence every pair among the three least-excess connectors has sum below5 and therefore, by the contrapositive of (D2), must be an edge.  Those three connectors form a triangle, contradiction.

So four dominators are impossible.

## 1.3 Three dominators are impossible

Suppose exactly three connectors dominate X3.  Their induced graph cannot be a triangle, again because `X3 union {a3}` is K9.  Hence some dominator pair u,v is nonadjacent and by (D2)

`kappa_u+kappa_v>=5`.

The fourth connector is bad, so by (D1) it consumes at least three additional excess units.  The bad-connector cost does not include the excess of u or v.

Thus total excess is at least8, contradicting K=6.

Therefore there are at most two X3-dominators.

## 1.4 If there are two, they are adjacent

Suppose u,v are the two dominators.  At least one bad connector exists.  If uv were a nonedge, (D2) would require `kappa_u+kappa_v>=5`, while one bad connector costs at least3 by (D1), again giving total excess at least8.

Thus uv must be an edge.

Consequently

`X3 union {a3,u,v}`

is a K11.

We have proved:

> **(10,10,8) K=6 capacity.**
>
> There are at most two X3-dominators.  If there are exactly two, they are target-adjacent and together with X3 and a3 form a saturated K11.   (D3)

This replaces the four-connector case split by one dominator-capacity statement.

---

# 2. Pattern (10,9,9)

Now let the block sizes be `(10,9,9)`, with size-nine blocks X2,X3 and anchors a2,a3.

All four connectors are pair-connectors.  The anchor-incidence counts force:

- two connectors miss a1 (the size-ten anchor);
- one connector misses a2;
- one connector misses a3.

Call a connector an **anchor-compatible Xi-dominator** (`i=2,3`) if it meets ai and is adjacent to every point of Xi.

The K4 equality proof gives two retained zero-cost consequences:

1. a connector which misses one size-nine anchor and has no available local excess must dominate the *other* size-nine block;
2. a connector missing the size-ten anchor either dominates one of X2,X3 or consumes the exceptional four-unit defect pattern.

We first prove an absolute capacity on a single size-nine block.

## 2.1 Two dominators of one K9 consume all six excess units

Let u,v be two anchor-compatible dominators of the same size-nine block Xi.

Each has eleven fixed neighbours: the nine vertices of Xi and its two anchor neighbours.

If uv is an edge, then

`Xi union {ai,u,v}`

is a K12, impossible.

Thus uv is a nonedge.

Among the remaining nineteen block vertices, u has at most `1+kappa_u` neighbours and v at most `1+kappa_v`.  Hence they have at least

`19-(1+kappa_u)-(1+kappa_v)=17-(kappa_u+kappa_v)`

common nonneighbours.

These form a clique, so the clique cap11 gives

> **`kappa_u+kappa_v>=6`.**                                 (D4)

Under total K=6, equality is forced and every vertex outside {u,v} has zero excess.

## 2.2 Equality leads to a second impossible dominator pair

Assume for contradiction that X2 has two anchor-compatible dominators u,v.

By (D4), they consume the whole excess budget:

`kappa_u+kappa_v=6`,

and all other connectors and all block vertices have zero excess.

Consider the remaining two connectors r,s.

Because they have zero excess, neither can use any positive-cost exceptional pattern.

- If such a connector misses a size-nine anchor, the retained local estimate forces it to dominate the other size-nine block.
- If it misses the size-ten anchor, the four-unit exceptional pattern is unavailable, so it must dominate at least one of X2,X3.

Thus each of r,s is an anchor-compatible dominator of X2 or X3.

Neither can dominate X2: that would give a third X2-dominator.  Indeed it is nonadjacent to at least one of u,v or else `X2 union {a2}` together with two adjacent dominators would already form K12; and any nonadjacent pair involving a zero-excess connector violates (D4).

Therefore both r and s must dominate X3.

But then (D4) applied to r,s requires

`kappa_r+kappa_s>=6`,

while both are zero.  Contradiction.

Hence no size-nine block admits two anchor-compatible dominators.

Therefore:

> **(10,9,9) K=6 capacity.**
>
> Each of X2 and X3 has at most one anchor-compatible connector which dominates it completely.   (D5)

---

# 3. Global K=6 c=4 interpretation

The four-connector equality frontier is therefore highly rigid.

- In the `(10,10,8)` partition, the common small block has at most two dominators; two dominators must be adjacent and form a saturated K11 with the block and its anchor.
- In the `(10,9,9)` partition, each size-nine block has dominator capacity one.

All remaining connectors are forced into the positive-cost exceptional missed-set geometries from the K4 analysis.

Thus `c=4,K=6` is no longer an arbitrary connector case tree.  It is a finite **dominator-capacity / expensive-exception** system.

The next reusable step is to combine these capacities with the exact positive-cost exceptional geometries and determine whether total excess six can support the required number of non-dominating connectors.