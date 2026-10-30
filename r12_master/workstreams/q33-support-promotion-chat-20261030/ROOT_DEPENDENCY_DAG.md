# Q33 local dependency DAG — support-promotion workstream

\`\`\`mermaid
flowchart TD
  P[Original E408 Q33 parent] --> WIT[Seven witnesses per exact-129 color]
  WIT --> SUP[Support floors m=8:31, m=9:32, m=10:34]
  WIT --> U[U-side reserve inequality]
  WIT --> W[W-side reserve inequality]
  SUP --> CELLS[Exact all-v,m,h arithmetic screen]
  U --> CELLS
  W --> CELLS
  CELLS --> EX[Excluded: 8:{31,32}; 9:{32,33}; 10:{34}]
  CELLS --> OPEN[Remaining scalar-feasible cells]
  OPEN --> NEXT[Full labelled component/gadget incidence theorem OPEN]
  NEXT --> ROOT[Q33 parent promotion OPEN]
\`\`\`

Gate statuses:
- Seven-witness interface: **PROVED_CONDITIONAL** under exact-129 factor and shell-label contracts.
- U/W inequalities: **PROVED_CONDITIONAL**.
- Arithmetic screen: **COMPUTATION_CERTIFIED**.
- Remaining graph-level completion: **OPEN**.
- Root promotion: **OPEN / NOT_CERTIFIED**.

This local DAG does not replace or edit the global root DAG.
