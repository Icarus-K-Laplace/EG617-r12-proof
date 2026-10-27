# Progress log — E408 global incidence / witness capacity

## 2026-10-26 — intake and local Q33 repairs

- Created isolated branch `workstream/r12-twochat-e408-global-20261026`.
- Audited Q33/Q32/unified witness-capacity sibling heads; siblings are read-only.
- Independently replayed the Q33 `(6,2,1^5)` verifier: 571,394 cases, zero failures.
- Proved `(7,1^6)` conditionally by a repaired double-star argument and exact gadget verifier.
- Reconciled the P49 frontier: locally open branches were `(4,4,1^5)` and `(4,3,2,1^4)` with all component-representative edges present.

## 2026-10-27 — Q33 exact-color count and global closure

- Proved m=10 exact-129 colors impossible in the Q33 31-point/56-witness terminal.
- Derived h<=4 selected gadget witnesses; an OA obstruction further gives h<=3, though h<=4 suffices below.
- Proved the decisive nonexact-U reserve inequality
  \[
  26(11-m)\le\delta+6h.
  \]
- Since delta<=17 and h<=4, the RHS is at most41. With m=10 excluded, m=9 requires52 and m=8 requires78. Contradiction.
- Hence the registered Q33 31-point/56-witness terminal is PROVED_CONDITIONAL impossible.
- This bypasses the two locally unresolved P49 all-component-edge-present profiles; P_C<=48 is not claimed.

Key Q33 commits:
- exact-color capacity theorem: `50e4f7c2299f1cb21a410779a27fdd9fd7795438`
- OA endpoint closure: `99d85042c32a87a27d56c321c025ec55a3f978f5`
- Q33 nonexact-U reserve closure: `5328f7ac5302836f96f4a24cefdbef748dc9c9ed`
- arithmetic verifier: `f4a133898f5527db5fa385b477cfc120021f52dc`

## 2026-10-27 — Q32 support frontier audit

- Kept the 284-edge Q33 and 285-edge Q32 ledgers completely separate.
- Audited and retained `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`.
- Closed v=44 directly by exceptional injectivity plus the sibling triple-pair terminal.
- Proved the stronger `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md`: any core vertex outside the exact witness union would need at least 2(m-1)>=14 distinct shell neighbors in a 13-point shell, so all nonfull supports v=44,45,46 are impossible and U=H.
- Promoted the support frontier to the sole v=47 case in commit `59beb7116175db64ee37b5b440369dc08742fcef` and canonical commit `74b67d84e1706ba04931bbff69c9cb067986b8da`.

## 2026-10-27 — decisive Q32 exact-color-count contradiction

A stronger residual-degree argument makes the support case split unnecessary and closes the registered Q32 terminal.

### Low-degree lemmas

Using the independent full-color degree floors and Brouwer/Kang--Pikhurko complement bounds:

1. A 131-edge non-target color cannot contain a degree-two vertex; hence its minimum degree is at least3.
2. In a 130-edge non-target color, every degree-three vertex lies in an isolated K4 component.
3. Two such isolated K4s are impossible: deleting them leaves a 53-vertex,118-edge graph with alpha<=10,omega<=5, whereas Brouwer gives at least119 edges. Therefore a 130-edge color has at most four degree-three vertices.
4. In a 132-edge non-target color, every degree-two vertex lies in an isolated K3. Four such triangles are impossible because the remaining 49-vertex graph would have120 edges and alpha<=8, below p_8(49)=126. Thus at most nine degree-two vertices exist.

### Collapse of m

Exceptional injectivity gives m distinct Type-I degree-nine exceptional vertices.

- m=10: the unique132-edge color is forced to have degree2 at all ten exceptional vertices, exceeding its maximum capacity9.
- m=9: the130-edge and131-edge colors are both forced to degree3 at all nine exceptional vertices; the130-edge color can support at most4.
- m=8: the three130-edge colors have total degree at most10 at each of eight exceptions; each has degree>=3, so at least two are degree3 at each exception. Demand is at least16 degree-three incidences, but total capacity is at most3*4=12.

Therefore all m in {8,9,10} are impossible. The registered E408 Q32 terminal is **PROVED_CONDITIONAL impossible**.

New Q32 commits:
- initial m=9,10 reduction: `27d3f6a66f52a9aa0097270e76091b0c2e645904`
- strengthened all-m closure: `7148b910f0597e7082eebde21cec8a87d0b2b79a`
- arithmetic verifier: `d38f8614f3dc5b886f1473e27436cf2c426de80c`
- Q32 terminal promotion: `699f58ccf84aac0c14ad7f296d4c7e051ee9a0c5`
- canonical E408 promotion: `95edebd4eca2c7fdd30ab975989219c9c39e7033`
- dependency audit: `8a62baa3796b63b949c8b590e7f4d70fd1215b76`

## Current state

- E408 Q33 registered terminal: **PROVED_CONDITIONAL impossible**.
- E408 Q32 registered terminal: **PROVED_CONDITIONAL impossible**.
- No live E408 terminal remains in this workstream under the registered reductions.
- EG617(r=12): **OPEN / NOT_CERTIFIED** because the K145-to-T61/front-end bridge, E407, and other sibling backend obligations remain outside this workstream.
- No claim of a complete K145 proof is made.