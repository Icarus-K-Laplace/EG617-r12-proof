# E332 decoration layers G=4 and G=5

Status: `PROVED EMPTY` for both layers.

This note starts from the canonical extreme-shell reduction:

- `q=30`, `e(core)=211`;
- undecorated missing degrees are only `0,1,2,11,12`;
- at most two undecorated high vertices of degree 11/12;
- `L`, the undecorated low set, is independent in the missing graph;
- `G=sum g` and `z=e(M)=30-G`;
- every missing edge has endpoint row-weight sum at least 12;
- the strengthened zero-gap theorem in `E332_STRONG_ZERO_GAP_REPIVOT.md` is available.

Write

- `H` = undecorated high vertices, `h=|H|`;
- `D` = decorated vertices, `k=|D|`;
- `L` = undecorated low vertices, `l=|L|`;
- `R=H union D`, `r=h+k`, so `h+k+l=13`.

Every low vertex has missing degree at most 2 and `L` is independent.

---

## 1. Closure of G=4

For `G=4`, the previously proved support count is exact:

`(h,k,l)=(2,4,7)`.

Let the two high regular vertices be `a,b`. Let

`s=e_M(L,R)`.

Because `z=26`, `L` is independent, and `e_M(R)<=C(6,2)=15`,

`s>=11`.

Also every low has degree at most2, so `s<=14`.

Each high vertex has missing degree at least11, but inside the six-point support `R` it has at most5 neighbours. Therefore each of `a,b` has at least6 neighbours in `L`. Their two `L`-neighbour sets have size at least6 inside a seven-point set, so they have at least five common low neighbours.

Choose one common low vertex `u`. Since `d_M(u)<=2`,

`N_M(u)={a,b}`.

Apply the strong zero-gap theorem to `ua` and `ub`. Because both endpoints are undecorated,

`N_M(u) union N_M(a)=A`,

`N_M(u) union N_M(b)=A`.

Since `N_M(u)={a,b}`, both high vertices are missing-adjacent to every shell vertex outside `{a,b}`. Thus each high is adjacent in `M` to all seven lows and all four decorated vertices.

Hence the fourteen high-low incidences already saturate the low degree budget:

`s=14`.

Therefore every low has degree exactly2, with neighbourhood `{a,b}`, and there are no low-decorated missing edges.

Let `J=M[D]`. Since `z=26`, the fixed high-low and high-decorated edges leave

`e(J)=4-e_M(ab)`.

Thus `e(J)` is 3 or4.

Every decorated vertex has decoration1. With no low neighbours,

`t_x=2+d_J(x)+1=3+d_J(x)<=6`.

For every edge `xy in E(J)`, pair-row coverage gives

`t_x+t_y>=12`.

Because each term is at most6, equality forces

`d_J(x)=d_J(y)=3`.

But in a four-vertex graph, one edge whose two endpoints both have degree3 already forces at least five edges: the edge itself plus the two remaining neighbours of each endpoint. This contradicts `e(J) in {3,4}`.

Therefore

`G=4` is impossible.

---

## 2. A uniform lemma for h=2

Assume now `G<=8` and `h=2`. Write `H={a,b}`.

Since `k<=G<=8`, we have `l=11-k`. Each high vertex has missing degree at least11 and at most `k+1` neighbours inside `H union D`, so it has at least

`10-k`

neighbours in `L`.

Therefore the two high vertices have at least

`2(10-k)-(11-k)=9-k>=1`

common low neighbours.

Choose a common low `u`. Again `N_M(u)={a,b}`. The strong zero-gap theorem forces each high to be adjacent in `M` to every shell vertex outside `{a,b}`.

Consequently, for every `h=2` survivor:

- both high vertices are adjacent to every low and every decorated vertex;
- every low has degree exactly2 and neighbourhood `{a,b}`;
- there are no low-decorated edges;
- writing `epsilon=1_{ab in E(M)}` and `J=M[D]`,

`e(J)=8-G-epsilon`.

Also `J` must contain an edge, because otherwise `L union D` would be an independent 11-set in `M`, contradicting `alpha(M)<=10`.

If `epsilon=0`, each high has weight11 and every edge `xy` of `J` forms an M-triangle with a high vertex. Triangle row coverage therefore gives

`t_x+t_y>=13`.

If `epsilon=1`, pair-row coverage still gives

`t_x+t_y>=12`.

For `x in D`,

`t_x=2+d_J(x)+g_x`.

These formulas will be used repeatedly below.

---

## 3. Closure of G=5, h=2

For `G=5`:

- if `epsilon=0`, then `e(J)=3` and every J-edge must satisfy `t_x+t_y>=13`;
- if `epsilon=1`, then `e(J)=2` and every J-edge must satisfy `t_x+t_y>=12`.

A three-edge graph is one of the standard types `3K2`, `P3+K2`, `P4`, `K1,3`, `K3` after isolated vertices are ignored. In every type, the inequalities

`g_x+g_y >= 9-d_J(x)-d_J(y)`

on its edges force total positive decoration strictly larger than5. For example:

- on `K1,3`, every centre-leaf edge requires `g_c+g_l>=5`, so positivity of the three leaves already gives total decoration at least7;
- on `K3`, every pair requires decoration sum at least5, so summing the three inequalities gives total decoration at least8;
- the path and matching types are even more expensive.

Thus `epsilon=0` is impossible.

For `epsilon=1`, a two-edge graph is either `2K2` or `P3`.

- `2K2`: each edge has degree sum2, so its two decorations sum to at least6; two disjoint edges already exceed total budget5.
- `P3`: each leaf-centre edge has degree sum3, so each requires leaf+centre decoration at least5. With both leaves positive, total decoration is at least6.

Thus `epsilon=1` is also impossible.

Hence no G=5 survivor has `h=2`.

---

## 4. Closure of G=5, h=0

The edge-capacity bound

`z <= 2l + C(r,2)`

with `z=25` forces `r>=5`. If `h=0`, then `r=k<=G=5`, hence

`k=5`, `l=8`.

Since all five decorated vertices are positive and their total decoration is5,

`g_x=1` for every decorated vertex.

Let `s=e_M(L,D)`. Because `e_M(D)<=10`,

`s>=15`,

while `s<=16`.

A decorated vertex incident with a low vertex has weight at least11 by the strengthened zero-gap inequality: for a low endpoint of degree2 the crude union bound already gives `t_D>=11`, and degree1 gives `t_D>=12`.

The total decorated weight is

`t(D)=55-s<=40`,

so at most three decorated vertices can be low-active. Thus at least two decorated vertices are low-inactive.

Two low-inactive decorated vertices cannot be adjacent in `M`: they have no low neighbours, `d_M<=4`, `g=1`, hence weight at most5 each, contradicting pair-row coverage12.

If `s=15`, then `e_M(D)=10`, so `D` is `K5`, contradicting the preceding nonadjacency of two inactive vertices.

If `s=16`, then `e_M(D)=9`. With at most three active and at least two inactive vertices, the only way to realize nine D-edges without an inactive-inactive edge is exactly three active and two inactive vertices with all nine allowable edges present. Each active vertex then has D-degree4. Because total low incidence is16, while every active vertex has weight

`t_x=4+1+x_x=5+x_x>=11`,

each active must have at least6 low neighbours, requiring at least18 low incidences. Contradiction.

Thus `G=5,h=0` is impossible.

---

## 5. Closure of G=5, h=1

Let the high regular vertex be `a`. Edge capacity forces `r=h+k>=5`, so either

- `k=4,l=8`, or
- `k=5,l=7`.

### 5.1 k=4, l=8

The decorations are a permutation of `(2,1,1,1)`.

#### High degree 11

The high vertex has a unique shell nonneighbour `w`. It has at least seven low neighbours. If `w` were low, strong zero-gap on any high-low edge would force that low endpoint to use another low vertex as its second missing neighbour, contradicting independence of `L`. Hence `w in D`.

Therefore `a` is adjacent in M to all eight lows. A degree1 low is impossible because `N_M(a)` misses `w`; strong zero-gap would fail to cover the shell. Hence every low has degree2 and its second neighbour is exactly `w`.

Thus `s=16`. The support has nine internal missing edges: three high-D edges and all six D-D edges. Hence `J=M[D]=K4`.

The three decorated vertices other than `w` have no low neighbours. For each of them

`t_i=4+g_i`.

Every pair among the three is an M-edge, so

`g_i+g_j>=4`.

Summing the three pair inequalities gives total decoration on those three vertices at least6, but at most4 is available after `g_w>=1`. Contradiction.

#### High degree 12

Now `a` is universal in `M`. Since the five-point support has at most ten internal edges, `s>=15`; equivalently there are at least seven low-decorated incidences in addition to the eight high-low edges.

Any decorated vertex receiving a low edge satisfies `t_D>=11`: for a low `u` with neighbours `{a,v}`, non-profitability of the legal degree2 repivot gives

`t_a+t_v-1>=22`,

and `t_a=12`.

The total decorated weight is 28 if `s=15` and 27 if `s=16`, so at most two decorated vertices are low-active. Hence at least two are inactive.

An inactive-inactive D-edge is impossible: the two inactive weights are at most6 and5 respectively because only one decoration unit is extra beyond the four mandatory units, so their sum is below12.

Therefore `s=15` would force `J=K4`, impossible. Thus `s=16`, `e(J)=5`, and exact edge counting forces two active and two inactive decorated vertices with `J=K4` minus the inactive-inactive edge.

Each active has J-degree3 and must satisfy

`x_i+g_i>=7`.

The two active low-incidences sum to8, while their decorations sum to at most3 because the two inactive vertices each consume one decoration unit. Hence

`(x_1+g_1)+(x_2+g_2)<=11<14`,

contradiction.

So `k=4` is impossible.

### 5.2 k=5, l=7

Here every decorated vertex has decoration1.

#### High degree 11

The same zero-gap argument shows that the unique high nonneighbour is a decorated vertex `w`, the high is adjacent to all seven lows, and every low has second missing neighbour `w`.

Thus `s=14`. The high contributes four high-D edges, so the five-vertex graph `J=M[D]` has seven edges.

Any edge between two decorated vertices other than `w` has endpoints of weight at most6. Pair-row coverage forces both endpoints to have J-degree4. Since seven J-edges cannot all be incident with `w`, such an edge exists. Its two endpoints are therefore J-universal; the union of their incident edges already accounts for all seven edges. Every remaining decorated vertex then has J-degree2 and weight4, but is adjacent to a universal endpoint of weight6, giving edge-weight sum10<12. Contradiction.

#### High degree 12

Let `r_L` be the number of low-decorated incidences. Then

`3<=r_L<=7`,

and

`e(J)=13-r_L`.

Every active decorated vertex satisfies

`x_i+d_J(i)>=9`,

because `t_i=2+x_i+d_J(i)>=11`. Since `d_J(i)<=4`, each active vertex consumes at least five low incidences.

- `r_L=3,4`: impossible immediately.
- `r_L=5`: exactly one active vertex, with five low neighbours and J-degree4. The remaining four inactive vertices span four J-edges. Any inactive-inactive edge requires both endpoints to have full J-degree4, which would force at least five edges among the four inactive vertices. Contradiction.
- `r_L=6`: again exactly one active vertex. It has J-degree at least3, so the inactive four span between three and four edges. Any one such edge forces at least five inactive edges. Contradiction.
- `r_L=7`: again exactly one active vertex; the inactive four span between two and four edges, and the same argument applies.

Thus `k=5` is impossible.

Combining all cases gives

`G=5` is impossible.

---

## Conclusion

The E332 extreme shell has no `G=4` or `G=5` survivor.

The active decoration window is therefore

`G in {6,7,8}`.
