# Finite-Tail Replay Protocol

## Admission before generation

1. Run `python PARAMETER_ADMISSION_VERIFIER.py PARAMETER_ADMISSION_MATRIX.json --audit-range 4 100`.
2. Query the exact parameter/module/profile, for example:
   `python PARAMETER_ADMISSION_VERIFIER.py PARAMETER_ADMISSION_MATRIX.json --query-r 13 --module ENDPOINT_DOMAIN_LOWER_BOUND_V1 --profile residual-core`.
3. If the query returns `BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE`, do not promote a generated schema instance as a theorem-level certificate.
4. If it returns `CONDITIONAL`, preserve the required assumption IDs in the certificate and receipt.

## Generate and replay one family member

Use `generate_parametric_certificate.py`; it invokes the existing module generator, independent verifier through the promotion gate, and records the admission matrix fingerprint.

For a direct forensic replay, run the commands in the receipt separately:

```bash
python verify_endpoint_domain.py certificates/endpoint_domain_r13_residual_core.json
python theorem_promotion_gate.py certificates/endpoint_domain_r13_residual_core.json --receipt certificates/endpoint_domain_r13_residual_core_receipt.json
```

For d1:

```bash
python verify_d1_shell_bound.py certificates/d1_shell_class_bound_r13.json
python theorem_promotion_gate.py certificates/d1_shell_class_bound_r13.json --receipt certificates/d1_shell_class_bound_r13_receipt.json
```

## Required tampering checks

- Change an instance parameter without regenerating the certificate: instance/certificate hash must fail.
- Remove an assumption ID from the ledger: gate must fail closed with `BLOCKED_UNKNOWN_ASSUMPTION_ID`.
- Query r=11 for either module: admission must return `BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE`.
- Change a row in the admission matrix, a source commit, or a parameter range: independent matrix verifier must reject the matrix.
- Change a D1 class-count row: independent D1 verifier must reject the certificate.
- Change a scalar candidate or reflection class: independent endpoint-domain verifier must reject the certificate.

## What a PASS does not mean

A matrix audit PASS means the registry matches the frozen source/range policy. A conditional module PASS means the arithmetic implication is independently checked under the stated premises. Neither status discharges RC/front extraction, closes the remaining endpoint terminals, proves an all-large-r theorem, or proves EG617(r).
