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

At Q31, V10 proves that no maximizing pivot has a regular shell neighbour of missing degree3 or10. Every regular shell vertex of a hypothetical Q31 maximum therefore has missing degree only

`{0,1,2,11,12}`.

Coverage is still OPEN. The shell-only witness

`M = K2 join (K2 disjoint_union 9K1)`

with decorations4,3 satisfies the current shell necessary conditions but is not a certified T61 completion.

Remaining branches:

- `Q=31` candidate coverage/completion;
- `Q=32` compatibility/coverage.

### E408

Closed maximum-charge branches:

- `Q=27`: impossible;
- `Q=28`: impossible.

Remaining branches:

- `Q=31` candidate coverage/completion;
- `Q=32`;
- `Q=33`.

The exact correction-cycle identity is

`sum(h+kappa)=sum(eta+m)`.

It does not force individual zero defects.

## High backend

### E333

`E333 = EMPTY` under the retained legal-backend and V4 five-family forcing contract.

### E334..E337 — Astra B V6

These remain OPEN.

`backend/HIGH_LAYER_BACKEND_V6_CANONICAL_AUDIT.md` independently replays V6. The verifier passed and every manifest SHA-256 matched.

New proved capacity:

- for `K in {2,4,6}`, repeated-pair `r=1`, allowance<=2 implies `m<=6`;
- the former core212 matching residual is impossible, and the obstruction extends through core213 (`K<=6`);
- the q<=32 short-row no-far branch has exactly two active hubs; one-hub and three-hub branches are empty.

The remaining B-line gaps are:

1. far-neighbour configurations;
2. missing-degree-three rows;
3. double-hub `r>=2`;
4. `r=1` allowance3;
5. for E335--E337 channels with `K>=8`, concentration and the overlap-10 K11 equality mechanism.

### E338..E340 — assistant right edge

Global low-decoration forcing proves

- `q36 => G>=3`;
- `q37 => G>=2`;
- `q38 => G>=3`.

Every q38,G=2 shell is eliminated.

For q36, regular d4/d9 ceiling exchanges are empty. Candidate coverage splits into:

1. a low-clique regime;
2. a shell-poor regime with at least five nonadjacent one-spoke pivots.

The entire `f=3` low-clique layer is CLOSED, so `f<=2`.

#### f=2 exact frontier

`backend/Q36_F2_SHELL_LEDGER_REDUCTION.md` gives the exact shell identity

`G=14-mu-delta+a_F-nu`.

Every low-clique vertex has missing degree2 or3.

For far target K2:

- at most3 d2 rows, with distinct disjoint pure K2 supports;
- d3 rows use at most two decorated missing-set classes;
- in the no-d2/two-class branch, total common-S allowance is at most1.

For far `2K1` with exactly one far-decoration incidence:

- `c=4,5,6` are EMPTY;
- the branch now starts at `c>=7`.

For far `2K1` with no far-decoration incidence:

- the two far 12-supports are disjoint and leave an 11-point remainder `R` with `alpha(H[R])<=2`;
- d2 rows have at most two distinct support classes;
- a repeated d2 class is the unique d2 class and is a zero-defect pure K2 repivoting to q35;
- for `n2>=3`, all d2 rows share that K2 and satisfy `3n2<=c+nu+2`, `2n2<=c+4`;
- the all-d2 subbranch has `c<=4`;
- d3 rows use at most two decorated missing-set classes;
- allowance-zero d3 class size<=2;
- allowance-one d3 classes have at most two distinct supports; if repeated, the repeated support is the unique pure q35 K3 class;
- allowance-two d3 class size<=6;
- the all-d3 / two-missing-class sector has `c<=6`.

The high-c all-d3 single-class sector is now completely CLOSED:

- `c=7`: EMPTY;
- `c=8`: EMPTY;
- `c=9`: EMPTY by `backend/Q36_F2_2K1_A0_C9_FULL_CLOSURE.md`;
- `c=10`: EMPTY by `backend/Q36_F2_2K1_A0_C10_FULL_CLOSURE.md`.

Moreover `backend/Q36_F2_2K1_A0_C10_MIXED_FULL_CLOSURE.md` closes every c=10 state containing at least one d2 row. Therefore the entire

`2K1, a_F=0, c=10`

layer is EMPTY.

The remaining `2K1,a_F=0` work is confined to mixed d2/d3 states with `c<=9`.

The remaining f=2 work is therefore concentrated in:

1. `2K1,a_F=1,c>=7`;
2. `2K1,a_F=0` mixed d2/d3 states with `c<=9`, beginning with c=9;
3. the far-target-K2 topology.

#### shell-poor interface

At least five one-spoke pivots carry 22-point anti-neighbourhoods Z with

`110<=e_H(Z)<=122`, `alpha(H[Z])<=2`,

and exact charge

`q_v=133-e_H(Z)+g_a+e(D,A\{a})`.

A simultaneous near-Mantel stability/compatibility theorem remains OPEN.

No full E338--E340 layer is yet closed.

## Closed backend interval

`E329,E330,E331,E332,E333` are empty under their stated proof contracts.

## Current global obligations

1. T61 E407: close Q31/Q32;
2. T61 E408: close Q31/Q32/Q33;
3. eliminate legal `R(4,49)` layers E334..E340.

The full EG617 r=12 theorem remains **OPEN / NOT_CERTIFIED**.