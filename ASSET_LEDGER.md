# Asset ledger

| Asset | Status | Notes |
|---|---|---|
| Degree-13 pivot decomposition `49=1+13+35` | PROVED | Core bookkeeping. |
| Shell identity `e(F)=91+q+e(H)` | PROVED | Exact. |
| CORE211 | PROVED | Every H in R(3,35) has e(H)>=211. |
| q27/q28/q29 repivot machinery | PROVED / q27 audit-dependent | Generic low-q backend tools. |
| E329,E330,E331 | PROVED EMPTY | Reconstructed backend closures. |
| E332 full layer | PROVED EMPTY / FROZEN | Preferred proof DAG: `backend/E332_FULL_CLOSURE.md`. |
| Front-end contextual recurrence | COMPUTATION_CERTIFIED | 1752 nodes, 144 outer stops, two independent implementations. |
| Front-end dichotomy `K145 -> R449 OR T61` | PROVED | No backend circularity. |
| T61 h12 branch | PROVED EMPTY | Uses R(4,48) floor310. |
| T61 E397..E400 | PROVED EMPTY | Repository-canonical. |
| T61 E401--E404 | PROVED EMPTY / CANONICAL REPLAY | `front_end/E401_E404_CANONICAL_CLOSURE.md`; independently reconstructed from V6 proof body. |
| T61 E405 | PROVED EMPTY / CANONICAL REPLAY | `front_end/E405_FULL_CLOSURE_CANONICAL.md`; independently reconstructed from V7 proof body. |
| <=288 47-core minimum-degree interface | PROVED | `front_end/E406_CORE_MINDEG_288.md`: e(C)<=288 implies delta(C)>=12. |
| q<=29,G<=7 hereditary promotion | PROVED | Under <=288 core interface and EDGE13, a regular missing-degree3--10 pivot reaches q>=30. |
| T61 q30 hereditary promotion | PROVED / INDEPENDENTLY REPLAYED | `front_end/Q30_HEREDITARY_PROMOTION_CANONICAL.md`: q30 reaches q>=31 within <=2 regular repivots. |
| E406 low-to-q30 bridge | PROVED | `front_end/E406_LOW_TO_Q30_BRIDGE.md`. |
| E406 q30->q31 distances d1,d2,d3,d10,d11,d12 | PROVED EMPTY | Independent closure files for all six classes. |
| T61 E406 | PROVED EMPTY | Canonical master: `front_end/E406_FULL_CLOSURE.md`. |
| T61 E397--E406 continuous h13 interval | PROVED EMPTY | Repository-canonical continuous closure. |
| T61 E407,E408 | OPEN | Active Line-A front-end window. V8 gives source-reported structure but does not close either layer. |
| Line-B V4 support repetition | SOURCE_REPORTED_PROVED / REPLAY_PENDING | Necessary survivor families D2-A/B/C/D,R9 with repetition lower bounds 8,8,5,7,9. |
| E333..E340 elimination | OPEN | Sole remaining backend interval. |
| Full EG617 r=12 theorem | OPEN | Must not be claimed solved until E407/E408 and E333..E340 are closed. |
