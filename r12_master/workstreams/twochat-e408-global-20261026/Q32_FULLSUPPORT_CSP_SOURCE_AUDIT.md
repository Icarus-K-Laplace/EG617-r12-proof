# E408 Q32 full-support CSP — source-contract audit

Date: 2026-10-30  
Auditing branch: workstream/r12-twochat-e408-global-20261026  
Read-only source branch: workstream/r12-q32-highsupport-root-20261028  
Audited sibling HEAD (historical): 92c9086c8b6ac554ed74b48a5d608aa546bcb977  
Latest sibling HEAD rechecked: 1de8a37556ba98ccbb8651f39a5192629453f0f1  
Status: **SOURCE CONTRACT RECONCILED; EXECUTION / PROOF REPLAY OPEN.**

**Supersession note (2026-10-30):** both earlier source-contract defects are now fixed in the latest sibling source. The model and independent verifier use the canonical count vector and source-correct outside profiles. The remaining blocker is not a known count-vector defect; it is execution of the full CSP, proof/candidate replay, and the remaining analytic graph cases.

## 1. Fixed E408 edge-count contract

The residual graph is K61, so it has

\[
\binom{61}{2}=1830
\]

edges. The E408 target color has exactly 408 edges; therefore the eleven non-target colors collectively have

\[
1830-408=1422
\]

edges. Under the registered Q32 outer ledger, every non-target color has \(129+s_C\) edges with \(s_C\ge0\) and

\[
\sum_C s_C=3.
\]

If m is the number of exact-129 colors, the only possible excess partitions are:

| m | Non-target edge counts | Target edge count |
|---:|---|---:|
| 8 | \(8\times129,\ 3\times130\) | 408 |
| 9 | \(9\times129,\ 1\times130,\ 1\times131\) | 408 |
| 10 | \(10\times129,\ 1\times132\) | 408 |

## 2. Defect A — model uses the wrong energy family for m=8,9

The sibling CSP q32_fullsupport_vertex_labelled_csp.py and its candidate verifier verify_q32_fullsupport_candidate.py currently set:
- target count \(e_0=398+m\);
- exact colors \(1,\ldots,m\) at 129 edges;
- colors \(m+1,\ldots,10\) at 130 edges;
- color 11 at 132 edges.

The total is internally balanced as a K61 coloring, but it represents target energy \(398+m\), not the fixed E408 contract for m=8,9:

| m | Current model target count | Current non-target total | Required E408 target count | Required non-target total |
|---:|---:|---:|---:|---:|
| 8 | 406 | 1424 | 408 | 1422 |
| 9 | 407 | 1423 | 408 | 1422 |
| 10 | 408 | 1422 | 408 | 1422 |

Thus the model currently covers the correct edge-count vector only for m=10. A future UNSAT result for the current m=8 or m=9 model would not close the corresponding E408/Q32 branch, because the model would exclude the true E408 count vector. The independent verifier repeats the same count mistake, so it does not catch this mismatch.

### Required correction

Keep \(e_0=408\) for all \(m\in\{8,9,10\}\) and encode the non-target counts according to the table in Section 1. With the existing label convention \(1,\ldots,m\) exact, this means:
- \(m=8\): colors 9, 10, 11 each have 130 edges;
- \(m=9\): color 10 has 130 and color 11 has 131 edges;
- \(m=10\): color 11 has 132 edges.

Update the model and the independent verifier independently, then add a regression asserting the full count vector and total 1830 edges for each m.

## 3. Historical defect B — superseded by latest sibling revision

The CSP specification and model allow the twelve Type-I K5 factors to carry the outside incidences permitted by the source-correct normal form:
- \(x_C\in O\): profile \((2,1^{11})\);
- \(x_C\in H\): profile \((2,2,1^{10})\) or \((3,1^{11})\).

The surplus outside incidences need not be confined to \(N_s,N_t\); they may lie in isolated factors. The model correctly enforces that every factor meets O, that the total outside count is 13 or 14 according to \(x_C\), and that each factor's outside count is within the appropriate cap.

However, the independent verifier contains the stricter check:

    for k, block in enumerate(comps[:10]):
        if sum(v in O for v in block) != 1:
            fail(...)

This forces all ten isolated factors to have exactly one O-vertex, contradicting the registered source-mode coverage correction. A legitimate isolated-double placement can be rejected by the verifier. Thus the verifier is not yet a complete verifier for the model's allowed source modes.

### Required correction

Replace the per-factor equality for comps[:10] with checks of the global source-correct outside-count profile:
- all twelve factors meet O;
- when \(x_C\in O\), the multiset is \((2,1^{11})\);
- when \(x_C\in H\), the multiset is \((2,2,1^{10})\) or \((3,1^{11})\).

The independent verifier should reconstruct the source edge set, then validate the factor outside-count multiset without imposing which factor carries the surplus.

## 4. Status and proof firewall

The latest sibling canonical/progress states the CSP is FORMULATION_ONLY / NOT_EXECUTED. No SAT, UNSAT, or Q32 closure is claimed by that branch. This audit is preventive and does not retract a solver result.

The analytic full-support reductions (37-unit gap ledger, pivot-neighborhood packing, residual incidence constraints) are separate proof assets. These CSP defects do not invalidate those analytic lemmas, but they prevent the current solver model/verifier pair from being treated as a complete E408 full-support proof pipeline.

Root status remains:

\[
\boxed{\text{EG617}(r=12):\ \text{OPEN / NOT\_CERTIFIED}.}
\]


## 5. Historical model revision checked at HEAD 92c9086 — superseded

After the pivot-packing integration commit, the model still contains:

    expected_total = {0: 398 + m, 11: 132}
    expected_total.update({c: 129 for c in exact})
    expected_total.update({c: 130 for c in range(m + 1, 11)})

The verifier blob remains fc6c8a5e2b2e8decd236f0d7336699c23f75be1f and retains both the same target-count formula and the comps[:10] exactly-one-O condition. The latest model/spec/verifier source IDs are:
- spec blob 94ce66ee7dcdf4dae6e7af0b9d8141c734eaca4c;
- model blob f8ea9ce29c91876af6b4d51ccfd1a599b1ae1d72;
- verifier blob fc6c8a5e2b2e8decd236f0d7336699c23f75be1f.

The pivot-packing strengthening does not repair either source-contract defect. No full solve has been run.


## 6. Latest sibling recheck — 2026-10-29, HEAD c6500b24dc78cd4c56cd90219080003aeb8e3cb5

### Defect B is fixed at the source-check level

The current verify_q32_fullsupport_candidate.py has source_outside_profile_errors(x, components). It checks that all twelve K5 factors meet O, that the aggregate outside count is 13 when x is outside H and 14 when x is in H, and that the per-factor cap is 2 or 3 respectively. With twelve factors, those bounds force the allowed source profiles (2,1^11), (2,2,1^10), or (3,1^11) without requiring the excess outside vertices to lie only in the special factors. The latest revision also adds self-test fixtures for the source modes. The former comps[:10] exactly-one-O rejection is absent. This closes the old verifier overrestriction, not the graph problem.

### Defect A remains in both current source files

The latest model blob is 22d74be03e7f4e3ce5f48ad8e02f8f9d17c3e663; the latest independent verifier blob is 629be29be020de79bc27b46a338c4966dc53823d. Both still encode target count 398+m and color 11 at 132. For m=8,9, that is not the fixed E408 target count 408.

The exact required vector is:

| m | Target color 0 | Exact colors | Remaining non-target colors | Sum |
|---:|---:|---|---|---:|
| 8 | 408 | colors 1–8: 129 each | colors 9,10,11: 130 each | 1830 |
| 9 | 408 | colors 1–9: 129 each | color 10: 130; color 11: 131 | 1830 |
| 10 | 408 | colors 1–10: 129 each | color 11: 132 | 1830 |

The model and verifier must be changed independently to this exact vector. A suitable model-side construction is:

~~~python
expected_total = {0: 408}
expected_total.update({c: 129 for c in exact})
if m == 8:
    expected_total.update({9: 130, 10: 130, 11: 130})
elif m == 9:
    expected_total.update({10: 130, 11: 131})
else:
    expected_total[11] = 132
~~~

The independent verifier should implement its own explicit vector table, not import or call the model's function.

### Exact arithmetic regression

Added verify_q32_fullsupport_count_vector_contract.py. It verifies for all m=8,9,10:
- all twelve color counts are present;
- target count is exactly 408;
- non-target total is 1422;
- non-target excess over 129 sums to 3;
- total edge count is C(61,2)=1830;
- the old 398+m target formula fails for m=8,9.

Executed locally with python -S -B /mnt/data/verify_q32_fullsupport_count_vector_contract.py; exit code 0. Source SHA256: a8ca2b64593ad808edd57acea710840a76ce04734288bb42d3dbcc1153b8fb27.

This regression certifies count-vector arithmetic only. It does not execute Z3, validate the complete CSP semantics, certify a graph realization, or prove UNSAT. Z3 was unavailable in the current runtime. The high-support sibling remains read-only; no sibling file was changed.


## 7. Latest sibling refresh — 2026-10-29, HEAD c6500b24dc78cd4c56cd90219080003aeb8e3cb5

The high-support branch advanced beyond the prior audited HEAD. Current source hashes are:
- model: 03e4d2ce98ab399ffafa53af016efd3c434150bc;
- independent verifier: 5708b7541b44cfc46bd82cf3d50b1e350472617b;
- CSP specification: 4f73ca96eb43512e94c72f05266462ba949eead4;
- canonical state: ab1148611d5a71d9e38c481a92bc49da474afcd4;
- progress log: 94e3127e3788bc05dc72d6fd080f78e9ad065a4a.

The new revisions harden candidate witness validation and wire the monochromatic-K6 separator into the solver. Inspection still finds the count vector:
~~~python
expected_total = {0: 398 + m, 11: 132}
expected_total.update({c: 129 for c in exact})
expected_total.update({c: 130 for c in range(m + 1, 11)})
~~~
and the independent verifier has the analogous expected_counts logic. Hence m=8,9 still use the wrong target edge count. The count-vector regression from this root workstream passes, but it does not execute the solver. No SAT/UNSAT result or root promotion is claimed.


## 8. Latest sibling recheck — 2026-10-30, HEAD 1de8a37556ba98ccbb8651f39a5192629453f0f1

The current read-only sibling files were re-fetched at the above HEAD:
- model q32_fullsupport_vertex_labelled_csp.py, blob aba51326e4585594e7d87bc2bb0ff6b2a3d7730d;
- independent verifier verify_q32_fullsupport_candidate.py, blob bc29a5fe2b4031ccf6aa3e9eb262ca7318c40343;
- CSP specification, blob 25714d9f9af244aa1af7eb4392cdea5e82b8220c;
- canonical state, blob afa72318cb0626a0e5fa2ca526eba4bd5984f506;
- progress log, blob 5aba23b4fb828bdef5d2a6fc7896b7be18469ae0.

The model imports expected_color_counts(m) from the independent verifier and constrains each color to that vector. The verifier defines:
- m=8: target 408, eight exact colors at 129, three nonexact colors at 130;
- m=9: target 408, nine exact colors at 129, nonexact colors at 130 and 131;
- m=10: target 408, ten exact colors at 129, one nonexact color at 132.

The verifier's source-outside-profile checks and malformed-input guard are present. The model includes lazy independent-set and clique (monochromatic-K6) separation. The branch specification still says FORMULATION ADDED / execution and proof replay pending. The current runtime has no z3, ortools, or pysat; no full solver run, SAT/UNSAT result, or candidate witness is imported.

The earlier sections of this audit document remain as a historical record of defects found in older sibling revisions. They are superseded by this Section 8 and must not be read as a description of the current sibling HEAD.


## 9. 2026-10-30 — z=3 no-double-track partner-fiber blocker

The latest root-side result is recorded in Q32_Z3_SWITCH_PARTNER_DEGREE_BLOCKER.md. It uses the exact 4,5,5 switch normal form from the read-only sibling's V47_THREE_BLOCK_SWITCH_LEMMA.md (blob 5c2decfca14cd8fca834415af9f159240b4237b1) and the zero-slack common small-map alignment. In a synchronized switch with transposition (s j), the vertex q_j receiving two extra small-component edges has k(q_j)=2 and is adjacent to every point of F_j as well as F_s. Therefore d_R(q_j)>=n_s+n_j, while e_Q(q_j)>=2 and e_Q(q_j)+d_R(q_j)=3 force d_R(q_j)<=1. Thus n_s+n_j<=1.

All three nontrivial F/G mismatch profiles from the exact partition-pair enumeration have n_s+n_j equal to 2 or 3, so they are impossible. If F=G, a switch is possible only between an empty fiber and a singleton fiber. The only registered profile with such a pair is (3,3,1,0), but a size-three fiber remains fixed and yields a monochromatic K13. Profiles (3,2,2,0) and (3,2,1,1) are also excluded by K13. Hence the no-double-track m=10, 3+7, z=3 branch reduces to aligned F=G profile (2,2,2,1), with every outer block aligned.

This is not a global Q32 closure. The double-track branch and the aligned-2221 terminal remain open. The full CSP still has no execution/proof-replay result in this runtime.


## 10. 2026-10-30 — correction of the z=3 switch-partner inference

The previous root commit's inference that q is adjacent to every residual r in F_j because both share neighbors A_j,B_j was invalid. Shared neighbors do not imply adjacency. The mismatched-case pointwise inequality n_s+n_j<=1 and its direct contradiction are withdrawn. The normalized 4,5,5 label pattern remains valid, but it does not prove the claimed residual adjacency.

The valid replacement is Q32_Z3_MISMATCH_RESIDUAL_DEGREE_CLOSURE.md. It uses the five-zero-switch/two-aligned-endpoint normal form, equality in y_D>=eta_D, and the residual degree identity. It eliminates 2+1 splits by a K3 degree contradiction and 1+1 splits by either a K2 degree contradiction or an impossible isolated K2 component in C3+P4. For F=G, the existing aligned-case switch blocker is valid and K13 leaves only profile (2,2,2,1).

The earlier Q32_Z3_SWITCH_PARTNER_DEGREE_BLOCKER.md is explicitly retracted. No global Q32 closure is claimed.
