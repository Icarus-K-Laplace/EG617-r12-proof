# EG617-R12 — The Twelve-Color Case of Erdős Problem 617

> **STATUS: The fixed $r=12$ theorem is claimed proved in the pinned informal mathematical proof, with finite computational verification and an independent AI-assisted audit PASS. The proof-DAG correction and fresh clean-room replay remain pending; no Lean kernel certification or external human review is claimed.**

## Main theorem

**Theorem.** There is no edge-coloring
\[
c:E(K_{145})\longrightarrow\{1,2,\ldots,12\}
\]
such that every 13-vertex subset of $K_{145}$ contains an edge of every one of the 12 colors.

Equivalently, every 12-edge-coloring of $K_{145}$ has a 13-vertex subset whose induced edges omit at least one color.

Here “balanced” means that every 13-vertex subset contains all 12 colors; it does not mean that the twelve color classes have equal cardinalities.

This proves the fixed $r=12$ case of the Erdős–Gyárfás balanced-coloring conjecture.

**Scope:** This repository claims the fixed $r=12$ instance only. It does not claim that the full conjecture for all $r\ge3$ is solved.

## Start here

1. **Integrated proof:** [FINAL_GLOBAL_PROOF.md](https://github.com/Icarus-K-Laplace/EG617-r12-proof/blob/c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2/r12_master/workstreams/astra-global-root-integration-chat-20261031/FINAL_GLOBAL_PROOF.md)
2. **Independent certification:** [FINAL_CERTIFICATION_REPORT.md](https://github.com/Icarus-K-Laplace/EG617-r12-proof/blob/09a88cc4fe1e2cf1f3a87475d6484f681910b23e/r12_master/workstreams/r12-final-certification-chat-20261031/FINAL_CERTIFICATION_REPORT.md)
3. **Branch and workstream map:** [PUBLICATION/WORKSTREAM_INDEX.md](PUBLICATION/WORKSTREAM_INDEX.md)
4. **Precise theorem status:** [PUBLICATION/PROOF_STATUS.md](PUBLICATION/PROOF_STATUS.md)
5. **Reproducibility:** [PUBLICATION/REPRODUCIBILITY.md](PUBLICATION/REPRODUCIBILITY.md)
6. **Public-release checklist:** [PUBLICATION/RELEASE_CHECKLIST.md](PUBLICATION/RELEASE_CHECKLIST.md)
7. **Preliminary security scan:** [PUBLICATION/PRELIMINARY_SECURITY_SCAN.md](PUBLICATION/PRELIMINARY_SECURITY_SCAN.md)
7. **Manuscript draft:** [PAPER/main.tex](PAPER/main.tex) and [PAPER/README.md](PAPER/README.md)
8. **Manuscript source map:** [PAPER/PROOF_SOURCE_MAP.md](PAPER/PROOF_SOURCE_MAP.md)
9. **Post-audit supplementary notes:** [PAPER/supplement/root/README.md](PAPER/supplement/root/README.md)

## Frozen proof and audit versions

| Artifact | Pinned commit | Status |
|---|---|---|
| Integrated K145 proof | c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2 | Main theorem stated PROVED |
| Independent certification | 09a88cc4fe1e2cf1f3a87475d6484f681910b23e | CERTIFICATION = PASS |
| Q30 adversarial report | a0f922ad09af99575bae581864b673aa4d41f00d | Q30 = PROVED under its exact E408 parent contract |

The certification is an AI-assisted informal mathematical audit with independent analytic derivations and finite replay. It is not proof-assistant formalization, external human peer review, or journal acceptance. The certification PR is currently an open PR (#1) inviting human review; it has not been merged.

## Proof architecture

The integrated argument proceeds through:

1. The original coloring-to-graph reduction and contextual 61-vertex residual.
2. The 47-vertex universal low-edge obstruction and 286-edge equality analysis.
3. The 48-vertex floor and h12 terminal.
4. The h13 repivot/charge argument and the unified COVER theorem.
5. The complete front-end recurrence and elimination of the unique T61 stop.

The precise dependency domains and frozen source provenance are recorded in the integrated proof package and certification report. The frozen 25-node machine-readable DAG has a known semantic-completeness defect (missing explicit GATE47, D48 and SHELL_MATCHING_BOUNDS nodes); a 28-node correction proposal is included in the publication-corrections branch but is not yet promoted into the frozen proof snapshot.

## What is not claimed

- The full conjecture for all $r\ge3$ is not solved here.
- The abstract uncolored high-energy $R(4,49)$ problem is not claimed solved; it is not a load-bearing dependency of the fixed-$r=12$ proof.
- No Lean 4/Mathlib or other proof-assistant formalization is claimed complete.
- No external human specialist review or journal acceptance is claimed.


## Post-audit package status (5 November 2026)

A targeted audit found no hybrid counterexample or load-bearing interface
gap in the E286 equality -> 287-edge floor -> COVER Q30 chain. The manuscript
and supplement now record the exact pivot identity
`E=91+q_p+e(C_p)`, the pointwise use of the 287-edge floor, the d=2 K4
repivot order, the h13 Q30 |X|=3 identity `rho=9`, and the same-parent
Family I/II arguments.

The frozen dependency DAG still needs correction: its 25-node version omits
explicit GATE47, D48 and SHELL_MATCHING_BOUNDS nodes. The 28-node proposal is
included in the supplementary package but has not yet been promoted. The
full integrated root verifier has not yet been rerun from a fresh clean
checkout. The fixed-r12 result is an informal mathematical proof with
finite computational support; it is not Lean-kernel certified, externally
peer-reviewed, or journal-accepted.

The publication-corrections work is staged on
`workstream/r12-publication-corrections-chat-20261105` and has not been
merged into `main`.

## AI-assisted research and writing

AI systems assisted with mathematical exploration, proof development, computational implementation, independent auditing, and manuscript preparation. AI systems are not authors. The human author(s) remain responsible for mathematical correctness, source attribution, reproducibility, and the final submitted text. Tool-use disclosure will follow the target journal's policy.

## Repository organization

Historical branches are retained for provenance. No historical research line is silently treated as the current canonical proof. See [PUBLICATION/WORKSTREAM_INDEX.md](PUBLICATION/WORKSTREAM_INDEX.md) for the complete remote branch snapshot and exact HEADs.

## Visibility and release

The documentation and manuscript-preparation changes have been merged into main, but repository visibility remains Private. Before making the repository public, complete the security and licensing checklist in [PUBLICATION/RELEASE_CHECKLIST.md](PUBLICATION/RELEASE_CHECKLIST.md).
