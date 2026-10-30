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

1. Pairwise perfect-matching existence is forced by exact alpha(H) separation and independently recomputed by the candidate verifier; no redundant matching-choice variables are added.
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


## Additional 2026-10-30 audits

### Guarded matching-composition cuts

A code audit found that the first lazy matching-composition implementation added unconditional consequences inferred from one candidate model. That was an overconstraint: a future legal model could make one incident pivot pair heavy or change the selected pivot blocks. **WITHDRAWN:** those unconditional cuts.

The solver now adds only implications guarded by:
- both incident pivot-pair edge counts remaining exactly four;
- the same four vertices remaining selected in each of the three pivot blocks;
- the same four matching edges remaining target-colored.

The multi-projection \(\mu_4(t)\) cut is guarded by the conjunction of the distinct matching-composition conditions. This preserves validity under changes of source placement and pivot blocks.

### Exact source-core and near-Turan strengthening

The solver now encodes the exact identity \(e_C(H)=B_C+G_C^H\), the source-parameter bounds for x in O / two-double / triple profiles, and the conditional 69/70 partition normal form. The independent verifier reconstructs a \(11K_4+K_3\) partition from the source witnesses whenever \(e_C(H)\le70\), and checks its cross-edge count.

### Nonexact m=9 floor reconciliation

The model uses the source-correct pointwise floors 4 for a 130-edge color and 3 for a 131-edge color, hence \(L_9=7\). The root global canonical/dependency summaries still contain an older \(L_9=6\) line; the read-only Case-II canonical/dependency audit explicitly marks 6 as stale and records \(4+3=7\). No root-side file was modified.
