# T61 H13 V10 canonical audit

Status: `PROVED_RELATIVE_TO_RETAINED_SEEDS` for the Q31 incidence theorem. Full `E407` and `E408` remain `OPEN`.

This file records an independent reading of the uploaded `T61_H13_V10` package. The package preserves the retained lower-order seeds explicitly and does not reuse the retracted zero-cycle shortcut.

## 1. Q31 incidence theorem

Under the retained T61 contract, if the maximum regular-pivot charge is `Q=31`, then no maximizing pivot has a regular shell neighbour of missing degree `3` or `10`.

The proof keeps the full repivot corrections and treats all five non-flat distance-three patterns simultaneously. The key ingredients are:

- a strengthened triangle row-cover lower bound `>=25` for the relevant 47-cores;
- a common regular `K11` block around a hypothetical d=3 maximum edge;
- labelled excess transport on the original core;
- a pointwise capacity argument forcing distinct 3-point rows to be equal or disjoint;
- the exact row-excess formula `Xi_rows = 33 - 3r + t`;
- an independent-six contradiction for the only possible row counts `r=4,5`.

The argument explicitly allows a neighbour of charge30; it does not assume every adjacent view is also a maximum.

Distance ten is reduced to the already-excluded distance-three situation.

Hence at a hypothetical Q31 maximum shell every regular shell vertex has missing degree only in

`{0,1,2,11,12}`.

## 2. Coverage is still open

V10 supplies an explicit shell-only necessary-condition witness

`M = K2 join (K2 disjoint_union 9K1)`

with decorations `4,3` on the inner K2 and zero elsewhere. It has `q=31`, satisfies the checked strengthened shell conditions, and has regular missing degrees only `2,12`.

This object is not asserted to complete to a genuine T61 parent. It proves only that the current shell inequalities do not force a d=3/10 candidate.

For this witness a genuine completion would require a 47-core with

- `e(C)=285` in E407 or `286` in E408;
- `delta(C)>=12`;
- the full T61 alpha/clique/density restrictions;
- labelled shell-core row sizes `12,12,7,6,2,...,2`;
- total shell-core incidence55;
- all repivoted cores valid.

The package records further necessary labelled constraints, including a regular `K10` block from the nine degree-two shell vertices. No realization or impossibility theorem is supplied.

## 3. Q32/Q33 interface

For `Q=30+k`, `k=1,2,3`, a maximizing d=3 exchange satisfies the exact system

- `0<=rho<=k-1`;
- `h+kappa+b = s-ell`;
- `eta+m+b = s`, with `s=k-rho`;
- full labelled excess transport on retained core vertices.

The ten-point block `B=A\S` is target-complete and has at most `rho<=2` decoration. For `k>=2` regular degree1/2 shell vertices can survive the basic EDGE13/TRIANGLE25 checks, so the Q31 equal/disjoint-row argument does not automatically lift.

## 4. Current exact front-end frontier

Relative to the retained seeds:

- `E407`: `Q in {31,32}` remains OPEN;
- `E408`: `Q in {31,32,33}` remains OPEN.

At Q31 the missing implication is now precisely a coverage/completion theorem for shells with regular missing degrees in `{0,1,2,11,12}`.

No full E407/E408 closure is claimed here.