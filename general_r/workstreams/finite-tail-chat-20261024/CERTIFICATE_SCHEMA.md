# Universal Finite-Tail Certificate Interface

The finite-tail pipeline is

`r -> theorem gate -> canonical constraints -> exact finite instance -> certificate -> independent verifier -> theorem promotion gate`.

The solver is never the proof interface by itself. The immutable instance, proof certificate, and tiny verifier are.

## 1. Required metadata for every parameter r

Every certified case must publish the following fields.

```text
statement
r
analytic_reduction_theorem
analytic_source_commit
assumption_ids
instance_schema
instance_profile
instance_sha256
symmetry_specification
certificate_kind
certificate_sha256
producer_tool_and_version
verifier_path
verifier_sha256
replay_command
finite_result
bridge_status
theorem_status
```

`theorem_status=PROVED` is permitted only when `bridge_status=PROVED` and every `assumption_id` in `ASSUMPTION_LEDGER.md` is certified for that same `r`.

## 2. Instance canonicalization

V1 reduced CSP instances use `eg617-finite-tail-csp-v1`:

- integer arithmetic only;
- JSON keys sorted lexicographically for hashing;
- compact separators `(',', ':')`;
- ASCII serialization;
- SHA-256 over the canonical payload, not over incidental pretty-print whitespace.

A changed theorem assumption, q ceiling, variable convention, symmetry rule, or constraint changes the payload and therefore the instance hash.

## 3. Symmetry layers

### Implemented in V1

At the scalar backend level, use the exact involution

`d <-> r+1-d`

whenever both values lie in the legal domain `0<=d<=r`. Search/reporting may keep one orbit representative after checking the full candidate set.

### Required for future graph/SAT adapters

The graph-level adapter must explicitly encode rather than merely describe its quotient:

1. **color permutation** — first fix the least-color role; canonically order all remaining color edge sets;
2. **vertex permutation** — fix the distinguished pivot, then refine shell/core vertices by exact invariant tuples;
3. **canonical labeling** — after invariant refinement, use a deterministic canonical colored-incidence representation;
4. **orbit representatives** — branch only on representatives under the current stabilizer;
5. **degree/support signatures** — include degree sequence, missing-degree sequence, support-class multiplicities, and any already-proved block invariants in the refinement key;
6. **stabilizer witness** — record enough data for the verifier to check that removed branches are genuinely symmetry-equivalent.

Until such a graph adapter and witness checker exist, the fields are marked `reserved`, not `implemented`.

## 4. Certification hierarchy

Use the strongest practical interface in this order.

### A. Analytic proof

Preferred. No solver certificate required. Still record the exact theorem source commit.

### B. Bounded enumeration

Allowed when the final state space is small and a tiny independent program can enumerate every canonical state with exact integer arithmetic. Record the complete canonical-state hash or deterministic generation recipe.

### C. SAT with LRAT/DRAT

Preferred machine route for large Boolean finite tails.

Required artifacts:

- deterministic DIMACS generator;
- documented variable map;
- CNF SHA-256;
- solver proof (`LRAT` preferred when available; otherwise DRAT plus deterministic conversion/checking path);
- independent proof checker invocation;
- no reliance on solver stdout as proof.

### D. Exact ILP certificate

Permitted only when the final infeasibility certificate is independently checkable with exact integers/rationals. Floating-point optimizer logs are not certificates. A Farkas-style rational witness or exhaustive integral branch certificate is acceptable if a tiny verifier checks it.

### E. Lean/Coq final implication

Ideal final layer after the finite certificates stabilize. Formalization should prove the implication from the checked finite certificate plus analytic theorem interfaces, not reimplement an opaque solver.

## 5. Independent verifier rule

The verifier must not simply call the producer or import its search implementation. It should:

- parse the immutable instance/certificate;
- re-derive all cheap formulas independently;
- check hashes;
- check every local proof step or invoke a standard small proof checker;
- return failure on unknown schema/assumption IDs;
- state its scope in the receipt.

`verify_instance.py` follows this rule for the V1 scalar CSP: it does not import `generate_instance.py` and independently re-derives the payload.

## 6. Replay receipt

A successful finite replay should emit a small JSON receipt of the form

```json
{
  "status": "PASS",
  "r": 13,
  "instance_sha256": "...",
  "certificate_sha256": "...",
  "assumptions": ["RC"],
  "finite_result": "UNSAT",
  "bridge_status": "PROVED|OPEN",
  "theorem_status": "PROVED|CONDITIONAL"
}
```

The receipt must never replace the actual certificate.

## 7. Promotion rule

A finite result closes parameter `r` only after the following conjunction is checked:

`analytic reduction for r`

`AND canonical instance exactly represents every surviving analytic state`

`AND symmetry quotient is sound and complete`

`AND machine certificate verifies`

`AND independent replay verifies`

Only then may a row move from `UNVERIFIED/CONDITIONAL` to `CERTIFIED` in the finite-tail matrix.
