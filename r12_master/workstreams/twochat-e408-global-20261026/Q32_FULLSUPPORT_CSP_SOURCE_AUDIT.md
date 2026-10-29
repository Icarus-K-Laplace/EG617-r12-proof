# E408 Q32 full-support CSP — source-contract audit

Date: 2026-10-29  
Auditing branch: workstream/r12-twochat-e408-global-20261026  
Read-only source branch: workstream/r12-q32-highsupport-root-20261028  
Audited sibling HEAD (historical): 92c9086c8b6ac554ed74b48a5d608aa546bcb977  
Latest sibling HEAD rechecked: c6500b24dc78cd4c56cd90219080003aeb8e3cb5  
Status: **ONE FORMULATION DEFECT REMAINS; no solver result exists to certify or retract.**

**Supersession note (2026-10-29):** the old Section 3 / Section 5 source-mode verifier defect has been fixed in the latest sibling revision. The remaining load-bearing defect is the target/non-target edge-count vector for m=8,9.

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
