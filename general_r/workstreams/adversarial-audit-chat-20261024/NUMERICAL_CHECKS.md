# Numerical and Symbolic Boundary Checks

## N-001 — Chat B AES threshold

Check:

`2r-9 > 5(3r-1)/8`.

Multiply by 8:

`16r-72 > 15r-5`

so

`r>67`.

Smallest integer threshold: **68**.

## N-002 — Chat A triangle-free AES threshold

Check:

`r-1 > 2(2r)/5 = 4r/5`.

Equivalent to

`r>5`.

Smallest integer threshold: **6**.

## N-003 — F matching-preclusion equality

Hall obstruction with `s` left vertices requires deletion of at least

`f_r(s)=s(r-s+1)`

cells.

Subtract r:

`f_r(s)-r=(s-1)(r-s)`.

Hence `f_r(s)>=r` for `1<=s<=r`, with equality exactly `s=1` or `s=r`; for `1<s<r` it is strict. These are exactly the full-row and full-column equality blockers.

## N-004 — F leftover-edge count

One affine parallel class has

`r*C(r,2)=r^2(r-1)/2`

edges.

A roughly balanced assignment of these edges among r colors differs from any all-one-color assignment on at least

`r^2(r-1)/2 - ceil(r(r-1)/2)`

edges, which is `Theta(r^3)`.

## N-005 — no SAT/ILP certificate yet

Round G-001 was analytic. No SAT/ILP/nauty witness has yet been produced for the open three-anchor range or the d2 plateau. Any later computational negative/positive result must be stored with a canonical encoding and independent verifier before promotion.
