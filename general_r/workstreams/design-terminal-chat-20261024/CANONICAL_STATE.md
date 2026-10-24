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
- D3: **OPEN as a classification route**; later theorem proves the contextual terminal family is empty for all `r>=6212`.
- D4: **OPEN**; the attempted `r>=6212` closure was withdrawn after finding an invalid clique/independence inference.
- D5: **OPEN** for the remaining finite parameter range; this does not close the front-end forcing interface.

## Single largest blocker

> **Hub propagation / exact-core theorem:** prove that the remaining `O(r)` non-target block and pair-multiplicity defects must also pass through the same `O(1)` exceptional hub kernel (or else force an omitted-color `(r+1)`-set).

If this propagation is proved, deleting `O(1)` exceptional vertices should expose an exact or near-exact large `TD(5,r)` core, making a robust nonextension theorem substantially more accessible.


## 2026-10-24 initial hub audit (superseded)

An initial low-incidence edit bound was proposed, along with a (d_i=6) singleton/4-block pattern. Adversarial checking found both proof gaps: the low-incidence argument ignored hub-incident target deletions and ordinary-label gaps; the (d_i=6) pattern failed to control independent sets that double two missing pairs. These claims were withdrawn. The corrected status and surviving results are recorded immediately below.

## 2026-10-24 correction — adversarial hub/cylinder audit

This section supersedes the earlier Hub Propagation subsection and any claim that a low-incidence off-hub pair necessarily costs Ω(r) non-target edits.

### Withdrawn

- The unconditional (d_i\le5\Rightarrow(6-d_i)(r-1)) edit bound is **DISPROVED as stated**; it overlooked target-deleted pairs incident to hubs and blocks lacking ordinary group representatives.
- The (d_i=6) singleton/4-block pattern is withdrawn as an (\alpha(G_i)\le r) example: an independent set can double two missing pairs while omitting the special cover block.
- The claimed “at most 27 low-incidence colors” consequence is withdrawn.

### Valid new statements

1. **Conditional ordinary-label cylinder lemma — PROVED_CONDITIONAL.** If every other ideal block contains an ordinary (B_k\setminus X) point for some (k\ne j), then a missing off-hub repeated pair (uv\subset B_j\setminus X) forces at least (r-1) non-target edits. The full hypothesis is recorded in `HUB_PROPAGATION_THEOREM.md`.
2. **Target-alpha K6 exclusion — PROVED_ANALYTIC.** (\alpha(G_0)\le5) implies every non-target (G_i) is (K_6)-free. Thus a **single-endpoint full star** to a clean 5-clique ideal block is impossible: it would create a (K_6) in (G_i). A split two-endpoint star can avoid this local K6 obstruction.
3. **Defect propagation insight — PROVED_CONDITIONAL.** A single-endpoint full star to a size-5 clique creates a forbidden K6, but split two-endpoint covers and multi-block barriers remain possible. The claim that every cheap cover creates a further defect is not proved.
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


## 2026-10-24 update — exact local closure and target-label blocker

### New verified local gadget

A two-block one-color gadget has one 6-block with a single missing pair, one 5-block with a single missing pair, and nine cross-block additions. It satisfies (\alpha(G_i)\le r) and (K_6)-freeness, with
[
R_i=2,\quad A_i=9,\quad s_i=7,\quad
|E(G_i)\triangle E(Q_i)|=11.
]
Full construction and verification are in `HUB_PROPAGATION_THEOREM.md`. It is **not** a target-labelled terminal coloring, but it proves that the non-target local conditions alone do not force a third defect or (s_i>8).

### Target-label obstruction

If (w\in B_j) has a target cross-star to (B_k), and (x\in B_k) lies in the same non-target ideal block as (w), then (wx) is a target-colored edge missing from (G_i). In a candidate cover block, an ordinary (z_k\in B_k\setminus X) cannot be adjacent to either (w) or (x) in (G_i), since both (wz_k) and (xz_k) are target-colored. A one-block cover therefore needs an exceptional (B_k)-point, or else the cover must involve other selected blocks / a further target-internal deletion.

A 9-edge two-coordinate barrier can handle one fixed blocked coordinate locally, so the global proof must count the full multi-block barrier network and pair ownership.

### Current blocker (updated)

The required theorem is a **target-labelled global cover inequality**. The previous simpler claim that K6-freeness forces every cheap cover to propagate indefinitely is too strong. The two-block gadget shows the local slack can be 7; the target labels are what may force higher cost or a global contradiction.

- Full Hub Propagation: **OPEN**.
- Exact-core route: **OPEN**.
- Robust nonextension: **OPEN**.
- No sufficiently-large-(r) closure is claimed.


## 2026-10-24 update — target-star permutation constraint

### Conditional theorem: destination map is a derangement

In the **exact hub-star model** (every target cross-group edge belongs to the specified hub stars, with no additional cross edges), each group (B_j) has a hub (a_j) with an internal target nonneighbor and a full target cross-star to (B_{f(j)}), where (f(j)\ne j). The target independence cap forces
[
\boxed{f\text{ is a derangement permutation on five groups}.}
]
If two groups share a destination, the two internal nonedges plus one point from each of the two groups outside the source groups and the omitted destination form a target-independent 6-set.

If the oversized group has a second hub with an internal nonneighbor and a full star, its destination must equal the first hub's destination; otherwise the same collision contradiction applies. The two oversized-group hubs must be target-adjacent, since otherwise the two hubs plus an ordinary point in their group and three points from groups avoiding their shared destination form an independent 6-set.

Status: **PROVED_CONDITIONAL** on the exact hub-star model; it does not yet prove every terminal reduces to that model. An O(r)-edge perturbation needs a stability version of this lemma.

### Conditional triangle obstruction

If the two oversized-group hubs and their common destination representative lie in one non-target ideal block, all three pairwise edges are target-colored, so they form an independent triple in (G_i). If all cross-block additions are confined to a single cover block, omitting that block yields an independent ((r+1))-set. Thus such a block requires a multi-block cover network, or the two hubs must be split / the block must omit the destination group.

### Updated structural frontier

The target correction map is no longer arbitrary: its five group-level destinations must form either a 5-cycle or a disjoint 2-cycle plus 3-cycle. The cheapest target-star clustering is ruled out. The next task is to classify the distribution of the oversized-group hubs across non-target ideal blocks and derive a lower bound for the required cover network.

- Destination-injectivity: **PROVED_CONDITIONAL**.
- Triangle obstruction: **PROVED_CONDITIONAL**.
- Full Hub Propagation: **OPEN**.
- Exact-core route: **OPEN**.
- Robust nonextension: **OPEN**.


## 2026-10-24 update — robust pair-of-nonedges inequality

For two internal target nonedges (P_j\subset B_j), (P_k\subset B_k) with all four cross pairs between them target-nonedges, define (U_\ell) in each remaining group as the vertices with no target edge to any endpoint of (P_j\cup P_k). If (A) is the total target cross-edge count, then
[
\boxed{|U_\ell||U_m|\le A\quad(\ell\ne m).}
]
Otherwise there are more candidate pairs in (U_\ell\times U_m) than target cross edges globally, so one pair avoids the target color and forms a target-independent 6-set with (P_j,P_k).

Because (A\le27r+15), at least two of the three remaining groups have at most (O(\sqrt r)) points outside the union of the four endpoint neighborhoods. This gives a robust partial version of the exact-star destination constraint.

Status: **PROVED_CONDITIONAL** on compatibility of the two source nonedges (their four cross pairs must be target-nonedges). The open bridge is to find a sufficiently large family of compatible source pairs or charge the conflicts to the global budget. Full Hub Propagation remains **OPEN**.


## 2026-10-24 — attempted bounded target-defect closure withdrawn

The claimed (r\ge6212) terminal nonexistence theorem is **WITHDRAWN** after adversarial review. The proof incorrectly asserted that a hub has at most four target-nonneighbors in (B_j\setminus X). Those ordinary vertices form a clique, so this does not produce an independent six-set. Consequently the claimed constant upper bound (D\le6210) was not proved.

The valid surviving statement is the color-ownership lower bound: some (B_h) has size at least (r+1), and each non-target color must own an edge inside any fixed ((r+1))-subset of (B_h). Hence
[
D_h:=\left|\binom{B_h}{2}\setminus E(G_0)\right|\ge r-1.
]
This is compatible with the current (O(r)) edit budget and does not close the terminal.

A bounded hub set can still support (O(r)) internal missing edges: each hub may be nonadjacent to (Theta(r)) points of the ordinary clique. The clique cap (omega(G_0)\le r-1) limits its internal neighbors, not its nonneighbors.

- Bounded target hub concentration: **PROVED_ANALYTIC**.
- Oversized-group lower bound (D_h\ge r-1): **PROVED_ANALYTIC**.
- Constant target-defect cap: **DISPROVED as stated**.
- Contextual terminal nonextension for sufficiently large (r): **OPEN**.
- Literal multi-block Hub Propagation: **OPEN**.
- Full front-end forcing: **OPEN**.

Full correction: `JOINT_DEFECT_PROPAGATION.md`.
