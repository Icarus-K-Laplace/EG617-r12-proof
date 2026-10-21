# EG617 r=12 proof reconstruction

> **STATUS: NOT_CERTIFIED**
>
> This repository tracks the clean-room reconstruction of the `r=12` case of Erdős Problem 617. The full theorem has **not** been proved yet.

This repository stores mathematical results, proof dependencies, certificates, and current frontiers. Working prompts for external agents are intentionally kept outside the repository.

## Current research program

- **Front-end:** eliminate the unique embedded T61 obstruction or extract a legal induced `R(4,49)`.
- **Low backend:** eliminate E332, now reduced to an extreme-degree q30 shell over a 211-edge 35-core.
- **High backend:** eliminate `333 <= e(F) <= 340` for legal `R(4,49)` residuals, preferably by a uniform stability theorem.

## Front-end master reduction

**PROVED dichotomy:**

`least-edge colour G -> legitimate induced R(4,49) OR embedded T61`.

The V1 contextual recurrence is **COMPUTATION_CERTIFIED** with 1752 nodes and 144 outer comparisons, replayed by two independent integer implementations.

Inside T61 we have proved:

- `alpha(R)=5` exactly under contextual no-extraction;
- anchor defect `z=0`, hence the anchor closed neighbourhood is a genuine K12;
- simplified outer ledger `E+sigma+g+x6+y6=408`;
- generic `R(4,48)` floor `>=310`;
- the entire T61 minimum-degree12 branch is empty;
- E397, E398, E399 and E400 in the h13 branch are empty.

Thus the current front-end terminal is

`T61: delta=13, 401<=E<=408`.

The next exact cells occur at q26 for E401:

`(26,25,1), (26,24,2), (26,23,3), (26,22,4)`

plus the q25 extension `(25,21,4)`.

## Backend state

Core assets:

- exact degree-13 pivot bookkeeping and shell charge identities;
- `CORE211`: `H in R(3,35) => e(H)>=211`;
- q28 profitable repivot;
- generic q29 good-repivot, which does **not** require `e(H)=211`;
- E329, E330 and E331 closed.

For E332, any survivor has

`q=30, e(H)=211`.

The equality analysis has now proved:

- undecorated shell missing degrees 4 through 9 are profitable and impossible;
- the full d10 equality branch is empty;
- the full d3 equality branch is empty;
- every remaining undecorated shell missing degree lies in `{0,1,2,11,12}`;
- there are at most two undecorated degree11/12 shell vertices;
- total shell decoration satisfies `G in {4,5,6,7,8}`;
- when `G=4`, the support counts are exactly `(h,k,l)=(2,4,7)`.

So the active E332 object is now an extreme-degree q30 shell, not the old d3/d10 row system.

## Machine-readable research state

For programmatic use and other research agents:

- `machine/CANONICAL_STATE.json`
- `machine/THEOREM_REGISTRY.json`
- `machine/OPEN_FRONTIERS.json`

These files contain only research results/status, exact frontier constraints, and source-file references.

## Main blockers

1. eliminate T61 h13, currently E401–E408;
2. eliminate the remaining E332 extreme-degree q30 shell;
3. eliminate E333–E340 with a uniform high-layer theorem.

Historical `CLOSED`/`UNSAT` labels are never accepted without exact assumptions and proof provenance.

Start with `RESEARCH_INDEX.md`, then `CANONICAL_STATE.md`, `PROOF_DAG.md`, `ASSET_LEDGER.md`, `OPEN_FRONTIERS.md`, or the machine-readable JSON files above.
