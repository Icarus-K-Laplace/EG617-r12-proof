# Parameterized Endpoint Certificate Families

Status: **PARAMETERIZED CONDITIONAL MODULES / NO EG617(r) PROMOTION**.

This interface reuses the existing generators and independent verifiers. It does not fork their arithmetic logic.

## Family A — `ENDPOINT_DOMAIN_LOWER_BOUND_V1`

For each admitted parameter `r>=12`, the generator lists every integer `d=0,...,r` and verifies exactly

`d(r+1-d) <= q_cap`.

Profiles:

| Profile | q ceiling | Assumptions | Admission |
|---|---:|---|---|
| `residual-core` | `q_cap=3r+2` | RC | Conditional for r>=12; blocked below 12 |
| `near-anchor` | `q_cap=3r-1` | RC + ANCHOR_K8 | Conditional for r>=12; broad ANCHOR_K8 is source-proved only for r>=68 |

The exact three-anchor theorem has a separate source and applies for r>=12 only when three pairwise nonadjacent degree-r anchors are established. It is not silently substituted for broad `ANCHOR_K8`.

The independent verifier reconstructs all `r+1` rows and the scalar reflection partition. A valid candidate-domain certificate only records which d-values are not excluded by this inequality; it does not assert that a surviving d is graph-realizable.

## Family B — `D1_SHELL_CLASS_BOUND_V1`

For every source-applicable `r>=12`, the exact arithmetic rows are

`N*r <= 6*r-2`, for `N=0,...,6`.

The verifier checks every row. Six classes require `6r) incidences, exceeding the cap `6r-2` by exactly two, so `N<=5`. Every `N>=7` is excluded by monotonicity. This is a shell-class count, not an owner-multiplicity bound.

The source theorem is conditional on RC + broad ANCHOR_K8. For `12<=r<68`, ANCHOR_K8 remains open in this broad context; for `r>=68`, ANCHOR_K8 is source-proved but RC/front extraction remains open.

## Unified CLI

The wrapper consults the independently checked admission matrix before invoking the frozen module generator and theorem gate.

Example, conditional residual-core family member:

```bash
python generate_parametric_certificate.py \
  --module ENDPOINT_DOMAIN_LOWER_BOUND_V1 --r 13 --profile residual-core \
  --output certificates/endpoint_domain_r13_residual_core.json \
  --receipt certificates/endpoint_domain_r13_residual_core_receipt.json
```

Example, conditional near-anchor family member:

```bash
python generate_parametric_certificate.py \
  --module ENDPOINT_DOMAIN_LOWER_BOUND_V1 --r 68 --profile near-anchor \
  --output certificates/endpoint_domain_r68_near_anchor.json \
  --receipt certificates/endpoint_domain_r68_near_anchor_receipt.json
```

Example, conditional d1 family member:

```bash
python generate_parametric_certificate.py \
  --module D1_SHELL_CLASS_BOUND_V1 --r 68 \
  --output certificates/d1_shell_class_bound_r68.json \
  --receipt certificates/d1_shell_class_bound_r68_receipt.json
```

The wrapper refuses `r<12` with `BLOCKED_SOURCE_REDUCTION_NOT_APPLICABLE`. The raw legacy generators remain callable for schema tests, but those outputs are not admitted as theorem-level certificates below r=12.

## Boundary audit

Under the baseline `q_cap=3r+2`, the only candidates in the medium interval `4<=d<=r-3` are:

- r=12: d=4 and d=9;
- r=13: d=4 and d=10;
- r=14: d=4 and d=11;
- every r>=15: none.

This is a scalar necessary-condition simplification conditional on RC. It is not a full endpoint closure. Under the strengthened `q_cap=3r-1`, d=4 and its symmetric partner are excluded for all r>=12, but that profile may only be used when RC + ANCHOR_K8 is explicitly retained in the theorem chain.

## Parameter coverage

`PARAMETER_ADMISSION_MATRIX.json` carries explicit rows r=4,...,100 plus a complete range partition for all integers r>=4. `PARAMETER_ADMISSION_VERIFIER.py` independently reconstructs every explicit row, checks the source registry and range partition, and supports query mode for arbitrary r>=4 (including r>100). Its PASS is an admission-policy audit, not an EG617 theorem.


## Low-order recurrence sources do not widen module admission

The front-recurrence branch additionally proves its abstract `M_r(2)` and `M_r(3)` cutoff sublemmas for `r>=6`, while `r=4,5` have abstract-contract counterexamples to the `M_r(2)` cutoff. Its potential theorem proves recurrence termination conditional on a finite sound seed/cutoff package for every `r>3`. These results do not provide a complete reduction from an original EG617 coloring to the recurrence contract. Consequently the endpoint-domain and D1 certificate families remain blocked for theorem-level use below r=12.
