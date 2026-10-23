# Live research state — 2026-10-23

This is the synchronized human-readable live state. It contains research results only, not agent prompts.

## Front end — T61

Canonical closure remains `E397..E406 = EMPTY`.

Reviewed V9/V10 state under retained lower-order seeds:

- E407: Q27 CLOSED; Q31/Q32 OPEN;
- E408: Q27/Q28 CLOSED; Q31/Q32/Q33 OPEN;
- maximizing Q31 has no regular d3/d10 neighbours;
- Q31 candidate coverage/completion remains the bottleneck.

## High backend

### E333

`E333 = EMPTY` under the retained legal-backend/V4 forcing contract.

### Astra-B E334..E337

V6 is independently replayed. Repeated-pair `r=1`, allowance<=2 and `K in {2,4,6}` implies multiplicity<=6, and the CORE212 matching residual is empty through core213. E334..E337 remain OPEN on far/d3, double-hub, allowance3 and higher-K mechanisms.

### Assistant-owned E338..E340

The K4,9 top-channel plateau family is empty. Low-decoration forcing gives q36=>G>=3, q37=>G>=2, q38=>G>=3; all q38,G=2 states are empty. q36 d4/d9 ceiling exchanges are empty.

q36 coverage splits into low-clique and shell-poor regimes. f=3 low-clique is CLOSED; hence f<=2.

#### q36 f=2, far 2K1, a_F=0

This branch is reduced to exactly three equality terminals. All c>=3 states are EMPTY and c=2 distinct-support is EMPTY. No d3 row survives.

Remaining:

1. c=2 repeated support: `M[X]=K1,4 + 4K1`, all X decorations1, shared pure K2 support D, both D endpoints adjacent exactly to the star centre, q35 repivot D14-saturated.
2. c=1,nu=2: `M[X]=K1,2 + 7K1`, both support endpoints adjacent exactly to the centre.
3. c=1,nu=3: `M[X]=K1,3 + 6K1`, both support endpoints adjacent to the centre and at most one extra D--X edge.

#### q36 f=2, far 2K1, a_F=1

`Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md` gives `A+G_Y=6-e_M(Y)`, `A>=2`, and the K11-minus-defects D14 incidence cap.

For c=7:

- A=2 is CLOSED;
- A=3 is the only remaining allowance;
- Y is a target K3 with decorations `(1,1,1)`;
- `{p} union C union Y=K11`;
- seven common-S 3-support rows lie in a 12-point alpha-two remainder.

The A=3 multiplicity analysis now proves:

- multiplicity4 impossible;
- partition `3+3+1` EMPTY;
- partition `3+2+2` EMPTY;
- partition `3+2+1+1` EMPTY;
- partition `3+1+1+1+1` EMPTY.

Hence every surviving support class has multiplicity at most2. Remaining partitions:

- `2+2+2+1`;
- `2+2+1+1+1`;
- `2+1+1+1+1+1`;
- seven singleton supports.

Any historical multiplicity-three one-edge intermediate generates the exact q35 equality shell `G'=13`, `z'=22` with target K10 base and regular missing-degree pattern `3,0,0,2,2,2,2`.

For c=8,9,10 the high-c normal form leaves finite allowance ranges; c=10 has exact A=6.

#### q36 f=2, far target K2

At most3 d2 rows exist, with distinct disjoint pure K2 supports. d3 rows use at most two decorated missing classes; no-d2/two-class total allowance is at most1.

#### shell-poor

At least five one-spoke pivots carry 22-point anti-neighbourhoods Z with `110<=e_H(Z)<=122`, `alpha(H[Z])<=2`, and exact charge `q_v=133-e_H(Z)+g_a+e(D,A\{a})`. A simultaneous near-Mantel stability theorem remains OPEN.

## Global state

Closed backend interval: `E329..E333`.

Remaining obligations:

- T61 E407/E408 high-Q coverage;
- backend E334..E340, with q36 right-edge sectors sharply reduced.

The full EG617 r=12 theorem remains **OPEN / NOT_CERTIFIED**.