# Three-Anchor K=6 / Two-Connector Normal Form

Status: **PROVED_ANALYTIC**.

This theorem advances the first surviving equality frontier of the global three-anchor obstruction.  It does not claim that `K=6` is impossible.  Instead it classifies the entire two-connector (`c=2`) regime into three rigid normal forms.

Dependencies:

- `GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`;
- the connector/nonneighbour inequality used in `GLOBAL_THREE_ANCHOR_C2_EXCESS_CLOSURE.md`;
- the common-nonneighbour clique lemma;
- `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`.

No E-layer labels and no finite computation are used.

---

## 1. Setup

Let H be a 35-point residual core with

- `alpha(H)<=3`;
- `omega(H)<=11`;
- `delta(H)>=12`;
- three pairwise nonadjacent degree-12 anchors `a1,a2,a3`;
- total excess

  `K=sum_v(d_H(v)-12)=6`.

Assume the three-anchor partition has connector count `c=2`.

Then there are three clique blocks

`X1,X2,X3`,

all of size 10, and two connectors `z,w`, each adjacent to all three anchors.

Put

`kappa_v=d_H(v)-12`.

Let `epsilon=1` if `zw` is a target edge and `epsilon=0` otherwise.

For a connector z let

`M_i(z)={x in X_i : zx is a target nonedge}`,

`m_i(z)=|M_i(z)|`,

`m(z)=m_1(z)+m_2(z)+m_3(z)`.

The exact degree count gives

> `m(z)=21-kappa_z+epsilon`.                                (C1)

For every `x in M_i(z)`, the retained common-nonneighbour argument gives

> `kappa_x >= m(z)-m_i(z)-13`.                              (C2)

The same identities hold for w.

---

## 2. Every connector has excess at least two

Suppose first `kappa_z=0`.

Then `m(z)>=21`.  If some part satisfies `m_i<=m-14`, the one-part excess estimate from (C2) consumes at least

`m-14>=7`

units of block excess, contradicting `K=6`.

Otherwise every part has `m_i>=m-13>=8`, whose sum exceeds m.  Thus `kappa_z=0` is impossible.

Now suppose `kappa_z=1`.

If `epsilon=0`, then `m=20`.  A part of size at most6 contributes at least six block-excess units, and together with `kappa_z=1` exceeds K.  If every part has size at least7, their sum is at least21>20.

If `epsilon=1`, the contradiction is even stronger.

Hence

> **`kappa_z>=2` and `kappa_w>=2`.**                         (C3)

Therefore the only connector-excess pairs, up to order, are

`(2,2),(2,3),(2,4),(3,3)`,

with any remaining part of K carried by block vertices.

---

## 3. Adjacent connectors force the first normal form

Assume `epsilon=1`.

If one connector had excess two, then by (C1) it would have `m=20`.  Since the other connector has excess at least two, at most two excess units remain in all block vertices.

If some nonneighbour part had size at most6, (C2) would force at least six block-excess units.  Otherwise all three parts would have size at least7, summing to at least21>20.

Thus no connector can have excess two when `epsilon=1`.

By (C3) and `K=6`, necessarily

> `kappa_z=kappa_w=3`,                                      (C4)

and every block vertex has zero excess.

Then (C1) gives `m(z)=m(w)=19`.  Since all block vertices have zero excess, (C2) forces every nonempty part to have size at least6.  Three parts summing to19 therefore have multiset

> `(7,6,6)`.                                                (C5)

Thus the adjacent K=6 state is completely normalized:

> **Type A.** `zw` is an edge; both connectors have excess3; all block vertices have excess0; each connector has block-nonneighbour profile `(7,6,6)` up to permutation.

---

## 4. Common-nonneighbour localization for nonadjacent connectors

Now assume `epsilon=0`.

Let

`L = M(z) intersect M(w)`

be the common block-nonneighbour set of z and w, with

`L_i=L intersect X_i`, `ell_i=|L_i|`, and `ell=|L|`.

Because z,w are nonadjacent, L is a target clique.

From (C1),

`ell >= m(z)+m(w)-30`
`    = 12-(kappa_z+kappa_w)`.                               (C6)

Let

`B=6-kappa_z-kappa_w`

be the total excess available on all block vertices.

Take `x in L_i`.  Inside `X_i union {a_i}`, x already has ten target neighbours, and x is nonadjacent to both connectors.  Since L is a clique, x is adjacent to all `ell-ell_i` points of L lying in the other blocks.  Therefore

`kappa_x >= ell-ell_i-2`.

Summing over L gives

> `B >= sum_i ell_i max(0,ell-ell_i-2)`.                    (C7)

For every nonadjacent K=6 connector pair, `B<=2` and (C6) gives `ell>=6`.

If L met at least two blocks, the right side of (C7) would be at least3: for a split of an integer `ell>=6` into at least two positive parts, the smallest possible contribution occurs at `1+(ell-1)` and is `ell-3>=3`.

Hence

> **all common block nonneighbours of z,w lie in one block.** (C8)

This localization is the key equality-rigidity step.

---

## 5. The pair (2,2) is impossible

If `kappa_z=kappa_w=2`, each connector has `m=19`.

Because only two block-excess units remain, (C2) forces every part size at least6; hence each profile is exactly `(7,6,6)`.

Equation (C6) gives

`ell>=8`.

But by (C8) all of L lies in one block, while either connector has at most seven nonneighbours in any block.

Contradiction.

Therefore

> `(2,2)` is impossible.                                    (C9)

---

## 6. The pair (2,3) is impossible

Let `kappa_z=2`, `kappa_w=3`.

For z, as above, the profile is exactly `(7,6,6)`.

For w, `m(w)=18`.  Since only one block-excess unit remains, (C2) rules out every part of size at most4; hence every w-part has size at least5.

By (C8), all intersections `M_j(z) intersect M_j(w)` vanish outside one distinguished block i.  Therefore, for `j!=i`,

`m_j(z)+m_j(w)<=10`.

But `m_j(z)>=6` and `m_j(w)>=5`, so the left side is at least11.

Contradiction.

Thus

> `(2,3)` is impossible.                                    (C10)

---

## 7. The pair (2,4): exact aligned profiles

Let `kappa_z=2`, `kappa_w=4`.

All excess is on the connectors, so every block vertex has excess zero.

For z the profile is `(7,6,6)`.

For w, `m(w)=17`; zero block excess and (C2) force every part to have size at least4.  A zero part is also impossible: if `M_i(w)=empty`, then w is adjacent to all of `X_i` and to anchor `a_i`, producing a K12.  Thus all parts are positive.

Let i be the unique block containing L.  For `j!=i`, disjointness of the two missed sets gives

`m_j(z)+m_j(w)<=10`.

If the 7-part of z occurred outside i, this would give at least `7+4=11`, impossible.  Hence the 7-part of z is exactly in block i.

For the other two blocks, `m_j(z)=6`, so `m_j(w)<=4`.  Since every w-part is at least4, both are exactly4.  Therefore the i-part of w is9.

Thus, after relabelling blocks,

> `m(z)=(7,6,6)`,
>
> `m(w)=(9,4,4)`,                                           (C11)

with the 7- and 9-parts aligned in the same block, and the two missed-set pairs in each other block partition that K10.

Moreover (C6) gives `ell>=6`; inside the aligned block the intersection has size between6 and7.

Hence:

> **Type B.** z,w are nonadjacent with connector excesses `(2,4)`; their profiles are exactly `(7,6,6)` and `(9,4,4)` with the large parts aligned.

---

## 8. The pair (3,3): exact aligned profiles

Let `kappa_z=kappa_w=3` and `epsilon=0`.

Again every block vertex has zero excess.

Each connector has `m=18`, and (C2) forces every part to have size at least5.

Let i contain L.  For `j!=i`, the missed sets are disjoint, so

`m_j(z)+m_j(w)<=10`.

Since each term is at least5, equality holds and both terms are5 in both outside blocks.  Consequently each connector has 8 nonneighbours in the aligned block.

Thus, after relabelling,

> `m(z)=m(w)=(8,5,5)`,                                      (C12)

with the 8-parts aligned.  The two 5-parts in each other block are complementary.  Equation (C6) gives `ell>=6`, so the aligned 8-parts intersect in 6,7, or8 vertices.

Hence:

> **Type C.** z,w are nonadjacent with connector excesses `(3,3)`; both profiles are `(8,5,5)` and the 8-parts are aligned.

---

## 9. Complete c=2 / K=6 classification

Combining the preceding sections:

> **K=6 two-connector normal-form theorem.**
>
> Under the three-anchor residual-core contract, every c=2 state with total excess K=6 belongs to exactly one of the following structural regimes:
>
> 1. **Type A:** connectors adjacent; excesses `(3,3)`; all block excess zero; both profiles `(7,6,6)`;
> 2. **Type B:** connectors nonadjacent; excesses `(2,4)`; all block excess zero; aligned profiles `(7,6,6)` and `(9,4,4)`;
> 3. **Type C:** connectors nonadjacent; excesses `(3,3)`; all block excess zero; aligned profiles `(8,5,5)` and `(8,5,5)`.
>
> The apparent regimes `(2,2)` and `(2,3)` are impossible.

In particular, **every surviving c=2 equality state places all six excess units on the two connectors and all thirty block vertices have degree exactly12.**

This is substantially stronger than the coarse bound `K>=6` and gives a finite equality geometry for the first surviving three-anchor layer.

---

## 10. Next global step

The natural continuation is not an E335 case split.  It is to perform the same K=6 equality-rigidity analysis for c=3 and c=4 and then seek one common contradiction or one finite family of equality models.

If all K=6 connector regimes are eliminated, the three-anchor theorem would sharpen to `K>=8`; if some survive, the theorem still identifies the exact equality geometries that any E335+ forcing theorem must realize.