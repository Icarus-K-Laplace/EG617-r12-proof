# Global Subcritical-Allowance Decomposition Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_PLATEAU_CAPACITY_THEOREM.md`;
- common-S exact exchange identity;
- common-S overlap theorem;
- common-S row closure;
- exact tau transport and lexicographic maximality.

Purpose: classify every common-missing-set support system below the first overlap threshold. This is the low-slack counterpart of `GLOBAL_FIRST_HIGH_SLACK_DECOMPOSITION.md` and applies directly to q32/d3 regimes with allowance at most2.

## 1. Setup

Let H satisfy

`alpha(H)<=r`.

Let Y be a common-S owner family with

`|S|=d>=2`.

For owner y let D_y be its d-point core support and define

`Delta_y=w(D_y)+mu(D_y)`,

where

`w_v=kappa_v+e_F(v,S)`,
`mu(D)=C(d,2)-e_H(D)`.

Let the common row allowance be a, so

`Delta_y<=a`.

Assume

> `a<=d-1`,                                                   (S1)

and let

`s=|S intersect X|<d`.                                       (S2)

For each owner define its q-loss

`ell_y=q-q_y=a-Delta_y>=0`.                                  (S3)

Split

- `Y_0={y:ell_y=0}` (plateau rows),
- `Y_-={y:ell_y>=1}` (strict-loss rows).

## 2. Plateau layer is bounded and singleton

By `GLOBAL_PLATEAU_CAPACITY_THEOREM.md`,

> `|Y_0|<=r`.                                                (S4)

Moreover every plateau row contains a private clean zero-charge witness, so no plateau support class can repeat.

Thus:

> every plateau row is a distinct singleton support class.   (S5)

For the r=12 residual core (`r=3`):

> `|Y_0|<=3`.                                                (S6)

## 3. Every strict support is globally isolated from distinct supports

Let y be a strict-loss owner. Then

`ell_y>=1`,

so by (S3)

`Delta_y<=a-1<=d-2`.                                        (S7)

Suppose D_y properly overlaps a distinct support E in h points, where

`1<=h<=d-1`.

The common-S overlap theorem gives

`h(d-h)<=Delta_y`.                                           (S8)

But for every proper overlap,

`h(d-h)>=d-1`.                                               (S9)

Combining (S7)--(S9) gives

`d-1<=Delta_y<=d-2`,

impossible.

Therefore:

> **every strict-loss support class is either equal to or disjoint from every other support class.**   (S10)

In particular, if D is a strict support class and E is any distinct support class, then

> `D intersect E=empty`.                                     (S11)

This includes plateau support classes: a strict support cannot properly overlap a plateau support.

## 4. Cross-density of distinct strict supports

Let D,E be distinct strict support classes.

They are disjoint by (S11).

Common-S row closure gives

`e_H(D,E)<=min(w(D),w(E))`.                                  (S12)

For a strict support,

`w(D)<=Delta(D)<=a-1`.

Hence

> `e_H(D,E)<=a-1`.                                           (S13)

Thus the distinct strict supports form a pairwise-disjoint d-block system of cross target-edge allowance at most `a-1`.

## 5. Block-transversal capacity of the strict layer

Let

`T(d,a-1)`

be any certified block-transversal capacity for pairwise-disjoint d-blocks with at most `a-1` target cross edges per pair in a graph with independence number at most r.

Then (S13) gives

> number of distinct strict support classes `<=T(d,a-1)`.    (S14)

Together with the plateau bound:

> **total number of distinct support classes**
>
> `<= r+T(d,a-1)`.                                          (S15)

This is a support-class bound, independent of owner multiplicities.

## 6. Owner multiplicity concentration

Let

`N=|Y|`,
`P=|Y_0|`,
`L=N-P`.

From plateau capacity,

`P<=r`,

so

> `L>=N-r`.                                                  (S16)

All L strict owners lie on at most `T(d,a-1)` distinct strict support classes. Therefore some strict support class has multiplicity at least

> `m_max>=ceil((N-r)/T(d,a-1))`                              (S17)

when `N>r`.

Because any repeated strict support has `s<d`, repetition/tau transport gives the usual one-unit repivot penalty and therefore

`Delta(D)<=a-1`,                                             (S18)

consistent with the structural derivation above.

Thus large owner count at subcritical allowance automatically becomes a repeated-support hereditary-packing problem.

## 7. r=12 d=3, allowance at most2

Take

`r=3`,
`d=3`,
`a<=2`.

Then distinct strict supports have cross allowance

`a-1<=1`.

`GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md` gives

`T(3,1)=3`.

Therefore:

> plateau owners `P<=3`;                                    (S19)
>
> distinct strict support classes `<=3`;                    (S20)
>
> total distinct support classes `<=6`.                     (S21)

Moreover

> `m_max>=ceil((N-3)/3)`.                                   (S22)

For N=10 this gives a repeated strict support of multiplicity at least3.

For N=9 it gives multiplicity at least2.

This is the canonical q32/d3 common-S decomposition; no Type-H/Type-P overlap analysis is needed at this lower allowance.

## 8. r=12 d=2, allowance at most1

Take

`r=3`,
`d=2`,
`a<=1`.

Every strict support has

`Delta<=0`,

so it is zero-charge and internally complete.

Distinct strict supports have cross allowance0. In particular the strict layer is even more rigid than the d2/cross-one transversal regime.

Plateau rows remain bounded by3 and singleton.

Thus low-allowance D2 systems reduce immediately to repeated pure K2 blocks plus at most3 plateau exceptions.

## 9. Relation to first-high-slack decomposition

At `a=d`, a one-loss row has defect `d-1`, exactly equal to the minimum proper-overlap cost. This creates the boundary common-hub/common-pair geometries classified by `GLOBAL_FIRST_HIGH_SLACK_DECOMPOSITION.md` and the zero-charge skeleton theorem.

The present theorem shows why no such geometry exists below that threshold:

> once `a<=d-1`, every strict row has defect at most `d-2`, so all proper overlap disappears automatically.

Therefore the global low-support bridge naturally splits by allowance, not by E-layer:

1. **subcritical:** `a<=d-1` — isolated strict blocks + bounded plateau;
2. **first high slack:** `a=d` — exact one-loss sunflower equality geometry;
3. higher slack — requires additional loss-layer descent.

This is a structural split with clear mathematical meaning.

## 10. Parameterized nature

Sections1--6 are symbolic in

- core independence bound r;
- support size d;
- row allowance a;
- block-transversal capacity T(d,a-1).

They do not use 35, 211, or the E-layer labels. Hence the theorem transfers to higher-r pivot systems once the same overlap and row-closure identities are available.