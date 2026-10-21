# EG617 r=12 proof reconstruction

> **STATUS: NOT_CERTIFIED**
>
> This repository tracks the clean-room reconstruction of the `r=12` case of Erdős Problem 617. The full theorem has **not** been proved yet.

## Current three-line program

- **Line A — Astra A:** eliminate the unique embedded T61 obstruction or extract a legal induced `R(4,49)`.
- **Line B — Astra B:** eliminate `333 <= e(F) <= 340` for legal `R(4,49)` residuals.
- **Line C — central line:** eliminate `E332`, reduced to `q=30` over a 211-edge 35-core.

## Front-end canonical state

**PROVED dichotomy:**

`least-edge colour G -> legitimate induced R(4,49) OR embedded T61`.

The V1 contextual recurrence is **COMPUTATION_CERTIFIED** with 1752 nodes and 144 outer comparisons, replayed by two independent integer implementations.

Inside T61 the current analytic state is:

- `alpha(R)=5` under contextual no extraction;
- anchor defect `z=0`, so the anchor closed neighbourhood is a genuine target K12;
- seven genuine K12 blocks exist in total;
- exact outer ledger `E+sigma+g+x6+y6=408`;
- generic `R(4,48)` floor strengthened to `e>=310`;
- the entire T61 minimum-degree12 branch is empty;
- E397, E398 and E399 are empty;
- therefore the surviving front-end window is

`T61: delta(R)=13, 400<=E<=408`.

The next exact layer is E400. Writing `E=397+s`, every degree13 pivot sees at most `s` units of neighbour excess. At E400 (`s=3`), any pivot seeing total excess3 falls into the exact q25 cell

`q=25, z=22, e(C47)=284`.

The current Line A target is a q25 shell theorem for decoration partitions `3`, `2+1`, and `1+1+1`.

Relevant proofs:

- `front_end/R448_FLOOR310.md`
- `front_end/T61_H12_CLOSURE.md`
- `front_end/E398_Q23_SHELL.md`
- `front_end/E399_Q24_SHELL.md`
- `front_end/T61_H13_LOW_LAYER.md`

## Backend assets

- Exact degree-13 pivot bookkeeping and shell charge identities.
- `CORE211`: `H in R(3,35) => e(H)>=211`.
- q28 profitable repivot.
- Generic q29 good-repivot: q29 + inherited `delta(H)>=12` gives a degree-13 pivot with `q_y>=30`; this does **not** require `e(H)=211`.
- E329, E330, E331 closed in the reconstructed DAG.
- E332 reduces to `(q,e(H))=(30,211)`.
- Equality CORE211 degree multisets: `14,12^34` or `13^2,12^33`.

## Main blockers

1. **Line A:** close T61 E400–E408, preferably via a parameterized q=22+r shell-stability theorem.
2. **Line C:** eliminate E332 q30+211.
3. **Line B:** eliminate E333–E340 with a uniform stability theorem.

Historical CLOSED/UNSAT labels are never accepted without exact assumptions and proof provenance.

Start with `RESEARCH_INDEX.md`, then `CANONICAL_STATE.md`, `PROOF_DAG.md`, `ASSET_LEDGER.md`, and `OPEN_FRONTIERS.md`.
