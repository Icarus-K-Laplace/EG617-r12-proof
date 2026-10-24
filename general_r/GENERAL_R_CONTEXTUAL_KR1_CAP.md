# General-r Contextual `kr+1` Cap Theorem

Status: **PROVED_SYMBOLIC** under the original balanced-colouring context. External input: Brouwer exact Turan stability.

This theorem unifies the new `4r+1` and `5r+1` full-color bounds and explains why the former is immediately contradictory after extraction while the latter is the first genuine terminal.

## 1. Setup

Let the original object be a balanced r-colouring: every `(r+1)`-set sees every one of the r colors.

Fix one target color and let F be its induced graph on a set R of

`n=kr+1`

vertices. Assume

`alpha(F)<=k`.

For every non-target color j let C_j be its graph on the same set R.

Then:

1. `alpha(C_j)<=r`, because an independent `(r+1)`-set in color j would miss color j;
2. `omega(C_j)<=k`, because a color-j `K_(k+1)` would be an independent `(k+1)`-set in F.

Thus every C_j satisfies a two-sided Ramsey constraint.

## 2. Ordinary alpha<=r minimum

Since

`kr+1=(k+1)+k(r-1)`,

the balanced union-of-r-cliques extremizer for alpha<=r has one clique of size `k+1` and `r-1` cliques of size k. Hence

`p_r(kr+1)`
` =C(k+1,2)+(r-1)C(k,2)`
` = r*k*(k-1)/2 + k.`

## 3. The clique cap costs at least k-1 extra edges

We claim

> **`e(C_j)>=p_r(kr+1)+(k-1)`.**

Suppose instead

`e(C_j)<=p_r(kr+1)+(k-2)`.

Let `J=bar(C_j)`. Then J is `K_(r+1)`-free and

`e(J)>=ex(kr+1,K_(r+1))-(k-2)`.

Brouwer's exact Turan stability theorem says that if `n>=2r+1` and a `K_(r+1)`-free graph has at least

`ex(n,K_(r+1))-floor(n/r)+2`

edges, then it is r-partite.

Here

`floor((kr+1)/r)=k`,

so the threshold is exactly `ex-(k-2)`. Therefore J is r-partite.

Any r-partition of `kr+1` vertices contains a part of size at least `k+1`. This is an independent `(k+1)`-set in J and hence a `K_(k+1)` in C_j, contradicting `omega(C_j)<=k`.

Thus the claimed edge floor follows.

## 4. Contextual target cap

The r color classes partition all pairs of R. Therefore

`e(F)<=C(kr+1,2)-(r-1)[p_r(kr+1)+(k-1)]`.

Substituting the formula above and simplifying gives

> **`e(F)<=U_(k,r)`**, where
>
> **`U_(k,r)=[k r^2 +(k^2-4k+2)r +4k-2]/2`.**

This is the full-color contextual cap at order `kr+1`.

## 5. Minimum-degree contradiction threshold

Suppose additionally

`delta(F)>=r+c`.

Then

`e(F)>=[(kr+1)(r+c)]/2`.

The lower-minus-upper difference is

`[(kc-k^2+4k-1)r + c-4k+2]/2`.

The natural extraction threshold is

`c=k-3`.

At this value the difference simplifies to

> **`[(k-1)r-(3k+1)]/2`.**

Hence:

> **If `delta(F)>=r+k-3` and `(k-1)r>3k+1`, then no such contextual residual exists.**

For every fixed k this holds for all sufficiently large r.

## 6. Why 4r+1 dies and 5r+1 survives

### k=4

The contextual cap is

`U_(4,r)=2r^2+r+7`.

The extraction gives minimum degree `r+1=r+k-3`. The contradiction gap is

`(3r-13)/2`,

positive for r>=5.

Thus the `4r+1` branch is automatically impossible.

### k=5

The contextual cap is

`U_(5,r)=(5r^2+7r+18)/2`.

Automatic contradiction would require minimum degree

`r+2=r+k-3`.

But the actual terminal reduction only leaves minimum degree r or r+1. Hence the density argument stops exactly one or two degree units short.

This explains structurally why `5r+1` is the first genuine terminal after the `4r+1` branch.

## 7. Strategic consequence

The general front architecture should be viewed as a contextual-density descent:

- any extracted `kr+1` residual whose minimum degree reaches `r+k-3` is killed by full-color Turan stability;
- `4r+1` already reaches that threshold;
- `5r+1` misses it and therefore carries the genuine terminal obstruction.

This is a multicolor theorem unavailable in the generic one-color Ramsey formulation.
