# General-r Symbolic Backend and Repivot Identities

Status: **PROVED_SYMBOLIC CONDITIONAL ON THE GENERAL BACKEND SETUP**.

The setup assumed here is:

- a residual graph F on `4r+1` vertices;
- `alpha(F)<=4`, `omega(F)<=r-1`;
- a legal pivot p of degree `r+1`;
- shell `A=N_F(p)`, so `|A|=r+1`;
- core `H=V(F)\N[p]`, so `|H|=3r-1`;
- every legal repivot core has minimum degree at least r.

These identities do not prove that the setup exists for every r. They prove that once it exists, the r=12 bookkeeping is exactly symbolic.

## 1. Shell charge and backend edge identity

Let

`M=bar(F[A])`,

`g_v=d_F(v)-(r+1)>=0` for `v in A`, and

`G_A=sum_(v in A)g_v`.

Define

`q=e(M)+G_A`.

For `v in A`, the number of core neighbours is

`t_v=d_M(v)+g_v`.

Summing over A,

`e_F(A,H)=sum_v t_v=2e(M)+G_A`.

Also

`e_F(A)=C(r+1,2)-e(M)`.

Therefore

`e(F)=(r+1)+e_F(A)+e_F(A,H)+e(H)`

`=C(r+2,2)+e(M)+G_A+e(H)`.

Hence

> **`e(F)=C(r+2,2)+q+e(H)`.**

For r=12, `C(14,2)=91`.

## 2. Core excess identity

Define

`K_r(H)=sum_v(d_H(v)-r)=2e(H)-r(3r-1)`.

If `E=e(F)`, the backend identity gives

`e(H)=E-C(r+2,2)-q`.

Thus

> **`K_r(H)=2(E-q-(2r^2+r+1))`.**

Indeed

`2C(r+2,2)+r(3r-1)=4r^2+2r+2`.

For r=12, `2r^2+r+1=301`, recovering

`K=2(E-301-q)`.

Thus the r=12 constant 301 is structural.

## 3. Symbolic regular repivot identity

Let y be a regular shell vertex, so `d_F(y)=r+1`.

Put

- `S=N_M(y)`, `d=|S|`;
- `T=A\(S union {y})`, so `|T|=r-d`;
- `D=N_H(y)`, so `|D|=d`;
- `kappa_v=d_H(v)-r`;
- `m(D)=C(d,2)-e_H(D)`;
- `B_y=e_M(T)+G_T`.

After repivoting y,

`A_y={p} union T union D`,

`H_y=(H\D) union S`.

Direct edge/decorative partition gives

> **`q_y=d(r+1-d)+B_y+kappa(D)+m(D)+e_F(S,D)`.**

Every correction term after the quadratic base is nonnegative.

This is the symbolic version of the r=12 formula `q_y=d(13-d)+P_y`.

## 4. Symbolic row closure

For `v in H\D`, compare its old and repivot-core degrees. It loses `e_H(v,D)` neighbours and gains `e_F(v,S)` neighbours. Since the new core has minimum degree at least r,

`r+kappa_v-e_H(v,D)+e_F(v,S)>=r`.

Hence

> **`e_H(v,D)<=kappa_v+e_F(v,S)`.**

Thus the common-S charge

`w_v=kappa_v+e_F(v,S)`

is already fully symbolic.

## 5. Nonadjacent regular zero-gap relation

For two nonadjacent regular vertices x,y of degree `r+1`, the core-minimum-degree condition gives

`|N_F(x) intersect N_F(y)|<=1`.

If x,y lie in one shell A, with missing sets `S_x,S_y` and core rows `D_x,D_y`, their common target neighbours are

`1 + (r+1-|S_x union S_y|) + |D_x intersect D_y|`.

Therefore

`r+2-|S_x union S_y|+|D_x intersect D_y|<=1`.

Since `|S_x union S_y|<=r+1`, equality is forced:

> **`S_x union S_y=A`,**
>
> **`D_x intersect D_y=empty`.**

This zero-gap theorem is independent of r.

## 6. Symbolic quadratic critical structure

Every regular repivot satisfies

`q_y>=d(r+1-d)`.

The base quadratic is symmetric under

`d <-> r+1-d`.

Thus all fixed-r missing-degree windows near a q ceiling are instances of the roots of

`d(r+1-d)<=Q`.

The r=12 d4/d9 symmetry at base value36 is the specialization

`4*(13-4)=9*(13-9)=36`.

A genuine general-q theorem should therefore use the quadratic roots, not fixed d labels.

## 7. Symbolic anchor envelope

If a general anchor theorem proves

`K_r(H)>=f(r,h)`

for an anchor configuration of total local excess h, then

`e(H)>=[r(3r-1)+f(r,h)]/2`.

Therefore

> **`q <= E - C(r+2,2) - [r(3r-1)+f(r,h)]/2`.**

For r=12 and the proved near-anchor value `f(12,h<=3)=8`, the bracket equals

`91+214=305`.

Hence 305 is not fundamental: it is the r=12 evaluation of the symbolic backend base plus the anchor-excess floor.
