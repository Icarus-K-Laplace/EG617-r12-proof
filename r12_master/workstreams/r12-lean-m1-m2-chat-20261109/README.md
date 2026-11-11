Download the independent ZIP from releases/EG617-r12-Lean-LEVEL1-R224-R337-20261111.zip in this workstream. The package-only manifest verifier and bundled paper/history references are inside that ZIP. In a Git checkout, run bash build-linux.sh from this directory. The following instructions describe the extracted ZIP.

# EG617(r=12): independent partial Lean formalization

**LEVEL 1 — M1 VERIFIED.** 72 declarations and 53 auxiliary theorems are kernel-verified. R224, R337 and the degree<=9 exclusion for GATE47 are proved. GATE47, E286, the287 floor and the original MainTheorem remain unproved.

Verified code: ee2dbe9d6d0c5298dc6cfc8a4f8c91e5d8bcdf06. [Clean Linux build and full audit](https://github.com/Icarus-K-Laplace/EG617-r12-proof/actions/runs/42953650338). Full output: logs/linux-42953650338-full.txt.

## Toolchain and dependencies

Lean4.35.0 commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc; Lake5.0.0-src+eb6cafb. Mathlib56a005855ea17e0b0958f73ec801ae140b0a1679. All nine manifest revisions are checked during the build; do not run lake update or upgrade them.

| Dependency | Fixed commit |
|---|---|
| plausible | dfa4f38190d07c37e315953e08b90fe2d95b3c24 |
| LeanSearchClient | d6b4c7be5be75ec4917c873ac50c756dc1436372 |
| importGraph | a41f0e9a4dea23188ea9cc1c41ac9f8bbafe0b93 |
| proofwidgets | df72b022e558978a1c50264cfc4d7fec86fa8e04 |
| aesop | 4a174c490d8707121c4a9290800489f105d85e07 |
| Qq | dce0ad79c486cb1fb504af04f953c3466b0c6db8 |
| batteries | 66e469188fe07963e5cf666c7d4433f45b8131c5 |
| Cli | c24fe6078c630e89b489bffe59b3e20ac30d12c8 |
| mathlib | 56a005855ea17e0b0958f73ec801ae140b0a1679 |

## Reproduce on Linux x86_64

Requirements: bash, git, curl, tar with zstd support, sha256sum, Node.js (CI uses24), internet access to GitHub and the official Mathlib cache, and sufficient disk/RAM. The ZIP includes source, not the large toolchain/dependency caches. It does not require this computer, D: paths, or an existing .lake directory.

From the extracted package root, verify the archive contents before building:

```bash
node verify-package.mjs
```

Install the same official toolchain in an empty task-specific directory:

```bash
mkdir -p toolchain
curl -fL --retry 3 https://github.com/leanprover/lean4/releases/download/v4.35.0/lean-4.35.0-linux.tar.zst -o toolchain/lean.tar.zst
echo "7289597a44543246c9227b8cae501767e095ce17f6d448b95fc4a8dc97268f6d  toolchain/lean.tar.zst" | sha256sum -c -
tar --zstd -xf toolchain/lean.tar.zst -C toolchain
export PATH="$PWD/toolchain/lean-4.35.0-linux/bin:$PATH"
set -o pipefail
bash build-linux.sh 2>&1 | tee build-full.txt
```

This exact build script is run by CI: it checks versions and nine dependency pins, preserves config hashes, downloads pinned caches, cleans the project, compiles six modules separately, runs lake build, the source scan, all #print axioms checks and complete statement inspection, then prints SHA256 for each Lean source/config. A source scan PASS alone is never a build PASS.

With dependencies already restored, the minimal project command is `cd lean && lake build`. For complete auditing use the script. The successful CI used a fresh runner and clean project with official caches; it did not rebuild all Mathlib from source. Windows artifact/resource failures are recorded historically; this release certifies the Linux workflow.

## Contents

- lean/: complete standard .lean sources, lakefile.lean, lean-toolchain, lake-manifest.json and audit scripts.
- build-linux.sh: standalone reproducible build; ci/: exact workflow reference.
- DECLARATION_STATEMENTS.md: all declaration source types and per-declaration axioms; logs/statement-inspection.txt: actual elaborated types.
- PAPER_THEOREM_MAPPING.md and FORMALIZATION_COVERAGE.md: exact frozen theorem mapping and remaining gaps.
- AXIOM_AUDIT.md: every transitive axiom report and explicit assumptions.
- logs/: complete successful and failed runs, independent attack outputs and preservation checks.
- paper/: immutable copies of the four specified frozen mathematical references, provenance in RECOVERY_INPUTS.json.
- history/: earlier checkpoint report, not current status.
- provenance/: byte-preserved original input ZIP, including earlier source versions and historical logs; not part of the active build.
- SHA256SUMS and verify-package.mjs: package content checks.

The four original mathematical modules are byte-identical to the verified input, and the16 M1 theorem statements are unchanged; logs/final-preservation.json records the checks. Newly proved partial results do not replace stronger paper statements. Only propext, Classical.choice and Quot.sound occur. No sorry/admit/custom mathematical axiom/native_decide/external oracle is used. MainTheorem is absent; this package does not certify the original EG617(r=12) theorem.
