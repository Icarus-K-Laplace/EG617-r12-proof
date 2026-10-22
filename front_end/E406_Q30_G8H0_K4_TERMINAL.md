# E406 q30 plateau: unique G8/h0 terminal

Status: `PROVED` reduction. The terminal geometry below remains to be eliminated.

Assume the E406 q30 global-maximum contract, no regular d3/d10 root, `G=8`, `h=0`.

The active/inactive inequalities from the generic shell analysis transfer verbatim through all cases except the E332-specific final K4-row-cover step. In particular:

- m=0 is impossible;
- m=1 is impossible;
- m>=3 is impossible;
- m=2 forces k<=6;
- k=5 and k=6 are impossible by shell pair/triangle weight contradictions.

Thus the only survivor is

`m=2, k=4`.

Let x,y be the active decorated vertices and u,v the inactive ones. Exact accounting gives

- `J=M[D]=K4`;
- `g_x=g_y=1`;
- `g_u+g_v=6`;
- `t_x=t_y=12`;
- `t_u+t_v=12`;
- `s=e_M(L,D)=16`.

The missing triangles xuv and yuv have total row-size exactly24. Since every missing triangle in T61 has core-row union at least24, equality forces

- `D_x,D_u,D_v` pairwise disjoint;
- `D_y,D_u,D_v` pairwise disjoint.

Also

`|D_x|=|D_y|=12`,
`|D_u|+|D_v|=12`.

The four shell vertices x,y,u,v form a missing K4. In T61, any two core vertices outside all four rows would be target-nonadjacent only at the cost of an independent6-set with this missing K4. Hence the uncovered core is a clique, and therefore has size at most11. Equivalently the four-row union has size at least36.

But

`|D_u union D_v|=12`

and this union is disjoint from both D_x and D_y. Therefore

`12+|D_x union D_y|>=36`.

Since both D_x,D_y have size12, equality forces

`D_x intersect D_y=empty`.

Thus all four rows are pairwise disjoint and their union has exactly36 vertices. The remaining11 core vertices form a target K11.

So the unique E406 G8/h0 plateau terminal is:

> four pairwise-disjoint decorated core rows of total size36, with the 11 uncovered core vertices inducing K11.

This is the E406 replacement for the E332 full-K4-row-cover terminal. The next step is to combine the nine low rows (total16 incidences), the 11-clique remainder, and the 285-core excess budget `sum(d_C-12)=6` to force a q31 repivot or contradiction.
