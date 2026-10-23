# Live research state — 2026-10-23

This is the synchronized human-readable live state. It contains research results only, not agent prompts.

## Front end — T61

The repository has continuous canonical h13 closure

`E397..E406 = EMPTY`.

### V9/V10 front-end state

`front_end/T61_H13_V9_CANONICAL_AUDIT.md` and `front_end/T61_H13_V10_CANONICAL_AUDIT.md` record the reviewed package results under the explicit retained lower-order seed contract.

Closed maximum-charge branches:

- E407: `Q=27` impossible;
- E408: `Q=27` impossible;
- E408: `Q=28` impossible.

V10 additionally proves that at a maximizing Q31 pivot no regular shell neighbour has missing degree3 or10. Hence every regular shell vertex of a hypothetical Q31 maximum has missing degree only

`{0,1,2,11,12}`.

Coverage remains OPEN. The shell-only witness

`M = K2 join (K2 disjoint_union 9K1)`

with decorations `4,3` on the inner K2 is not yet a genuine T61 completion.

Remaining front-end branches:

- E407: `Q in {31,32}`;
- E408: `Q in {31,32,33}`.

The exact correction-cycle identity remains

`sum(h+kappa)=sum(eta+m)`;

it does not imply individual zero defects.

## High backend

### E333 — V5 closure

`backend/E333_V5_CANONICAL_CLOSURE.md` proves, relative to the retained legal-backend/V4 forcing contract,

`E333 = EMPTY`.

Thus the remaining high backend interval is

`E334..E340 OPEN`.

### Astra-B V6 — E334..E337

`backend/HIGH_LAYER_BACKEND_V6_CANONICAL_AUDIT.md` independently replays V6. The verifier passed and every manifest SHA-256 matched.

Relative to the retained backend contract V6 proves:

- CORE212 matching residual impossible, extending through core213 / total core excess `K<=6`;
- repeated-pair `r=1`, allowance<=2 and `K in {2,4,6}` implies multiplicity `m<=6`;
- the q<=32 short-row no-far branch has exactly two active hubs; one-hub and three-hub branches are empty.

E334--E337 remain OPEN. The remaining B-line gaps are far/d3 forcing, double-hub `r>=2`, allowance3, and for higher layers the `K>=8` concentration / overlap-10 K11 equality mechanisms.

### Assistant-owned right-edge subline — E338..E340

The complete K4,9 top-channel plateau family is empty.

Global low-decoration forcing proves

- `q36 => G>=3`;
- `q37 => G>=2`;
- `q38 => G>=3`.

Every q38,G=2 shell is eliminated. For q36, regular d4/d9 ceiling exchanges are empty.

Candidate coverage splits into:

1. a low-clique regime;
2. a shell-poor regime with at least five nonadjacent one-spoke pivots in CORE211.

The entire f=3 low-clique layer is CLOSED, so the low-clique branch has `f<=2`.

#### q36 f=2 — exact current state

`backend/Q36_F2_SHELL_LEDGER_REDUCTION.md` gives the exact shell identity

`G=14-mu-delta+a_F-nu`

and every low-clique row has missing degree2 or3.

For far target K2:

- at most3 d2 rows, with distinct disjoint pure K2 supports;
- d3 rows use at most two decorated missing-set classes;
- in the no-d2/two-class sector, total common-S allowance is at most1.

For far `2K1` with exactly one far-decoration incidence:

- all low rows share one d3 missing set;
- `c=4,5,6` are EMPTY;
- the surviving branch has `c>=7`.

For far `2K1` with `a_F=0`:

- the two far 12-supports are disjoint and leave an 11-point remainder `R` with `alpha(H[R])<=2`;
- d2 rows have at most two distinct support classes;
- a repeated d2 class is the unique d2 class and is a zero-defect pure K2 repivoting to q35;
- if `n2>=3`, all d2 rows share that K2 and satisfy `3n2<=c+nu+2`, `2n2<=c+4`;
- the all-d2 branch has `c<=4`;
- d3 rows use at most two decorated missing-set classes;
- allowance-zero d3 class size<=2;
- allowance-one repeated classes are unique pure q35 K3 classes;
- allowance-two d3 class size<=6;
- all-d3/two-missing-class sector has `c<=6`.

The high-c all-d3/single-class sector is completely CLOSED:

- `c=7` and `c=8` by the high-c zero-gap normal form and decoration overflow;
- `c=9` by `backend/Q36_F2_2K1_A0_C9_FULL_CLOSURE.md`;
- `c=10` by `backend/Q36_F2_2K1_A0_C10_FULL_CLOSURE.md`.

The c=10 common-point proof is analytic: row closure in the triangle-free complement forces all ten 3-supports to share one core point, then the K11 `{p} union C` plus D14 support-incidence cap gives a contradiction.

`backend/Q36_F2_2K1_A0_C10_MIXED_FULL_CLOSURE.md` also eliminates every c=10 state containing at least one d2 row. Therefore the entire

`2K1, a_F=0, c=10`

layer is EMPTY.

The remaining f=2 targets are now:

1. `2K1,a_F=0` mixed d2/d3 states with `c<=9`, beginning with c=9;
2. `2K1,a_F=1,c>=7`;
3. the far-target-K2 topology.

#### shell-poor interface

`backend/Q36_ONESPOKE_EXACT_FORMULA.md` proves that a nonadjacent one-spoke pivot v with 12-neighbour support D and 22-point anti-neighbourhood Z satisfies

`q_v=m(D)+kappa(D)+g_a+e(D,A\{a})`

and

`q_v=133-e_H(Z)+g_a+e(D,A\{a})`,

with

`110<=e_H(Z)<=122`, `alpha(H[Z])<=2`.

The shell-poor branch contains at least five simultaneous such near-Mantel anti-neighbourhoods. Its remaining task is a joint stability/compatibility theorem.

No full E338 layer is yet claimed closed.

## Closed low backend

`E329,E330,E331,E332,E333` are empty under their stated canonical/retained contracts. E332 remains frozen.

## Global state

The full EG617 r=12 theorem remains `OPEN / NOT_CERTIFIED`.

The mathematical obligations are now:

1. T61 E407 high-Q branches `31,32`;
2. T61 E408 high-Q branches `31,32,33`;
3. legal R(4,49) backend `E334..E340`, with E333 closed and the q36/q38 right-edge sectors sharply reduced.