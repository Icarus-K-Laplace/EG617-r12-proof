# E332 exact H2-G7-K4minusE row-class reduction

Status: `PROVED` for the reductions below. The exact cell is not yet empty.

Assume the exact surviving two-high G=7 state from `E332_H2_CLASSIFICATION.md`:

- high regular vertices `a,b`, with `ab notin E(M)` and `t_a=t_b=11`;
- decorated vertices `x,y`, with `xy in E(M)`, `g_x+g_y=7`, `t_x+t_y=13`;
- nine low regular vertices, each with missing neighbourhood `{a,b}`;
- the support `{a,b,x,y}` induces `K4-e`, missing only `ab`.

Write core rows

`A=D_a`, `B=D_b`, `X=D_x`, `Y=D_y`.

Then `|A|=|B|=11`, `|X|+|Y|=13`.

## 1. Exact triangle equalities

Both `a,x,y` and `b,x,y` are M-triangles. Their total row weights are

`11+13=24`.

The triangle-row union lemma says every M-triangle has row union at least24. Therefore equality holds, and hence

- `A`, `X`, `Y` are pairwise disjoint;
- `B`, `X`, `Y` are pairwise disjoint;
- `X cap Y=empty` and `P:=X union Y` has size13.

Thus both A and B are disjoint from P.

Let

`r=|A cap B|`.

Partition the 35-core as

- `R=A cap B`, size r;
- `A0=A\B`, size 11-r;
- `B0=B\A`, size 11-r;
- `P=X union Y`, size13;
- `C` = the remaining vertices, size r.

For triangle `a,x,y`, the 11 vertices outside `A union P` form a clique; this set is exactly `B0 union C`.

For triangle `b,x,y`, the 11 vertices outside `B union P` form a clique; this set is exactly `A0 union C`.

Therefore both

`B0 union C` and `A0 union C`

are K11s in the core. In particular C is a clique.

## 2. The overlap parameter is 0 or at least9

For any `c in C`, the two K11 cliques force c to be adjacent in the core to

- all `r-1` other vertices of C;
- all `11-r` vertices of A0;
- all `11-r` vertices of B0.

Hence

`d_H(c) >= (r-1)+2(11-r)=21-r`.

The 211-core degree multiset is either `14,12^34` or `13^2,12^33`.

Thus:

- `1<=r<=6` would force a core degree at least15, impossible;
- `r=7` would force all seven C-vertices to have degree at least14, impossible;
- `r=8` would force all eight C-vertices to have degree at least13, impossible.

Therefore

`r=0 or r in {9,10,11}`.

## 3. Every low row lies inside P

Let u be any one of the nine low vertices. Since `N_M(u)={a,b}`, the legal d=2 repivot is a zero-slack plateau:

`t_a+t_b=22=d(13-d)`.

The exact repivot identity and `delta(H)>=12` therefore force:

- `D_u` has size2;
- its two vertices form an H-edge;
- both endpoints have core degree12;
- `D_u cap A=empty` and `D_u cap B=empty`.

Hence initially

`D_u subseteq P union C`.

If `r=0`, C is empty and we are done.

Assume `r>=9` and suppose an endpoint `c of D_u` lies in C. Since C is a clique of size at least9 and the whole 211-core has only two units of degree excess, among the vertices of `C\D_u` there exists a degree12 vertex `c'`.

Under repivot at u, the new core is

`H_u=(H\D_u) union {a,b}`.

The vertex c' is outside A union B, so it gains no new neighbour from a or b. But c' is adjacent to c because C is a clique, so it loses at least one neighbour when D_u is removed. Thus its new core degree is at most11, contradicting the universal minimum-degree12 theorem for the repivoted 35-core.

Therefore no endpoint of D_u lies in C, and

`D_u subseteq P=X union Y`

for every low u.

## 4. Distinct low-row edges are disjoint

Each low row D_u is now an H-edge on the 13-point set P, and both endpoints have core degree12.

Suppose two different low rows are distinct edges sharing one endpoint:

`D_u={c,d}`, `D_v={c,e}`, with `d!=e`.

Repivot at u. The vertex e remains in the new core, has original core degree12, and lies in P, hence outside A union B. It therefore gains no new neighbour from a or b.

But e is adjacent in H to the removed vertex c because `{c,e}=D_v` is an H-edge. So e loses a core neighbour and receives no replacement, leaving degree at most11 in the repivoted core. Contradiction.

Thus any two distinct low-row edges are vertex-disjoint.

## 5. Finite row-class consequence

The 13-point set P contains at most six pairwise vertex-disjoint edges. Therefore the nine low rows can use at most six distinct H-edges.

Consequently the nine lows split into at most six equality classes according to identical row edge, and at least one row class has multiplicity at least2.

This converts the exact H2-G7-K4minusE cell from a free incidence problem into a finite row-multiplicity / repivot-consistency problem.

## Current target

Use repivot at representatives of repeated row classes. Each such repivot lands in either another G7/h2 plateau view or a G8/h1 view. Combine the row-class multiplicities with `E332_G7_G8_H1_UNIFORM_REDUCTION.md` to eliminate all possible class patterns.
