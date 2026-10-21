# E398 exact q23 shell classification

Status: `PROVED` for the local cell described below.

## Local cell

Let `R` be a T61 residual with `E=398`. Its degree multiset is `14^3,13^58`.

Take a degree-13 pivot `p` adjacent to one of the three degree-14 vertices. Then the already proved excess-neighbour bound gives the exact pivot data

`q=23`, `z=22`, `G=1`, `e(C47)=284`.

Let `A=N(p)` be the 13-shell, `M=complement(R[A])`, and let `x in A` be the unique degree-14 shell vertex. Thus

`g_x=1`, all other shell decorations are zero, and `e(M)=22`.

## Theorem

The missing graph `M` has a unique normal form up to the location of the decorated vertex:

`M = (K_{2,11} plus the edge joining the 2-side) minus one cross edge`.

Equivalently its degree multiset is

`12,11,2^10,1`.

The two high-degree vertices will be called the centres; the remaining 11 vertices are independent in `M`, ten of them have missing degree2 and one has missing degree1.

The decorated vertex `x` may lie on a centre or a leaf; the graph normal form itself is fixed.

## Proof

### 1. M is K4-free and not triangle-free

An M-K4 consists of four pairwise target-nonadjacent shell vertices. Their core rows must cover at least 36 of the 47 core vertices: otherwise the remaining at least12 core vertices contain an independent2-set, producing an independent6-set in R. For the four K4 vertices S,

`q >= t(S)-e_M(S) >=36-6=30`,

contradicting q=23. Hence M is K4-free.

On the other hand, the shell matching lemma for h=13 supplies a 3-matching. If M were triangle-free, the six matching endpoints have total row weight at least `3*11=33`; Mantel gives at most9 missing edges on those six endpoints, so

`q>=33-9=24`,

again contradicting q=23. Hence M contains a triangle.

### 2. Fix a triangle T

Let `T` be any M-triangle and let `B=A\T`, |B|=10. Put

- `c=e_M(T,B)`,
- `u=e_M(B)`.

Since e(M)=22,

`3+c+u=22`, so `c+u=19`.

The three core rows of T must cover at least24 core vertices: otherwise three mutually nonadjacent shell vertices together with an independent3-set in the uncovered core would form an independent6-set. Therefore

`t(T)>=24`.

If the decorated vertex x is outside T, `t(T)=6+c`, so c>=18 and u<=1.
If x lies in T, `t(T)=7+c`, so c>=17 and u<=2.

### 3. The outside graph B has no missing edge

Suppose `rs` is an M-edge inside B.

Every B-vertex has at most two neighbours in T because M is K4-free. Also `u<=2`. Thus an undecorated B-vertex has weight at most4. If x lies outside T, the decorated B-vertex has weight at most5; if x lies in T all B-vertices are undecorated.

Hence for any possible outside edge rs,

`t_r+t_s <=9`.

But an M-edge requires the union of its two core rows to have size at least11, and therefore `t_r+t_s>=11`. Contradiction.

Thus

`u=0`, `c=19`.

So B is independent in M. K4-freeness implies every B-vertex has at most two neighbours in T. Nineteen incidences over ten vertices therefore mean exactly nine B-vertices have two T-neighbours and one has one T-neighbour.

### 4. One triangle vertex has no B-neighbour

Among the nine 2-neighbour B-vertices, at least eight are undecorated (all nine are undecorated if x lies in T). Such a B-vertex has weight2. Therefore each triangle vertex adjacent to one of these ordinary 2-neighbour vertices must have weight at least9 by the pair-cover inequality.

If all three triangle vertices met an ordinary 2-neighbour B-vertex, their total weight would be at least27. But with c=19,

`t(T)=25` when x is outside T and `t(T)=26` when x lies in T.

Hence some triangle vertex has no ordinary 2-neighbour in B.

It cannot be adjacent only to the unique 1-neighbour B-vertex: its own weight would then be at most4 (including the possible decoration), while that B-vertex has weight at most2, violating the required edge weight sum at least11.

If x lies outside T, it also cannot be the sole B-neighbour of this triangle vertex: the resulting weights are again far below11.

Therefore one triangle vertex has no B-neighbour at all.

### 5. The remaining two vertices are the global centres

All 19 T-B incidences are therefore carried by the other two triangle vertices. Since each B-vertex has at most two T-neighbours, one centre meets all ten B-vertices and the other meets nine.

Counting also the two triangle edges incident to each centre gives M-degrees12 and11. The third triangle vertex has M-degree2. Among B, nine vertices have degree2 and one has degree1.

There are no edges in B, so the two centres are joined to an independent 11-set consisting of the third triangle vertex and B, with exactly one missing centre-leaf incidence, and the centres are adjacent to each other.

This is precisely

`(K_{2,11} + centre edge) - one cross edge`.

## Immediate structural consequences

For the pivot p:

- shell target degrees are 0 and1 at the two centres, 10 at each ordinary degree2 leaf, and11 at the unique degree1 leaf;
- an undecorated centre has core-row size11 or12;
- an undecorated ordinary leaf has core-row size2;
- the decorated degree14 shell vertex has core-row size `d_M(x)+1`.

This normal form must occur around every degree13 vertex adjacent to a degree14 vertex in an E398 survivor, so the global graph contains at least 36 such exact local shells (counted by high-low incidences, before high-high corrections). The next open step is their multi-pivot compatibility.
