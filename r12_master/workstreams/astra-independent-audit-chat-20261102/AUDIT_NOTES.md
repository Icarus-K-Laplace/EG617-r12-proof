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
