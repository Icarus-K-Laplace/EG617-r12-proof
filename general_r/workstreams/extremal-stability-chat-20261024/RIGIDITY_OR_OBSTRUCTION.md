# Rigidity-or-Obstruction — F-004

## Target theorem (OPEN)

For every sufficiently large r, a hypothetical balanced coloring of K_(r^2+1) should yield either:
(A) enough exact orthogonal partitions to invoke the frozen affine-skeleton nonextension theorem; or
(B) a direct (r+1)-vertex set omitting a color.
No r_0 is currently proved.

## Proved subtheorem R/O-1: low-slack linear rigidity

For each color i with s_i<=r^2/100,
**d_i>=31r/40**.
Füredi partitions H_i into r parts of sizes at least 4r/5 with at most r^2/50 missing cross-edges. Since A_i hits every K_r of H_i, weighted transversal hitting yields d_i>=4r/5-(r^2/50)/(4r/5)=31r/40.

This is a genuine local rigidity theorem, but the global slack average does not guarantee any color in this low-slack layer.

## Proved subtheorem R/O-2: scalar tradeoff

For d_i<r, SLACK_NEIGHBORHOOD_TRADEOFF.md gives an explicit F_r(d_i) with s_i>=F_r(d_i), combining Brouwer, the d_i=2 equality audit, and weighted transversal hitting.

The scalar integer program has feasible optimum d_i=r and s_i=binom(r,2) for all i. Thus the two sum identities and one-color inequalities do not close the theorem.

## Missing graph-level constraint

The disjoint sets A_i must simultaneously hit all K_r's of H_i, and every old edge has exactly one color. The scalar vector (s_i,d_i) and an intersection-collision matrix do not encode this simultaneous incidence system.

A successful next theorem must charge defects across colors, or classify the incidence kernel when all d_i are close to r. No such theorem is claimed here.

## Status

- Low-slack linear rigidity: PROVED_CONDITIONAL.
- Scalar joint slack–degree inequality: PROVED_CONDITIONAL.
- Rigidity-or-direct-obstruction dichotomy: OPEN.
- All-large-r theorem: OPEN.


## Proved subtheorem R/O-3 — extreme-neighborhood exclusion

For every color i,
\[
d_i\le r^2-\left\lceil\frac{3r^2-5r+2}{2r}\right\rceil.
\]
This follows by summing the coarse Brouwer lower bound \(s_j\ge C+2r-1-rd_j\) over all colors \(j\ne i\) and using the exact global slack budget. Separately, the within-\(A_i\) color-richness condition gives \(d_i\le r(r-1)\). For r>=5 the global bound is stronger.

This excludes a single neighborhood containing all but fewer than roughly \(1.5r\) vertices, but does not constrain the central degree regime near r.
