# Global d=3 A2 Connected Signature-Code Reduction

Status: `PROVED_ANALYTIC`.

Dependencies:

- zero-charge incidence-signature theorem;
- allowance-two overlap saturation;
- `GLOBAL_D3_A2_TWO_COMPONENT_FULL_CLOSURE.md`;
- exact matching-number-two reduction;
- `alpha(H)<=3`.

Purpose: encode the final connected fully-decorated nine-owner support system by at most three zero-charge incidence signatures. This replaces the remaining support topology by a six-code weighted graph.

## 1. Zero-signature codes

The final residual support-intersection graph is connected, has at least two support classes, and every proper overlap at allowance2 is an exact saturation overlap consisting only of zero-charge support vertices.

By the global incidence-signature theorem, at most three distinct zero-charge incidence signatures occur. Label them

`Z_1,Z_2,Z_3`.

For each distinct support class D define its zero-signature code

`I(D)={i : D contains Z_i}`.

Because the support-intersection graph is connected and has more than one vertex, every support intersects another support, hence contains at least one shared zero-charge point. Thus

> `I(D)` is nonempty.                                         (S1)

## 2. Support intersection is exactly code intersection

If two support classes D,E intersect, every point of `D intersect E` is zero-charge. Such a point belongs to some zero signature Z_i represented in both supports, so

`I(D) intersect I(E) != empty`.

Conversely, if i lies in both codes, both supports contain the whole signature class Z_i and hence intersect.

Therefore

> `D intersect E != empty` iff `I(D) intersect I(E) != empty`.   (S2)

The support-intersection graph is exactly the intersection graph of the codes.

## 3. The code 123 is impossible

Suppose a support D had code `{1,2,3}`.

Then D contains at least one representative from each of three distinct zero signatures. Distinct zero signatures are pairwise target-nonadjacent.

Since |D|=3, D consists exactly of those three representatives and contains no target edge.

But every allowance-two 3-support satisfies

`mu(D)<=2`,

hence

`e_H(D)>=1`.

Contradiction.

Thus only the six codes

> `{1},{2},{3},{1,2},{1,3},{2,3}`                           (S3)

can occur.

## 4. A doubleton code occurs for at most one distinct support class

Suppose two distinct supports D,E had the same code `{i,j}`.

Their common zero core contains the signature classes Z_i and Z_j.

If the total common core has three vertices, then a 3-support containing it is uniquely determined, so D=E, contradiction.

Otherwise the common core consists of one representative from each of the two distinct zero signatures. Those two zero vertices are target-nonadjacent.

A nontrivial pairwise-intersecting common-pair family at allowance2 cannot have a target-nonedge common pair: the private positive center needed to make each support legal would see both common points, and row closure against the other support would require two target edges from a charge-one private vertex.

Therefore two distinct supports cannot share such a doubleton zero core.

Hence:

> each of the codes `12,13,23` supports at most one distinct support class.   (S4)

Singleton codes may support several classes; they are exactly the common-core hub/pair pattern groups.

## 5. Matching number in code language

The final support hypergraph has matching number exactly2.

By (S2), disjoint support classes are exactly disjoint codes.

Among the six allowed nonempty proper subsets of `{1,2,3}`, two codes are disjoint only in the following forms:

1. two different singleton codes `{i}`, `{j}`;
2. a singleton `{i}` and its opposite doubleton `{j,k}`.

Two doubleton codes always intersect.

Since a disjoint pair exists, at least one singleton code occurs.

Since no three pairwise-disjoint supports exist, the three singleton codes cannot all occur.

## 6. Canonical connected-code dichotomy

There are therefore exactly two structural regimes.

### Type I — two singleton signature groups

At least two singleton codes occur, say

`{1}` and `{2}`.

Then the support system already contains a disjoint pair across those groups. The third singleton group `{3}` is absent, because three singleton groups would give a matching of size3.

The remaining possible bridge classes have codes

`12,13,23`.

Connectedness requires either

- the direct bridge `12`, or
- both `13` and `23`.

### Type II — one singleton signature group

Exactly one singleton code occurs, say `{1}`.

To realize matching number2 there must be a support disjoint from it. The only allowed disjoint code is

`23`.

Therefore

> code `23` occurs.                                           (S5)

Connectedness then requires at least one of the bridge codes

`12` or `13`.

Thus the final connected residual is reduced to

> **Type I:** two singleton groups plus doubleton bridges;
>
> **Type II:** one singleton group, the opposite doubleton support, and at least one connector doubleton.   (S6)

No other support topology is possible.

## 7. Weighted form

Let

- `A_i` be the total owner multiplicity on singleton-code group `{i}`;
- `b_ij` be the owner multiplicity of the unique doubleton-code support `{i,j}` (zero if absent).

Then

`A_1+A_2+A_3+b_12+b_13+b_23=9`.                              (S7)

Every signature-star subfamily is pairwise intersecting. By the low-charge component theorem its owner weight is at most6:

`A_1+b_12+b_13<=6`,
`A_2+b_12+b_23<=6`,
`A_3+b_13+b_23<=6`.                                         (S8)

The three doubleton supports, when all present, form the no-global-core triangle family and therefore have total owner weight at most6:

`b_12+b_13+b_23<=6`.                                        (S9)

Finally, every disjoint pair of support classes has owner-weight sum at most5 because all `M>=6` windows have been closed.

Equations (S6)--(S9) are the complete weighted code interface for the final connected regime.