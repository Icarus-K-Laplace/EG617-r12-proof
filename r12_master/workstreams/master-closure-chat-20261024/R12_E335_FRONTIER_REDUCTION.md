# E335 reduced to a q=30 / 214-edge-core equality contract

Status: **PROVED_CONDITIONAL** on the registered q27 shell closure and q28/q29 repivot theorems.

## Theorem

Assume F is a legal 49-point residual with E=e(F)=335, with the full all-pivot legal-core contract. Then F has a degree-13 pivot p such that

- q_p=30;
- e(H_p)=214;
- K(H_p)=2e(H_p)-420=8;
- H_p contains three pairwise nonadjacent degree-12 vertices.

## Proof

The universal legal-core floor gives e(H_y)>=214 for every degree-13 pivot y. Hence the exact pivot identity yields

q_y=335-91-e(H_y)<=30

for every pivot.

The registered q27 shell closure excludes q=27. If a pivot has q=28, the q28 profitable-repivot theorem produces a degree-13 pivot with q'>=30. If a pivot has q=29, the q29 good-repivot theorem produces a degree-13 pivot with q'>=30. Since every pivot also satisfies q'<=30, either case produces a q=30 pivot. If the initial pivot already has q=30, the conclusion is immediate.

At q=30, the exact identity gives e(H_p)=335-91-30=214, hence K(H_p)=8.

Finally, K=8 means at most eight vertices have degree above12, so at least27 vertices have degree12. Since omega(H_p)<=11, choose a nonadjacent degree-12 pair a,b. Their open neighbourhoods have total size at most24, leaving at least nine vertices nonadjacent to both. At most eight vertices in H_p have degree above12, so at least one of those common nonneighbours has degree12. This gives three pairwise nonadjacent degree-12 vertices. QED.

## Exact remaining E335 contract

The universal core floor and low-charge repivots do not by themselves eliminate E335. They reduce it to the following single equality question:

> Can a legal 49-point residual have a degree-13 pivot p with q_p=30 and a 35-core H_p satisfying alpha(H_p)<=3, omega(H_p)<=11, delta(H_p)>=12, e(H_p)=214, together with all exact shell-row, decoration, and induced-set cap constraints?

The registered three-anchor theorem gives the lower bound K>=8 and is therefore tight at this boundary; it does not eliminate K=8. The next proof must exploit the simultaneous q=30 shell contract and the K=8 core equality structure, or prove a stronger legal-core floor.

## Status boundary

This is a reduction, not an E335 closure. E335 remains OPEN until the q=30 / e(H)=214 equality contract is eliminated or shown to force a contradiction with the shell.
