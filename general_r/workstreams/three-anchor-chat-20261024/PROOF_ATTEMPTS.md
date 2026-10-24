# Proof attempts and proved lemmas

## 1. Exact anchor partition (reverified)

Every non-anchor vertex meets at least one anchor, else together with the three anchors it forms an independent 4-set. If `c` vertices meet at least two anchors and `t` meet all three, then counting anchor incidences gives

`3r = (3r-4) + c + t`, hence `c+t=4`.

For each `i`, `Xi union {ai}` is a clique: if two vertices of `Xi` were nonadjacent, they together with the other two anchors would form an independent 4-set. Hence `|Xi|<=r-2`. Writing `d_i=(r-2)-|Xi|`,

`d_1+d_2+d_3=c-2`.

This gives exactly `(0,0,0)`, `(0,0,1)`, `(0,0,2)`, `(0,1,1)` up to permutation.

If `q_i` denotes connectors missing anchor `ai`, then `ai` has `2+d_i` connector neighbours, so

`q_i=c-(2+d_i)=d_j+d_k`.

This fixes the connector incidence multiset in every pattern.

---

## 2. Tripartite degree-2 transversal-cover lemma

Let `G` be a tripartite graph with nonempty parts `A,B,C`, maximum degree at most 2, and suppose every transversal `(a,b,c)` spans at least one edge. Order `a=|A|<=b=|B|<=c=|C|`.

Then either

1. `b<=2`; or
2. `(a,b,c)` is `(1,3,3)` or `(2,3,3)`.

### Proof
If `b>=4`, take `x in A`. Since `deg(x)<=2`, the sets `B0=B\N(x)` and `C0=C\N(x)` are nonempty. Every edge between a missing pair must be present: otherwise `x,b,c` is an independent transversal. Hence `B0-C0` is complete bipartite. Since every vertex has degree at most 2, `|B0|,|C0|<=2`. Thus `x` must have at least `b-2>=2` neighbours in `B` and at least `c-2>=2` in `C`, contradicting `deg(x)<=2`. Therefore `b<=3`.

Assume `b=3`. If `c>=4`, the same argument shows `C0` is nonempty and has size at most 2, hence `x` has at least `c-2>=2` neighbours in `C`. Since `B0` is also nonempty, the completeness of `B0-C0` forces `|B0|<=2`, so `x` also has at least one neighbour in `B`. Thus `deg(x)>=3`, contradiction. Hence `c=3`.

If now `a=3`, every vertex of `A` has at least one neighbour in each of `B,C`, so every `A`-vertex has degree exactly 2. Therefore there are six `A-(B union C)` incidences. The total degree capacity of `B union C` is 12, leaving at most six degree slots, i.e. at most three `B-C` edges. But for any fixed `x in A`, its two-by-two nonneighbour sets in `B,C` must span a complete `K_{2,2}`, requiring four `B-C` edges. Contradiction. Thus `a<=2`.

### Equality add-on
If `(a,b)=(2,2)` and `c>4`, then `A-B` must be complete. Otherwise a missing pair `ab` would require every `c in C` to be adjacent to `a` or `b`, but `|N_C(a) union N_C(b)|<=4`. Hence for `c>4`, the `K_{2,2}` is complete and saturates all degree-2 capacity of `A union B`, so there are no edges from `A union B` to `C`.

---

## 3. Full closure of the `c=2` pattern

Assume `c=2`. Then both connectors `u,v` meet all three anchors and every `Xi` has size `m=r-2`.

Let `P` be the exclusive vertices with positive excess; write `p=|P|`, `K_X=sum_{x in X1 union X2 union X3}(d(x)-r)`. Then `p<=K_X`. Let connector `z` have excess `k`, and let `eps` be 1 if `uv` is an edge and 0 otherwise. Since `z` already sees the three anchors,

`|N_X(z)|=r-3+k-eps`.

For each block define

`E_i(z)=Xi \ (N(z) union P)`.

These are exact-degree vertices nonadjacent to `z`. Any `x in E_i(z)` has total external degree exactly 2, hence cross-X degree at most 2. Moreover `H[E_1,E_2,E_3]` has no independent transversal, else together with `z` it gives an independent 4-set.

### Case 1: all three `E_i(z)` are nonempty
Apply the tripartite lemma.

If two parts have size at most 2, say `E_i,E_j`, then

`|N_X(z) cap (Xi union Xj)| >= 2(r-2) - (p_i+p_j) - 4`.

Since the left side is at most `r-3+k-eps`,

`r <= 5 + (p_i+p_j) + k - eps <= 5 + K_X + k <= 12`.

Thus this subcase is impossible for `r>=13`.

The only other lemma outcomes have all three exact-nonneighbour parts of size at most 3, and total size at most 8. But the total number of X-nonneighbours of `z` is

`3(r-2) - (r-3+k-eps) = 2r-3-k+eps`.

At most `p` of them are positive-excess vertices, hence

`sum_i |E_i(z)| >= 2r-3-k+eps-p >= 2r-10+eps`,

which already exceeds 8 for `r>=10`. So this is impossible.

Therefore for every `r>=13`, Case 1 is impossible.

For `r=12`, the only escape from the first inequality is full equality: `eps=0`, `K=7`, both connectors have zero excess, all seven positive-excess exclusive vertices have excess exactly one, and for each connector the exact-nonneighbour sizes are `(2,2,10)`. By the equality add-on above, the two size-2 parts span a complete `K_{2,2}` and those four vertices have no cross edges to the size-10 part. Every positive-excess vertex is nonadjacent to both connectors and has cross-X degree exactly 3. Pick a positive vertex `p` in one of the two small-block unions. For the opposite size-2 exact set `B` and the size-10 exact set `C`, vertices of `B` have their degree-2 cross capacity saturated by the `K_{2,2}`, hence are nonadjacent to both `p` and `C`. Therefore every `c in C` must be adjacent to `p` (else `z,p,b,c` is independent for any `b in B`). This gives `p` at least 10 cross neighbours, contradicting cross degree 3. Thus the `r=12` equality escape is impossible too.

### Case 2: some `E_i(z)` is empty
Suppose `E_1(z)=empty`. Because `z` is adjacent to anchor `a1`, clique cap `omega(H)<=r-1` forces `z` to miss at least one vertex of `X1`, so choose `x in X1\N(z)`. Since `E_1` is empty, `x in P`; let its excess be `e_x>=1`.

Let `p_i=|P cap Xi|`. Since all nonneighbours of `z` in `X1` lie in `P1`,

`|N(z) cap X1| >= r-2-p_1`.

Hence

`|N(z) cap (X2 union X3)| <= p_1+k-eps-1`.

For `j=2,3`, this gives

`|E_j(z)| >= r-1-p-k+eps`,

where `p=p_1+p_2+p_3`. Since `p+k<=K_X+k<=K<=7`, both exact sets have size at least `r-8+eps`, hence at least 4 for `r>=12`.

Now consider triples `x,y2,y3` with `yj in E_j(z)`. Let `B0,C0` be the vertices in `E_2,E_3` nonadjacent to `x`. If both are nonempty they must be complete bipartite, else `z,x,y2,y3` is independent. Exact vertices have cross-X degree at most 2, so `|B0|,|C0|<=2`. Since both exact sets have size at least 4, the cross-X degree of `x` is therefore at least `min(|E_2|,|E_3|)`, hence at least `r-1-p-k+eps`.

But `x` has total external degree `2+e_x`, so

`e_x >= r-3-p-k+eps`.

Among the `p` positive exclusive vertices, all vertices other than `x` contribute at least one excess, so

`K_X >= e_x + (p-1) >= r-4-k+eps`.

Therefore

`K >= K_X+k >= r-4+eps >= 8`

for every `r>=12`, contradiction to `K<=7`.

This closes Case 2 and hence the entire `c=2` symbolic family.
