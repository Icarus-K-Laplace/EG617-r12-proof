# EG617 r=12 — M2 / GATE47 workstream

This is a partial formalization, not a proof of GATE47 or the original K145 proposition.
The original mathematical definitions and the verified LEVEL 1 source are preserved.
See FORMALIZATION_COVERAGE.md and the full build logs before interpreting any PASS.

Lean: 4.35.0, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc.
Mathlib: 56a005855ea17e0b0958f73ec801ae140b0a1679.
The nine dependency revisions are fixed in lean/lake-manifest.json.
Lake: 5.0.0-src+eb6cafb.

## Reproduce on Linux

Install the exact toolchain named in lean/lean-toolchain. With Git, Node.js,
bash and the matching lake/lean on PATH, from this directory run:

```sh
bash build-linux.sh 2>&1 | tee full-reproduction.log
```

The script downloads the selected Mathlib cache, checks all nine Git revisions,
checks that configuration hashes did not change, cleans the project target,
builds each module, runs `lake build`, prints every project declaration's
transitive axioms, checks the allowlist, prints statements, and emits SHA256s.
For a subsequent ordinary build use `cd lean && lake build`.
No cache or compiled project objects are included in the standalone archive.
Network access is needed for pinned dependencies and the official Mathlib cache.

CI uses Ubuntu 24.04 and a new ASCII directory without .git or .lake; it verifies
the SHA256 of the official Lean archive before extracting it. Its workflow copy
is in ci/. GitHub's root .github/workflows file is the sole user-approved exception
to this workstream's write boundary.

## Structure

- lean/EG617/Basic: original K145 proposition and coloring definitions.
- lean/EG617/Frontend: M1, Turan complement bounds, hereditary D, least color <=870.
- lean/EG617/Core: exact admissibility, R224/R337, odd cycles, edge ledger, R23 reductions.
- lean/EG617/Audit: machine-printable statement and axiom audit entry points.
- logs/: complete CI failures/successes and diagnostic counterexample results.
- attacks/: independent diagnostic programs; their outputs are never Lean premises.
- *_FORMALIZATION.md, *_COVERAGE.md, *_MAPPING.md: explicit completion boundaries.

Windows reproducibility remains limited by the previously documented .ir and
.olean.private failures and memory/disk constraints. Linux CI evidence is reported
separately; a lexical source-scan PASS never means lake build PASS.

Repository branch: workstream/r12-lean-m2-r23-cost12-chat-20261111.
Frozen paper source was read at immutable commit
c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2, path
r12_master/workstreams/astra-global-root-integration-chat-20261031/frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md.
See FROZEN_CLASSIFICATION_SOURCE.md for the four exact branches. The original
frozen file is not edited or required by the standalone Lean build.

Verified checkpoint: 53a7f495d0487672d4ed36e0f572b9d4fe0b0c72;
successful CI: https://github.com/Icarus-K-Laplace/EG617-r12-proof/actions/runs/43793403878.
The standalone build, complete axiom audit and source/config hash comparison passed.
Logs include all failed iterations as well as the complete successful run.
The COMPLETE R23 classification is proved by r23_complete_classification:
C5(10,A,1,1,B), A+B=11, 1<=A,B<=10; a legal single-edge deletion of such a
graph; or C5(9,9,2,1,2). All actual vertex fibers and adjacency are certified.
Universal Cost-6 is proved by r23_cost_six; the R335 nonneighborhood transfer is also verified. Sharp R335/R336 and GATE47 remain open. All195 project declarations and163
theorems were checked; those counts do not imply any unproved parent theorem.

tools/collect-evidence.mjs is a maintainer evidence-extraction utility; its baseline
comparison requires the original Git checkout. It is not needed to build the ZIP.
The SHA256SUMS at the archive root covers every packaged file except itself.
To verify on Linux run `sha256sum -c SHA256SUMS` before building.
