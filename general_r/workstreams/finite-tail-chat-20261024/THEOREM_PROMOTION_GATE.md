# Theorem Promotion Gate

Date: 2026-10-24

## Purpose

This gate separates four different claims that must never be conflated:

1. deterministic encoding exists;
2. a finite module certificate is independently verified;
3. a conditional lemma is certified under explicitly named analytic assumptions;
4. the original EG617(r) theorem is proved.

Passing levels 1–3 does not imply level 4.

## Promotion states

| State | Required evidence | Permitted claim |
|---|---|---|
| `SCHEMA_ONLY` | deterministic encoding/hash only, or no applicable reduction theorem | plumbing works; no mathematical theorem promoted |
| `CONDITIONAL_LEMMA_CERTIFIED` | exact module certificate passes the independent verifier; theorem statement and all assumption IDs are frozen | the module implication holds if the listed assumptions hold |
| `ANALYTICALLY_DISCHARGED` | every consumed assumption has a theorem source applicable to this exact r | conditionality removed for this module only |
| `EG617_PROVED` | complete reduction equivalence, exhaustive canonical state space, sound symmetry witnesses, verified contradiction certificate, and all assumptions discharged | EG617(r) is proved |

The `ENDPOINT_DOMAIN_LOWER_BOUND_V1` and `D1_SHELL_CLASS_BOUND_V1` modules can reach `CONDITIONAL_LEMMA_CERTIFIED`; neither can reach `EG617_PROVED`. The latter records the proved-conditional d1 shell count consequence `N<=5` from the sibling endpoint classification, while the bounded-allowance d1 nonextension theorem remains open.

## Mandatory gate checks

For every module certificate, the gate must verify:

- the module identifier and exact theorem statement;
- immutable source branch, commit, path, and applicability;
- every assumption ID against the machine-readable snapshot in `ASSUMPTION_LEDGER.md`;
- exact integer/rational arithmetic, with no floating-point rounding;
- canonical variable map and complete constraint-generation version;
- instance SHA-256 and certificate SHA-256;
- producer/generator SHA-256 and constraint-generation version;
- an independent verifier that does not import producer code;
- verifier SHA-256, generation command, verifier replay command, and gate replay command;
- whether the module is applicable at this r;
- whether the module proves only a necessary condition or closes the full graph case.

## Current module: ENDPOINT_DOMAIN_LOWER_BOUND_V1

Mathematical statement, conditional on the selected q-ceiling profile:

For a legal regular repivot at a maximal-q state, if the missing degree is d, then
`q_y >= d(r+1-d)` and `q_y <= q_cap`; hence
`d(r+1-d) <= q_cap`.

The certificate enumerates every integer d from 0 through r, computes the lower bound exactly, and marks precisely the values not excluded by this necessary inequality.

This is a real conditional arithmetic lemma, not merely schema validation. It does not prove that any surviving degree is realizable, does not close any endpoint class, and does not prove graph nonexistence.

## Current module: D1_SHELL_CLASS_BOUND_V1

Under the sibling endpoint classification's A+B assumptions and r>=12, the shell-incidence premises imply `N*r<=6r-2`; hence six d1 shell classes are impossible and `N<=5`. The exact arithmetic certificate and independent verifier check the N=0,...,6 table. This is not an absolute bound on owner multiplicity within a shell class, so bounded-allowance d1 nonextension remains OPEN.

The gate uses the immutable module ID to select `verify_d1_shell_bound.py`; the generator, verifier, gate, source commit, assumptions, and replay command are all recorded in the committed receipt.

## Current status

- Module gate: `PASS_CONDITIONAL_MODULE` for r >= 12 after replay.
- For r < 12: `SCHEMA_ONLY` because the general RC reduction is not certified there.
- EG617 theorem promotion: **BLOCKED**. RC/front extraction is open, and the modules only prove local necessary-domain / shell-class bounds; neither exhausts graph states or proves a contradiction.
- No new EG617(r) theorem is claimed.
