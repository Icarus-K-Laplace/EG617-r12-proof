# Progress log

## 2026-10-24 — initialization

- Created isolated branch `workstream/general-r-three-anchor-20261024` from `workstream/general-r-architecture-20261024`.
- Reverified the anchor-incidence partition symbolically: `c+t=4`, `d_1+d_2+d_3=c-2`, four block patterns only.
- Derived the exact connector-miss identity `q_i=d_j+d_k`, fixing the connector type multiset for every pattern.
- Complement formulation initially gave an analytic large-r theorem via Andrasfai–Erdos–Sos.

## 2026-10-24 — parity collapse

- Observed that `K_r=2e-r(3r-1)` is always even.
- Therefore the contradiction branch is `K<=6`, not `K<=7`.
- This removed the entire apparent `K=7` equality layer and sharpened the complement/AES threshold from `r>=68` to `r>=60`.

## 2026-10-24 — c=2 closure

- Proved a parameter-free tripartite transversal-cover lemma for maximum cross degree two.
- Closed the full `c=2`, `(r-2,r-2,r-2)` geometry for every `r>=12`.

## 2026-10-24 — rectangle/focus mechanism

- Proved the pair-connector rectangle lemma: if pair connector `z` misses `ak`, its nonneighbour sets in the two incident exclusive blocks span a complete bipartite graph.
- Converted rectangles into excess charges using the exact baseline external capacities `2+d_i`.
- Proved additivity when rectangles share one block but have disjoint opposite blocks.
- Proved the common-nonneighbour clique lemma for nonadjacent connector pairs.
- Proved same-missing-anchor disjointness for nonadjacent pair connectors.

## 2026-10-24 — c=3 closure

- Closed `c=3`, deficits `(0,0,1)`, for every `r>=13`.
- Two nonfocused pair connectors are too expensive; two focused connectors force a large common-nonneighbour rectangle; exactly one focus remains.
- Eliminated the unique `r=13,K=6` mixed-focus boundary using the triple connector degree budget.

## 2026-10-24 — c=4 large-r closure

- Introduced focus collision.
- For `(0,0,2)`, at most two connectors can focus on `X3`; this first closed the geometry for `r>=17`.
- For `(0,1,1)`, no two connectors can focus on the same deficit-1 block; this first closed the geometry for `r>=17`.
- At this point the full Exact Three-Anchor theorem was proved for all `r>=17`.

## 2026-10-24 — boundary compression to r>=13

- Eliminated the remaining `r=16,15,14,13` layers analytically in both `c=4` geometries.
- `(0,0,2)`:
  - `r=16`: two required nonfocused connectors cannot fit two local six-unit charges;
  - `r=15`: adjacency forces `k=6` on each nonfocused connector;
  - `r=14`: the only shared `(10,1)` equality rectangle saturates an `X3` vertex that focused connectors must meet;
  - `r=13`: cross-group equality forces `(k,a,b)=(3,4,2)` and is incompatible with required focus; same-group focus strengthens the effective `X3` capacity from four to two and closes the last branch.
- `(0,1,1)`:
  - `r=16,15`: the `(0,1)` connectors focus and the two type-U nonfocus rectangles exceed budget;
  - `r=14`: the only nonfocused `(0,1)` boundary `(k,a,b)=(6,3,2)` would force three other connectors to focus on the same block;
  - `r=13`: both `(0,1)` connectors focus; the type-U pair is killed by disjoint `(3,3)` equality rectangles or by the strengthened `(2,2)` charge when adjacent.

## 2026-10-24 — Level-4 r=12 absorption

- Reopened only the proof-engineering residue at `r=12`; no historical fixed-r case table was imported.
- `c=3`, `(10,10,9)`:
  - both-nonfocus costs at least eight;
  - both-focus contradicts the clique cap through a common-nonneighbour clique of size at least 13;
  - the mixed-focus branch is governed by effective `R22`;
  - every low-budget layer has a saturated rectangle vertex, which forces the triple/focused connector to cover all or almost all of the opposite 10-clique, yielding a 12-clique or an impossible degree count.
- `c=4`, `(10,10,8)`:
  - classified by `f=0,1,2` focused connectors;
  - `f=0` and `f=1` die by additive `R24/R23` charge;
  - `f=2` reduces to two exact `R22` equality skeletons `(1,8)` and `(8,1)`, both eliminated analytically.
- `c=4`, `(10,9,9)`:
  - classified by `s=0,1,2` occupied focus slots;
  - `s=0,1` die by additive charge;
  - all `s=2` ownership patterns but one cost at least nine;
  - the remaining two-U branch reduces to the same `(1,8)/(8,1)` skeletons, each producing an independent 4-set.
- Added `R12_UNIFIED_CLOSURE.md` as the standalone Level-4 proof asset.

## Current milestone

> **Exact Three-Anchor Excess Theorem is `PROVED_ANALYTIC` for every `r>=12`.**

This is now the requested **Level-4 completion**. The theorem no longer depends on the parent project's historical `r=12` closure.

No computation-certified theorem claim is used. Small integer checks were used only to discover equality patterns; all promoted claims are written as analytic threshold/equality arguments.

## Next target

No theorem gap remains in this workstream. The highest-value next action is an independent proof audit of `R12_UNIFIED_CLOSURE.md` and the existing `r>=13` rectangle/focus proof, with special attention to charge additivity and focus-collision hypotheses, before upstream consumers promote the theorem as a dependency.
