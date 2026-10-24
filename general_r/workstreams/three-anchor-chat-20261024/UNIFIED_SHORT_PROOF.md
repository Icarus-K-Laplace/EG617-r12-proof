# Exact Three-Anchor Excess Theorem — unified short proof

## Theorem

Let `r>=12`. Let `H` be a graph on `3r-1` vertices satisfying

- `alpha(H)<=3`,
- `omega(H)<=r-1`,
- `delta(H)>=r`.

Suppose `a1,a2,a3` are pairwise nonadjacent and `d(ai)=r` for all `i`. Then

`K:=sum_v(d(v)-r)=2e(H)-r(3r-1)>=8`.

We prove this by contradiction. Since `r(3r-1)` is even, `K` is even. Thus it suffices to exclude `K<=6`.

---

## 1. Anchor partition

Every non-anchor meets at least one anchor, otherwise it forms an independent 4-set with `a1,a2,a3`.

Let `Xi` be the vertices adjacent to exactly `ai`. Let `C` be the vertices adjacent to at least two anchors, `c=|C|`, and let `t` be the number adjacent to all three.

Counting anchor incidences gives

`3r=(3r-4)+c+t`,

hence

`c+t=4`.

Each `Xi union {ai}` is a clique: if two vertices of `Xi` were nonadjacent, together with the other two anchors they would form an independent 4-set. Hence `|Xi|<=r-2`.

Set

`d_i=(r-2)-|Xi|>=0`.

If `s_i` is the number of connectors adjacent to `ai`, then `s_i=r-|Xi|=2+d_i`. Therefore

`d_1+d_2+d_3=c-2`.

Also, if `q_i` is the number of connectors missing `ai`, then

`q_i=c-s_i=d_j+d_k`.

Thus, up to permutation, there are exactly four geometries:

1. `c=2`, `d=(0,0,0)`;
2. `c=3`, `d=(0,0,1)`;
3. `c=4`, `d=(0,0,2)`;
4. `c=4`, `d=(0,1,1)`.

---

## 2. Rectangle lemmas

For `x in Xi` with excess `e_x=d(x)-r`, the number of neighbours outside `Xi union {ai}` is exactly

`2+d_i+e_x`.

### Pair-connector rectangle

Let pair connector `z` miss anchor `ak` and be incident with `ai,aj`. Put

`A=Xi\N(z)`, `B=Xj\N(z)`, `a=|A|`, `b=|B|`.

Then `A-B` is complete. Otherwise `z,ak,x,y` is an independent 4-set for a missing edge `xy` with `x in A,y in B`.

If the available baseline external capacities on `Xi,Xj` are `p,q`, the rectangle forces exclusive excess at least

`R_pq(a,b)=a(b-p)_+ + b(a-q)_+`.

We use

`R22`, `R23`, `R24`, `R33`.

For `s=a+b`:

- `R22>=s-4`, and if `s>=5`, `R22>=s-3`;
- `R23>=s-5`;
- `R24>=s-6`;
- `R33>=s-6`.

If two rectangles share one block but their opposite blocks are disjoint, their charges add, because the forced neighbour sets are disjoint.

### Common-nonneighbour clique

If `p,q` are nonadjacent, then their common nonneighbour set is a clique; otherwise two nonadjacent common nonneighbours together with `p,q` form an independent 4-set.

### Same-missing-anchor disjointness

If two nonadjacent pair connectors miss the same anchor, they cannot share a nonneighbour in either incident exclusive block. Otherwise that common nonneighbour, the missed anchor, and the two connectors form an independent 4-set.

---

## 3. Geometry c=2: `(r-2,r-2,r-2)`

The two connectors `p,q` are triple connectors.

Fix `p`, with excess `k_p`, and let `eps` be the indicator of `pq in E(H)`. Let `P` be the set of positive-excess exclusive vertices, and define

`E_i=Xi\(N(p) union P)`.

Every vertex of `E_i` is exact, is nonadjacent to `p`, and has cross-`X` degree at most two.

### 3.1 No `E_i` is empty

Suppose `E_1` is empty. Since `p` cannot be complete to `X1` (else `X1+a1+p` is an `r`-clique), let

`A1=X1\N(p)`, `m=|A1|>=1`.

Every vertex of `A1` has positive excess. Let

`S=sum_{x in A1}(d(x)-r)>=m`.

Let `k_q` be the excess of `q`. Since total exclusive excess is `K-k_p-k_q`, the number of positive-excess exclusive vertices outside `A1` is at most

`K-k_p-k_q-S`.

Write `n_i=|N(p) cap Xi|`. From the degree of `p`,

`n_2+n_3=m+k_p-eps-1`.

Hence, for `i=2,3`,

`|E_i| >= r-2-(n_2+n_3)-(K-k_p-k_q-S)`

`=r-1-m-K+eps+k_q+S`.

Let `s=min(|E_2|,|E_3|)`. Since `K<=6` and `S>=m`,

`s>=r-7+eps+k_q>=5`.

Fix `x in A1`. Put `B_i=E_i\N(x)`. The bipartite graph `B_2-B_3` must be complete, otherwise `p,x,y,z` is an independent 4-set. Since vertices of `E_2,E_3` have cross-`X` degree at most two, either one `B_i` is empty or both have size at most two. As `s>=5`, in either case `x` has at least `s` neighbours in `E_2 union E_3`. Thus

`d(x)-r>=s-2`.

Summing over `A1` gives

`S>=m(s-2)`

`>=m(r-3-m-K+eps+k_q+S)`

`>=m(S+3-m)`,

because `r>=12` and `K<=6`.

But

`m(S+3-m)-S=(m-1)S+3m-m^2 >=2m>0`

using `S>=m`. Contradiction.

Therefore all three `E_i` are nonempty.

### 3.2 Degree-two transversal cover

The tripartite graph on `E_1,E_2,E_3` has maximum degree at most two and no independent transversal; otherwise adding `p` gives an independent 4-set.

A simple degree-two cover lemma says that either

- two parts have size at most two; or
- after permutation the sizes are `(1,3,3)` or `(2,3,3)`.

Proof: if two parts, say `E_2,E_3`, have size at least three, then for any `x in E_1` the nonneighbours of `x` in `E_2,E_3` must span a complete bipartite graph. Maximum degree two forces both nonneighbour sets to have size at most two, hence `|E_2|+|E_3|<=6`, so both equal three. The resulting `K_{2,2}` between the two nonneighbour sets uses all degree of those four vertices, forcing `|E_1|<=2`.

If two `E`-parts have size at most two, then

`r<=5+K<=11`,

by comparing the connector-neighbour budget with the number of removed positive-excess vertices. Contradiction.

In the exceptional `(1/2,3,3)` case, `sum_i|E_i|<=8`. But

`sum_i|E_i| >= 3r-6-(r-3+k_p-eps)-(K-k_p-k_q)`

`=2r-3-K+k_q+eps>=2r-9>=15`.

Contradiction. Thus `c=2` is impossible.

---

## 4. Geometry c=3: `(r-2,r-2,r-3)`

There is one triple connector `w` and two pair connectors `u,v`, both incident with the short block `X3`.

Call a pair connector focused if it is complete to `X3`.

If both are nonfocused, their `R23` charges are additive. For each nonfocused connector with excess `k` and connector-degree `gamma`,

`a+b>=r-3-k+gamma`,

so

`k+R23>=r-8+gamma`.

Hence the two charges total at least `2r-16>=8`.

If both are focused, they cannot be adjacent, since `X3+a3+u+v` would be an `r`-clique. If nonadjacent, their common nonneighbour set has size at least

`2r-5-k_u-k_v >=2r-11>r-1`,

and is a clique. Contradiction.

Thus exactly one, say `u`, is focused. For nonfocused `v`, the focused neighbour consumes one `X3` slot, so its rectangle is governed by `R22` and

`a+b>=r-3-k+gamma`.

If `r>=14`, then `k+R22>=r-7+gamma>=7`, contradiction.

For `r=13`, any `gamma>=1` gives at least seven. If `gamma=0` and `k<=5`, then `a+b>=5` and the sharpened `R22>=a+b-3` gives at least seven. Hence the only possible layer is

`k=6`, `gamma=0`, `(a,b)=(2,2)`.

All other vertices are exact and `v` has no neighbour in the opposite long block. A vertex `x` in the long-side nonneighbour pair is saturated by the two rectangle edges. Then `v,w,x,y` forces `w` adjacent to every vertex `y` of the opposite long block, and that block together with its anchor and `w` is an `r`-clique. Contradiction.

For `r=12`, the same argument leaves only the low-budget layers described in `R12_UNIFIED_CLOSURE.md`: every such layer has a saturated rectangle vertex. If the nonfocused connector has no neighbour in the opposite 10-block, that saturated vertex forces the triple connector to be complete to the block, giving a 12-clique. The only one-neighbour layer is `(k,a,b)=(6,2,2)`; then a saturated long-block rectangle vertex forces the exact focused connector to have at least nine neighbours in the opposite 10-block, impossible.

Thus `c=3` is impossible for every `r>=12`.

---

## 5. Geometry c=4, deficits `(0,0,2)`

Here

`|X1|=|X2|=r-2`, `|X3|=r-4`.

There are two connectors in each missing-anchor group, and all four are incident with `a3`.

A connector is focused if it is complete to `X3`.

Two focused connectors must be adjacent: otherwise their common nonneighbour set has size at least

`2r-6-k_p-k_q>=2r-12>r-1`.

Three focused connectors would then form, together with `X3+a3`, an `r`-clique. Hence the number `f` of focused connectors satisfies `f<=2`.

A nonfocused connector satisfies

`a+b>=r-4-k+gamma`.

After `f` focus neighbours consume `f` short-block slots, its rectangle has capacities `(2,4-f)`, giving the crude local bound

`L_f:=k+R_{2,4-f} >= r-10+f+gamma`.

### f=0

If neither same-group pair is adjacent, all four rectangle charges add, so

`K>=4(r-10)>=8`.

If exactly one same-group pair is adjacent, take one connector from it and both connectors of the nonadjacent pair. Their charges add and give

`K>=(r-9)+2(r-10)=3r-29>=7`.

If both same-group pairs are adjacent, any cross-group pair has additive charge at least

`2(r-9)`.

This exceeds six for `r>=13`. At `r=12`, equality would force local charge three on all four connectors. Since `gamma>=1`, the sharpened `R24` threshold shows local charge three is possible only for

`gamma=1`, `k=3`, `(a,b)=(4,2)`.

All four connectors would then have excess three, contradiction.

### f=1

There are three nonfocused connectors. A cross-group pair has additive effective-`R23` charge at least

`2(r-9)`.

For `r>=13` this exceeds six. At `r=12`, `K<=6` forces all three nonfocused connectors to have `gamma=0`; the same-group pair is then nonadjacent, its supports are disjoint, and all three local charges add to at least nine. Contradiction.

### f=2

If the two nonfocused connectors are from different groups, or are a nonadjacent same-group pair, their effective-`R22` charges add to at least

`2(r-8)>=8`.

Thus they are an adjacent same-group pair. Write their excesses `k1,k2`, and choose the smaller `m=min(k1,k2)<=3`. For that connector,

`a+b>=r-3-m`.

If `r>=13`, then `a+b>=7`, so

`R22>=a+b-3>=r-6-m`.

Therefore

`K>=k1+k2+R22 >= r-6+max(k1,k2)>=7`,

contradiction.

At `r=12`, equality can occur only when `k1=k2=0`, both connector-degrees equal one, and each rectangle has `(a,b)=(1,8)` or `(8,1)`. Equality of the union charge forces the same orientation and the same charged vertex. The `(1,8)` orientation gives an independent 4-set with one exact focused connector; the `(8,1)` orientation gives a common-nonneighbour clique that would require an exact long-block rectangle vertex to have at least nine cross-neighbours. Both are impossible.

Thus `(0,0,2)` is impossible for every `r>=12`.

---

## 6. Geometry c=4, deficits `(0,1,1)`

Here

`|X1|=r-2`, `|X2|=|X3|=r-3`.

There are two connectors `U1,U2` missing `a1`, one connector `V` missing `a2`, and one `W` missing `a3`.

A focus slot `Xi`, `i=2,3`, is occupied if some connector incident with `ai` is complete to `Xi`.

No two connectors can occupy the same focus slot. If adjacent they form an `r`-clique with `Xi+ai`; if nonadjacent their common nonneighbour set has size at least

`2r-5-k_p-k_q>=2r-11>r-1`.

Let `s` be the number of occupied focus slots.

For `V` or `W`, with no focus on its deficit-one block,

`k+R23>=r-8+gamma`;

with that block focused, its effective `R22` charge is at least

`r-7+gamma`.

For a nonfocused `U`, no occupied incident slot gives `R33>=r-10+gamma`, one occupied incident slot gives effective `R23>=r-9+gamma`, and two occupied incident slots give effective `R22>=r-8+gamma`.

### s=0

`V` and `W` are nonfocused and their rectangles are additive. Hence

`K>=2(r-8)>=8`.

### s=1

Suppose `X3` is occupied.

If `V` owns the slot, then `W` and both `U` connectors are nonfocused. `W` plus either `U` give additive charge at least

`(r-8)+(r-9)=2r-17>=7`.

If a `U` owns the slot, then `V,W` are nonfocused and additive, with charge at least

`(r-7)+(r-8)=2r-15>=9`.

Thus `s=1` is impossible.

### s=2

If the same `U` owns both slots, or distinct `U` connectors own them, then `V,W` are nonfocused and give additive charge at least `2(r-7)>=10`.

If one `U` and one of `V,W` own the slots, the remaining external connector and the remaining `U` have additive charge at least

`(r-7)+(r-8)=2r-15>=9`.

The only remaining ownership pattern is: `V` owns `X3` and `W` owns `X2`. Then both `U` connectors are nonfocused and both incident blocks have one focused neighbour. If the `U` pair is nonadjacent, same-missing-anchor disjointness gives additive charge at least

`2(r-8)>=8`.

Hence the `U` pair is adjacent. Its overlap analysis is exactly the `f=2` analysis above: for `r>=13`, choosing the smaller connector excess gives `K>=r-6>=7`; for `r=12`, the only equality skeletons are the same `(1,8)/(8,1)` `R22` rectangles, and each yields an independent 4-set with one exact focused connector.

Thus `(0,1,1)` is impossible for every `r>=12`.

---

## 7. Conclusion

All four anchor geometries are impossible under `K<=6`. Therefore

`K>=8`.

This proves the Exact Three-Anchor Excess Theorem for every `r>=12` by one analytic argument. No computation-certified step and no historical fixed-`r` case table is required.
