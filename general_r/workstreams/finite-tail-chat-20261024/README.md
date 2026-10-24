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
- `ASSUMPTION_LEDGER.md` — analytic/machine boundary and per-assumption scope.
- `CERTIFICATE_SCHEMA.md` — universal certificate/replay contract.
- `TEST_VECTORS.json` — frozen r=12..15 regression hashes.
- `CANONICAL_STATE.md` — current support, search-space and certification matrix.
- `PROGRESS_LOG.md` — chronological workstream updates.

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

The first module, `ENDPOINT_DOMAIN_LOWER_BOUND_V1`, now turns this necessary inequality into a complete exact certificate and independent replay. It proves only the necessary scalar domain; it does not close any endpoint class. The next graph/SAT adapter will instantiate only endpoint terminal modules whose analytic premises are certified for that parameter.

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
