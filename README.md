# EG617 r=12 proof reconstruction

> **STATUS: NOT_CERTIFIED**
>
> This repository tracks the clean-room reconstruction of the `r=12` case of Erdős Problem 617. The full theorem has **not** been proved yet.

## Current three-line program

- **Line A — Astra A:** eliminate the unique embedded T61 obstruction or extract a legal induced `R(4,49)`.
- **Line B — Astra B:** eliminate `333 <= e(F) <= 340` for legal `R(4,49)` residuals.
- **Line C — central line:** eliminate `E332`, reduced to `q=30` over a 211-edge 35-core.

## Front-end master reduction

**PROVED dichotomy:**

`least-edge colour G -> legitimate induced R(4,49) OR embedded T61`.

The V1 contextual recurrence is **COMPUTATION_CERTIFIED** with 1752 nodes and 144 outer comparisons, replayed by two independent integer implementations.

Inside T61 we have now proved:

- `alpha(R)=5` exactly under contextual no-extraction;
- anchor defect `z=0`, hence the anchor closed neighbourhood is a genuine K12;
- simplified outer ledger `E+sigma+g+x6+y6=408`;
- generic `R(4,48)` floor `>=310`;
- the entire T61 minimum-degree12 branch is empty;
- E397, E398, E399 and E400 in the h13 branch are empty.

Thus the current front-end terminal is

`T61: delta=13, 401<=E<=408`.

The low-edge shell ladder is now:

- q23 closes E398;
- q24 closes E399;
- uniform q25 closes E400;
- q26 / E401 is the next target, with cells `(26,25,1),(26,24,2),(26,23,3),(26,22,4)` and the q25-G4 extension `(25,21,4)`.

## Backend assets

- Exact degree-13 pivot bookkeeping and shell charge identities.
- `CORE211`: `H in R(3,35) => e(H)>=211`.
- q28 profitable repivot.
- Generic q29 good-repivot: q29 + inherited `delta(H)>=12` gives a degree-13 pivot with `q_y>=30`; this does **not** require `e(H)=211`.
- E329, E330, E331 closed in the reconstructed DAG.
- E332 reduces to `(q,e(H))=(30,211)`.
- Equality CORE211 degree multisets: `14,12^34` or `13^2,12^33`.

## Main blockers

1. **Line A:** close T61 h13, currently E401–E408.
2. **Line C:** eliminate E332 q30+211.
3. **Line B:** eliminate E333–E340 with a uniform stability theorem.

Historical `CLOSED`/`UNSAT` labels are never accepted without exact assumptions and proof provenance.

Start with `RESEARCH_INDEX.md`, then `CANONICAL_STATE.md`, `PROOF_DAG.md`, `ASSET_LEDGER.md`, and `OPEN_FRONTIERS.md`.
