# E332 G=7, h=0 reduction

Status: `PROVED` for every eliminated cell below. The full `G=7,h=0` layer is not yet closed.

Assume the canonical E332 extreme-shell state with

- `G=7`, hence `z=e(M)=23`;
- no undecorated high vertices (`h=0`);
- decorated set `D`, `k=|D|`;
- low regular set `L`, `l=13-k`;
- `L` independent and every low has missing degree at most2;
- strengthened zero-gap and profitable-repivot inequalities;
- pair-row coverage and the triangle-row union lemma.

Let

`s=e_M(L,D)`, `J=M[D]`.

Then

`e(J)=23-s`,

and the total decorated row weight is

`t(D)=53-s`.

A decorated vertex incident with a low is called active. Every active decorated vertex has row weight at least11. A degree1 low requires its unique decorated neighbour to have row weight at least12. If a degree2 low has decorated neighbours x,y, non-profitability gives

`t_x+t_y-e_J(xy)>=22`.

Also, any triangle contained in J has total row weight at least24.

---

## 1. k=3 is impossible

Here `l=10`. Edge capacity forces

`s=20`, `J=K3`.

All ten lows have degree2. Also `t(D)=33`, so the three decorated vertices, all active, must each have weight exactly11.

Every degree2 low has its two neighbours joined by an edge of J. Non-profitability therefore requires

`11+11-1>=22`,

which is false. Hence k=3 is impossible.

---

## 2. k=4 is impossible

Here `l=9`, and edge capacity gives `s in {17,18}`.

### s=17

Then `J=K4` and `t(D)=36`.

At most three decorated vertices can be active. If three were active, their weights contribute at least33 and the inactive K4 vertex has weight at least4, contradiction. Thus exactly two vertices are active.

The two inactive vertices are adjacent in K4, so pair-row coverage gives inactive weight sum at least12. But their decorations plus the two positive active decorations have total7. Writing the inactive weights as `3+g_i`, their edge already forces inactive decoration sum at least6, leaving at most1 decoration unit for two active vertices. Contradiction.

### s=18

Then `J=K4-e` and `t(D)=35`. Again exactly two vertices are active.

Since `L` has size9, two inactive decorated vertices cannot be nonadjacent in J: otherwise `L` plus those two vertices is an independent 11-set in M. Hence the inactive pair is a J-edge.

If the unique missing edge joins the active pair, both inactive vertices have J-degree3 and their pair edge requires decoration sum at least6, again leaving fewer than two positive decoration units for the active pair.

If the unique missing edge is active-inactive, the inactive degrees are2 and3, so their edge requires decoration sum at least7, even worse.

The missing edge cannot be the inactive pair by the independence argument. Hence s=18 is impossible.

Therefore k=4 is impossible.

---

## 3. k=5 is impossible

Here `l=8`, `13<=s<=16`, `7<=e(J)<=10`, and `37<=t(D)<=40`.

At most three decorated vertices are active and at least two are active.

### Three active vertices

There are two inactive vertices. Their total row weight is at most `t(D)-33<=7`, so they cannot be adjacent in J. Therefore `e(J)<=9`, excluding s=13.

For s=14, J has9 edges. With the inactive pair forced to be the unique nonedge, both inactive vertices have J-degree3, so their row weights already sum to at least8, contradicting the available at most6. The cases s=15,16 have even less available inactive row weight. Thus three active vertices are impossible.

### Two active vertices

There are three inactive vertices. Since `L` has size8, the inactive triple cannot be independent: otherwise `L` plus the triple is an independent 11-set. Hence J contains an inactive-inactive edge.

The total decoration on the three inactive vertices is at most5. For an inactive edge ij,

`d_J(i)+d_J(j)+g_i+g_j>=12`.

Because the third inactive vertex and both active vertices are decorated positively, one has `g_i+g_j<=4`; hence the edge endpoints must both have J-degree4 and the inactive decoration budget is forced to equality: the inactive total is5 and the active decorations are both1.

But if two inactive vertices are J-universal, the third inactive vertex is adjacent to both. Applying pair-row coverage to the two resulting inactive edges gives, after summing,

`g_i+g_j+2g_k >= 8`,

while the forced inactive decoration total is only5 and `g_k>=1`; equivalently the two edge inequalities require more inactive decoration than available. Contradiction.

Hence k=5 is impossible.

Thus every G=7,h=0 survivor has `k in {6,7}`.

---

## 4. k=6: the low-incidence values s=8,9,10,11 are impossible

Here `l=7`, the decorations are a permutation of `(2,1,1,1,1,1)`, and

`8<=s<=14`.

The inactive decorated subgraph is triangle-free: even the three largest possible inactive row weights are at most `7,6,6`, whose sum is below24, contradicting the triangle-row union lemma if an inactive triangle existed.

### s=8

`J=K6`, `t(D)=45`. At least two vertices are active. Four inactive K6 vertices already contribute row weight at least24, while two active vertices contribute at least22, exceeding45. More active vertices are worse.

### s=9

`J=K6-e`, `t(D)=44`. Three active vertices are impossible by total row weight, so exactly two are active and four inactive.

Equality in the row-weight budget forces the missing J-edge to join two inactive vertices, the unique decoration2 to lie on an active vertex, and both active vertices to have row weight11. But `s=9` on seven lows gives five degree1 lows. Every degree1 low requires its neighbour to have row weight at least12. Contradiction.

### s=10

`e(J)=13`, `t(D)=43`. Three active vertices are impossible by row weight, so exactly two are active.

There are four inactive vertices. Their induced graph is triangle-free and must contain at least four edges because only nine J-edges can involve the active pair. Hence it is exactly C4, all eight active-inactive edges and the active-active edge are present.

Every inactive vertex has J-degree4. Each C4 edge therefore requires endpoint decoration sum at least4. Summing the four edge inequalities gives inactive decoration total at least8, exceeding the global budget7.

### s=11

`e(J)=12`, `t(D)=42`.

If three vertices are active, the inactive total weight is at most9. Hence the inactive triple contains no edge. Edge count then forces the active triangle and all nine active-inactive edges to be present, giving each inactive vertex weight at least4 and inactive total at least12, contradiction.

Thus exactly two vertices are active. The four inactive vertices induce a triangle-free graph with three or four edges.

- If it has three edges, the active edge and all eight active-inactive edges are forced. The inactive graph is P4 or K1,3. Pair-row coverage on its edges requires inactive decoration total greater than5 in either graph.
- If it has four edges, the inactive graph is C4. If the active edge is absent, all eight cross edges are present and every inactive C4 edge forces decoration sum at least4, giving inactive decoration total at least8. If the active edge is present, exactly one cross edge is absent; summing the four C4 pair inequalities is even stronger and forces inactive decoration total at least9.

All cases contradict the available inactive decoration budget at most5.

Therefore s=11 is impossible.

So for k=6 only

`s in {12,13,14}`

remain.

---

## 5. k=7: the low-incidence values s=2,...,9 are impossible

Here `l=6`, every decorated vertex has decoration1, and the inactive decorated subgraph is triangle-free because an inactive triangle has total row weight at most21<24.

Write m for the number of active decorated vertices.

The triangle-free inactive-edge bound plus total row-weight bound eliminates s=2 through7 directly:

- s=2: edge density requires at least5 active vertices, but total decorated weight permits at most4;
- s=3: the only edge-maximal m=4 configuration already gives inactive row weight far above the available budget;
- s=4,5: the inactive degree sum forced by `e(J)=19,18` exceeds the total inactive row-weight budget;
- s=6: the only m=2 edge-maximal configuration has inactive graph K2,3 and total row weight at least49>47;
- s=7: with m=2 the inactive degree sum alone forces total row weight above46, while m>=3 is worse.

For completeness, the last two values admit sharp equality analyses.

### s=8

`e(J)=15`, `t(D)=45`. Exactly two vertices are active. The only numerical equality possibility has the active edge present, all ten active-inactive edges present, and a four-edge triangle-free graph on the five inactive vertices. It forces both active vertices to have row weight11. But s=8 on six lows includes four degree1 lows, each requiring neighbour weight at least12. Contradiction.

### s=9

`e(J)=14`, `t(D)=44`. Again exactly two vertices are active. The only possible edge/weight equality has the active edge present, all ten cross edges present, and three inactive edges. The two active row weights sum to23. Since s=9 on six lows consists of three degree2 and three degree1 lows, both active vertices receive a degree1 low. Hence both must have weight at least12, contradicting total active weight23.

Therefore for k=7 only

`s in {10,11,12}`

remain.

---

## Current G=7,h=0 frontier

Every G=7,h=0 survivor is now confined to:

- `k=6`, `s in {12,13,14}`;
- `k=7`, `s in {10,11,12}`.

No k=3,4,5 state survives, and all lower-incidence k=6/7 cells are analytically closed.
