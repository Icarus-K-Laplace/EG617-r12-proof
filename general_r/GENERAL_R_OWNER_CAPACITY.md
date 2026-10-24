# General-r Sunflower Owner-Capacity Formulas

Status: **PROVED_SYMBOLIC under the general hereditary cap and common-S sunflower contract**.

## 1. General hereditary cap in the first nontrivial range

For the least-colour target graph in an r-colouring, define

`D_r(t)=C(t,2)-(r-1)p_r(t)`,

where `p_r(t)` is the minimum number of edges in a t-vertex graph with independence number at most r.

For

`r<=t<2r`,

one has

`p_r(t)=t-r`,

so

> **`D_r(t)=C(t,2)-(r-1)(t-r)`.**

For r=12 this is exactly

`Dcap(t)=C(t,2)-11(t-12)`.

The formulas below assume the induced set used in the packing inequality lies in this range.

## 2. d=2 common-zero-hub pattern

Let a repeated boundary one-loss pattern contain k distinct support classes and N owners in total.

The symbolic sunflower inequality is

`2N+k <= D_r(N+k+2)-C(N+1,2)`.

Substitution and simplification give

> **`N <= r-3 + (k^2-3k+6)/(2(r-k))`.**

For fixed `k<=3`, the correction term tends to zero. In particular, for all sufficiently large r,

> **`N<=r-3`.**

At r=12 and k=1,2,3 this yields N<=9, exactly the existing r=12 capacity.

## 3. d=3 Type-H common-zero-hub pattern

The symbolic packing inequality is

`3N+3k <= D_r(N+2k+2)-C(N+1,2)`.

Hence

> **`N <= r-4 + (2k^2-6k+7)/(r+1-2k)`.**

For fixed k<=3 and sufficiently large r this gives

> **`N<=r-4`.**

At r=12:

- k=1,2 give N<=8;
- k=3 gives the exceptional arithmetic ceiling N<=9, which is why the r=12 proof needs a separate low-charge barrier to recover N<=8.

For r>=13 the k=3 correction is `7/(r-5)<1`, so the hereditary inequality alone already yields the integer bound

> **`N<=r-4`**

for every k<=3.

Thus the r=12 Type-H three-class exception is a genuine small-r equality artifact.

## 4. d=3 Type-P common-zero-pair pattern

Using the crude universal Type-P inequality

`3N+1+k <= D_r(N+k+3)-C(N+1,2)`,

one obtains

> **`N <= r-4 + (k^2-3k+10)/(2(r-k))`.**

For fixed k<=3 and sufficiently large r,

> **`N<=r-4`.**

At r=12 all k=1,2,3 give N<=8.

## 5. Asymptotic interpretation

The canonical boundary one-loss capacities have slopes

- d2 common-hub: `N<=r-3+o(1)`;
- d3 Type H/P: `N<=r-4+o(1)`.

Therefore owner packing alone does **not** create a slope contradiction against a shell forcing demand of order r: both sides naturally have slope one.

Any all-sufficiently-large-r contradiction must obtain an additional asymptotic gain from at least one of:

1. anchor excess `f(r)` growing with r;
2. a shell forcing theorem demanding nearly all `r+1-d` possible owners while excluding several exceptional rows;
3. a repivot potential that makes equality capacities unstable;
4. a stronger hereditary cap range than the first-range formula above.

This is an important negative result for strategy: the r=12 numbers 9 and8 are not evidence of a sublinear owner capacity.

## 6. General theorem schema

Under a general common-S boundary one-loss theorem and a core independence bound three, incidence-signature collapse yields at most three canonical sunflower patterns. For each pattern, the exact owner capacity is obtained by substituting the appropriate common-core/petal data into the universal sunflower inequality

`dN + internal support contribution <= D_r(base+support union)-C(N+1,2)`.

Thus owner capacity is a symbolic hereditary-cap function, not a fixed-r combinatorial constant.
