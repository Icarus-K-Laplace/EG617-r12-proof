# Global d=3 Allowance-One Sharp Capacity Theorem

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_COMMON_S_OWNER_CLIQUE_THEOREM.md`;
- `GLOBAL_D3_ALLOWANCE_ONE_COLLAPSE.md`;
- `GLOBAL_HEREDITARY_SUPPORT_PACKING_THEOREM.md`;
- common-S row closure;
- the inherited r=12 caps `D(14)=69`, `D(17)=81`;
- the legal residual contracts `alpha(H)<=3`, `omega(F)<=11`.

This theorem sharpens the low-allowance triple-support bridge from a qualitative multiplicity collapse to a six-owner capacity theorem. It is the d=3 analogue of the sharp d=2 transversal-capacity theorem.

## 1. Setup

Use the common-S notation with the current r=12 backend constants:

- shell size `h=13`;
- core size `n=35`;
- `alpha(H)<=3`;
- a family Y of N regular shell owners sharing one missing set `S` of size `d=3`;
- each owner y has a 3-point core support `D_y`;
- row allowance `a<=1`;
- `s=|S intersect X|<3`;
- core charge `w_v=kappa_v+e_F(v,S)`;
- total charge `W=sum_H w_v`.

Assume

> `W<=35`.                                                    (1)

The earlier collapse theorem applies because

`35 < 3(35-9)=78`.

Hence, whenever `N>=4`, there is a repeated support class D with multiplicity

> `m>=ceil(N/2)`,                                             (2)

and every repeated support is a zero-charge target K3:

> `w(D)=0`, `H[D]=K3`.                                       (3)

In particular every point of D has `kappa=0` and is target-anticomplete to S.

## 2. Common-S dense base

Let

`T=A\(S union Y)`.

By `GLOBAL_COMMON_S_OWNER_CLIQUE_THEOREM.md`,

- Y is a target clique;
- every Y--T pair is a target edge;
- p is target-adjacent to `Y union T`.

The 11-point base

`B={p} union Y union T`

therefore satisfies

`e(B)>=10+C(N,2)+N(10-N)`.                                  (4)

For N=10,9,8,7 this lower bound is respectively

`55,55,54,52`.                                               (5)

If D is a repeated zero-charge target K3 of multiplicity m, its m owners contribute exactly `3m` certified B--D edges, and `e_H(D)=3`.

Applying `D(14)=69` to `B union D` gives

> `e(B)+3m+3 <=69`.                                          (6)

Omitted B--D edges are nonnegative, so (6) is valid as a lower-bound packing inequality.

## 3. N>=9 is impossible

For N=10 or N=9, (5)--(6) give

`55+3m+3<=69`,

hence

> `m<=3`.                                                     (7)

But (2) gives

- N=10: `m>=5`;
- N=9: `m>=5`.

Contradiction.

The common-S owner-clique theorem already excludes N>=11. Therefore

> `N<=8`.                                                     (8)

## 4. The N=8 equality candidate is forced to 4+4

Assume N=8.

Equation (5)--(6) gives

`54+3m+3<=69`,

so

> `m<=4`.                                                     (9)

The collapse theorem gives a repeated class of multiplicity at least4.

There are at most three distinct support classes.

- One class would have multiplicity8, contradicting (9).
- Three classes can have at most one repeated class under the collapse theorem's charge hypothesis. Then the two other classes are singletons, so the repeated class has multiplicity6, again contradicting (9).
- Hence there are exactly two support classes, and both are repeated.

Since their multiplicities sum to8 and each is at most4, they are exactly

> `4+4`.                                                      (10)

Call the two supports D and E.

Both are zero-charge target K3s. Because they are distinct common-S supports, they are disjoint; common-S row closure gives

> `e_H(D,E)=0`.                                               (11)

## 5. N=8 is killed by D17

For N=8 the leftover shell set T has size2. The base bound is

`e(B)>=54`.

The induced 17-set

`B union D union E`

contains at least

- 54 base edges;
- `3*4=12` owner edges into D;
- `3*4=12` owner edges into E;
- 3 internal edges in D;
- 3 internal edges in E;
- zero required D--E edges by (11).

Thus

`e(B union D union E)>=54+12+12+3+3=84`.                    (12)

But the inherited cap is

`D(17)=81`.

Contradiction.

Therefore

> `N!=8`.                                                     (13)

## 6. The N=7 equality candidate is forced to 4+3

Assume N=7.

From (5)--(6),

`52+3m+3<=69`,

so

> `m<=4`.                                                     (14)

The collapse theorem gives a repeated class of multiplicity at least4.

As above:

- one support class would have multiplicity7, impossible;
- three classes would force one repeated class of multiplicity5 and two singleton classes, impossible by (14).

Hence there are exactly two support classes D,E, with multiplicities

> `4+3`.                                                      (15)

Both D and E are repeated zero-charge target K3s, they are disjoint, and

> `e_H(D,E)=0`.                                               (16)

## 7. Row-closure lower bound in the 4+3 terminal

Put

`R=H\(D union E)`.

Then `|R|=29`.

Because D is a zero-charge K3, every point of D has core excess0, hence core degree exactly12. It has two neighbours inside D and no neighbours in E. Therefore each point of D has exactly10 target neighbours in R, so

> `e_H(D,R)=30`.                                              (17)

Similarly

> `e_H(E,R)=30`.                                              (18)

For every `v in R`, common-S row closure against D and E gives

`e_H(v,D)<=w_v`,

`e_H(v,E)<=w_v`.                                             (19)

Now define

`L={v in R:w_v<=1}`.

### Claim: L is a target clique.

Take distinct `u,v in L`. Suppose `uv` were a target nonedge.

By (19), each of u and v has at most one target neighbour in D. Hence their combined D-neighbourhood has size at most2, so choose

`d in D`

target-nonadjacent to both u and v.

The same argument gives

`e in E`

target-nonadjacent to both u and v.

By (16), `de` is also a target nonedge. Thus

`{u,v,d,e}`

is an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore L is a target clique. Since `omega(F)<=11`,

> `|L|<=11`.                                                  (20)

Hence at least

`29-11=18`

vertices of R have charge at least2. Consequently

> `W>=sum_(v in R) w_v>=18*2=36`.                            (21)

This contradicts the standing hypothesis `W<=35`.

Therefore

> `N!=7`.                                                     (22)

## 8. Sharp capacity conclusion

Combining Sections3,5,7 and the owner-clique bound gives

> **Global d=3 allowance-one sharp capacity theorem.**
>
> In the r=12 backend, any common-S triple-support family satisfying
>
> - `a<=1`;
> - `s<3`;
> - `W<=35`;
> - the retained residual/core/hereditary contracts
>
> has
>
> **`N<=6`.**                                                 (23)

No computer enumeration is used.

## 9. Structural interpretation

The proof has exactly the requested architecture:

1. low allowance forces distinct supports into a sparse block system;
2. repetition plus tau-maximality forces repeated supports to become zero-charge K3s;
3. hereditary packing kills large owner multiplicity;
4. the only numerical equality candidates are `4+4` and `4+3`;
5. D17 kills `4+4`;
6. row closure plus low-charge clique rigidity kills `4+3`.

Thus the contradiction is

> inequality -> repeated-K3 equality geometry -> equality-geometry contradiction,

not a list of E-layer cases.

## 10. Relation to the global bridge

This theorem gives a complete low-support bridge for one important regime:

> common-S, d=3, allowance at most1, low total charge.

Any unresolved backend family that can be extracted into seven such owners is immediately impossible.

Crucially, the theorem does **not** identify the source-reported E334 `eleven-view system` with one common-S family. That translation remains a separate bridge obligation; if eleven views use several missing sets, they must first be partitioned/extracted into common-S owner subfamilies.

## 11. Generalization

The proof separates into a parameterized part and r=12 equality caps.

Parameterized ingredients:

- common-S owner clique;
- low-allowance repetition collapse;
- row-closure low-charge clique argument.

The numerical r=12 inputs are only

- the 14- and 17-point hereditary caps;
- the residual clique cap11;
- the 35-point core size through the final `29=35-6` count.

For higher r, the same proof template gives a capacity theorem once the corresponding hereditary caps and core size are substituted.