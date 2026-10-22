# Asset ledger

| Asset | Status | Notes |
|---|---|---|
| Degree-13 pivot decomposition `49=1+13+35` | PROVED | Core bookkeeping. |
| Shell identity `e(F)=91+q+e(H)` | PROVED | Exact. |
| CORE211 | PROVED | Every H in R(3,35) has e(H)>=211. |
| q27/q28/q29 repivot machinery | PROVED / q27 audit-dependent | Generic low-q backend tools. |
| E329,E330,E331 | PROVED EMPTY | Reconstructed backend closures. |
| E332 reduction to q30+211 | PROVED | `backend/E329_E332_CLOSURE.md`. |
| E332 d4..9 | PROVED EMPTY | Profitable repivot. |
| E332 d10 | PROVED EMPTY | Equality branch closure. |
| E332 d3 | PROVED EMPTY | Equality branch closure. |
| E332 strengthened zero-gap theorem | PROVED | Full-shell union / row-disjointness constraint. |
| E332 triangle-row union lemma | PROVED | Every M-triangle has core-row union at least24. |
| E332 missing-K4 row-cover lemma | PROVED | Every M-K4 covers the full 35-core by its four core rows. |
| E332 G=4 | PROVED EMPTY | Full layer. |
| E332 G=5 | PROVED EMPTY | Full layer. |
| E332 G=6 | PROVED EMPTY | Full layer. |
| E332 G=7 | PROVED EMPTY | h0, h1 and H2-G7-K4minusE all closed. Preferred h1 route: `backend/E332_H1_UNIFIED_FINAL.md`. |
| E332 unified one-high theorem | PROVED | G7: `b<=g_x` and `b>=k+g_x-3`; G8: `b<=g_x-1` and `b>=k+g_x-4`; collapses both one-high branches to k=3 terminals. |
| E332 G=8,h1 -> h0 | PROVED | Unique surviving one-high terminal `(k,r)=(3,7)` repivots to G8,h0 or overflows decoration. |
| E332 unified G8,h0 theorem | PROVED EMPTY | Master identities `W_A=22+a-b+g_A>=11m` and inactive-edge lower bound imply `a>=k+8m-21`; all m=0,1,2 equality geometries eliminated. See `backend/E332_G8_H0_UNIFIED_CLOSURE.md`. |
| E332 full layer | PROVED EMPTY | Preferred master DAG: `backend/E332_FULL_CLOSURE.md`. No low-backend frontier remains. |
| Front-end contextual recurrence | COMPUTATION_CERTIFIED | 1752 nodes, 144 outer stops, two independent implementations. |
| Front-end dichotomy `K145 -> R449 OR T61` | PROVED | No backend circularity. |
| T61 h12 branch | PROVED EMPTY | Uses R(4,48) floor310. |
| T61 E397..E400 | PROVED EMPTY | Repository-canonical. |
| T61 E401--E404 Line-A V6 package | SOURCE_REPORTED_PROVED / REPLAY_PENDING | Uniform q<=29 theorem + 127-row exact rational certificate reported. |
| T61 E405..E408 | OPEN | Package-level remaining front-end window if V6 replay is accepted. |
| Line-B V2 adjacent two-pivot system | SOURCE_REPORTED | Exact exchange identities. |
| Line-B V2 q34/q35 quotient compression | SOURCE_REPORTED | 76 necessary quotient rows. |
| Line-B V2 local q30--q33 certificates | SOURCE_REPORTED | Naive one-step Phi monotonicity is false. |
| E333..E340 elimination | OPEN | Sole remaining backend interval. |
| Full EG617 r=12 theorem | OPEN | Must not be claimed solved. |
