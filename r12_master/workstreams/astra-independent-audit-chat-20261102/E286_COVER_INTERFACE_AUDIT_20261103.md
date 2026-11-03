# E286 <-> COVER interface audit

Date: 2026-11-03  
Frozen integration snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`  
Audit branch: `workstream/r12-astra-independent-audit-20261102`  
Scope: abstract 286-edge equality theorem, the 287-edge core floor, and the E407/E408 h13 COVER terminal.

## Verdict

**NO HYBRID COUNTEREXAMPLE OR LOAD-BEARING INTERFACE GAP FOUND.**

The key distinction is that E286 concerns a 47-vertex graph with exactly 286 edges and degree excess
[
T_{12}=2e-12\cdot47=8,
]
whereas the E408, Q=30 COVER terminal has a 47-core with 287 edges and degree excess
[
T_{12}=2\cdot287-12\cdot47=10.
]
The E286 support classification is not transported to the 287-edge Q30 core. COVER has its own q30 shell classification. The two arguments meet only through the pointwise 287-edge floor.

No frozen theorem source was modified. The report and the small arithmetic checker are new files in this audit workstream only.

## 1. Frozen source provenance

All theorem text below was read at the pinned integration commit, not inferred from status labels.

| Source | Blob SHA | Relevant lines |
|---|---|---:|
| `frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md` | `e596cdee0ae465a1fe82a8538e991dbc228db235` | 5-158 |
| `frozen/cover/COVER_THEOREM.md` | `f73c0a331cb22c3e553e679abb24ed65eab004ee` | 5-288 |
| `frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md` | `a8151c82da6486b43a735aa3aae64cc5db502b43` | 9-135 |
| `LOW_EDGE_AND_286_THEOREM_AUDIT.md` | `597b9893d0dbb944df202226fd9b830d28ba42f5` | 5-12, 23-44 |
| `PROOF_DAG.json` | `29e88b994f07a540481908fe6f1b18447d39a45b` | nodes 17-25, 44-61 |

The integration `SOURCE_MANIFEST.json` records the exact originating commits and blobs: low-edge/gate from `783c72090205d4bd1a6eefce1dec09e15f78e319`, E286 from `c3d07b2ca5912b1b0c1c6998303c19c3c2911340`, and COVER from `531e41c79e08dd2bb3892ca9ba8a491a56678565`. The pinned tree contains all three frozen snapshots.

## 2. The 287-edge floor is pointwise and correctly licensed

For every regular vertex p of a 61-vertex parent F, let
[
A=N_F(p),\quad C_p=F-N_F[p],\quad |A|=13,\quad |C_p|=47.
]
The parent-to-core identity is
[
E=e(F)=91+q_p+e(C_p),\qquad q_p=z_p+G_p.
]
It follows by the exact partition into the 13 pivot edges, the 78 possible shell edges, the shell-to-core edges, and the core edges. More explicitly, if M is the missing graph on A, z=e(M), and (g_a=d_F(a)-13\ge0), then
[
t_a=d_M(a)+g_a,qquad e_F(A,C_p)=\sum_{a\in A}t_a=2z+G,
]
so (e(F)=13+(78-z)+(2z+G)+e(C_p)=91+z+G+e(C_p)).

Every C_p is an induced 47-vertex subgraph of the SAME parent F. It inherits:
- (alpha(C_p)\le4), since an independent 5-set in C_p together with p would be an independent 6-set in F;
- (omega(C_p)\le11);
- every hereditary D-cap, by induced-subgraph inheritance.

The low-edge gate is not inferred from order or energy. The self-contained theorem M says that an actual (J\in R(4,47)) with (e(J)\le286) has (delta(J)\ge12) (low-gate source lines 9-10, 108-135). The abstract low285 theorem then excludes (e\le285) at that minimum degree, and E286 excludes the remaining equality (e=286) for every simple 47-vertex graph with
[
\delta\ge12,\quad\alpha\le4,\quad\omega\le11
]
(E286 source lines 5-15). Thus every actual parent core satisfies
[
oxed{e(C_p)\ge287}
]
for EVERY regular p, not merely for a selected maximizing pivot.

This licenses the pointwise bounds
[
q_p\le E-91-287=
\begin{cases}
29,&E=407,\\
30,&E=408.
\end{cases}
]
Taking a maximum afterward gives Q≤29 or Q≤30. The dependency DAG places ABSTRACT_286 below R447_FLOOR287, and that floor below both h13 energy terminals; COVER_407_408 itself depends on COVER_Q29_GENERAL and CORE211. There is no edge from the COVER conclusion back into E286 or the 287 floor. The written DAG summary also explicitly separates CORE211 from COVER chronology.

## 3. Why the E286 hypotheses transfer to each actual core

E286 itself needs no D-cap and no color factorization. It needs only order47, exactly286 edges, minimum degree12, alpha≤4 and omega≤11.

For an actual parent core C_p, order, alpha and omega are inherited as above. If e(C_p)≤286, the hereditary minimum-degree gate M supplies delta≥12. Therefore the abstract E286 theorem applies. This is the correct two-stage use:
1. hereditary caps + e≤286 -> delta≥12;
2. abstract E286 -> e≠286, after the separately proved e≤285 exclusion.

No proof step asserts that every 47-vertex graph of order47 and edge count at most286 automatically has minimum degree12.

## 4. Repivoting stays inside one fixed parent

For a regular shell vertex y of p, put (S=N_M(y)), (D_y=N_C(y)), and d=|S|=|D_y|. Directly from the same parent F,
[
C_y=F-N_F[y]=(C_p\setminus D_y)\cup S.
]
The sets removed and inserted both have size d, so |C_y|=47. It is another induced core of the SAME 61-vertex graph F, not an augmented graph or a graph assembled from different parents. Hence alpha≤4, omega≤11 and all D-caps are inherited again.

The exact edge ledger gives
[
e(C_y)=E-91-q_y.
]
Thus whenever E=408 and q_y≥29,
[
e(C_y)\le408-91-29=288.
]
The COVER Section 8 gate (source lines 183-202) then gives (delta(C_y)\ge12). This is the required order of inference: first lower-bound q_y using only the old core's minimum degree; only then infer the new core's minimum degree and use the inserted-vertex identity. No circular use of the new-core degree bound was found.

## 5. The delicate d=2 / K4 repivot, independently derived

This is the only place in the q30 no-middle-degree branch where the proof must first show q_y≥29 before using the new core's degree-12 gate.

Assume E=408, Q=30, and a maximizing pivot p with q_p=30. If the missing shell M contains a K4, let S_0 be its four vertices. The missing-K4 row-union bound gives t(S_0)≥36. The pivot identity
[
q_p=t(S_0)-e_M(S_0)+e_M(A\setminus S_0)+G_{A\setminus S_0}
]
and e_M(S_0)=6 force
[
t(S_0)=36,\quad e_M(A\setminus S_0)=0,\quad G_{A\setminus S_0}=0.
]
So the other nine shell vertices are regular and M-independent. Since z≥22 and every outside point has M-degree at most2 into S_0, at least one outside regular vertex y has d_M(y)=2.

Let S=N_M(y) be the corresponding edge of the K4. Then e_M(S)=1. With
[
\rho=e_M(A\setminus S)+G_{A\setminus S},
]
the pivot identity gives
[
30=q_p=t(S)-1+\rho,
\qquad\rho=31-t(S).
]
The exact repivot identity (COVER lines 62-80) at d=2 and beta=12 is
[
q_y=22+\rho+h_{12}+\kappa+b
=53-t(S)+h_{12}+\kappa+b.
]
The complementary pair (R=S_0\setminus S) is also an M-edge. EDGE12 gives t(R)≥12, while t(S_0)=36, so t(S)≤24 and therefore
[
q_y\ge53-24=29.
]
(Using the already available EDGE13 gives the stronger t(R)≥13, t(S)≤23 and q_y≥30.)

Now, and only now, e(C_y)≤288, so the new core has minimum degree12. Since S is an M-edge, its two vertices are nonadjacent in F. Their degrees in the inserted core are exactly
[
d_{C_y}(s)=t_s-e_F(s,D_y),\qquad s\in S.
]
The correction is nonnegative, so t_s≥12 for both s. Hence t(S)≥24 and t(R)=36-t(S)≤12, contradicting EDGE13 (which requires t(R)≥13). The branch is closed. Every inequality uses a stated core and a licensed degree gate.

## 6. Q30 families: same-parent repivots and no duplicated excess

### Family I

COVER lines 218-250 derive the complete Family I/II alternatives from the same E408 parent. In Family I, K={p}∪Y is a regular target K11; all ten low vertices and p are regular. Every active low repivots in the SAME F, has q=30, and hence has a 287-edge core with minimum degree12.

The row triangles are either equal or disjoint. Their multiplicities c_i=11-k_i are in {1,2,3} and sum to11. Distinct row triangles are anticomplete by the degree calculation in the core of a different row class. If r is the number of distinct triangles, alpha(F)≤5 gives r≤5 and c_i≤3 gives r≥4.

The excess count is a partition, not repeated charging:
- total degree excess over13 is (2E-13\cdot61=23);
- the three vertices of row triangle i each have degree c_i+12, contributing exactly (3(c_i-1));
- the triangles are disjoint, so their total contribution is (3(11-r));
- the remaining (50-3r) vertices therefore have excess (23-3(11-r)).

For r=5, the 35 remainder vertices have only5 excess units, but each must complete some row triangle to avoid an independent 6-set; each such completion forces degree at least15, costing at least2 per remainder vertex. For r=4, the 38 remainder vertices have only2 excess units, so at least36 are regular; two nonadjacent such vertices would leave one common-avoiding representative in each of the four anticomplete triangles, giving an independent 6-set. Hence these at least36 vertices form a clique, contradicting omega≤11. This reproduces the two terminal contradictions without reusing any vertex's excess twice.

### Family II

COVER lines 267-282 give ten regular K10 pivots v_i. Their two-point outside sets T_i are pairwise disjoint: a point in T_i is adjacent to v_i alone in K. For i≠j, in the actual 287-edge core C_{v_j},
[
d_{C_{v_j}}(x)=13-1-e_F(x,T_j)\ge12,
qquad x\in T_i,
]
so the pairs T_i are pairwise anticomplete. Choosing one point from each pair gives an independent 10-set, contradicting alpha(F)≤5. All ten cores are taken from the same parent F; no edge or vertex is silently transferred between different parents.

## 7. E286 support and charge accounting

E286 source lines 27-47 classify the four-seed incidence quotient. I independently re-enumerated all support multisets with support sizes at least2, total surplus incidence5, and each of four seed degrees at least2, modulo S4:
- h=3: 9 raw multisets -> 2 orbits;
- h=4: 40 raw multisets -> 3 orbits;
- h=5: 48 raw multisets -> 5 orbits.

Total: exactly10 support orbits, matching the theorem table. This is only the finite quotient check; the blocker-completeness and graph-theoretic reductions remain analytic obligations.

I also re-evaluated every displayed scalar blocker on a,b∈{1,...,11}. The minima are:
- f11: 6 at (2,2);
- f10,11: 4 at (2,3);
- f9,11: 2 at (2,4);
- f10,10: 2 at (3,3);
- three-star K10: 6;
- two mixed K9 points: 5;
- mixed K10/K11: 5 at (2,2).

The shared-center issue is handled pointwise, not by adding whole-clique excess repeatedly:
- For a K11 with two incidences, (max(0,a+b-2)\ge(a-2)_++(b-2)_+).
- For a K10 with three incidences and at most one zero opposite-missing-set size, (max(0,a+b+c-3)\ge(a-2)_++(b-2)_++(c-2)_+).

The second inequality's “at most one zero” condition is exactly the D-support geometry: the single K10/K10 point may complete one K10; both mixed points have nonempty missing sets in their K11 leaves. The first is the shared-leaf K11 accounting. The source proves these inequalities algebraically (E286 lines 81-87 and 127-133); I independently checked all bounded integer cases a,b,c∈{0,...,11}, obtaining zero counterexamples. The opposite clique contributions and point contributions are disjoint; only the shared center vertices require the pointwise inequality.

The previous focused double-K11-pair audit in this same branch also checked the 3,387 permitted intersection states and obtained a local lower bound14, above the theorem's required budget8. That check is supplementary; the frozen Section11 analytic case split remains the proof.

## 8. Hybrid counterexample arithmetic

The exact ledger (E=91+q+e(C)) rules out every attempted splice of the E286 equality case with the q30 terminal:

| Parent E | Pivot charge q | Implied 47-core edges | Disposition |
|---:|---:|---:|---|
| 407 | 30 | 286 | Excluded by the 287 floor; therefore q≤29 pointwise |
| 408 | 31 | 286 | Excluded by the 287 floor; therefore q≤30 pointwise |
| 408 | 30 | 287 | This is the genuine Q30 boundary; E286 does not apply (its T=8 hypothesis is absent; this core has T=10) and COVER Sections10-12 exclude it |

So there is no graph satisfying both the E286 equality hypotheses and the E408 Q30 local terminal at the same pivot. The two proof branches do not share or double-spend the E286 excess budget.

## 9. Reproducibility and limits

Added `RECHECK_E286_COVER_INTERFACE_20261103.py`, a standard-library-only checker for the support quotient, scalar minima, shared-center inequalities, pivot ledger, and d=2 K4 repivot arithmetic. The same checker logic was executed in this session. It reports `PASS_ARITHMETIC_AND_FINITE_QUOTIENT_CHECKS_ONLY`.

This checker does NOT:
- search all 47- or 61-vertex graphs;
- prove the analytic blocker/support reductions;
- execute the complete root verifier from a clean checkout;
- certify the proof in Lean/Coq or another proof-assistant kernel;
- substitute for external human combinatorics review.

**Final disposition:** no hybrid counterexample and no fatal interface/quantifier/parent-transfer gap found in the targeted E286 -> 287-floor -> COVER Q30 audit. The remaining status is an informal mathematical proof with finite computational support, pending clean-root reproduction and external expert review.
