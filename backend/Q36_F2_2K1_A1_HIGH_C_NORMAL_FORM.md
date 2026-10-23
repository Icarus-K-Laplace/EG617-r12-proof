# q36 f=2, 2K1 far, a_F=1 — high-c normal form

Status: `PROVED REDUCTION` under `Q36_F2_2K1_A1_REDUCTION.md`, row closure, the all-pivot minimum-degree theorem, inherited D14, and lexicographic q36 maximality.

This parameterizes every remaining c>=7 state.

## 1. Setup

Let x0 be the unique decorated shell vertex with a far target neighbour. All c low owners have the same d3 missing set

`S=F union {x0}`.

Let

- `Y=X\{x0}`;
- `|Y|=10-c`;
- `nu_0=d_(M[X])(x0)`;
- `nu_Y=e_M(Y)`;
- `G_Y=sum_(y in Y)g_y`;
- `A=c+nu_0+g_0-8` be the common-S allowance.

The shell ledger is

`G=14-c-nu`,

and `nu=nu_0+nu_Y` because every missing edge of X is either incident with x0 or lies inside Y.

## 2. Exact inactive-decoration identity

Using `G=g_0+G_Y`,

`A+G_Y`
`= c+nu_0+g_0-8 + 14-c-(nu_0+nu_Y)-g_0`
`= 6-nu_Y`.

Therefore

> `A+G_Y=6-nu_Y`.                                         (1)

Every vertex of Y is decorated, so

`G_Y>=|Y|=10-c`.

Hence

> `A<=c-4-nu_Y<=c-4`.                                     (2)

## 3. Universal lower bound A>=2

Let u be any low owner. It is regular and missing-adjacent to x0.

The union of their shell missing neighbourhoods has size

`c+3+nu_0`:

- the c low owners missed by x0;
- the two far vertices supplied by the owner row and the one far non-neighbour of x0;
- x0 itself from the owner's missing triple;
- the nu_0 internal X-missing neighbours of x0.

The regular/decorated missing-edge inequality gives

`c+3+nu_0+g_0 >= 13 + |D_u intersect D_x0|`.

Since `A=c+nu_0+g_0-8`,

> `|D_u intersect D_x0|<=A-2`.                            (3)

In particular

> `A>=2`.                                                   (4)

Every low support therefore contains at least `5-A` vertices outside the core row of x0 whenever `A<=5`.

## 4. The inactive 11-point base

The set

`B0={p} union C union Y`

has exactly

`1+c+(10-c)=11`

vertices.

The pivot p is target-adjacent to C and Y, C is a target clique, and every inactive decorated vertex in Y is target-adjacent to every low owner. The only target nonedges inside B0 are the `nu_Y` missing edges internal to Y.

Hence

> `e(B0)=55-nu_Y`.                                        (5)

For any core triple T subset R, inherited D14 gives

> `lambda(T)+e_F(Y,T)+e_H(T)<=14+nu_Y`,                  (6)

where lambda_v is the number of low supports containing v.

Since `alpha(H[R])<=2`, every triple has at least one H-edge, so

> `lambda(T)<=13+nu_Y`.                                   (7)

## 5. Repeated-support multiplicity bound

Let a 3-support D be used by m>=2 low owners.

If its support defect were the full allowance A, its repivot would remain at q36. All three support vertices have at least two shell owners and are globally decorated. The repivot removes x0 but retains all `|Y|` old decorated vertices, so the new decorated-vertex count is at least

`|Y|+3 > |Y|+1=|X|`,

contradicting lexicographic maximality.

Thus every repeated support repivots to q<=35.

Each support vertex has global decoration at least m-1 from its m shell owners. The repivot retains all inactive decoration G_Y. Since every q<=35 shell has total decoration at most13,

> `G_Y+3(m-1)<=13`.                                       (8)

Also applying (6) to T=D and using `lambda(D)>=3m`, `e_H(D)>=1` gives

> `3m<=13+nu_Y`.                                           (9)

These are two independent multiplicity bounds.

## 6. c-specific normal forms

### c=7

`|Y|=3`. From (1),(4):

- A=3 implies `nu_Y=0`, `G_Y=3`; Y is a target K3 and all three inactive decorations equal1;
- A=2 implies `G_Y=4-nu_Y`, hence `nu_Y in {0,1}`.

Thus A is exactly2 or3. Equations (8)--(9) imply every support class has multiplicity at most4.

### c=8

`|Y|=2`. Equation (1) gives `A+G_Y=6-nu_Y` with `G_Y>=2`, so

`2<=A<=4-nu_Y`.

Again every repeated class has multiplicity at most4.

### c=9

`|Y|=1`, so `nu_Y=0` and

`A+g_Y=6`.

Hence `2<=A<=5`.

### c=10

Y is empty. Equation (1) forces

> `A=6`.                                                     (10)

The base B0 is the target K11 `{p} union C`. Equation (9) gives every repeated support multiplicity at most4.

## 7. New frontier

The remaining `2K1,a_F=1,c>=7` branch is now a finite high-c support problem with:

- one common missing triple S;
- allowance A in the ranges above;
- an 11-point K11-minus-nu_Y base carrying the D14 incidence cap (6);
- every repeated support of multiplicity at most4 and q<=35.

The next target is c=7, where only A=2 or3 remains.