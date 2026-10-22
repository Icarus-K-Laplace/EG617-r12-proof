# Open frontiers

## Front-end — T61 h13

Latest package-level remaining window:

`T61: E406..E408, delta=13`.

### E406 — boundary-complete, bridge-open

Every possible adjacent q30->q31 final-rise distance class is proved empty:

`d=1,2,3,10,11,12`.

Hence the local coexistence classification is complete. There is no legal adjacent q30--q31 pivot edge.

The **only** remaining E406 obligation is:

> prove independently that every E406 parent satisfying S31 and the hereditary T61 contract must generate an actual adjacent q30--q31 boundary edge.

The V6/V7 source packages report the ingredients for that ladder, but the complete implication has not yet been replayed from a repository proof body. Therefore E406 is currently

`CONDITIONAL_EMPTY_ON_BOUNDARY_FORCING_BRIDGE`.

See `front_end/E406_BOUNDARY_BRIDGE_STATUS.md`.

### E407--E408 — Astra-A line

V8 explicitly leaves:

- `E407: Q_max=27`;
- `E408: Q_max in {27,28}`;
- global compatibility/cycles of nonzero correction terms.

## High backend — E333..E340

This is the only open legal R(4,49) backend interval.

Line-B V4 reports necessary survivor families

`D2-A, D2-B, D2-C, D2-D, R9`

with repetition lower bounds

`8,8,5,7,9`.

These are necessary shell rows, not realized graphs. The next valid target is a repeated-pair/core-support capacity theorem in the 35-point core.

## Closed low backend

`E329,E330,E331,E332` are empty; E332 is frozen.

## Current global open obligations

1. E406 boundary-forcing bridge;
2. E407/E408;
3. legal R(4,49) high layers E333..E340.

The full EG617 r=12 theorem remains **OPEN / NOT_CERTIFIED**.
