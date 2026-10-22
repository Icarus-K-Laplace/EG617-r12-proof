# E406 d=3 Type-A: no H-vertex is full to all four support rows

Status: `PROVED`. This applies to every surviving Type-A d3 platform, not only O=4.

Let H be the 35-point remainder in the four-triangle compression. We use

- `e(H) in {151,152}`;
- `alpha(H)<=4` (inherited from the 47-point core);
- the saturated Type-A identities from `E406_D3_REMAINDER_SATURATION.md`.

## 1. H has minimum degree at least3

Suppose `v in H` has `d_H(v)<=2`. Its H-nonneighbourhood U has at least32 vertices.

If H[U] contained an independent4-set, those four vertices together with v would form an independent5-set in the 47-point core, contradicting `alpha(C)<=4`. Hence

`alpha(H[U])<=3`.

Equivalently, the complement of H[U] is K4-free. By Turan,

`e(H[U]) >= C(32,2)-ex(32,K4)
          = 496-floor(32^2/3)
          = 496-341
          = 155`.

But `e(H)<=152`, contradiction.

Therefore

`delta(H)>=3`.      (H-MIN3)

## 2. Type-A core excess on a single H-vertex is at most2

There are two saturated Type-A regimes.

### Defect d=1

The exact saturation identity is

`eps_x+s_D(x)=1`

for every H-vertex. Hence `eps_x<=1`.

This includes the eta=1 branch and the eta=0,xi=1 branch.

### Defect d=0

Here

`h_x=eps_x+s_D(x)-1>=0`

and

`sum_H h_x=1`.

Thus each `h_x<=1`, so

`eps_x+s_D(x)<=2`,

hence `eps_x<=2`.

Therefore every Type-A survivor satisfies

`eps_x<=2` for every x in H.      (EPS2)

## 3. Four-full vertices are impossible

Assume x is full to all four support triangles. Then x has exactly12 support-triangle neighbours and no partial support incidence. Since

`d_C(x)=12+eps_x`,

its H-degree is

`d_H(x)=eps_x`.

By (EPS2), `d_H(x)<=2`, contradicting (H-MIN3).

Hence no Type-A d3 survivor contains a vertex full to all four support rows.

## 4. O=4 consequence

The possible membership-increment partitions of `O=4` are

- `1+1+1+1`: four doubles;
- `2+1+1`: one triple plus two doubles;
- `2+2`: two triples;
- `3+1`: one four-full plus one double.

The last multiplicity type is now impossible.

Thus every modern Type-A O4 survivor belongs to one of only three multiplicity types:

`four doubles`, `one triple + two doubles`, `two triples`.