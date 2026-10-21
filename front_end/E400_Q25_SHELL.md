# Uniform q25 shell theorem and T61 E400 closure

Status: `PROVED`.

This note eliminates all q25 low-pivot cells with shell decoration sum `G=1,2,3`, and consequently closes the entire T61 E400 layer.

## 1. Common q25 cell

Let R be a T61 residual with `E=400`, `delta(R)=13`. Take a degree-13 pivot p and write

- `A=N(p)`, `|A|=13`;
- `C=R-N[p]`, `|C|=47`;
- `M=complement(R[A])`;
- `z=e(M)`;
- decorations `g_a=d_R(a)-13`, total `G=sum_A g_a`;
- weights `t_a=d_M(a)+g_a`;
- `q=z+G`.

The inherited 47-core floor is284, so every degree13 pivot in E400 satisfies

`q<=400-91-284=25`.

The 14-point cap gives `z>=22`.

We prove:

> **q25 shell theorem.** No E400 degree13 pivot can satisfy `q=25` with `1<=G<=3`.

Equivalently, all cells

- `(z,G)=(24,1)`;
- `(23,2)`;
- `(22,3)`

are impossible.

The proof uses only the standard shell contracts:

- `alpha(M)<=10`;
- M has a 3-matching;
- each M-edge has endpoint row-weight sum at least11;
- each M-triangle has row-weight sum at least24;
- an M-K4 is impossible in q25 because it would force q at least30;
- the exact repivot lower bound for an undecorated shell vertex.

---

## 2. Triangle case is impossible

Fix an M-triangle T and let B=A\T, so |B|=10. Put

`c=e_M(T,B)`, `u=e_M(B)`.

Since `z=25-G`,

`3+c+u=25-G`, hence

`c+u=22-G`.

Triangle row coverage gives

`t(T)=6+c+G_T>=24`.

Using `G=G_T+G_B`, this implies

`u+G_B<=4`.

Suppose rs were an M-edge inside B. K4-freeness gives at most two T-neighbours for each endpoint, and

`d_B(r)+d_B(s)<=u+1`.

Therefore

`t_r+t_s <=4+(u+1)+G_B <=9`,

contradicting the required missing-edge weight sum at least11. Thus

`u=0`.

Hence

`c=22-G`.

But every B-vertex has at most two neighbours in T, so `c<=20`. Therefore the case G=1 is already impossible.

### G=2

Now c=20, so every B-vertex has T-degree2.

A regular degree2 B-vertex has weight2 and forces each adjacent triangle vertex to have weight at least9.

If all three triangle vertices meet regular B-vertices, then `t(T)>=27`. Since

`t(T)=26+G_T`,

we must have `G_T>=1`.

- If `G_T=1`, then equality forces all three triangle weights to be9. Any regular B-vertex y has two adjacent missing neighbours of weights9,9. Repivoting at y gives

  `q_y-q >= 23-18 =5`,

  because its 2-row lies in a 47-core of minimum degree at least12. Thus `q_y>=30`, contradicting the universal E400 bound `q_y<=25`.

- If `G_T=2`, then `G_B=0` and the triangle weights sum28 with each at least9, hence are `10,9,9`. Every B-vertex is regular degree2; its two triangle neighbours have weight sum at most19, so the same repivot bound gives a strict increase to `q_y>25`, contradiction.

If some triangle vertex i meets no regular B-vertex, all its B-neighbours are decorated. Let their decorations be positive integers `r_j`; with `g_i` the decoration on i, the total budget gives

`g_i+sum r_j <=2`.

If k such decorated B-neighbours exist, then `h_i=c_i+g_i=k+g_i`. For any one of them the missing-edge inequality requires

`h_i >=7-r_j`.

But `r_j <= 2-g_i-(k-1)=3-g_i-k`, so the right side is at least `4+g_i+k`, strictly larger than `h_i`. Contradiction.

Thus G=2 triangle cells are impossible.

### G=3

Now c=19: nine B-vertices have T-degree2 and one has T-degree1.

If all three triangle vertices meet regular degree2 B-vertices, each has weight at least9, so `t(T)>=27`. Since `t(T)=25+G_T`, we have `G_T>=2`.

- `G_T=2`: triangle weights are all9. There are at least eight regular degree2 B-vertices; repivoting any one whose neighbours have weights9,9 raises q by at least5, contradiction.
- `G_T=3`: `G_B=0`; triangle weights sum28, so they are `10,9,9`. Every B-vertex is regular; any degree2 B-vertex has neighbour-weight sum at most19 and gives a profitable repivot, contradiction.

If a triangle vertex i meets no regular degree2 B-vertex, its B-neighbours can only be decorated degree2 vertices or the unique degree1 vertex. A degree1 neighbour requires even more weight than a degree2 neighbour and is immediately impossible under total decoration3. For decorated degree2 neighbours the same budget argument as above gives

`k+g_i < 7-r_j`

for at least one required edge, contradiction.

Therefore G=3 triangle cells are impossible.

So no q25 cell with G=1,2,3 contains a triangle.

---

## 3. Triangle-free case is impossible

Assume M is triangle-free.

### 3.1 Matching number is exactly3

The h13 shell supplies a 3-matching. A 4-matching would have eight endpoints with total weight at least44. Mantel gives at most16 missing edges among those endpoints, hence

`q>=44-16=28`,

contradicting q25. Therefore

`nu(M)=3`.

### 3.2 M is bipartite

Any odd cycle of length at least7 already gives too much charge: summing the edge inequalities around a C_(2k+1) gives endpoint weight at least `ceil(11(2k+1)/2)`, and for C7 this yields q at least32.

So a nonbipartite M would contain a C5. Let B be the other eight vertices. Summing the five cycle-edge inequalities gives

`t(C5)>=28`.

The subset identity then gives

`25 >= 28-5+e(M[B])+G_B`,

so

`e(M[B])+G_B<=2`.

Write c for the number of C5-B edges. Since `z=25-G`,

`c=20-G-e(M[B])`.

Triangle-freeness gives at most two cycle neighbours per B-vertex, hence `c<=16`.

For G=1 this is already impossible.

For G=2 or3, if `e(M[B])>0`, choose a B-edge xy. Because `nu(M)=3`, every C5-B edge must then have its B-end in {x,y}: otherwise that cross edge, xy, and a 2-matching in the C5 avoiding the cycle endpoint form a 4-matching. Thus c<=4, contradicting the displayed lower bound (at least15).

Hence `e(M[B])=0`, which gives c=18 or17 for G=2 or3, again exceeding16.

Thus M is bipartite.

### 3.3 König cover and regular-vertex repivots

Since M is bipartite and `nu(M)=3`, König gives a vertex cover X of size3. Let Y=A\X, so |Y|=10 and Y is independent.

Let `e_X=e(M[X])`; triangle-freeness gives `e_X<=2`. From the subset identity with S=X,

`t(X)=25+e_X-G_Y`.

We claim no undecorated y in Y can have missing degree2 or3.

- If `d_M(y)=3`, then its missing-neighbour set is all X. The degree-3 repivot lower bound gives

  `q_y-q >= 30-(t(X)-e_X) = 5+G_Y >0`,

  contradicting `q_y<=25`.

- If `d_M(y)=2`, let its two missing neighbours be i,j in X and k the third cover vertex. Nonprofitability would require

  `t_i+t_j-e_M(ij) >=22`.

  Hence

  `t_k <= 25+e_X-G_Y - (22+e_M(ij)) <= 5-G_Y`.

  Because `alpha(M)<=10` and Y itself is an independent10-set, k must have at least one neighbour b in Y. The missing-edge inequality gives

  `t_b >= 11-t_k >= 6+G_Y`.

  But `t_b=d_M(b)+g_b<=3+g_b<=3+G_Y`, contradiction.

Therefore every undecorated Y-vertex has missing degree at most1.

At most G of the ten Y-vertices are decorated. Decorated Y-vertices have missing degree at most3. Hence

`e_M(X,Y) <= (10-G)*1 + G*3 = 10+2G <=16`.

But

`e_M(X,Y)=z-e_X >= (25-G)-2 =23-G`,

which is at least20 for G<=3. Contradiction.

Thus the triangle-free channel is impossible as well.

This proves the q25 shell theorem.

---

## 4. E400 is empty

For E400 the total degree excess above13 is

`Xi=7`,

and every degree13 pivot sees at most3 units of neighbour excess.

Let p be a degree13 vertex adjacent to at least one positive-excess vertex. Then `G_p` is 1,2, or3.

- If `G_p=1`, q is 23,24,or25. The q23 cell is impossible by `E398_Q23_SHELL.md`; the q24 `(z,G)=(23,1)` cell is impossible by `E399_Q24_SHELL.md`; the q25 cell is impossible by this theorem.
- If `G_p=2`, q is24 or25. The q24 `(22,2)` cell was already eliminated; q25 is eliminated here.
- If `G_p=3`, q is forced to25 with z22, eliminated here.

Therefore **no degree13 vertex can be adjacent to any positive-excess vertex**.

But the total excess is only7, so there are at most seven positive-excess vertices. Any such vertex has degree at least14 and hence cannot obtain all its neighbours inside a set of at most seven vertices. It must have a degree13 neighbour, contradiction.

Therefore

`T61(E400)=empty`.

The surviving front-end window advances to

`401<=E<=408`, `delta=13`.
