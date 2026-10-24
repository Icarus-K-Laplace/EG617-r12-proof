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


## 2026-10-24 — Hub propagation / exact-core audit

### Frozen source read

Read and froze the current versions of:
- `CANONICAL_STATE.md`
- `DESIGN_TERMINAL_DEFINITION.md`
- `DEFECT_CONCENTRATION.md`
- `STABILITY_THEOREMS.md`
- `NONEXTENSION.md`
- `COUNTEREXAMPLES.md`
- `R12_TO_GENERAL_SOURCE.md`
- `T61_GENERALIZATION_MAP.md`
- `PROGRESS_LOG.md`

No sibling branch or directory was modified.

### New theorem: low-incidence hub propagation

For a non-target ideal partition (Q_i=\bigcup_{a=1}^rK(C_a)), define repeated-group incidence (d_i) and missing-group incidences (m_{ij}). The exact identity is
[
\sum_{j=1}^5m_{ij}=d_i-1.
]
If a repeated-group pair (uv\subset B_j\setminus X) is missing from (G_i) and (d_i\le5), then
[
|E(G_i)\triangle E(Q_i)|\ge(6-d_i)(r-1).
]
Proof: (m_{ij}\ge1), otherwise (u,v) plus one (B_j)-point from each other block is an (i)-independent ((r+1))-set. At least (6-d_i) other group labels occur in every block. For each such label, every point in each other block must be joined in (G_i) to (u) or (v), giving ((r-1)) distinct cross-block edits per label.

Thus for (r\ge44), at most 27 colors can contain a low-incidence ((d_i\le5)) repeated-group pair away from the target hub set. Status: **PROVED_ANALYTIC**.

### Counterexample attack: high-incidence trap

An explicit one-color abstract block system was constructed for every (r\ge8):
- six 6-blocks, one singleton, one 4-block, and (r-8) 5-transversals;
- target-group sizes exactly ((r,r,r,r,r+1));
- repeated-group incidence (d_i=6);
- ideal excess (Delta_i=11), six deleted repeated-group edges and four added cross-block edges;
- actual color slack (s_i=9), edit distance (10), size energy (23), and (\alpha(G_i)\le r).

The singleton label is 1; the 4-block has labels 2,3,4,5; their four cross edges block every ((r+1))-set that doubles a missing repeated-group pair. The six repeated pairs can all be placed outside (X).

This is **not** a full terminal coloring: other colors, target cross-cover, and global pair-disjointness have not been completed. It does disprove the naive local inference that scalar stability and a one-color independence condition alone force every non-target defect to touch (X). Up to (lfloor(8r+5)/9\rfloor=\Theta(r)) such patterns fit the scalar non-target slack bound, so the high-incidence regime cannot be discarded by budget rhetoric alone.

### New assets and commits

- `HUB_PROPAGATION_THEOREM.md`: HP-LI proof and explicit high-incidence obstruction. Commit: `ac5dbeb393a661a85a13e3b24e74a2a2933f520b`.
- `MULTICOLOR_DEFECT_BUDGET.md`: exact per-color ledger and global defect accounting. Commit: `085d81cf4c5868784e231ceacd4396b84c9988b9`.
- `ROBUST_EXACT_CORE.md`: exact-core boundary and missing interface theorem. Commit: `99d8d3afb51a0bca18f4abd7dbd5424d6d81a816`.
- `NONEXTENSION_CLOSURE.md`: exact cross-pair budget and nonextension blocker. Commit: `f6e2cf8ae9dec20a8153c22b9dc6a9a3024d8d54`.

### Current blocker

The remaining task is a **global pair-disjointness / trap-completion inequality**: rule out a linear family of (d_i\ge6) local traps after enforcing that every cross-group pair has exactly one actual color, target cross edges are unavailable to non-target colors, and target internal deletions are a finite resource. Alternatively, construct a globally compatible family. No such inequality is proved yet.

### Status

- D1: conditionally reached as before.
- Low-incidence part of D3: **PROVED_ANALYTIC**.
- Full Hub Propagation: **OPEN**.
- Exact-core route: **OPEN**.
- Robust nonextension D4: **OPEN**.
- No sufficiently-large-(r) closure is claimed.
