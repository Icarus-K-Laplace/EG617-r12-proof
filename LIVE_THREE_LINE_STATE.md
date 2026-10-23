# Live research state — 2026-10-23

This is the synchronized human-readable live state. It contains research results only, not agent prompts.

## Front end — T61

The repository has continuous canonical h13 closure

`E397..E406 = EMPTY`.

E406 is independently closed by `front_end/E406_FULL_CLOSURE.md`.

### V9 low-Q upgrade

`front_end/T61_H13_V9_CANONICAL_AUDIT.md` independently replays the uploaded V9 package under its explicit retained lower-order seed contract.

New proved relative-to-seed exclusions:

- E407: `Q_max=27` impossible;
- E408: `Q_max=27` impossible;
- E408: `Q_max=28` impossible.

The exact correction-cycle identity is

`sum(h+kappa)=sum(eta+m)`

around a closed legal walk. It does **not** imply all nonnegative corrections vanish. The old purely algebraic zero-defect inference is `RETRACTED`.

The exact remaining front-end maximum-charge branches are

- E407: `Q in {31,32}`;
- E408: `Q in {31,32,33}`.

Full E407 and E408 remain OPEN.

## High backend

### E333 — V5 closure

`backend/E333_V5_CANONICAL_CLOSURE.md` independently replays the uploaded V5 package.

Under the retained legal-backend and V4 five-family forcing contract,

`E333 = EMPTY`.

Thus the remaining high backend interval is

`E334..E340 OPEN`.

### Assistant-owned right-edge subline — E338..E340

The complete K4,9 top-channel plateau family is empty under its stated lexicographic contract.

The q36 middle-distance ceiling branches are also completely removed:

- `backend/Q36_COMPENSATED_K49_NORMAL_FORM.md`;
- `backend/Q36_D9_COMPENSATED_CLOSURE.md`;
- `backend/Q36_D4_COMPENSATED_DYNAMICS.md`;
- `backend/Q36_D4_SUPPORT_CLASS_REDUCTION.md`;
- `backend/Q36_D4_COMPENSATED_CLOSURE.md`.

Hence q36 has no adjacent regular d4 or d9 exchange.

#### Candidate-coverage reduction

`backend/Q36_CANDIDATE_COVERAGE_CLUSTER_REDUCTION.md` proves that regular shell vertices form target-clique components, a decorated shell vertex can see regular vertices in at most one component, and all low-distance regular vertices lie in one component.

Therefore every remaining q36 shell belongs to one of two regimes:

1. **low-clique regime:** one low target clique C plus at most three far/high regular shell vertices;
2. **shell-poor regime:** no low adjacent regular vertices, hence at most two adjacent regular pivots. CORE211 pivot abundance then forces at least five nonadjacent one-spoke legal pivots in the 35-core.

#### f=3 far layer

`backend/Q36_F3_FAR_LAYER_REDUCTION.md` treats the maximal far layer f=3:

- far `K3`: EMPTY;
- far `3K1`: EMPTY;
- only `K2 union K1` survives.

The surviving K2+K1 state has two 11-supports overlapping in10 or11 points, one disjoint 12-support, and all low-clique 3-supports confined to an 11/12-point remainder.

`backend/Q36_F3_K21_TERMINAL_STRENGTHENING.md` further proves for every such low-clique triple D:

- `kappa(D)+m(D)<=1`;
- D induces at least two target edges;
- its shell-incidence mass is at least9 or10 depending on the 11-support overlap;
- every low-clique repivot has q<=35, so no q36 plateau cycle remains in this terminal.

#### shell-poor one-spoke interface

`backend/Q36_ONESPOKE_EXACT_FORMULA.md` proves that for a legal nonadjacent one-spoke pivot v with unique shell neighbour a, 12-neighbour set D and 22-point anti-neighbourhood Z,

`q_v=m(D)+kappa(D)+g_a+e(D,A\{a})`

and equivalently

`q_v=133-e_H(Z)+g_a+e(D,A\{a})`.

Moreover

`110<=e_H(Z)<=122`, `alpha(H[Z])<=2`.

Thus the shell-poor branch contains at least five simultaneous 22-point near-Mantel anti-neighbourhoods. Its remaining task is a joint stability/compatibility theorem for these five structures.

No full E338 edge layer is yet claimed closed. The q36 candidate-coverage problem has, however, been reduced from arbitrary shells to one finite dense-triple terminal plus one simultaneous near-Mantel one-spoke stability problem (along with the analogous f=0,1,2 low-clique layers still to be reduced).

## Closed low backend

`E329,E330,E331,E332,E333` are empty under their stated canonical/retained contracts. E332 remains frozen.

## Global state

The full EG617 r=12 theorem remains `OPEN / NOT_CERTIFIED`.

The mathematical obligations are now:

1. T61 E407 high-Q branches `31,32`;
2. T61 E408 high-Q branches `31,32,33`;
3. legal R(4,49) backend `E334..E340`.
