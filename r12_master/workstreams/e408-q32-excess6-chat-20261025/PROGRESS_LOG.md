# Progress log — E408 Q32 / 285-edge / excess-six

## 2026-10-25 — isolated workstream initialization and independent branch intake

Created branch workstream/r12-e408-q32-excess6-20261025 from ultimate-closure head 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40. All writes are confined to r12_master/workstreams/e408-q32-excess6-chat-20261025/.

Read-only sibling heads checked:
- emergency sprint: f4c3b06891d29238d4f9cca2588f442004b6dc97;
- emergency-sprint continuation: 5258c5fe17af3bf17eb7a2bfb08315c9be9116cd;
- ultimate closure: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40;
- witness packing: 6292f77598df9cf841f04b012b81f44753567cc3;
- zero-excess witness: 07d19abfd6c1c749c7360526e4a04a3eb865fb2e;
- master closure: e46da35aedce7bbaaf11756b50192bd157956239.

Rechecked the canonical distinction: E408 Q32 has e(H)=285 and total excess six; the 284-edge/excess-four conclusions belong to E407 Q32 and E408 Q33 and are not imported. Read the registered E408 seven-block equality system and exact-129 contextual blocker theorem.

## 2026-10-25 — new all-shell-support witness and capacity theorem

1. Re-derived the exact-129 witness family without assuming M[B]=empty. The Type-I normal form has twelve pairwise-disjoint K5 cliques: ten isolated components plus two in the exceptional gadget. Since alpha(H)≤4, each must meet {p}∪A. The 14-point outside budget implies at least eight isolated components per exact color have exactly one outside-H vertex, yielding an independent 4-set in H. Cross-color witnesses intersect in at most one vertex. This improves the earlier six-witness floor while keeping the KP classification as an explicit dependency.
2. Independently derived the correct 285-edge capacity inequality:
   6N ≤ e(complement H[U]) ≤ C(v,2)-p4(47-v)-12v+285-E_U.
   The 285 constant and excess-six budget are retained throughout.
3. Recomputed exact integer support thresholds: v≥33,35,37 when m=8,9,10 exact-129 colors. If k exceptional gadget vertices are outside H, N≥8m+k and the thresholds strengthen accordingly.
4. Derived the shell count 22≤e(M)≤32 and 0≤G_A=32-e(M)≤10 from the 14-point color-edge cap and q=32. Explicitly retained the possibility of up to six zero-shell-support core vertices; no invalid full-support comparison is used.
5. Coupled the core witnesses to the seven outer K12 blocks. The blocker theorem M_C≥15+P_C and the at-most-two non-witness component bound imply at least ceil((P_C+1)/7) distinct witness components per exact color are used as outer blockers. Aggregating the exact duplicate ledger gives at least 11, 20, or 29 such components when m=8,9,10.
6. Added a parameterized exhaustive shell-support dichotomy by α(M)=10 versus α(M)≤9. The core capacity theorem is uniform in both branches; the split is not assumed.
7. Added verify_core285_capacity.py. It checks integer arithmetic and case tables only, not graph realizability or the external KP classification.

## Current status

**E408 Q32: OPEN / NOT_CERTIFIED.** The workstream has established a stronger necessary-structure reduction covering both M[B]=empty and M[B] nonempty. The next unresolved task is a graph-level compatibility/contradiction for the surviving core-support profiles and the labelled seven-block blocker assignments. No complete SAT/ILP/CSP model or UNSAT certificate is claimed.
