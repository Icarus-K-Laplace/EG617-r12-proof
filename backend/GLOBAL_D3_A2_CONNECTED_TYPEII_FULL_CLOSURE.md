# Global d=3 A2 Connected Type-II Full Closure

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D3_A2_CONNECTED_SIGNATURE_CODE_REDUCTION.md`;
- `GLOBAL_D3_A2_TWO_COMPONENT_FULL_CLOSURE.md`;
- `GLOBAL_FULLY_DECORATED_TO_ONESPOKE_BRIDGE.md`;
- low-charge intersecting / signature-star capacity;
- common-S row closure;
- `alpha(H)<=3`, `omega(H)<=11`.

Purpose: exclude the entire connected Type-II signature-code regime without enumerating owner-weight cells.

## 1. Type-II weighted setup

Type II has exactly one singleton signature group, say code `{1}`, and the opposite doubleton support code `{2,3}`. Connectedness requires at least one connector code `{1,2}` or `{1,3}`.

Let

- `A` be total owner multiplicity on singleton-code `{1}` supports;
- `b=b_23` be multiplicity of the opposite support D_23;
- `c=b_12+b_13` be total connector multiplicity.

Then

`A+b+c=9`.                                                   (T1)

The signature-star at 1 is pairwise intersecting, so

`A+c<=6`.                                                     (T2)

Hence

> `b>=3`.                                                     (T3)

The doubleton-code subfamily is pairwise intersecting and has owner capacity at most6, so

`b+c<=6`.

Therefore

> `A>=3`.                                                     (T4)

Any singleton-code support class is disjoint from D_23. Since all disjoint-pair owner weights are at most5,

`m + b <=5`

for every `{1}` support class of multiplicity m. By (T3),

> `m<=2`.                                                     (T5)

Combining (T4)--(T5):

> the singleton group contains at least two distinct support classes.   (T6)

## 2. Support-union size and positive-charge vertices

Let Z_i denote the entire zero-signature class i and put

`z_i=|Z_i|>=1`.

A connector, say D_12, is a 3-support containing `Z_1 union Z_2`, hence

`z_1+z_2<=3`.                                                (T7)

The opposite support D_23 gives

`z_2+z_3<=3`.                                                (T8)

Therefore

> `z_1+z_2+z_3<=5`.                                         (T9)

All zero-charge support-union vertices belong to these three signature classes. Every support-union vertex outside their union has positive integer common-S charge; otherwise it would define a fourth zero signature.

There are at most three distinct singleton-code support classes and at most three doubleton-code classes. A singleton-code 3-support introduces at most two private vertices, and a doubleton-code support introduces at most one private vertex beyond its zero cores.

Hence the number P of positive private support-union vertices satisfies

> `P<=3*2+3=9`.                                               (T10)

Let U be the full owner-support union. Then

`|U|=z_1+z_2+z_3+P`,
`W_U>=P`.                                                     (T11)

The three zero signatures have pairwise target-nonadjacent representatives, so

`alpha(H[U])=3`.

The fully-decorated support-to-one-spoke theorem applies:

`k >= 32-2|U|+W_U`
`   >=32-2(z_1+z_2+z_3)-P`
`   >=32-10-9`
`   =13`.                                                     (T12)

Thus at least13 legal one-spoke pivots exist outside U.

## 3. No one-spoke pivot can hit the singleton zero core Z1

Let v be one such one-spoke pivot. Then

`w_v=1`.

Suppose v is target-adjacent to some vertex of Z_1.

Every singleton-code support contains the whole zero core Z_1. By row closure, the one target edge from v into Z_1 consumes the full allowance of v against every singleton-code support. Hence v is target-nonadjacent to every private vertex of every `{1}` support.

By (T6), choose two distinct singleton-code supports. Their private parts are cross target-anticomplete by the common-core intersecting-family theorem. Choose one private vertex p from the first and q from the second. Then

`pq`

is a target nonedge, and v is target-nonadjacent to p,q.

Now consider D_23. It contains three core vertices. Row closure gives

`e_H(v,D_23)<=1`.

Hence v is target-nonadjacent to at least two points of D_23. In particular choose a zero-signature representative

`r in Z_2 union Z_3`

which v does not hit; if the only target neighbour lies in one zero class, use a representative of the other, while if it lies on a private center either zero class works.

The zero vertex r lies outside both singleton supports and is therefore target-anticomplete to p and q.

Thus

`{v,r,p,q}`

is an independent4-set, contradiction.

Therefore:

> every one-spoke pivot is target-nonadjacent to all of Z_1.   (T13)

## 4. Any two one-spoke pivots are target-adjacent

Take two distinct one-spoke pivots v,w.

By row closure against the 3-support D_23,

`e_H(v,D_23)<=1`,
`e_H(w,D_23)<=1`.

Therefore each has at least two target-nonneighbours in D_23. Two 2-subsets of a 3-set intersect, so there exists

`d in D_23`

which is target-nonadjacent to both v and w.                  (T14)

Choose any

`z in Z_1`.

By (T13), both v and w are target-nonadjacent to z.

Also z has zero charge and lies outside D_23. Row closure gives

`e_H(z,D_23)=0`,

so in particular

`zd`

is a target nonedge.                                         (T15)

If vw were a target nonedge, then

`{v,w,z,d}`

would be an independent4-set in H.

Therefore every pair of one-spoke pivots is target-adjacent.

Hence the at least13 one-spoke pivots form a target K13, contradicting

`omega(H)<=11`.

## 5. Type-II closure

Thus:

> **Connected Type-II full closure.**
> No final fully-decorated q32 nine-owner support system can have exactly one singleton zero-signature group together with the opposite doubleton support.   (T16)

Combined with the signature-code reduction, the only remaining connected regime is Type I:

- two singleton signature groups;
- no third singleton group;
- doubleton bridge codes providing connectedness.