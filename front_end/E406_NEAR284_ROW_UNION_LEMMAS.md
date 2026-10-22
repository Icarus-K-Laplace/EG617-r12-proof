# E406 near-284 row-union lemmas

Status: `PROVED` under the explicit T61 E406 hereditary-cap contract.

Let `C` be any 47-point core arising from an E406 degree-13 pivot with

`e(C) in {284,285,286}`.

The established Line-A near-core theorem gives `delta(C)>=12`. The inherited core family has `alpha(C)<=4`, `omega(C)<=11`, and the hereditary smaller-core statements used below.

For a shell vertex x, write `D_x=N_C(x)` for its core row and `t_x=|D_x|`.

## 1. Missing shell edge => row union at least13

Let a,b be nonadjacent shell vertices, equivalently `ab in E(M)`. Put

`U=D_a union D_b`, `m=|U|`.

Every vertex of `C-U` is nonadjacent to both a and b. Hence an independent4-set in `C-U`, together with a,b, would make an independent6-set in the ambient T61 residual. Therefore

`alpha(C-U)<=3`.

We prove `m>=13`.

### m<=10

Then `|C-U|>=37`, contradicting the inherited fact `R(3,37)=empty`.

### m=11

Then `C-U` has36 vertices and therefore at least234 edges.

At most

`e(C)-234 <= 52`

core edges meet U. Hence

`sum_{u in U} d_C(u)
 <= (e(C)-e(C-U)) + e_C(U)
 <= 52 + C(11,2)
 = 107`.

But `delta(C)>=12` gives the lower bound132. Contradiction.

### m=12

Now `C-U` has35 vertices and at least211 edges. Thus at most

`e(C)-211 <=75`

core edges meet U, and

`sum_{u in U} d_C(u)
 <=75+C(12,2)
 =141
 <144`,

again contradicting minimum degree12.

Therefore

`|D_a union D_b|>=13`.   (PAIR-13)

This is stronger than the older weight-only edge inequality in the near-284 E406 regime.

## 2. Missing shell triangle => row union at least24

Let a,b,c form an M-triangle, i.e. they are pairwise nonadjacent in the ambient graph. Put

`U=D_a union D_b union D_c`.

Every vertex outside U is nonadjacent to all three shell vertices. If `|U|<=23`, then `C-U` has at least24 vertices. Any independent3-set there, together with a,b,c, gives an independent6-set in the ambient T61 residual. Thus the avoidance graph has independence number at most2.

But the inherited statement `R(2,24)=empty` forbids such a24-point avoidance set. Hence

`|D_a union D_b union D_c|>=24`.   (TRI-24)

## 3. Consequences for the d=3 q31 platforms

In every d=3 q31 platform, each active regular low b has a 3-point core support `U_b`.

### Type B platform

The three-point shell side has row sizes `(11,10,10)`.

PAIR-13 implies:

- every `U_b` is disjoint from each 10-row;
- `U_b` meets the 11-row in at most one vertex.

### Type A platform

The shell side has row sizes `(11,11,10)`, and the two 11-weight shell vertices are themselves nonadjacent, so they form an M-edge.

Let their rows be R1,R2 and the 10-row be R3.

For any active low support U:

- PAIR-13 gives `U intersect R3=empty`;
- TRI-24 on the shell triangle formed by the two 11-weight vertices and the active low gives
  `|R1 union R2 union U|>=24`.

Since `|R1|=|R2|=11` and `|U|=3`, this forces

`|R1 intersect R2|<=1`.

Moreover:

- if `|R1 intersect R2|=1`, then every active U is disjoint from `R1 union R2`;
- if `R1 intersect R2=empty`, then every active U meets `R1 union R2` in at most one vertex.

These are uniform support-location restrictions and will be used in the d=3 multi-support compatibility analysis.