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


## Emergency r=12 sprint overlay — 2026-10-25

This overlay supersedes older frontier descriptions above where they conflict. The theorem remains **OPEN / NOT_CERTIFIED**.

### Front end

- E397–E406 are closed under their recorded contracts.
- E407 Q32: V12's finite kernel/shell certificate has been independently replayed. The fresh archive hash is 0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36; all 28 manifest entries passed. The verifier reproduced 8,677 weight vectors, 17,957 count states, 1,984 labelled necessary shells, and 554 OPEN shell states after the three recorded screens. This certifies finite coverage only, not a completed parent graph.
- The 554 states reduce to five rho=0 templates sharing a regular K11 against one 284-edge core. A new exact-129 color-factor argument now gives a witness-packing consequence for all five templates: A/B have at least 28 hub-complete independent 4-sets; C/D and E with a full row have at least 35; E without a full row has at least 42 sets hitting both P3 endpoints. All families are pairwise linear and satisfy Hall-perfect-matching constraints. This does not yet contradict the core degree/edge budget. Full proof: r12_master/workstreams/ultimate-closure-chat-20261024/R12_E407_Q32_COLOR_FACTOR_CROSSCUT.md.
- E408 Q32 and Q33 remain OPEN. The E407 Q32 certificate cannot be transferred to the 285-edge Q32 core without a separate threshold certificate; Q33's seven-block near-Latin system still lacks a global contradiction.

### Backend

E335–E340 remain open. In the E335 three-anchor branch, the retained state is q=30, e(H)=214, K=8, with equality/connector cases not all discharged. No backend result is silently used to close E407.

### Dependencies and certification

The new A/C theorem depends on the retained E407 shell-row contract and Kang–Pikhurko's exact-129 Type-I classification. The V12 replay verifies the finite certificate only; analytic screen rules retain their explicit lower-order hypotheses. No residual-core, three-anchor, or repivot theorem from sibling workstreams is used in the new A/C argument.
