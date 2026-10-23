# q36 candidate coverage — f=2 exact shell ledger

Status: `PROVED REDUCTION` under the q36 CORE211 top-channel contract, `Q36_CANDIDATE_COVERAGE_CLUSTER_REDUCTION.md`, and the q36 d4/d9 closures.

This treats the low-clique regime with exactly two far/high regular shell vertices. It does not yet close the full f=2 layer.

## 1. Shell partition

Let

- `C` be the unique low regular target clique, `|C|=c`;
- `F={a,b}` be the two far/high regular shell vertices;
- `X` be the decorated shell vertices, `|X|=r`.

Then

`c+r=11`.

Let

- `mu=e_M(F)`, so `mu=0` when F is a target K2 and `mu=1` when F is 2K1;
- `delta=e_M(C,X)`;
- `nu=e_M(X)`;
- `a_F=e_F(F,X)`.

Every y in C is missing-adjacent to both far vertices. Since q36 has no regular d4/d9 exchange and every low regular degree is at most3, necessarily

> `d_M(y) in {2,3}` for every y in C.

Hence each y misses at most one decorated vertex and

> `delta<=c`.                                               (1)

The number of d3 vertices in C is exactly delta; the remaining `c-delta` vertices have d2.

## 2. Far/decorated incidence bound

A decorated shell vertex can have regular target neighbours in at most one regular target-clique component.

### F=K2

For a far regular vertex u, if `t_u=e_F(u,X)`, then

`d_M(u)=c+(r-t_u)=11-t_u`.

Since u is high, `d_M(u)>=10`, so `t_u<=1`. Thus

> `a_F<=2`.                                                 (2)

### F=2K1

The two far vertices lie in different regular components. Any decorated vertex with a far target neighbour is therefore anticomplete to C. Two such decorated vertices would make every y in C miss at least four shell vertices (the two far vertices plus those two decorated vertices), impossible.

Moreover one decorated vertex cannot target both far singleton components. Hence

> `a_F<=1`.                                                 (3)

## 3. Exact q36 shell ledger

The missing edges of M are exactly

- the `2c` C--F pairs;
- `mu` inside F;
- `delta` between C and X;
- `2r-a_F` between F and X;
- `nu` inside X.

Therefore

`e(M)=2c+mu+delta+2r-a_F+nu`
`    =22+mu+delta-a_F+nu`.

Since q=36=e(M)+G,

> `G=14-mu-delta+a_F-nu`.                                  (4)

This identity will be used as the f=2 master ledger.

## 4. Exact d2 row formula

Let y in C have missing degree2. Then its missing set is exactly F.

Its outside set is `(C\{y}) union X`. The outside missing-edge contribution is `delta+nu`, and all shell decoration lies in X. Hence

`B_y=delta+nu+G=14-mu+a_F`.

The exact repivot formula gives

> `q_y=36-mu+a_F + kappa(D_y)+m(D_y)+e_F(F,D_y)`.           (5)

All final terms are nonnegative.

Consequences:

### F=K2 (`mu=0`)

If a d2 row exists, q36 maximality forces

- `a_F=0`;
- `kappa(D_y)=0`;
- `m(D_y)=0`;
- `e_F(F,D_y)=0`;
- `q_y=36`.

Thus every d2 support is a pure K2 of core-degree12 vertices, target-anticomplete to F.

All d2 rows have the same missing set F and zero common-S allowance. Hence their supports are equal or disjoint, and distinct supports are target-anticomplete.

Equal supports cannot occur: a support repeated by two owners has both support vertices globally decorated, while a q36 repivot removes only the two regular far vertices and retains every old decorated shell vertex. The shell-decoration count tau would strictly increase, contradicting lexicographic maximality.

Therefore all d2 supports are distinct, disjoint, and pairwise target-anticomplete. Four such supports would give an independent4-set in H. Hence

> in the F=K2 branch, the number of d2 vertices in C is at most3.       (6)

### F=2K1 (`mu=1`)

Equation (5) gives

`kappa(D_y)+m(D_y)+e_F(F,D_y) <= 1-a_F`.

Thus the allowance is zero when `a_F=1`, and at most one when `a_F=0`. No stronger realization claim is made here.

## 5. Exact d3 row formula

Let y in C have d3 and let x in X be its unique additional missing neighbour. For each decorated vertex x define

- `n_x=#{y in C : yx in M}`;
- `nu_x=d_(M[X])(x)`;
- `L_x=n_x+nu_x+g_x`.

For a y counted by n_x, its missing set is `F union {x}`.

Deleting y and x from the outside ledger gives

`B_x=14-mu+a_F-L_x`.

Hence the exact d3 charge formula is

> `q_y=44-mu+a_F-L_x + Delta_x`,                            (7)

where

`Delta_x=kappa(D_y)+m(D_y)+e_F(F union {x},D_y)>=0`.

q36 maximality therefore forces

> `L_x>=8-mu+a_F`,                                         (8)

and for every row in this missing-set class

> `Delta_x <= A_x := L_x-(8-mu+a_F)`.                      (9)

So `A_x` is the exact common-S allowance for the class of low rows missing x.

## 6. K2 far topology: at most two d3 missing-set classes

Assume F is a target K2 (`mu=0`).

Let `n_2=c-delta` be the number of d2 rows. If `n_2>0`, section4 already gives `a_F=0` and `n_2<=3`.

Let `X_0={x:n_x>0}` and `h=|X_0|` be the number of distinct decorated vertices missed by d3 rows.

Summing L_x over X_0 gives

`sum_(X_0)L_x <= delta+2nu+G = 14+a_F+nu`.                 (10)

The decoration floor `G>=r=11-c`, together with (4), gives

`nu<=3+n_2+a_F`.                                           (11)

If `h>=3`, (8) requires

`sum L_x >= 3(8+a_F)`,

whereas (10)--(11) give at most

`17+n_2+2a_F <=20+2a_F`.

Since `n_2<=3` whenever d2 rows occur, this is strictly smaller than `24+3a_F`. If no d2 row occurs, `n_2=0` and the contradiction is stronger.

Therefore

> in the F=K2 branch, d3 rows use at most two decorated missing vertices: `h<=2`.    (12)

If in addition there are no d2 rows, then `delta=c` and (11) sharpens to `nu<=3+a_F`. For `h=2`, summing the exact allowances gives

`A_x+A_z <= nu-2-a_F <=1`.                                 (13)

Thus the no-d2 K2 branch has at most two common-S d3 classes, and when two occur their total allowance is at most one.

## 7. Current f=2 interface

Every q36 f=2 low-clique candidate satisfies the exact ledger (4).

For far target K2:

- d2 rows, if present, have pure disjoint K2 supports and there are at most3 of them;
- d3 rows split into at most two decorated missing-set classes;
- if all low rows are d3 and both classes occur, their total common-S allowance is at most1.

For far 2K1:

- `a_F<=1`;
- d2 row allowance is exactly `1-a_F`;
- every d3 class obeys the exact threshold/allowance formulas (8)--(9).

The remaining work is joint-core capacity for these few d2/d3 classes, especially the far-2K1 branch where the two large far supports are disjoint and leave an 11/12-point alpha-two remainder.