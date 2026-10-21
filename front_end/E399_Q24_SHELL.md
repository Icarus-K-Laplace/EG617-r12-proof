# E399 q24 shell cells and closure

Status: `PROVED`.

This note closes the E399 T61 layer by eliminating the two exact q24 shell cells that can occur around low-degree vertices adjacent to positive-excess vertices.

## Common shell contract

Let `R` be a T61 residual with `E=399`, `delta(R)=13`. For a degree-13 pivot `p`, write

`A=N(p)`, `|A|=13`, `C=R-N[p]`, `|C|=47`, `M=complement(R[A])`.

Let `z=e(M)`, decorations `g_a=d_R(a)-13`, `G=sum_A g_a`, weights `t_a=d_M(a)+g_a`, and `q=z+G`.

The inherited facts used below are:

- `alpha(M)<=10` (an independent 11-set in M plus p would form a target K12);
- every M-edge has endpoint row-weight sum at least11;
- every M-triangle has total row weight at least24;
- an M-K4 would force q at least30, hence M is K4-free in the q24 cells;
- the h13 shell has a 3-matching;
- every 47-core in these exact cells has at least284 edges, so in E399 every degree-13 pivot has `q<=24`.

We eliminate two cells:

1. `(q,z,G)=(24,22,2)`;
2. `(q,z,G)=(24,23,1)`.

---

## Theorem A. The cell (q,z,G)=(24,22,2) is impossible

### A1. Triangle-free case

Take three disjoint M-edges and let S be their six endpoints. Pair-row coverage gives `t(S)>=33`. Mantel gives `e_M(S)<=9`. The subset identity gives

`24=q >= t(S)-e_M(S) >=33-9=24`.

Thus equality holds throughout:

- `t(S)=33`;
- `M[S]=K3,3`;
- the seven outside vertices B are independent in M;
- `G_B=0`.

A 4-matching would similarly give `q>=44-16=28`, so the matching number is exactly3.

Because B is independent and triangle-freeness prevents a B-vertex from meeting both sides of the K3,3, the whole M is bipartite. By König, M has a vertex cover of size3. Any size-3 cover of the induced K3,3 is exactly one of its bipartition sides. Hence all S-B edges meet one side, call it X; the opposite side Y has no outside attachments.

There are `22-9=13` S-B edges. Summing the nine K3,3 edge inequalities gives equality on every K3,3 edge, so the three X-vertices have a common weight a and the Y-vertices have weight `11-a`.

Since Y has no outside attachments,

`3(11-a)=9+G_Y`.

Here `0<=G_Y<=2`, so necessarily `a=8`, `G_Y=0`.

Every B-vertex adjacent to X is undecorated and must satisfy

`d_M(b)+8>=11`,

hence `d_M(b)=3`: every nonisolated B-vertex is adjacent to all three X-vertices. Therefore the number of S-B edges is a multiple of3, contradicting 13.

So the triangle-free channel is impossible.

### A2. Triangle case

Fix an M-triangle T and let B be the other ten shell vertices. Put

`c=e_M(T,B)`, `u=e_M(B)`.

Since z=22,

`c+u=19`.

Triangle row coverage gives

`6+c+G_T=t(T)>=24`,

hence

`u+G_B<=3`.

If rs were an M-edge inside B, K4-freeness gives at most two T-neighbours for each endpoint. Moreover

`d_B(r)+d_B(s)<=u+1`.

Thus

`t_r+t_s <=4+(u+1)+G_B <=8`,

contradicting the required edge weight sum at least11. Therefore `u=0`, `c=19`.

So B is independent; nine B-vertices have T-degree2 and one has T-degree1.

At least seven of the nine degree-2 B-vertices are undecorated. Any triangle vertex incident with such a regular degree-2 B-vertex has weight at least9.

If all three triangle vertices meet a regular degree-2 B-vertex, then `t(T)>=27`. Since `t(T)=25+G_T<=27`, equality forces `G_T=2`, all three triangle weights equal9, and `G_B=0`. But then the unique regular degree-1 B-vertex requires its triangle neighbour to have weight at least10, contradiction.

Hence some triangle vertex i meets no regular degree-2 B-vertex. We show it meets no B-vertex at all. Its possible B-neighbours are only decorated degree-2 vertices and the unique degree-1 vertex. The number of decorated degree-2 vertices is at most `G_B`, and `g_i<=G_T`, so with `h_i=c_i+g_i` we have

`h_i<=G_B+1+G_T=3`.

If i met a decorated degree-2 vertex with decoration r>=1, the edge inequality would give

`h_i>=7-r>=5`, contradiction.

If i met the degree-1 vertex with decoration r>=0, the edge inequality would give

`h_i>=8-r>=6`, contradiction.

Thus i has no B-neighbour. Then B together with i is an independent 11-set in M, contradicting `alpha(M)<=10`.

Therefore `(q,z,G)=(24,22,2)` is impossible.

---

## Theorem B. The cell (q,z,G)=(24,23,1) is impossible

### B1. Triangle-free case

The same 3-matching equality gives an induced K3,3 on six endpoints, an independent outside set B of size7, `G_B=0`, matching number exactly3, and a bipartite graph whose size-3 vertex cover is one side X of the K3,3.

Now there are `23-9=14` S-B edges, all incident with X. The opposite side Y has no outside attachments. Since total decoration is1,

`3(11-a)=9+G_Y`, `0<=G_Y<=1`,

again forcing `a=8`, `G_Y=0`.

Every nonisolated B-vertex must then have missing degree3 and meet all of X. Hence the number of S-B edges is divisible by3, contradicting 14.

### B2. Triangle case

For a triangle T and outside B10, z=23 gives

`c+u=20`.

Triangle coverage and total decoration1 again imply

`u+G_B<=3`.

The same endpoint estimate excludes any edge inside B, so `u=0`, `c=20`. Thus every B-vertex has T-degree2.

If some triangle vertex meets no regular B-vertex, it can meet at most the unique decorated B-vertex; the edge inequality is then incompatible with the bound on its own `c_i+g_i`, so that triangle vertex has no B-neighbour and B plus it is an independent 11-set, impossible.

Therefore all three triangle vertices meet regular degree-2 B-vertices and each has weight at least9.

Here `t(T)=26+G_T`. If `G_T=0`, this contradicts `t(T)>=27`. Hence `G_T=1`, `G_B=0`, and all three triangle weights are exactly9.

Choose any B-vertex y. It is undecorated, has missing degree2, and its two missing neighbours are adjacent in the triangle. Repivot at y. If D is its 2-vertex core row, the exact repivot identity simplifies to

`q_y-q = I_C(D)-t_a-t_b+e_R({a,b},D)`.

The 47-core has minimum degree at least12, so `I_C(D)>=23`, while `t_a=t_b=9`. Hence

`q_y-q>=5`,

so `q_y>=29`.

But in the same E399 graph every degree-13 pivot satisfies `q_y<=24` from the 284-core floor. Contradiction.

Thus `(q,z,G)=(24,23,1)` is impossible.

---

## E399 closure

The total degree excess above13 in E399 is5. The canonical neighbour-excess bound shows no vertex can have excess at least3, so the only degree-excess partitions are

- `2+2+1`;
- `2+1+1+1`;
- `1+1+1+1+1`.

If a degree15 vertex exists, it has many degree13 neighbours; any such low neighbour sees excess2 and lies in the impossible `(24,22,2)` cell. Hence the first two partitions are impossible.

It remains to consider `14^5,13^56`.

A degree13 vertex cannot be adjacent to two degree14 vertices, because that again gives `(24,22,2)`. It also cannot be adjacent to exactly one degree14 vertex:

- if q=23, then `(z,G)=(22,1)` and the already proved q23 shell classification from `E398_Q23_SHELL.md` applies; its forced missing graph has an independent 11-set, contradiction;
- if q=24, then `(z,G)=(23,1)`, excluded by Theorem B above.

So no degree13 vertex can be adjacent to any degree14 vertex. But each degree14 vertex has only four other positive-excess vertices available and needs fourteen neighbours. Contradiction.

Therefore

`T61(E399)=empty`.

The surviving h13 front-end window is now

`400<=E<=408`.
