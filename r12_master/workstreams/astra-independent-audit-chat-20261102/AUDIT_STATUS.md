# Independent EG617(r=12) audit status

Date: 2026-11-02
Frozen Astra integration snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`
Audit branch: `workstream/r12-astra-independent-audit-20261102`

## Findings this round

1. **Finite recurrence replay:** two independently transcribed integer implementations agree at 1,752 nodes, with zero mismatches. All 144 extraction stops were checked; the unique survivor is ((d,j,a,n)=(11,6,5,61)), with bound397 and budget408. See `RECHECK_FRONTEND.py/json`.
2. **Lower-order finite checks:** the M2 type quotient and M3 23-vertex blowup representatives were independently rechecked; 20 compatible type-set pairs, 10 missing-cross-edge cases, and 61 representatives (49 valid, 12 excluded) were obtained. See `RECHECK_LOWER_M2_M3.py/json`.
3. **E286 finite checks:** support orbit counts 2,3,5 and scalar minima were reproduced. See `RECHECK_E286_SUPPORTS.py/json`.
4. **E286 D support:** a previously implicit zero-completer case has been filled by a scalar-charge argument. The proof is recorded separately in `E286_D_SUPPORT_REPAIR.md`. Together with the original sections 3–12, this closes the ten listed support orbits at the analytic-reading level. No counterexample was found. This repair is not Lean-formalized.
5. **Shared-leaf accounting:** the original baseline sentence is imprecise for a vertex missing exactly one point, but the intended inequality is valid. A corrected pointwise derivation is in `AUDIT_NOTES.md`.
6. **COVER beta=12:** the possible circularity in Section9 is resolved. Formula (3) needs the parent core minimum degree12 only; formula (4) needs the repivoted core minimum degree12. The text licenses these at the relevant uses.
7. **h13 COVER q30:** a line-by-line reading of the q30 Family I/II reduction and eliminations found no additional concrete counterexample in this pass. The analytic arguments still require formal/independent peer verification.

## Root-package issues still open

- The 25-node `PROOF_DAG.json` is acyclic and its parent references resolve, but it omits explicit nodes for ledger entries `GATE47` and `D48`. A corrected proposal is in `PROOF_DAG_CORRECTED_PROPOSAL.json`; the frozen integration branch was not modified.
- The Q32 25-point common-neighborhood bound cites SECOND_TURAN in one source, while a self-contained shortest-odd-cycle/Mantel proof is also vendored. The integration source map must identify which route is actually invoked.
- External leaves BROOKS, TURAN, AES, and SECOND_TURAN need exact statement/hypothesis entries in the final theorem ledger.
- No Lean kernel certification of the original K145 theorem is established by this audit. No full clean-room CI run of the integration commit was reported.

## Certification posture

The finite arithmetic and the specific local repairs recorded here have passed this audit session. The K145 proof is **not certified by this report as a whole**: dependency-ledger closure, clean-room build, proof-assistant status, and further independent analytic review remain separate requirements. The global integration branch and all sibling workstreams were left unchanged.
