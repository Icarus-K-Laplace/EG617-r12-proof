# E332 G=6, h=0 closure

Status: `PROVED EMPTY`.

Assume the active E332 extreme-shell state with decoration total `G=6` and no undecorated high vertices (`h=0`). Then `z=e(M)=24`.

Let `D` be the decorated set, `k=|D|`, and `L` the undecorated low set, `l=13-k`. Since `L` is independent and every low has degree at most2,

`24=z <= 2l + C(k,2)`.

This forces `k>=4`. Since `k<=G=6`, there are three cases.

A decorated vertex incident with a low vertex has weight at least11 by the strengthened zero-gap theorem: for a low endpoint of degree at most2,

`|N(u) union N(v)|+g_v>=13`

and the crude union bound gives `t_v=d_M(v)+g_v>=11`.

Call such a decorated vertex low-active.

---

## Case k=4, l=9

The edge-capacity bound is sharp:

`24 = 2*9 + C(4,2)`.

Therefore every low has degree2 and `M[D]=K4`.

The total low incidence is18 and the total decorated row weight is

`t(D)=54-18=36`.

Every active decorated vertex has weight at least11. If two decorated vertices were inactive, their mutual K4 edge would have endpoint weights at most6 and5 respectively (the total decoration is only6), contradicting pair-row coverage12. Hence at most one vertex is inactive.

If one vertex were inactive, the other three active vertices would consume at least33 row-weight, leaving at most3 for the inactive vertex, but an inactive vertex already has J-degree3 and positive decoration, hence weight at least4. Contradiction.

If all four are active, their total weight is at least44>36. Contradiction.

Thus k=4 is impossible.

---

## Case k=5, l=8

Now the decorations are a permutation of `(2,1,1,1,1)`.

Let `s=e_M(L,D)`. Since `e(M[D])<=10`,

`14<=s<=16`.

The decorated weight sum is

`t(D)=54-s<=40`,

so at most three decorated vertices are active. Hence at least two are inactive.

Two inactive decorated vertices cannot be adjacent: their weights are at most6 and5 respectively, so the edge-weight sum is below12. Therefore the inactive set is independent in `M[D]`.

### s=14

Then `e(M[D])=10`, so `M[D]=K5`, impossible because two inactive vertices would be adjacent.

### s=15

Then `e(M[D])=9`. The only way to realize nine edges with at most three active vertices and no inactive-inactive edge is exactly three active and two inactive vertices, with every allowed edge present: the active vertices induce `K3`, every active is adjacent to both inactive vertices, and the inactive pair is the unique nonedge.

Each active vertex therefore has D-degree4. Among the eight lows, total incidence15 means seven lows have degree2 and one has degree1.

A degree2 low whose neighbours are active vertices `i,j` gives, by non-profitability of its legal repivot,

`t_i+t_j-1>=22`,

so

`t_i+t_j>=23`.

Write `x_i` for the low-incidence count of active vertex i. Since `t_i=4+x_i+g_i`, for every used active pair `ij` we obtain

`x_k <= g_i+g_j`,

where k is the third active vertex and `x_1+x_2+x_3=15`.

If only one pair type occurs among the seven degree2 lows, the third active vertex can receive only the degree1 low. But then its weight is at most `4+1+2=7`, whereas a degree1 low requires neighbour weight at least12. Thus at least two pair types occur.

If, say, pairs12 and13 both occur, then

`x_3<=g_1+g_2`,

`x_2<=g_1+g_3`.

The two inactive vertices consume at least two decoration units, so the active decoration sum is at most4, and only one active decoration can equal2. Hence

`x_2+x_3<=6`,

forcing `x_1>=9`, impossible because there are only eight lows.

Thus s=15 is impossible.

### s=16

All eight lows have degree2 and `e(M[D])=8`. Again exactly three decorated vertices are active and two inactive; among the nine allowed active-active / active-inactive edges, exactly one is missing.

Every low corresponds to a pair of active vertices. At least two pair types occur because all three active vertices have positive low-incidence.

For a used active pair `ij` that is an M-edge, non-profitability gives

`t_i+t_j>=23`.

With `x_1+x_2+x_3=16`, this yields

`x_k <= d_J(i)+d_J(j)+g_i+g_j-7`.

There is only one extra decoration unit, so `g_i+g_j<=3`, and `d_J(i)+d_J(j)<=8`. Thus every used edge-pair gives `x_k<=4`. A used nonedge pair is even stronger.

Two distinct used pair types therefore force two of the incidence counts to be at most4, hence the third is at least8. Because no `x_i` exceeds8, equality is forced:

`(x_1,x_2,x_3)=(8,4,4)`

up to permutation, and the only used pair types are12 and13, each four times.

Equality in the two bounds forces all three active vertices to have J-degree4 and the central active vertex to carry the unique decoration2. But if all three active vertices have J-degree4, all nine allowed edges are present, contradicting `e(M[D])=8`.

Thus s=16 is impossible.

Hence k=5 is impossible.

---

## Case k=6, l=7

All six decorated vertices have decoration1.

Let `s=e_M(L,D)`. Since `e(M[D])<=15`,

`9<=s<=14`,

and

`e(M[D])=24-s`.

Every active decorated vertex has weight at least11. Since `d_J<=5` and `g=1`, every active vertex consumes at least five low incidences.

### s=9

At least two active vertices are required to carry nine incidences because one vertex sees at most seven lows, but two active vertices require at least ten incidences. Contradiction.

### s=10

Exactly two active vertices are possible. The D-graph has14 edges, i.e. `K6` minus one edge. There are four inactive vertices.

Any inactive-inactive edge requires both endpoints to have J-degree5, because their weights are `d_J+1` and must sum to at least12. Hence any inactive vertex of degree4 cannot have an inactive neighbour. With four inactive vertices this is impossible unless both endpoints of the unique missing edge are the two active vertices, so all inactive vertices have degree5.

Then each active vertex has J-degree4 and therefore needs at least six low incidences, requiring at least12 incidences instead of10. Contradiction.

### s=11,12,13,14

Again there can be only two active vertices, because three would consume at least15 incidences. Thus there are four inactive vertices.

If an inactive-inactive edge exists, both endpoints must have J-degree5. But a J-degree5 inactive vertex is adjacent to all other D-vertices, so every other inactive vertex has an inactive neighbour and is therefore also forced to have J-degree5. Consequently all four inactive vertices have degree5, which already contributes all six inactive-inactive edges and all eight active-inactive edges, at least14 J-edges.

For `s=11,12,13,14`, however,

`e(J)=13,12,11,10`,

respectively. Contradiction whenever an inactive-inactive edge exists.

If no inactive-inactive edge exists, at most

`C(2,2)+2*4=9`

J-edges are possible, also below each of 10,11,12,13.

Thus all four values are impossible.

Hence k=6 is impossible.

---

## Conclusion

There is no E332 extreme shell with

`G=6, h=0`.

Combined with the exact h=2 classification, any G=6 survivor must have either

- `h=1`, or
- the unique `H2-G6-K4` support state from `E332_H2_CLASSIFICATION.md`.
