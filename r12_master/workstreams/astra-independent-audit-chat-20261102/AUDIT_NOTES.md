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
