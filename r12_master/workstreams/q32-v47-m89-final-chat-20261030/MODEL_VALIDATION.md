# Model validation and overconstraint audit

## Source audit

| Item | Result | Status |
|---|---|---|
| 61-point edge variables and unique edge ownership | Present | PROVED_CONDITIONAL |
| Exact color counts 408 / 129 / 130 / 131 | Correct vector in both m cases | PROVED_CONDITIONAL |
| Twelve Type-I K5 factors per exact color | Present | PROVED_CONDITIONAL |
| All legal outside profiles | Sum and caps imply exactly the three permitted profiles | PROVED_CONDITIONAL |
| Special-factor single-outside witnesses | Allowed; no factor-index restriction | PROVED_CONDITIONAL |
| At least ten witnesses per exact color | Follows from profiles; now explicitly checked by verifier | PROVED_CONDITIONAL |
| Cross-color pairwise linearity | Follows from unique edge ownership; now explicitly checked | PROVED_CONDITIONAL |
| Full support U=H | Explicit coverage constraints and verifier | PROVED_CONDITIONAL |
| alpha(H)<=4, alpha(G_C)<=12, omega(G_C)<=5 | Lazy exact separation and independent verifier | PROVED_CONDITIONAL |
| Reserve caps | Uses unconditional (4,5,5); stronger caps only conditional | PROVED_CONDITIONAL |

## New m=8/9 strengthening

1. Existential perfect matching variables for every pivot-block pair.
2. Pointwise neighbor constraints for each pivot vertex against every other pivot block.
3. Exact per-block degree ledger `X_i+Y_i=5+epsilon_i`.
4. Lazy light-pair matching-composition cuts.
5. Multi-projection edge lower bounds using the independently enumerated `mu_4(t)` table.
6. Independent candidate verifier now recomputes perfect matchings, uniqueness of light pairs, all forced compositions, per-block ledgers, residual-to-pivot neighbor counts, witness counts, and cross-color linearity.

These additions are consequences of the frozen source contract and alpha(H)<=4; they do not force any special-factor placement.

## Common-P applicability audit

The inspected `V47_ALIGNED_TYPEI_COMPONENT_NORMAL_FORM.md`, `V47_T0_POINTWISE_COLOR_SATURATION.md`, and `V47_Z01_SHARED_P_FACTOR_PACKING.md` are part of the aligned m=10 3+7 track cell. They do not establish an m=8/9 track partition. Their six common-P factors and residual-signature rules are therefore not used here.

## Execution status

The dependency-free local verifier for scalar arithmetic, source profiles, the matching-composition cases, and the K4,4 lookup table passed. The full Z3 solver was **not run**: the available Python runtime has no `z3-solver` module. No solver version, SMT run, SAT candidate, UNSAT proof, or proof replay is claimed.

## Invalid shortcuts explicitly rejected

- **WITHDRAWN:** `delta(H[R])>=12-m` without controlling extra Q-R edges.
- **WITHDRAWN:** `d_H(q,R)>=13-m` without controlling extra Q-Q edges.
- **WITHDRAWN for m=8/9:** importing the aligned m=10 common-P and residual-signature constraints.
