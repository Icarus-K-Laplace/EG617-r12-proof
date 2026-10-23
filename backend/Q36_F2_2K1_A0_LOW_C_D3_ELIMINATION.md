# q36 f=2, 2K1 far, a_F=0 — elimination of all d3 rows for c<=6

Status: `PROVED` under `Q36_F2_2K1_A0_REDUCTION.md`, the exact d3 allowance formula, and the regular/decorated missing-edge inequality.

Combined with the c=7,8,9,10 closures, this reduces the entire `2K1,a_F=0` branch to pure-d2 terminals with `c<=4`.

## 1. Setup

Let c<=6. Put n2 for the number of d2 low rows and n3=c-n2 for d3 rows. The decorated shell set has size

`r=11-c>=5`.

For every decorated vertex x used by d3 rows define

`n_x=#{low owners missing x}`,
`nu_x=d_(M[X])(x)`,
`A_x=n_x+nu_x+g_x-7`.

The `a_F=0,2K1` d3 formula gives exactly this common-S allowance. The regular/decorated missing-edge inequality between a low owner and its decorated missing vertex gives

> `A_x>=3` for every active d3 class.                       (1)

By `Q36_F2_2K1_A0_REDUCTION.md`, d3 rows use at most two active decorated missing vertices.

## 2. Two active classes are impossible

Suppose x,z are active and let Y=X\{x,z} be the inactive decorated set. Since r>=5,

`|Y|>=3`.

Let `e_xz` be1 if xz is a missing edge and0 otherwise, and let `nu_Y=e_M(Y)`. Summing the two allowances and using

- `n_x+n_z=n3`;
- the exact shell ledger `G=13-c+n2-nu`;
- `nu_x+nu_z = nu + e_xz - nu_Y`;
- `g_x+g_z=G-G_Y`;

all c,n2 and mixed active-inactive missing edges cancel, giving

`A_x+A_z = e_xz - nu_Y - G_Y - 1`.                         (2)

Every vertex of Y is decorated, so `G_Y>=|Y|>=3`. Therefore the right side of (2) is at most

`1-0-3-1=-3`,

contradicting nonnegative allowances.

Hence two active d3 classes are impossible.

## 3. One active class is impossible

Suppose x is the unique active d3 missing vertex and let Y=X\{x}. Then

`|Y|=r-1>=4`.

All missing edges of M[X] are either incident with x or lie inside Y, so

`nu=nu_x+nu_Y`.

Using `n_x=n3=c-n2`, the shell ledger and `G=g_x+G_Y`, we obtain the exact cancellation

`A_x+G_Y = 6-nu_Y`.                                       (3)

Since every vertex of Y is decorated,

`G_Y>=|Y|>=4`.

Therefore (3) gives

`A_x<=2-nu_Y<=2`,

contradicting the universal lower bound (1), `A_x>=3`.

Thus one active d3 class is impossible as well.

## 4. Consequence

For every `c<=6` candidate in the `2K1,a_F=0` branch,

> `n3=0`.

Hence every low row has missing degree2.

But `Q36_F2_2K1_A0_REDUCTION.md` already proves that the all-d2 branch satisfies

> `c<=4`.

Therefore

> `c=5` and `c=6` are EMPTY.

Together with the existing full closures for c=7,8,9,10, the entire `2K1,a_F=0` branch is reduced to four pure-d2 terminals:

`c in {1,2,3,4}`.

No mixed d2/d3 or all-d3 state remains anywhere in this branch.