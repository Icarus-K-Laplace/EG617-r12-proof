# Clean-room replay record — Q33 minimum-degree and 284-core source gate

Date: 2026-10-30  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-q33-v47-excess4-universal-core-attack-20261030  
Write scope: r12_master/workstreams/q33-v47-excess4-universal-core-chat-20261030/

## 1. Raw archive identity

The four uploaded archives were extracted in a clean working directory and their SHA256 values recomputed from bytes:

| Archive | Recomputed SHA256 | Expected | Result |
|---|---|---|---|
| FRONTEND_LINE_A_V1.zip | 8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac | same | PASS |
| BACKEND49_FIRST_PRINCIPLES_AUDIT_V1.zip | 3801a02fa8e9f53b19c5d289d14deb2f9ef7923e8c63497ca829ad998b433315 | same | PASS |
| HIGH_LAYER_BACKEND_V8.zip | 8c05b4490a4c0cdaf08be20180902ec2b5e126f5f275c35f2f12ff353bb825da | same | PASS |
| T61_H13_V11.zip | 27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4 | same | PASS |

Only FRONTEND_LINE_A_V1 supplies the lower-order source used by the minimum-degree theorem. The other archives were hash-checked as provenance/context; BACKEND49 and HIGH_LAYER are not theorem dependencies, and V11 is explicitly not used.

## 2. Internal source hashes recomputed

| Source | SHA256 |
|---|---|
| SOURCES/S31_AUDIT/STRICT_DESCENT_PROOF.md | d91e44a2d9a9cf17d8766f9b0b3c442d8e6bb0818b45a9657618c9119fc306ae |
| SOURCES/S31_AUDIT/SEED_AND_CORE_AUDIT.md | ed2c98b85c82ce7ed439506b6828593639face53c87b2a78225dcba2f84565bc |
| core_audit/SEED_NEIGHBOURHOOD_EXCERPT.md | b287b12026c4e7968d8acd1800c570b6c4ea2a2aaedd24f5083396da0a466ec0 |
| core_audit/SEED_TRIANGLE_FREE_EXCERPT.md | 713b2163617650ee96e7e315f02a273a4873b8e87843e4ca90149991f007ef33 |
| core_audit/SEED_MIN_DEGREE_EXCERPT.md | 21f00e2409446424518b035eef436cc33bb0a732ab94849c98909307bc4de98f |
| core_audit/CORE_FLOOR_284_PROOF.md | 0ebf37349c7e1c9fdfef54c95b9cb42363b9daa6c32e870cc9a4b5eca5bb837d |
| core_audit/COMPLETION_CERTIFICATE.csv | 2603ef814d77fb34f2f13569d64ed15ca40bc4c9d9b85518b41e83da8feaecd9 |
| core_audit/verify_completion.py | 094d2ea62847af6a28fec136ca2990e13ec32f7cb9beaac8a25ea51e7f39ba32 |

The five-block-v2 and terminal-v1 copies of the 127-row CSV have identical hashes. Their verifier copies also have identical hashes.

## 3. Exact execution

The following commands were executed with Python 3 against the extracted archive:

~~~bash
python3 FRONTEND_LINE_A_V1/SOURCES/S31_AUDIT/inputs/five_block_v2/S31_FIVE_BLOCK_TERMINAL_CLOSURE_V2/core_audit/verify_completion.py
python3 FRONTEND_LINE_A_V1/SOURCES/S31_AUDIT/inputs/terminal_v1/S31_TERMINAL_BLOCK_CLOSURE_V1/INPUTS/verify_completion.py
python3 FRONTEND_LINE_A_V1/SOURCES/S31_AUDIT/verify_audit.py
python3 Q33_SOURCE_COMPLETE_REPLAY.py --certificate FRONTEND_LINE_A_V1/SOURCES/S31_AUDIT/inputs/five_block_v2/S31_FIVE_BLOCK_TERMINAL_CLOSURE_V2/core_audit/COMPLETION_CERTIFICATE.csv
~~~

Observed outputs:

1. Both original rational verifiers: EXACT_CERTIFICATE_VERIFIED, rows=127.
   - (11,11,11,11): 32 rows, maximum 773/1089.
   - (10,11,11,11): 95 rows, maximum 39/44.
2. Original source audit verifier: EXACT_ARITHMETIC_SUPPLEMENT_VERIFIED.
   - d3_parameter_rows=15;
   - d3_defect_rows=25;
   - d10_coupling_rows=4;
   - strict_descent_status=PROVED_FOR_EXPLICIT_PARENT_CLASS;
   - original_K145_bridge=OPEN.
3. Q33 source-complete replay: PASS_EXACT_ARITHMETIC_REPLAY.
   - Density caps checked: D(13)=67, D(14)=69, D(23)=132, D(24)=144, D(25)=146, D(37)=237.
   - Triangle-free shortest-cycle bounds checked: 23 -> 122, 25 -> 145, 18 -> 73.
   - R(3,35) extension charge maximum: 6.
   - Degree-10 floor: 289.
   - Degree-11 floor: 287.
   - Support multiset counts: 9, 40, 48.
   - Mixed support matrix classes: (0,2,2,0) and (1,1,1,1).
   - Exact charge minima: 6, 6, 4, 5.
   - Optional exact Fraction replay of all 127 certificate rows passed.

## 4. Mathematical scope of the replay

The 127-row certificate is COMPUTATION_CERTIFIED for one precise finite rational inequality: the weighted-transversal averaging lemma in the 47-vertex private-clique argument when the four clique sizes are 11^4 or (10,11,11,11) and total degree excess is at most two.

It is not a full-graph search, not an UNSAT certificate, and not an input to the minimum-degree implication
\[
J\in\mathcal R(4,47),\ e(J)\le286\Longrightarrow\delta(J)\ge12.
\]
That implication is proved analytically by the independent R(2,24), R(3,35), R(3,36), R(3,37) chain and the degree 9/10/11 pivot arguments.

The R(3,35) 121/122-edge neighbourhood classification is an analytic argument reproduced in SEED_NEIGHBOURHOOD_EXCERPT.md and summarized in SEED_AND_CORE_AUDIT.md. The finite scripts check its arithmetic bounds and the 127-row certificate; they do not replace the type-classification proof.

## 5. Status

- Archive/source identity: COMPUTATION_CERTIFIED.
- 127-row rational certificate: COMPUTATION_CERTIFIED.
- R(2,24) and R(3,35) minimum-degree seed chain: PROVED for the explicit hereditary-cap class.
- Minimum-degree source gate for R(4,47), e<=286: PROVED.
- Universal 47/284 nonexistence: PROVED by its analytic proof.
- E408/Qmax=33 parent contradiction: PROVED_CONDITIONAL under the exact T61 h13 parent contract.
- Original K145 bridge and global EG617(r=12): OPEN / NOT_CERTIFIED.


## 6. V11 finite-kernel boundary check (not a theorem dependency)

For completeness, the T61_H13_V11.zip finite verifier was also executed:
~~~bash
python3 T61_H13_V11/verify_kernel_certificate.py
~~~
It returned COMPUTATION_CERTIFIED with 684 kernel-weight assignments, 349 outside-count states, 259 labelled necessary shells, 252 Family-A and 7 Family-B survivors, and zero actual completed graphs claimed. Certificate SHA256: 0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b.

This only replays the finite kernel-coverage computation. The completion exclusions are separate analytic proofs. No V11 conclusion is used in either the minimum-degree theorem or the Q33 284-core contradiction.
