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
Frozen paper source: frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md at
c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2, as attributed in the retained independent
audit. This checkout contains the audit text; the frozen file itself is not present.
No stronger claim of byte-for-byte paper access is made.
