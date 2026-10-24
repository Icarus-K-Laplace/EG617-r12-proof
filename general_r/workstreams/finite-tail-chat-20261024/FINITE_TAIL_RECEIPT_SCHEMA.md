# Finite-Tail Theorem Receipt Schema

Schema ID: `eg617-finite-tail-theorem-receipt-v1`.

A final parameter receipt is not a solver log. It is a proof-dependency manifest whose status is the conjunction of all required gates.

## Required fields

```json
{
  "schema": "eg617-finite-tail-theorem-receipt-v1",
  "statement": "full exact statement of EG617(r)",
  "r": 13,
  "analytic_reduction": {
    "source_branch": "...",
    "source_commit": "...",
    "source_path": "...",
    "source_blob_sha256": "...",
    "parameter_applicability": {"min_r": 12, "max_r": null},
    "terminal_contract": "...",
    "status": "PROVED|CONDITIONAL|OPEN"
  },
  "assumption_ids": ["RC"],
  "admission": {
    "matrix_path": "PARAMETER_ADMISSION_MATRIX.json",
    "matrix_sha256": "...",
    "admission_verifier_path": "parameter_admission_verifier.py",
    "admission_verifier_sha256": "...",
    "status": "ADMISSIBLE|CONDITIONAL|BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE"
  },
  "finite_instance": {
    "path": "...",
    "schema": "...",
    "generator_path": "...",
    "generator_version": "...",
    "generator_sha256": "...",
    "instance_sha256": "...",
    "certificate_path": "...",
    "certificate_sha256": "...",
    "certificate_kind": "ANALYTIC|BOUNDED_ENUMERATION|LRAT|DRAT|EXACT_ILP|NONE"
  },
  "symmetry": {
    "kind": "NONE|SCALAR_REFLECTION|GRAPH_WITNESS",
    "witness_path": "...",
    "witness_sha256": "...",
    "status": "VERIFIED|OPEN|NOT_APPLICABLE"
  },
  "replay": {
    "verifier_path": "...",
    "verifier_sha256": "...",
    "verification_command": "...",
    "gate_path": "theorem_promotion_gate.py",
    "gate_sha256": "...",
    "gate_command": "..."
  },
  "bridge_status": "PROVED|CONDITIONAL|OPEN",
  "assumptions_discharged_for_r": false,
  "complete_state_space": false,
  "certificate_verified": false,
  "eg617_r_status": "OPEN|CONDITIONAL|PROVED",
  "eg617_r_proved": false
}
```

## Promotion invariant

`eg617_r_proved=true` is legal only if all of the following are true for the same r:

1. the analytic reduction is applicable and proved;
2. the reduction covers every legal original state;
3. the terminal contract and all assumption IDs are discharged;
4. the finite state space is complete;
5. every symmetry quotient has a sound and complete independent witness;
6. the exact certificate passes an independent verifier;
7. independent replay succeeds;
8. no bridge remains OPEN or CONDITIONAL.

The current endpoint-domain and d1 shell-class receipts are local conditional-module receipts, not final theorem receipts.
