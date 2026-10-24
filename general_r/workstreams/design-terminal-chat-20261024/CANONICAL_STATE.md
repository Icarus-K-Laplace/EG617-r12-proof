# General-r design-terminal workstream — canonical state

Date: 2026-10-24
Branch: `workstream/general-r-design-terminal-20261024`
Scope: only the `(5r+1)` front-end terminal / stability / nonextension branch.

## Headline state

- `5r+1` is **STRUCTURAL**, not numerology: at an anchor of target degree `r-1`, after an inclusion-maximal packing of `r-6` target `K_r` blocks in the anchor nonneighbourhood, the residual has exactly `5r+1` vertices. Status: **PROVED_SYMBOLIC**.
- The general forcing implication `failure of (4r+1) extraction => this anchored stop` is **OPEN** and belongs to the interface with the residual-extraction workstream.
- Once the anchored stop is reached under the contextual assumption that no legal `(4r+1)` residual exists, the residual has `alpha=5`, `omega<=r-1`, `delta>=r`, and inherits all multicolor density caps. Status: **PROVED_SYMBOLIC**.
- The r=12 facts `delta in {12,13}`, outer defect at most 11, and `z=0` are **NOT** general terminal axioms. The two-row minimum-degree window ceases to follow from the anchor budget already at `r>=16`; for `r>=20` the hereditary cap itself forces quadratic outer charge. Status: **PROVED_SYMBOLIC / DISPROVED_AS_GENERAL_PATTERN**.

## Exact local multicolor slack theorem

Let `W` be a `(5r+1)` terminal residual. Write color 0 for the target color and define

- `s_0=e(G_0[W])-p_5(5r+1)`,
- `s_i=e(G_i[W])-p_r(5r+1)` for `1<=i<=r-1`.

Then

`p_5(5r+1)=(5r^2-3r)/2`,

`p_r(5r+1)=10r+5`,

and the color edge partition gives

> **`sum_i s_i = 9r+5`.**

Status: **PROVED_SYMBOLIC**.

The target complement is `K_6`-free and non-5-partite. Brouwer plus the Kang--Pikhurko equality classification sharpen the target deficit to

> **`s_0>=r`.**

Therefore

> **`sum_(i>0)s_i<=8r+5`.**

Status: **PROVED_ANALYTIC**.

## Simultaneous multicolor stability

Furedi stability applied to every color complement supplies ideal clique partitions `Q_i` with

> `sum_i |E(G_i) Delta E(Q_i)| <=27r+15`.

The ideal edge multiplicities satisfy

> `sum_e |m(e)-1|<=27r+15`.

For the non-target partitions,

> `sum_(i>0)sum_j(|B_ij|-5)^2<=65r+39`.

After deleting at most `92r+54` non-target ideal blocks, at least

> `r^2-93r-54`

surviving blocks are size-5 exact transversals of the five target ideal groups, form partial parallel classes by color, and are pairwise linear.

Thus the terminal is `O(r)` block-defect away from a partial resolvable `TD(5,r)` / transversal 5-GDD geometry. Status: **PROVED_ANALYTIC**.

## Stronger target-side rigidity: constant-width + bounded hubs

`DEFECT_CONCENTRATION.md` strengthens generic stability using the hereditary density caps.

Let the five target ideal groups have sizes `a_1,...,a_5`. If `D` is the number of ideal internal target edges deleted, then

`D >= (r-1) sum_j(a_j-r)_+`,

while Furedi gives `D<=27r+15`. Hence for every `r>=44`,

> **`r-26 <= a_j <= r+27` for every target ideal group.**

So the target partition is `r+O(1)`, not merely `r+O(sqrt r)`.

Let `A` be the number of target cross-group additions. For every deleted internal target edge `uv`, the product-cover argument gives

`d_cross(u)+d_cross(v) >= H_r`,

where

`H_r=(r-26)-(27r+15)/(r-26)=r-53+o(1)`.

For `r>=70`, define the hub set

`X={v:d_cross(v)>=H_r/2}`.

Then every target internal deletion touches `X`, and

> **`|X|<=4(27r+15)/H_r =108+o(1)`.**

For example `|X|<=114` for `r>=1000`. Outside `X`, each target ideal group is an actual target clique. Status: **PROVED_ANALYTIC**.

This changes the asymptotic picture materially: target internal corrections cannot be spread across all `5r+1` vertices. They are forced through a bounded exceptional kernel.

## Nonextension progress

- The existing affine-plane theorem says two exact orthogonal `r`-by-`r` clique partitions already imply nonextension. Status: **PROVED_ANALYTIC upstream**.
- A deleted target edge forces a linear-size cross-edge cylinder cover; minimum equal-group covers have a one-coordinate two-owner-star form. Status: **PROVED_ANALYTIC**.
- The naive exact `RTD(5,r)+one extra point` completion is impossible for `r>=6`; it violates the target clique cap and, even without that cap, yields a target-independent 6-set. Status: **PROVED_ANALYTIC**.

## Current success level

- D1: **achieved conditionally** on reaching `d=r-1,j=r-6`.
- D2: **OPEN** — Chat A interface still has to force the stop.
- D3: **OPEN**, but the surviving large-r geometry is now reduced to a bounded target-hub kernel plus an `r^2-O(r)` partial resolvable transversal design.
- D4: **OPEN**.
- D5: **OPEN**.

## Single largest blocker

> **Hub propagation / exact-core theorem:** prove that the remaining `O(r)` non-target block and pair-multiplicity defects must also pass through the same `O(1)` exceptional hub kernel (or else force an omitted-color `(r+1)`-set).

If this propagation is proved, deleting `O(1)` exceptional vertices should expose an exact or near-exact large `TD(5,r)` core, making a robust nonextension theorem substantially more accessible.
