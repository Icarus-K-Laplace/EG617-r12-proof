# E332 uniform reduction for the remaining one-high branches (G=7,8)

Status: `PROVED` for the reductions in this note.

Assume the canonical E332 state:

- `q=30`, `e(core)=211`, `delta(core)>=12`;
- every undecorated shell missing degree lies in `{0,1,2,11,12}`;
- total decoration `G in {7,8}`;
- exactly one undecorated high shell vertex `a` (`h=1`);
- decorated set `D`, `k=|D|`;
- undecorated low set `L`, `l=12-k`;
- `L` is independent in the missing graph;
- strengthened zero-gap theorem and the triangle-row union lemma are available.

Write `J=M[D]`.

## 1. High missing-degree 11 is impossible for both G=7 and G=8

Assume `d_M(a)=11`, and let `w` be the unique shell vertex not missing-adjacent to `a`.

For every low vertex `u`, the edge `au` together with the strengthened zero-gap theorem forces `u` to have degree2 with second missing neighbour exactly `w`. Hence:

- `w in D`;
- `a` is missing-adjacent to every low and every decorated vertex except `w`;
- every low has missing neighbourhood `{a,w}`;
- there are no other low-decorated missing edges.

Exact edge counting gives

`e(J)=k+7-G`.

Also `L union (D-{w})` has size11. Therefore `J-w` cannot be edgeless, otherwise this would be an independent 11-set in `M`, contradicting `alpha(M)<=10`.

Choose an edge `xy` in `J-w`. Then `a,x,y` form an M-triangle. Since `t_a=11`, triangle-row coverage gives

`t_x+t_y>=13`.

For `x,y != w`,

`t_x=1+d_J(x)+g_x`, `t_y=1+d_J(y)+g_y`.

If a graph has `m=e(J)` edges, then for any edge `xy`,

`d_J(x)+d_J(y)<=m+1=k+8-G`.

Therefore

`g_x+g_y >= 11-(k+8-G)=G+3-k`.

The other `k-2` decorated vertices are all positive, so the total decoration is at least

`(G+3-k)+(k-2)=G+1`,

contradicting total decoration `G`.

Hence:

`d_M(a)=11` is impossible for both `G=7` and `G=8`.

## 2. High missing-degree 12: every low is of type {a} or {a,x}

Now `d_M(a)=12`, so `a` is universal in the missing shell.

Let

`r=e_M(L,D)`

be the number of low-decorated missing incidences. Since a low has missing degree at most2, every low has missing neighbourhood either `{a}` or `{a,x}` for a unique decorated vertex `x`.

The edge ledger is

`r+e(J)=18-G`.

Thus:

- for `G=7`, `e(J)=11-r`;
- for `G=8`, `e(J)=10-r`.

Call a decorated vertex **active** if it receives at least one low edge, and let `m` be the number of active decorated vertices.

For an active `x`, choose a low `u` with `N_M(u)={a,x}`. Since `a in N_M(x)`,

`|N_M(u) union N_M(x)| = d_M(x)+1`.

The strengthened zero-gap theorem therefore gives

`t_x=d_M(x)+g_x >= 12`.

Every inactive decorated vertex has weight at least2 because it is adjacent to `a` and has positive decoration.

The total decorated row weight is

`t(D)=36-G+k-r`.

Hence

`12m+2(k-m) <= 36-G+k-r`,

or

`10m <= 36-G-k-r`.

In particular `m<=2`.

## 3. Two active decorated vertices are impossible

Assume `m=2`. Put `n=k-2` and `e=e(J)=18-G-r`.

At most one J-edge lies inside the active pair, and at most `2n` edges join active to inactive vertices.

If `e-1<=2n`, then the sum of J-degrees over inactive vertices is at least `e-1`. Therefore

`t(D) >= 24 + 2n + (e-1)
       = 37+2k-G-r,
`

while the exact value is `36-G+k-r`, a contradiction by `k+1>0`.

If `e-1>2n`, then after saturating the active-active edge and all active-inactive edges, the remaining edges lie inside the inactive set. The inactive degree sum is at least

`2(e-1)-2n`.

Hence

`t(D) >= 24+2n+2(e-1)-2n = 22+2e = 58-2G-2r`.

But the active-weight inequality already gives

`k+r <= 16-G`.

Thus

`(58-2G-2r) - (36-G+k-r)
 =22-G-k-r
 >=6`,

again impossible.

Therefore:

`m<=1`.

## 4. Consequences when r>0

If `r>0`, then `m=1`. Let `x` be the unique active decorated vertex. The inactive decorated set has size `k-1`.

Because

`|L| + |D\{x}| = (12-k)+(k-1)=11`,

the inactive induced graph must contain an edge, or else M would contain an independent 11-set.

Let `ij` be such an inactive edge. Since `e(J)=18-G-r`,

`d_J(i)+d_J(j) <= e(J)+1 = 19-G-r`.

Pair-row coverage gives

`g_i+g_j >= 10-d_J(i)-d_J(j) >= G+r-9`.

All other `k-2` decorated vertices are positive, so

`G >= (G+r-9)+(k-2)`.

Hence every one-active survivor satisfies

`k+r<=11`.

A second consequence comes from total-weight minimization. When `e(J)>k-1` (equivalently `k+r<19-G`), after putting as many J-edges as possible on the unique active vertex, the inactive degree sum is at least

`2e(J)-(k-1)`.

Using active weight at least12 gives the necessary condition

`r>=11-G`.

Thus:

- for `G=7`, every one-active survivor has `r>=4` and `k+r<=11`;
- for `G=8`, every one-active survivor has `r>=3` and `k+r<=11` (with the equality boundary handled by the same inactive-edge correction; in particular `k=8,r=3` is impossible).

## 5. Exact remaining parameter windows

### G=7, h=1

Every survivor has high missing-degree12 and either:

1. `r=0`, no active decorated vertex, with `k in {6,7}`; or
2. exactly one active decorated vertex, with
   - `k=3, r=8`;
   - `k=4, r in {5,6,7}`;
   - `k=5, r in {4,5,6}`;
   - `k=6, r in {4,5}`;
   - `k=7, r=4`.

### G=8, h=1

Every survivor has high missing-degree12 and either:

1. `r=0`, no active decorated vertex, with `k in {5,6,7,8}`; or
2. exactly one active decorated vertex, with
   - `k=3, r in {7,8}`;
   - `k=4, r in {4,5,6,7}`;
   - `k=5, r in {3,4,5,6}`;
   - `k=6, r in {3,4,5}`;
   - `k=7, r in {3,4}`.

No high-degree11 state and no two-active state survives.

## Conclusion

The remaining one-high E332 frontier for both `G=7` and `G=8` is a single-active (or zero-active) universal-high problem. The next attack should use the exact `J` edge count together with pair/triangle/K4 row coverage to eliminate the finite `(k,r)` windows above.
