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

The proof tracks labelled excess and simultaneous row compatibility; it does not use the retracted zero-cycle shortcut and it allows neighbouring q30 views.

Thus a hypothetical Q31 maximum shell has regular missing degrees only

`{0,1,2,11,12}`.

Coverage remains OPEN. V10 supplies a shell-only necessary-condition witness

`M = K2 join (K2 disjoint_union 9K1)`

with decorations `4,3` on the inner K2. This is not a genuine T61 completion; its 47-core compatibility is the first concrete completion test.

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

Astra B is assigned E334--E337, beginning with the 212-edge-core extension of the repeated-pair capacity theorem.

### Assistant-owned right-edge subline — E338..E340

The complete K4,9 top-channel plateau family is empty under its stated lexicographic contract.

`backend/HIGH_RIGHT_EDGE_LOW_DECORATION_FORCING.md` proves the global low-decoration thresholds

- `q36 => G>=3`;
- `q37 => G>=2`;
- `q38 => G>=3`.

In particular every q38,G=2 shell is forced to be K4,9 and every decoration placement, including the final cross-side one-unit/one-unit state, is eliminated.

The q36 middle-distance ceiling branches are completely removed by

- `backend/Q36_COMPENSATED_K49_NORMAL_FORM.md`;
- `backend/Q36_D9_COMPENSATED_CLOSURE.md`;
- `backend/Q36_D4_COMPENSATED_DYNAMICS.md`;
- `backend/Q36_D4_SUPPORT_CLASS_REDUCTION.md`;
- `backend/Q36_D4_COMPENSATED_CLOSURE.md`.

Hence q36 has no adjacent regular d4 or d9 exchange.

#### Candidate-coverage reduction

`backend/Q36_CANDIDATE_COVERAGE_CLUSTER_REDUCTION.md` proves that every remaining q36 shell belongs to one of two regimes:

1. **low-clique regime:** one low target clique C plus at most three far/high regular shell vertices;
2. **shell-poor regime:** no low adjacent regular vertices, hence at most two adjacent regular pivots and at least five nonadjacent one-spoke legal pivots in the CORE211 core.

#### Low-clique far layers

The maximal far layer f=3 is now completely empty.

The proof chain is

- `backend/Q36_F3_FAR_LAYER_REDUCTION.md`;
- `backend/Q36_F3_K21_TERMINAL_STRENGTHENING.md`;
- `backend/Q36_F3_K21_SUPPORT_CLASS_COLLAPSE.md`;
- `backend/Q36_F3_FULL_CLOSURE.md`.

The final closure uses the fact that the 11/12-point remainder R has `alpha(H[R])<=2`, hence at least25/30 target edges, while row closure and the total CORE211 excess2 give upper bounds21/26.

Therefore the low-clique q36 regime now satisfies

`f<=2`.

The remaining low-clique work is the analogous `f=0,1,2` reduction.

#### Shell-poor one-spoke interface

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
3. legal R(4,49) backend `E334..E340`, with E333 closed and the q36/q38 right-edge sectors sharply reduced as above.