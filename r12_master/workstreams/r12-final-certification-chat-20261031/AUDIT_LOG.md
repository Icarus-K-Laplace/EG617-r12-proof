# Independent certification log

Audit date: 2026-10-31, Asia/Shanghai. Commissioned mathematical audit by Codex;
not an external journal review, not a proof-assistant formalization.

## Round 1 — provenance, foundational algebra and clean-room finite replay

Source HEAD is c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2. Its parent is
c6c17bb6b1fee0e350fd0ff649680333f30c9f88, whose parent is original Global Root
b0459807acd4b7e386148056ddf77d7998918893. GitHub compare reports ahead by 2,
behind by 0, 48 files added, all confined to the integration workstream.
Main is 278639de8572ffab12fe859d36f776fbb88fc4f0. All 41 initial branch heads
were queried using git ls-remote, in addition to GitHub connector checks.
Certification branch was created at the pinned integration commit.

Actually read: COVER proof and verifier, minimum-degree gate M1–M6, direct
low-edge proof, capacity and augmentation proofs, 286 equality proof, h12
proof, frontend proof and recurrences, h13 certificates, final proof, ledger,
energy inventory, manifest and dependency DAG. External AES and second-Turan
original statements were retrieved; Brooks original reprint was retrieved.

Mathematical derivations checked: exact shell and repivot identities; alpha
inheritance; deficient-clique implication; licensing of beta=11 versus beta=12;
safe augmentation under the five abstract assumptions; pointwise excess
allocation before summing shared-clique contributions. Full written derivations
and the final disposition are separate deliverables, not implied by this log.

Execution 1: recurrence agrees at 1,752 nodes with both reference programs and
retained data; one outer survivor d=11,j=6,n=61, floor397,budget408. Independent
Q27/Q28 enumeration gives 2/8 states and 81,920 subset checks. Support orbits
are 2/3/5. The initial integrity check FAILED because checkout converted LF
to CRLF (system core.autocrlf=true). No theorem was falsified by that failure.

Repair: hashes are now computed from raw git show bytes, each checkout file is
also checked to differ only by LF-to-CRLF conversion. The rerun passed integrity
and every completed finite subtask. Original workstream files were not edited.

Remaining after this round: lower-order family replay, q20 replay, full analytic
obligation matrix, adversarial classification audit, final certification decision.
No root promotion is authorized by intermediate computational results.

The exact commits containing this log are available from git history; a commit
cannot truthfully contain its own future hash.
