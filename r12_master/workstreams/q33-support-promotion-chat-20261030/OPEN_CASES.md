# Q33 support-promotion — exact remaining OPEN frontier

Status: OPEN / NOT_CERTIFIED.

## Aggregate support profile

With the KP-refined residual component core interval 10<=sum(c_i)<=12, the necessary U/W screen excludes:
- m=8: v=31..38;
- m=9: v=32..39;
- m=10: v=34..40.

The first aggregate survivors remain (8,39), (9,40), and (10,41). All larger v through47 remain feasible in this relaxation. These are aggregate cost-pair survivors, not labelled graph realizations.

## Common-gadget degree restriction

Every KP Type-I gadget vertex has minimum C-degree5. A nonexact color with 130/131/132 edges and alpha<=12 has minimum degree2/1/1. With the residual bound 60-d_F(z)<=47:
- m=9: a common core gadget vertex would have degree at least48, impossible; W_* is empty.
- m=10: a common core gadget vertex would have degree at least51, impossible; W_* is empty.
- m=8: the lower bound is46, so at most two common gadget-core vertices remain, each degree-saturated at46 or47.

Consequently the union of all component-core vertices is all47 core points for m=9,10. For m=8 it has size at least45.

## First-survivor W structures

- m=8,v=39: H[W]=4K2; eight exact-color 3-edge matchings partition K_{2,2,2,2}.
- m=9,v=40: H[W]=3K2 union K1; nine exact-color 2-edge matchings partition K_{2,2,2,1}.
- m=10,v=41: six-point W with at most three units of aggregate W slack.

## Next structural attack

For m=9,10, exploit that every one of the47 core vertices lies in an isolated component of at least one exact-129 color, while for each color the ten component cores and gadget core partition H. Label the two special K5 core subsets and exceptional vertex in every KP gadget, then couple these to pairwise linearity and the core degree/excess ledger.

For m=8, attack the saturated one/two-point common-gadget exception: exact-color degrees must all be5 and nonexact degrees all2, except for at most one extra degree unit per common point. Combine with the shell target-degree cap of at most2.

Q33 remains OPEN.
