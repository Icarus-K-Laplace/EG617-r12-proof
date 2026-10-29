# Root audit replay log — 2026-10-29

Target branch at audit start: workstream/r12-twochat-e408-global-20261026  
Target HEAD: 937a905ed26e54ec10e9bdade1d9b655da8f6176  
Target tree: f0875b716df36b1273fa1f6faf0eebaa7f865200  
Status: **FAIL-CLOSED; root remains OPEN / NOT_CERTIFIED**

## Replay 1 — E407 local U-reserve arithmetic

Input contract: |U|=29, 49 pairwise edge-disjoint selected four-set blocks, and e(L_U)<=310.

Independent arithmetic:
- 49*C(4,2)=294;
- p12(29)=5*C(3,2)+7*C(2,2)=22;
- 294+22=316>310.

Result: **PASS for the local arithmetic only**. This does not verify V12 finite coverage or the parent-to-29-point/49-block contract.

## Replay 2 — Q33 high-support reserve arithmetic

The exact source committed as verify_q33_high_support_u_reserve.py was executed in a clean standard-library process:

    python -S -B r12_master/workstreams/twochat-e408-global-20261026/verify_q33_high_support_u_reserve.py

Local replay path during authoring: /mnt/data/verify_q33_high_support_u_reserve.py  
Exit code: 0  
Standard error: empty  
Source SHA256: 9a47974a1e5ac461caa5313e6551b73765a1954102e83ff59ffd540d8851ee66

Actual output:

    E407_LOCAL_RESERVE: p12(29)=22; 49*C(4,2)=294; 316>310 PASS
    Q33_MIN_SUPPORT: p12(31)=26 PASS
    v w f0 f1 h_max eL_upper reserve_upper p12 exclude_by_reserve
    31 16  9 15  4 353  41 26 8,9
    32 15  7 12  5 375  69 28 8
    33 14  5 10  6 398  98 30 -
    34 13  3  8  7 422 128 32 -
    35 12  2  6  8 447 159 34 -
    36 11  1  4  8 472 184 36 -
    37 10  0  3  8 498 210 39 -
    38  9  0  2  8 525 237 42 -
    39  8  0  1  8 553 265 45 -
    40  7  0  0  8 581 293 48 -
    41  6  0  0  8 610 322 51 -
    42  5  0  0  8 640 352 54 -
    43  4  0  0  8 671 383 57 -
    44  3  0  0  8 702 414 60 -
    45  2  0  0  8 734 446 63 -
    46  1  0  0  8 767 479 66 -
    47  0  0  0  8 797 509 69 -
    RESULT: Q33 reserve closes m=8,9 at v=31 and m=8 at v=32 only;
            the scalar reserve alone does not close v>=33, nor m=9,10 at v>=32.
    LIMITATION: arithmetic replay only; no graph realization or parent support promotion certified.

The verifier exhaustively enumerates the 5^3 and 5^4 small overlap profiles for each support size. It does not search for graphs, prove a support-equality theorem, or certify V12.

## Replay 3 — V12 source/manifest/package check

Searched all 30 repository branch trees for T61_H13_V12.zip and V12-related manifest/verifier/certificate names. No matching archive, manifest, or verifier was found. The only V12-named path found is consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md, blob d6868acc40bf69fbbff092d466b60efd95a3afcd, whose status is SOURCE_REPORTED / INDEPENDENT_REPLAY_PENDING.

Additional GitHub checks:
- releases endpoint: 0 releases;
- commit-history query for exact path T61_H13_V12.zip: 0 commits.

Reported archive SHA256 0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36 and certificate SHA256 cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30 remain historical reports. No V12 replay was performed because source bytes and verifier were unavailable.

## Replay 4 — sibling E407 status

Read-only sibling branch workstream/r12-twochat-e407-closure-20261026 at HEAD 0192807d1f3b2193aa65c25b9f671b36821aaded. Its FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md, OPEN_CONTRACTS.md, and PROOF_DEPENDENCY_AUDIT.md remain OPEN / NOT_CERTIFIED. No sibling files were changed.

## Explicit non-claims

- No full graph search or UNSAT certificate was executed.
- No proof-assistant proof was produced.
- No V12 archive replay was performed.
- No degree-nine exceptional-vertex assumption is used.
- No root theorem or Q32 closure is claimed.
