# Canonical state — 2026-10-22

## The theorem is not certified

Target: prove the `r=12` case of Erdős Problem 617. Current status: **NOT_CERTIFIED**.

## Backend

For every legitimate residual `F in R(4,49)`, a degree-13 pivot gives

`e(F)=91+q+e(H)`, with `H in R(3,35)` and clean core floor `e(H)>=211`.

### Closed low backend

`E329,E330,E331,E332` are empty. E332 is complete and frozen. The legal `R(4,49)` backend obligation is exactly

`E333..E340`.

Preferred E332 proof asset:

`backend/E332_FULL_CLOSURE.md`.

## Front-end master reduction

The certified dichotomy is

`least-edge K145 counterexample -> induced legal R(4,49) OR embedded T61`.

The contextual recurrence is computation-certified at 1752 nodes and 144 stopping comparisons.

### Continuous canonical h13 closure E397--E406

The repository now contains independent proof bodies closing every T61 h13 layer

`E397,E398,...,E406`.

Earlier V6/V7 package labels for E401--E405 have been independently replayed and are no longer the canonical evidence source.

New canonical replay assets:

- `front_end/E401_E404_CANONICAL_CLOSURE.md`;
- `front_end/E405_FULL_CLOSURE_CANONICAL.md`;
- `front_end/Q30_HEREDITARY_PROMOTION_CANONICAL.md`;
- `front_end/E406_LOW_TO_Q30_BRIDGE.md`;
- `front_end/E406_FULL_CLOSURE.md`.

#### E401--E404

A uniform theorem proves that at any pivot with

`q<=29`, `G<=7`, `delta(C)>=12`, and EDGE13,

there is an undecorated missing-degree3--10 repivot with

`q_y>=30`.

Together with the <=288 core interface, pure q23/q24 shell lemmas and high-low cut accounting, this closes E401--E404 analytically.

#### E405

The canonical E405 replay proves:

- no embedded 36-point alpha<=3 object can occur;
- every actual 47-core has minimum degree at least11;
- q25/q26 promote to q>=27;
- a high-low cut forces maximum charge Q>=27;
- Q=27,28,29 contradicts uniform promotion;
- Q=30 contradicts the independently replayed q30 hereditary promotion theorem.

Hence E405 is empty.

#### E406

S31 gives a pivot with q<=30. The independent low-to-q30 bridge produces a genuine q30 pivot. The canonical q30 theorem reaches q31 within at most two regular repivots, so the final step is an actual q30->q31 edge. Its distance lies in

`{1,2,3,10,11,12}`,

and all six classes are independently empty.

Hence E406 is empty.

### Active T61 frontier: E407--E408 only

V8 source-reported structure remains useful:

- at a maximum-charge pivot `Q=30+k`, `1<=k<=3`, every regular missing-degree-3 neighbour satisfies `rho<=k-1`;
- the boundary `rho=k` is excluded;
- exact excess-migration and reverse-repivot identities are supplied.

V8 explicitly leaves:

- `E407: Q_max=27`;
- `E408: Q_max in {27,28}`;
- correction-term compatibility/cycles.

Those statements are not yet a closure of either layer.

Thus the active T61 edge window is exactly

`E407,E408`.

## High backend live state

Line-B V4 reports a support-repetition reduction to necessary families

`D2-A,D2-B,D2-C,D2-D,R9`

with repetition lower bounds

`8,8,5,7,9`.

These are necessary shell rows only, not realized graphs. `E333..E340` remain OPEN.

## Current independent mathematical obligations

Exactly two remain:

1. close T61 `E407,E408`;
2. eliminate legal `R(4,49)` layers `E333..E340`.

There is no remaining E332, E401--E406, or source-replay obligation for those closed front-end layers.

## Certification warning

EG617 r=12 remains OPEN until both remaining obligations are discharged.
