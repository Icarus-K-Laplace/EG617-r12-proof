# Asset ledger

| Asset | Status | Notes |
|---|---|---|
| Degree-13 pivot decomposition `49=1+13+35` | PROVED | Core bookkeeping. |
| Shell identity `e(F)=91+q+e(H)` | PROVED | Exact. |
| CORE211 | PROVED | Every H in R(3,35) has e(H)>=211. |
| q27/q28/q29 repivot machinery | PROVED / q27 audit-dependent | Generic low-q backend tools. |
| E329,E330,E331 | PROVED EMPTY | Reconstructed backend closures. |
| E332 full layer | PROVED EMPTY / FROZEN | Preferred proof DAG: `backend/E332_FULL_CLOSURE.md`; unified terminal proofs in `backend/E332_H1_UNIFIED_FINAL.md` and `backend/E332_G8_H0_UNIFIED_CLOSURE.md`. |
| Front-end contextual recurrence | COMPUTATION_CERTIFIED | 1752 nodes, 144 outer stops, two independent implementations. |
| Front-end dichotomy `K145 -> R449 OR T61` | PROVED | No backend circularity. |
| T61 h12 branch | PROVED EMPTY | Uses R(4,48) floor310. |
| T61 E397..E400 | PROVED EMPTY | Repository-canonical. |
| T61 E401--E404 Line-A V6 | SOURCE_REPORTED_PROVED / REPLAY_PENDING | V6 package result; tracked separately from repository-canonical proof bodies. |
| T61 E405 Line-A V7 | SOURCE_REPORTED_PROVED / REPLAY_PENDING | V7 package result; q30 promotion component has since been independently replayed. |
| E406 core minimum degree through 288 edges | PROVED | `front_end/E406_CORE_MINDEG_288.md`: inherited 47-core with e<=288 has delta>=12. |
| E406 low-charge q22--q26 promotion | PROVED | `front_end/E406_LOW_Q_PROMOTION_22_26.md`. |
| E406 q27/q28 elimination | PROVED | `front_end/E406_Q27_Q28_ELIMINATION.md`. |
| E406 q29 transfer | PROVED | Generic q29 theorem migrated at hypothesis level; E406 q29 reaches q30. |
| T61 q30 hereditary promotion | PROVED / INDEPENDENTLY REPLAYED | `front_end/Q30_HEREDITARY_PROMOTION_CANONICAL.md`: q30 reaches q>=31 within <=2 regular repivots. |
| E406 q30->q31 distance d1 | PROVED EMPTY | `front_end/E406_D1_FULL_CLOSURE.md`. |
| E406 q30->q31 distance d2 | PROVED EMPTY | Full d2 retained-star/e1 closure chain. |
| E406 q30->q31 distance d3 | PROVED EMPTY | Type-A/Type-B, O5 and all O4 multiplicities closed. |
| E406 q30->q31 distance d10 | PROVED EMPTY | `front_end/E406_Q31_PLATFORM_SUPPORT_RIGIDITY.md`. |
| E406 q30->q31 distance d11 | PROVED EMPTY | `front_end/E406_D11_FULL_CLOSURE.md`. |
| E406 q30->q31 distance d12 | PROVED EMPTY | `front_end/E406_D12_FULL_CLOSURE.md`. |
| T61 E406 | PROVED EMPTY | Canonical master: `front_end/E406_FULL_CLOSURE.md`. No remaining E406 obligation. |
| T61 E407,E408 | OPEN | Active Line-A front-end window. V8 gives source-reported structure but does not close either layer. |
| Line-B V4 support repetition | SOURCE_REPORTED_PROVED / REPLAY_PENDING | Necessary survivor families D2-A/B/C/D,R9 with repetition lower bounds 8,8,5,7,9. |
| E333..E340 elimination | OPEN | Sole remaining backend interval. |
| Full EG617 r=12 theorem | OPEN | Must not be claimed solved until E407/E408 and E333..E340 are closed. |
