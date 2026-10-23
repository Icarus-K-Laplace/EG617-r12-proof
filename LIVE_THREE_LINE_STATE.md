# Live research state — 2026-10-23

This is the synchronized human-readable live state. It contains research results only, not agent prompts.

## Front end — T61

Canonical closure remains `E397..E406 = EMPTY`.

Reviewed V9/V10 state under retained lower-order seeds:

- E407: Q27 CLOSED; Q31/Q32 OPEN;
- E408: Q27/Q28 CLOSED; Q31/Q32/Q33 OPEN;
- at maximizing Q31, regular d3/d10 neighbours are impossible;
- Q31 coverage/completion remains the front-end bottleneck.

## High backend

### E333

`E333 = EMPTY` under the retained legal-backend/V4 forcing contract.

### Astra-B E334..E337

V6 is independently replayed. Repeated-pair `r=1`, allowance<=2 and `K in {2,4,6}` implies multiplicity<=6, and the CORE212 matching residual is empty through core213. E334..E337 remain OPEN on far/d3, double-hub, allowance3 and higher-K mechanisms.

### Assistant-owned E338..E340

The K4,9 top-channel plateau family is empty. Low-decoration forcing gives

- q36 => G>=3;
- q37 => G>=2;
- q38 => G>=3;

and all q38,G=2 states are empty. q36 d4/d9 ceiling exchanges are empty.

q36 coverage splits into low-clique and shell-poor regimes. f=3 low-clique is CLOSED; hence f<=2.

#### q36 f=2, far 2K1, a_F=0

This branch has undergone a complete large-scale collapse.

Closed layers:

- all c=7,8,9,10 states, including all-d3 and mixed d2/d3;
- c=5,6 by the low-c d3 elimination plus the all-d2 cap;
- c=3,4 by the far-pair independent5 argument;
- c=2 with distinct d2 supports.

No d3 row survives anywhere in this branch.

Only three equality terminals remain:

1. c=2 repeated support:
   `M[X]=K1,4 + 4K1`, all X decorations1, shared pure K2 support D, both D endpoints adjacent exactly to the star centre.
2. c=1, nu=2:
   `M[X]=K1,2 + 7K1`, both support endpoints adjacent exactly to the centre.
3. c=1, nu=3:
   `M[X]=K1,3 + 6K1`, both support endpoints adjacent to the centre and at most one extra D--X edge.

The current exact proof chain is summarized in `backend/Q36_F2_LIVE_FRONTIER.md` and `OPEN_FRONTIERS.md`.

#### q36 f=2, other branches

For `2K1,a_F=1`, c=4,5,6 are EMPTY; only c>=7 remains.

For far target K2, d2 rows are at most3 pure disjoint K2 supports and d3 rows use at most two decorated missing classes.

#### shell-poor

At least five one-spoke pivots carry 22-point anti-neighbourhoods Z with

`110<=e_H(Z)<=122`, `alpha(H[Z])<=2`,

and exact charge

`q_v=133-e_H(Z)+g_a+e(D,A\{a})`.

A simultaneous near-Mantel stability theorem remains OPEN.

## Global state

Closed backend interval: `E329..E333`.

Remaining obligations:

- T61 E407/E408 high-Q coverage;
- legal backend E334..E340, with the q36 right edge now sharply reduced.

The full EG617 r=12 theorem remains **OPEN / NOT_CERTIFIED**.