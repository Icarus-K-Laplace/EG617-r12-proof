# Independent replay log — Q33 284 core and minimum-degree source

Date: 2026-10-30

## 1. Repository freeze

- Repository: Icarus-K-Laplace/EG617-r12-proof.
- Isolated branch: workstream/r12-q33-v47-excess4-universal-core-attack-20261030.
- Workstream HEAD at source-complete checkpoint: a69e395129096ba693ca2e4daf3dc8d2ae1d5b86.
- Read-only parent root: workstream/r12-twochat-e408-global-20261026 at b0459807acd4b7e386148056ddf77d7998918893.
- All changes were confined to r12_master/workstreams/q33-v47-excess4-universal-core-chat-20261030/.
- No global canonical file or sibling workstream was changed.

## 2. Source archive hashes

- FRONTEND_LINE_A_V1.zip: 8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac.
- BACKEND49_FIRST_PRINCIPLES_AUDIT_V1.zip: 3801a02fa8e9f53b19c5d289d14deb2f9ef7923e8c63497ca829ad998b433315.
- HIGH_LAYER_BACKEND_V8.zip: 8c05b4490a4c0cdaf08be20180902ec2b5e126f5f275c35f2f12ff353bb825da.
- T61_H13_V11.zip: 27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4.

## 3. 127-row rational certificate

The two retained copies of COMPLETION_CERTIFICATE.csv have identical SHA256:
2603ef814d77fb34f2f13569d64ed15ca40bc4c9d9b85518b41e83da8feaecd9.

The two retained copies of verify_completion.py have identical SHA256:
094d2ea62847af6a28fec136ca2990e13ec32f7cb9beaac8a25ea51e7f39ba32.

Both original verifiers were run:
- five_block_v2/core_audit/verify_completion.py -> EXACT_CERTIFICATE_VERIFIED, 127 rows;
- terminal_v1/INPUTS/verify_completion.py -> EXACT_CERTIFICATE_VERIFIED, 127 rows.

Exact table:
- (11,11,11,11): 32 rows, maximum 773/1089;
- (10,11,11,11): 95 rows, maximum 39/44.

No floating-point tolerance is used. The verifier checks exact Fraction inequalities, coverage and uniqueness of all expected rows.

## 4. Independent source-complete replay

Script: Q33_SOURCE_COMPLETE_REPLAY.py.

Command:
python3 Q33_SOURCE_COMPLETE_REPLAY.py --certificate COMPLETION_CERTIFICATE.csv

Observed status: PASS_EXACT_ARITHMETIC_REPLAY.

Checked:
- D(13),D(14),D(23),D(24),D(25),D(37);
- R(2,24) degree/cap arithmetic;
- shortest-odd-cycle/Mantel bounds for 23,25,18 vertices: 122,145,73;
- 121/122 extension-cost arithmetic;
- R(3,35), R(3,36), R(3,37) lower-order floors;
- degree-10 floor 289 and degree-11 floor 287;
- support configurations 9,40,48;
- two mixed 2x2 support matrix classes;
- exact charge minima 6,6,4,5;
- all127 rational rows when the retained CSV is supplied.

The replay is a finite arithmetic check only. It does not certify the analytic classification by graph search.

## 5. V11 package boundary

T61_H13_V11.zip was independently extracted and verify_kernel_certificate.py was run. It reproduced the package's 684 kernel assignments, 349 outside-count states, 259 labelled shells, 252 Family-A and 7 Family-B survivors. This finite kernel replay does not certify all V11 analytic completion claims.

Crucially, no V11 result is used in the minimum-degree proof or Q33 parent contradiction.

## 6. Proof-audit corrections

1. Replaced the former 2+epsilon common-neighbour claim in the universal 284 theorem with the correct 3+epsilon bound proved from the 25-set shortest-cycle/Mantel argument.
2. Repaired the b=5 private-clique capacity proof's displayed residual-set count: the exact lower bound is 21-b+s_i>=25, not merely22. This implies the subsequent t1>=2,t2>=6,t3>=8 bounds.
3. Rewrote the degree-10 minimum-pivot step explicitly via 10+2e(S)+e(S,C)>=100; no clique assumption on S is made.
4. Kept the 127-row certificate's role precise: it certifies the b=3,4 weighted-transversal inequality, not a full graph search.

## 7. Final status

- Minimum-degree theorem J in R(4,47), e(J)<=286 => delta(J)>=12: PROVED.
- Universal 284-edge core nonexistence: PROVED.
- E408 / Qmax=33 parent contradiction: PROVED_CONDITIONAL under the explicit h13 E408 parent contract.
- Full EG617(r=12): OPEN / NOT_CERTIFIED.

## 8. Direct source retention in the isolated branch

The following are now committed inside this workstream:
- COMPLETION_CERTIFICATE.csv (128 lines including header; 127 exact rows);
- verify_completion.py (standalone Fraction verifier);
- VERIFIED_COMPLETION.json (the exact replay output);
- SOURCE_ASSET_MANIFEST.md (archive and source hashes).

The Q33_SOURCE_COMPLETE_REPLAY.py command is now:
    python3 Q33_SOURCE_COMPLETE_REPLAY.py --certificate COMPLETION_CERTIFICATE.csv

The local source archive remains retained in the uploaded file library. The branch's own copy of the CSV is confirmed to have 128 lines and the same final row as the retained archive copy.

## 9. Default-branch write incident and correction

One SOURCE_ASSET_MANIFEST.md create operation initially omitted the explicit branch argument and therefore wrote to the repository default branch. The mistake was detected immediately. The manifest was deleted, then the main ref was force-restored with an expected-head lease to its exact pre-incident parent 278639de8572ffab12fe859d36f776fbb88fc4f0. Thus main's tree and branch history are restored to the observed pre-write state. No global canonical file or sibling workstream file was changed. All subsequent writes explicitly specify the isolated branch. This incident is recorded for audit transparency.


## 10. Clean-room execution actually performed in this turn

See CLEAN_ROOM_REPLAY_20261030.md for the byte-derived archive/source hashes and exact commands. Both original certificate verifiers were executed from the extracted archive in this turn and returned EXACT_CERTIFICATE_VERIFIED (127 rows each). The source arithmetic supplement returned EXACT_ARITHMETIC_SUPPLEMENT_VERIFIED; the Q33 source-complete arithmetic replay returned PASS_EXACT_ARITHMETIC_REPLAY. This is not merely an imported prior-session run report.

The source-complete run checked D(13),D(14),D(23),D(24),D(25),D(37), triangle-free bounds 122/145/73, the degree10/11 floors 289/287, support configurations 9/40/48, the P/D matrix classes, charge minima 6/6/4/5, and the optional exact Fraction replay of all127 rows.
