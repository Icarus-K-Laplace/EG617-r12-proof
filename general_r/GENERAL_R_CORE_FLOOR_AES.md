# General-r Core Floor from Andrasfai–Erdos–Sos

Status: **PROVED_SYMBOLIC CONDITIONAL ON THE GENERAL RESIDUAL-CORE CONTRACT**.

This theorem is genuinely uniform in r. It does not assume any r=12 edge floor.

## Contract

Let r>=12 and let H be a graph on

`n=3r-1`

vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- `delta(H)>=r`.

Define

`K_r(H)=sum_v(d_H(v)-r)=2e(H)-r(3r-1)`.

Because `r(3r-1)` is always even, K_r(H) is an even nonnegative integer.

## Theorem

> **`K_r(H)>=2`.**
>
> Equivalently
>
> `e(H) >= [r(3r-1)+2]/2`.

For r=12 this gives `e(H)>=211`.

## Proof

Assume `K_r(H)=0`. Since every degree is at least r, H is r-regular.

Let `L=bar(H)`. Then

- `|L|=3r-1`;
- L is `(2r-2)`-regular;
- `omega(L)<=3` because `alpha(H)<=3`, so L is K4-free;
- `alpha(L)<=r-1` because `omega(H)<=r-1`.

For r>=12,

`2r-2 > 5(3r-1)/8`

because this inequality is equivalent to `r>11`.

The Andrasfai–Erdos–Sos theorem for K4-free graphs therefore forces L to be 3-partite.

One part has size at least

`ceil((3r-1)/3)=r`.

That part is independent in L, contradicting `alpha(L)<=r-1`.

Hence `K_r(H)!=0`. Since K_r(H) is an even nonnegative integer, `K_r(H)>=2`.

## Interpretation

The r=12 constant CORE211 is not an isolated numerical phenomenon. It is the first value r for which the AES threshold inequality is strict:

`2r-2 > 5(3r-1)/8`.

Thus the symbolic baseline core floor is

`E_core(r) := [r(3r-1)+2]/2`

for every r>=12, provided the general residual-core contract supplies `delta(H)>=r`, `alpha(H)<=3`, and `omega(H)<=r-1`.

The unresolved generalization is therefore upstream: prove the residual-core minimum-degree source uniformly in r.
