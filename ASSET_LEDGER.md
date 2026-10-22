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
| E332 G=4 | PROVED EMPTY | Exact `(h,k,l)=(2,4,7)` cell eliminated. |
| E332 G=5 | PROVED EMPTY | All h=0,1,2 support cases eliminated. |
| E332 triangle-row union lemma | PROVED | Every M-triangle has core-row union at least24; equality total-size24 forces pairwise row disjointness. |
| E332 G=6,h=0 | PROVED EMPTY | Active/inactive decorated support contradiction. |
| E332 H2-G6-K4 | PROVED EMPTY | Triangle-row equality plus zero-gap gives three disjoint 12-sets in a 35-core. |
| E332 G=6,h=1 | PROVED EMPTY | Complete high-degree11/12 case split for k=3..6. |
| E332 G=6 | PROVED EMPTY | Full decoration layer closed; see `backend/E332_G6_FULL_CLOSURE.md`. |
| E332 remaining decoration range | OPEN | Only G=7,8 remain. |
| Matching-transversal rigidity | PROVED | Front-end block tool. |
| Equality rotation of genuine blocks | PROVED | Closes high-cross seven/eight-block alternatives. |
| Eight genuine K12 blocks => legitimate R(4,49) | PROVED | Full residual contract. |
| Front-end contextual recurrence | COMPUTATION_CERTIFIED | 1752 nodes, 144 outer stops, two independent implementations. |
| Front-end dichotomy `K145 -> R449 OR T61` | PROVED | No backend circularity. |
| T61 residual alpha=5 | PROVED | Contextual no-extraction. |
| T61 anchor defect z=0 | PROVED | Matching-transversal contradiction. |
| generic R(4,48) floor 310 | PROVED | q20 leaf-rotation over CORE211. |
| T61 minimum-degree12 branch | PROVED EMPTY | q20 rotation + R448 floor310. |
| T61 E397 | PROVED EMPTY | Unique degree14 cannot be adjacent to any degree13 pivot. |
| T61 E398 | PROVED EMPTY | q23 shell contradiction. |
| T61 E399 | PROVED EMPTY | q24 cells. |
| T61 E400 | PROVED EMPTY | uniform q25 shell theorem. |
| T61 E401--E404 Line-A V6 package | PACKAGE_AUDIT_PENDING | User/Astra report says PROVED; not yet promoted to repository-canonical status pending independent replay. |
| T61 E405..E408 | OPEN | If V6 passes audit, this is the remaining front-end window. |
| S31 strict descent | PROVED | Only E406/delta13 explicit parent. |
| S27 closure | CONDITIONAL / SCOPE-LIMITED | Requires exact minimum-degree premise. |
| canonical S30 coverage from arbitrary T61 | OPEN | Must not be assumed. |
| Line-B V2 high-layer package | PACKAGE_AUDIT_PENDING | E333--E340 remain open; V2 reports two-pivot identities and quotient-state compression. |
| E332 elimination | OPEN | Reduced to G=7,8. |
| E333..E340 elimination | OPEN | Line B. |
| Full EG617 r=12 theorem | OPEN | Must not be claimed solved. |
