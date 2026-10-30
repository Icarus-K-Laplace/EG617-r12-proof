# Canonical state — E407 V12 recovery and root promotion

Date: 2026-10-30  
Repository: `Icarus-K-Laplace/EG617-r12-proof`  
Branch: `workstream/r12-e407-v12-root-promotion-20261030`  
Exclusive write directory: `r12_master/workstreams/e407-v12-root-promotion-chat-20261030/`  
Base: `workstream/r12-twochat-e408-global-20261026` at `b0459807acd4b7e386148056ddf77d7998918893`.

## Current status

- **V12 archive recovered:** PASS. Original ZIP restored from ChatGPT Library; SHA-256 matches the historical report.
- **Internal integrity:** PASS. 29/29 files verify against `SHA256SUMS.txt`.
- **V11 source lineage:** PASS. All five V11 source copies match the recovered V11 archive byte-for-byte and match the V12 source manifest.
- **Original verifier:** PASS. Re-executed from a clean extraction.
- **Independent verifier:** COMPUTATION_CERTIFIED. Independently reproduces 8,677 weights, 17,957 count states, 1,984 necessary shells, screen partition 90/1,192/148/554, and all per-kernel totals.
- **Survivor mapping:** PASS. All 554 OPEN survivors map uniquely to one of A--E; all outside-row pattern checks pass.
- **U-reserve arithmetic:** PROVED_CONDITIONAL. 294 selected edges + 22 required by one unselected color =316, exceeding the 310 edge cap by six.
- **E407 Q32 parent promotion:** PROVED_CONDITIONAL under the retained V12 C0 hypotheses and the MS-29 29-point/49-block template-to-support contract.
- **Unconditional E407 closure:** NOT PROMOTED.
- **EG617(r=12) root:** OPEN / NOT_CERTIFIED.

## Key finding

The global root's historical V12 `OPEN: source/replay missing` row is superseded for the finite artifact/replay gate: the original archive was in Library, not in the inspected GitHub branch trees. The finite certificate and full survivor-to-template mapping are now independently replayed.

The archive itself still stops at five necessary templates and explicitly reports zero completed parent graphs. The 29-point support set U is a separate parent bridge, not a consequence of the 13-vertex finite enumeration. Until MS-29 is proved or its exact source theorem is attached and audited, the parent promotion remains conditional.

## Workstream artifacts

- `V12_ARCHIVE_INVENTORY.md`
- `V12_HASH_AUDIT.md`
- `V12_INDEPENDENT_REPLAY.md`
- `V12_INDEPENDENT_REPLAY.json`
- Independent replay source (downloadable companion artifact; SHA-256 recorded in `V12_INDEPENDENT_REPLAY.md`)
- `V12_SURVIVOR_COVERAGE.md`
- `V12_SURVIVOR_TEMPLATE_RANGES.json`
- `E407_PARENT_PROMOTION_THEOREM.md`
- `E407_ROOT_DEPENDENCY_RECEIPT.md`
- `verify_u_reserve_independent.py`
- `OPEN_CASES.md`

The original V12 ZIP remains in Library at `/T61_H13_V12.zip` (file ID `file_00000000fa1881f4bfbef443ae0fe03d`); it is not duplicated into this branch. The independent verifier accepts a local ZIP path with `--archive`.

## Next load-bearing task

Prove the MS-29 bridge: every legal A--E completion admits the common 29-point U carrying the 49 pairwise-linear selected support blocks. Reconcile the C0 lower-order seed status. Only after those dependencies close should the global root DAG be updated.
