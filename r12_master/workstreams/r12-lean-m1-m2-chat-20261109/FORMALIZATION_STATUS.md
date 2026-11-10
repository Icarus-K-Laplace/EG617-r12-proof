# Recovery in progress — 2026-11-09

Current acceptance: LEVEL 1 — M1 VERIFIED. Clean Linux run 42620051771 at
commit 64599f21f6d5f43a6c1fc385ee2eedb68525ee45 passed all four M1 modules,
the complete project build, all 47 declaration axiom checks and statement
inspection. The only axiom dependencies are propext, Classical.choice and
Quot.sound. No original mathematical module or candidate theorem statement
was weakened.

M2-A is now in progress. Core.Admissibility states the exact hereditary-cap
contract and develops genuine induced/nonneighborhood helpers. Core.R224
contains a candidate complete proof of the first lower-order parent using
Mathlib's already formalized AES theorem. These 13 additional declarations
are pending actual compilation and audit. GATE47 itself is only a target
definition, not a theorem. LEVEL 2 has not been achieved; M2-B/C/D are pending.

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
