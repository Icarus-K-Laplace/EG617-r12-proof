# q36 f=2 far-target-K2 — c=8 no-d2, allowance one full closure V2

Status: `PROVED` under `Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION_V2.md`, `Q36_F2_FAR_K2_D14_CONTRACT_CORRECTION.md`, common-S row closure, CORE211, `alpha(H)<=3`, and the actual parent clique bound `omega<=11`.

This closes the sole `rho=1, 4+4` equality terminal left by the corrected A=1 reduction. No global target-K4 prohibition and no false `{p} union C union F` K11 base is used.

## 1. Equality terminal

The V2 reduction proves that the only possible A=1 state has:

- inactive decorated pair `Y` a target nonedge (`rho=1`);
- exactly two distinct support classes D,E;
- D,E target K3s of owner multiplicity4 each;
- both supports have defect0;
- D and E are target-anticomplete to each other;
- D,E are target-anticomplete to every shell vertex in `F union X`;
- `a_F=2` and the active decorated vertex x has `t_x=e_F(x,F)=0`.

Put

`S=F union {x}`

and for every core vertex v define

`w_v=kappa_v+e_F(v,S)`.

For D,E we have w=0 on all six block vertices.

## 2. Low-weight outside vertices form a target clique

Let u,v be core vertices outside `D union E` with

`w_u<=1`, `w_v<=1`.

Row closure against D gives

`e_H(u,D)<=1`, `e_H(v,D)<=1`.

Thus each of u,v is target-nonadjacent to at least two of the three vertices of D. Two subsets of a 3-set of size at least2 intersect, so there exists

`d in D`

that is target-nonadjacent to both u and v.

The same argument with E gives

`e in E`

target-nonadjacent to both u and v.

Since D and E are target-anticomplete, de is a target nonedge.

If uv were also a target nonedge, then

`{u,v,d,e}`

would be an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore

> any two outside core vertices with weight at most1 are target-adjacent.   (1)

So the set

`L={v in H\(D union E): w_v<=1}`

is a target clique. The parent/core clique contract gives

`|L|<=11`.                                                   (2)

## 3. Global lower bound on common-S weight

There are

`35-6=29`

core vertices outside D union E. By (2), at least

`29-11=18`

of them have `w_v>=2`.

The six D/E vertices have weight0. Hence

> `sum_(v in H) w_v >=18*2=36`.                              (3)

## 4. Exact global upper bound

CORE211 gives

`sum_H kappa_v=2`.                                           (4)

For a regular far shell vertex f, its core-row size equals its shell missing degree

`|D_f|=11-t_f`,

where `t_f=e_F(f,X)`. Summing the two far rows gives

`|D_a|+|D_b|=22-a_F=20`                                    (5)

because the equality terminal has `a_F=2`.

For the active decorated vertex x,

`d_M(x)=10-t_x+nu_x`

and the A=1 identity gives

`g_x=1+a_F-nu_x`.

Therefore its core-row size is

`|D_x|=d_M(x)+g_x`
`     =11+a_F-t_x`
`     =13`                                                    (6)

because `a_F=2`, `t_x=0`.

Thus the total target incidence from S into the core is

`e_F(S,H)=20+13=33`.                                         (7)

Combining (4) and (7),

> `sum_H w_v =2+33=35`.                                     (8)

This contradicts the lower bound (3).

## 5. Conclusion

The corrected A=1 equality terminal is impossible. Therefore

> `q36 f=2`, far-target-K2, `c=8`, no-d2, `A=1` is EMPTY.

Together with the shell-only A=0 closure, the safely certified low-allowance state is now:

- A=0: EMPTY;
- A=1: EMPTY by this V2 proof;
- A=2: reopened pending corrected-D14 audit;
- A=3,A=4: OPEN.