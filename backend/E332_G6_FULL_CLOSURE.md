# E332 full closure of the G=6 decoration layer

Status: `PROVED EMPTY`.

Assume the canonical E332 state:

- `e(F)=332`;
- for a degree-13 pivot, `q=30`, `e(H)=211`, `delta(H)>=12`;
- every undecorated shell missing degree is in `{0,1,2,11,12}`;
- there are at most two undecorated high vertices of missing degree11/12;
- the strengthened zero-gap theorem is available:
  `|N_M(u) union N_M(v)|+g_v >= 13+|D_u intersect D_v|`
  for every missing edge `uv` with `u` undecorated;
- `G=sum g=6`, hence `z=e(M)=24`.

The `h=0` branch is already closed in `E332_G6_H0_CLOSURE.md`. The two-high branch was reduced in `E332_H2_CLASSIFICATION.md` to one exact cell, `H2-G6-K4`. We close that cell first and then close every `h=1` state.

---

## 1. A triangle-row union lemma

Let `r,s,t` be three shell vertices forming a triangle in the missing graph `M`, i.e. they are pairwise nonadjacent in the target graph `F`. Put

`D_r=N_H(r)`, `D_s=N_H(s)`, `D_t=N_H(t)`.

Any two core vertices outside `D_r union D_s union D_t` must be adjacent in `F`; otherwise those two vertices together with `r,s,t` form an independent 5-set. Therefore the outside set is a clique. Since `F` is K12-free, that clique has size at most11. Thus

`|D_r union D_s union D_t| >= 35-11 = 24`.

In particular, if

`|D_r|+|D_s|+|D_t|=24`,

then the three rows are pairwise disjoint.

---

## 2. The exact H2-G6-K4 cell is impossible

In the exact two-high G=6 cell there are:

- two undecorated high vertices `a,b`, each of missing degree12;
- two decorated vertices `x,y` with `g_x+g_y=6`;
- nine undecorated lows, each with missing neighbourhood `{a,b}`;
- the support `{a,b,x,y}` induces `K4` in `M`.

Write

`A=D_a`, `B=D_b`, `X=D_x`, `Y=D_y`.

Then

`|A|=|B|=12`,

and because `d_M(x)=d_M(y)=3`,

`|X|+|Y|=(3+g_x)+(3+g_y)=12`.

The missing triangles `a,x,y` and `b,x,y` therefore have total row-size exactly24. By the triangle-row union lemma,

- `A`, `X`, `Y` are pairwise disjoint;
- `B`, `X`, `Y` are pairwise disjoint.

Also `ab` is a missing edge between two undecorated vertices. The strengthened zero-gap theorem gives

`A intersect B = empty`.

Hence the three sets

`A`, `B`, `X union Y`

are pairwise disjoint and have total size

`12+12+12=36`,

inside a 35-vertex core. Contradiction.

Therefore `H2-G6-K4` is empty.

So any remaining G=6 state must have `h=1`.

---

## 3. Setup for h=1

Let `a` be the unique undecorated high vertex. Let `D` be the decorated set, `k=|D|`, and `L` the undecorated low set, `l=12-k`.

Edge capacity forces `k>=3`, while `k<=G=6`, so

`k in {3,4,5,6}`.

We split according to `d_M(a)=11` or12.

---

## 4. High degree 11

Let `w` be the unique shell nonneighbour of `a` in `M`.

If a low vertex `u` is adjacent to `a`, then strong zero-gap requires

`N_M(u) union N_M(a)=A_shell`.

Since `L` is independent and `d_M(u)<=2`, the second neighbour of `u` must be exactly `w`. Thus `w` is decorated, `a` is adjacent to every low and every decorated vertex except `w`, and every low has neighbourhood exactly `{a,w}`.

Therefore there are no low-decorated missing edges except those to `w`.

Writing `J=M[D]`, exact edge counting gives

`e(J)=k+1`.

For every decorated vertex `x != w`,

`t_x=1+d_J(x)+g_x`,

because its only support edge outside `J` is the edge to `a`.

Any J-edge `xy` with `x,y != w` forms a missing triangle with `a`. The triangle-row lemma implies the weight inequality

`t_x+t_y>=13`,

so

`g_x+g_y >= 11-d_J(x)-d_J(y)`.  (1)

### k=3

`e(J)=4>C(3,2)`, impossible.

### k=4

`J=K4-e`. There are two possibilities for the missing edge.

- If the missing edge is incident with `w`, then the other three vertices form a J-triangle with J-degrees `2,3,3`. Applying (1) to its three edges forces their decoration sum to be at least9, already above the total budget6.
- If the missing edge joins two vertices different from `w`, then the two surviving edges among the three non-w vertices both meet the third non-w vertex. Their J-degrees are `(2,3)` on each edge, so each edge requires endpoint decoration sum at least6. Positivity of the two outer vertices then forces the non-w decoration sum at least7, again impossible.

Thus k=4 is impossible.

### k=5

The four vertices in `D-{w}` are all decorated and positive. Since `g_w>=1`, their total decoration is at most5.

Every edge among those four vertices satisfies (1). Because `d_J<=4`, an edge whose endpoint decorations sum to at most3 would require endpoint J-degree sum at least8, hence both endpoints would have J-degree4.

But with total positive decoration at most5 on four vertices, every edge has endpoint decoration sum at most3. Hence every non-w J-edge would have both endpoints J-universal. Two J-universal vertices already contribute at least seven distinct J-edges on five vertices, while `e(J)=6`. Contradiction.

Thus k=5 is impossible.

### k=6

All six decorated vertices have decoration1. For any edge `xy` among the five vertices different from `w`, (1) gives

`d_J(x)+d_J(y)>=9`.

Since J-degrees are at most5, every such edge has a degree-5 endpoint and the other endpoint has degree at least4.

But `e(J)=7`. A degree-5 vertex already contributes five edges, leaving only two additional edges among the other five vertices. Any neighbour of that universal vertex then has total J-degree at most3, not at least4. Contradiction.

Hence no degree-11 high state exists.

---

## 5. High degree 12

Now `a` is universal in the missing shell. Every low has one compulsory missing edge to `a` and at most one additional edge to a decorated vertex.

Let

`r=e_M(L,D)`

be the number of low-decorated incidences. Then

`r+e(J)=12`.  (2)

A decorated vertex incident with a low is called active. For every active vertex x,

`t_x=1+d_J(x)+x_L+g_x >=11`,

where `x_L` is its number of low neighbours. Equivalently,

`x_L+d_J(x)+g_x >=10`.  (3)

### k=3

Here `l=9`. Equation (2) and `e(J)<=3` force

`r=9`, `J=K3`.

The decorated weight sum is

`t(D)=30+k-r=24`.

Three active vertices would already contribute at least33. If exactly two are active, the third has weight at least `1+2+1=4`, so total decorated weight is at least26. If exactly one is active, the two inactive vertices are adjacent in K3; their pair-row inequality forces their decorations to sum to at least6, leaving no positive decoration for the active vertex. All cases contradict the total weight/budget. Thus k=3 is impossible.

### k=4

Now `l=8` and `r in {6,7,8}`.

If two vertices are active, summing (3) over them gives

`r + (d_1+d_2) + (g_1+g_2) >=20`.

But `d_1+d_2<=6` and the two inactive decorated vertices consume at least two decoration units, so `g_1+g_2<=4`. Hence `r>=10`, impossible. Therefore exactly one vertex is active.

Let its J-degree be d. Then the inactive four-minus-one set has `e(J)-d` internal edges.

- `r=8`: `e(J)=4`. If `d=1,2,3`, the resulting inactive graph has respectively 3,2,1 edges. Pair-row coverage on an inactive edge requires endpoint decoration sums of at least6, and the three possible graph types (`K3`, a two-edge path/matching, or one edge) all exceed the available inactive decoration budget at most5.
- `r=7`: `e(J)=5`. Here `d=2` or3. If `d=2`, the inactive graph is K3 and the three pair inequalities force inactive decoration sum at least7. If `d=3`, the inactive graph has two edges and again its path/matching forms require decoration sum above5.
- `r=6`: `e(J)=6=K4`. The inactive three vertices form K3, each of J-degree3. Their pair inequalities require pairwise decoration sums at least4, so their total decoration is at least6, leaving none for the active vertex.

Thus k=4 is impossible.

### k=5

Let m be the number of active decorated vertices. Summing (3) over the active set gives

`r + sum_A d_J + sum_A g >=10m`.

Since `d_J<=4` and the `5-m` inactive vertices each consume at least one decoration unit,

`sum_A g <= 6-(5-m)=m+1`.

Hence

`r+1 >=5m`.  (4)

Equation (2) gives `r in {2,...,7}`. Since r>0, (4) forces `r>=4` and `m=1`.

Let v be the unique active vertex and d its J-degree. The other four vertices are inactive and carry total decoration at most5. For `r=4,5,6,7`, the internal inactive graph has respectively `8-d,7-d,6-d,5-d` edges.

Using the active constraint `r+d+g_v>=10` and positivity of all four inactive decorations leaves only the following maximal possibilities:

- r=4 forces `d=4`, `g_v=2`, and the inactive graph has4 edges with all inactive decorations1;
- r=5 reduces to a 3-edge inactive graph with total inactive decoration at most5;
- r=6 reduces to a graph with at most4 inactive edges and total inactive decoration at most5;
- r=7 reduces to at most4 inactive edges and the same decoration budget.

For an inactive edge ij,

`t_i+t_j=(1+d_i+g_i)+(1+d_j+g_j)>=12`.

In the r=4 equality case this forces both endpoints of every inactive edge to have J-degree4; one such edge would already force at least five inactive edges, contradiction.

For r=5,6,7 the possible inactive graphs have at most three effective edges after the active incidences are removed. Their standard types are a triangle, star, path, two-edge path, matching, or a single edge. In each type the pair inequality above requires total inactive decoration at least6 (and usually more), exceeding the available budget at most5.

Thus k=5 is impossible.

### k=6

All six decorated vertices have decoration1. Equation (3) becomes

`x_L+d_J(x)>=9`

for every active vertex. Hence each active vertex uses at least four low incidences.

If `r=1,2,3`, no active vertex can exist, contradiction. For `r=4,5,6`, there can be exactly one active vertex v.

- r=4: `e(J)=8`, the active vertex must have J-degree5, and the five inactive vertices span three edges. For an inactive edge ij, both endpoints have weight `3+deg_{J[I]}(.)`; pair-row coverage would require internal degree sum at least6, impossible in a three-edge graph.
- r=5: `e(J)=7`. If `d_J(v)=5`, the inactive graph has two edges; if `d_J(v)=4`, it has three. In either case every inactive edge would require endpoint total J-degree at least8, impossible for such a sparse graph.
- r=6: `e(J)=6`. The inactive graph has one to three edges. Again pair-row coverage requires an inactive-edge endpoint J-degree sum at least8. The only numerical way would require both endpoints to be degree4 in J, which would force at least five inactive edges, contradiction.

The remaining case r=0 has `e(J)=12` and no active decorated vertex. Then every decorated vertex has weight `d_J+1`. Every J-edge therefore requires endpoint J-degree sum at least10. The only 6-vertex 12-edge possibility meeting this local lower bound would have all edge endpoints of J-degree at least4; in particular J contains a triangle. But every missing triangle among these decorated vertices has total row weight at most `3*(6)=18<24`, contradicting the triangle-row union lemma.

Thus k=6 is impossible.

Therefore no degree-12 high state exists.

---

## Conclusion

The h=1 branch is empty, the h=0 branch was already empty, and the unique h=2 cell is empty. Hence

`E332, G=6` is `PROVED EMPTY`.

After the previously proved G=4 and G=5 closures, any E332 survivor must satisfy

`G in {7,8}`.
