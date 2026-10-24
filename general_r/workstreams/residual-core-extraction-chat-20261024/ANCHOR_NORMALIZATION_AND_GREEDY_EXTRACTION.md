# Anchor normalization and canonical greedy extraction

Status: `PROVED_SYMBOLIC` except where explicitly marked `OPEN`.

This file removes the r=12 outer `(d,j)` two-parameter bookkeeping. All anchor defects can be compressed onto the single critical ray `n=ar+1` by induced-subgraph averaging.

## Lemma 1. A minimum-degree anchor has d <= r-1

Let `G` be the least-color graph of a hypothetical counterexample on `r^2+1` vertices, with `r>=3`. Then

`e(G)<=r(r^2+1)/2`,

so the average degree is at most `r`.

If `delta(G)>=r`, then `G` is `r`-regular. Also `alpha(G)<=r`, so

`chi(G)>=ceil((r^2+1)/r)=r+1`.

But Brooks' theorem applied componentwise gives `chi(G)<=r`: no component is `K_{r+1}` because `omega(G)<=r`, and the odd-cycle exception is irrelevant for `r>=3`.

Contradiction. Therefore

> `delta(G)<=r-1`.

Status: `PROVED_ANALYTIC`.

External theorem used: Brooks.

## Lemma 2. Anchor identity and raw ray

Choose a minimum-degree anchor `x` of degree

`d=r-s`, with `1<=s<=r`.

The minimum-degree pivot identity gives

`e(G)=C(d+1,2)+q+e(G-N[x])`, `q>=0`.

Hence the non-neighborhood residual `R` has

- order `(r-1)r+s`;
- independence number at most `r-1`;
- inherited hereditary cap;
- edge budget

  `B_s(r-1)=r(r^2+1)/2-C(r-s+1,2)`.

More generally, after `j` extracted `K_r` blocks, write

`a=r-1-j`.

Then

`|R_a|=ar+s`

and

`e(R_a)<=B_s(a)
 := r(r^2+1)/2-C(r-s+1,2)-(r-1-a)C(r,2)`.

Explicitly,

`B_s(a)=[a r^2-a r+r^2+2rs-r-s^2+s]/2`.

Status: `PROVED_SYMBOLIC`.

## Lemma 3. Induced trimming collapses every anchor defect to s=1

Fix `a>=1`. Let `R` be a graph with

`|R|=ar+s`, `s>=1`,

and

`e(R)<=B_s(a)`.

Then there exists an induced subgraph `R'` on exactly

`ar+1`

vertices satisfying

> `e(R')<=B_1(a)`.

All hereditary alpha/omega/color-cap constraints pass to `R'`.

### Proof

Choose uniformly a `(ar+1)`-vertex subset. Its expected edge count is

`e(R) * C(ar+1,2)/C(ar+s,2)`.

Thus some induced subset has at most that many edges. It remains to verify

`B_s(a) C(ar+1,2) <= B_1(a) C(ar+s,2)`.

After clearing the positive factor 2, the right side minus the left side equals

`r(s-1)[a^2 r s-2a^2 r+2ar^2+ars+rs+s]/2`.

For `s=1` this is zero. For `s>=2`, every term in the bracket is nonnegative after combining the first two as `a^2 r(s-2)`, while the remaining terms are positive. Hence the difference is positive.

Status: `PROVED_SYMBOLIC`, independent of r.

### Consequence

The anchor-defect rays `s=2,...,r` need not be separately eliminated. They can be **normalized by trimming** to the critical ray `s=1` before the block-extraction analysis begins.

This replaces 12 separate r=12 degree rows by one canonical all-r state.

## Lemma 4. Canonical critical-ray budget

After trimming, define the canonical state `R_a` by

- `|R_a|=ar+1`;
- `alpha(R_a)<=a`;
- inherited cap;
- edge budget

  `e(R_a)<=B_a`,

where

`B_a:=B_1(a)=r((a+1)r-a+1)/2`.

The generic Turan floor is

`p_a(ar+1)=a C(r,2)+r`,

and

> `B_a-p_a(ar+1)=C(r,2)`.

Also

> `B_a-B_{a-1}=C(r,2)`.

Status: `PROVED_SYMBOLIC`.

## Lemma 5. Removing a K_r preserves the canonical state

Suppose canonical `R_a` contains a target-color clique `Q=K_r`, with `a<=r-1`. Let

`R_{a-1}=R_a-Q`.

Then

- `|R_{a-1}|=(a-1)r+1`;
- `e(R_{a-1})<=B_{a-1}`;
- `alpha(R_{a-1})<=a-1`.

### Edge budget

Deleting `Q` removes at least its `C(r,2)` internal edges, so

`e(R_{a-1})<=B_a-C(r,2)=B_{a-1}`.

### Independence cap

The balanced-coloring condition implies that any vertex outside a target-color `K_r` has at most one target-color neighbor in that clique: otherwise the `r+1` vertices consisting of the block plus the outsider cannot realize all `r` colors.

If `R_{a-1}` contained an independent set `I` of size `a`, then at most `a<r` target-color edges join `I` to `Q`. Some `q in Q` has no target-color neighbor in `I`, so `I union {q}` is an independent `(a+1)`-set in `R_a`, contradiction.

Status: `PROVED_SYMBOLIC`.

## Canonical greedy process

Starting from the minimum-degree anchor:

1. take its non-neighborhood residual;
2. apply Lemma 3 once to normalize to `R_{r-1}` on `(r-1)r+1` vertices;
3. while the current `R_a` contains a target-color `K_r`, remove one and pass to `R_{a-1}`.

Every state remains on the single ray

`|R_a|=ar+1`, `e(R_a)<=B_a`, `alpha(R_a)<=a`.

Let `a_*` be the first value at which the process is `K_r`-free.

Then `R_{a_*}` additionally has

`omega(R_{a_*})<=r-1`.

## Lemma 6. For r>=17, the process cannot pass below a=4

At `a=4`, a canonical state has order `4r+1` and alpha at most 4.

If it is `K_r`-free, `RESIDUAL_BRANCH_CLOSURE.md` applies and gives Branch A.

If it contains a `K_r`, Lemma 5 would produce `R_3` on `3r+1` vertices with `alpha<=3`.

But `R_3` is impossible for `r>=17`:

- if `R_3` is `K_r`-free, any induced `3r`-subset contradicts the `3r` exclusion in `RESIDUAL_BRANCH_CLOSURE.md`;
- if `R_3` contains a `K_r`, deleting it gives `R_2` on `2r+1` vertices with `alpha<=2`;
  - if `R_2` is `K_r`-free, any induced `2r`-subset contradicts the `2r` exclusion;
  - if `R_2` contains a `K_r`, deleting it gives `R_1` on `r+1` vertices with `alpha<=1`, i.e. a target-color `K_{r+1}`, forbidden in the original counterexample.

Therefore a canonical `R_4` must be `K_r`-free and is automatically the desired `4r+1` residual.

Status: `PROVED_ANALYTIC` for `r>=17`.

## Exact 5r+1 terminal

If the first `K_r`-free state is `a_*=5`, define

> `T_r := R_5`.

It satisfies the exact symbolic contract

- `|T_r|=5r+1`;
- `alpha(T_r)<=5`;
- `omega(T_r)<=r-1`;
- every induced subgraph satisfies the hereditary least-color cap;
- `e(T_r)<=B_5=3r^2-2r`;
- `T_r` is `K_r`-free by maximality of the greedy process.

This is a verifiable general definition of the `5r+1` terminal; it is not merely an affine/design analogy.

If `T_r` contains a `K_r`, it is not terminal: deleting that block immediately yields the `4r+1` residual and Branch A.

## The only remaining extraction blocker

For `r>=17`, every full hypothetical counterexample therefore yields, after canonical normalization and greedy block removal, exactly one of:

1. **Branch A:** first `K_r`-free state occurs at `a=4`, hence a `4r+1` residual whose full pivot/core contract is proved; or
2. a first `K_r`-free canonical state with `a>=5`.

The desired dichotomy is reduced to the single lemma:

> **OPEN HIGH-LEVERAGE LEMMA:** a first `K_r`-free canonical stop cannot occur with `a>=6`.

If this lemma is proved, the complete front-end dichotomy becomes

`4r+1 residual` OR exact `5r+1` terminal `T_r`.

Status of the no-stop-for-`a>=6` lemma: `OPEN`.