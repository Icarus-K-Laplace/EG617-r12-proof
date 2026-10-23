# Open frontiers

## Front-end — T61 h13

The continuous closed interval is `E397..E406 = EMPTY`.

Reviewed V9/V10 results remain relative to their explicit retained lower-order seed contract.

### E407

- `Q=27`: CLOSED;
- `Q=31`: OPEN candidate coverage/completion;
- `Q=32`: OPEN.

At Q31 no maximizing pivot has a regular d3 or d10 neighbour; hypothetical regular missing degrees lie in `{0,1,2,11,12}`.

### E408

- `Q=27,28`: CLOSED;
- `Q=31,32,33`: OPEN.

The exact correction-cycle identity is `sum(h+kappa)=sum(eta+m)`; it does not imply individual zero defects.

## High backend

### E333

`E333 = EMPTY` under the retained legal-backend/V4 forcing contract.

### E334..E337 — Astra B line

These remain OPEN. V6 proves repeated-pair capacity through core213 (`K<=6`) and removes the former CORE212 matching residual. Remaining work is far/d3 forcing, double-hub `r>=2`, allowance3, and the higher-`K` concentration / overlap-10 K11 equality mechanisms.

### E338..E340 — assistant right edge

Global right-edge facts:

- `q36 => G>=3`;
- `q37 => G>=2`;
- `q38 => G>=3`;
- every q38,G=2 shell is empty;
- q36 regular d4/d9 ceiling exchanges are empty;
- the complete K4,9 top-channel plateau family is empty.

For q36, candidate coverage splits into low-clique and shell-poor regimes. The f=3 low-clique layer is CLOSED, so `f<=2`.

#### q36 f=2 — far 2K1, a_F=0

This entire branch is now CLOSED.

`backend/Q36_F2_2K1_A0_STAR_TERMINALS_FULL_CLOSURE.md` closes the last three c=2/c=1 missing-star equality terminals by combining row closure with the E338 total degree-excess budget39. Together with the previous c>=3, c=2-distinct and low-c closures:

> `2K1, a_F=0` is EMPTY.

#### q36 f=2 — far 2K1, a_F=1

`backend/Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md` gives

`A+G_Y=6-e_M(Y)`, `A>=2`,

and

`lambda(T)+e(Y,T)+e_H(T)<=14+e_M(Y)`.

Current exact layer status:

- `c=7`: CLOSED. A=2 and A=3 are both EMPTY; the final A=3 all-singleton support system is closed by `Q36_F2_2K1_A1_C7_A3_ALL_SINGLETON_FULL_CLOSURE.md`.
- `c=8`: A=2 and A=3 are CLOSED. Only A=4 remains OPEN. `Q36_F2_2K1_A1_C8_A4_MULTIPLICITY_REDUCTION.md` proves multiplicity4 impossible and any multiplicity-three support must be a target K3 satisfying `O_D+e(Y,D)<=2`, hence forcing at least three external owner incidences into supports disjoint from D.
- `c=9`: A=2 and A=3 are CLOSED. A=4 and A=5 remain OPEN. `Q36_F2_2K1_A1_C9_A4_MULTIPLICITY_REDUCTION.md` proves multiplicity4 impossible and any multiplicity-three support must be a target K3 satisfying `O_D+e(y,D)<=2`, forcing at least four external owner incidences into disjoint supports.
- `c=10`: exact A=6 remains OPEN.

Thus the former high-c support problem has advanced to the first genuine slack-three geometry: repeated K3 supports coexisting with a forced disjoint-support family.

#### q36 f=2 — far target K2

This topology remains OPEN:

- at most3 d2 rows, with distinct disjoint pure K2 supports;
- d3 rows use at most two decorated missing-set classes;
- in the no-d2/two-class sector, total allowance<=1.

#### shell-poor interface

At least five one-spoke pivots carry 22-point anti-neighbourhoods Z with

`110<=e_H(Z)<=122`, `alpha(H[Z])<=2`,

and exact charge

`q_v=133-e_H(Z)+g_a+e(D,A\{a})`.

A simultaneous near-Mantel stability/compatibility theorem remains OPEN.

No full E338 layer is yet claimed closed.

## Closed backend interval

`E329,E330,E331,E332,E333` are empty under their stated contracts.

## Current global obligations

1. T61 E407: close Q31/Q32;
2. T61 E408: close Q31/Q32/Q33;
3. eliminate legal backend layers E334..E340.

The full EG617 r=12 theorem remains **OPEN / NOT_CERTIFIED**.