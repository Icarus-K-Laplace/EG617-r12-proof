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


## 2026-10-24 update — Hub propagation audit

### New proved component

For each non-target ideal partition (Q_i=\bigcup_{a=1}^rK(C_a)), let (d_i) count repeated target-group incidences and (m_{ij}=r-\#\{a:C_a\cap B_j\ne\varnothing\}). Then
[
\sum_{j=1}^5m_{ij}=d_i-1.
]
If a repeated-group pair (uv\subset B_j\setminus X) is absent from (G_i) and (d_i\le5), then
[
|E(G_i)\triangle E(Q_i)|\ge(6-d_i)(r-1).
]
For (r\ge44), at most 27 non-target colors can contain such a low-incidence off-hub pair. Status: **PROVED_ANALYTIC**. Full proof: `HUB_PROPAGATION_THEOREM.md`.

### High-incidence warning

A concrete one-color block system with (d_i=6), eight nonclean blocks, (s_i=9), edit distance (10), and size energy (23) satisfies (\alpha(G_i)\le r) while its repeated-group pairs lie outside (X). It is not a full terminal coloring, but it proves that scalar stability budgets and one-color independence alone do **not** force all non-target defects into the target hub set. Status of the naive local propagation claim: **DISPROVED**. Full global Hub Propagation remains **OPEN**.

### Exact-core / nonextension status

The (r^2-O(r)) clean-block count still does not imply an exact TD or two exact orthogonal partitions. Up to (\lfloor(8r+5)/9\rfloor=\Theta(r)) copies of the local high-incidence pattern fit the scalar non-target slack budget; whether they can coexist with global pair-disjointness and the target cross-cover is unresolved.

The sharp remaining blocker is a **global pair-disjointness / trap-completion inequality** ruling out a linear family of high-incidence traps, or else an explicit globally compatible construction. No such inequality is currently proved.

Updated success levels:
- D1: conditionally achieved.
- D2: **OPEN** (Chat A interface).
- Low-incidence part of hub propagation: **PROVED_ANALYTIC**.
- Full Hub Propagation: **OPEN**.
- D3 exact terminal classification: **OPEN**.
- D4 robust nonextension: **OPEN**.
- D5: **OPEN**.

Latest substantive assets:
- `HUB_PROPAGATION_THEOREM.md`
- `MULTICOLOR_DEFECT_BUDGET.md`
- `ROBUST_EXACT_CORE.md`
- `NONEXTENSION_CLOSURE.md`

This update supersedes any earlier suggestion that the bounded target-hub result alone should expose an exact core after deleting (O(1)) vertices; that conclusion requires the still-open non-target propagation theorem.


## 2026-10-24 correction — adversarial hub/cylinder audit

This section supersedes the earlier Hub Propagation subsection and any claim that a low-incidence off-hub pair necessarily costs Ω(r) non-target edits.

### Withdrawn

- The unconditional (d_i\le5\Rightarrow(6-d_i)(r-1)) edit bound is **DISPROVED as stated**; it overlooked target-deleted pairs incident to hubs and blocks lacking ordinary group representatives.
- The (d_i=6) singleton/4-block pattern is withdrawn as an (\alpha(G_i)\le r) example: an independent set can double two missing pairs while omitting the special cover block.
- The claimed “at most 27 low-incidence colors” consequence is withdrawn.

### Valid new statements

1. **Conditional ordinary-label cylinder lemma — PROVED_CONDITIONAL.** If every other ideal block contains an ordinary (B_k\setminus X) point for some (k\ne j), then a missing off-hub repeated pair (uv\subset B_j\setminus X) forces at least (r-1) non-target edits. The full hypothesis is recorded in `HUB_PROPAGATION_THEOREM.md`.
2. **Target-alpha K6 exclusion — PROVED_ANALYTIC.** (\alpha(G_0)\le5) implies every non-target (G_i) is (K_6)-free. Thus a one-block star cover to a clean 5-clique ideal block is impossible: it would create a (K_6) in (G_i).
3. **Defect propagation insight — PROVED_ANALYTIC locally.** Any cheap cylinder cover must make its cover block non-clique in the actual non-target color; the resulting new defect must itself be covered. The global chain/cycle cost is still **OPEN**.
4. **Exact cross-pair budget — PROVED_SYMBOLIC.**
[
A=9r+5-\Delta_0+D-S_{\rm non},
\]
where (A) is target cross edges, (D) target internal deletions, and (S_{\rm non}=\sum_{i>0}s_i).

The one-color constant-cost star construction is not a full-terminal counterexample: it violates target (\alpha\le5) by creating a (K_6) in a non-target color. It is useful only as an adversarial audit showing that the target-alpha constraint must be used jointly.

### Current blocker and success levels

The remaining task is a **defect-chain cost theorem**: every cover of a non-target missing pair creates a further defect unless it makes a forbidden (K_6); prove that all such chains/cycles exceed the combined (O(r)) slack and target cross-cover budget, without double-counting pairs.

- D1: conditionally achieved as before.
- D2: **OPEN** (Chat A interface).
- Conditional cylinder lemma: **PROVED_CONDITIONAL**.
- Full Hub Propagation: **OPEN**.
- Exact-core route: **OPEN**.
- Robust nonextension D4: **OPEN**.
- D5: **OPEN**.

Corrected assets: `HUB_PROPAGATION_THEOREM.md`, `MULTICOLOR_DEFECT_BUDGET.md`, `ROBUST_EXACT_CORE.md`, `NONEXTENSION_CLOSURE.md`, `PROGRESS_LOG.md`.
