# Canonical State — Exact Three-Anchor Excess workstream

Branch: `workstream/general-r-three-anchor-20261024`

## Contract
Assume `r>=12`, `|V(H)|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`, and three pairwise nonadjacent degree-`r` anchors `a1,a2,a3`. Define

`K_r(H)=sum_v(d_H(v)-r)=2e(H)-r(3r-1)`.

## Current verdict

**GENERAL-R RESULT: `PROVED_SYMBOLIC` for every `r>=13`.**

Together with the pre-existing certified `r=12` closure in the parent project, this is a **Level-3 completion** of the Exact Three-Anchor Excess Conjecture for all `r>=12`.

The remaining research target is only Level 4: absorb `r=12` into the same short parameterized argument instead of citing the historical fixed-r closure.

## Core reductions

1. `K_r` is always even. Hence a counterexample to `K_r>=8` has `K_r<=6`.
2. Every non-anchor meets at least one anchor.
3. With exclusive blocks `Xi`, connector count `c`, triple-connector count `t`, and deficits `d_i=(r-2)-|Xi|`:
   - `c+t=4`;
   - `d_1+d_2+d_3=c-2`;
   - only `(0,0,0)`, `(0,0,1)`, `(0,0,2)`, `(0,1,1)` occur.
4. If `q_i` is the number of connectors missing `ai`, then

   `q_i=d_j+d_k`.

   Thus connector incidence types are completely fixed by the deficit vector.
5. A pair connector missing anchor `ak` forces a complete bipartite rectangle between its nonneighbour sets in the two incident exclusive blocks.
6. Two nonadjacent connectors have a common-nonneighbour set which is a clique.
7. Two nonadjacent pair connectors missing the same anchor have disjoint nonneighbour supports in both incident exclusive blocks.
8. **Focus convention:** a connector is said to focus on `Xi` only when it is adjacent to anchor `ai` and is complete to the corresponding exclusive block `Xi`. Completeness to a third, non-incident block is not counted as focus. All focus-collision arguments use this incident-block convention.

## Closed geometries

### c=2 / deficits (0,0,0)
Two triple connectors, block sizes `(r-2,r-2,r-2)`.

**Closed for all `r>=12`** by the degree-2 tripartite transversal-cover lemma.

### c=3 / deficits (0,0,1)
One triple connector, two pair connectors, block sizes `(r-2,r-2,r-3)`.

**Closed for all `r>=13`** by focus/nonfocus rectangles. The unique `r=13,K=6` arithmetic boundary forces the triple connector to cover an entire `(r-2)` block despite insufficient degree.

### c=4 / deficits (0,0,2)
Four pair connectors, block sizes `(r-2,r-2,r-4)`.

**Closed for all `r>=13`**. At most two connectors can focus on `X3`; therefore at least two are nonfocused. Rectangle charge closes `r>=17`; the boundary `r=13,14,15,16` is eliminated analytically using additivity/disjointness and the fact that focused connectors consume external degree slots on `X3`.

### c=4 / deficits (0,1,1)
Four pair connectors, block sizes `(r-2,r-3,r-3)`.

**Closed for all `r>=13`**. No two connectors can focus on the same incident deficit-1 block: adjacency gives an `r`-clique, while nonadjacency gives a common-nonneighbour clique larger than `r-1`. Thus at least two connectors are nonfocused; local `(3,3)` and `(2,3)` rectangle charges close all `r>=13`, with the small boundary layers handled analytically.

## Independent complement check
Let `J=bar H`. Then `J` is `K4`-free and

`d_J(v)=2r-2-(d_H(v)-r)`.

Under a counterexample `K<=6`, `delta(J)>=2r-8`. Classical Andrasfai–Erdos–Sos therefore gives an independent proof for `r>=60`, since `2r-8>5(3r-1)/8` then forces `J` to be 3-partite, contradicting `alpha(J)<=r-1`.

This route is now only a consistency check; the rectangle/focus proof reaches every `r>=13`.

## Main files

- `THEOREM.md`: theorem statement and branch-by-branch closure.
- `PROOF_ATTEMPTS.md`: detailed analytic proof.
- `EQUALITY_CASES.md`: all low-budget boundary layers and their elimination.
- `COUNTEREXAMPLE_SEARCH.md`: falsification status and relaxed-candidate notes.
- `PROGRESS_LOG.md`: chronological research record.
