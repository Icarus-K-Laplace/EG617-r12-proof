# E408 Q32 full-support CSP — source-contract audit

Date: 2026-10-29  
Auditing branch: workstream/r12-twochat-e408-global-20261026  
Read-only source branch: workstream/r12-q32-highsupport-root-20261028  
Audited sibling HEAD: 5f1cccb917f0d13c27f9e3fc2dfa77418dc1abff  
Status: **FORMULATION DEFECTS FOUND; no solver result exists to certify or retract.**

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

## 3. Defect B — candidate verifier overrestricts Type-I outside placements

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
