# Exact-129 gadget alignment certificate

Date: 2026-10-25  
Status: **FINITE_GADGET_VERIFIED**  
Verifier source: GADGET_ALIGNMENT_VERIFIER.js  
Verifier source commit: 6c84ffb136c72554ea682ff29fc8d94d640e4fa0  
Current verifier blob SHA: 91abc289801c6c6837a5ea7d8993035ed2568cbd

## Contract

For each \(s\in\{1,2,3,4\}\), the verifier builds the exact 11-vertex normal form:
- \(A=\{a_0,\ldots,a_4\}\) and \(B=\{b_0,\ldots,b_4\}\) are cliques;
- \(a_0\) is adjacent to \(b_0,\ldots,b_{s-1}\);
- \(x\) is adjacent to \(a_1,\ldots,a_4\) and \(b_s,\ldots,b_4\);
- there are no other cross-edges.

It enumerates every subset of the 11 vertices and tests clique status by checking every internal pair. This covers all \(2^{11}=2048\) subsets for each of the four normal forms. It then exhausts every high omitted clique \(E\) of size four or five and every disjoint low omitted pair of type \((5,5)\) or \((5,4)\).

## Exact counts

| \(s\) | \(K_5\) cliques | \(K_4\) cliques | disjoint \(K_5/K_5\) pairs | disjoint \(K_5/K_4\) pairs | high \(K_5\) alignment checks | high \(K_4\) alignment checks | failures |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 18 | 3 | 28 | 124 | 558 | 0 |
| 2 | 3 | 15 | 2 | 20 | 66 | 330 | 0 |
| 3 | 3 | 15 | 2 | 20 | 66 | 330 | 0 |
| 4 | 4 | 18 | 3 | 28 | 124 | 558 | 0 |
| **Total** |  |  |  |  | **380** | **1,776** | **0** |

The 380 high-\(K_5\) checks split into 36 checks against low \((5,5)\) pairs and 344 against low \((5,4)\) pairs. The 1,776 high-\(K_4\) checks split into 168 and 1,608 respectively. All \(2,156\) alignment checks passed in the deterministic in-session replay of the verifier's enumeration algorithm.

The universal \(K_5\)-families are:
\[
\mathcal D_1=\{A,B\},\quad
\mathcal D_2=\mathcal D_3=\{A,B,A'\},\quad
\mathcal D_4=\{A',B\},
\qquad A'=(A\setminus\{a_0\})\cup\{x\}.
\]
For every tested high omitted clique \(E\), some \(D\in\mathcal D_s\) is disjoint from \(E\) and from at least one member of the low omitted pair. Every disjoint \(K_5/K_5\) pair also has a member disjoint from each \(D\in\mathcal D_s\).

## Completeness and scope

The graph normal form is derived analytically in Theorem 12.1. Given that contract, the verifier is exhaustive because every subset of the 11 vertices is enumerated, every \(K_4\) and \(K_5\) is discovered by exact pairwise clique testing, and every eligible disjoint pair is tested. This is a fixed-size gadget check, not an expanding-\(r\) graph search.

The certificate proves only the finite alignment lemma used by P49_BOUNDARY_EXCLUSION.md. It does not independently certify the exact-129 factor theorem, the seven-block equality embedding, or the full EG617(r=12) theorem.
