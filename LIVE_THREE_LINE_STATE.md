# Live research state — 2026-10-23

This is the synchronized human-readable live state. It contains research results only, not agent prompts.

## Front end — T61

Canonical closure remains `E397..E406 = EMPTY`.

Reviewed V9/V10 state under retained lower-order seeds is superseded at source level by delivered V11:

- V11 package is present, but independent replay in this assistant session is still pending because the local archive executor failed;
- source-reported V11 result: E407 maximum `Q=31` is excluded;
- source-reported V11 result: E408 maximum `Q=31` is excluded;
- retained lower-order seeds remain CONDITIONAL;
- therefore the source-level frontier is:
  - E407: only `Q=32` OPEN;
  - E408: `Q=32,33` OPEN.

See `front_end/T61_H13_V11_SOURCE_AUDIT.md` for the evidence boundary.

## High backend

### E333

`E333 = EMPTY` under the retained legal-backend/V4 forcing contract.

### Astra-B E334..E337

V6 was independently replayed earlier. Repeated-pair `r=1`, allowance<=2 and `K in {2,4,6}` implies multiplicity<=6, and the CORE212 matching residual is empty through core213.

Delivered V7 is present but independent replay in this assistant session is pending because the local archive executor failed. Source-reported V7 gives:

- E334 maximal pivot is forced to `q=32`, `e(H)=211`;
- q30/core213 and q31/core212 channels are excluded;
- allowance<=1 and `W<=30` imply `m<=floor((2r+5)/3)`;
- at K=8, two K11s overlapping in 10 vertices cannot coexist;
- E334 remains OPEN on the d3 eleven-view system, `r=2/allowance=2`, and `r=1/allowance=3`;
- E335..E337 remain OPEN.

See `backend/HIGH_LAYER_BACKEND_V7_SOURCE_AUDIT.md`.

### Assistant-owned E338..E340

The K4,9 top-channel plateau family is empty. Low-decoration forcing gives q36=>G>=3, q37=>G>=2, q38=>G>=3; all q38,G=2 states are empty. q36 d4/d9 ceiling exchanges are empty.

q36 coverage splits into low-clique and shell-poor regimes. f=3 low-clique is CLOSED; hence f<=2.

#### q36 f=2, far 2K1, a_F=0 — CLOSED

`Q36_F2_2K1_A0_STAR_TERMINALS_FULL_CLOSURE.md` closes the last missing-star equality terminals. The entire `2K1,a_F=0` branch is EMPTY.

#### q36 f=2, far 2K1, a_F=1

Current exact status:

- c=7: CLOSED;
- c=8: A=2 and A=3 CLOSED; A=4 OPEN;
- c=9: A=2 and A=3 CLOSED; A=4,A=5 OPEN;
- c=10: exact A=6 OPEN.

#### q36 f=2, far target K2

Global d2 reduction now gives, for c>=3, at most one d2 row. In c=8 with one d2 row:

- all seven d3 owners form one missing-set class;
- A=2 is CLOSED;
- A=3 multiplicity-four and multiplicity-three one-edge terminals are CLOSED;
- the entire multiplicity-three target-K3 sector is now CLOSED by `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_GLOBAL_MASS_CLOSURE.md`, using the exact global mass `sum_H(kappa+e(.,S))=37` versus a forced lower bound 54;
- therefore c=8, one-d2, A=3 now has support multiplicity at most2;
- A=4 remains OPEN.

Two intermediate far-K2 files that used an invalid K4-freeness assumption are explicitly marked RETRACTED; the global-mass closure is independent of that mistake.

#### shell-poor

At least five one-spoke pivots carry 22-point anti-neighbourhoods Z with `110<=e_H(Z)<=122`, `alpha(H[Z])<=2`, and exact charge `q_v=133-e_H(Z)+g_a+e(D,A\{a})`. A simultaneous near-Mantel stability theorem remains OPEN.

## Global state

Closed backend interval: `E329..E333`.

Remaining obligations:

- T61 E407 Q32 and E408 Q32/Q33 at source-reported V11 level;
- backend E334..E340, with E334 source-reported V7 reduced to the unique q32/core211 channel and q36 right-edge sectors sharply reduced.

The full EG617 r=12 theorem remains **OPEN / NOT_CERTIFIED**.