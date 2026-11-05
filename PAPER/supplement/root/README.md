# Supplementary audit and reproducibility materials for EG617(r=12)

This directory records the post-audit clarification of the 47-vertex E286 equality boundary, the pointwise 287-edge core floor, and the 61-vertex h13 COVER Q30 terminal. It is supplementary proof documentation and an audit record; it does not replace the frozen integrated proof.

## Files

- `E286_COVER_INTERFACE_AUDIT_20261103.md`: full interface audit, including source provenance, the exact pivot ledger, the d=2/K4 repivot sequence, the X=3 near-witness, and Family I/II same-parent arguments.
- `H13_Q30_X3_BRANCH_RHO_IDENTITY_20261103.md`: expanded derivation of `rho=9` and `q_y>=31` in the |X|=3 branch.
- `RECHECK_E286_COVER_INTERFACE_20261103.py` and its JSON result: finite support-orbit, scalar-minimum, overlap-inequality and pivot-ledger checker.
- `RECHECK_H13_Q30_X3_BRANCH.py` and its JSON result: finite replay of the 36 positive pair-type distributions in the |X|=3 local charge identity.
- `PROOF_DAG_CORRECTED_PROPOSAL.md/.json`: 28-node dependency-graph correction proposal. It is not yet promoted into the frozen 25-node integration DAG.
- `DAG_DEPENDENCY_CORRECTION_NOTE_20261105.md`: concise explanation of the three omitted dependency nodes and the proposed edges.

## Mathematical interface in one line

For a regular pivot p in a 61-vertex parent F, with the notation of the frozen COVER theorem,
`E=e(F)=91+q_p+e(C_p)`.
Every actual 47-core C_p inherits the parent alpha/omega/cap conditions. The 287-edge floor is applied pointwise to every regular pivot before taking the maximum Q.

## Reproduction

From the repository root:

```bash
python -B PAPER/supplement/root/RECHECK_E286_COVER_INTERFACE_20261103.py
python -B PAPER/supplement/root/RECHECK_H13_Q30_X3_BRANCH.py
```

The saved JSON files are preserved audit outputs. A future release should regenerate them from a clean checkout and compare the resulting mathematical fields. These scripts check bounded arithmetic/finite quotients only; they do not search all 47- or 61-vertex graphs, prove the analytic reductions, execute the full root verifier, or certify the theorem in Lean/Coq.

## Status boundary

- The frozen integrated proof snapshot remains `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.
- The frozen `PROOF_DAG.json` remains unchanged; its semantic dependency map omits explicit `GATE47`, `D48`, and `SHELL_MATCHING_BOUNDS` nodes.
- The corrected 28-node DAG is a proposal pending semantic review and promotion.
- A fresh clean-room run of the complete root verifier has not been completed by this publication-corrections branch.
- No complete Lean kernel proof of the original K145 theorem is claimed.
- External human combinatorics review and journal review remain outstanding.
