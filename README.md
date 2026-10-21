# EG617 r=12 proof reconstruction

> **STATUS: NOT_CERTIFIED**
>
> This repository tracks the clean-room reconstruction of the `r = 12` case of Erdős Problem 617. The full theorem has **not** been proved yet.

## Current canonical state (2026-10-21)

The project is split into three independent research lines:

- **Line A — front-end / Astra A:** exclude the unique embedded T61 obstruction or extract a legitimate induced `R(4,49)` from it.
- **Line B — high-layer backend / Astra B:** eliminate `333 <= e(F) <= 340` for legitimate `F in R(4,49)`.
- **Line C — central line:** eliminate the current lowest surviving backend layer `E332`, reduced to `q=30` over a 211-edge 35-core.

## Front-end breakthrough

The broad `K145 -> R(4,49)` bridge has been reduced to a single outer stop.

**PROVED dichotomy:**

`least-edge colour G -> legitimate induced R(4,49) OR embedded T61`.

T61 is exactly the stop

`(d,j,a,n)=(11,6,5,61)`

with six genuine K12 blocks, `397<=E<=408`, `delta in {12,13}`, `alpha<=5`, `omega<=11`, inherited density caps, and the exact ledger

`E+sigma+z+g+x_6+y_6=408`.

The contextual recurrence is **COMPUTATION_CERTIFIED**: 1752 nodes and 144 outer comparisons were replayed by two independent integer implementations. The uploaded package manifest was independently checked with 73/73 files matching.

## Backend assets

- Exact degree-13 pivot bookkeeping and shell charge identities.
- `CORE211`: `H in R(3,35) => e(H)>=211`.
- Analytic `q=28` profitable-repivot mechanism.
- Analytic **generic q29 good-repivot lemma**: under q29 and inherited `delta(H)>=12`, there is a new degree-13 pivot `y` with `q_y>=30`. This does **not** require `e(H)=211`.
- Backend layers through `E331` closed modulo the audited uniform-q27 theorem.
- `E332` reduces to `q=30, e(H)=211`.
- Equality 211-core degree multisets are `14,12^34` or `13^2,12^33`.

## Front-end local assets

- Matching-transversal rigidity and equality rotation close the seven/eight-block high-cross branches.
- Eight genuine K12 blocks produce a legitimate `R(4,49)`.
- S31 strict descent is valid only under its explicit 61-point, 406-edge, minimum-degree13 parent contract.
- T61 is not automatically in that parent class.
- For the specified S30 `(5,7,8,8)` row-labelled branch, the singleton-triangle case is closed; new saturation lemmas leave 14 k0 and 13 k1 scalar necessary cases. These are not graph survivors or a complete profile classification.

## Main blockers

1. **Line A:** exclude embedded T61 or extract a legitimate induced `R(4,49)`.
2. **Line C:** eliminate `E332:q30+211`.
3. **Line B:** eliminate `E333...E340`, preferably with a uniform stability theorem.

Historical `CLOSED` labels are never accepted without reconstruction of hypotheses and proof provenance.

See `CANONICAL_STATE.md`, `PROOF_DAG.md`, `ASSET_LEDGER.md`, `OPEN_FRONTIERS.md`, `TEAM_SPLIT.md`, `STATUS_POLICY.md`, `front_end/FRONTEND_BRIDGE_THEOREM.md`, and `certificates/frontend_line_a_v1/`.
