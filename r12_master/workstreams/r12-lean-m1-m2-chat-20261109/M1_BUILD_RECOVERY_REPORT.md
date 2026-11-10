# M1 recovered — actual Linux kernel verification

Acceptance: LEVEL 1 — M1 VERIFIED.
Commit: `64599f21f6d5f43a6c1fc385ee2eedb68525ee45`.
Run: https://github.com/Icarus-K-Laplace/EG617-r12-proof/actions/runs/42620051771
Complete original output: `logs/linux-42620051771-full.txt`.

Ubuntu 24.04, official Lean 4.35.0 commit
`eb6cafb7290e8bd5f2937522d8d804f58f02bafc`.
The official Linux archive SHA256 was checked before extraction:
`7289597a44543246c9227b8cae501767e095ce17f6d448b95fc4a8dc97268f6d`.
Mathlib remains `56a005855ea17e0b0958f73ec801ae140b0a1679`; all nine actual
dependency Git revisions were compared against the unchanged manifest.

All four modules passed separately: TuranArithmetic, EdgeCounting,
TuranBounds, HereditaryCaps. The whole project then built. All 47 project
declarations passed `#print axioms`, the allowlist and one-report-per-declaration
coverage check, and complete statement inspection. The 20 new declarations
contain 16 proved auxiliary theorems. Standard axiom union only:
propext, Classical.choice, Quot.sound.

Windows failures occurred while loading dependency artifacts. Clean Linux
then exposed actual source issues, fixed without changing theorem statements:
doc-comment placement, dependent induced-graph types, an explicit graph
argument, a dependent edge-set rewrite, normalization of choose(145,2), and
an unsupported audit formatting option. The failed Linux logs are preserved
separately. Neither category is evidence of a mathematical counterexample.

The four original mathematical modules remain byte-identical; all 16 new
theorem statements remain textually identical modulo whitespace to the input.
See `logs/statement-preservation.json`.

The successful run used a fresh hosted runner and pinned official dependency
caches, then cleaned and compiled project proofs. It is not a source rebuild
of all Mathlib. Arithmetic smoke tests are not imported as proof evidence.

M1 proves the paper's initial color-counting layer, not the complete frontend
or K145 contradiction. MainTheorem is absent. Current M2 source additions have
their own pending verification status and do not inherit this PASS.
