# Independent audit notes — EG617(r=12) K145 integration

Date: 2026-11-02
Audit branch: `workstream/r12-astra-independent-audit-20261102`
Base snapshot: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`
Repository: `Icarus-K-Laplace/EG617-r12-proof`

## Scope and isolation

This is an independent review record only. It does not edit or promote the frozen integration proof.

The integration branch was created from the earlier global root snapshot. A compare of the integration publication commit `c6c17bb6b1fee0e350fd0ff649680333f30c9f88` against global base `b0459807acd4b7e386148056ddf77d7998918893` reports that the added files are confined to `r12_master/workstreams/astra-global-root-integration-chat-20261031/`. The shared global branch remains at the older root snapshot; the new proof package is therefore isolated, not yet promoted into the canonical global root.

## Work independently checked

The audit read the lower-order chain, the 286-edge equality theorem, the 47/48-core gates, the COVER theorem, the h12 and h13 terminal arguments, and the K145-to-T61 extraction/recurrence proof.

No fatal counterexample or contradictory inequality has been found in the portions reviewed so far. This is an independent mathematical reading audit, not a claim of external peer review or proof-assistant certification.

### Finite q=27/q=28 shell classification — independently reimplemented

A separate Python implementation reconstructed the bipartite 3-hub/10-low shell enumeration from the stated row-multiplicity, Hall, EDGE12 and INS11 constraints. It did not import the frozen verifier.

Results:

| Check | q=27 | q=28 |
|---|---:|---:|
| Nonnegative 8-tuples summing to 10 | 19,448 | 19,448 |
| Tuples surviving edge and Hall filters | 882 | 891 |
| Hub-decoration trials | 32,665 | 51,118 |
| Complete decoration allocations | 2 | 16 |
| Canonical states | 2 | 8 |

The canonical state sets exactly match the theorem's expected lists. I then reconstructed each retained 13-vertex graph and checked all (2^{13}=8,192) subsets per state:
- the exact subset charge identity;
- α(M) ≤ 10;
- EDGE12 on every missing edge;
- INS11 at every regular vertex;
- nonnegative decorations and (z ≥ 22).

Total direct subset checks: **81,920**, all passed. The independently reproduced enumeration counters also match the frozen `frozen/cover/VERIFICATION_RESULT.json`.

### Analytic checks

The following steps were re-derived or checked line-by-line:
- the repivot identities (3) and (4), including the signs of (h_\beta,\eta_\beta,\kappa,m,b);
- the lower-order route through R(2,24), R(2,23), R(3,35), R(3,36), and R(3,37);
- the 286-edge equality exclusion and the use of the T=8 common-neighbor bound;
- the R(3,35) edge floor 211, using the strict AES threshold (22>5\cdot35/8);
- the 47-core gate (e(C)\le288\Rightarrow\delta(C)\ge12) and EDGE13;
- the q\le28 triangle-channel reduction and the q27/q28 shell classification;
- the q30 Family I/II derivation and the global excess contradictions;
- the contextual R(4,49) exclusion and the recurrence/extraction logic leading to the unique T61 terminal ((d,j)=(11,6)).

The root integration verifier explicitly reports `shell_search_rerun: false`: it checks the frozen enumeration source digest, the retained state list, and all 81,920 subset identities, but does not rerun the full 19,448-vector search. The separate reimplementation above closes that particular reproducibility gap for the q27/q28 finite classification. It does not replace an independent execution of the complete root verifier.

## Nonfatal proof-text clarifications

These are presentation/contract clarifications, not identified counterexamples.

1. **COVER_THEOREM.md, line 175 (B1, q=28):** before saying that base points from two distinct row classes are nonadjacent “by the same formula”, state explicitly that for every pair of distinct row classes (i\ne j), the displayed core-degree formula and δ((C_p))\ge11 imply (T_i\) is anticomplete to (T_j\). Then choose (p\) in a third row class and base points in the other two classes. This makes the deficient-clique contradiction immediate.

2. **COVER_THEOREM.md, line 205 (uniform promotion):** state at the start that (p\) is chosen to maximize (Q\), so (q_p=Q\). The final application does choose a maximizing pivot; stating it in the local lemma makes the inference (q_y\ge30\) versus (q_y\le Q\le29\) explicit.

3. **COVER_THEOREM.md, line 255 (Family I):** the formula (12-e_F(x,T_v)\) is already the correct simplification of (d_F(x)-c_i-e_F(x,T_v)\), since (d_F(x)=c_i+12\). No correction is needed. A prior chat note alleging a missing (c_i\) was mistaken and is withdrawn.

## Current certification boundary

- The isolated integration package states the original K145 theorem is proved under its explicit hereditary T61 contract.
- The 25-node proof DAG is acyclic; acyclicity alone does not verify the mathematics.
- The finite checks are ordinary Python, not Lean kernel checks.
- The original global root branch has not yet been updated to this integration package.
- No external referee or independent domain expert has reviewed the complete proof in this audit.

Accordingly, the accurate status is: **strong, internally coherent proof package with substantial independent checks; no fatal flaw found in the reviewed chain; final global promotion, full reproducible root rerun, and proof-assistant formalization remain separate tasks.**

## Next audit actions

1. Add the two clarifying sentences in a new proof revision, leaving the frozen snapshot immutable.
2. Reproduce the complete root verifier and record exact environment/output hashes.
3. Continue adversarial review of every dependency edge in the 25-node DAG before any global-root promotion.


## External theorem source checks

The two classical external inputs used in the audited chain were checked against accessible source records:

- Kang–Pikhurko, *Maximum K_{r+1}-free graphs which are not r-partite*, Matematychni Studii 24 (2005), 12–20, Theorem 1. For n=49 and r=12, the required regime n≥r+3 and r≤(n−1)/2 holds. The exact bound is
  \[
  e(L)\le t_{12}(49)-\lfloor49/12\rfloor+1
       =1100-4+1=1097.
  \]
  This gives at least 79 edges in the complementary colour graph on the 49-set. The journal's article record and the scanned journal PDF identify the paper and theorem. <https://matstud.org.ua/texts/2005/24_1/24_1_012_020.html>

- Andrásfai–Erdős–Sós, *On the connection between chromatic number, maximal clique and minimal degree of a graph*, Discrete Mathematics 8 (1974), 205–218, Theorem 1.1. At r=3, the strict threshold is \(5n/8\). For n=35, \(22>175/8=21.875\), so a 22-regular K4-free complement is 3-partite, exactly as used in the 211-edge floor. <https://doi.org/10.1016/0012-365X(74)90133-2>

These checks validate the cited theorem statements and numerical hypotheses; they do not constitute an independent proof of either classical theorem.


The standalone reproduction script is committed at `r12_master/workstreams/astra-independent-audit-chat-20261102/RECHECK_Q27_Q28.py`. The audit-session implementation was executed independently and reproduced the counters above; the committed script exposes the same standard-library-only procedure for later reruns.


## Additional root-level rechecks (2026-11-02)

### Contextual recurrence

Two separately transcribed integer implementations were executed in the audit session and compared over the full `a=0..12, n=0..145` table. There were **zero node mismatches**. The 1,752 nontrivial recurrence nodes agree; all 144 extraction-stop pairs were recomputed, with the unique survivor

`(d,j,a,n)=(11,6,5,61)`, lower bound 397 and edge budget 408.

The only terminal minimum-degree rows compatible with the budget are:
- (h=12): core floor 308, charge floor 20, row floor 406;
- (h=13): core floor 284, charge floor 22, row floor 397.

The recorded result is `REPRODUCED_CHECKS.json`. This checks the finite recurrence arithmetic and the stated outer-stop computation; it does not independently prove the analytic inequalities used to define the recurrence.

### E286 finite support and scalar checks

A separate enumeration of all multisets of support subsets of the four independent degree-12 seeds, with (h=3,4,5), total support size (h+5), and every seed multiplicity at least two, recovers exactly **2, 3, 5** orbits, respectively. Their clique-size patterns match the ten orbits in the frozen E286 theorem.

The displayed scalar functions in E286 Sections 3–4 were also exhaustively checked on the integer domain (1\le a,b\le11); their minima match the claimed lower bounds. The result is recorded in `RECHECK_E286_SUPPORTS.json`, with a standalone script in `RECHECK_E286_SUPPORTS.py`.

These finite checks do not verify the analytic interpretation of each scalar as a lower bound on disjoint excess charges, nor the subsequent blocker/overlap accounting in Sections 5–12.

### Proof-DAG completeness finding

The 25-node `PROOF_DAG.json` is acyclic and all parent references resolve, but its node set does not explicitly include two load-bearing theorem nodes that are separate entries in `GLOBAL_THEOREM_LEDGER.md`:

- `GATE47`: the (e\le286\Rightarrow\delta\ge12) gate needed for the 287-edge floor;
- `D48`: the minimum-degree-12 theorem for every (R(4,48)) graph, used in both the 310-edge floor and the h12 inserted-center contradiction.

The current DAG has no explicit `GATE47` dependency under `R447_FLOOR287`, and no `D48` dependency under `R448_FLOOR310` or `H12_EMPTY`. If these are intentionally packaged into broader nodes, the theorem ledger and DAG need an explicit mapping. `INDEPENDENT_VERIFIER.py::verify_dag` checks only acyclicity and parent-key existence, not completeness against the theorem ledger.

This is a **dependency-documentation gap**, not a mathematical counterexample. The proposed correction is recorded in `DAG_COMPLETENESS_AUDIT.md`. The frozen Astra integration branch was not edited.

### Public statement scope

The public Erdős Problems page states Problem 617 for all (r\ge3), with (K_{r^2+1}) and (r+1)-sets, and currently labels the overall conjecture open. The present integration theorem, if fully validated, is only the fixed (r=12) case (K_{145}); it does not settle the all-(r) conjecture. The public status is therefore not contradicted by a fixed-parameter claim. <https://www.erdosproblems.com/617>

## Current audit posture

The finite q27/q28 shell enumeration, contextual recurrence arithmetic, and E286 support-orbit/scalar minima have now been independently reproduced in this audit session. The remaining high-value adversarial work is the analytic blocker/overlap proof in E286 and the complete h13 q30 Family I/II elimination. The proof DAG also needs an explicit theorem-ledger crosswalk before its acyclicity result can be treated as dependency-closure evidence.


### Q32 285-edge support recheck

The original Q32 theorem's finite support reduction was also re-enumerated. The (h=3,4,5) support-orbit counts are (2,3,5). For (h=5), after the degree pattern (3,3,2,2) is aligned with the canonical support labels and the U4 exclusion of a K11--K11 support edge is applied, exactly two templates remain: P and D. The scalar minima are U4 = 6, U5 = 4, and the D mixed-edge bound = 5. The pointwise D accounting inequality was checked on 1,000 K10-vertex configurations and 100 K11-vertex configurations, with zero violations. Results and a standalone checker are in `RECHECK_Q32_SUPPORTS.json` and `RECHECK_Q32_SUPPORTS.py`.

A label-alignment bug was found in the first draft of the audit recheck scripts: the seed-degree vector was calculated before canonical relabeling and then attached to the canonical support. This did not change the orbit counts or the multiset of clique-size patterns, but it could misidentify which canonical labels were K10 versus K11. Both scripts were corrected to recompute seed degrees from the canonical support before any label-sensitive filtering. The corrected Q32 result now gives exactly the two expected P/D templates. This was an audit-script issue, not a defect found in the frozen theorem.

### Additional external-dependency ambiguity

The frozen Q32 theorem states its 25-point common-neighborhood bound relative to Kang–Pikhurko, Theorem 1 at (n=25,r=2). The vendored `COMMON_NEIGHBORHOOD_CAPACITY.md` also supplies a self-contained shortest-odd-cycle plus Mantel derivation of the same 145-edge bound. The root dependency DAG should explicitly say which route is used for `ABSTRACT_LOW285`: add a `SECOND_TURAN` edge if the published theorem is invoked, or cite the elementary derivation as the actual dependency if it is used instead. The current DAG includes `SECOND_TURAN` for the contextual (R(4,49)) proof but does not map this separate Q32 use.


### Lower-order M2/M3 finite recheck

The 5-cycle type quotient was independently enumerated: 20 nonempty compatible type-set pairs, each with side sizes 1-by-1 or 1-by-2, and 10 incompatible missing-cross-edge endpoint cases. The 23-vertex M2 blowup/edge-deletion representatives were then reconstructed independently:
- 61 representatives total;
- 49 satisfy the α\le11 premise;
- 12 are discarded because they contain an independent 12-set;
- all 263 maximal independent sets across the 49 valid representatives admit one of the proposed 12-sets with cost at most 6;
- the maximum minimum cost is exactly 6, forcing at least (78-6=72>D(14)=69) edges in the 14-point contradiction.

The standalone checker and result are `RECHECK_LOWER_M2_M3.py` and `RECHECK_LOWER_M2_M3.json`. This validates the finite family/type enumeration and the proposed neighborhood-cost tests; it does not prove the analytic classification of every possible triangle-free graph on 23 vertices.


### Standalone frontend recurrence replay

The two-transcription recurrence comparison is now preserved as a standalone script, `RECHECK_FRONTEND.py`, with its output in `RECHECK_FRONTEND.json`. Re-execution in this audit session checked 1,752 nontrivial nodes with zero mismatches, all 144 ((d,j)) extraction stops, and the unique survivor ((11,6,5,61)). The two minimum-degree rows at the T61 budget are exactly (h=12) with row floor406 and (h=13) with row floor397. This is an arithmetic/replay check, not a proof of the analytic graph inequalities.


## Additional analytic reading pass

A second adversarial reading pass was made over the load-bearing proof text, beyond the finite scripts:

- **M1–M6 lower-order gates:** checked the shortest-odd-cycle edge bounds, the 23-point blowup classification, the M3 12-set cost argument, the R(3,35)/R(3,36)/R(3,37) degree steps, and the R(4,47) low-edge gate arithmetic. No contradictory inequality was found in the reviewed steps.
- **D48 / R(4,48):** checked the degree-11 shell contradiction, the 211-edge R(3,35) floor, the q20 equality family, and the inserted-center repivot obstruction. No counterexample was found in the stated family.
- **Q32 / 285-edge theorem:** checked the seed-support accounting, U3/U4/U5 scalar thresholds, and the P/D residual support patterns. The finite checks above support the stated arithmetic; the analytic use of the common-neighborhood lemma remains subject to the explicit SECOND_TURAN-versus-elementary-route clarification.
- **E286:** checked the four-seed support bookkeeping and the disjoint-charge mechanism at the level of the displayed formulas. The support-orbit and scalar checks reproduce the finite tables, but they do not certify every blocker/overlap inference in Sections 5–12.
- **h13 COVER q30:** re-derived the q30 Family I/II case split, the K4-free reduction, the r=4/r=5 excess contradictions, and the ten-pair independent-set contradiction. No arithmetic contradiction or concrete counterexample was found. The proof-text clarifications about maximizing pivot and cross-row anticompleteness remain useful.

These are reading-audit results, not a formal verification. The strongest remaining adversarial target is still the analytic E286 blocker/overlap accounting and the completeness of the final theorem dependency map.


### E286 Section 3 and Section 9 pointwise accounting audit

A closer audit of the shared-leaf paragraph and the D-support pointwise inequality found **two imprecise justifications, but no counterexample to the inequalities themselves**.

#### Shared K11 leaf

The prose says a vertex missing one or both points has internal degree 10 plus “those two point adjacencies” as baseline 12. If it misses exactly one point, it is adjacent to only the other point, so the literal baseline is 11, not 12. The conclusion is nevertheless valid and can be stated exactly.

For a vertex (x) in the shared K11, let (S) be the subset of the two points to which (x) is nonadjacent. If their opposite missing sets have sizes (a_i) in distinct cliques, then each missed point forces (a_i) distinct neighbors outside the shared K11. Hence
[
d(x)ge 10+(2-|S|)+sum_{iin S}a_i
=12+sum_{iin S}(a_i-1).
]
Thus
[
epsilon(x)ge max!left(0,sum_{iin S}(a_i-1)ight)
ge sum_{iin S}max(0,a_i-2).
]
For (|S|=1), the last inequality is immediate; for (|S|=2), it is exactly the displayed shared-leaf inequality. This proves the intended no-double-counting conclusion with a corrected baseline explanation.

#### D support: negative increments

For D, the support pattern is ({01,02,03,12,13}), with K10s 0,1 and K11s 2,3. The text says there is at most one potentially negative increment at a vertex. This is true at a K10 vertex: its three incidences comprise one K10--K10 point (the only one that can have an empty opposite missing set) and two K10--K11 points (a point cannot complete a K11). But at a K11 vertex there are two incidences, both opposite K10s, and both increments can in principle be negative if both points complete their respective K10s.

The pointwise inequality still holds at a K11 vertex because there are only two terms. For any integers (x,yge-1),
[
max(0,x+y)ge max(0,x-1)+max(0,y-1).
]
Set (x=a_1-1,y=a_2-1). At K10 vertices the original “at most one negative among three” argument applies; at K11 vertices use this two-term inequality. This repairs the stated pointwise accounting without changing its conclusion.

#### Remaining D-case issue

This reading pass does not yet independently certify the transition “Every mixed point not complete to its K10 contributes at least 5 by (5)” in all completion patterns. Formula (5) is stated for a mixed pair with an additional K10-completing vertex, or an unspecified “usual diamond accounting.” The D paragraph should explicitly identify, for each noncompleting mixed point, which other support point supplies that completion, or state and prove the alternative diamond lemma for the zero-completer case. In particular, the case where neither of the two mixed points at a given K10 completes that K10 needs an explicit charge argument. This is the next targeted audit item; it is a proof-clarity/possible-gap flag, not yet a counterexample.

#### Section 11 same-K11-pair case split

The five cases in Section 11 are exhaustive after choosing a common small side when one exists: ((2,2)); ((1,2)) with disjoint or nested missing sets; and ((1,1)) with distinct or identical missing vertices. The local degree lower bounds in each listed case are arithmetically consistent with the (Tle8) budget. No counterexample to that case split was found in this reading pass.


### D-support zero-completer lemma — derived repair

The D-case completion issue can be closed from the existing scalar blockers. Let (P=z_{01}), (A=z_{02}), (B=z_{03}), with (K_0,K_1) the K10s and (K_2,K_3) the K11s. Suppose neither (A) nor (B) completes (K_0). Write their missing sets as (A_2,A_3\subset K_0) and (B_2\subset K_2,B_3\subset K_3), all nonempty.

**Claim:** under (T\le8), (P) must complete (K_0). If not, there are two cases.

1. **P also misses K1.** Its two missing sets are positive, so the K10/K10 scalar blocker applies. The three point charges and the shared K0 charge add:
   [
   f_{10,10}(a_0,b_0)+f_{10,11}(a_2,b_2)+f_{10,11}(a_3,b_3)
   \ge 2+4+4=10.
   ]
   To see the only possible overlap is harmless, for (x\in K_0) missing a subset (S\subset\{P,A,B\}), the three support adjacencies and the forced opposite missing sets give
   [
   \epsilon(x)\ge\max\left(0,\sum_{i\in S}(b_i-1)\right)
   \ge\sum_{i\in S}\max(0,b_i-3).
   ]
   The other missing-set charges lie in the three distinct cliques K1,K2,K3, and the point charges are distinct.

2. **P completes K1.** The two mixed scalar blockers add to at least (4+4=8). Their only shared charged vertices are in K0; if (x\in A_2\cap A_3), then
   [
   \epsilon(x)\ge\max(0,b_2+b_3-3)
   \ge\max(0,b_2-3)+\max(0,b_3-3),
   ]
   so the charges still add. Equality at total budget 8 forces both blockers to attain their unique minima ((a_i,b_i)=(2,3)), with all excess concentrated on A and B and zero on every clique vertex. Since P completes K1 and has zero excess, its K0 missing set (A_0) has size at least 8 (it has at least (10+(10-|A_0|)) neighbors in K1 and K0). But then (A_2,A_3), each of size 2, must both avoid (A_0), or a vertex in their intersection with (A_0) has degree at least 13. The complement of (A_0) has size at most 2, so (A_2=A_3=K_0\setminus A_0). A vertex in this common 2-set then has internal degree 9, adjacency to P, and all three forced neighbors in each of B2 and B3, giving degree at least 16, contradiction.

Thus, if neither mixed point completes K0, P necessarily completes K0; but then P is the additional K10-completing vertex required by (5), and the two mixed blockers each cost at least 5. Their K0 charges add by the same pointwise argument, giving (T\ge10), contradiction. Therefore at least one of A,B completes K0. By symmetry, at least one of z12,z13 completes K1.

Consequently the D-case split in Section 9 is exhaustive under (T\le8): each K10 has at least one completing mixed point. If exactly one completes, the other mixed point has the additional completing vertex needed for (5), giving a 5-unit charge. If both complete, their two point excesses sum to at least 7 by the common-neighbor bound. If the two 5-unit charges from K0 and K1 share a K11 leaf, the shared-leaf inequality makes them additive. Hence:
- one K10 with two completers gives at least (7+5=12) (or (7+7=14));
- one completer at each K10 gives at least (5+5=10).

This supplies the missing zero-completer argument and closes the D support elimination at the level of the stated analytic inequalities. It is a hand-derived lemma recorded in this audit; it has not been Lean-formalized or machine-checked.


### COVER beta=12 licensing cross-check

I checked a possible circularity in Section 9: it applies formula (3) with (eta=12) to a regular shell vertex (y), even though the new repivoted core (C_y) has not yet been shown to have minimum degree 12. This is **not** a gap in that step. In the notation of Section 3,
[
q_y=d(\beta+1-d)+\rho+h_\beta+\kappa+b,
\qquad
h_\beta=\sum_{x\in D_y}(d_C(x)-\beta).
]
Only the old parent core (C) enters (h_\beta); the terms (ho,kappa,b) are nonnegative independently. Section 9 has already licensed (delta(C)\ge12) from (e(C)\le288), so formula (3) yields the required lower bound without assuming (delta(C_y)\ge12).

The new core's minimum degree is needed only when formula (4) is used to assert (eta_{12}\ge0), for example in the equality arguments in Sections 10–12. There it is separately licensed: once (q_y\ge29) (K4 branch) or (q_y=30) (Family I/II), the new core has at most288 or exactly287 edges, and the Section 8/9 low-edge gate gives (delta(C_y)\ge12). Thus the apparent beta=12 circularity is resolved by the distinction between formulas (3) and (4).
