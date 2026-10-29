# Q32 non-full-support sibling import and full-support frontier audit

Updated: 2026-10-29  
Repository: \`Icarus-K-Laplace/EG617-r12-proof\`  
Owning branch: \`workstream/r12-twochat-e408-global-20261026\`  
Write scope: \`r12_master/workstreams/twochat-e408-global-20261026/\`  
Status: **Q32 support 44–46 CLOSED CONDITIONALLY; support 47 OPEN. Root theorem remains OPEN / NOT_CERTIFIED.**

## 1. Read-only sibling source freeze

The current root workstream imported the following sibling states without modifying either sibling:

- Low-support branch \`workstream/r12-q32-caseII-v44-final-20261028\`, HEAD \`9afd7c1a59056052974f9dc78933010d10e88bba\`.
- High-support branch \`workstream/r12-q32-highsupport-root-20261028\`, HEAD \`5f1cccb917f0d13c27f9e3fc2dfa77418dc1abff\`.

The low-support canonical state says all \`|U|=44,45,46\` rows for \`m=8,9,10\` are closed under the registered 285-edge Q32 contract. The high-support canonical state independently records the same closure and then isolates \`|U|=47\` as the only remaining support size.

This is a **conditional proof import**, not a claim that this root workstream independently re-proved every source lemma. No sibling branch was changed by this audit.

## 2. Non-full support status matrix

All entries below are conditional on the exact-129 Type-I source theorem, the registered E408 Q32 residual contract, and the explicitly named Kang–Pikhurko / second-Turán inputs used by the cited local proofs.

| Support \(v=|U|\) | \(m=8\) | \(m=9\) | \(m=10\) |
|---:|---|---|---|
| 44 | CLOSED: direct no-core-only degree-four contradiction | CLOSED: all-double and one-triple zero-shell contradictions | CLOSED: corrected multiplicity \(n_w\ge m-6\) |
| 45 | CLOSED: source-correct weighted special-incidence / 130-edge local obstruction | CLOSED: 130-edge core-only degree-four obstruction | CLOSED: source-correct zero-shell multiplicity |
| 46 | CLOSED: Case I by 130-edge minimum degree four; Case II by surplus budget | CLOSED: 131-edge minimum degree three plus Case-II 130-edge obstruction | CLOSED: Case I degree budget; Case II zero-shell multiplicity |

Source documents and blob IDs:

- Low-support canonical: \`r12_master/workstreams/q32-caseII-v44-final-chat-20261028/CANONICAL_STATE.md\`, blob \`98eac1c7bba8f7e9dd921104b96ffd03dccc5335\`.
- Low-support dependency audit: blob \`2adcded87ae5918eac73d29b9b443e2664887313\`.
- \(v=44,m=8\): \`V44_M8_DIRECT_NO_CORE_ONLY_CLOSURE.md\`, blob \`08ecefa2c9839d4e2864864ae64e91abb7a3f242\`.
- \(v=44,m=9\), all-double / one-triple: blobs \`fedc53b9ed62ce43df905b13e82ab1e3107945a5\` / \`cb666be2aea47b65719f025ab2f2066915e34374\`.
- \(v=45\) full support-layer closure: \`V45_SOURCE_CORRECT_CLOSURE.md\`, blob \`c17acc7171e55246fa67226421c17ced5b8556f7\`.
- \(v=45,46,m=9\): \`V45_V46_M9_CLOSURE.md\`, blob \`8f1e7b65f5857e9d982ebca1bdfe181d49fda5f0\`.
- \(v=46\) Case II: \`V46_CASEII_CLOSURE.md\`, blob \`f1e39bfcd6e335e45a6beab81535d725d605cef9\`.
- Shared local obstruction: \`Q32_130_NO_CORE_ONLY_DEG4.md\), high-support branch blob \`f7dbe22f2af6627c7471068683a3cc839339c1a6\`; low-support sibling carries its own corresponding source blob.

The former degree-nine exceptional-vertex argument and the injectivity-dependent \`Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md\` are **not** used in this import.

## 3. Full support \(v=47\): exact remaining frontier

For all eleven non-target colors on \(H\), the ordinary floor is \(69\) edges. Since \(\binom{47}{2}-285=796\), the exact multicolor gap ledger is

\[
\sum_C g_C=796-11\cdot69=37,\qquad g_C=e_C(H)-69\ge0.
\]

The source-correct exact-color placement theorem gives \(g_C\le6\), with placement-sensitive upper bounds. The pivot-neighborhood packing theorem selects \(m\) pairwise vertex-disjoint independent \(K_4\) blocks \(Q_i\), and \(R=H\setminus\bigcup_iQ_i\) has size \(47-4m\). Its common-pool edge baseline is \(253\), leaving \(32\) units of slack. The audited scalar relaxation remains feasible, so it is not an UNSAT certificate.

The current read-only high-support branch reports:

- \(m=8\): **OPEN** at \(v=47\).
- \(m=9\): **OPEN** at \(v=47\).
- \(m=10\): the subcase \(\chi(\overline{H[R]})\ge5\) is closed by the residual-incidence / light-block analysis. The remaining \(\chi(\overline{H[R]})\le4\) subcase is **OPEN**.

Relevant source blobs:
- High-support canonical at the latest read-only head: a93c934ac128c27e8e518966735c231a62dfdcf3 (branch HEAD 5f1cccb917f0d13c27f9e3fc2dfa77418dc1abff).
- \`V47_ALL_COLOR_RESERVE.md\`: \`c71156c4e08c08146be792796600c5fbfc708cf0\`.
- \`V47_PIVOT_NEIGHBORHOOD_PACKING.md\`: \`10fb644df30419304482dffed89a577be8fc1710\`.
- \`V47_RESIDUAL_INCIDENCE_COVER.md\`: \`8af079fefdc525b26d5be837f638b58f968babc4\`.
- \`V47_LIGHT_BLOCK_GRAPH_DISCONNECTED_REDUCTION.md\`: \`eea5a4cdb80e9111da6861e4eff8b2029d12cf9e\`.
- \`V47_37_RESIDUAL_TRACK_TRANSVERSAL.md\`: \`f02f55cf21d80784b089b25f84c99e76991ef688\`.

The high-support workstream explicitly retracts its former global matching-map rigidity claim; this root import does not use that retracted lemma. Its new full-support CSP remains FORMULATION_ONLY / NOT_EXECUTED and has two source-contract defects recorded in Q32_FULLSUPPORT_CSP_SOURCE_AUDIT.md; no solver output is imported. Local verifiers certify their stated finite arithmetic/label checks only, not the global graph nonexistence.

## 4. Root decision

The Q32 dependency has been narrowed from all support sizes \(44\le v\le47\) to a full-support \(v=47\) terminal, with a further partial closure in the \(m=10\), high-chromatic residual subcase.

\[
\boxed{\text{E408 Q32 remains OPEN / NOT\_CERTIFIED.}}
\]

No root promotion is authorized. The independent E407 V12 parent-coverage gate and E408 Q33 support-promotion gate also remain OPEN.


## 5. Full-support CSP is not yet trusted — 2026-10-29

Latest high-support branch HEAD: 5f1cccb917f0d13c27f9e3fc2dfa77418dc1abff (canonical blob a93c934ac128c27e8e518966735c231a62dfdcf3). New CSP source blobs:
- Q32_FULLSUPPORT_VERTEX_LABELLED_CSP.md: 6bc7ebec290fd204111fdf7877ab63319184449b.
- q32_fullsupport_vertex_labelled_csp.py: 7602fda163700c4e482edc1fac963faa484b46bd.
- verify_q32_fullsupport_candidate.py: fc6c8a5e2b2e8decd236f0d7336699c23f75be1f.

The independent audit found the target-edge count mismatch for m=8,9 and the verifier's overrestriction on the first ten factor outside counts. The sibling progress log explicitly states the CSP is not executed. These are preventive formulation findings; no SAT/UNSAT result is retracted because none is claimed.
