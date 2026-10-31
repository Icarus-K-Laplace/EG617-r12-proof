# EG617(r=12) independent certification package

Start with FINAL_CERTIFICATION_REPORT.md. The verdict is **CERTIFICATION=PASS**,
meaning the documented independent informal mathematical audit and finite
replay passed, not proof-assistant formalization or external human peer review.

Read the three analytic certificates in order: LOWER_ORDER_AND_CORE_CERTIFICATE,
COVER_ANALYTIC_CERTIFICATE, FRONTEND_H12_AND_GLOBAL_CERTIFICATE. The obligation
matrix and canonical DAG expose every dependency. The gap register records
failed checks and their repairs instead of suppressing them.

## Reproduction in the repository

Use a full clone of Icarus-K-Laplace/EG617-r12-proof, check out the independent
certification branch, and run from the repository root:

    python -B r12_master/workstreams/r12-final-certification-chat-20261031/INDEPENDENT_REPLAY.py

Python3.12.14 was used; only the standard library and Git are required. The full
clone must contain the pinned integration commit and the recorded originating
commits. The script neither fetches from the network nor writes to source
directories. It writes its result only beside itself, verifies raw Git blobs
independently of checkout newline conventions, and exits nonzero on any failed
subtask. The JSON includes all shell states, all1,752 nodes and all144 stops.
Timing/environment fields and consequently the result SHA256 may vary on rerun;
the mathematical arrays and states are the reproducibility targets.

BUILD_AUDIT_INDEX.py renders the manually written adjudication ledger and source
location index. It is a reporting tool, not a proof checker. Run it only when
changing that ledger. SHA256SUMS.txt authenticates this delivered audit snapshot
and excludes itself. A later rerun changes the recorded results and requires a
new checksum manifest if distributing that new snapshot.

The standalone delivered ZIP also contains the raw pinned integration sources
and supplemental exact285 theorem for reading. Running Git provenance checks
still requires the full repository; the ZIP is not represented as a replacement
for Git history. Source proofs have not been modified by the audit.

Root promotion requires the separate procedure in ROOT_PROMOTION_RECOMMENDATION.md.
