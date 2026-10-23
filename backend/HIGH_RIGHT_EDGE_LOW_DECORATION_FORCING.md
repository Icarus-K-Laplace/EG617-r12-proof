# High-backend right edge — low-decoration forcing at q36--q38

Status: `PROVED` under the standard legal `R(4,49)` backend contract, the all-pivot 35-core minimum-degree12 theorem, and lexicographic maximality where explicitly invoked.

This continues `HIGH_RIGHT_EDGE_ATOMIC_DEFECT_THEOREM.md`, `HIGH_LAYER_V3_JOINT_CANONICAL.md`, and the closed `K4,9` plateau assets. It does not close an entire edge layer.

## 1. Regular-shell cluster lemma

Fix a degree-13 pivot `p` with 13-shell `A`, missing graph `M`, and decoration `g_x=d_F(x)-13`.

Let `R={x in A:g_x=0}` be the regular shell vertices.

For two regular vertices `u,v` with `uv in M`, the canonical zero-gap relation gives

`N_M(u) union N_M(v)=A`.

Hence target adjacency restricted to `R` is transitive. Indeed, if `uv` and `vw` are target edges but `uw in M`, then `v` belongs to neither missing neighbourhood, contradicting the displayed union. Therefore

> `F[R]` is a disjoint union of target cliques `C_1,...,C_k`, with `k<=4` because `alpha(F)<=4`.

Equivalently `M[R]` is complete multipartite.

Now let `x` be decorated. Its target-neighbours in `R` lie in at most one clique `C_i`; otherwise two such neighbours from different cliques form a regular missing edge whose zero-gap union omits x.

If x is target-adjacent to a proper nonempty subset `U` of one regular clique C, choose regular `v in C\U`. The nonadjacent regular/decorated codegree bound from `HIGH_LAYER_V3_JOINT_CANONICAL.md` gives

`|N_F(v) intersect N_F(x)| <= 1+g_x`.

But `p union U` consists of common target neighbours, so

> `|U|<=g_x`.                                             (PA)

Thus a decorated vertex either attaches completely to one regular clique or has at most `g_x` regular target neighbours.

## 2. q36 with G=0

All13 shell vertices are regular. Let the target-clique sizes be `n_1,...,n_k`, `k<=4`, sum13.

Since `q=e(M)=36`,

`sum_(i<j)n_i n_j=36`, equivalently `sum n_i^2=97`.

The positive integer partitions of13 into at most4 parts satisfying this equation have the unique solution

`9+4`.

Hence `M=K_(4,9)`. The already-proved full `K4,9` plateau closure eliminates this state.

Therefore q36 cannot have G=0.

## 3. q36 with G=1

There is one decorated vertex x with `g_x=1`, and 12 regular vertices. Let `a` be its number of regular target neighbours and let `c` be the number of missing edges among the regular vertices. Since `e(M)=35`,

`c+12-a=35`, so `c-a=23`.

The only regular clique partitions with `23<=c<=32` are

| partition | c | required a=c-23 |
|---|---:|---:|
| 9+3 |27|4|
| 9+2+1 |29|6|
| 9+1+1+1 |30|7|
| 8+4 |32|9|

In the first three rows the required attachment is a proper subset larger than `g_x=1`, contradicting (PA). In the last row `a=9` exceeds every clique size.

Thus q36 cannot have G=1.

## 4. q36 with G=2

### 4.1 One decorated vertex of weight2

Again there are12 regular vertices. Now `e(M)=34`, so

`c-a=22`.

The only arithmetic candidates are

| partition | c | required a |
|---|---:|---:|
|9+3|27|5|
|9+2+1|29|7|
|9+1+1+1|30|8|
|8+4|32|10|

None is a complete-clique attachment, and all proper attachment sizes exceed `g_x=2`. Impossible by (PA).

### 4.2 Two decorated vertices of weight1

There are11 regular vertices. Let their target attachment sizes be a,b and let `mu` be1 if the two decorated vertices form a missing edge, otherwise0. The equation `e(M)=34` is

`a+b-mu=c-12`.

For each decorated vertex, (PA) says its attachment is 0 or1 unless it is complete to a regular clique. The finite partition check has a unique solution:

- regular partition `8+1+1+1`;
- `mu=1`;
- `a=b=8`.

Thus both decorated vertices are complete to the K8, are target-nonadjacent to each other, and are target-nonadjacent to each of the three singleton regular cliques.

The two decorated vertices together with the three singleton regular vertices form an independent5-set in F, contradicting `alpha(F)<=4`.

Hence

> `q=36 => G>=3`.                                         (36)

## 5. q37 with G=0 or1

### G=0

All13 vertices are regular and `e(M)=37`. No positive partition of13 into at most4 parts has cross-pair count37. Hence G=0 is impossible.

### G=1

One vertex x has `g_x=1`, 12 vertices are regular, and `e(M)=36`. Thus

`c-a=24`.

After (PA), exactly two arithmetic possibilities survive:

1. regular partition `9+3`, with x complete to the K3;
2. regular partition `8+4`, with x complete to the K8.

Both give `M=K_(4,9)`.

In case1 the decoration lies on the four-side, already eliminated by the full `K4,9` plateau closure.

In case2 the decoration lies on the nine-side. Let X be the regular four-side and Y the nine-side, containing x and eight regular vertices. For each regular `y in Y`,

- `d_M(y)=4`;
- its common missing set is X;
- `rho=1`, because the unique decoration x lies in the retained Y-side;
- at q37 the atomic-defect budget has total slack1.

Therefore `rho=1` exhausts the budget: every support `D_y` is a pure K4 of core-degree12 vertices, X is target-anticomplete to D_y, and the repivot remains at q37.

Lexicographic maximality forces every inserted support vertex to be globally regular: the old decorated vertex x is retained, while X is entirely regular, so any decorated inserted vertex would strictly increase tau.

Two Y-vertices cannot share a support, since a shared support vertex would have internal core degree12 plus at least two shell neighbours, contradicting global regularity. The common-S theorem with zero remaining allowance makes the eight supports pairwise disjoint and target-anticomplete.

Choosing one vertex from each gives an independent8-set in the 35-core, contradicting `alpha(H)<=3`.

Hence

> `q=37 => G>=2`.                                         (37)

## 6. q38 with G=0 or1

For G=0, no at-most-four-part partition of13 has cross count38.

For G=1, one weight1 decorated vertex and12 regular vertices give

`c-a=25`.

The only partitions with feasible cross count require attachment sizes

- `9+3`: a=2;
- `9+2+1`: a=4;
- `9+1+1+1`: a=5;
- `8+4`: a=7.

None is a complete-clique attachment and all exceed the partial bound `a<=1`. Therefore

> `q=38 => G>=2`.                                         (38)

## 7. Classification of q38, G=2

The same partition arithmetic plus (PA) gives an exact shell classification.

### One decorated vertex with g=2

The only possibilities are

- regular partition `9+3`, decorated vertex complete to K3;
- regular partition `8+4`, decorated vertex complete to K8.

### Two decorated vertices with g=1 each

Up to exchange the only possibilities are

- regular partition `9+2`, the decorated vertices target-adjacent and both complete to K2;
- regular partition `8+3`, the decorated vertices target-nonadjacent, one complete to K8 and the other to K3;
- regular partition `7+4`, the decorated vertices target-adjacent and both complete to K7.

Every listed shell is exactly `K_(4,9)` in the missing graph. Thus

> every q38 ceiling shell with G=2 is a K4,9 shell.          (K49-2)

The already-proved K4,9 closure eliminates all placements with all decoration on the four-side.

If all decoration lies on the nine-side, that placement is also impossible: every regular nine-side vertex has d=4 and `rho=2`, which exhausts the q38 atomic-defect budget. Hence its support is a pure K4 of core-degree12 vertices and gives a q38 plateau. Lexicographic maximality makes the support globally regular. Distinct regular nine-side vertices cannot share a support, and zero remaining common-S allowance makes distinct supports disjoint and target-anticomplete. There are at least seven regular nine-side vertices, yielding an independent set of size at least7 in H, contradiction.

Therefore the only q38,G=2 placement not eliminated by the present theorem is

> the cross-side K4,9 state with one unit of decoration on each side.

## 8. New right-edge interface

At a lexicographically maximal top-channel pivot:

- q36 requires `G>=3`;
- q37 requires `G>=2`;
- q38 requires `G>=2`;
- if q38 has `G=2`, the only remaining placement is the cross-side decorated K4,9 shell.

This theorem does not close E338--E340. Its purpose is to remove the entire low-decoration sector except one explicit q38 cross-side topology.