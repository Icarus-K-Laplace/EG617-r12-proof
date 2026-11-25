# Second h4 orbit: disjointness review

Frozen E286 Sections 3 and 6 use the support vector [1,0,1,0,0,1,1,0,0,0,0].
Its seed incidence counts are (3,2,2,2). The seed ledger gives private clique
sizes (10,11,11,11). Positive fibers give p of type 01, r of type 03, and q
of type 23. Their supports differ, so these are three distinct vertices.
Each has at least two seed neighbors and is outside every private clique.

| Case | Regions charged | Check |
|---|---|---|
| p misses K0 | p with K0 and K1, q with K2 and K3 | All private cliques are pairwise disjoint. Both points are exterior and distinct. Total at least 4+6. |
| p and r complete K0 | p and r, q with K2 and K3 | p and r are distinct exterior common completers. Neither belongs to the opposite region. Total at least 7+6. |
| p completes K0 and r misses K0 | r, q, A in K0, C in K2, B union D in K3 | These five regions are disjoint. The point p supplies one additional neighbor to each vertex in A. It is outside K3, hence outside B, and outside K0. |

For the mixed case take A and B to be the exact missing sets for r, C and D
those for q. Alpha at most four forces all A–B and C–D edges. On B intersect D
the forced sets A and C are disjoint, so ten internal neighbors give excess
at least (a+c-2) truncated at zero. On B minus D, q supplies one additional
neighbor, distinct from the internal neighbors and A. The lower bound is
(a-1) truncated at zero. On D minus B the analogous extra neighbor is r,
giving (c-1) truncated at zero. No adjacency among p, q, and r is required.

Summing over B union D bounds |B|(a-2)₊+|D|(c-2)₊. The mixed cost 5 and the
opposite cost 6 use precisely those two scalar terms on the shared clique.
Their sum then exceeds the global excess 8. Adding the two individual bounds
on actual clique excess without this overlap argument would be invalid.

Independent integer checks in attacks/h4-second-review.py cover 110 positive
mixed parameters and 48,048 feasible shared-leaf size/intersection tuples.
The scalar minimum 5 occurs only at (2,2). At (0,9) the cost vanishes, so the
separate K10 completion case is necessary. These checks cover integer
parameters. All statements about actual vertices are proved in Lean.
