# E332 extreme-degree shell reduction

Status: `PROVED` for the reductions below. This is the active Line C object after the d3/d10 closures and the new decoration-layer eliminations.

## Setup

Assume the E332 q30+211 state. The d3 and d10 branches are proved empty, while undecorated degrees4..9 are profitable. Hence every undecorated shell vertex has missing degree only

`0,1,2,11,12`.

Write

- `G=sum g`, so `z=e(M)=30-G`;
- `H` = undecorated high vertices of missing degree11 or12;
- `L` = undecorated low vertices of missing degree0,1,2;
- `D` = decorated vertices;
- `h=|H|`, `k=|D|`, `l=|L|`.

The low set `L` is independent in `M`.

The previously proved support arguments give

`h<=2`.

## Strengthened zero-gap theorem

A new canonical theorem is available in `E332_STRONG_ZERO_GAP_REPIVOT.md`:

for every missing edge `uv` with `u` undecorated,

`|N_M(u) union N_M(v)| + g_v >= 13 + |D_u intersect D_v|`.

Therefore every missing edge between two undecorated vertices satisfies exact zero-gap equality:

`N_M(u) union N_M(v)=A`,

`D_u intersect D_v=empty`.

This is strictly stronger than the historical F-version inequality.

## Decoration layers G=4 and G=5

Both are now `PROVED EMPTY`.

Full proof: `backend/E332_G4_G5_CLOSURE.md`.

The G=4 closure starts from the former exact support count `(h,k,l)=(2,4,7)`, uses a common low neighbour of the two high vertices, forces all lows to have neighbourhood exactly the two highs, and reduces the decorated four-vertex graph to an impossible 3/4-edge pair-weight system.

The G=5 closure is complete across h=0,1,2. It combines:

- edge-capacity on the low/support cut;
- zero-gap forcing of almost-universal high vertices;
- active/inactive decorated-vertex weight bounds;
- exact small support edge counts;
- degree-1/2 low repivot inequalities.

Hence

`G in {6,7,8}`

for every remaining E332 survivor.

## G=6, h=0

The entire branch is `PROVED EMPTY`.

Full proof: `backend/E332_G6_H0_CLOSURE.md`.

The proof considers `k=4,5,6`. In each case low-active decorated vertices have weight at least11, while inactive-inactive edges are heavily restricted by the small decoration budget. Exact edge counts force dense support graphs incompatible with those pair-weight constraints.

## Two-high classification

All `h=2` states are now classified in `backend/E332_H2_CLASSIFICATION.md`.

There are no h=2 states for G=4,5,8. The only possible h=2 cells in the remaining range are:

### H2-G6-K4

- `G=6`;
- two undecorated high vertices with their mutual edge present in M;
- two decorated vertices with total decoration6 and their mutual edge present;
- nine undecorated lows, each with missing neighbourhood exactly the two highs;
- the four support vertices induce `K4` in M.

### H2-G7-K4minusE

- `G=7`;
- two undecorated high vertices with their mutual edge absent in M;
- two decorated vertices with total decoration7 and their mutual edge present;
- nine undecorated lows, each with missing neighbourhood exactly the two highs;
- the four support vertices induce `K4-e`, with the missing support edge between the highs.

## Current Line C frontier

E332 can now survive only in:

1. `G=6,h=1`, or the exact `H2-G6-K4` cell;
2. `G=7,h=0 or1`, or the exact `H2-G7-K4minusE` cell;
3. `G=8,h=0 or1`.

The next attack should first close the two exact h=2 equality cells using their row-union systems, then close `G=6,h=1`, and finally parameterize the same support accounting through G=7,8.
