# Proof attempts — analytic proof ledger

This file contains the current parameterized proof. No statement below depends on computational enumeration.

## 1. Setup, partition, parity

Let `a1,a2,a3` be pairwise nonadjacent degree-`r` anchors. Every other vertex meets at least one anchor, else it completes an independent 4-set with the anchors.

Let `Xi` be adjacent to exactly `ai`; let `C` be adjacent to at least two anchors, `c=|C|`; let `t` count triple connectors. Anchor incidence gives

`3r=(3r-4)+c+t`, so `c+t=4`.

Each `Xi union {ai}` is a clique: two nonadjacent vertices of `Xi` plus the other two anchors would be independent. Hence `|Xi|<=r-2`. Put

`d_i=(r-2)-|Xi|`.

Then

`d_1+d_2+d_3=c-2`,

so, up to permutation, the only deficit vectors are

`(0,0,0)`, `(0,0,1)`, `(0,0,2)`, `(0,1,1)`.

If `q_i` is the number of connectors missing `ai`, anchor `ai` has `2+d_i` connector neighbours, hence

`q_i=c-(2+d_i)=d_j+d_k`.

Thus the connector types are fixed by the deficit vector.

Finally

`K=2e(H)-r(3r-1)`

is even. Hence a counterexample to `K>=8` automatically satisfies

`K<=6`.

For `x in Xi` with excess `e_x=d_H(x)-r`, its number of neighbours outside `Xi union {ai}` is exactly

`2+d_i+e_x`.

We call `2+d_i` its **baseline external capacity**.

---

## 2. Rectangle and focus lemmas

### 2.1 Pair-connector rectangle
Suppose pair connector `z` misses anchor `ak` and is incident to `ai,aj`. Let

`A=Xi\N(z)`, `B=Xj\N(z)`.

Then `A-B` is complete. Otherwise `z,ak,x,y` is an independent 4-set for a missing `xy` with `x in A,y in B`.

If the baseline external capacities are `p=2+d_i`, `q=2+d_j`, this forces exclusive excess at least

`R_pq(a,b)=a(b-p)_+ + b(a-q)_+`,

where `a=|A|`, `b=|B|`.

If two such rectangles share one block but their opposite blocks are disjoint, their charges add: on an overlap vertex the required neighbour sets are disjoint and

`(u+v-p)_+ >= (u-p)_+ + (v-p)_+`.

We use four instances:

`R_22=a(b-2)_+ + b(a-2)_+`,

`R_23=a(b-2)_+ + b(a-3)_+`,

`R_24=a(b-2)_+ + b(a-4)_+`,

`R_33=a(b-3)_+ + b(a-3)_+`.

Elementary threshold splitting gives

- `R_22>=a+b-4`, and if `a+b>=5`, `R_22>=a+b-3`;
- `R_23>=a+b-5`, and if `a+b>=6`, `R_23>=a+b-4`;
- `R_24>=a+b-6`, and if `a+b>=7`, `R_24>=a+b-5`;
- `R_33>=a+b-6`, and if `a+b>=7`, `R_33>=a+b-4`.

Also `R_22=0` implies `a,b<=2`; `R_23=0` implies `a<=3,b<=2`; `R_24=0` implies `a<=4,b<=2`; and `R_33=0` implies `a,b<=3`.

### 2.2 Common-nonneighbour clique
If `p,q` are nonadjacent vertices, then their common nonneighbour set

`M(p,q)=V\({p,q} union N(p) union N(q))`

is a clique: two nonadjacent vertices in `M` together with `p,q` form an independent 4-set.

### 2.3 Same-missing-anchor disjointness
If two nonadjacent pair connectors both miss the same anchor `ak`, they cannot share a nonneighbour in either incident exclusive block. Indeed a common nonneighbour `x` is also nonadjacent to `ak`, so `{p,q,ak,x}` would be independent. Thus their two rectangle supports are disjoint blockwise.

---

## 3. c=2 closure for all r>=12

Here `d=(0,0,0)` and both connectors are triple connectors. For a connector `z` of excess `k`, let `eps` indicate the edge between the two connectors. Then

`|N_X(z)|=r-3+k-eps`.

Let `P` be the positive-excess exclusive vertices and

`E_i=Xi\(N(z) union P)`.

Every vertex in each `E_i` is exact and has cross-X degree at most two. Moreover `E_1,E_2,E_3` have no independent transversal, else adding `z` gives an independent 4-set.

Use the following degree-2 transversal-cover lemma: a tripartite graph with nonempty parts, maximum degree at most two, and no independent transversal has either two parts of size at most two, or, after ordering sizes, pattern `(1,3,3)` or `(2,3,3)`. The proof is the standard nonneighbour-rectangle argument: for `x` in one part, its nonneighbour sets in the other two must be complete bipartite; maximum degree two bounds both by two.

If two `E`-parts have size at most two, connector degree counting gives

`r <=5+K<=11`,

contrary to `r>=12`. The `(1/2,3,3)` exceptions have total size at most eight, while direct counting gives

`sum |E_i| >=2r-9>=15`.

If some `E_i` is empty, clique cap forces a positive-excess nonneighbour `x` in that block. The other two exact-nonneighbour sets each have size at least `r-7>=5`; their transversal-cover condition forces enough cross degree on `x` that

`K>=r-4>=8`.

Thus `c=2` is impossible for every `r>=12`.

---

## 4. c=3 closure for every r>=13

Here `d=(0,0,1)`, so block sizes are `(r-2,r-2,r-3)`. The connector identity gives one triple connector `w`, one pair connector `u` missing `a1`, and one pair connector `v` missing `a2`.

Call a pair connector focused if it is complete to `X3`.

For a nonfocused pair connector of excess `k` and connector-degree `gamma`, its nonneighbour counts `a>=1` in the incident zero-deficit block and `b>=1` in `X3` satisfy

`a+b>=r-3-k+gamma`.

Its rectangle has `(2,3)` capacities, hence

`k+R_23(a,b)>=r-8+gamma`.

If both pair connectors are nonfocused, their charges are additive because their opposite zero-deficit blocks are distinct; for `r>=13` this costs at least ten. If both are focused, they are nonadjacent (otherwise `X3+a3+u+v` is an `r`-clique); their common nonneighbour sets in `X1,X2` form a huge complete rectangle and force `K>=2r-9`.

Thus exactly one is focused, say `u`. For the nonfocused `v`, every `X3` rectangle vertex already has neighbour `u`, so its effective charge becomes `R_22`. If `uv` is an edge,

`K>=r-6>=7`,

impossible by parity. If `uv` is a nonedge, the same gives `K>=r-7`; this closes `r>=14`. At `r=13`, `K<=6` forces the unique boundary

`k_v=6`, `gamma_v=0`, `(a,b)=(2,2)`.

Then all other vertices are exact, `v` has no `X2` neighbours, the two `X1` rectangle vertices use their two external slots on the two `X3` rectangle vertices, and the latter use their three slots on those two plus focused connector `u`. Hence all these rectangle vertices are nonadjacent to the triple connector `w`. For fixed rectangle vertex `x in X1` and any `y in X2`, the set `{v,w,x,y}` would be independent unless `wy` is an edge. Thus `w` must see all `r-2=11` vertices of `X2`, but exact `w` already sees three anchors and has only ten remaining degree slots. Contradiction.

Thus `c=3` is impossible for every `r>=13`.

---

## 5. c=4, deficit vector (0,0,2): closure for every r>=13

Now

`|X1|=|X2|=r-2`, `|X3|=r-4`.

There are two pair connectors missing `a1` and two missing `a2`; all four are incident to `a3`.

### 5.1 Focus cap
Call a connector focused if it is complete to `X3`.

If two focused connectors `p,q` were nonadjacent, their common nonneighbour set is a clique. They share `X3 union {a3}` (size `r-3`) as common neighbours, so

`|M(p,q)| >= (3r-3)-[(r+k_p)+(r+k_q)-(r-3)]`

`=2r-6-k_p-k_q >=2r-12>r-1`.

Impossible. Hence every pair of focused connectors is adjacent. Three focused connectors would then form a triangle and, with `X3 union {a3}`, an `r`-clique. Therefore at most two connectors are focused, so at least two are nonfocused.

### 5.2 Local nonfocus charge
For a nonfocused connector with excess `k` and connector-degree `gamma`, let `a>=1` be its nonneighbour count in the incident zero-deficit block and `b>=1` in `X3`. Then

`a+b>=r-4-k+gamma`,

and

`k+R_24(a,b)>=r-10+gamma`.

Rectangles of nonfocused connectors from the two different missing-anchor groups charge additively. If two same-group connectors are nonadjacent, their supports are disjoint by Lemma 2.3, so their charges also add.

### 5.3 Boundary r=16
Each nonfocused connector costs at least `6+gamma`. Since at least two are nonfocused, different-group or nonadjacent same-group pairs cost at least twelve. An adjacent nonfocused connector has cost at least seven by `gamma>=1`. Contradiction.

### 5.4 Boundary r=15
Different-group or nonadjacent same-group nonfocused pairs cost at least ten. Thus a possible pair would have to be adjacent and same-group, so `gamma>=1` for both. Then

`a+b>=12-k`.

If `k<=5`, then `a+b>=7` and the improved bound `R_24>=a+b-5` gives

`k+R_24>=7`,

impossible. Hence each connector would need `k=6`, impossible for two distinct connectors under total `K<=6`.

### 5.5 Boundary r=14
Different-group or nonadjacent same-group pairs already cost at least eight. Thus the two required nonfocused connectors are adjacent and same-group, and the other two connectors are focused.

For an adjacent nonfocused connector,

`a+b>=11-k`.

For `k=0,1,2,3,4`, the improved rectangle bound gives respectively at least `R_24=6,5,4,3,2`; `k=5,6` already consumes almost/all budget. For two connectors, the lower bound

`K >= k_1+k_2+max(R_1,R_2)`

is at most six only when `k_1=k_2=0` and `R_1=R_2=6`.

Equality forces `a=10,b=1` for each. To keep the union charge at six, the two rectangles must have the same unique `X3` vertex and the same ten-vertex zero-block side; otherwise that `X3` vertex sees more than ten cross neighbours or two distinct `X3` vertices each carry six excess. Thus the common `X3` vertex has all `4+6=10` external slots consumed by the rectangle and cannot meet a connector. But the other-group connectors are focused and hence adjacent to every `X3` vertex. Contradiction.

### 5.6 Boundary r=13
If there is a nonfocused connector in each missing-anchor group, additivity and the local lower bound give `K>=6`. Equality under `K<=6` forces each local charge to equal three. Since

`a+b>=9-k`,

and `R_24>=a+b-6` (with the stronger `a+b-5` bound once the sum is at least seven), equality is possible only at

`k=3`, `(a,b)=(4,2)`, `R_24=0`.

The two connector excesses already use all six units, so all exclusive vertices are exact. The two `X3` rectangle vertices of either connector use all four external slots on its four-vertex zero-block side and cannot meet a focused connector. The remaining connectors cannot be nonfocused (that would require positive rectangle charge with no budget), so they must be focused, contradiction.

Therefore the two required nonfocused connectors are the same-group pair, and the other-group pair is focused. Every `X3` vertex now already has two focused connector neighbours. Hence a nonfocused rectangle has effective capacities `(2,2)` instead of `(2,4)`.

If the same-group nonfocused pair is nonadjacent, its supports are disjoint and each strengthened local charge is at least five, so the sum is at least ten. If they are adjacent, `gamma>=1` and

`a+b>=10-k`.

If `k<=5`, then `a+b>=5` and `R_22>=a+b-3`, giving local charge at least seven. Hence each connector would require `k=6`, impossible for two connectors. Thus `r=13` is closed.

Therefore the `(0,0,2)` geometry is impossible for every `r>=13`.

---

## 6. c=4, deficit vector (0,1,1): closure for every r>=13

Now

`|X1|=r-2`, `|X2|=|X3|=r-3`.

There are two type-U connectors missing `a1`, one connector `v` missing `a2`, and one `w` missing `a3`.

### 6.1 Focus collision
A connector complete to `X2` or `X3` is focused on that block. No two connectors can focus on the same deficit-1 block `Xi`.

If focused connectors `p,q` are adjacent, `Xi union {ai,p,q}` is an `r`-clique. If they are nonadjacent, their common nonneighbour set is a clique, while their common neighbours include `Xi union {ai}` of size `r-2`; hence

`|M(p,q)| >=2r-5-k_p-k_q >=2r-11>r-1`.

Thus at most one connector focuses on each of `X2,X3`, so at least two connectors are nonfocused.

### 6.2 Local charges
A nonfocused type-U connector has incident capacities `(3,3)` and

`k+R_33>=r-10+gamma`.

A nonfocused connector `v` or `w` has incident capacities `(2,3)` and

`k+R_23>=r-8+gamma`.

Charges of nonfocused `v,w` are additive although they overlap in `X1`, because their opposite blocks are `X3` and `X2`. Likewise a nonfocused type-U rectangle charges additively with the appropriate `(0,1)` rectangle because their opposite blocks are distinct.

### 6.3 r>=17
Every nonfocused connector would already exceed total budget in the relevant local inequality, forcing all four to focus, contradicting the focus-collision lemma.

### 6.4 r=16
The `(0,1)` connectors `v,w` cannot be nonfocused because each would cost at least eight, so they focus on `X3,X2`, respectively. Both type-U connectors are therefore nonfocused. If either has positive connector-degree, its local cost is at least seven. Thus both have `gamma=0`, are nonadjacent, and their same-missing-anchor supports are disjoint. Their charges add to at least twelve. Contradiction.

### 6.5 r=15
Again `v,w` are forced to focus, so both type-U connectors are nonfocused. If they are nonadjacent, disjoint supports give cost at least ten. If adjacent, `gamma>=1` and

`a+b>=12-k`.

For `k<=5`, `a+b>=7` and `R_33>=a+b-4`, so local charge is at least eight. Hence each connector would need `k=6`; two such connectors violate `K<=6`.

### 6.6 r=14
Suppose a `(0,1)` connector, say `v`, is nonfocused. Its local bound is at least `6+gamma`, so `K<=6` forces `gamma=0`. Also

`a+b>=11-k`.

If `k<=5`, then `a+b>=6` and `R_23>=a+b-4`, giving local charge at least seven. Hence `k=6`. The entire budget is used, so `R_23=0`, and the only possibility with `a+b>=5` is `(a,b)=(3,2)`.

Thus all other vertices are exact, `v` has no neighbours in the third block `X2`, and its three `X1` rectangle vertices and two `X3` rectangle vertices are externally saturated by the rectangle. Also `v` is nonadjacent to every connector. Fix a rectangle vertex `x in X1`. For any other connector `z` and any `y in X2`, if `zy` were absent then `{v,z,x,y}` would be independent. Hence every other connector is complete to `X2`, contradicting the focus-collision lemma. Therefore both `(0,1)` connectors focus on `X3,X2`.

The two type-U connectors are then nonfocused. If nonadjacent, their disjoint charges sum to at least eight. If adjacent, `gamma>=1`; for `k<=4`, the sum bound is at least seven and the improved `R_33` inequality gives local cost at least seven. Thus each connector would need at least five excess units, so two connectors exceed total budget. Contradiction.

### 6.7 r=13
If both `(0,1)` connectors are nonfocused, their additive local charges total at least ten. If exactly one is nonfocused, say `v`, focus capacity leaves at least one type-U connector nonfocused; their rectangles have disjoint opposite blocks and add to at least `5+3=8`. Thus both `(0,1)` connectors focus, on `X3` and `X2`, and both type-U connectors are nonfocused.

If the type-U pair is nonadjacent, its supports are disjoint. The two local lower bounds sum to at least six. Equality under `K<=6` forces `gamma=0` and local charge three for each. Since

`a+b>=9-k`,

the only way to attain three is

`k=3`, `(a,b)=(3,3)`, `R_33=0`.

The two connector excesses use all six units, so every exclusive vertex is exact. But every rectangle vertex in `X2` or `X3` already has three cross-rectangle neighbours, exhausting its baseline capacity three, while the corresponding focused connector is complete to that block. Contradiction.

If the type-U pair is adjacent, every `X2` rectangle vertex already has the focused `w` neighbour and every `X3` rectangle vertex the focused `v` neighbour. Thus both rectangle capacities drop from three to two. With `gamma>=1`,

`a+b>=10-k`.

If `k<=5`, then `a+b>=5` and `R_22>=a+b-3`, giving local charge at least seven. Hence each type-U connector would require `k=6`, impossible for two distinct connectors.

Thus `r=13` is closed.

Therefore the `(0,1,1)` geometry is impossible for every `r>=13`.

---

## 7. Conclusion

All four anchor geometries are exhausted. Hence

`K_r(H)>=8`

for every `r>=13` under the stated residual-core contract. Together with the pre-existing `r=12` closure, this is a Level-3 completion of the Exact Three-Anchor Excess Conjecture.

The only remaining proof-engineering target is Level 4: replace the separate `r=12` citation by extending the same focus/rectangle argument through the last small equality layers.
