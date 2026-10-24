# Progress log

## 2026-10-24 — initialization

- Created isolated branch `workstream/general-r-three-anchor-20261024` from `workstream/general-r-architecture-20261024`.
- Reverified the anchor-incidence partition symbolically: `c+t=4`, `d_1+d_2+d_3=c-2`, four block patterns only.
- Derived the exact connector-miss identity `q_i=d_j+d_k`, fixing the connector type multiset for every pattern.
- Complement formulation initially gave an analytic large-r theorem via Andrasfai–Erdos–Sos.

## 2026-10-24 — parity collapse

- Observed that `K_r=2e-r(3r-1)` is always even.
- Therefore the contradiction branch is `K<=6`, not `K<=7`.
- This removed the entire apparent `K=7` equality layer.

## 2026-10-24 — rectangle/focus machinery

- Proved the exact anchor partition and pair-connector rectangle lemma.
- Converted rectangle obligations into excess charges using baseline external capacities `2+d_i`.
- Proved charge additivity for rectangles with disjoint opposite blocks.
- Proved the common-nonneighbour clique lemma.
- Proved same-missing-anchor disjointness for nonadjacent pair connectors.

## 2026-10-24 — first parameterized closure

- Closed `c=2` for every `r>=12` using a degree-two tripartite transversal-cover argument.
- Closed `c=3` for every `r>=13`.
- Closed both `c=4` geometries first for large `r`, then analytically compressed the boundary to every `r>=13`.
- This produced a Level-3 theorem when composed with the parent project's existing `r=12` closure.

## 2026-10-24 — Level-4 r=12 absorption

- Reopened only the proof-engineering residue at `r=12`; no historical fixed-r case table was imported.
- `c=3`, `(10,10,9)`: mixed focus reduces to effective `R22`; every low-budget layer has a saturated rectangle vertex, forcing an impossible complete/almost-complete cover of the opposite 10-block.
- `c=4`, `(10,10,8)`: classified by `f=0,1,2` focused connectors. `f=0,1` die by additive charge; `f=2` reduces to the two exact `(1,8)/(8,1)` equality skeletons, both eliminated analytically.
- `c=4`, `(10,9,9)`: classified by `s=0,1,2` occupied focus slots. All but one ownership pattern die by additive charge; the final two-U overlap reduces to the same `(1,8)/(8,1)` skeletons and is eliminated by independent-4 forcing.
- Added `R12_UNIFIED_CLOSURE.md`.

## 2026-10-24 — unified short-proof audit

- Re-audited the full theorem instead of stopping at Level 4.
- Replaced the old `r=13..16` c=4 boundary stack by a uniform focus-count proof:
  - `(0,0,2)` is handled by `f=0,1,2` focused connectors for all `r>=12`;
  - `(0,1,1)` is handled by `s=0,1,2` occupied focus slots for all `r>=12`;
  - for `r>=13`, the only overlap branch dies from the single inequality `K>=r-6+max(k1,k2)>=7`;
  - `r=12` leaves only `(1,8)/(8,1)` equality skeletons.
- Strengthened the `c=2` proof. If an exact-nonneighbour part `E_i` were empty, let `m` be the number of positive-excess nonneighbours in that block and `S` their total excess. Self-consistency of the two remaining exact-nonneighbour blocks gives

  `S >= m(S+3-m)`,

  while `S>=m`, so the right side exceeds `S` by at least `2m`. Contradiction.
- With all three `E_i` nonempty, the degree-two tripartite cover lemma and the global lower bound `sum|E_i|>=2r-9` close `c=2` cleanly.
- Added `UNIFIED_SHORT_PROOF.md` as the canonical 2–6-page-style analytic proof.

## Current milestone

> **Exact Three-Anchor Excess Theorem is `PROVED_ANALYTIC` for every `r>=12`.**

The preferred proof is now `UNIFIED_SHORT_PROOF.md`. It does not rely on computation-certified steps, the historical fixed-`r=12` case closure, or separate `r=13..16` case tables.

## Next target

No theorem gap remains in this workstream. The highest-value action is external/independent proof review before the theorem is promoted upstream as a hard dependency for the general-r backend.
