# Progress log — R12 witness-packing line

## 2026-10-25 — initial witness-packing theorem

- Inspected the repository's fixed-r=12 emergency, ultimate-closure, master-closure, and zero-excess branches.
- Proved a labelled witness-packing support theorem from exact-129 K5 components: at least seven independent Q-sets per exact-129 color (including a possible p+Q component), pairwise-linear across colors.
- Derived the Turán support floor v>=29 for E407 Q32 and v>=31 for E408 Q33; identified the remaining exact color profiles.
- Published initial theorem at commit c6b4c81dd7899835c08b3c2e701b762ec4fb2148, then moved the substantive artifact to the isolated workstream branch.

## 2026-10-25 — live cross-branch reconciliation and correction

- Read latest emergency head 87a58429070cffbd90991045e0375102fcc4ec0d, ultimate head 28f47fb7c8f273e6a70bf19f4ee961e8023f5981, zero-excess head 95255a82f126fadbc8834c799df1374e5fc86fca, and master-closure head e46da35aedce7bbaaf11756b50192bd157956239. Also checked general-r/Astra branch status; these remain separate contracts and were not imported as fixed-r=12 theorems.
- Corrected the count distinction: at least seven total Q-sets but only six guaranteed B-labelled Q-sets per exact-129 color.
- Combined the six disjoint B-labelled witnesses with total core excess four to prove at least two zero-excess B-labelled witnesses per exact-129 color, hence at least 14 in E407 and 16 in E408 Q33.
- Imported the Q33 high-k packing and the outer-block blocker-occurrence inequality with notation kept separate.
- Audited the emergency witness-star proof: the second-Turán step forces tripartiteness, not completeness. Recorded the precise gap and the corrected local structural conclusion without claiming the full core theorem is false.
- Added verify_witness_packing.py; the standard-library arithmetic verifier was independently run and all assertions passed.
- Added CROSS_BRANCH_SYNC_20261025.md and CANONICAL_STATE.md.

## Current status

**EG617(r=12): OPEN / NOT_CERTIFIED.**

Next mathematical target: classify the E407 v=29 / 49-witness and E408 Q33 v=31 / 56-witness boundary kernels with actual shell-row incidence and core degree/excess constraints. Scalar overlap bounds alone are insufficient.
