# Front-end dependency DAG

Overall bridge status: **OPEN**. The terminal-obstruction reduction is **PROVED**. Detailed statuses are tracked in `ASSUMPTION_LEDGER.md`.

```mermaid
flowchart TD
  H[Hypothetical balanced K145] --> C[Least colour m <= 870 / alpha12 / D caps]
  C --> M[K12 matching property]
  M --> T[Matching-transversal rigidity]
  T --> ROT[Equality rotation saturates all twelve cross slots]
  ROT --> B8[Eight genuine blocks imply alpha49 <= 4]
  ROT --> B7[Seven genuine blocks imply alpha61 <= 5]
  K8[Eight genuine blocks exist: OPEN] --> B8
  LOW[R224 / generic delta R335 >= 12] --> R37[R336 floor234 / R337 empty]
  R37 --> MAX[No nine-block packing]
  C --> MAX
  MAX --> F[Legitimate induced R449]
  B8 --> F
  F --> P[All legal degree13 pivots / exact inherited shell contracts]
  C --> BROOKS[Original minimum degree <= 11]
  BROOKS --> AN[Maximal anchored genuine K12 packing]
  M --> AN
  AN --> LED[Exact ledger with sigma z g x y]
  AN --> INH[Induced contextual R-class at each maximal stop]
  NF[Temporary no induced R449 in THIS G] --> CUT[Contextual a4 order cutoff48]
  LOW --> SEEDS[Generic floors131 / 210 / 234 / 308]
  CORE[Audited universal R447 floor284] --> REC[Exact finite inductive recurrence]
  SEEDS --> REC
  CUT --> REC
  REC --> CERT[1752-node certificate /144 stop comparisons]
  CERT --> ONE[Only d11 j6 a5 n61 stop]
  LED --> ONE
  INH --> ONE
  ONE --> TERMINAL[Embedded T61 / E397..408 / min degree12 or13]
  TERMINAL -. OPEN exclusion or49 extraction .-> F
  TERMINAL --> FILTER{E406 and min degree13 verified?}
  FILTER -->|yes| S31[Certified S31: some q <= 30]
  S31 -. OPEN coverage .-> S30[Canonical S30 contracts]
  S30 --> LAB[Specified row-labelled 5788 branch]
  LAB --> EDGE[Singleton cross-edge count k=0,1,2]
  EDGE -->|k2| CLOSED[Analytic singleton-triangle closure]
  EDGE -->|k0 or k1| NEW[New saturation and forced-edge lemmas]
  NEW --> REST[14 and13 necessary scalar cases / completion OPEN]
```

## No circular back-end dependence — PROVED

The temporary no-R449 hypothesis is not an imported theorem about R449. It is the negation of extraction in one fixed original graph. All recurrence operations remain induced subgraphs of that same graph. The final conclusion is a disjunction: extraction succeeds, or T61 survives.

The inputs to the recurrence stop at lower-order generic seeds. S27, S30 and S31 are downstream filters only, not premises for forcing the outer stop.

## Interfaces that must not be collapsed

|Interface|Status|What is actually proved / missing|
|---|---|---|
|Eight genuine blocks -> R449|PROVED|Independence, clique maximality and hereditary caps verified|
|Anchored d11 plus seven genuine blocks -> R449|PROVED|The anchor is an independent representative, not an assumed clique|
|Six anchored blocks -> seven genuine unanchored blocks|OPEN|The candidate anchor needs z=0, or a different packing argument|
|Embedded T61 -> E406/delta13 parent|OPEN|Exact residual edge and minimum-degree cases remain|
|S31 q-descent -> actual outer extraction or block creation|OPEN|A changed pivot is not a changed graph or an extra clique|
|Row-labelled5788 with singleton triangle -> contradiction|PROVED|Proof does not cover missing singleton edges without further argument|
|Every T61 survivor is one of these local objects|OPEN|This is a coverage theorem, not a consequence of local status labels|