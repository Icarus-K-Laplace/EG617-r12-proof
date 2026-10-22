# Asset ledger

| Asset | Status | Notes |
|---|---|---|
| Degree-13 pivot decomposition `49=1+13+35` | PROVED | Core bookkeeping. |
| Shell identity `e(F)=91+q+e(H)` | PROVED | Exact. |
| Subset charge / exact repivot identities | PROVED | Core local-to-global tools. |
| CORE211: `H in R(3,35) => e(H)>=211` | PROVED | Clean reconstruction. |
| 211-core degree multisets | PROVED | `14,12^34` or `13^2,12^33`. |
| q28 profitable repivot | PROVED | Analytic. |
| q29 generic good-repivot | PROVED | q29 + inherited delta(H)>=12 => degree13 repivot q_y>=30; no e(H)=211 premise. |
| uniform q27 contradiction | PROVED / AUDIT-DEPENDENT | Type-I/II proof retained as explicit dependency. |
| E329,E330,E331 backend closures | PROVED | Reconstructed DAG. |
| E332 -> `(q,e(H))=(30,211)` | PROVED | Active Line C follows. |
| q30 undecorated degrees4..9 | PROVED EMPTY | Automatically profitable. |
| E332 d10 equality branch | PROVED EMPTY | Pure K3,10 reduction + row-overlap/coverage contradiction. |
| E332 d3 equality branch | PROVED EMPTY | Two-state A/B reduction + four-pivot triangle-incidence contradiction. |
| E332 surviving regular degrees | PROVED | Only `{0,1,2,11,12}` remain for undecorated shell vertices. |
| E332 high regular count | PROVED | At most two degree11/12 undecorated vertices. |
| E332 strengthened zero-gap theorem | PROVED | Regular missing edge covers full shell up to decoration; regular-regular edge gives full union and disjoint core rows. |
| E332 triangle-row union lemma | PROVED | Every M-triangle has core-row union at least24. |
| E332 G=4 | PROVED EMPTY | Exact support cell eliminated. |
| E332 G=5 | PROVED EMPTY | All h=0,1,2 support cases eliminated. |
| E332 G=6 | PROVED EMPTY | h0, h1, and H2-G6-K4 all eliminated; standalone full proof. |
| E332 G=7,h=0 | PROVED EMPTY | k=3..7 all eliminated; `backend/E332_G7_H0_REDUCTION.md` now contains full closure. |
| E332 G7/G8 one-high uniform reduction | PROVED | High missing-degree11 impossible; high degree12 has at most one low-active decorated vertex; one-active states satisfy `k+r<=11`, with `r>=4` for G7 and `r>=3` for G8. See `backend/E332_G7_G8_H1_UNIFORM_REDUCTION.md`. |
| E332 H2-G7-K4minusE | PROVED EMPTY | Row-class reduction + low-repivot decoration overflow: a row class of multiplicity m sends the plateau shell to decoration `7+2m>=9`, impossible since q=30 and z>=22. |
| E332 G=7,h=1 | OPEN / SHARPLY REDUCED | Only universal-high zero/one-active parameter windows remain. |
| E332 G=8,h=0 | OPEN | No-high branch. |
| E332 G=8,h=1 | OPEN / SHARPLY REDUCED | Only universal-high zero/one-active parameter windows remain; no h=2,G=8 state exists. |
| Matching-transversal rigidity | PROVED | Front-end block tool. |
| Equality rotation of genuine blocks | PROVED | Closes high-cross seven/eight-block alternatives. |
| Eight genuine K12 blocks => legitimate R(4,49) | PROVED | Full residual contract. |
| Front-end contextual recurrence | COMPUTATION_CERTIFIED | 1752 nodes, 144 outer stops, two independent implementations. |
| Front-end dichotomy `K145 -> R449 OR T61` | PROVED | No backend circularity. |
| T61 residual alpha=5 | PROVED | Contextual no-extraction. |
| T61 anchor defect z=0 | PROVED | Matching-transversal contradiction. |
| generic R(4,48) floor310 | PROVED | q20 leaf-rotation over CORE211. |
| T61 minimum-degree12 branch | PROVED EMPTY | q20 rotation + R448 floor310. |
| T61 E397 | PROVED EMPTY | Repository-canonical. |
| T61 E398 | PROVED EMPTY | q23 shell contradiction. |
| T61 E399 | PROVED EMPTY | q24 cells. |
| T61 E400 | PROVED EMPTY | uniform q25 shell theorem. |
| T61 E401--E404 Line-A V6 package | SOURCE_REPORTED_PROVED / REPLAY_PENDING | Reported uniform q<=29 shell theorem + 127-row rational certificate; package-level window becomes E405--E408. |
| T61 E405..E408 | OPEN | Remaining package-level front-end window if V6 replay is accepted. |
| Line-B V2 adjacent two-pivot system | SOURCE_REPORTED | Exact exchange identities; reverse equality not independent. |
| Line-B V2 q34/q35 quotient compression | SOURCE_REPORTED | 76 necessary quotient rows; triangle-free non-bipartite branch eliminated. |
| Line-B V2 local q30--q33 certificates | SOURCE_REPORTED | Four exact local certificates refute naive one-step Phi monotonicity. |
| E333..E340 elimination | OPEN | No high layer closed by V2. |
| Full EG617 r=12 theorem | OPEN | Must not be claimed solved. |
