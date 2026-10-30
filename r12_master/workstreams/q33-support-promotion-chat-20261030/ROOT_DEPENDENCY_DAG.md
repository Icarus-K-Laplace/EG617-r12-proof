# Q33 local dependency DAG — variable-core support-promotion

\`\`\`mermaid
flowchart TD
  P[Original E408 Q33 parent] --> KP[Exact-129: ten K5 plus G11]
  KP --> CORE[Each component core size c_i<=4; gadget core g=47-sum c_i in 7..11]
  P --> WIT[Seven selected witnesses per exact color]
  WIT --> TYPES[No gadget: 7 component K4s; gadget: 6 component K4s + gadget Q]
  CORE --> GROUP[Variable residual component profiles (c_i,k_i)]
  TYPES --> GROUP
  GROUP --> GAD[alpha(C[G_C])<=2 gives p2 gadget-core U/W costs]
  WIT --> RES[U/W reserves with overlap cap4]
  GAD --> DP[Exact variable-core profile DP]
  RES --> DP
  DP --> EX[Excluded support cells]
  DP --> OPEN[Remaining profile-feasible cells]
  OPEN --> ROOT[Full labelled incidence theorem / root promotion OPEN]
\`\`\`

Statuses:
- Exact-129 factor and seven-witness interface: **PROVED_CONDITIONAL** under registered parent contracts.
- Variable-core reserve inequalities: **PROVED_CONDITIONAL**.
- Exact finite profile screen: **COMPUTATION_CERTIFIED**.
- Full labelled graph completion: **OPEN**.
- Root promotion: **OPEN / NOT_CERTIFIED**.


## 2026-10-30 component-only support branch

The canonical support branch now uses seven guaranteed isolated-K5 component K4s per exact-129 color, hence h=0. The selected 42m component edges are charged exactly once. The remaining three components per color have variable core sizes, and the gadget core contributes p_2 U/W costs. The resulting U/W reserve DP excludes the support ranges listed in OPEN_CASES.md; the remaining v>=39,40,41 ranges (for m=8,9,10) still require a labelled incidence argument. No root promotion is made.


## 2026-10-30 source profile and W boundary correction

The selected component-only support family forces at least one remaining shell vertex into the 11-vertex gadget. Therefore gadget core size is at most10 and the three unselected component core sizes sum to 9..12. The finite profile verifier uses this source-correct interval.

At the first aggregate survivors, the m=8,v=39 and m=9,v=40 W budgets are exactly saturated. The corresponding W cores are 4K2 and 3K2 union K1, and each exact-color W edge set is a matching of size3 or2. The m=10,v=41 W slack is at most3. These are child reductions only; no parent/root promotion is made.
