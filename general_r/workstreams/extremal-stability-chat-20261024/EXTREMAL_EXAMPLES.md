# Extremal Examples and Sharpness

## 1. Problem translation

A balanced `r`-coloring is a partition

`E(K_n)=C_1 disjoint_union ... disjoint_union C_r`

such that `alpha(C_i)<=r` for every color `i`.

For `n=r^2`, Turan gives the per-color lower bound

`e(C_i)>=m_0 := r*C(r,2)=r^2(r-1)/2`.

The total edge count is

`C(r^2,2)=(r+1)m_0`.

Thus the total excess over the one-parallel-class minimum is exactly `m_0`:

`sum_i (e(C_i)-m_0)=m_0`.

This identity alone does not force the standard `(m_0,...,m_0,2m_0)` distribution.

## 2. Affine-plane skeleton family — exact construction

Assume an affine plane of order `r` exists. Let its parallel classes be

`P_1,...,P_r,Q`.

Each class is a partition of the `r^2` points into `r` lines of size `r`; every pair of points lies on a unique line and hence in a unique parallel class.

Construction:

1. For each `i in [r]`, every edge within a line of `P_i` receives color `i`.
2. Every remaining edge lies within a line of `Q`.
3. Assign each `Q`-edge an arbitrary color in `[r]`, independently of all other `Q`-edges.

For each color `i`, the graph `C_i` contains all `r` cliques from `P_i`. Therefore any `r+1` vertices contain two points on one `P_i`-line, so they contain color `i`. This holds simultaneously for all colors.

Hence every assignment in step 3 is a balanced coloring of `K_{r^2}`.

The original Erdős--Gyárfás construction is the special case in which all `Q`-edges receive one fixed color.

## 3. Size and flexibility

One parallel class contains

`m_0=r*C(r,2)=r^2(r-1)/2`

edges. Therefore the skeleton supports `r^{m_0}` labeled leftover assignments.

If the `Q`-edges are distributed approximately evenly among the colors, the resulting coloring differs from every “single-heavy-color” standard assignment on `Theta(r^3)` edges. Thus any stability conjecture stated as `O(r)` or `o(r^2)` **edge recolorings to one standard coloring** is false.

The invariant structure is instead:

- `r` orthogonal partitions `P_i`;
- one missing parallel class `Q`;
- arbitrary color labels on `Q`-edges.

## 4. Perfect-sector converse target

Suppose a balanced coloring of `K_{r^2}` has, for every color `i`, a spanning clique partition into at most `r` color-`i` cliques. Pairwise edge-disjointness implies that the partitions are pairwise orthogonal. Since there are `r^2` points, each partition must have exactly `r` blocks and every pair of blocks from distinct partitions meets in exactly one point; all blocks have size `r`.

Thus the `r` partitions form an `r`-net of order `r`. By the classical deficiency-one completion theorem for nets / equivalently the unique extension of `r-2` MOLS to a complete set, this net completes to an affine plane by adding one parallel class `Q`.

Under that imported classical theorem, the perfect sector is exactly the affine-skeleton family above: all edges already lying in a `P_i` block are forced to color `i`, and the only unforced pairs are the `Q`-edges.

This converse is useful structurally, but the all-r Problem 617 proof still needs to show that a hypothetical counterexample enters this perfect sector.

## 5. Non-prime-power warning

Prime powers supply affine planes and therefore sharp `K_{r^2}` examples. This explains the “infinitely many r” sharpness statement in the original paper.

Do **not** assume the existence of an affine plane for arbitrary composite `r`. In particular orders 6 and 10 are impossible, while the general non-prime-power existence problem is not settled by a universal theorem.

Also do not infer that `K_{r^2}` is unbalanced whenever no affine plane exists: balanced colorings outside the clique-partition/net sector are logically possible and must be treated separately.
