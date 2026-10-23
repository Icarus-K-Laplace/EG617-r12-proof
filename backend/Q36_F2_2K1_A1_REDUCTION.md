# q36 f=2 — two-singleton far branch with one far-decoration incidence

Status: `PROVED REDUCTION` under `Q36_F2_SHELL_LEDGER_REDUCTION.md`, CORE211, row closure, and lexicographic q36 maximality.

This treats the branch

- the two far regular vertices form `2K1` in the target graph (`mu=1`);
- `a_F=e_F(F,X)=1`.

It eliminates `c=4,5` and reduces `c=6` to an exact allowance-two equality terminal.

## 1. All low rows share one d3 missing set

Let `F={a,b}` and let x0 be the unique decorated vertex with a far target neighbour.

Because a decorated shell vertex can target regular vertices in at most one regular clique component, x0 is target-anticomplete to the low clique C.

Every y in C is already missing-adjacent to a and b. Since low regular missing degree is at most3, y cannot miss any other decorated vertex. Therefore

- every y in C has `d_M(y)=3`;
- every y has the same missing set
  `S=F union {x0}`;
- every other decorated vertex is target-complete to C.

Thus `delta=c`, and the exact f=2 ledger gives

`G=14-1-c+1-nu=14-c-nu=3+r-nu`,

where `r=11-c` and `nu=e_M(X)`.

The decoration excess above the mandatory one unit per decorated vertex is therefore

`G-r=3-nu`,

so

> `nu<=3`.                                                  (1)

## 2. The far supports leave a 12-point alpha-two remainder

The far vertex adjacent to x0 has missing degree11; the other has missing degree12. Their core supports A,B therefore have sizes11 and12.

Because a,b are regular and target-nonadjacent, zero-gap gives

`A intersect B=empty`.

Every low y is target-nonadjacent to both a and b, so its 3-support D_y is disjoint from `A union B`.

Put

`R=H\(A union B)`.

Then `|R|=12` and every low support is contained in R.

Every vertex of R is target-nonadjacent to both shell vertices a,b. If H[R] contained an independent triple, that triple together with {a,b} would form an independent5-set in F. Hence

> `alpha(H[R])<=2`, and in particular `e_H(R)>=30`.         (2)

## 3. Exact common-S allowance

Let

`nu_0=d_(M[X])(x0)`.

Since x0 is missed by all c low vertices, the d3 formula from the f=2 ledger gives

`L_0=c+nu_0+g_0`,

with common-S allowance

> `A_0=L_0-8=c+nu_0+g_0-8`.                               (3)

Maximality requires `A_0>=0`.

From (1), all decoration beyond the mandatory unit sum is `3-nu`, so

`g_0<=4-nu`.

Also `nu_0<=nu`. Therefore

`nu_0+g_0<=4`,

and (3) yields

> `0<=A_0<=c-4`.                                           (4)

In particular `c>=4`.

## 4. c=4 is impossible

Here (4) gives `A_0=0`.

The common-S overlap theorem for d=3 implies distinct supports are disjoint and target-anticomplete; equal supports are also allowed algebraically.

Equal supports cannot repeat. With zero allowance every repivot stays at q36 and the support is a pure K3 of H-degree12 vertices, target-anticomplete to S. If the same support served two owners, all three support vertices would be globally decorated. Repivoting removes only the one decorated vertex x0 and retains all other old decorated vertices, so tau would strictly increase.

Thus the four owners require four distinct pairwise-antocomplete K3 supports. Choosing one vertex from each gives an independent4-set in H, contradiction.

Therefore

> `c!=4`.                                                   (5)

## 5. c=5 is impossible

Now `A_0<=1`.

If `A_0=0`, the previous argument is already stronger.

Assume `A_0=1`. Proper overlap of two 3-supports costs

`h(3-h)=2>1`,

so distinct supports are again disjoint, with at most one target edge between them.

Three distinct support classes are impossible inside R: choose one vertex uniformly from each class. The expected number of target edges among the three choices is at most `3/9<1`, so some choice has no target edge, giving an independent triple in H[R], contradicting (2). Thus there are at most two support classes.

A single support class of multiplicity5 is impossible. Any repeated support must use defect zero; otherwise its repivot would remain at q36 and increase tau. Hence it is a pure K3 and repivots to q35. Its three vertices each have global decoration at least4. The old shell retains decoration at least

`G-g_0 >= (9-nu)-(4-nu)=5`.

Thus the new q35 shell would have decoration total at least

`5+3*4=17`,

whereas the inherited D14 bound gives `G'<=q'-22=13`.

So there are exactly two distinct support classes D1,D2.

At least one is repeated; every repeated class has zero defect and therefore has

- H[D_i]=K3;
- kappa(D_i)=0;
- `e_F(x0,D_i)=0`.

Let `L=R\(D1 union D2)`, so |L|=6.

Because `alpha(H[R])<=2` and `e_H(D1,D2)<=1`, every v in L must have at least two neighbours in one of D1,D2. Otherwise each block contains a non-neighbour of v and the pair can be chosen target-nonadjacent, producing an independent triple with v. Row closure therefore gives

`w_v:=kappa_v+e_F(v,x0)>=2`

for every v in L. Hence

`sum_L w_v>=12`.                                           (6)

But globally on R,

`sum_R w_v <= kappa(R)+e_F(x0,R)`
`             <=2+|N_H(x0)|`.

Here

`|N_H(x0)|=d_M(x0)+g_0`
`         =c+1+nu_0+g_0`
`         <=5+1+4=10`.

Thus `sum_R w_v<=12`. Equality in (6) would force every support vertex to have w=0. In particular x0 has no neighbour in either D1 or D2, so all its R-neighbours lie in the six-point set L. Then

`sum_R w_v<=kappa(R)+6<=8`,

contradicting (6).

Therefore

> `c!=5`.                                                   (7)

## 6. c=6 forces the allowance-two equality terminal

For c=6, (4) gives `A_0<=2`.

### A_0=0

Impossible by the zero-allowance argument.

### A_0=1

Distinct supports are disjoint with cross-edge count at most1, and there are at most two support classes by the same alpha-two argument.

If one class has multiplicity at least5, its zero-defect q35 repivot contributes at least `3*4=12` inserted decoration, while the retained old decoration is at least

`G-g_0 >= (8-nu)-(4-nu)=4`;

thus `G'>=16>13`, impossible.

The remaining multiplicity partitions are 4+2 or3+3. Both support classes are repeated, hence both have zero defect and are pure K3s target-anticomplete to x0.

Again L has six vertices. Alpha-two plus at most one cross-edge between the two K3s gives `w_v>=2` for every v in L, so `sum_L w_v>=12`.

But both support blocks have w=0, so x0 can meet only L inside R. Hence

`sum_R w_v<=kappa(R)+6<=8`,

contradiction.

Therefore `A_0=1` is impossible.

Consequently

> `c=6 => A_0=2`.                                          (8)

By (3),

`nu_0+g_0=4`.

Since separately `nu_0<=nu` and `g_0<=4-nu`, equality forces

> `nu_0=nu`, `g_0=4-nu`.                                  (9)

Thus every missing edge of M[X] is incident to x0, all other decorated vertices have decoration exactly1, and

`|N_H(x0)|=d_M(x0)+g_0`
`         =(c+1+nu_0)+g_0`
`         =7+4=11`.                                        (10)

Because `nu<=3`, the c=6 branch is reduced to four exact layers `nu=0,1,2,3`.

## 7. Current interface

In the `F=2K1, a_F=1` f=2 branch:

- `c>=6`;
- c=4 and5 are empty;
- if c=6, all six low rows share one d3 missing set and have common-S allowance exactly2;
- the distinguished decorated vertex x0 has an 11-point core row;
- all X-missing edges are incident to x0;
- `g_x0=4-nu` and every other decorated vertex has g=1.

The remaining c=6 terminal is now a finite six-row allowance-two compatibility problem inside the 12-point alpha-two remainder R. The cases c>=7 remain to be reduced separately.