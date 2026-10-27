# Dependency audit — E408 global incidence sprint

Updated: 2026-10-27

## 1. Source branch heads checked

The following source branches were inspected at these exact heads. They remain read-only in this workstream.

| Source | HEAD | Role |
|---|---|---|
| workstream/r12-e408-q33-global-compat-20261025 | 0cb2ff3968f005c9cb255958df7c02b220678701 | Q33 seven-block incidence ledger, P49 screens, gadget row contracts |
| workstream/r12-e408-q32-excess6-20261025 | a0ba6db26c7e8b00a4217dcbcbf298895dff93ce | Q32 285-edge capacity and support-44 terminal |
| workstream/r12-unified-witness-capacity-20261025 | faa8183c150dd78b000d0957fa8a63cebd52e146 | labelled witness-capacity theorem, support-41 terminal |
| workstream/r12-witness-packing-chat-20261025 | f5d3daa07403877ede9885e1bd5c2f46b16d81da | witness packing constraints |
| workstream/r12-zero-excess-witness-20261025 | c8c4833c7830370a703d228ee23e3b88484d6baa | zero-excess witness constraints |
| workstream/r12-ultimate-closure-20261024 | 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 | root proof DAG and retained contracts |

## 2. Q33 profile \((6,2,1^5)\)

Source theorem:
r12_master/workstreams/e408-q33-global-compat-chat-20261025/R12_P49_R6_R2_DOUBLE_STAR_EXCLUSION.md

Source verifier:
r12_master/workstreams/e408-q33-global-compat-chat-20261025/verify_p49_r6_r2_double_star.py

Audit:
- Reimplemented and reran the finite gadget/incidence predicates in an independent Python runtime.
- Exact results: 452 Case-A checks, 570,942 Case-B/C checks, total 571,394, zero failures.
- The proof constructs a C-colored K12 and a vertex with at least two C-edges into it.
- The conclusion is PROVED_CONDITIONAL on the registered row classifications, exact-129 factor theorem, gadget normal forms, and universal-D alignment contract.

This is not based on the older one-external-edge inference.

## 3. Q33 profile \((7,1^6)\)

New files in this branch:
- Q33_P49_R7_DOUBLE_STAR_EXCLUSION.md
- verify_q33_p49_r7_double_star.py

Audit:
- The exact gadget normal forms were reconstructed from the source branch.
- The universal-D property for every disjoint low-block K5/K5 pair was checked.
- The high-pair alignment property was exhaustively checked for every pair of clique sets \(E,F\) with \(|E\cup F|\ge4\).
- Results: 48 low-pair/\(D\) tests and 27,380 high-pair tests, zero failures.
- The graph proof treats \(n=0\), \(n=1\), and \(n\ge2\) no-component-row cases separately; no branch is left implicit.
- The contradiction uses two external C-edges into the same C-colored K12.

Status: PROVED_CONDITIONAL under the named exact-129, row-budget, row-blocker, and gadget contracts.

## 4. Historical inference audit

The old Q33 file R12_P49_BOUNDARY_EXCLUSION.md contains historical Case-I/V material. It is not used as a current proof source for the remaining all-component-edge-present branches.

The inference that one external C-edge into a C-colored K12 is impossible is false; the correct capacity is at most one such edge per outside vertex. The separate R6/R2 double-star theorem and the new R7 theorem do not rely on that inference.

The statement “ten disjoint C-colored K12s imply \(P_C\le42\)” has not been established by the star-capacity lemma alone and is not used here. Any future proof using that bound must supply an independent, valid argument.

## 5. Q32 support theorem

Source:
r12_master/workstreams/e408-q32-excess6-chat-20261025/CORE285_CAPACITY_THEOREM.md

Source terminal:
r12_master/workstreams/e408-q32-excess6-chat-20261025/LOW_SUPPORT_TRIPLE_PAIR_CAPACITY.md

The source proves the 285-edge support floor \(|U|\ge44\) and the pair-uniqueness terminal at \(|U|=44\). It remains conditional on the E408 Q32 outer embedding and exact-129 Type-I classification. The \(v=44\) terminal is still OPEN. No 284-edge result is imported.

## 6. Remaining proof dependencies

- Exact-129 Type-I factorization and exceptional-gadget classification: retained external extremal input; not reproved in this branch.
- Seven-block equality ledger and \(P_C+R_C+s_C=62\): retained outer-embedding contract; must ultimately be derived from the original K145 hypothesis.
- The two remaining Q33 P49 all-component-edge-present branches: OPEN.
- Q33 global labelled-witness/core-capacity contradiction: OPEN.
- Q32 \(v=44\) triple-pair terminal: OPEN.
- Original K145-to-T61 reduction and the full EG617(r=12) theorem: OPEN / NOT_CERTIFIED.


## 7. Q33 exact-color count capacity theorem

New theorem: Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md. Arithmetic verifier: verify_q33_exact_color_count_capacity.py. The h=4 endpoint has a separate exhaustive verifier: verify_q33_h4_orthogonal_array.py.

Independent replay of the finite dynamic program gives:
- 20 variables \(k_i\in\{0,1,2,3,4\}\), cost budget 33: maximum incidence sum 46;
- 10 variables, cost budget 17: maximum incidence sum 23;
- 10 variables with required incidence sum 24: minimum pair-cost 18;
- the pointwise bound \(k\le3/2+\binom{k}{2}/2\) holds for all five possible values.

The graph-level conditional proof first derives \(h\le4\) from the 16-point complement \(W\), then charges overlaps between unselected component K4s and selected gadget witnesses at no more than four edges per gadget witness. It excludes \(m=10\), and shows \(m=9\Rightarrow h\ge1\). This uses the 284-edge Q33 contract only; no 285-edge result is imported.

Status: PROVED_CONDITIONAL for the named contracts. If (m=9), (delta\ge14,10,6) for (h=1,2,3). The h=4 endpoint would force (H[W]=4K_4) and an edge-partition of (K_{4,4,4,4}) into four (K_4)'s and 24 triangles; this induces impossible OA(4,4,2,2), so h<=3. Q33 global compatibility remains OPEN.

The R7 double-star theorem's pigeonhole sentence was also clarified: the selected vertex belongs to at least two row-neighbor sets (V'\setminus E_i), so it is adjacent to at least two rows of the constructed (K_{12}). This is a wording audit correction, not a change in the theorem.
