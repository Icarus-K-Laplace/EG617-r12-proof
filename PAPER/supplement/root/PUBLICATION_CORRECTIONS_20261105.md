# EG617(r=12): publication corrections uploaded on 5 November 2026

## Staging and provenance

- Publication-corrections branch: `workstream/r12-publication-corrections-chat-20261105`.
- Branch base: `main` at `fb053df9167f5faa91c54771c7b6fe31ca212f04`.
- Frozen mathematical integration snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.
- Source audit branch copied into the supplement: `workstream/r12-astra-independent-audit-20261102` at `9ddb7c0a6282172288ef49c96861cfb93f4fde19`.
- No changes were made to `main`, the frozen integration snapshot, or sibling research branches. This branch has not been merged.

## Corrections made

### Manuscript

`PAPER/main.tex` now:
1. Clarifies that “balanced” means every 13-set contains all 12 colors, not equal color-class sizes.
2. States the exact two-stage 47-core floor: if e(H)<=286, GATE47 gives delta(H)>=12; the low-285 theorem excludes e<=285 and E286 excludes equality, hence e(H)>=287.
3. Distinguishes the E286 equality case (degree excess 8) from a 287-edge core (degree excess 10); the E286 support classification is not applied to the 287-edge COVER core.
4. States the exact parent/pivot identity E=91+q_p+e(C_p), and applies the 287-edge floor pointwise to every regular pivot before taking Q=max q_p.
5. Records the beta-12 repivot identity only in the setting where the old core is known to have minimum degree at least 12. In the E408,Q=30 maximizing-pivot case, e(C_p)=287 and the <=288 gate supplies this hypothesis.
6. Makes explicit the required order in the d=2 K4 branch: first q_y>=29 from EDGE12, then e(C_y)<=288 and delta(C_y)>=12, then inserted-vertex degrees and EDGE13 give the contradiction.
7. Adds the |X|=3 heavy-set identity rho=9 and q_y>=31.
8. States that the Q30 classification is only used under its exact E408, 61-vertex parent contract.
9. Records the DAG and clean-room acceptance caveats, and updates the working-draft date.

The manuscript remains a working draft. Its full proof transcription, references, LaTeX build, and human editorial approval are not complete.

### Supplementary materials

Copied into `PAPER/supplement/root/`:
- full E286-COVER interface audit;
- expanded h13 Q30 |X|=3 rho derivation;
- E286-COVER arithmetic/orbit checker and recorded JSON output;
- h13 Q30 |X|=3 checker and recorded JSON output;
- 28-node corrected DAG proposal in Markdown and JSON;
- this correction log and the supplement README.

### Repository/publication documentation

Updated:
- root `README.md`: exact meaning of “balanced”, current DAG and clean-room caveats, links to the supplement;
- `PAPER/README.md`: supplementary inventory and explicit not-submission-ready status;
- `PAPER/PROOF_SOURCE_MAP.md`: mapping from manuscript claims to frozen sources and new supplementary notes;
- `PUBLICATION/PROOF_STATUS.md`: targeted-audit result and unresolved package-level acceptance items;
- `PUBLICATION/REPRODUCIBILITY.md`: commands and scope for the new finite arithmetic checkers, plus the clean-room boundary.

## Mathematical source crosswalk

| Claim | Frozen source at integration commit |
|---|---|
| E286 equality theorem | `frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md`, blob `e596cdee0ae465a1fe82a8538e991dbc228db235`, lines 5-158 |
| 47-point low-edge/minimum-degree gate | `frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md`, blob `a8151c82da6486b43a735aa3aae64cc5db502b43`, lines 9-135 |
| COVER pivot and repivot identities; q29/q30 terminal | `frozen/cover/COVER_THEOREM.md`, blob `f73c0a331cb22c3e553e679abb24ed65eab004ee`, Sections 1-12 |
| Frozen machine-readable DAG | `PROOF_DAG.json`, blob `29e88b994f07a540481908fe6f1b18447d39a45b`, 25 nodes |
| Theorem dependency ledger | `GLOBAL_THEOREM_LEDGER.md`, blob `a08a0bb0746d58e166df3f85d53f3a9bac178a44` |

## Checks performed for this upload

- The 28-node proposal was parsed: all parent references resolve, the graph is acyclic, and all 28 nodes occur in the transitive dependency set of `K145_EMPTY`.
- Independent finite arithmetic was rechecked: support-orbit counts are 2, 3, 5 (ten total); the |X|=3 branch has 36 positive pair-type distributions, each giving rho=9 and q_y>=31; listed scalar minima were reproduced; the two shared-center inequalities have zero counterexamples on their stated bounded integer domains.
- All changes are staged on the publication-corrections branch. The frozen proof sources remain unchanged.

## What was not done

- The Python files and their previously recorded JSON outputs were copied from the audit branch; the Python scripts were not executed as a fresh clean-room run during this upload.
- The full integrated root verifier was not run from a fresh checkout.
- The LaTeX manuscript was not compiled in a clean TeX environment.
- No Lean/Mathlib kernel proof of the original K145 theorem was produced or certified.
- No external human combinatorics review or journal review was performed.

**Disposition:** the current corrections are uploaded on a reviewable branch. This is not a clean-room acceptance, formal certification, or publication-ready release.
