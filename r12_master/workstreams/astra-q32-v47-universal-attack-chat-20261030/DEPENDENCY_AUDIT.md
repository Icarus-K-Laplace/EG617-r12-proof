# Independent dependency ledger

## Exact U6 graph contract

U6 is a theorem about a graph H satisfying:

    |H|=47, e(H)=285, delta(H)>=12, alpha(H)<=4, omega(H)<=11.

The analytic proof does not use any source-color classification, witness support, sibling branch, solver output, or failed-search inference.

## Parent mapping

The genuine T61 parent F has 61 vertices, delta(F)=13, alpha(F)<=5, omega(F)<=11 and e(F)=408. For a target-degree-13 pivot p, let H=F-N_F[p]. Then:

- |H|=47;
- e(F)=91+q+e(H), so q=32 gives e(H)=285;
- p is anticomplete to H, so alpha(H)<=4;
- H is induced in F, so omega(H)<=11.

The missing edge is delta(H)>=12. Its current route is E406_CORE_MINDEG_288.md -> CORE211.md -> the R(3,35) minimum-degree seed. The integration audit records the latter seed's A4 23-neighbourhood / cap-two proof body as missing from the current source set. See Q32_PARENT_CONTRACT_MAPPING.md. Thus the parent application is NOT independently certified.

## Conclusion dependencies

| Result | Status | Inputs |
|---|---|---|
| Degree-12 independent four-set | PROVED_CONDITIONAL | Five-item CORE; ordinary Turan |
| Private-clique / five-point reduction | PROVED_CONDITIONAL | Five-item CORE |
| Common-neighbor inequality U2 | PROVED_CONDITIONAL | Five-item CORE; Kang–Pikhurko Theorem 1 at n=25,r=2 |
| At most one exterior point completes a K10 | PROVED_CONDITIONAL | U2; clique cap and excess budget |
| Two-K11 pair spends all six excess | PROVED_CONDITIONAL | CORE; independent-five blocker |
| Two-template theorem U1 | PROVED_CONDITIONAL | Preceding lemmas; support counting and rotation |
| P impossibility | PROVED_CONDITIONAL | U1; U3; mixed-pair lower bound 8>6 |
| D impossibility | PROVED_CONDITIONAL | U1; U3; aggregated mixed-pair lower bound 10>6 |
| Universal graph theorem U6 | PROVED_CONDITIONAL | Five-item CORE; ordinary Turan; Kang–Pikhurko Theorem 1 |
| Genuine E408/Q32 parent implies CORE | OPEN / NOT_CERTIFIED | delta(H)>=12 lower-order seed not independently certified |
| All m=8,9,10 and all Q32 support sizes | PROVED_CONDITIONAL only if parent CORE is certified | U6; no color-specific premise |
| Q33, E407 and full EG617(r=12) closure | OPEN here | Outside U6 and this write scope |

## External theorem parameter map

For a 25-vertex set W with alpha(H[W])<=2, the complement is triangle-free. It cannot be bipartite because omega(H)<=11 would then cover W by two cliques of total order at most22. Kang–Pikhurko Theorem 1 at n=25,r=2 bounds the non-bipartite triangle-free complement by 145 edges. Hence e(H[W])>=155, contradicting the degree-sum upper bound 153.

The Kang–Pikhurko 61-point exact-129 equality classification is used only by SOURCE_CONTRACT_AUDIT.md, not by U6.

## Sibling isolation

Read-only snapshots were refreshed on 2026-10-30. No A, B, C, D, low-support or high-support theorem is a premise of U6. The latest observed B head is recorded in source_manifest.json. No sibling or global branch was modified.

## Acceptance boundary

- Conditional core theorem: complete and independently reviewed.
- Finite support and terminal arithmetic: independently replayed.
- Parent delta premise: not independently certified; A4 source recovery remains open.
- Root promotion: not issued.
- No exhaustive graph search, solver UNSAT, or global EG617 closure is claimed.
