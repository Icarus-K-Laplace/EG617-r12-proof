# Recovery in progress — 2026-11-09

Current acceptance: not yet LEVEL 1. The earlier LEVEL 0 environment blocker
has been bypassed on clean Linux. Run 42618394534 at commit 9871b65 compiled
TuranArithmetic and EdgeCounting successfully. TuranBounds exposed an omitted
explicit graph argument and a dependent-type rewrite error. These are
FORMALIZATION GAP, not mathematical counterexamples. The latest repair uses
an explicit edge-set partition without changing any theorem statement.
TuranBounds and HereditaryCaps, followed by the full axiom/type audit, remain
pending. M2 has not been started.

The previous baseline has 27 declarations and 17 verified auxiliary theorems.
The M1 candidate adds 20 declarations including 16 theorem candidates.
No MainTheorem exists. No conclusion about correctness or falsity of the
original EG617 proof follows from an environment failure.

The exact available input and branch/frozen source identities are recorded
in RECOVERY_INPUTS.json. The separately named `(2).zip` was not found; its
identity with the available archive is not asserted.

Work is isolated to this workstream and the dedicated CI workflow on branch
workstream/r12-lean-m1-m2-chat-20261109. The frozen mathematical files and main
branch are not modified.
