# EG617 r=12 proof reconstruction

> **STATUS: NOT_CERTIFIED**
>
> This repository tracks the clean-room reconstruction of the `r = 12` case of Erdős Problem 617. The full theorem has **not** been proved yet.

## Current canonical state (2026-10-21)

The project is split into three independent research lines:

- **Line A — front-end bridge (Astra A):** derive a legitimate 49-vertex residual from a hypothetical original `K_145` counterexample.
- **Line B — high-layer backend (Astra B):** eliminate `333 <= e(F) <= 340` for `F in R(4,49)`.
- **Line C — central line:** eliminate the current lowest surviving backend layer `E332`, reduced to `q = 30` over a 211-edge 35-core.

Current conservative completion estimate for a complete, auditable proof: **~63%**.

## Certified / high-confidence assets

- Exact degree-13 pivot bookkeeping and shell charge identities.
- `CORE211`: `H in R(3,35) => e(H) >= 211`.
- Analytic `q=28` profitable-repivot mechanism.
- Analytic **generic q29 good-repivot theorem**: under the q29 shell contract and inherited `delta(H)>=12`, there exists a new degree-13 pivot `y` with `q_y>=30`. This existence theorem does **not** require `e(H)=211`; CORE211 enters separately when converting it into the E331 contradiction.
- Backend layers through `E331` closed modulo the audited uniform-`q27` theorem; `E332` reduces to `q=30, e(H)=211`.
- For `e(H)=211`, the only degree multisets are `14,12^34` or `13^2,12^33`.
- S31 strict descent under its explicit 61-point parent contract.
- S30 `(5,7,8,8)` **row-labelled branch** closed only under its explicit singleton-adjacency inputs; the full profile is not globally certified from that result alone.
- Eight-block high-cross branch can be analytically removed once eight genuine target `K_12` blocks exist, giving the residual independence bound `alpha(Y) <= 4`.

## Main blockers

1. **Front-end bridge remains OPEN:** `K_145 -> legitimate 49-point residual` is not yet fully proved.
2. **Backend remains OPEN:** `E332` and higher layers `E333...E340` are not fully eliminated.
3. Historical `CLOSED` labels are never accepted without reconstruction of hypotheses and proof provenance.

See `CANONICAL_STATE.md`, `PROOF_DAG.md`, `ASSET_LEDGER.md`, `OPEN_FRONTIERS.md`, `TEAM_SPLIT.md`, and `STATUS_POLICY.md`.
