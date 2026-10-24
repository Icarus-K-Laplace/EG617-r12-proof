# Endpoint Module Schema

## Architecture

The theorem-aware path is

`r -> certified theorem gates -> canonical constraints -> reduced CSP -> certificate -> independent verifier -> theorem-promotion gate`.

Each module is an immutable contract, not a bag of solver clauses. It binds a theorem statement, source commit, applicability, assumption IDs, variable map, generator version, instance hash, certificate hash, generator/verifier hashes, generation command, verifier replay command, gate replay command, and promotion state.

## Module manifest fields

Every future endpoint module must provide:

- `module_id`, `module_kind`, schema version, and exact theorem statement;
- source branch, immutable commit, path, theorem identifier, and parameter applicability;
- all consumed assumption IDs and their per-r status;
- a canonical variable map with domains and meanings;
- exact constraint formulas and the theorem that justifies each constraint;
- deterministic generation version and canonical JSON rules;
- instance and certificate hashes;
- certificate format and completeness argument;
- independent verifier path/hash and replay command;
- module status, bridge status, and EG617 promotion status.

Unknown assumption IDs, unknown constraint IDs, unsupported parameter ranges, or missing proof artifacts must fail closed.

## First module: ENDPOINT_DOMAIN_LOWER_BOUND_V1

### Exact conditional theorem

Fix r >= 12 and select one of the following q ceilings:

- `residual-core`: under RC, `q_cap = 3r+2`;
- `near-anchor`: under RC and ANCHOR_K8, `q_cap = 3r-1`.

For a legal regular repivot at a maximal-q state, the analytic lower bound gives

`q_y >= d(r+1-d)`.

The selected global ceiling gives `q_y <= q_cap`. Therefore every such repivot must satisfy

`0 <= d <= r` and `d(r+1-d) <= q_cap`.

The certificate's domain is exactly the integer solution set of that necessary inequality. The converse is deliberately not claimed: a surviving d need not correspond to any graph state.

### Exact certificate contents

The generator emits:

1. the theorem/assumption/source manifest;
2. a row for every integer `d=0,...,r`;
3. exact integer `d(r+1-d)`, q ceiling, slack, and the admissibility bit;
4. the complete candidate degree list;
5. scalar-reflection classes with explicit singleton-boundary handling;
6. a canonical instance hash and a certificate hash over the complete body.

The independent verifier reconstructs these fields from `r` and the profile without importing the generator. It checks row completeness and order, every arithmetic value, every candidate, every reflection class, both hashes, and the fixed theorem scope.

## Second module: D1_SHELL_CLASS_BOUND_V1

Under the sibling endpoint classification's hypotheses A+B and r>=12, each distinct d1 missing-partner shell vertex has incidence at least r, while the total shell incidence is at most 6r-2. Thus if N is the number of d1 shell classes,

`N*r <= 6r-2`.

Six classes would require `6r` incidences, exceeding the cap by exactly 2; hence `N<=5`. The module certificate checks N=0,...,6 exactly and uses monotonicity to exclude every N>=7. It does not prove bounded multiplicity inside one of the five classes.

Replay:

```bash
python generate_d1_shell_bound.py 13 --output certificates/d1_shell_class_bound_r13.json
python verify_d1_shell_bound.py certificates/d1_shell_class_bound_r13.json
python theorem_promotion_gate.py certificates/d1_shell_class_bound_r13.json --receipt certificates/d1_shell_class_bound_r13_receipt.json
```

The module consumes `RC + ANCHOR_K8`, is conditional for r=12,...,67, and remains conditional on RC even for r>=68. Its arithmetic certificate verifies the counting implication; it does not independently prove the upstream graph-theoretic shell lemmas.

## Conditional vs hard constraints

- If the reduction source is not applicable at this r, the module is `SCHEMA_ONLY`.
- If it is applicable but an assumption remains open, the lemma may be recorded as `CONDITIONAL_LEMMA_CERTIFIED`; its constraints may be used only in an explicitly conditional branch.
- A constraint may be activated in an unconditional theorem instance only after all its assumptions are proved for that exact r.
- This module cannot close d0, d1, d2, d3, or high-endpoint graph cases. It only removes missing-degree values violating the necessary quadratic inequality.

## Exact arithmetic and reproducibility

All values are integers. JSON is serialized with sorted keys, compact separators, ASCII encoding, then SHA-256 hashed. No floating-point arithmetic or optimizer output appears in this module.

Replay:

```bash
python generate_endpoint_domain.py 13 --profile residual-core --output /tmp/eg617-endpoint-r13.json
python verify_endpoint_domain.py /tmp/eg617-endpoint-r13.json
python theorem_promotion_gate.py /tmp/eg617-endpoint-r13.json --receipt /tmp/eg617-endpoint-r13-receipt.json
```
