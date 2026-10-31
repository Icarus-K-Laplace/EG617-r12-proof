# EG617-R12 — The Twelve-Color Case of Erdős Problem 617

> **STATUS: PROVED — fixed parameter $r=12$, by an informal mathematical proof with finite computational verification and an independent AI-assisted certification PASS.**

## Main theorem

**Theorem.** There is no edge-coloring
\[
c:E(K_{145})\longrightarrow\{1,2,\ldots,12\}
\]
such that every 13-vertex subset of $K_{145}$ contains an edge of every one of the 12 colors.

Equivalently, every 12-edge-coloring of $K_{145}$ has a 13-vertex subset whose induced edges omit at least one color.

This proves the fixed $r=12$ case of the Erdős–Gyárfás balanced-coloring conjecture.

**Scope:** This repository claims the fixed $r=12$ instance only. It does not claim that the full conjecture for all $r\ge3$ is solved.

## Start here

1. **Integrated proof:** [FINAL_GLOBAL_PROOF.md](https://github.com/Icarus-K-Laplace/EG617-r12-proof/blob/c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2/r12_master/workstreams/astra-global-root-integration-chat-20261031/FINAL_GLOBAL_PROOF.md)
2. **Independent certification:** [FINAL_CERTIFICATION_REPORT.md](https://github.com/Icarus-K-Laplace/EG617-r12-proof/blob/09a88cc4fe1e2cf1f3a87475d6484f681910b23e/r12_master/workstreams/r12-final-certification-chat-20261031/FINAL_CERTIFICATION_REPORT.md)
3. **Branch and workstream map:** [PUBLICATION/WORKSTREAM_INDEX.md](PUBLICATION/WORKSTREAM_INDEX.md)
4. **Precise theorem status:** [PUBLICATION/PROOF_STATUS.md](PUBLICATION/PROOF_STATUS.md)
5. **Reproducibility:** [PUBLICATION/REPRODUCIBILITY.md](PUBLICATION/REPRODUCIBILITY.md)
6. **Public-release checklist:** [PUBLICATION/RELEASE_CHECKLIST.md](PUBLICATION/RELEASE_CHECKLIST.md)
7. **Manuscript draft:** [PAPER/main.tex](PAPER/main.tex) and [PAPER/README.md](PAPER/README.md)
8. **Manuscript source map:** [PAPER/PROOF_SOURCE_MAP.md](PAPER/PROOF_SOURCE_MAP.md)

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

The precise dependency domains and frozen source provenance are recorded in the integrated proof package and certification report.

## What is not claimed

- The full conjecture for all $r\ge3$ is not solved here.
- The abstract uncolored high-energy $R(4,49)$ problem is not claimed solved; it is not a load-bearing dependency of the fixed-$r=12$ proof.
- No Lean 4/Mathlib or other proof-assistant formalization is claimed complete.
- No external human specialist review or journal acceptance is claimed.

## AI-assisted research and writing

AI systems assisted with mathematical exploration, proof development, computational implementation, independent auditing, and manuscript preparation. AI systems are not authors. The human author(s) remain responsible for mathematical correctness, source attribution, reproducibility, and the final submitted text. Tool-use disclosure will follow the target journal's policy.

## Repository organization

Historical branches are retained for provenance. No historical research line is silently treated as the current canonical proof. See [PUBLICATION/WORKSTREAM_INDEX.md](PUBLICATION/WORKSTREAM_INDEX.md) for the complete remote branch snapshot and exact HEADs.

## Visibility and release

The documentation and manuscript-preparation changes have been merged into main, but repository visibility remains Private. Before making the repository public, complete the security and licensing checklist in [PUBLICATION/RELEASE_CHECKLIST.md](PUBLICATION/RELEASE_CHECKLIST.md).
