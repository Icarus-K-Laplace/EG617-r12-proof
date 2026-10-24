# General-r Multicolor Owner-Capacity Theorem

Status: **PROVED_SYMBOLIC**, conditional only on the residual being within target hereditary deficit epsilon of `D_r(4r+1)` and the quantitative multicolor regular-clique bound.

## 1. Common-S owners form a regular target clique

In every common-S family, the owner set Y consists of regular shell vertices and the pivot p is regular. Distinct owners are target-adjacent because each owner's shell missing set is exactly S, which does not contain another owner. Every owner is also target-adjacent to p.

Therefore

> **`{p} union Y` is a target clique of size `N+1`, and every one of its vertices has target degree exactly `r+1`.**

No support geometry, zero-signature theorem, or loss assumption is needed.

## 2. Apply multicolor near-extremal stability

Let

`epsilon=D_r(4r+1)-e(F)`.

By `GENERAL_R_MULTICOLOR_STABILITY_D3_WINDOW.md`, any target clique B consisting of target-degree-`r+1` vertices satisfies

`2|B| <= (r-1)+2epsilon+epsilon sqrt(4epsilon+1)`.

Apply this to `B={p} union Y`. Then

`2(N+1) <= (r-1)+2epsilon+epsilon sqrt(4epsilon+1)`.

Hence:

> **Multicolor owner capacity**
>
> `N <= [r-3+2epsilon+epsilon sqrt(4epsilon+1)]/2`.

For every fixed epsilon,

> **`N <= r/2+O_epsilon(1)`.**

Thus near the maximum residual edge layer the owner-capacity slope is one half, not one.

## 3. Exact and deficit-two specializations

At hereditary equality (`epsilon=0`):

> **`N<=floor((r-1)/2)-1`.**

For `epsilon<=2`, the stronger exact Brouwer-partite argument in `GENERAL_R_NEAR_EQUALITY_MULTICOLOR_CLIQUE_OBSTRUCTION.md` gives

> **`N+1<=floor((r-1+epsilon)/2)`.**

These bounds are frequently sharper than the general square-root formula.

## 4. Comparison with hereditary sunflower capacity

The earlier support-packing capacities were

- d2 common hub: `N<=r-3+o(1)`;
- d3 Type H/P: `N<=r-4+o(1)`.

Those have slope one and cannot by themselves produce an asymptotic owner-demand contradiction.

The multicolor theorem instead has slope one half.

Therefore the general-r programme should now seek a shell/extraction theorem of the form

> `some common-S family has N>(1/2+c)r-O(1)`

for any fixed `c>0`, or even `N>=r/2+C(epsilon)` with a sufficient constant gap.

Such a theorem would immediately contradict the present capacity throughout a fixed-deficit residual window.

## 5. New high-leverage bridge

This identifies a more precise downstream target than improving sunflower constants:

> **Majority Common-S Extraction Lemma.** In every non-anchor/non-improving maximal shell near the extremal residual layer, more than half of the scalable regular owners share one missing set S (or one canonical zero-skeleton which induces such a family).

Combined with the present theorem, that would close the concentrated-support branch for all sufficiently large r.

The unresolved issue is therefore owner *demand*, not owner capacity.
