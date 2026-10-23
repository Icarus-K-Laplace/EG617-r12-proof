# T61 H13 V9 canonical audit

Status: `PROVED_RELATIVE_TO_RETAINED_SEEDS` for the low-Q maximum branches. Full `E407` and `E408` remain `OPEN`.

This file records the independently replayed contents of the uploaded `T61_H13_V9` package. The package does not recertify its lower-order seed theorems; those remain explicit retained inputs.

## Retained input contract

Let `R` be a 61-vertex T61 parent with

- `delta(R)=13`;
- `alpha(R)<=5`;
- `omega(R)<=11`;
- all inherited `D(n)` density caps.

For a regular pivot `p`, use the canonical shell/core notation `A,C,M,g,t,z,G,q_p`, and let `Q=max q_p` over regular pivots.

Retained seeds used by V9:

- `R(2,24)=empty` and every `R(2,23)` has at least 131 edges;
- every `R(3,35)` has minimum degree at least 12 and at least 211 edges.

These seeds are not newly proved by V9.

## 1. Global shell interface recovered

V9 proves an embedded `R(3,36)` exclusion inside the T61 parent. Consequently every genuine 47-core has minimum degree at least 11.

For every missing-shell edge `ab`, the uncovered core has at most 35 vertices, giving the missing interface

`|N_C(a) union N_C(b)| >= 12`, hence `t_a+t_b>=12`.

Together with the inherited caps this supplies the full hypotheses of the historical q27/q28 shell classifications on the actual 47-core shells; no 35-core minimum-degree12 claim is transported to those shells.

## 2. Exact repivot formula at the degree-11 baseline

For a regular shell neighbour `y`, let

- `d=d_M(y)`;
- `S=N_M(y)`;
- `D_y=N_C(y)`.

Then V9 proves

`q_y=d(12-d)+rho+h11+kappa+b`,

where all correction terms are nonnegative under the recovered minimum-degree11 interface.

Also, the degree-11 vertices of any `C in R(4,47)` form a target clique, conditional only on the retained `R(3,35)` minimum-degree12 seed.

## 3. Maximum Q=27 is impossible for E407 and E408

The audited q27 shell classification reduces every q27 maximum pivot to

`M = K_(3,a) + isolates`, `a in {8,9}`,

with three hub weights `(9,9,9)` and ten other shell vertices undecorated.

For every active nonhub `y`, the exact degree-11 repivot identity and `Q=27` force all residual corrections to zero. Hence every active core row is a triangle of degree-11 core vertices. The deficient-core clique theorem and repivoting force all active rows to coincide.

The resulting induced 14-set has at least

`55+3+3a >=82`

edges, contradicting `D(14)=69`.

Therefore

- `E407: Q_max=27` is impossible;
- `E408: Q_max=27` is impossible.

## 4. Maximum Q=28 shell reduction

The q28 classification has 19 historical shell types. V9 rechecks their exact hypotheses on the real 47-core.

- all 11 triangular types are excluded by new-core degree at most10;
- six non-B1 bipartite types are excluded by repeated deficient rows and the same induced-set contradiction;
- only the two B1 forms remain at a q28 pivot.

This yields a regular-block geometry: every regular pivot lies in a unique target `K11`, regular vertices are partitioned into such blocks, and true-twin classes inside a block have size exactly two or three.

## 5. 289-edge 47-core classification

V9 proves the following auxiliary theorem.

If `C in R(4,47)` has

- `e(C)=289`;
- `delta(C)=11`;
- at least one degree-11 vertex,

then the entire degree-11 set is either

1. a target `K10` whose vertices are true twins in `C`, or
2. a target `K11`.

The proof uses a degree-11 pivot, the retained 35-core floor/minimum degree, the 23-point lower bound, and the inherited `D14` cap. The missing graph of the 11-shell is forced to a star; the one-edge exceptional case gives the K10 twin alternative.

## 6. E408 maximum Q=28 is impossible

In the hypothetical q28 parent the regular-block geometry forces nine degree-11 vertices in the 289-edge maximizing core.

- If the degree-11 set is K11, the two additional vertices give an induced 13-set with at least `55+18+1=74` edges, contradicting `D(13)=67`.
- If it is the K10 twin case, the nine forced vertices become global true twins, contradicting the exact twin-class sizes two or three.

Therefore `E408: Q_max=28` is impossible.

## 7. Exact correction-cycle identity

For any legal adjacent regular pivots, with a common valid core baseline `beta`, V9 derives the exact pair of charge formulas and hence

`q_y-q_p = h-eta+kappa-m`.

For every closed legal walk,

`sum(h+kappa)=sum(eta+m)`.

This is a signed conservation identity. It does **not** imply that the nonnegative corrections vanish individually.

V9 includes a concrete 61-vertex local graph demonstrating a two-edge closed walk with nonzero cross correction `b=1` in each direction. That graph is explicitly not a T61 survivor and its selected pivots are not global maximizers. Its role is only to refute the invalid purely algebraic zero-defect inference.

Accordingly the inference

`closed walk + nonnegative corrections => all corrections zero`

is `RETRACTED`.

## 8. Updated exact frontier

Under the retained-seed contract:

### E407

- `Q=27`: `PROVED IMPOSSIBLE`;
- `Q=31`: `OPEN`;
- `Q=32`: `OPEN`.

### E408

- `Q=27`: `PROVED IMPOSSIBLE`;
- `Q=28`: `PROVED IMPOSSIBLE`;
- `Q=31`: `OPEN`;
- `Q=32`: `OPEN`;
- `Q=33`: `OPEN`.

At q31 the first unresolved distance-three plateau states are the five scalar patterns

`(h,kappa,b,m,eta)` =

- `(1,0,0,0,1)`;
- `(1,0,0,1,0)`;
- `(0,1,0,0,1)`;
- `(0,1,0,1,0)`;
- `(0,0,1,0,0)`.

These are necessary parameter patterns, not realized graphs. q32 and q33 have larger slack analogues. A genuine incidence/compatibility theorem or a new increasing potential is still required.

## Verification audit

`python -B verify_v9.py` was independently rerun and returned `COMPUTATION_CERTIFIED`, with 21 shell witnesses, 8192 subsets per shell, and the local graph check passing.

The package `SHA256SUMS.txt` matches the shipped files. Re-running the verifier rewrites three generated JSON files with LF line endings rather than the shipped CRLF line endings, changing their byte hashes but not their parsed content. This is a reproducibility-format issue, not a mathematical-content mismatch.

## Canonical conclusion

The front-end T61 frontier is now exactly

`E407: Q in {31,32}`

and

`E408: Q in {31,32,33}`,

relative to the retained lower-order seed contract. Neither full layer is yet closed.