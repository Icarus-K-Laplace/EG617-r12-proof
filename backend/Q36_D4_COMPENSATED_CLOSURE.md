# q36 compensated d4 ceiling branch — full closure

Status: `PROVED` under the standard legal backend contract and the preceding q36 compensated reductions.

This eliminates every q36 zero-defect d4 ceiling exchange.

## 1. Setup

By `Q36_COMPENSATED_K49_NORMAL_FORM.md`, a surviving d4 exchange has

- a decorated four-side S, |S|=4;
- a regular nine-side U, |U|=9;
- S and U target cliques;
- a target cross graph C between S and U;
- every s in S decorated with `g_s=d_C(s)>0`;
- `G=e(C)<=14`;
- the original zero column y in U has cross-degree0.

For `u in U`, write

`c=d_C(u)`.

Since u is globally regular,

`d_M(u)=4-c`,

and its core-row size is also `4-c`.

## 2. Exact rho for an active column

Assume `c>0` and let

`C_u=N_F(u) intersect S`, `|C_u|=c`.

The missing set of u is `S\C_u`, so the outside set in the exact repivot identity is

`T_u=(U\{u}) union C_u`.

There are no missing edges inside U and none inside S. Hence the only missing edges in `T_u` go between `C_u` and `U\{u}`.

Fix `s in C_u`. In the compensated normal form, s has target cross-degree `g_s` in U. Since u is one of those target neighbours, exactly

`9-g_s`

vertices of `U\{u}` are missing-neighbours of s.

Therefore

`e_M(T_u)=sum_(s in C_u)(9-g_s)`.

All U-vertices are regular, while the decoration inside T_u is exactly

`G_Tu=sum_(s in C_u)g_s`.

Thus the rho term is exact:

> `rho_u=e_M(T_u)+G_Tu=9c`.                                (1)

## 3. Cross-degrees 1,2,3 force a strict q-rise

The exact repivot theorem gives

`q_u=d(13-d)+rho_u+h+kappa+b`,

with all final three terms nonnegative.

Using `d=4-c` and (1):

### c=1

`d=3`, so

`q_u>=3*10+9=39>36`.

### c=2

`d=2`, so

`q_u>=2*11+18=40>36`.

### c=3

`d=1`, so

`q_u>=1*12+27=39>36`.

All contradict q36 maximality.

Hence every active column must satisfy

> `c=4`.                                                    (2)

Such a column has missing degree0 and empty core row; it is a true-twin column of the pivot inside the closed shell.

## 4. Final counting contradiction

Let a be the number of active columns. By (2), every active column contributes four target cross edges. Hence

`G=4a`.

Every row of S is nonempty, so `a>=1`. The inherited D14 bound gives `G<=14`, therefore

`a<=3`.

Thus the number of zero columns is

`n_0=9-a>=6`.                                               (3)

But `Q36_D4_SUPPORT_CLASS_REDUCTION.md` proves that every surviving compensated d4 state has exactly one zero-column support class, and `Q36_D4_COMPENSATED_DYNAMICS.md` proves that the multiplicity of one K4 support class is at most4.

Therefore

`n_0<=4`,                                                   (4)

contradicting (3).

Hence no compensated d4 q36 ceiling state survives.

## 5. q36 middle-distance conclusion

Together with `Q36_D9_COMPENSATED_CLOSURE.md`:

> a q36 lexicographically maximal CORE211 pivot has no adjacent regular shell exchange of missing degree4 or9.

Thus any remaining q36 ceiling survivor must have every adjacent regular positive distance in

`{1,2,3,10,11,12}`

(with distance0 reserved for true twins).

This is a strict structural reduction of the E338 ceiling channel, not yet a proof that the entire q36 channel is empty: a candidate-coverage theorem forcing a d4/d9 exchange is still required.