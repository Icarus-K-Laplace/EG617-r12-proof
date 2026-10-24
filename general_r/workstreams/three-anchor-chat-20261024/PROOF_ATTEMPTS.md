# Proof attempts and proved lemmas

## 1. Exact anchor partition (reverified)

Every non-anchor vertex meets at least one anchor, else together with the three anchors it forms an independent 4-set. If `c` vertices meet at least two anchors and `t` meet all three, anchor-incidence counting gives

`3r=(3r-4)+c+t`, hence `c+t=4`.

For each `i`, `Xi union {ai}` is a clique: two nonadjacent vertices of `Xi` together with the other two anchors would form an independent 4-set. Hence `|Xi|<=r-2`. Writing `d_i=(r-2)-|Xi|`,

`d_1+d_2+d_3=c-2`.

Thus, up to permutation, the only deficit patterns are

`(0,0,0)`, `(0,0,1)`, `(0,0,2)`, `(0,1,1)`.

If `q_i` denotes the number of connectors missing anchor `ai`, then `ai` has exactly `2+d_i` connector neighbours, so

`q_i=c-(2+d_i)=d_j+d_k`.

This fixes the connector incidence multiset in every pattern.

---

## 2. Parity lemma

`K_r(H)=2e(H)-r(3r-1)` is even. The first term is even; the second is even because either `r` is even or `3r-1` is even. Therefore throughout the contradiction branch

`K_r<=7  ==>  K_r<=6`.

This is a global structural gain, not a case assumption.

---

## 3. Tripartite degree-2 transversal-cover lemma

Let `G` be tripartite with nonempty parts `A,B,C`, maximum degree at most 2, and suppose every transversal spans an edge. Order `a=|A|<=b=|B|<=c=|C|`. Then either `b<=2`, or `(a,b,c)` is `(1,3,3)` or `(2,3,3)`.

Proof. If `b>=4`, choose `x in A`. The nonneighbour sets `B0=B\N(x)` and `C0=C\N(x)` are nonempty and must induce a complete bipartite graph, else an independent transversal exists. Maximum degree 2 gives `|B0|,|C0|<=2`, so `x` has at least two neighbours in each of `B,C`, contradiction. Thus `b<=3`. If `b=3<c`, the same argument forces at least two neighbours of `x` in `C` and at least one in `B`, contradiction. Hence `c=3`. If `a=3`, every `A`-vertex has degree exactly two, one into each other part. The six used degree slots on `B union C` leave room for at most three `B-C` edges, but the two-by-two nonneighbour sets of any fixed `x in A` require a `K_{2,2}`, contradiction. Thus `a<=2`.

Equality add-on: if `(a,b)=(2,2)` and `c>4`, then `A-B` is complete; otherwise a missing pair would require all of `C` to lie in the union of two degree-2 neighbourhoods, of size at most four. The `K_{2,2}` then saturates all cross-degree capacity of `A union B`.

---

## 4. Full closure of the c=2 geometry

Here `d=(0,0,0)`, so `|Xi|=r-2` and the two connectors `u,v` are both triple connectors.

For a connector `z` of excess `k`, let `eps=1` if `uv` is an edge and `0` otherwise. Then

`|N_X(z)|=r-3+k-eps`.

Let `P` be positive-excess exclusive vertices and define

`E_i(z)=Xi \ (N(z) union P)`.

Every vertex in `E_i` is exact degree `r`, hence has cross-X degree at most two. An independent transversal of `E_1,E_2,E_3` together with `z` would be an independent 4-set, so the degree-2 transversal-cover lemma applies.

If all three `E_i` are nonempty and two have size at most two, then

`2(r-2)-(p_i+p_j)-4 <= r-3+k-eps`,

hence

`r <= 5+(p_i+p_j)+k-eps <= 5+K <= 11`,

using parity `K<=6`. This contradicts `r>=12`. The exceptional `(1/2,3,3)` outputs have total size at most eight, while

`sum |E_i| >= 2r-3-k+eps-|P| >= 2r-9+eps >=15`,

again impossible.

If some `E_i` is empty, say `E_1`, clique cap forces `z` to miss some positive-excess `x in X1`. The other two exact-nonneighbour sets each have size at least `r-1-|P|-k+eps >= r-7+eps >=5`. Their transversal-cover requirement forces the cross degree of `x` to be at least that size, giving

`e_x >= r-3-|P|-k+eps`.

Adding the at least `|P|-1` excess units carried by the other positive vertices yields

`K_X >= r-4-k+eps`, hence `K>=r-4+eps>=8`.

Thus the entire `c=2` branch is impossible for all `r>=12`.

---

## 5. Pair-connector rectangle lemma

Suppose pair connector `z` misses anchor `ak` and is incident to anchors `ai,aj`. Let

`A = Xi \ N(z)`, `B = Xj \ N(z)`.

Then `A-B` is complete in `H`: otherwise for a missing edge `xy` with `x in A,y in B`, the four vertices `{z,ak,x,y}` are pairwise nonadjacent.

If exact baseline external capacities in `Xi,Xj` are `b_i=2+d_i`, `b_j=2+d_j`, this gives the robust charge

`K_X >= |A| (|B|-b_i)_+ + |B| (|A|-b_j)_+`,

before using any additional connector neighbours. Two rectangles sharing a block but using disjoint opposite blocks can be charged additively: on an overlap vertex, the required neighbour sets are disjoint and

`(p+q-b)_+ >= (p-b)_+ + (q-b)_+`.

Two elementary integer inequalities used below are, for positive integers `a,b`,

`a(b-2)_+ + b(a-3)_+ >= a+b-5`,

`a(b-2)_+ + b(a-2)_+ >= a+b-4`.

For `a+b>=5`, the second improves to

`a(b-2)_+ + b(a-2)_+ >= a+b-3`.

These follow immediately by splitting at `a<=2/3` and `b<=2`.

---

## 6. Full symbolic closure of c=3 for r>=13

Here, after relabeling,

`d=(0,0,1)`, `(|X1|,|X2|,|X3|)=(r-2,r-2,r-3)`.

The connector-incidence identity gives exactly one triple connector `w`, one pair connector `u` missing `a1`, and one pair connector `v` missing `a2`.

Call a pair connector **focused** if it is complete to `X3`.

### 6.1 Two nonfocused pair connectors are impossible
For a nonfocused pair connector `z` of excess `k` and connector-degree `gamma`, let `a>=1` be its number of nonneighbours in its incident zero-deficit block (`X2` for `u`, `X1` for `v`) and `b>=1` its number of nonneighbours in `X3`.

Since all X-neighbours of `z` number `r+k-2-gamma`, even assigning all possible neighbours to the third block gives

`a+b >= r-3-k+gamma`.

The rectangle lemma and the first elementary inequality yield a local charge

`k + a(b-2)_+ + b(a-3)_+ >= r-8+gamma`.

For `u` and `v`, the zero-deficit sides lie in disjoint blocks `X2` and `X1`; their rectangle charges are additive even where their `X3` sides overlap. Hence if both are nonfocused,

`K >= 2(r-8) >=10`

for `r>=13`, contradiction.

### 6.2 Two focused pair connectors are impossible
If both `u,v` are complete to `X3`, then `uv` is a nonedge, because otherwise `X3 union {a3,u,v}` is an `r`-clique.

Let `A subset X1` and `B subset X2` be the common nonneighbours of `u,v`. They form a complete bipartite graph, else `{u,v,x,y}` is independent. A focused pair connector `z` has only

`1+k_z-gamma_z`

neighbours in `X1 union X2`. Therefore

`|A|+|B| >= 2r-6-k_u-k_v+gamma_u+gamma_v`.

Under `K<=6`, both sets are nonempty. Since both blocks have baseline external capacity two, the complete rectangle gives, using `|A|+|B|>=5`,

`K >= k_u+k_v + |A|(|B|-2)_+ + |B|(|A|-2)_+`

`>= k_u+k_v + |A|+|B|-3`

`>= 2r-9 >=17`,

for `r>=13`, contradiction.

Thus exactly one pair connector is focused.

### 6.3 Mixed case: exactly one focused
Assume `u` is focused and `v` is nonfocused. Let `A subset X1`, `B subset X3` be the nonneighbour rectangle of `v`, with sizes `a,b>=1`, and let `k=k_v`, `gamma=deg_C(v)`.

Because `u` is complete to `X3`, every vertex of `B` already has the connector neighbour `u`. Hence the rectangle charge strengthens to

`F(a,b)=a(b-2)_+ + b(a-2)_+`.

Also

`a+b >= r-3-k+gamma`.

If `uv` is an edge, then `gamma>=1`, so

`K >= k+F >= k+(a+b-4) >= r-7+gamma >= r-6 >=7`.

Since `K` is even, this contradicts `K<=6` for every `r>=13`.

Now suppose `uv` is a nonedge. If `r>=14`, the same estimate with `gamma>=0` gives

`K >= r-7 >=7`,

again impossible by parity. It remains only `r=13`.

At `r=13`, a value `K<=6` forces equality in every preceding inequality. The only positive-integer solution is

`k=6`, `gamma=0`, `(a,b)=(2,2)`, `K=6`.

Indeed if `a+b>=5` then the stronger bound `F>=a+b-3` already gives at least seven; while `a+b>=10-k`, so `a+b<=4` forces `k=6`, and `F=0` with sum four forces `(2,2)`.

Thus `v` has no neighbours in `X2`, is nonadjacent to both other connectors, and consumes all six excess units. Every other vertex is exact. Each `x in A` has exactly its two neighbours in `B` outside `X1 union {a1}`, so `xw` is a nonedge. Each `y in B` has exactly its two neighbours in `A` plus `u`, so `yw` is a nonedge. Since also `vw` is a nonedge, for any fixed `x in A` and any `z in X2`, the four vertices `{v,w,x,z}` would be independent unless `wz` is an edge. Hence `w` must be adjacent to all `|X2|=11` vertices of `X2`. But `w` is exact degree 13 and already adjacent to the three anchors, leaving only ten remaining neighbour slots. Contradiction.

Therefore the entire `c=3` geometry is impossible for every `r>=13`.
