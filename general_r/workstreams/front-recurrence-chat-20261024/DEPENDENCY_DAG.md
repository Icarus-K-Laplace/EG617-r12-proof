# Dependency DAG — Front Recurrence Round 2

Date: 2026-10-24  
Status: **two threshold cutoffs proved; seed envelope and all-state dominance open.**

```mermaid
flowchart TD
  A[Contextual contract: alpha(J)<=a, omega(J)<=r-1, inherited D_r caps]
  B[Complement H: omega(H)<=a, alpha(H)<=r-1, e(H)>=(r-1)p_r(n)]
  C[a=2: H triangle-free, Delta(H)<=r-1]
  D[n>=2r+1: p_r(n)>n/2 contradicts edge cap]
  E[n=2r: equality forces H (r-1)-regular]
  F[AES theorem for r>=6 forces H bipartite]
  G[M_r(2)<=2r-1 for r>=6]
  H1[a=3 minimum-degree pivot]
  I1[Core has alpha<=2; size <=2r-1]
  J1[Degree/cap inequality 2(r-1)p_r(n)>n(2r-1)]
  K[M_r(3)<=3r for r>=6]
  L[Eliminate outer t=1 states a=2,3]
  M[Five seed excess formulas]
  N[All-state outer-budget dominance]
  O[All-large-r front closure]
  A-->B-->C
  C-->D
  C-->E-->F-->G
  D-->G
  G-->H1-->I1-->J1-->K-->L
  M-->N-->O
  L-->N
```

## Node status

- **Proved, threshold (r\ge6):** (M_r(2)\le2r-1), (M_r(3)\le3r).
- **Proved, all (r>3):** no contextual (a=2) state with (n\ge2r+1).
- **Proved, threshold (r\ge6):** outer t=1 states ((a,n)=(2,2r+1),(3,3r+1)) are empty.
- **Conditional:** (a=4,n=4r+1) is excluded only under the no-extraction reductio; otherwise it is the target residual.
- **Open:** general-r excesses at the five seed coordinates, and the remaining all-state integer dominance.
- **Not proved:** any explicit (r_0) for the EG617 theorem.

## Cross-line interface status

I's local slack-gap theorem is about the full counterexample coloring's (q^2)-point neighborhood (W=V\setminus\{x\}). It does not apply to arbitrary H residual states of order (ar+O(1)) with only (alpha\le a); no H seed floor is inferred from it. The cutoff proofs above use H's own inherited-cap contract and the named external AES theorem.