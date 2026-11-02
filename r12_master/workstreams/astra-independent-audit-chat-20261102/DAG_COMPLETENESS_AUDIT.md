# Proof-DAG completeness audit

Date: 2026-11-02
Integration snapshot audited: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`
Audit branch: `workstream/r12-astra-independent-audit-20261102`

## Result

The stored `PROOF_DAG.json` has 25 nodes, all parent references resolve, and the graph is acyclic. This verifies graph syntax and acyclicity only. A crosswalk against `GLOBAL_THEOREM_LEDGER.md` shows that the DAG does not explicitly represent two load-bearing theorem nodes that the ledger itself lists separately:

1. **GATE47** — every (R(4,47)) graph with (ele286) has minimum degree at least 12.
2. **D48** — every (R(4,48)) graph has minimum degree at least 12.

This is a dependency-documentation/completeness defect in the published DAG, not a demonstrated counterexample to the mathematical proof.

## Evidence from the proof text

### GATE47

`GLOBAL_THEOREM_LEDGER.md` has a separate row:

> GATE47: Every R(4,47) with e<=286 has delta>=12.

The source is `frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md`, Theorem M, especially M6. The final theorem then uses this gate before the 285-edge augmentation theorem and the 286-edge equality exclusion to infer the strict 287-edge floor. `FINAL_GLOBAL_PROOF.md` says exactly: “The low-edge gate plus 286 exclusion imply e(C)>=287.”

But the DAG has:
- `R447_FLOOR287: [LOWER_ORDER, ABSTRACT_LOW285, ABSTRACT_286]`
- no `GATE47` node and no edge from `R447_FLOOR287` to it.

If the author intended `LOWER_ORDER` to include M6, that conflicts with the theorem ledger, which separates M1–M5 (`LOWER`) from `GATE47`. The crosswalk must make this explicit.

### D48

`GLOBAL_THEOREM_LEDGER.md` separately lists:

> D48: Every R(4,48) graph has delta>=12.

The source is `H12_AND_EXCEPTIONAL_PARENT_AUDIT.md`, Section 1. This result is used:
- to exclude the q=20 equality family by the inserted-center repivot argument (Sections 2–3);
- to ensure every repivoted 48-core in the T61 h=12 proof still has minimum degree 12 (Section 5).

But the DAG has:
- `R448_FLOOR310: [LOWER_ORDER, CORE211, Q20_CLASSIFICATION]`
- `H12_EMPTY: [R448_FLOOR310, LOWER_ORDER, Q20_CLASSIFICATION]`
- no `D48` node or corresponding dependency edge.

The 310-edge floor proof itself also invokes Section 1's D48 gate before applying the Q20 shell argument. Therefore the D48 dependency should be explicit both in the R448 floor proof node and in H12 closure (unless a documented theorem node is deliberately defined to package both statements).

## Suggested corrected dependency fragment

The following is a proposal only; it does not edit the frozen integration branch:

```json
{
  "GATE47": ["LOWER_ORDER"],
  "R447_FLOOR287": ["GATE47", "ABSTRACT_LOW285", "ABSTRACT_286"],
  "D48": ["LOWER_ORDER"],
  "R448_FLOOR310": ["D48", "CORE211", "Q20_CLASSIFICATION"],
  "H12_EMPTY": ["D48", "R448_FLOOR310", "Q20_CLASSIFICATION"]
}
```

The exact lower-order and cap dependencies should be expanded if the ledger chooses atomic nodes rather than packaged theorem nodes. In particular, `D48` is not a consequence of `R448_FLOOR310` alone: the latter is an edge-count conclusion, while the inserted-center argument needs the minimum-degree statement for every repivoted 48-core.

## Verifier limitation

`INDEPENDENT_VERIFIER.py::verify_dag` checks only:
- every referenced parent key exists;
- no directed cycle occurs;
- the number of visited nodes.

It does not compare DAG nodes with the theorem ledger, test that every proof-text citation has a represented dependency, or verify the theorem statements. Thus the verifier's `ACYCLIC` result is accurate but insufficient to certify dependency completeness.

## Other crosswalk notes

- `BROOKS`, `TURAN`, `AES`, and `SECOND_TURAN` appear as explicit DAG leaves but do not have separate theorem-ledger rows with their precise statements and application hypotheses. Their uses are described in the frontend/COVER documents, but a complete ledger should map each external leaf to its exact citation and local use.
- `Q32` and `Q33` are ledger rows but are marked “not needed separately” because the 285/low-edge route supplies the needed floor. They need not be load-bearing DAG nodes.
- `GEN49` is explicitly OPEN and outside the K145 dependency path; this is correct.
- The 25-node DAG remains acyclic after adding the two proposed theorem nodes and edges, but acyclicity should be rerun after the integration authors make a revision.

## Certification impact

No mathematical counterexample has been found in the reviewed dependency chain. However, the claim that the 25-node DAG is a complete representation of every load-bearing theorem dependency is not yet supported by the ledger crosswalk. The K145 proof should be described as a strong proof package under active independent audit, not as having passed a complete dependency-closure certification.


## Additional dependency ambiguity: Q32 and SECOND_TURAN

The frozen `UNIVERSAL_Q32_THEOREM.md` and its audit describe the 25-point common-neighborhood bound as using Kang–Pikhurko Theorem 1 at (n=25,r=2). The integration package separately vendors `COMMON_NEIGHBORHOOD_CAPACITY.md`, which gives an elementary shortest-odd-cycle/Mantel proof of the same 145-edge bound without the general second-Turan theorem.

The current DAG has `SECOND_TURAN -> CONTEXTUAL49_EMPTY`, but no `SECOND_TURAN -> ABSTRACT_LOW285` edge. This is correct only if the elementary 25-point derivation is the route actually used for the 285-edge theorem. If the published theorem is invoked, add the missing edge. The proof ledger/source map should identify the chosen route explicitly.


## Theorem-ledger to DAG crosswalk

| Ledger node | Current DAG mapping | Audit note |
|---|---|---|
| CAP | `COLOR_CAPS` | Explicit |
| LOWER | `LOWER_ORDER` | Explicit; this is M1–M5, not the separately listed GATE47 |
| CORE211 | `CORE211` | Explicit |
| LOW285 | `ABSTRACT_LOW285` | Explicit; clarify whether its 25-point bound uses the elementary route or SECOND_TURAN |
| EX286 | `ABSTRACT_286` | Explicit |
| GATE47 | **missing** | Must feed R447_FLOOR287 |
| FLOOR47 | `R447_FLOOR287` | Present, but missing its GATE47 input |
| Q32 / Q33 | no separate node | Ledger says these are not needed separately because LOW285 implies the required floor |
| CTX49 | `CONTEXTUAL49_EMPTY` | Explicit |
| D48 | **missing** | Must feed R448_FLOOR310 and H12_EMPTY |
| Q20 | `Q20_CLASSIFICATION` | Explicit conditional shell theorem |
| FLOOR48 | `R448_FLOOR310` | Present, but missing its D48 input |
| C29 | `COVER_Q29_GENERAL` | Explicit |
| C407/C408 | `COVER_407_408` | Explicit |
| H12 | `H12_EMPTY` | Present, but missing its direct D48 input |
| H13LOW | `H13_E_LE406_EMPTY` | Explicit |
| H13TOP | `H13_E407_EMPTY` and `H13_E408_EMPTY` | Explicit split |
| STOP | `T61_OTHER_DEGREES` and `T61_EMPTY` | Explicit split |
| REPLAY | `RECURRENCE` plus verifier output | Computational evidence; not currently a distinct DAG node |
| K145 | `K145_EMPTY` | Explicit |
| GEN49 | outside the DAG | Correctly OPEN and outside the final dependency path |

The ledger's separate GATE47 and D48 rows make their omission more than a naming preference: the final floor and h12 proof use these results as independent reusable statements. The corrected proposal file adds them explicitly.

External leaves are represented in the DAG but not given separate theorem-ledger rows: `BROOKS`, `TURAN`, `AES`, and `SECOND_TURAN`. A final public proof package should give each leaf its exact cited statement and the local hypothesis check. This is particularly important for the conditional Q32/SECOND_TURAN choice described above.
