# Canonical State — Exact Three-Anchor Excess workstream

Branch: `workstream/general-r-three-anchor-20261024`

## Contract
Assume `r>=12`, `|V(H)|=3r-1`, `alpha(H)<=3`, `omega(H)<=r-1`, `delta(H)>=r`, and three pairwise nonadjacent degree-`r` anchors `a1,a2,a3`. Define

`K_r(H)=sum_v(d_H(v)-r)=2e(H)-r(3r-1)`.

## Current verdict

**EXACT THREE-ANCHOR EXCESS THEOREM: `PROVED_ANALYTIC` for every `r>=12`.**

This is now a **Level-4 completion**: the proof no longer cites the historical fixed-`r=12` closure. The same anchor-partition / focus / rectangle language closes `r=12` directly; see `R12_UNIFIED_CLOSURE.md`.

## Core reductions

1. `K_r` is always even. Hence a counterexample to `K_r>=8` has `K_r<=6`.
2. Every non-anchor meets at least one anchor.
3. With exclusive blocks `Xi`, connector count `c`, triple-connector count `t`, and deficits `d_i=(r-2)-|Xi|`:
   - `c+t=4`;
   - `d_1+d_2+d_3=c-2`;
   - only `(0,0,0)`, `(0,0,1)`, `(0,0,2)`, `(0,1,1)` occur.
4. If `q_i` is the number of connectors missing `ai`, then `q_i=d_j+d_k`. Thus connector incidence types are completely fixed by the deficit vector.
5. A pair connector missing anchor `ak` forces a complete bipartite rectangle between its nonneighbour sets in the two incident exclusive blocks.
6. Two nonadjacent connectors have a common-nonneighbour set which is a clique.
7. Two nonadjacent pair connectors missing the same anchor have disjoint nonneighbour supports in both incident exclusive blocks.
8. Focus means completeness to an incident near-maximal exclusive block. Focused neighbours consume baseline external slots on that block, strengthening `R24 -> R23 -> R22` or `R33 -> R23 -> R22` rectangle charges.

## Closed geometries

### c=2 / deficits (0,0,0)
Two triple connectors, block sizes `(r-2,r-2,r-2)`.

**Closed for all `r>=12`** by the degree-2 tripartite transversal-cover lemma.

### c=3 / deficits (0,0,1)
One triple connector, two pair connectors, block sizes `(r-2,r-2,r-3)`.

**Closed for all `r>=12`.** For `r>=13` the mixed-focus rectangle charge closes symbolically. At `r=12`, both-nonfocus and both-focus branches are impossible; the unique mixed-focus low-budget layers force a saturated rectangle vertex, which in turn forces either the triple connector or the focused connector to see essentially/all of the opposite 10-clique, producing a 12-clique or an impossible degree count.

### c=4 / deficits (0,0,2)
Four pair connectors, block sizes `(r-2,r-2,r-4)`.

**Closed for all `r>=12`.** For `r>=13` this is the existing focus/nonfocus closure. At `r=12`, let `f` be the number of connectors focused on the short block. The focus cap gives `f<=2`.

- `f=0`: additive `R24` charges exceed six; the only putative double-adjacency equality would require excess 3 on all four connectors.
- `f=1`: effective `R23` charges on the three nonfocused connectors exceed six.
- `f=2`: effective `R22` leaves only two equality skeletons, `(a,b)=(1,8)` or `(8,1)`, with all six excess units on one exclusive vertex. Each skeleton creates an independent 4-set or an oversized common-nonneighbour clique.

### c=4 / deficits (0,1,1)
Four pair connectors, block sizes `(r-2,r-3,r-3)`.

**Closed for all `r>=12`.** No two connectors may focus on the same deficit-1 block. At `r=12`, classify by the number `s` of occupied focus slots among the two deficit-1 blocks:

- `s=0`: the two `(0,1)` connector rectangles already add to at least 8;
- `s=1`: an additive `R23/R22` pair costs at least 7;
- `s=2`: every ownership pattern except `V` focusing one block and `W` the other costs at least 9; the remaining two-U overlap branch reduces to the same `(1,8)/(8,1)` equality skeletons and is eliminated by an independent 4-set.

## Independent complement check
Let `J=bar H`. Then `J` is `K4`-free and

`d_J(v)=2r-2-(d_H(v)-r)`.

Under a counterexample `K<=6`, `delta(J)>=2r-8`. Classical Andrasfai–Erdos–Sos gives an independent coarse proof for sufficiently large `r`; the focus/rectangle proof is strictly stronger and reaches the full range `r>=12`.

## Main files

- `THEOREM.md`: theorem statement and branch-by-branch closure.
- `PROOF_ATTEMPTS.md`: parameterized proof for `r>=13` and core lemmas.
- `R12_UNIFIED_CLOSURE.md`: direct analytic absorption of `r=12` into the same proof language.
- `EQUALITY_CASES.md`: low-budget equality layers and their elimination.
- `COUNTEREXAMPLE_SEARCH.md`: falsification status and relaxed-candidate notes.
- `PROGRESS_LOG.md`: chronological research record.
