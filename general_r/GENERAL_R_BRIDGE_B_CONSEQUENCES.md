# General-r Consequences of Bridge B

Status: **PARTLY PROVED_SYMBOLIC, partly CONDITIONAL on the general near-anchor theorem and common-S contract**.

This file records only consequences that can be derived symbolically from the r=12 Bridge B package. It does not claim complete Bridge B closure.

## 1. Exact transported-excess identity is all-r

For a common-S owner y with support D_y and for `z in H\D_y`, define

`w_z=kappa_z+e_F(z,S)`.

The repivoted core excess is exactly

> **`kappa'_z=w_z-e_H(z,D_y)`.**

For `s in S`,

> **`kappa'_s=sigma_s-e_F(s,D_y)`.**

These identities are structural and independent of r once the symbolic common-S contract is in force.

## 2. General missing-pair count

Let H_y have order `3r-1`, minimum degree at least r, and let u,v be nonadjacent vertices with total new excess

`rho=kappa'_u+kappa'_v`.

If `c_uv=|N(u) intersect N(v)|`, then the number X of common non-neighbours of u,v outside the pair is

> **`|X|=r-3-rho+c_uv`.**

For r=12 this is `9-rho+c_uv`.

If `K_r(H_y)<=6`, at most `6-rho` vertices outside the pair have positive excess. Therefore X contains at least

`r-9+c_uv`

zero-excess vertices.

Hence for every r>=12 and rho<=3, there are at least three zero-excess common non-neighbours before any further exclusions. Conditional on the general near-anchor theorem, this gives the same low-charge absorption mechanism as in r=12.

## 3. Direct forcing makes numerical absorption global

If the general direct near-anchor theorem and the general near-anchor excess theorem are both available, every legal core satisfies

`K_r>=8`.

Then every legal owner core already satisfies the strengthened q envelope. Therefore a last line of the form

`q_y<=q_max`

is only numerical absorption, not graph nonexistence. A genuine Bridge B closure must still prove strict incompatibility or strict potential improvement at equality/positive loss.

This conceptual warning is all-r.

## 4. First d2 positive-loss concentration is r=12-only

Consider the symbolic analogue of the first r=12 d2 concentration state:

- support size d=2;
- missing-set edge count b=1;
- original core excess `K_r=8`;
- allowance `a=3`;
- positive loss `ell_y=1`;
- every owner in a nontrivial subfamily has no old outside zero;
- at least two distinct supports occur.

For d=2,

`beta=d(r+1-d)=2(r-1)`

and the exact charge sum is

`W=K_r+beta+a+b=8+2(r-1)+3+1=2r+10`.

Simultaneous no-outside-zero forces all old zeros into the intersection of the distinct d2 supports. Since two distinct 2-sets intersect in at most one point, there is at most one old zero. Therefore all but at most one of the `3r-1` core vertices have positive integer charge, so

`W>=3r-2`.

Combining:

`2r+10>=3r-2`,

hence

> **`r<=12`.**

Therefore:

> **For every r>=13, the first d2 positive-loss concentration state is impossible outright.**

At r=12 equality holds:

`W=34=3r-2`,

forcing exactly one zero and charge one on every other vertex, which explains the rigid `0,1^34` profile found in the fixed-r Bridge B package.

Thus that profile is a genuine small-r boundary artifact, not part of the asymptotic obstruction.

## 5. Consequence under strengthened q ceiling

If the general near-anchor theorem gives `K_r>=8`, then at the maximum residual layer

`q<=3r-1`.

For d=3,

`d(r+1-d)=3(r-2)`,

so the common-S allowance satisfies

`a<=5-B<=5`.

Hence every d3 common-S owner for every r>=12 lies in a fixed bounded allowance window. In particular:

- the b=2 sector is entirely within the low-charge `a<=5` window;
- the b=1 sector is absorbed through a<=4;
- only the single symbolic boundary `b=1,a=5` can escape the pair-excess<=3 test.

Thus the r=12 d3 high-slack frontier does not grow with r; it collapses to one fixed equality pattern in the general problem as well.

## 6. Remaining all-r Bridge B obligation

After the direct near-anchor forcing theorem, Bridge B should no longer be formulated as a broad extraction theorem. Its genuinely reusable target is narrower:

> **Positive-Loss Equality Incompatibility.** Under the strengthened q ceiling, show that every d2 or d3 common-S equality/positive-loss state either strictly improves a symbolic repivot potential or violates the direct near-anchor equality structure.

For r>=13 the first d2 concentrated equality is already gone, and d3 leaves only the bounded b=1,a=5 boundary. This is a substantial asymptotic simplification.
