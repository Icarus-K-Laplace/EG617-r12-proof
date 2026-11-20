# EG617 E286 / COVER isolated formalization

Branch: workstream/r12-lean-e286-cover-chat-20261118. New results are candidates
until explicitly supported by CI_STATUS.json. Original MainTheorem is absent.

Lean4.35.0, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc.
Mathlib56a005855ea17e0b0958f73ec801ae140b0a1679; all nine dependencies are pinned
in lean/lake-manifest.json. Standard sources and lakefile.lean are in lean/.

With the exact toolchain, Git, Node.js and bash installed:
```
bash build-linux.sh 2>&1 | tee full-reproduction.log
```
The script fetches the pinned Mathlib cache and performs actual lake builds,
complete statement and axiom inspection and source/config SHA256 checks.
For an ordinary subsequent build: cd lean && lake build.

frozen/ contains unedited mathematical source copies, not trusted proof terms.
Their historical PROVED labels are not Lean evidence. logs/ retains full evidence;
attacks/ contains diagnostic tests only. ci/ copies this branch's unique workflow.
The other workstream and frozen repository originals are not modified.

The certified mathematical reduction is e286_actual_support_nine_remaining:
the original five E286 hypotheses imply an actual support configuration among
nine remaining representatives, after the first of the complete ten is excluded.
E286 itself, core47_edge_floor_287, COVER and MainTheorem remain unproved.

Read FORMALIZATION_COVERAGE.md and OPEN_BLOCKERS.md for the exact boundary,
THEOREM_MAPPING.md for frozen-source correspondence, and DECLARATION_STATEMENTS.md
for complete theorem statements. AXIOM_AUDIT.md links the complete per-declaration
audit. No unproved mathematical assumption substitutes for a missing proof.

For the standalone ZIP, verify its files before building with:
```
sha256sum -c SHA256SUMS
bash build-linux.sh 2>&1 | tee full-reproduction.log
```
The ZIP contains every tracked workstream file, full CI logs and a provenance
record. Local drafts, toolchain caches and parallel workstreams are excluded.
Linux CI is the independent clean-build evidence; no Windows build pass is claimed.
