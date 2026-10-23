# q36 f=3 K2+K1 terminal — alpha2 remainder strengthening

Status: `PROVED REDUCTION` under `Q36_F3_FAR_LAYER_REDUCTION.md`, the all-pivot row-closure theorem, inherited D13, and lexicographic q36 maximality.

This further reduces the only surviving f=3 candidate.

## 1. Terminal notation

The far regular shell is

`F={a,b,z}`,

where ab is a target edge and z is target-nonadjacent to both a and b.

Let

- `A=N_H(a)`, |A|=11;
- `B=N_H(b)`, |B|=11;
- `Z=N_H(z)`, |Z|=12.

The previous reduction proves

- `Z` is disjoint from A and B;
- `h=|A intersect B|` belongs to `{10,11}`;
- all low-clique supports `D_y`, y in C, are disjoint from `A union B union Z`;
- every D_y has size3;
- `kappa(D_y)+m(D_y)<=2`.

Also `c=|C|>=6` and the decorated shell X has size at most4.

## 2. The 11-supports are dense

The repivot at a has d=11 and outside defect B=0. Since A and B overlap in at least10 vertices, at least ten vertices of A have two old shell neighbours a,b and are globally decorated.

If `q_a=36`, the a-shell would therefore contain at least ten decorated inserted vertices, whereas the old q36 pivot has at most four decorated shell vertices. This would strictly increase the lexicographic secondary potential tau.

Hence

`q_a<=35`, and similarly `q_b<=35`.                         (1)

The exact d11 charge formula gives

`q_a=22+kappa(A)+m(A)+e_F(S_a,A)`,

where `S_a=(C union X) union {z}`.

A is disjoint from every C-support and from Z, so the only shell neighbours from S_a that A can have lie in X. Put

`x_A=e_F(A,X)`.

Then

`kappa(A)+m(A)+x_A<=13`.                                   (2)

The inherited D13 cap gives another useful lower bound on m(A). The induced 13-set

`{a,b} union A`

has

`1+11+h+e_H(A)=12+h+e_H(A)`

target edges. Since D13=67,

`e_H(A)<=55-h`,

so

> `m(A)=55-e_H(A)>=h`.                                     (3)

The same statements hold for B.

## 3. Missing-pair remainders have alpha at most2

Fix y in C and let D=D_y.

The shell pair y,a is a target nonedge. Its core supports D and A are disjoint. Put

`W=H\(D union A)`.

Then |W|=21.

Every vertex of W is target-nonadjacent to both y and a: otherwise it would belong to D or A. If H[W] contained an independent triple, those three vertices together with the missing shell pair {y,a} would form an independent5-set in F, contradicting `alpha(F)<=4`.

Therefore

`alpha(H[W])<=2`.

By Mantel in the complement,

`e_H(W)>=C(21,2)-floor(21^2/4)`
`=210-110`
`=100`.                                                     (4)

## 4. Pair-capacity lower bound on A--D edges

Let `U=A union D`, so |U|=14.

For any subset U of the 211-core,

`sum_(u in U)d_H(u)=12|U|+kappa(U)=2e_H(U)+e_H(U,W)`.

Combining with

`211=e_H(U)+e_H(W)+e_H(U,W)`

gives the exact identity

`e_H(U)=e_H(W)+12|U|+kappa(U)-211`.

Using |U|=14 and (4),

`e_H(U)>=57+kappa(A)+kappa(D)`.                             (5)

Now

`e_H(A)=55-m(A)`,
`e_H(D)=3-m(D)`.

Hence (5) yields

`e_H(A,D)>=m(A)+m(D)+kappa(A)+kappa(D)-1`.                  (6)

## 5. Row closure turns pair capacity into shell-incidence mass

Apply row closure for the a-repivot to a vertex v in D. Since D is disjoint from A,

`e_H(v,A)<=kappa_v+e_F(v,S_a)`.

A D-vertex is not adjacent to z (otherwise it would lie in Z). Its shell neighbours in S_a therefore lie only in `C union X`.

Summing over D,

`e_H(A,D)<=kappa(D)+e_F(D,C union X)`.                      (7)

Combine (6) and (7), cancel kappa(D), and use (3):

`e_F(D,C union X)`
`>=m(A)+kappa(A)+m(D)-1`
`>=h+m(D)-1`.                                               (8)

Thus every low-clique 3-support has at least

- 9 shell incidences when h=10;
- 10 shell incidences when h=11.

## 6. q36 plateau is impossible for a low-clique row

For y in C, the previous f=3 ledger gives

`q_y=34+kappa(D_y)+m(D_y)`.

Suppose equality reached q36. Then

`kappa(D)+m(D)=2`.                                         (9)

But by (8), the three vertices of D have at least9 shell incidences into C union X. Their total global decoration is

`sum_(v in D)g_v`
`=kappa(D)+e_F(D,A_shell)-3`
`=kappa(D)+e_F(D,C union X)-3`
`>=kappa(D)+h+m(D)-4`
`=h-2`,

using (9).

Since h>=10, this is positive. Therefore at least one inserted support vertex is globally decorated.

Repivoting y removes only the three regular far vertices F and retains all old decorated shell vertices X. Thus a q36 repivot would have strictly more decorated shell vertices than p, contradicting lexicographic maximality.

Hence (9) is impossible, and in fact

> `kappa(D_y)+m(D_y)<=1`                                   (10)

for every y in C.

Consequently

- `q_y<=35` for every low-clique y;
- every D_y induces at least two of its three possible H-edges;
- the total internal excess captured by any D_y is at most1.

## 7. Updated K2+K1 terminal

The only f=3 candidate now has:

- h=10 or11;
- an 11/12-point remainder R containing all c>=6 low supports;
- every support D_y is a 3-subset of R;
- `m(D_y)+kappa(D_y)<=1`;
- each D_y sends at least `h+m(D_y)-1` shell incidences into C union X;
- every low-clique repivot has q at most35.

This removes all q36 low-clique plateau cycles from the f=3 terminal. What remains is a finite dense-triple incidence problem inside R.