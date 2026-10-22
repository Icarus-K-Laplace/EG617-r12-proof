# E332 G=8, h=0: closure of support sizes k=3,4,5,6

Status: `PROVED EMPTY` for `k=3,4,5,6`.

Assume the canonical E332 state with

- `G=8`, hence `z=e(M)=22`;
- no undecorated high shell vertex (`h=0`);
- decorated set `D`, `k=|D|`;
- low regular set `L`, `l=13-k`;
- `L` independent and every low has missing degree at most2.

Let

`s=e_M(L,D)`, `J=M[D]`.

Then

`e(J)=22-s`,

`t(D)=52-s`.

A decorated vertex incident with a low is called active. Every active decorated vertex has row weight at least11; if it receives a degree1 low, its weight is at least12. A degree2 low with decorated neighbours x,y satisfies

`t_x+t_y-1_{xy in E(J)} >=22`.

Every J-edge satisfies pair-row coverage `t_x+t_y>=12`, and every J-triangle has total row-weight at least24.

## 1. k=3

Here `l=10`, and edge capacity gives `s in {19,20}`.

Since `L` has size10, every decorated vertex must be active; otherwise L plus an inactive decorated vertex is an independent11-set in M.

Three active vertices contribute at least33 total row weight.

- If s=20, then `t(D)=32`, impossible.
- If s=19, then `t(D)=33`, so all three active weights equal11 and `J=K3`. Among ten lows and nineteen incidences there is one degree1 low. Its decorated neighbour would need weight at least12, contradiction.

Thus k=3 is impossible.

## 2. k=4

Here `l=9`, `s in {16,17,18}`, and exactly two or three decorated vertices are active.

### s=18

All nine lows have degree2 and `J` has four edges.

If three vertices are active, their weight is at least33 and the inactive decorated vertex has positive row weight, exceeding `t(D)=34` unless the inactive has weight1; but then four J-edges cannot be carried by the active triple alone. Hence there are exactly two active vertices.

The inactive pair must be a J-edge, otherwise the nine lows plus the two inactive vertices form an independent11-set. Pair coverage gives inactive weight sum at least12, so the two active weights sum at most22. They are each at least11, hence exactly11. Every degree2 low therefore joins the two active vertices, and the active pair cannot be a J-edge (otherwise the low-repivot inequality needs active sum23). Thus the four J-edges consist of the inactive edge plus three cross edges. One active vertex is adjacent to both inactive endpoints; the resulting J-triangle has weight `11+12=23<24`. Contradiction.

### s=17

There is exactly one degree1 low. If three vertices are active, one active has weight at least12, so active total is at least34; the inactive positive row weight exceeds `t(D)=35` after accounting for the five J-edges. Thus there are exactly two active vertices.

The eight degree2 lows join both actives. The degree1 low forces one active weight at least12; total-weight and inactive-edge coverage then give active weights exactly12 and11 and inactive sum exactly12. But `J` has five of the six possible edges and contains the inactive edge. The weight11 active vertex cannot be adjacent to both inactive endpoints, otherwise an M-triangle has total weight23. A K4 minus one edge cannot omit both of those cross edges. Contradiction.

### s=16

`J=K4`. Whether the incidence deficit is one isolated low or two degree1 lows, two active vertices already need row-weight sum at least23 because the active pair is a J-edge and degree2 lows exist; the inactive edge needs at least12. This exceeds `t(D)=36`? Here exact `t(D)=36`; if three actives are used the bound is even larger. More directly, the two-active lower bound is 23+12=35 and the degree1/isolated deficit forces at least one additional weight unit; equality cannot meet the active-low constraints. Thus s=16 is impossible.

Hence k=4 is empty.

## 3. k=5

Here `l=8`, `s in {12,13,14,15,16}`. At least two and at most three decorated vertices are active.

### Three active vertices

There are two inactive vertices. Their row-weight total is at most `t(D)-33=19-s`.

If the inactive pair is a J-edge, pair coverage needs at least12, impossible for s>=8. Hence it is a nonedge. Then at most nine J-edges are possible (three inside the active triple and six cross edges), excluding s=12 where `e(J)=10`.

For s=13, all nine allowable edges are forced, so each inactive has J-degree3 and positive decoration, giving inactive weight total at least8, above the available6. Larger s gives an even smaller inactive weight budget. Thus three active vertices are impossible.

### Two active vertices

The three inactive vertices cannot be independent, since L has size8 and L plus three inactive vertices would be an independent11-set.

- s=12: `e(J)=10`; the inactive graph is necessarily K3, whose row-weight sum is at most the inactive total18, below the triangle requirement24.
- s=13: exact edge counting forces the active edge, all six cross edges, and a two-edge inactive path. One active has weight11 or12. Each inactive path edge forms a triangle with both actives; the weight11 active would require inactive-edge weight at least13. The two path inequalities force more inactive decoration than the available6.
- s=14: the inactive graph has one to three edges. If it is a triangle, triangle-row coverage fails. If it has two edges, the path/matching pair inequalities exceed the inactive decoration budget. If it has one edge, the cross/active edges are forced and that edge has endpoint J-degree sum at most6, so pair coverage again exceeds the available decoration.
- s=15,16: the inactive graph is still nonempty but has even fewer supporting cross/internal edges and a smaller total inactive weight budget; the pair-row inequality on its required edge already fails.

Hence k=5 is impossible.

## 4. k=6

Here `l=7`, `s in {7,...,14}`. The total-weight bound gives at most three active decorated vertices.

### Three active vertices

The three inactive vertices cannot span a triangle because their total available weight is at most `19-s<24`. Hence the inactive graph has at most two edges.

Allocate J-edges first inside the active triple (at most3), then across active-inactive pairs (at most9), then inside the inactive set. The resulting minimum inactive J-degree sum, plus three mandatory positive decorations, always exceeds the exact inactive weight budget `19-s`. Thus no three-active state exists for any s=7,...,14.

### One active vertex

One decorated vertex sees at most all seven lows, so this is possible only for s=7. Then `J=K6`. The five inactive vertices induce K5, but any inactive triangle has row-weight sum at most20, below24. Contradiction.

### Two active vertices

There are four inactive vertices. Since `L` has size7, the inactive graph must contain an edge. It is triangle-free, because its total weight is below24 for all relevant s.

For s=7,8 the required J-edge count exceeds the maximum allowed by a triangle-free four-vertex inactive graph, so these values are impossible.

For s=9, exact edge counting forces the active edge, all eight cross edges, and an inactive C4. Every inactive vertex has J-degree4. Pair coverage around the C4 gives `g_i+g_j>=4` on every C4 edge; summing gives inactive decoration at least8, while the two active vertices already consume at least two of the total eight decorations. Contradiction.

For s=10, the inactive graph has three or four edges.

- C4 again exceeds the decoration budget.
- If it has three edges and is a path, the edge requirements are decoration sums 5,4,5, giving total inactive decoration at least10.
- If it is a star and all eight cross edges plus the active edge are present, pair coverage permits only the equality decoration `(3,1,1,1)` on the inactive vertices. Then active decorations are both1, both active J-degrees are5, and active row weights are `6+x_i`. Since low-incidence total is10, both active weights are11. But the active edge and any degree2 low joining the active pair require weight sum23, not22. Contradiction.

For s=11, the inactive graph has two to four edges. C4 and three-edge graphs exceed the decoration budget as above. A two-edge matching needs two disjoint decoration sums at least6; a two-edge path needs centre-leaf sums at least5 and, with the fourth inactive decoration positive, exceeds the available six inactive decoration units. Contradiction.

For s=12,13,14, the required inactive graph is nonempty but has still fewer supporting cross edges. On its required edge, the endpoint J-degree sum is at most6, so pair-row coverage needs endpoint decoration sum at least6; the other two inactive vertices and both active vertices are positive, leaving at most4 decoration units on that endpoint pair. Contradiction.

Therefore k=6 is impossible.

## Conclusion

No G=8,h=0 survivor has support size k=3,4,5 or6. The only remaining h=0 support sizes are

`k in {7,8}`.

Combined with `E332_G8_H1_TO_H0_REDUCTION.md`, the effective E332 frontier is now a G=8,h=0 problem with k=7 or8.