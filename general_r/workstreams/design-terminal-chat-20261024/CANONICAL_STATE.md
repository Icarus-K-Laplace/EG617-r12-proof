# General-r design-terminal workstream — canonical state

Date: 2026-10-24
Branch: `workstream/general-r-design-terminal-20261024`
Scope: only the `(5r+1)` front-end terminal / stability / nonextension branch.

## Headline state

- `5r+1` is **STRUCTURAL**, not numerology: at an anchor of target degree `r-1`, after an inclusion-maximal packing of `r-6` target `K_r` blocks in the anchor nonneighbourhood, the residual has exactly `5r+1` vertices. Status: **PROVED_SYMBOLIC**.
- The general forcing implication `failure of (4r+1) extraction => this anchored stop` is **OPEN** and belongs to the interface with the residual-extraction workstream.
- Once the anchored stop is reached under the contextual assumption that no legal `(4r+1)` residual exists, the residual has `alpha=5`, `omega<=r-1`, `delta>=r`, and inherits all multicolor density caps. Status: **PROVED_SYMBOLIC**.
- The r=12 facts `delta in {12,13}`, outer defect at most 11, and `z=0` are **NOT** general terminal axioms. The two-row minimum-degree window ceases to follow from the anchor budget already at `r>=16`; for `r>=20` the hereditary cap itself forces quadratic outer charge. Status: **PROVED_SYMBOLIC / DISPROVED_AS_GENERAL_PATTERN**.

## Main new theorem: linear total multicolor slack on `5r+1`

Let `W` be a `(5r+1)` terminal residual. Write color 0 for the target color. Define

- `s_0=e(G_0[W])-p_5(5r+1)`,
- `s_i=e(G_i[W])-p_r(5r+1)` for `1<=i<=r-1`.

Then

`p_5(5r+1)=(5r^2-3r)/2`,

`p_r(5r+1)=10r+5`,

and the edge partition gives the exact identity

> `sum_{i=0}^{r-1} s_i = 9r+5`.

Status: **PROVED_SYMBOLIC**.

This is the key stability gain: on the terminal, the *total* Turan slack of all `r` colors is only `O(r)`, rather than `Theta(r^3)` on the original `r^2+1` vertex set.

## Target-color strict Brouwer gap

The target complement is `K_6`-free and non-5-partite. Brouwer gives `s_0>=r-1`. Kang--Pikhurko classify equality. Every equality graph contains an independent part of size at least `r`, while the terminal target clique cap gives `alpha(complement)=omega(target)<=r-1`. Hence equality is impossible:

> `s_0 >= r`.

Therefore

> `sum_{i=1}^{r-1}s_i <= 8r+5`.

Status: **PROVED_ANALYTIC** (using verified Brouwer and Kang--Pikhurko theorems).

## Simultaneous stability / finite geometry

Furedi's quantitative Turan stability applied to every color complement produces ideal clique partitions `Q_i` on the same vertex set with

> `sum_i |E(G_i) Delta E(Q_i)| <= 27r+15`.

The target ideal is a union of 5 clique blocks; every non-target ideal is a union of `r` clique blocks. The induced ideal edge multiplicity `m(e)` satisfies

> `sum_e |m(e)-1| <= 27r+15`.

For the non-target partitions, the total block-size energy obeys

> `sum_{i=1}^{r-1} sum_j (|B_{ij}|-5)^2 <= 65r+39`.

Consequently, after deleting at most `92r+54` non-target ideal blocks in total, the surviving blocks are:

1. size 5;
2. exact transversals of the 5 target ideal groups;
3. pairwise linear (two surviving blocks share at most one point);
4. still grouped by color into partial parallel classes.

Thus every terminal is within linear defect of a **partial resolvable transversal design `TD(5,r)` / 5-GDD geometry**. Status: **PROVED_ANALYTIC**.

This is the precise finite-geometric interpretation presently justified. It is not yet an affine-plane classification.

## Nonextension progress

- Existing architecture theorem: the standard affine-plane `r^2` construction cannot accept one extra vertex; more abstractly, two exact orthogonal `r`-by-`r` clique partitions already imply nonextension. Status: **PROVED_ANALYTIC** upstream.
- New local cylinder lemma: if an ideal target group contains a deleted target edge `uv`, then `alpha(target)<=5` forces at least `L` cross-group target edges, where `L` is the minimum size of the other four ideal groups. In the equal-size equality case, the minimum cover is a one-coordinate two-owner star. Status: **PROVED_ANALYTIC**.
- The target clique cap forces at least 6 internal deletions from any 5-clique ideal partition. Status: **PROVED_ANALYTIC**.
- The naive exact `RTD(5,r)+one extra point` completion is impossible for `r>=6`: it already violates the target clique cap, and even if that cap is ignored, an SDR across the omitted parallel class gives a target-independent 6-set. Status: **PROVED_ANALYTIC**.

## Current success level

- D1 (precise symbolic terminal): **achieved conditionally on reaching the `d=r-1,j=r-6` stop**.
- D2 (front failure forces terminal): **OPEN**; interface theorem from Chat A is missing.
- D3 (classify all sufficiently large terminals): **OPEN**, but now reduced to `O(r)`-defect partial resolvable `TD(5,r)` objects.
- D4 (nonextension for sufficiently large r): **OPEN**.
- D5 (all r>3): **OPEN**.

## Single largest blocker

> **Defect-to-rigidity theorem:** classify or eliminate an `O(r)`-defect partial resolvable `TD(5,r)` on `5r+1` points under the original color-completion constraints.

The present bound is strong enough to leave only `O(r)` exceptional block incidences among `Theta(r^2)` design blocks, but those exceptions can still be distributed over all vertices. A repair theorem, concentration theorem, or direct extra-point incidence contradiction is still required to close the sufficiently-large-r terminal branch.
