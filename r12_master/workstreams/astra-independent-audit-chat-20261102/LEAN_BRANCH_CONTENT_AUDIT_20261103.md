# Repository Lean-artifact provenance check

Date: 2026-11-03

## Scope

Read-only inspection of branch workstream/r12-lean-formalization-20261031 in Icarus-K-Laplace/EG617-r12-proof.

- Branch HEAD: c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2
- Commit date: 2026-10-31T05:14:20Z
- Recursive tree entries: 508

## Observed contents

The branch tree contains:
- **0** files ending in .lean;
- **0** lakefile, lean-toolchain, Main.lean, or MainTheorem paths;
- **0** files under .github/workflows/;
- file extensions in the tree are .csv, .json, .md, .py, .txt, and extensionless files.

Therefore this GitHub branch is not itself a Lean project checkout and cannot serve as evidence of Lean kernel compilation or theorem certification. Its branch name is not evidence of formalization completeness.

## Certification boundary

This finding is limited to the named branch at the stated HEAD. It does not establish that no separate local ZIP, release asset, or untracked working directory contains Lean files. Any such separate package must be audited independently for:
1. the exact original theorem statement and theorem mapping;
2. absence of sorry, untrusted axioms, or weakened assumptions;
3. clean lake build from a fresh extraction;
4. a kernel-checked declaration of the original K145 theorem, not only auxiliary lemmas;
5. reproducible build logs and source hashes.

No Lean certification is claimed by this repository inspection. No branch or source file was modified outside the isolated audit branch.
