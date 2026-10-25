# Exact-129 gadget alignment certificate

Date: 2026-10-25  
Status: **FINITE_GADGET_VERIFIED**  
Verifier source: GADGET_ALIGNMENT_VERIFIER.js  
Verifier source commit: 6b5b356b1c3e8c70a7b8a296d6af46863b6a2a49  
Verifier blob SHA: 5ea65b9b190de378121aa6a4d326f053ff329bb9

## Contract

For each \(s\in\{1,2,3,4\}\), the verifier builds the exact 11-vertex normal form:
- \(A=\{a_0,\ldots,a_4\}\) and \(B=\{b_0,\ldots,b_4\}\) are cliques;
- \(a_0\) is adjacent to \(b_0,\ldots,b_{s-1}\);
- \(x\) is adjacent to \(a_1,\ldots,a_4\) and \(b_s,\ldots,b_4\);
- there are no other cross-edges.

It exhausts all \(2^{11}=2048\) vertex subsets in each normal form and checks clique status by every internal pair. It then enumerates every disjoint clique pair of the required sizes and checks the alignment statements below.

## Exact exhaustive counts

| \(s\) | \(K_3\) | \(K_4\) | \(K_5\) | disjoint 55 pairs | disjoint 54 pairs | disjoint 53 pairs | disjoint 44 pairs |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 32 | 18 | 4 | 3 | 28 | 52 | 65 |
| 2 | 30 | 15 | 3 | 2 | 20 | 40 | 50 |
| 3 | 30 | 15 | 3 | 2 | 20 | 40 | 50 |
| 4 | 32 | 18 | 4 | 3 | 28 | 52 | 65 |

The universal \(K_5\) families are
\[
\mathcal D_1=\{A,B\},\quad
\mathcal D_2=\mathcal D_3=\{A,B,A'\},\quad
\mathcal D_4=\{A',B\},
\qquad A'=(A\setminus\{a_0\})\cup\{x\}.
\]
Every universal \(D\) has a disjoint member in every disjoint \(55\) pair.

The verifier asserts all of the following, with no failures:

| Alignment property | Checks |
|---|---:|
| High omitted \(K_5\) vs low pair 55/54 | 380 |
| High omitted \(K_4\) vs low pair 55/54 | 1,776 |
| High omitted \(K_3\) vs low pair 55 | 312 |
| High omitted \(K_5\) vs low pair 53/44 | 1,476 |
| Fixed high omitted \(K_5\) vs two low pairs 55/54 | 10,592 |
| Two omitted pairs, types 55/54/53/44, excluding 53+53 | 60,288 |
| One omitted pair of type 55/54/53/44 vs two low pairs 55/54 | 392,872 |
| **Total alignment checks** | **467,696** |

The pair/pair property chooses a member of size at least four from each pair, so the chosen omitted sets lie in the six-set \(U\setminus D\) and pairwise intersect. The triple property likewise chooses size-at-least-four members from all three pairs.

The \(53+53\) pair/pair combination is deliberately excluded because it is not universally alignable by this \(D\)-family. The proof never invokes that alignment: the all-low occurrence is excluded by the pair-sum budget, while the \((6,3,1^5)\) occurrence is handled directly by its component/gadget excess inequalities. The verifier does **not** claim that a high \(K_4\) can always be aligned with a low \(53\) pair in isolation; that broader claim has counterexamples for \(s=2,3\). The \(K_3\)-against-\(54\) property is also not asserted; it has counterexamples for \(s=2,3\).

For the high-\(K_5\)-versus-\(53\) checks, the minimum allowed low omitted-set size is three. If the chosen low member is the \(K_3\), its size together with the high \(K_5\) is \(5+3=8>6\); both lie in \(U\\setminus D\), so they necessarily intersect. This is sufficient for the blocker step and is distinct from the unproved high-\(K_4\)-versus-\(53\) assertion.

## Scope

These are exact finite checks on four fixed 11-vertex graphs. They certify only the gadget alignment lemmas used by P49_BOUNDARY_EXCLUSION.md and the R=14 boundary analysis. They do not independently certify the exact-129 factor theorem, the seven-block equality embedding, the global 56-witness reduction, or EG617(r=12).
