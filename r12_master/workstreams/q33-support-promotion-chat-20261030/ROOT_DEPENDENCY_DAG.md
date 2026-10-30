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
