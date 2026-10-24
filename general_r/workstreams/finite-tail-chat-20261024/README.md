# EG617 General-r Finite-Tail Certification

This workstream turns a future theorem

`exists r0, for all r>=r0, EG617(r)`

into a replayable plan for the remaining finite interval `4<=r<r0`.

It does **not** repeat the r=12 proof independently for every r. The architecture is

`parameter r`

`-> explicit analytic theorem gate`

`-> deterministic canonical constraints`

`-> reduced CSP / future SAT or exact-ILP instance`

`-> immutable certificate`

`-> independent tiny verifier`

`-> theorem-promotion gate`.

## Files

- `generate_instance.py` — deterministic V1 reduced-CSP generator.
- `verify_instance.py` — independent re-derivation/hash verifier; does not import the generator.
- `generate_endpoint_domain.py` / `verify_endpoint_domain.py` — exact missing-degree necessary-domain module and independent verifier.
- `generate_d1_shell_bound.py` / `verify_d1_shell_bound.py` — conditional d1 shell-class count module (`N<=5`) and independent verifier.
- `theorem_promotion_gate.py` — module-ID dispatch, assumption-ledger checks, producer/verifier hashes, and separate conditional-vs-EG617 promotion decisions.
- `ASSUMPTION_LEDGER.md` — analytic/machine boundary and per-assumption scope.
- `CERTIFICATE_SCHEMA.md` — universal certificate/replay contract.
- `TEST_VECTORS.json` — frozen r=12..15 regression hashes.
- `CANONICAL_STATE.md` — current support, search-space and certification matrix.
- `PROGRESS_LOG.md` — chronological workstream updates.
- `THEOREM_PROMOTION_GATE.md`, `ENDPOINT_MODULE_SCHEMA.md`, `SYMMETRY_CERTIFICATION.md`, `GRAPH_CSP_ADAPTER.md` — theorem-aware module and symmetry contracts.
- `CERTIFICATE_REPLAY_REPORT.md` — exact replay results, hashes, and adversarial checks.
- `certificates/endpoint_domain_r13_residual_core.json` plus receipt — verified conditional scalar-domain module.
- `certificates/d1_shell_class_bound_r13.json` plus receipt — verified conditional d1 shell-class bound.

## Deterministic generation

Example:

```bash
python generate_instance.py 13 --profile residual-core --output /tmp/eg617-r13.json
python verify_instance.py /tmp/eg617-r13.json
```

For the stronger anchor branch:

```bash
python generate_instance.py 13 --profile near-anchor --output /tmp/eg617-r13-anchor.json
python verify_instance.py /tmp/eg617-r13-anchor.json
```

A verifier `PASS` means only that the canonical reduced CSP payload is exactly the one specified by the V1 theorem interface and that its hash matches. It does **not** mean EG617(13) is proved.

## V1 theorem profiles

`residual-core` consumes assumption `RC` and derives `q<=3r+2`.

`near-anchor` consumes `RC + ANCHOR_K8` and derives `q<=3r-1`.

The current general residual-core source is marked for `r>=12`; generation below 12 is intentionally allowed only so the certificate format is universal. Such instances remain `SCHEMA_ONLY` until a parameter-specific reduction is attached.

## Why the first CSP is small

The general-r backend already proves the exact regular-repivot base

`q_y >= d(r+1-d)`.

Combining this with the applicable q ceiling determines the legal missing-degree domain before any graph search. This immediately demonstrates that the finite-tail solver should be modular rather than a parameter-scaled copy of r=12:

- at baseline, r=12..14 retain the boundary d=4 orbit;
- from r>=15, all medium missing degrees disappear;
- under ANCHOR_K8, the medium degrees disappear already from r>=12.

Two modules now pass the conditional promotion gate: `ENDPOINT_DOMAIN_LOWER_BOUND_V1` certifies the necessary scalar domain, and `D1_SHELL_CLASS_BOUND_V1` certifies the conditional bound of at most five d1 shell classes. Neither closes the d1 terminal or proves graph nonexistence. The next graph/SAT adapter will instantiate only endpoint terminal modules whose analytic premises are certified for that parameter.

## Symmetry policy

V1 implements only the exact scalar reflection `d <-> r+1-d`.

A future graph/SAT adapter must make color/vertex quotienting independently checkable through a deterministic canonical colored-incidence form and stabilizer witnesses. Merely using a symmetry-breaking heuristic inside a solver is insufficient for certification.

## Machine-proof policy

Preferred order:

1. analytic closure;
2. bounded enumeration with a tiny exact checker;
3. SAT with LRAT/DRAT proof checking;
4. exact integer/rational ILP infeasibility witness;
5. Lean/Coq wrapper for the final finite implication.

Opaque solver success, floating-point optimizer logs, or unreplayable search output are not accepted as proof artifacts.

## Current global status

No concrete all-large-r threshold `r0` has yet been certified by the sibling synthesis. The latest integration records three remaining asymptotic interfaces: front extraction/RC, residual endpoint terminal closure, and robust design-terminal stability. The three-anchor excess theorem is no longer an asymptotic blocker above r=68.

Accordingly this workstream is now `CONDITIONAL_MODULE_CERTIFIED`, not `FINITE_TAIL_CLOSED`. No new EG617(r) theorem has been proved.
