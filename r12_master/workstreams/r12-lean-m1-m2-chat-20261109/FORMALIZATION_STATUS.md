# Formalization coverage

LEVEL 1 — M1 VERIFIED, with partial M2 progress. [Actual run](https://github.com/Icarus-K-Laplace/EG617-r12-proof/actions/runs/42953650338); commit ee2dbe9d6d0c5298dc6cfc8a4f8c91e5d8bcdf06. 72 declarations / 53 theorems kernel-verified. Original27/17 plus M1 additions20/16 plus M2 additions25/20. No unverified source is included.

Fully formalized: original K145 definitions and missing-color equivalence; independent/monochromatic bounds; induced Turan-complement bound; unique-color edge partition; cross-color ledger; hereditary D(n); least color and870 edges; exact R(a,n); all hereditary and nonneighbor inheritance; R224 emptiness on any24-vertex type; R337 emptiness on any37-vertex type; R335 degree>=11; R447 degree>=10.

Partially formalized: LOWER and GATE47. GATE47's d<=9 case is excluded, but d10 and d11 are NOT excluded. Gate47Statement is not a proof. These partial degree bounds are named separately and do not replace the sharp frozen statements.

FORMALIZATION GAP: 23-point121/122 classification; low-cost12-set transport; R223>=131; sharp R335 degree12 and R336 degree13; remaining GATE shell cases; LOW285; E286 all ten-orbit completeness/shared-center/blocker/excess proofs; FLOOR47; CORE211; CTX49; D48; Q20; FLOOR48; COVER; h12/h13; E407/E408; STOP; full K145. MainTheorem ABSENT. REPLAY is not a Lean proof. GEN49 remains outside the frozen final path.

No mathematical counterexample to the exact frozen theorem has been established. Failure to finish these proofs is not evidence that the original theorem is false. No full-proof percentage is claimed.

Clean Ubuntu24.04 used the exact official Lean4.35 archive and all nine fixed dependency revisions, with pinned official dependency caches. It rebuilt the project, not all Mathlib from source. The same standalone build-linux.sh is executed by CI. Windows resource failures remain historical, and do not invalidate or substitute for the successful Linux run.
