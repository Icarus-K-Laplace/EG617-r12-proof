# Progress log — E408 global incidence / witness capacity

## 2026-10-26 — intake and local Q33 repairs

- Created isolated branch `workstream/r12-twochat-e408-global-20261026`.
- Audited Q33/Q32/unified witness-capacity sibling heads; siblings are read-only.
- Independently replayed the Q33 \((6,2,1^5)\) verifier: 571,394 cases, zero failures.
- Proved \((7,1^6)\) conditionally by a repaired double-star argument and exact gadget verifier.
- Reconciled the P49 frontier: locally open branches were \((4,4,1^5)\) and \((4,3,2,1^4)\) with all component-representative edges present.

## 2026-10-27 — exact-color count and W-capacity advances

- Proved \(m=10\) exact-129 colors impossible in the Q33 31-point/56-witness terminal.
- Derived preliminary \(h\le4\) for selected gadget witnesses; excluded \(h=4\) by an OA(4,4,2,2) obstruction, giving \(h\le3\).
- Added joint U/W pair-cost bounds for the ninth exact color.
- Derived a nonexact-color W reserve: every non-target color has at least four W-edges; equality is a four-edge matching.
- This sharpened the remaining exact-color branches and exposed the common 96-edge endpoint kernel `2 K4 + 24 K3 + 3 M4`.
- Constructed and independently verified an explicit realization of that abstract kernel. This was an important adversarial audit: the kernel alone is feasible and cannot be used as a contradiction without additional contextual structure.

Commits:
- exact-color capacity theorem: `50e4f7c2299f1cb21a410779a27fdd9fd7795438`
- OA endpoint closure: `99d85042c32a87a27d56c321c025ec55a3f978f5`
- nonexact W reserve theorem: `6b63f3491f49e222221f410279e96c61975f7083`
- W reserve verifier: `6beddb6bee7f3a8486b54f3b92474b0de563950a`
- endpoint-kernel feasibility verifier: `699b18dc0982aed83f30288ccffb81f87d9bd060`

## 2026-10-27 — decisive Q33 global closure

A stronger cross-layer count closes the registered Q33 minimum-support terminal.

1. Every non-target color restricted to the 31-point set U has independence number at most 12, hence at least
   \[
   p_{12}(31)=26
   \]
   U-edges.
2. Of the 56 selected witnesses, \(56-h\) are exact-color component witnesses, occupying exactly
   \[
   6(56-h)=336-6h
   \]
   distinct edges of \(L=\overline{H[U]}\).
3. Since \(e(L)=336+\delta\), all nonexact colors combined have at most \(\delta+6h\) available U-edge slots.
4. Therefore
   \[
   26(11-m)\le\delta+6h.
   \]
5. The previous theorem excludes \(m=10\). For \(m=8,9\), using only \(\delta\le17\) and preliminary \(h\le4\), the right side is at most 41, while the required left side is 78 or 52.

Contradiction. Thus the registered 31-point/56-witness Q33 terminal is impossible.

This bypasses the two locally unresolved P49 all-component-edge-present profiles; a colorwise proof of \(P_C\le48\) is no longer needed for Q33 closure.

New commits:
- Q33 nonexact-U reserve closure: `5328f7ac5302836f96f4a24cefdbef748dc9c9ed`
- arithmetic verifier: `f4a133898f5527db5fa385b477cfc120021f52dc`
- canonical promotion: `932a3b7e2cfce5b846d3ada0399e24106d85e5ef`
- global contradiction rewrite: `b539b9aadfeb434dc7c840f69987e447a01c9967`
- P49 status update: `da2748d271b382206082ac463b8d7e86bdd277b9`
- dependency audit update: `be2b5b3b361dd627f1922740179c34d9a673e463`

## Current state

- E408 Q33 registered minimum-support terminal: **PROVED_CONDITIONAL impossible**.
- Local P49 \((4,4,1^5)\), \((4,3,2,1^4)\): still locally OPEN but globally bypassed.
- E408 Q32 285-edge support floor \(|U|\ge44\): retained theorem.
- E408 Q32 \(|U|=44\) triple-pair terminal: **OPEN** and now the next primary target.
- EG617(r=12): **OPEN / NOT_CERTIFIED**. No claim of a complete proof is made.