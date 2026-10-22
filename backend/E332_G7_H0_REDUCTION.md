# E332 G=7, h=0 full closure

Status: `PROVED EMPTY`.

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

Any triangle contained in J has total row weight at least24.

---

## 1. k=3 is impossible

Here `l=10`. Edge capacity forces

`s=20`, `J=K3`.

All ten lows have degree2. Also `t(D)=33`, so the three decorated vertices, all active, must each have weight exactly11.

Every degree2 low has its two neighbours joined by a J-edge. Non-profitability would require

`11+11-1>=22`,

false. Thus k=3 is impossible.

---

## 2. k=4 is impossible

Here `l=9`, and edge capacity gives `s in {17,18}`.

### s=17

Then `J=K4` and `t(D)=36`.

Three active vertices would contribute at least33 and the inactive K4 vertex has weight at least4, contradiction. Thus exactly two vertices are active.

The two inactive vertices are adjacent, so pair-row coverage requires inactive weight sum at least12. Their J-degrees are3, hence their decorations sum to at least6. This leaves at most one decoration unit for two active decorated vertices, impossible.

### s=18

Then `J=K4-e`, `t(D)=35`, and again exactly two vertices are active.

The two inactive vertices must be adjacent: otherwise those two vertices together with the independent nine-point set L form an independent 11-set in M.

If the unique missing edge joins the active pair, both inactive vertices have J-degree3 and their edge forces decoration sum at least6. If the missing edge is active-inactive, the inactive degrees are2 and3 and their edge forces decoration sum at least7. The missing edge cannot be the inactive pair. Every case exceeds the decoration budget after reserving one positive unit for each active vertex.

Thus k=4 is impossible.

---

## 3. k=5 is impossible

Here `l=8`, `13<=s<=16`, `7<=e(J)<=10`, and `37<=t(D)<=40`.

At least two and at most three decorated vertices are active.

### Three active vertices

There are two inactive vertices. Their total row weight is at most `t(D)-33<=7`, so they cannot be adjacent. Hence `e(J)<=9`, excluding s=13.

For s=14, J has9 edges, so the inactive pair is the unique nonedge. Each inactive vertex has J-degree3, hence inactive total weight at least8, already above the available at most6. The cases s=15,16 are even tighter. Thus three active vertices are impossible.

### Two active vertices

There are three inactive vertices. Since `|L|=8`, the inactive triple cannot be independent; hence it contains an edge ij.

The three inactive decorations total at most5. Pair-row coverage on ij and positivity of the third inactive vertex force the endpoints to be J-universal and force the inactive decoration budget to equality. The third inactive vertex is then adjacent to both universal endpoints. Applying pair-row coverage to those two edges requires more than the available inactive decoration total5. Contradiction.

Therefore k=5 is impossible.

So every survivor would have k in {6,7}.

---

## 4. k=6 is impossible

Now `l=7`, decorations are a permutation of `(2,1,1,1,1,1)`, and `8<=s<=14`.

The inactive decorated subgraph is triangle-free: even the three largest possible inactive row weights are at most `7,6,6`, whose sum is below24.

### s=8

`J=K6`, `t(D)=45`. At least two vertices are active. Four inactive K6 vertices already contribute row weight at least24 and two active vertices at least22, exceeding45.

### s=9

`J=K6-e`, `t(D)=44`. Exactly two vertices are active and four inactive. Equality in the weight budget forces the missing edge to join two inactive vertices, the unique decoration2 to be active, and both active row weights to equal11. But s=9 on seven lows has five degree1 lows, each requiring neighbour weight at least12. Contradiction.

### s=10

`e(J)=13`, `t(D)=43`. Exactly two vertices are active. The inactive four-point graph is triangle-free and must contain four edges, so it is C4; all active-inactive edges and the active edge are present. Every inactive vertex has J-degree4. Summing pair-row coverage around the C4 forces inactive decoration total at least8>7.

### s=11

`e(J)=12`, `t(D)=42`.

Three active vertices are impossible: the inactive total weight would be at most9, hence no inactive edge, but edge count then forces all nine active-inactive edges and the active triangle, giving inactive total weight at least12.

Thus exactly two vertices are active. Let epsilon indicate whether the active edge is present and let e_I be the number of inactive edges. Since there are at most eight cross edges,

- epsilon=0 implies `e_I in {3,4}`;
- epsilon=1 implies `e_I in {2,3,4}`.

For epsilon=0,e_I=3, all cross edges are present and the inactive graph is P4 or K1,3. Pair-row coverage requires inactive decoration total at least10 or6 respectively, above the available at most5. The e_I=4 case is C4 and requires at least9.

For epsilon=1,e_I=2, all cross edges are present. A matching requires inactive decoration at least12; P3 plus an isolated vertex requires at least7. The e_I=3,4 cases are no weaker. Contradiction.

### s=12

`e(J)=11`, `t(D)=41`.

Three active vertices again leave inactive total weight at most8. With no inactive edge, at least eight cross edges are forced, so inactive weight is at least `8+3=11`, contradiction.

Thus exactly two vertices are active. If epsilon=0 then `e_I in {3,4}`; if epsilon=1 then `e_I in {2,3,4}`. The same P4/K1,3/matching/P3/C4 edge inequalities as above require inactive decoration strictly greater than5 in every case. Hence s=12 is impossible.

### s=13

`e(J)=10`, `t(D)=40`.

Three active vertices leave inactive total weight at most7; no inactive edge is possible, but then at least seven cross edges plus three positive inactive decorations give weight at least10. Thus exactly two vertices are active.

Now epsilon=0 gives `e_I>=2` and epsilon=1 gives `e_I>=1`. Even the weakest single-edge all-cross case requires the two edge-endpoint decorations to sum to at least6, and the other two inactive vertices are positive. All higher e_I cases are stronger. Contradiction.

### s=14

All seven lows have degree2, `e(J)=9`, `t(D)=39`.

Three active vertices are impossible by the same inactive-weight count. Thus exactly two vertices are active. The four inactive vertices cannot be independent, because together with L they would form an independent 11-set; hence `e_I>=1`.

For e_I=1, the best possible cross support gives a single inactive edge with endpoint J-degrees at most3 and3, requiring endpoint decoration sum at least6; the other two inactive vertices are positive. For e_I=2,3,4 the standard triangle-free inactive graphs only reduce endpoint degrees or create more edge inequalities. Every case needs inactive decoration above5. Contradiction.

Therefore k=6 is impossible.

---

## 5. k=7 is impossible

Here `l=6`, all decorations equal1, and `2<=s<=12`.

The inactive decorated subgraph is triangle-free because an inactive triangle has total row weight at most21<24.

Let m be the number of active vertices.

### s=2,...,7

Combining the triangle-free inactive-edge bound with the total row-weight budget eliminates these values:

- s=2 requires at least5 active vertices by edge density, but weight permits at most4;
- s=3 forces the edge-maximal m=4 configuration, whose inactive row weight already exceeds the budget;
- s=4,5 force inactive degree sum above the available inactive row weight;
- s=6 forces the edge-maximal m=2 state with inactive graph K2,3, whose total row weight is too large;
- s=7 similarly forces inactive degree sum above the weight budget.

### s=8

`e(J)=15`, `t(D)=45`. Exactly two vertices are active. The unique numerical equality has the active edge, all ten cross edges, and four inactive edges, and it forces both active weights to11. But s=8 on six lows has four degree1 lows, contradiction.

### s=9

`e(J)=14`, `t(D)=44`. Exactly two vertices are active. The equality state has the active edge, all ten cross edges, three inactive edges, and active total weight23. Here there are three degree1 lows and both active vertices receive one, so both must have weight at least12, contradiction.

### s=10

`e(J)=13`, `t(D)=43`.

Three active vertices leave inactive total weight at most10. Writing e_A for active-active edges, c for cross edges and e_I for inactive edges,

`t(I)=c+2e_I+4=17-e_A+e_I>=14`,

contradiction. Thus exactly two vertices are active.

If the active edge is absent, edge capacity forces `e_I=3` and all ten cross edges. If it is present, `e_I` lies between2 and4. In every case an inactive edge has

`d_I(u)+d_I(v)<=5`,

while the two cross-degrees contribute at most4 and the two decorations contribute2. Hence its endpoint row-weight sum is at most11, contradicting pair-row coverage12. Thus s=10 is impossible.

### s=11

`e(J)=12`, `t(D)=42`. Three active vertices again give inactive weight at least13>9, so exactly two are active.

The inactive edge count is between1 and4. For a triangle-free five-vertex graph with at most4 edges, every edge has endpoint internal-degree sum at most5. Cross-degree sum is at most4 and decorations contribute2, so every inactive edge has weight sum at most11, impossible. Since edge count forces at least one inactive edge, contradiction.

### s=12

All six lows have degree2, `e(J)=11`, `t(D)=41`. Three active vertices are impossible by the same weight count. Thus exactly two are active.

The set `L` together with the five inactive decorated vertices would be an independent 11-set if there were no inactive edge, so `e_I>=1`. Weight budget again gives `e_I<=4`. The same endpoint internal-degree bound (`<=5`) plus at most four cross incidences and two decoration units makes every inactive edge have row-weight sum at most11, contradiction.

Therefore k=7 is impossible.

---

## Conclusion

There is no E332 extreme shell with

`G=7, h=0`.

The remaining E332 G=7 frontier is now

- `h=1`, and
- the exact two-high state `H2-G7-K4minusE`.

Together with the complete G=4,5,6 closures and the absence of h=2,G=8, the global Line-C frontier is:

- `G=7,h=1`;
- `H2-G7-K4minusE`;
- `G=8,h=0`;
- `G=8,h=1`.
