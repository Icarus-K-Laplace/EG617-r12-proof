# E406 d=3: saturated 35-point remainder ledger

Status: `PROVED` under the four-triangle compression. E406 remains `OPEN`.

Let `T1,...,T4` be the four pairwise anticomplete K3 support classes in the q31 284-edge core C, and let H be the remaining35 core vertices.

Let D={d1,d2,d3} be the 3-point shell side of the q31 platform. No active B-shell vertex has any neighbour in H; the current pivot y has no core neighbours. Thus for x in H,

`d_R(x)=d_C(x)+s_D(x)`,

where `s_D(x)=|N_F(x) intersect D|`.

Write `eps_x=d_C(x)-12` and `h_x=d_R(x)-13`. Then

`h_x = eps_x+s_D(x)-1 >=0`.   (SAT)

The four support triangles already consume almost all of the ambient E406 degree excess, which makes (SAT) nearly an equality partition.

## 1. Type B: exact partition

Type B has no defective support class. All four triangles are pure degree12 K3s and anticomplete to D.

The support-class vertices contribute exactly all core-side ambient excess. Consequently

`sum_{x in H} h_x=0`.

Hence every H-vertex satisfies

`eps_x+s_D(x)=1`.

The four triangles carry no core excess, so the 35-point remainder has total core excess4. Therefore exactly

- 31 H-vertices have `eps=0`, `s_D=1`;
- 4 H-vertices have `eps=1`, `s_D=0`.

The D-row sizes are `(11,10,10)` and all D-to-core incidences lie in H. Thus the three D-rows are pairwise disjoint and partition exactly the31 degree12 H-vertices.

Moreover

- `e(H)=152`;
- the T-H incidence count is120;
- `sum_H eps=4`.

## 2. Type A: at most one unit away from a partition

Type A has at most one defective support class. Write

- `eta` for its internal core-excess contribution (`eta in {0,1}`);
- `xi` for its D-to-support cross defect (`xi in {0,1}`);

with `eta+xi=d<=1`.

Then

- T-H incidences = `120+eta`;
- `e(H)=152-eta`;
- `sum_H eps=4-eta`;
- D-to-H incidences = `32-xi`;
- `sum_H h = 1-d`.

### d=1

Every H-vertex has h=0, hence

`eps_x+s_D(x)=1`.

So the D-rows on H are pairwise disjoint:

- if `eta=1,xi=0`, they cover32 degree12 H-vertices and the remaining3 vertices have core degree13;
- if `eta=0,xi=1`, they cover31 degree12 H-vertices and the remaining4 vertices have core degree13.

### d=0

Now `sum_H h=1`. Thus exactly one H-vertex carries the unique ambient excess unit beyond the equality pattern. Consequently the D-rows are still a near-partition:

- either they are pairwise disjoint;
- or there is exactly one duplicated D-incidence, carried by a single core-degree12 H-vertex.

No H-vertex can lie in three D-rows.

## 3. Avoidance constraints supplied by the shell

Every active B-shell vertex is nonadjacent to all of H and to every D-vertex.

Therefore, for every j,

`alpha(H\R_j)<=3`,

where `R_j=N_H(d_j)`: otherwise four independent vertices of `H\R_j`, together with an active B-vertex and d_j, form an independent6-set in the T61 residual.

In Type A, d1 and d2 are themselves nonadjacent shell vertices. Hence

`alpha(H\(R1 union R2))<=2`:

three independent vertices outside both rows, together with an active B-vertex and d1,d2, would form an independent6-set.

The Type-A pair rows also satisfy `|R1 intersect R2|<=1` from the earlier TRI-24 support argument.

Thus the possible 35-point remainder is forced simultaneously by:

- 151/152 total edges;
- total core excess at most4;
- four pairwise anticomplete support triangles outside H;
- three D-rows that are an exact or one-unit-near partition;
- `alpha(H\R_j)<=3` for all j;
- in Type A, `alpha(H\(R1 union R2))<=2`.

This is the current exact normal form for the remaining d=3 final-rise class.