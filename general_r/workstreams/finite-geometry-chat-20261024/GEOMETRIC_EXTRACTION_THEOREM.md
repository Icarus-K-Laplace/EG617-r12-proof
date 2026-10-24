# Geometric Extraction Theorem — Current Status

Status: **Conditional local extraction PROVED; global extraction OPEN**.

## Theorem K.G1 — Conditional two-direction extraction

Let a hypothetical counterexample to P(q) be given, with q>=3. Fix x and W=V\{x}. If two colors i,j have local slacks

\[
1\le s_i(x),s_j(x)\le q-2,
\]

then the q^2 points W carry two orthogonal partitions into q monochromatic K_q blocks. Each partition is a direction class in the abstract net sense, and every block in either class meets every block in the other in exactly one point.

For each color k in {i,j}, let E_k be its s_k cross-block defect edges. The extra vertex x determines a color label on every point of W. The non-k neighbors of x in each k-block form nonempty sets, and E_k must block every transversal choosing one such non-k neighbor from each of the q blocks. Moreover, some block has at most s_k non-k neighbors, so x is joined to at least q-s_k vertices of that block in color k.

This theorem is fully proved by LOW_SLACK_COORDINATIZATION.md and does not use q prime power.

## What is not proved

- No global theorem forces two colors to satisfy 1<=s_i(x),s_j(x)<=q-2 at a common vertex x.
- Two orthogonal partitions give a 2-net, not a full affine plane.
- A prime-power value of q does not give arbitrary extracted partitions field coordinates.
- The positive-slack transversal-blocking systems have not been shown incompatible.

## Exact route to a finite-geometry contradiction

A valid completion would need to prove one of:

1. at least three or more pairwise orthogonal direction classes, with the relevant block families explicitly identified;
2. a full affine-plane/net completion theorem whose hypotheses match the extracted incidence structure;
3. a direct contradiction from the defect edges and the extra-vertex color matrix, without completing a plane.

Only after proving that the shell contains full size-q blocks in distinct directions, with pairwise intersections at most one, may the partial Kakeya union bound be applied. The current local extraction theorem does not yet provide such a shell or three-direction family.
