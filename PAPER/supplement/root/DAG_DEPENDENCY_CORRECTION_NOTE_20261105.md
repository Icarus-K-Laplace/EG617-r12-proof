# Proof-DAG dependency correction note

Date: 2026-11-05

## Frozen object and issue

The frozen integration snapshot is `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`. Its `r12_master/workstreams/astra-global-root-integration-chat-20261031/PROOF_DAG.json` has blob SHA `29e88b994f07a540481908fe6f1b18447d39a45b` and 25 nodes. It is syntactically valid and acyclic, but the source-to-DAG crosswalk identifies three load-bearing intermediate results that are separately used in the proof and are not explicit nodes in the frozen graph:

1. `GATE47`: if an actual 47-vertex graph in the relevant R(4,47) class has at most 286 edges, then its minimum degree is at least 12.
2. `D48`: every actual 48-vertex graph in the relevant R(4,48) class has minimum degree at least 12.
3. `SHELL_MATCHING_BOUNDS`: the shell matching lower bounds used in the q20 classification, COVER q29 argument, and recurrence.

The corresponding analytic statements are present in the frozen proof sources; this is a dependency-documentation defect, not a demonstrated missing mathematical implication.

## Required edges

The proposed graph adds:
- `GATE47 <- LOWER_ORDER`, and `R447_FLOOR287` depends explicitly on `GATE47`;
- `D48 <- LOWER_ORDER`, and both `R448_FLOOR310` and `H12_EMPTY` depend explicitly on `D48`;
- `SHELL_MATCHING_BOUNDS <- COLOR_CAPS`, and `Q20_CLASSIFICATION`, `COVER_Q29_GENERAL`, and `RECURRENCE` depend explicitly on `SHELL_MATCHING_BOUNDS`.

It also makes `Q20_CLASSIFICATION` depend on `LOWER_ORDER`, because the q20 shell proof uses the M1 pair-row bound in addition to Turán/cap input.

## Proposed graph check

The proposed JSON is in `PROOF_DAG_CORRECTED_PROPOSAL.json`. On 2026-11-05 it was parsed and checked as a directed dependency graph:
- 28 nodes;
- every referenced parent key exists;
- no directed cycle;
- every node is in the transitive dependency set of `K145_EMPTY`.

This is a graph-structure check only. It does not prove that every mathematical dependency has been identified or that the theorem nodes themselves are correct. The proposal must be reviewed against `GLOBAL_THEOREM_LEDGER.md` and the source proofs before promotion. The frozen integration file was not modified.

## Acceptance boundary

Do not describe the frozen 25-node DAG as semantically complete. Do not describe the 28-node proposal as an accepted replacement until its source crosswalk is reviewed and it is promoted with a new immutable proof snapshot. The full root verifier's DAG check is a syntax/acyclicity check; it does not detect omitted theorem dependencies.
