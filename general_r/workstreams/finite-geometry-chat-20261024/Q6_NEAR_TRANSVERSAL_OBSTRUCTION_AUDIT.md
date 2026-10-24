# q=6 Case B — Near-Transversal Incidence Audit

Status: **The net-plus-clique-partition subkernel is realizable as a Latin-square incidence structure; this is not a full EG617 coloring.**

## Purpose

K.RM5 forces, for q=6 in Case B, three orthogonal 6-clique partitions (a 3-net / Latin square of order 6) and a partition into one 6-set plus six 5-sets, where the 6-set is a transversal and each 5-set is a near-transversal of all three directions.

It would be incorrect to try to rule out this incidence pattern by Euler–Tarry alone. The following explicit Latin square realizes exactly this subkernel.

## Explicit order-6 Latin square

\[
L=\begin{pmatrix}
0&1&2&3&4&5\\
1&0&3&2&5&4\\
2&3&4&5&0&1\\
3&2&5&4&1&0\\
4&5&0&1&3&2\\
5&4&1&0&2&3
\end{pmatrix}.
\]

The following label array partitions its 36 cells into seven disjoint sets. Label 0 is the full transversal; labels 1 through 6 are near-transversals of size 5.

\[
M=\begin{pmatrix}
0&6&5&2&1&3\\
3&4&0&1&5&2\\
6&5&3&0&2&4\\
1&2&4&6&0&5\\
4&1&6&5&3&0\\
2&0&1&3&4&6
\end{pmatrix}.
\]

## Direct checks

- Label 0 occurs six times, once in each row, column, and symbol class of L; hence it is a transversal.
- Each label k in {1,...,6} occurs exactly five times, with no repeated row, column, or L-symbol; hence it is a near-transversal.
- The seven label classes partition all 36 cells, since every cell has exactly one label.
- Each row and column of M contains 0 and five distinct nonzero labels. The same is true in each symbol class of L, because each near-transversal uses each L-symbol at most once.

Therefore the design-level subkernel “one transversal plus six disjoint near-transversals” is realizable even though L has no orthogonal mate.

## What this does and does not refute

This is an **abstract Latin-square incidence example**, not a full graph-level EG617 counterexample. It does not supply the three non-6-partite residual color graphs at b_i=5, their exceptional-star defects, the 14 witness roots, or the required edge colors between R and X.

The audit rules out only the overstrong claim that the 3-net plus the (6,5,5,5,5,5,5) partition is itself impossible. Any proof closing r=7 Case B must use the additional high-color exceptional-star constraints or the witness/root incidence conditions.


## Cross-line full-contract update

J branch commit c0c31e82b2bd8b4c3c5a7ab6092b660d16bd686b proves the root-block capacity theorem J.W8. It shows the full EG617 Case B cannot realize the residual equality profile at q=6: every one of the 14 roots would need to fully c-dominate one of seven c-clique blocks, but the block capacities total only 13. Combined with the Euler–Tarry bound, this closes Case B at r=7.

The explicit Latin square above remains a valid **abstract design-level realization** of the net/near-transversal subkernel. It is not a counterexample to J.W8 because it does not include the outside root vertices and their color-c neighborhood requirements.
