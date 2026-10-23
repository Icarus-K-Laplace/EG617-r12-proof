# Open frontiers

## Front-end — T61 h13

The continuous closed interval is

`E397..E406 = EMPTY`.

The reviewed V9/V10 assets are recorded in

- `front_end/T61_H13_V9_CANONICAL_AUDIT.md`;
- `front_end/T61_H13_V10_CANONICAL_AUDIT.md`.

All statements remain relative to their explicit retained lower-order seed contract.

### E407

Closed maximum-charge branch:

- `Q=27`: impossible.

At Q31, V10 proves that no maximizing pivot has a regular shell neighbour of missing degree3 or10. Therefore every regular shell vertex of a hypothetical Q31 maximum has missing degree only

`{0,1,2,11,12}`.

Coverage is still OPEN: the shell-only witness

`M = K2 join (K2 disjoint_union 9K1)`

with decorations4,3 satisfies the current shell necessary conditions but has only regular degrees2,12. It is not a certified T61 completion. Its 47-core compatibility is the first concrete completion test.

Remaining exact branches:

- `Q=31` candidate coverage/completion;
- `Q=32` compatibility/coverage.

### E408

Closed maximum-charge branches:

- `Q=27`: impossible;
- `Q=28`: impossible.

Remaining exact branches:

- `Q=31` candidate coverage/completion;
- `Q=32`;
- `Q=33`.

### Correction-cycle warning

The exact closed-walk identity is

`sum(h+kappa)=sum(eta+m)`.

It does not force every correction term to vanish. The old zero-cycle shortcut is RETRACTED.

## High backend

### E333

`E333 = EMPTY` under the retained legal-backend and V4 five-family forcing contract.

### E334..E337 — Astra B

These remain OPEN. The active task is the parameterized V5 repeated-pair capacity extension through larger core excess, starting with the 212-edge-core residual in E334.

### E338..E340 — assistant right edge

The q36--q38 atomic-defect program remains active.

New global low-decoration forcing in `backend/HIGH_RIGHT_EDGE_LOW_DECORATION_FORCING.md` proves

- `q36 => G>=3`;
- `q37 => G>=2`;
- `q38 => G>=3`.

Every q38,G=2 shell is forced to be K4,9 and every decoration placement, including the cross-side one-unit/one-unit state, is eliminated.

For q36, every regular d4/d9 ceiling exchange is already empty via the compensated-K4,9 chain. Hence all adjacent regular positive distances of a remaining q36 survivor lie in

`{1,2,3,10,11,12}`.

`backend/Q36_CANDIDATE_COVERAGE_CLUSTER_REDUCTION.md` splits q36 coverage into:

1. **low-clique regime:** one low target clique plus at most three far/high regular vertices;
2. **shell-poor regime:** at most two adjacent regular pivots, forcing at least five nonadjacent one-spoke legal pivots in CORE211.

The entire maximal far layer `f=3` is now CLOSED. The proof chain is

- `backend/Q36_F3_FAR_LAYER_REDUCTION.md`;
- `backend/Q36_F3_K21_TERMINAL_STRENGTHENING.md`;
- `backend/Q36_F3_K21_SUPPORT_CLASS_COLLAPSE.md`;
- `backend/Q36_F3_FULL_CLOSURE.md`.

Thus the low-clique q36 branch now has

`f<=2`.

The remaining low-clique task is to reduce/eliminate `f=0,1,2`.

The shell-poor branch is governed by `backend/Q36_ONESPOKE_EXACT_FORMULA.md`: at least five one-spoke pivots carry 22-point anti-neighbourhoods Z with

`110<=e_H(Z)<=122`, `alpha(H[Z])<=2`,

and exact charge

`q_v=133-e_H(Z)+g_a+e(D,A\{a})`.

A simultaneous near-Mantel stability/compatibility theorem remains OPEN.

No full E338--E340 edge layer is yet closed.

## Closed backend interval

`E329,E330,E331,E332,E333` are empty under their stated proof contracts.

## Current global obligations

1. T61 E407: close Q31/Q32;
2. T61 E408: close Q31/Q32/Q33;
3. eliminate legal `R(4,49)` layers E334..E340.

The full EG617 r=12 theorem remains **OPEN / NOT_CERTIFIED**.