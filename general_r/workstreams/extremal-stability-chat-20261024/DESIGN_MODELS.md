# Design Models

## Model A — affine plane skeleton

Point set `V`, `|V|=r^2`.

Parallel classes `P_1,...,P_r,Q`, each consisting of `r` disjoint blocks/lines of size `r`.

Axioms used by this workstream:

1. each `P_i` and `Q` partitions `V`;
2. a block from one class and a block from a different class meet in exactly one point;
3. every pair of points belongs to exactly one line among all `r+1` classes.

No field arithmetic is used in the nonextension theorem.

## Model B — r-net skeleton

Keep only `P_1,...,P_r` and forget `Q`.

Pairwise orthogonality means every block from `P_i` meets every block from `P_j` in exactly one point for `i!=j`.

Equivalently, after choosing two classes as rows and columns, the remaining `r-2` classes encode `r-2` mutually orthogonal Latin squares of order `r`.

The classical deficiency-one completion theorem says this structure has a unique final parallel class `Q`, yielding an affine plane. This imported theorem should be cited explicitly whenever arbitrary-r completion is used.

## Model C — coloring supported on the skeleton

Each color `i` contains every edge internal to every `P_i` block. Edges on the final class `Q` may be colored arbitrarily.

Important: a color graph need not equal a disjoint union of its `P_i` cliques. It may contain many extra `Q`-edges. Therefore arguments that require a color graph to be **exactly** a union of cliques do not automatically apply to the full sharp family.

## Model D — grid for one color

Fix color `i`. Orthogonal classes `(P_i,Q)` identify the points with cells of an `r x r` grid:

- `P_i` lines = rows;
- `Q` lines = columns.

Every permutation matrix (one point from each row and each column) is automatically independent in color `i`, regardless of the arbitrary coloring of `Q`-edges, because any edge between two selected points lies in some other base class `P_j`.

This grid observation is the key to the new nonextension theorem.

## Matching-preclusion lemma

Let `F` be a set of cells in an `r x r` grid meeting every permutation matrix. Then `|F|>=r`.

If `r>=3` and `|F|=r`, then `F` is exactly one full row or one full column.

Proof: view cells as edges of `K_{r,r}`. If deleting `F` destroys every perfect matching, Hall gives a set of `s` left vertices whose remaining neighborhood has size at most `s-1`. Thus `F` contains all edges from those `s` left vertices to at least `r-s+1` right vertices, so

`|F| >= s(r-s+1) >= r`.

For `1<s<r`, the inequality is strict when `r>=3`; equality occurs only at `s=1` (a row-star) or `s=r` (a column-star).
