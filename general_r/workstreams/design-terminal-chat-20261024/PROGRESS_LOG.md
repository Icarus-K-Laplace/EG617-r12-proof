# Progress log

## 2026-10-24 — initial design-terminal pass

### Repository isolation

Created branch `workstream/general-r-design-terminal-20261024` from `workstream/general-r-architecture-20261024`. This workstream modifies only `general_r/workstreams/design-terminal-chat-20261024/`.

### Source archaeology completed

Read the general-r front structural source, constant dictionary, multicolor Turan stability route, affine-plane nonextension theorem, and r=12 front-end bridge / T61 / E397--E405 / S30-S31 source files.

Key archaeology verdicts:

- `61=5r+1` is exact anchor/block algebra;
- `408=3r^2-2r` is exact anchor-ledger algebra;
- `alpha=5`, `omega<=r-1` are structural at the stop;
- under contextual no-extraction, `delta>=r` is symbolic;
- r=12 `delta<=r+1`, outer defect<=11, and `z=0` do not scale.

### New analytic results — pass 1

1. **Exact terminal slack budget:** `sum_i s_i=9r+5`.
2. **Strict target gap:** `s_0>=r` using Brouwer plus Kang--Pikhurko equality classification.
3. **Non-target slack budget:** `sum_(i>0)s_i<=8r+5`; for `r>=15` some non-target color has slack at most8.
4. **Simultaneous stability:** ideal clique partitions exist with total edit distance at most `27r+15`.
5. **Block energy:** non-target total size-deviation energy at most `65r+39`.
6. **Partial RTD theorem:** after deleting at most `92r+54` ideal non-target blocks, at least `r^2-93r-54` clean blocks form partial parallel classes of a linear transversal 5-GDD.
7. **Cylinder lemma:** one internal target deletion forces a linear-size cross-edge cover; equality has one-coordinate two-owner-star form in the equal-group case.
8. **Construction search:** the naive exact `RTD(5,r)+one point` model is impossible for `r>=6`.

## 2026-10-24 — defect concentration pass

The first pass still allowed the `O(r)` correction budget to be distributed over all vertices. The hereditary density caps rule this out for target internal defects.

### Constant-width target partition

For the five Furedi target groups `B_j`, let `D` be the number of ideal internal target edges absent in the actual target graph. The inherited cap on each `B_j` gives

`D >= (r-1) sum_j(|B_j|-r)_+`.

Since Furedi gives `D<=27r+15`, for `r>=44` the total positive size deviation is at most27. As the five deviations sum to1,

> `r-26<=|B_j|<=r+27`.

Status: **PROVED_ANALYTIC**.

### Refined cylinder degree bound

Let `A` be the number of target cross-group additions. Every internal target deletion `uv` satisfies

`d_cross(u)+d_cross(v) >= H_r`,

`H_r=(r-26)-(27r+15)/(r-26)=r-53+o(1)`.

This follows by covering the four-dimensional tuple product: edges incident to `u` or `v` cover at most a `1/L` fraction, while other cross edges cover at most `1/L^2`.

Status: **PROVED_ANALYTIC**.

### Bounded hub set

For `r>=70`, define

`X={v:d_cross(v)>=H_r/2}`.

Every target internal deletion touches `X`, while total cross degree is `2A<=54r+30`. Therefore

> `|X|<=4(27r+15)/H_r=108+o(1)`.

In particular `|X|<=114` for `r>=1000`.

Outside `X`, every target ideal group is an actual target clique. Status: **PROVED_ANALYTIC**.

### Updated blocker

The target-side defect layer is no longer allowed to disperse. The remaining high-leverage task is:

> propagate the same bounded-hub concentration to the `O(r)` bad non-target blocks / pair-multiplicity defects, or derive an omitted-color `(r+1)`-set when they avoid the hub kernel.

If successful, the large-r terminal reduces to an exact large transversal-design core plus `O(1)` exceptional vertices, which is a much sharper nonextension target.

### Status

D1 remains reached conditionally. D2 is still the Chat-A interface. D3/D4 are not closed, but the large-r survivor has been reduced from arbitrary `O(r)`-defect geometry to a bounded target-hub kernel plus an `r^2-O(r)` partial resolvable TD core.
