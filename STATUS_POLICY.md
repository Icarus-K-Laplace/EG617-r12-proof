# Proof status policy

Every mathematical asset in this repository must have exactly one status.

- `PROVED` — complete analytic proof from explicitly listed hypotheses.
- `COMPUTATION_CERTIFIED` — finite computation with a reproducible/verifiable certificate.
- `CONDITIONAL` — valid only under explicit unresolved hypotheses or parent contracts.
- `OPEN` — not proved.
- `RETRACTED` — historical claim no longer accepted.

## Rules

1. Historical words such as `CLOSED`, `PASS`, `DONE`, or `UNSAT` do not automatically imply `PROVED`.
2. A proof may use a previous result only if its exact hypotheses match the current branch.
3. Solver infeasibility is not accepted as a mathematical proof unless accompanied by a checkable certificate or an independently reconstructed analytic proof.
4. A local profile closure may not be promoted to a global theorem without a proved classification/completeness argument.
5. Front-end and backend contracts must remain separate. In particular, a backend theorem about `R(4,49)` does not prove the original `K_145 -> residual` bridge.
6. The repository must never state that EG617 `r=12` is solved until every edge in the canonical proof DAG is `PROVED` or `COMPUTATION_CERTIFIED`.
