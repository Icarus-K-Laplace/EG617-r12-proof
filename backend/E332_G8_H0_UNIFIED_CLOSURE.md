# Unified closure of E332, G=8, h=0

Status: `PROVED EMPTY`.

This note gives a shorter and more robust replacement for the case-heavy split of `E332_G8_H0_K3_K6_CLOSURE.md` and `E332_G8_H0_FULL_CLOSURE.md`.

Assume the canonical E332 state with

- `q=30`, `e(core)=211`, `delta(core)>=12`;
- total shell decoration `G=8`;
- no undecorated high shell vertex (`h=0`);
- decorated set `D`, `k=|D|`;
- undecorated low set `L`, `|L|=13-k`;
- `L` independent and every low has missing degree at most2;
- strengthened zero-gap theorem, pair-row coverage, triangle-row union, and `alpha(M)<=10`.

Let

- `s=e_M(L,D)`;
- `J=M[D]`, so `e(J)=22-s`;
- `A` be the low-active decorated vertices, `m=|A|`;
- `I=D\A`;
- `a=e_J(A)`, `c=e_J(A,I)`, `b=e_J(I)`;
- `g_A=sum_{x in A} g_x`.

Every active decorated vertex has row weight at least11.

## 1. The master active-weight identity

The active row-weight sum is

`W_A = s + 2a + c + g_A`.

Since `a+b+c=22-s`, this becomes

`W_A = 22 + a - b + g_A`.

Therefore

`22+a-b+g_A >= 11m`.  (1)

Now assume `b>0`, and choose an inactive edge `uv`.

Its two endpoints have at most `2m` active cross-incidences in total. Inside the b-edge inactive graph,

`d_I(u)+d_I(v) <= b+1`.

The other `k-m-2` inactive decorated vertices each consume at least one decoration unit, hence

`g_u+g_v <= 8-g_A-(k-m-2)=10-k+m-g_A`.

Thus

`t_u+t_v <= 2m+(b+1)+(10-k+m-g_A)`

`= b+11-k+3m-g_A`.

Pair-row coverage gives `t_u+t_v>=12`, so

`b >= 1+k-3m+g_A`.  (2)

Combining (1) and (2), with `b<=22+a+g_A-11m`, gives

`a >= k+8m-21`.  (3)

This is the main compression inequality.

## 2. The case b=0

If `b=0`, then `L union I` is independent in M and has size

`|L|+|I|=(13-k)+(k-m)=13-m`.

Since `alpha(M)<=10`, necessarily `m>=3`.

Using `a<=C(m,2)` and `g_A<=8-k+m`, inequality (1) gives

`11m <= 22+C(m,2)+8-k+m`.

For `m>=4` this is impossible. For `m=3`, equality forces

`k=3`, `a=3`, `g_A=8`.

Thus `J=K3`, `s=19`, and `W_A=33`, so all three active row weights are exactly11. But ten low vertices carry nineteen incidences, hence exactly one low has missing degree1. A degree1 low requires its decorated neighbour to have row weight at least12 by the strengthened zero-gap theorem. Contradiction.

Hence every survivor must have `b>0`.

## 3. Consequences of b>0

From (3), `a<=C(m,2)` and `k>=m`:

- every `m>=3` is impossible;
- if `m=2`, then `k<=6`;
- only `m=0,1,2` require consideration.

## 4. No-active case m=0

Then `s=0` and `e(J)=22`.

Since all k decorated vertices are positive and total decoration is8, `k<=8`; but `C(7,2)=21`, so `k=8` and every decoration equals1.

For every J-edge, pair coverage gives

`d_J(u)+d_J(v)>=10`.

If J contains a triangle, triangle-row coverage gives degree sum at least21, so all three triangle vertices have degree7. Thus every triangle would consist entirely of universal vertices.

If there is at most one universal vertex, J is triangle-free, impossible because `e(J)=22>16` by Mantel. If there are at least two universal vertices and any nonuniversal vertex exists, those two universal vertices together with it form a triangle containing a nonuniversal vertex, impossible. All eight vertices cannot be universal because that would give28 edges.

Contradiction. Hence `m=0` is impossible.

## 5. One-active case m=1

The unique active vertex sees at most all `13-k` lows, so

`s<=13-k`.

It has at most `k-1` cross edges into I. Hence

`b=e(J)-c >= 22-(13-k)-(k-1)=10`.

Thus `k>=6`.

### k=6

I has five vertices and `b>=10`, so `J[I]=K5`. Any inactive triangle has full J-degree sum at most15. Its decoration sum is at most5 because the active vertex and the two other inactive vertices are positive. Hence its row-weight sum is at most20<24, contradicting triangle-row coverage.

### k=7

I has six vertices and `b>=10>9`; hence it contains a triangle. The full J-degree sum of an inactive triangle is at most18, while its decoration sum is at most4. Thus the triangle row-weight sum is at most22<24. Contradiction.

### k=8

All decorations equal1. The active weight is at least11, so if c is its J-cross degree,

`s+c>=10`.

Therefore

`b=22-s-c<=12`.

If `J[I]` contains a triangle, triangle-row coverage forces all three triangle vertices to have full J-degree7, hence internal degree6; three such universal vertices in the seven-vertex inactive graph force at least15 inactive edges, contradicting `b<=12`.

So `J[I]` is triangle-free. For an inactive edge uv in a triangle-free seven-vertex graph,

`d_I(u)+d_I(v)<=7`.

Adding at most two active cross-incidences gives full degree sum at most9. With decorations1 on both endpoints,

`t_u+t_v<=11<12`, contradicting pair-row coverage.

Thus `m=1` is impossible.

## 6. Two-active case m=2

Because `|L|+|I|=11`, the inactive graph must contain an edge, so `b>0` as already assumed.

From (3), `k<=6`. Also `k>=4`, since for k=2 or3 the inactive set has at most one vertex and cannot contain an edge.

We now have only k=4,5,6.

### k=4

I has two vertices, so `b=1`. Inequality (2) gives

`1>=g_A-1`.

Since both active decorations are positive, `g_A=2`.

The inactive decoration total is6. Pair coverage on the unique inactive edge forces both inactive vertices to be adjacent to both active vertices; thus `c=4`.

If the active pair is not a J-edge (`a=0`), then (1) gives active row-weight sum23. One active vertex has weight11. The inactive edge has row-weight sum exactly12, and together with that weight-11 active vertex forms a J-triangle of total23, contradicting triangle-row coverage.

Hence `a=1`. Then `J=K4` and both active weights are12.

Let the inactive vertices be u,v. The two triangles `xuv` and `yuv` have total row-size exactly24. Hence

- `D_x,D_u,D_v` are pairwise disjoint;
- `D_y,D_u,D_v` are pairwise disjoint.

A missing K4 has full core row cover:

`D_x union D_y union D_u union D_v = V(core)`,  (K4-cover)

because any core vertex outside all four rows would be nonadjacent in F to four shell vertices forming an independent 4-set, creating an independent 5-set.

Therefore `D_u union D_v` is a 12-set disjoint from `D_x union D_y`, and K4-cover forces

`|D_x union D_y|=23`, hence `|D_x intersect D_y|=1`.

The active low incidences total16 and both active vertices have exactly eight low neighbours. Hence at least seven lows have missing neighbourhood `{x,y}`.

For any such pair-low w, the strengthened zero-gap equality on wx and wy gives

`D_w subseteq D_u union D_v`.

Each vertex of `D_u union D_v` has one base shell adjacency to u or v. If its multiplicity among the pair-low rows is m_z, its global degree excess is at least m_z.

There are at least14 endpoint incidences of pair-low rows on this 12-set. The minimum possible sum of multiplicity squares is18, so for at least one pair-low row `{r,s}`,

`m_r+m_s>=3`.

Repivot at that degree-13 low. The two active decorations x,y (total decoration2) leave the shell, while the two imported core vertices contribute global excess at least `m_r+m_s>=3`. Thus

`G' >= 8-2+3 =9`,

contradicting the universal E332 ceiling `G'<=q'-22<=8`.

So k=4 is impossible.

### k=5

I has three vertices. An inactive triangle has total row-weight strictly below24, so `J[I]` is triangle-free and `b<=2`.

Inequality (2) gives `b>=g_A`; since `g_A>=2`,

`b=2`, `g_A=2`.

Thus `J[I]=P3`. Equality in the inactive-edge bound forces every inactive vertex to be adjacent to both active vertices, and the inactive decorations are exactly

`(4,1,1)`

with 4 on the path centre.

If `a=0`, (1) gives both active row weights11. The path centre and either leaf have row weights8 and4, and with either active vertex form a J-triangle of total23, contradiction.

If `a=1`, the active row-weight sum is23, so one active vertex still has weight11. The same triangle has total23. Contradiction.

Hence k=5 is impossible.

### k=6

I has four vertices. Inequalities (1) and (2) force

`a=1`, `b=g_A+1`.

The inactive graph is triangle-free, so `b<=4`; hence `g_A` is2 or3.

If `g_A=3`, then `b=4` and `J[I]=C4`. Equality in the inactive-edge bound forces endpoint decoration sum3 on every C4 edge. Summing around the cycle gives inactive decoration total6, but the true inactive decoration total is5. Contradiction.

If `g_A=2`, then `b=3`. Equality in the edge bounds forces all four inactive vertices to be adjacent to both active vertices and every inactive edge to have endpoint decoration sum4. The only triangle-free three-edge graph on four vertices compatible with inactive decoration total6 is a star with decoration pattern

`(3,1,1,1)`.

Equation (1) gives both active row weights11. The star centre has row weight8 and each leaf row weight4. An active vertex, the star centre and any leaf form a J-triangle of total23, contradiction.

Thus k=6 is impossible.

## Conclusion

All possibilities m=0,1,2 are impossible, and m>=3 was already excluded. Therefore no `G=8,h=0` E332 shell exists.

Combined with `E332_G8_H1_TO_H0_REDUCTION.md`, the entire G=8 layer is empty. This gives a unified proof of the final E332 decoration layer and independently reconfirms

`E332 = EMPTY`.
