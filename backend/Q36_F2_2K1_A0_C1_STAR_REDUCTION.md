# q36 f=2, 2K1 far, a_F=0 — c=1 star reduction

Status: `PROVED REDUCTION` under the exact d2 formula, inherited D14, and `alpha(F)<=4`.

## 1. Setup

Let C={y}. Its d2 support is a two-point set D. Let X be the ten decorated shell vertices and put

`nu=e_M(X)`, `k=e_F(D,X)`.

The shell ledger gives

`G=13-nu`.

Since all ten X-vertices are decorated, `G>=10`, hence

`nu<=3`.

Also nu>0, because if nu=0 then `{p} union C union X` is a target K12, contradicting `omega(F)<=11`.

Thus `nu in {1,2,3}`.

The d2 defect is

`kappa(D)+m(D)<=1`,

where `m(D)=1-e_H(D)`.

The 14-point set `{p} union C union X union D` gives

`66-nu + (1-m(D)) + 2 + k <=69`,

so

> `k<=nu+m(D)`.                                             (1)

## 2. D must be a target K2

If `m(D)=1`, the two support vertices are target-nonadjacent. The far pair F={a,b} is also target-nonadjacent and is target-anticomplete to X and D.

To avoid an independent5-set `{a,b} union D union {x}`, every x in X would have to be adjacent to at least one D-endpoint. Hence `k>=10`.

But (1) gives `k<=nu+1<=4`, contradiction.

Therefore

> `H[D]=K2`, `m(D)=0`, and `k<=nu`.                         (2)

## 3. Every D-endpoint must cover M[X]

Fix d in D. If an M[X]-edge x1x2 had both endpoints target-nonadjacent to d, then `{a,b,d,x1,x2}` would be an independent5-set.

Hence `N_X(d)` is a vertex cover of M[X]. Let tau be the vertex-cover number of M[X]. Then both D-endpoints have at least tau neighbours in X, so

`k>=2tau`.                                                  (3)

Since nu>0, tau>=1. Combining (2)--(3),

`2tau<=nu<=3`.

Thus nu=1 is impossible, and for nu=2 or3 necessarily

> `tau=1`.                                                   (4)

Therefore all missing edges of M[X] share one common vertex h.

## 4. Exact remaining terminals

### nu=2

`M[X]=K1,2 disjoint_union 7K1`.

Equation (2)--(3) force `k=2`. Each D-endpoint has exactly one X-neighbour, and because that one-point neighbourhood must cover both missing edges, both endpoints are target-adjacent exactly to the star centre h.

Here `G=11`; the two endpoints of D have total inserted decoration determined by their one owner and their X-incidence, and the q35/q36 repivot saturates the available D14 decoration budget.

### nu=3

`M[X]=K1,3 disjoint_union 6K1`.

We have `2<=k<=3`. Both D-endpoints are target-adjacent to the star centre h; there is at most one additional D--X target edge outside h.

Here `G=10`.

## 5. Conclusion

The c=1 branch is reduced to exactly two missing-star families:

- `nu=2`: `K1,2 + 7K1`, with both support endpoints adjacent only to the centre;
- `nu=3`: `K1,3 + 6K1`, with both support endpoints adjacent to the centre and at most one additional D--X edge.

This is a reduction, not yet a closure.