# q36 f=2, 2K1 far, a_F=0 — high-c single-class normal form

Status: `PROVED` under `Q36_F2_2K1_A0_REDUCTION.md`, the low-allowance capacity theorems, all-pivot core minimum degree 12, row closure, inherited D14, and lexicographic q36 maximality.

This theorem treats the all-d3 / single decorated missing-vertex branch for `c>=7` and closes `c=7,8` completely.

## 1. Setup

Use the `2K1, a_F=0` notation. The two far regular shell vertices have disjoint 12-point core supports, leaving an 11-point remainder `R` with

`alpha(H[R])<=2`.

Assume every low vertex belongs to one d3 class: all `c>=7` low owners miss the same decorated shell vertex `x` in addition to the two far vertices.

Let

- `nu=e_M(X)`;
- `nu_x=d_(M[X])(x)`;
- `g_x` be the shell decoration of x;
- `A=c+nu_x+g_x-7` be the common-S allowance;
- `D_x=N_H(x)` be the core row of x.

The exact shell ledger is

`G=13-c-nu`.

There are `r=11-c` decorated shell vertices. All decorated vertices other than x contribute at least one unit each, hence

`g_x<=G-(r-1)=3-nu`.                                      (1)

Consequently

`A<=c-4`.                                                   (2)

## 2. Regular/decorated zero-gap at a low owner

Let y be any low owner and `D_y=N_H(y)`, |D_y|=3.

Because all low rows miss the same triple,

`N_M(y)=F union {x}`.

Moreover x is missing-adjacent to all c low vertices and to both far vertices, together with its `nu_x` missing neighbours inside X. Hence

`|N_M(y) union N_M(x)|=c+3+nu_x`.

The all-pivot minimum-degree12 exchange inequality for the missing shell edge yx is

`|N_M(y) union N_M(x)|+g_x >= 13+|D_y intersect D_x|`.

Using the definition of A gives

> `|D_y intersect D_x|=e_F(x,D_y)<=A-3`.                  (3)

Thus every low support contains at least

`3-(A-3)=6-A`                                              (4)

vertices of `R\N_H(x)`.

## 3. The two far rows force the opposite bound

For either far regular vertex a, its shell missing neighbourhood has size12. Applying the same regular/decorated exchange inequality to the missing edge ax gives

`|N_H(a) intersect D_x|<=g_x-1`.

The two far supports are disjoint, so together they meet D_x in at most `2(g_x-1)` vertices.

Since

`|D_x|=d_M(x)+g_x=c+2+nu_x+g_x=A+9`,

we obtain

`e_F(x,R)>=A+9-2(g_x-1)=A+11-2g_x`.

Therefore, if

`t=|R\N_H(x)|`,

then

> `t<=2g_x-A`.                                              (5)

But (4) requires `t>=6-A`. Combining with (5) yields

`6-A<=2g_x-A`,

hence

> `g_x>=3`.                                                 (6)

Together with (1), this forces equality everywhere:

> `nu=0`, `g_x=3`, `nu_x=0`, `A=c-4`.                     (7)

Now (5) and (4) are equalities:

> `t=10-c`.                                                 (8)

Moreover every support D_y contains the complete t-point set

`Z=R\N_H(x)`,

and contains exactly `c-7` vertices of `N_H(x) intersect R`.

Thus every high-c support has the exact form

> `D_y=Z union P_y`, where `|Z|=10-c` and `|P_y|=c-7`.      (9)

This is the high-c single-class normal form.

## 4. Uniform decoration inequality for a support class

Let a distinct support D have owner multiplicity s.

Every vertex of Z belongs to every one of the c low supports, hence has at least c old shell neighbours and therefore global decoration at least `c-1`.

Every vertex of `P_y` is adjacent to x and to all s owners of its support class, hence has global decoration at least s.

Repivoting one owner removes x and the two regular far vertices. Since `G=13-c` and `g_x=3`, the retained old decoration is exactly

`G-g_x=10-c=t`.

Therefore the new shell decoration satisfies

`G' >= t + t(c-1) + (c-7)s`
`   = c(10-c)+(c-7)s`.                                    (10)

On the other hand, by (3) and (7),

`e_F(x,D)=c-7`,

so the exact support defect gives

`q_D=33+kappa(D)+m(D)`.

Since the common-S allowance is `A=c-4`,

`kappa(D)+m(D)<=3`.

The inherited 14-point missing-edge floor gives

`G'<=q_D-22=11+kappa(D)+m(D)<=14`.                         (11)

Combining (10)--(11):

> `c(10-c)+(c-7)s<=14`.                                   (12)

## 5. c=7 is impossible

Here `t=3` and every support equals the same three-point set Z. Formula (10) already gives

`G'>=7*3=21`,

contradicting (11).

Therefore

> `c=7` is EMPTY.                                          (13)

This also closes both residual cases `|R\N(x)|=2,3` from the earlier allowance-three reduction: the exact zero-gap argument shows only t=3 can occur, and that state is impossible by decoration overflow.

## 6. c=8 is impossible

Here `t=2`, and every support has the form

`D_y=Z union {p_y}`

for the same two-point set Z.

For any support class `s>=1`, (10) gives

`G'>=8*2+s=16+s>=17`,

again contradicting the universal upper bound14 in (11).

Hence

> `c=8` is EMPTY.                                          (14)

## 7. c=9 and c=10 residuals

The normal form also sharply reduces the only larger possible low-clique sizes.

### c=9

`t=1`. Every support is

`D_y={z} union P_y`, `|P_y|=2`,

for one common core vertex z.

Equation (12) gives

`9+2s<=14`,

so every support class has

> `s<=2`.                                                    (15)

Therefore the nine owners require at least five distinct support classes.

Moreover a q36 plateau support is impossible: the common vertex z is already adjacent to all nine owners, while the two petals are adjacent to x and their owner(s); repivoting would insert three decorated vertices and retain the other old decorated shell vertex, strictly increasing tau. Hence every support actually has `q<=35` and

`kappa(D)+m(D)<=2`.

If a class repeats (`s=2`), (10)--(11) force equality

`kappa(D)+m(D)=2`,

so its q35 repivot saturates the D14 decoration bound.

### c=10

`t=0`. Every support is a 3-subset of `N_H(x) intersect R`.

Equation (12) gives

`3s<=14`,

so

> `s<=4`.                                                    (16)

Thus ten owners require at least three distinct support classes.

Again a q36 plateau support would insert three decorated vertices into a shell whose old tau is one, so every support has `q<=35` and `kappa(D)+m(D)<=2`.

## 8. New frontier

The all-d3 / single-class high-c branch is now completely normalized:

- c=7: EMPTY;
- c=8: EMPTY;
- c=9: one common core vertex plus at least five 2-petal support classes, each multiplicity <=2;
- c=10: at least three 3-support classes, each multiplicity <=4.

The next task is the finite support-capacity closure of c=9 and c=10. The mixed d2/d3 branches and the far-target-K2 topology remain separate.