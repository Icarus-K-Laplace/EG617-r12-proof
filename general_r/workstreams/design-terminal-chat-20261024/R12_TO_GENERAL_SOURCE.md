# r=12 source archaeology for the general design-terminal branch

Status labels distinguish exact symbolic sources from fixed-r closure artifacts.

## Sources read

The reverse engineering used the canonical r=12 front-end bridge, T61 new lemmas, T61 h13 layer ledger, E401--E404 closure, E405 closure, and S30/S31 interface, together with the general-r structural-source and constant-dictionary files.

No E333--E408 backend casework is reused as a proof ingredient here.

## Structural chain

The r=12 outer stop is not a mysterious 61-point graph. It comes from the general anchor formula

`|R|=r^2-d-jr`.

At the terminal anchor `d=r-1` and block count `j=r-6`, this gives

`|R|=5r+1`.

For `r=12`, this is `61`, with six anchored `K12` blocks. The next packing level `j=r-5` gives `4r+1=49`.

The greedy independence bound `alpha(R)<=r-1-j` becomes 5 at the 61-stop and 4 at the 49-stop. Maximality gives `omega(R)<=r-1`, hence 11 at r=12.

## Exact general outer ledger

The r=12 number 408 is also structural:

`M_r - C(r,2) - (r-6)C(r,2) = 3r^2-2r`.

Thus the general ledger is

`e(R)+sigma+z+g+x+y=3r^2-2r`.

At r=12 this is exactly 408.

## Why the r=12 narrow edge window is not general

The general hereditary cap at `n=5r+1` is

`D_r(5r+1)=(5r^2+15r+10)/2`.

Hence the outer charge in (T-LEDGER) is at least

`(3r^2-2r)-D_r(5r+1)=(r^2-19r-10)/2`.

For `r>=20` this is positive and `Theta(r^2)`. Therefore the r=12 phenomenon in which the entire outer defect is at most 11 cannot persist asymptotically.

Similarly, the anchor budget alone gives

`delta(R)<=floor((6r^2-4r)/(5r+1))`.

Combining with contextual `delta(R)>=r` yields the r=12-style upper bound `delta<=r+1` only while

`r^2-15r-2<0`,

i.e. for integer `r<=15`. It is not an asymptotic theorem.

## Consequence for `z=0`

The r=12 proof of `z=0` spends the tiny outer charge `408-E<=11`. Since general outer charge is forced to be quadratic for `r>=20`, that argument cannot be promoted. Thus

> `z=0` / `N[v]=K_r` is tagged **DISPROVED_AS_GENERAL_PATTERN as a forced consequence of the same ledger**.

This does not assert that `z` must be positive in every future terminal; it says the r=12 forcing mechanism is intrinsically small-r.
