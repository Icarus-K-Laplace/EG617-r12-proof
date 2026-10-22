# T61 E401--E404 canonical closure

Status: `PROVED EMPTY` for all four edge layers under the explicit T61 hereditary-cap h13 contract.

This file independently reconstructs the V6 analytic proof body. It does not rely on the V6 result label, S30, S31, E332, or any E333--E340 backend theorem.

## Common setup

Let R be a 61-vertex graph with

- `delta(R)>=13`;
- `alpha(R)<=5`;
- `omega(R)<=11`;
- all inherited density caps `D(n)`.

At a degree-13 pivot p write

- `A=N(p)`, `|A|=13`;
- `C=R-N[p]`, `|C|=47`;
- `M=complement(R[A])`;
- `g_a=d_R(a)-13`;
- `t_a=d_M(a)+g_a`;
- `z=e(M)`, `G=sum g`, `q=z+G`.

Exact counting gives

`E=91+q+e(C)`.

The inherited 14-point cap gives `z>=22`, and `alpha(M)<=10`.

We use the accepted universal 47-core floor

`e(C)>=284`.

## 1. Universal <=288 core interface

For every inherited `C in R(4,47)` with `e(C)<=288`,

`delta(C)>=12`.

A degree at most9 would leave a forbidden 37-point `R(3,37)` object. Degree10 would leave a 36-core of at least234 edges and force `e(C)>=289`.

For degree11, use the 11-shell / 35-core decomposition. A missing shell edge exists. Its two rows cover at least12 points by the lower-order `R(2,24)` exclusion, so the shell charge is at least11. CORE211 then gives

`e(C)>=66+11+211=288`.

At equality, the two rows are disjoint and cover exactly12 core vertices. Their 23-point complement has at least131 edges. Exact cut counting then forces at least64 edges inside the 12-row union. Adding the two shell vertices gives a 14-set with at least76 edges, violating `D(14)=69`.

Hence degree11 is impossible.

### EDGE13

At such a core, every missing shell edge ab has core-row union at least13. If the union had size at most12, extend it to a 12-set X in C and let Y=C-X. Then Y is an inherited 35-point object with independence at most3, so `e(Y)>=211`. Minimum degree12 in C gives

`e(C[X])>=144-288+211=67`,

impossible on 12 vertices.

Therefore

`t_a+t_b>=13`

for every M-edge.

## 2. Uniform q<=29 promotion theorem

Assume at a degree-13 pivot

`q<=29`, `G<=7`, `delta(C)>=12`, and EDGE13.

Then there exists an undecorated shell vertex y with

`3<=d_M(y)<=10`.

### Structural proof

Let

`X={a in A:t_a>=11}`.

Three such vertices would yield

`q>=33-3=30`,

so `|X|<=2`.

Suppose no undecorated vertex has missing degree3 through10. Every undecorated vertex outside X then has missing degree0,1 or2. No M-edge outside X can touch such a vertex, because its endpoint-weight sum would be at most12, violating EDGE13. Therefore every edge outside X has two decorated endpoints. Let D be the decorated vertices outside X; `|D|<=G<=7`.

- `|X|=0`: all edges lie on at most7 vertices; K4-freeness gives `z<=16<22`.
- `|X|=1`, weight11: all edges lie on at most8 vertices; K4-freeness gives `z<=21<22`.
- `|X|=1`, weight at least12: on the other12 vertices there is either a missing triangle or a 2-matching, otherwise the graph is a star/triangle-plus-isolates and has an independent11-set. A triangle gives q>=31; a 2-matching together with X gives q>=30.
- `|X|=2`: if the other11 vertices contain an edge, the four vertices consisting of X and that edge have weight at least35 and at most5 missing edges, so q>=30. If they contain no edge, they form an M-independent11-set.

All cases contradict q<=29.

Thus the desired undecorated middle-degree y exists.

### Exact repivot

Let `d=d_M(y)`, `S=N_M(y)`, `D_y=N_C(y)`. Define

- `rho=e_M(A\S)+G_(A\S)`;
- `h=sum_(v in D_y)(d_C(v)-12)`;
- `kappa=binom(d,2)-e_C(D_y)`;
- `b=e_R(S,D_y)`.

Exact edge accounting gives

`q_y=d(13-d)+rho+h+kappa+b`.

All correction terms are nonnegative. For `3<=d<=10`,

`d(13-d)>=30`.

Hence

`q_y>=30`.

This theorem is analytic; it does not identify scalar necessary states with graph realizations.

## 3. Mandatory 3-matching and pure low-q shell lemmas

Every 13-point missing shell with `z>=22` and `alpha(M)<=10` has a 3-matching. A matching number at most2 would leave an independent9-set and, by Konig/cross-edge counting, either too few edges or an independent11-set.

Two energy-independent pure shell lemmas are needed below.

### Pure q23,z22,G1 is impossible

K4 is impossible since it forces q>=30. If M is triangle-free, the endpoints of a 3-matching have total row weight at least33 and at most9 induced missing edges, forcing q>=24.

Hence M contains a triangle T. Let B be the outside10-set. The triangle identity gives

`e_M(B)+G_B<=2`.

An edge in B would violate the inherited EDGE11 row bound, so B is independent and there are19 T--B missing edges. Nine B-vertices have T-degree2 and one has degree1. At least eight degree2 vertices are undecorated. One triangle vertex must avoid all undecorated degree2 vertices; the one-unit decoration budget plus EDGE11 then forces it to avoid every B vertex. Thus B plus that triangle vertex is an independent11-set in M. Contradiction.

### Pure q24,z22,G2 is impossible

If M is triangle-free, equality on the 3-matching endpoints forces an induced `K3,3`, an independent outside7-set, and a size-3 Konig cover. The opposite K3,3 side has no outside attachments. Summing the nine edge inequalities forces cover-side weight8 and opposite-side weight3. Every nonisolated outside vertex must meet all three cover vertices, so the 13 outside attachment edges would have to be divisible by3. Contradiction.

If M contains a triangle T, the outside10-set again has no internal missing edge and there are19 T--B edges. If all triangle vertices meet regular degree2 outside points, their weights must all be9 and the unique degree1 outside point violates EDGE11. Otherwise one triangle vertex has no regular degree2 neighbour; the decoration budget makes every remaining possible B-edge violate EDGE11, so it avoids all of B, creating an independent11-set.

Thus the pure q24,G2 shell is impossible.

## 4. Global excess-support lemmas

Let L be the degree-13 vertices and H the positive-excess vertices. Put

`Xi=sum_(v in H)(d(v)-13)=2E-61*13`, `h=|H|`.

If `Xi<=14`, every high vertex has at least

`15-Xi`

degree-13 neighbours, because it has at most h-1 high neighbours and h<=Xi.

For E401,E402,E403 the guaranteed counts are respectively6,4,2.

For the E404 terminal unit-excess case we use a cut inequality. If all high excesses equal1 and every degree-13 vertex has at most one high neighbour, then

`e(H,L)<=61-h`,

while degree counting and the hereditary cap give

`e(H,L)>=14h-2D(h)`.

Hence necessarily

`15h-2D(h)<=61`.

## 5. E401 is empty

At E401, every degree-13 pivot has

`q<=401-91-284=26`.

In fact for every pivot the core count is at most

`310-q<=288`

because q>=22, so the <=288 core interface and EDGE13 apply. Also `G<=q-22<=4`.

The uniform theorem produces a genuine degree-13 repivot with

`q_y>=30`.

But the universal 284-core floor in the same E401 parent gives `q_y<=26`. Contradiction.

Therefore E401 is empty.

## 6. E402 is empty

At E402, `Xi=11`; every high vertex has at least4 regular neighbours. Choose a regular neighbour p of any high vertex. Then `G_p>=1`, so

`23<=q_p<=27`.

Its core has

`e(C)=311-q_p<=288`,

and `G<=5`. The uniform theorem gives q_y>=30, whereas every E402 pivot satisfies

`q_y<=402-91-284=27`.

Contradiction.

Therefore E402 is empty.

## 7. E403 is empty

At E403, `Xi=13`; every high vertex has at least2 regular neighbours. Choose such a low-high pivot p. Then

`23<=q_p<=28`.

If q=23, the shell must have `z=22,G=1`, excluded by the pure q23 lemma.

If q>=24, then

`e(C)=312-q<=288`, `G<=6`,

so the uniform theorem produces q_y>=30. But every E403 pivot has q_y<=28. Contradiction.

Therefore E403 is empty.

## 8. E404 is empty

Here total excess is15 and every pivot has q<=29.

First show every degree-13 pivot has `G<=1`. If `G>=2`, then q>=24. At q24, `z=22,G=2`, excluded by the pure q24 lemma. At q>=25, the core has

`e(C)=313-q<=288`,

and `G<=7`, so uniform promotion gives q_y>=30>29. Contradiction.

Thus every regular pivot sees at most one unit of high excess.

If any high vertex had excess at least2, it would have degree at least15. There are at most15 high vertices, so it cannot find all neighbours within H and must have a regular neighbour p. Then p sees `G>=2`, contradiction.

Therefore all high vertices have excess1, and `h=15`.

Apply the high-low cut inequality:

`15h-2D(h)<=61`.

But `D(15)=72`, so

`225-144=81>61`.

Contradiction.

Therefore E404 is empty.

## Conclusion

Under the explicit T61 h13 hereditary-cap contract,

> **E401, E402, E403 and E404 are all empty.**

These closures are now repository-canonical and no longer merely source-reported V6 results.

## Dependency boundary

The proof uses only accepted lower-order hereditary-cap seeds, CORE211, the universal 47-core floor284, Mantel/Turan, Konig, the named AES theorem inside CORE211, and exact shell/repivot bookkeeping. It does not use S30, S31, E405/E406, or the 49-point backend closure.
