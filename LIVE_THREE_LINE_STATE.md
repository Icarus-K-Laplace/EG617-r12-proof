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

V10 additionally proves:

> at a maximizing Q31 pivot, no regular shell neighbour has missing degree3 or10.

Thus a hypothetical Q31 maximum shell has regular missing degrees only

`{0,1,2,11,12}`.

Coverage remains OPEN. V10 supplies a shell-only necessary-condition witness

`M = K2 join (K2 disjoint_union 9K1)`

with decorations `4,3` on the inner K2. This is not a genuine T61 completion; its 47-core compatibility remains the first concrete completion test.

The exact remaining front-end branches are

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

### Astra-B V6 — E334..E337 capacity extension

`backend/HIGH_LAYER_BACKEND_V6_CANONICAL_AUDIT.md` independently replays the uploaded V6 package. The verifier passed all certified arithmetic and every manifest SHA-256 matched.

Relative to the retained backend contract, V6 proves:

- `CORE212_MATCHING_RESIDUAL_IMPOSSIBLE`, strengthened through core213 / total core excess `K<=6`;
- for repeated missing pairs with `r=1`, allowance<=2 and `K in {2,4,6}`, multiplicity satisfies `m<=6`;
- the short-row no-far branch at q<=32 has exactly two active hubs; the one-hub and three-hub branches are analytically excluded.

This covers the repeated-pair obstruction in the actual core211/212/213 E334 channels when the family is forced.

E334--E337 remain OPEN. The uncovered Astra-B work is explicitly:

1. far-neighbour and missing-degree-three forcing;
2. double-hub branches with `r>=2`;
3. the `r=1` allowance-three boundary;
4. for higher layers, `K>=8` concentration and the overlap-10 K11 equality mechanism.

### Assistant-owned right-edge subline — E338..E340

The complete K4,9 top-channel plateau family is empty under its stated lexicographic contract.

`backend/HIGH_RIGHT_EDGE_LOW_DECORATION_FORCING.md` proves

- `q36 => G>=3`;
- `q37 => G>=2`;
- `q38 => G>=3`.

Every q38,G=2 shell is eliminated, including the final cross-side K4,9 state.

The q36 middle-distance ceiling branches d4/d9 are completely removed by the compensated-K4,9 proof chain. Hence q36 has no adjacent regular d4 or d9 exchange.

#### Candidate-coverage split

Every remaining q36 shell belongs to one of two regimes:

1. **low-clique regime:** one low target clique C plus far/high regular vertices;
2. **shell-poor regime:** at most two adjacent regular pivots and at least five nonadjacent one-spoke legal pivots in CORE211.

The entire f=3 low-clique layer is CLOSED by

- `backend/Q36_F3_FAR_LAYER_REDUCTION.md`;
- `backend/Q36_F3_K21_TERMINAL_STRENGTHENING.md`;
- `backend/Q36_F3_K21_SUPPORT_CLASS_COLLAPSE.md`;
- `backend/Q36_F3_FULL_CLOSURE.md`.

Therefore the low-clique branch has `f<=2`.

#### New f=2 reduction

`backend/Q36_F2_SHELL_LEDGER_REDUCTION.md` gives an exact shell ledger for two far vertices. With low clique C and decorated set X, `|C|+|X|=11`, and

`G=14-mu-delta+a_F-nu`,

where `mu=e_M(F)`, `delta=e_M(C,X)`, `nu=e_M(X)`, and `a_F=e_F(F,X)`.

Every low row has missing degree2 or3. For far target K2:

- there are at most3 d2 rows, all with distinct disjoint pure K2 supports;
- d3 rows use at most two decorated missing-set classes;
- if no d2 row occurs and both d3 classes occur, their total common-S allowance is at most1.

`backend/Q36_F2_2K1_A1_REDUCTION.md` treats the two-singleton far topology with exactly one far-decoration incidence. All low rows then share one d3 missing set. It proves

- c=4 and c=5 are EMPTY;
- c=6 forces allowance exactly2;
- in the c=6 terminal all X-missing edges are incident to one decorated vertex x0, `g_x0=4-nu`, every other decorated vertex has g=1, and `|N_H(x0)|=11`.

Thus this formerly arbitrary f=2 sector is reduced to a small allowance-two six-row compatibility terminal plus the remaining c>=7 / other far-incidence branches.

#### Shell-poor interface

`backend/Q36_ONESPOKE_EXACT_FORMULA.md` proves that a nonadjacent one-spoke pivot v with 12-neighbour support D and 22-point anti-neighbourhood Z satisfies

`q_v=m(D)+kappa(D)+g_a+e(D,A\{a})`

and

`q_v=133-e_H(Z)+g_a+e(D,A\{a})`,

with

`110<=e_H(Z)<=122`, `alpha(H[Z])<=2`.

The shell-poor branch contains at least five simultaneous such near-Mantel anti-neighbourhoods. Its remaining task is a joint stability/compatibility theorem.

No full E338 edge layer is yet claimed closed.

## Closed low backend

`E329,E330,E331,E332,E333` are empty under their stated canonical/retained contracts. E332 remains frozen.

## Global state

The full EG617 r=12 theorem remains `OPEN / NOT_CERTIFIED`.

The mathematical obligations are now:

1. T61 E407 high-Q branches `31,32`;
2. T61 E408 high-Q branches `31,32,33`;
3. legal R(4,49) backend `E334..E340`, with E333 closed, V6 narrowing E334--E337, and the q36/q38 right-edge sectors sharply reduced as above.