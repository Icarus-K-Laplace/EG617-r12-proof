# E407 V12 root dependency receipt

Date: 2026-10-30  
Workstream branch: `workstream/r12-e407-v12-root-promotion-20261030`  
Base branch: `workstream/r12-twochat-e408-global-20261026`  
Base HEAD at branch creation: `b0459807acd4b7e386148056ddf77d7998918893`  
Dedicated E407 closure branch audited read-only: `workstream/r12-twochat-e407-closure-20261026` at `0192807d1f3b2193aa65c25b9f671b36821aaded`.

## Receipt status

**V12 finite archive/replay gate: PASS.**  
**E407 Q32 parent contradiction: PROVED_CONDITIONAL.**  
**Unconditional E407 closure: NOT ISSUED.**  
**EG617(r=12) root receipt: NOT ISSUED / OPEN.**

## Audited dependency edges

| Edge | Result | Evidence / limitation |
|---|---|---|
| Library V12 source -> exact archive | PASS | `/T61_H13_V12.zip`, 190,249 bytes, SHA-256 `0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36`. |
| Archive -> internal files | PASS | 29/29 SHA entries pass `SHA256SUMS.txt`. |
| V12 input copies -> V11 source archive | PASS | Five V11 source copies match byte-for-byte and match `INPUT_SOURCE_HASHES.json`; V11 ZIP SHA-256 `27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4`. |
| V12 generator/verifier -> finite certificate | PASS | Original `verify_q32_certificate.py` executed successfully from a clean extraction. |
| Independent replay -> finite certificate | PASS | Separate verifier reproduces 8,677 weights, 17,957 count states, 1,984 shells and all per-kernel counts. |
| Screen -> survivor labels | PASS | 90 D3_RHO1, 1,192 NEAR_K12_CAPACITY, 148 K9_PAIR_ROWS, 554 OPEN; zero screen mismatches. |
| OPEN survivors -> A--E templates | PASS | 554/554 unique template labels; all candidate outside-row checks pass; zero failures. |
| E407 Q32 parent -> V12 C0 input contract | CONDITIONAL | Requires the retained E407/Q32 maximum-pivot, hereditary-cap, EDGE13, TRIANGLE25, V8 boundary and lower-order seed hypotheses. The V12 source itself marks C0 CONDITIONAL. |
| Each A--E completion -> 29-point/49-block support object | CONDITIONAL | The global root DAG records the template-to-support interface as `PROVED_CONDITIONAL`; `SUPPORT_BLOCK_ANCHOR_IDENTITY.md` is conditional on the frozen minimum-support boundary and exact-129 factor theorem. The dedicated E407 branch's `FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md` is `OPEN / NOT_CERTIFIED` as a same-core incompatibility proof target; that OPEN status is not itself a refutation of the support interface. The V12 ZIP does not derive `|U|=29`, so MS-29 remains a retained conditional premise. |
| 29-point/49-block support object -> U-reserve contradiction | PROVED_CONDITIONAL | 294 selected edges + 22 edges required by one unselected color = 316, while the core ledger gives at most310. Independent arithmetic replay gap: six. |
| E407 Q32 -> unconditional empty | NOT PROMOTED | MS-29 and retained analytic input edges remain conditional. |
| E407 -> full EG617(r=12) | OPEN | E408 Q32 full support, E408 Q33 support promotion, other root branches and front-end K145-to-T61 bridge remain outside this workstream. |

## Reconciliation of historical status difference

The global root DAG previously recorded V12 as `OPEN` because the archive, manifest and verifier had not been recovered from GitHub and the reported survivor map had not been replayed. The archive is now recovered from Library and the finite enumeration/screen/template mapping is independently replayed. This workstream therefore closes that *artifact/replay* gap.

The old V12 README and `E407_Q32_FULL_CLOSURE.md` correctly say that V12 alone leaves five templates and produces no completed parent graph. The global root's later U-reserve crosscut is a separate conditional theorem. It bypasses the need to solve the five-template simultaneous-core compatibility problem only if the MS-29 support contract is valid for every legal A--E completion.

The dedicated E407 closure branch remains read-only and is not rewritten here. Its `OPEN_CONTRACTS.md` status is not silently changed. This receipt is an independent workstream receipt, not a root proof receipt.

## Root promotion decision

Promote the V12 computation row from `OPEN: source/replay missing` to `COMPUTATION_CERTIFIED under C0`.

Promote the E407 Q32 local contradiction to `PROVED_CONDITIONAL under C0 + MS-29`.

Do **not** mark E407 unconditional `PROVED`, and do **not** issue an EG617(r=12) root receipt.
