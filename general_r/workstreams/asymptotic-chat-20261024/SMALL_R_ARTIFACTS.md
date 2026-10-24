# Small-r Artifacts

This file records fixed-r difficulties that provably disappear once r is large. The list is certified but not yet claimed exhaustive over every historical E-layer file.

## A1. d2 concentrated positive-loss state — cutoff exactly r<=12

In the d2 exact one-loss three-class branch the sibling endpoint theorem gives

`W=K+2r-2+a+b`

and the three-class charge barrier gives

`W>=3r-2`, hence

`K+a+b>=r`.

For the historical concentrated state

`K=8, a=3, b=1`,

we have

`W=2r+10`.

Comparing with `3r-2` gives

`2r+10>=3r-2`, hence

> **`r<=12`.**

Therefore this entire state is a genuine r=12 boundary artifact and cannot recur for any r>=13.

Status: **PROVED_SYMBOLIC**.

## A2. d4 / symmetric d=(r-3) medium-support headache

The regular-repivot quadratic base is

`d(r+1-d)`.

At `d=4` or `d=r-3` it equals `4(r-3)=4r-12`.

With only the universal core floor `K>=2`,

`q<=3r+2`,

so these degrees are impossible for every `r>=15`.

With `K>=8`,

`q<=3r-1`,

so they are impossible already for every `r>=12`.

Thus the historical r=12 d4/d9 Bridge-C-type medium-support difficulty is not an asymptotic family.

Status: **PROVED_SYMBOLIC**.

## A3. Four simultaneous high-endpoint owners

The sibling repivot theorem shows that four high owners would force

`q>=4r-13`.

Against `q<=3r-1`, this is impossible for every `r>=13` because

`4r-13>3r-1`.

The unique arithmetic boundary r=12 forces equality throughout and is separately contradicted by the multicolour equality regular-clique obstruction.

Hence

> **all r>=12 have at most three high owners**, and the only place where the coarse slope comparison itself fails is r=12.

Status: **PROVED_CONDITIONAL_ON_A_B**.

## A4. Balanced degree-(r+1)^3 near-anchor exception

The symbolic near-anchor reduction lists ten constant deficit patterns. Every lower-minus-upper transversal gap is a quadratic polynomial positive for every r>=13.

At r=12 exactly one coarse-cover cell escapes: the historical `(10,9,6)` cell, which requires the additional fixed-r degree-capacity argument.

Thus the extra r=12 case is a true small-r arithmetic artifact; for r>=13 the balanced near-anchor branch reduces automatically to exact degree-r anchors.

Status: **PROVED_SYMBOLIC**.

## A5. d3 allowance-five / top-q frontier

This one is stronger than small-r-only: it is **not a surviving pathology at all**.

The common-S equality B-floor shows `q=3r-1` is impossible for d3, hence `a+B<=4`; the sibling Bridge-B absorption then closes the whole d3 common-S endpoint for every r>=12 under A+B.

Status: **CLOSED_ALL_R>=12 under A+B**.

## A6. R9 / many disjoint d2 supports with a charge-one witness

The old repetition-nine phenomenon is governed by an r-independent Ramsey bound: under the stated cross-allowance and an outside charge-at-most-one witness, at most eight disjoint two-point supports can occur.

Therefore this is not a new growing family as r increases. Its equality geometry remains bounded.

Status: **PROVED_ANALYTIC**, independent of r once `alpha(H)<=3`.

## Summary table

| historical difficulty | asymptotic fate | cutoff |
|---|---|---:|
| concentrated d2 `K=8,a=3,b=1` | impossible | `r>=13` |
| d4 / d=(r-3) medium supports, baseline | impossible | `r>=15` |
| d4 / d=(r-3) with K>=8 | impossible | `r>=12` |
| four high owners | impossible | all `r>=12`; slope alone from 13 |
| balanced `(r+1)^3` extra near-anchor cell | automatic reduction | `r>=13` |
| d3 top-q/allowance-five | fully closed | `r>=12` under A+B |
| d2 charge-one disjoint-support proliferation | uniformly bounded by 8 | all r |

## Next scan target

The next historical families to parameterize are the remaining d0/d1 terminal states and d2 positive-loss plateau states not covered by the exact one-loss three-class theorem. These are the only sectors still capable of changing the all-large-r backend conclusion.
