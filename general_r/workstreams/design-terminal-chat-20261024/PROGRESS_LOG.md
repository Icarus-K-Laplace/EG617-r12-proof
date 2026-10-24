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

### New analytic results

1. **Exact terminal slack budget:** `sum_i s_i=9r+5`.
2. **Strict target gap:** `s_0>=r` using Brouwer plus Kang--Pikhurko equality classification.
3. **Non-target slack budget:** `sum_(i>0)s_i<=8r+5`; for `r>=15` some non-target color has slack at most8.
4. **Simultaneous stability:** ideal clique partitions exist with total edit distance at most `27r+15`.
5. **Block energy:** non-target total size-deviation energy at most `65r+39`.
6. **Partial RTD theorem:** after deleting at most `92r+54` ideal non-target blocks, at least `r^2-93r-54` clean blocks form partial parallel classes of a linear transversal 5-GDD.
7. **Mandatory target corrections:** at least six ideal internal target edges must be deleted to enforce `omega<=r-1`.
8. **Cylinder lemma:** one internal target deletion forces at least the minimum opposite-group size many target cross edges; equality has one-coordinate two-owner-star form in the equal-group case.
9. **Construction search:** the naive exact `RTD(5,r)+one point` model is impossible for `r>=6`.

### Current blocker

Convert `O(r)` global defect in an almost-complete resolvable `TD(5,r)` into exact rigidity/nonextension. Candidate next directions:

- classify the one-defect-per-color incidence vector;
- prove defects concentrate on `O(1)` exceptional points or derive a contradiction if they disperse;
- exploit pair-capacity across the five groups to recover two exact orthogonal partitions on a large core;
- combine the cylinder lemma for multiple mandatory internal deletions to force incompatible owner coordinates.

### Status

D1 reached conditionally; D2/D3/D4 remain open. No sufficiently-large-r closure is claimed.
