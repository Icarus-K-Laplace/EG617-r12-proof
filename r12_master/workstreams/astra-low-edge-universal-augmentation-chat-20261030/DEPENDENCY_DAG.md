# Independent dependency DAG

Date: 2026-10-30. All statuses refer to the statements' explicit hypotheses.

```mermaid
flowchart TD
  B[Elementary shortest odd cycle + Mantel] --> C[25-point capacity and common-neighbor bound: PROVED]
  KP[Kang-Pikhurko n25,r2: audited alternative] -.-> C
  C --> A[Safe augmentation at every step: PROVED]
  U[Exact285 U6: independently audited] --> L[47-point low-edge obstruction: PROVED]
  A --> L
  C --> D[Direct total-excess-at-most6 proof: PROVED]
  D --> L
  B --> M2[R224 empty and121/122-neighborhood classification]
  M2 --> M3[R335 minimum degree12]
  M3 --> M4[R336 floor234; R337 empty]
  M4 --> M[Generic R447 minimum-degree gate: PROVED]
  M --> F[R447 strict floor286: PROVED]
  L --> F
  P[Actual h13 T61 contract + inherited caps] --> H[Induced47-core and E-91-q identity]
  H --> X[Four parent charge layers impossible: PROVED_CONDITIONAL]
  F --> X
  X --> Q[E407 q<=30; E408 q<=31]
  R[Other front-end and root coverage obligations: OPEN here] --> G[Global EG617: NOT PROMOTED]
```

## Exact input ledger

| Node | Minimal input | Status |
|---|---|---|
|C|n47,e<=285,delta>=12,alpha<=4,omega<=11;25-point triangle-free upper145|PROVED|
|A|C applied anew at every current graph; exact285 U6 only at terminal|PROVED|
|L via augmentation|A plus independently audited U6|PROVED|
|L direct|T<=6, elementary Turan, C, private-clique blockers and pointwise inequalities|PROVED|
|M|R447 including all inherited D-caps, e<=286; reconstructed R224/R335/R336/R337 chain|PROVED|
|F|M and L; no exact284 theorem or127-row certificate|PROVED|
|H|actual61-point h13 F, alpha<=5,omega<=11, induced caps; chosen degree13 pivot|PROVED_CONDITIONAL on parent contract|
|X|H and F; charges as in the matrix|PROVED_CONDITIONAL on parent contract|
|Finite arithmetic/type replay|self-contained new verifier; no sibling-code import|COMPUTATION_CERTIFIED|
|Global original problem|all other parent/coverage dependencies|OPEN here|

The exact284 Q33 theorem is audited as a cross-check, not a premise of L. Q33's minimum-degree source is credited as the starting source for M, and its omitted type classification is reconstructed here. V11, V12, MS-29, selected support unions, exact129 factorization, degree-nine assertions, and target omega<=5 are absent from every new proof path.

The two proofs of L share C and the private-clique ideas; they are not claimed to be statistically or conceptually unrelated. The augmentation path uses U6 as a theorem, while the direct path reproduces the structural contradictions under T<=6 without invoking U6.
