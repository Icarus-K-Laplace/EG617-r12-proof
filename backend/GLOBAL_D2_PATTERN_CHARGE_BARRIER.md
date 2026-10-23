# Global d=2 Pattern Charge Barrier

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_D2_ONE_LOSS_PATTERN_CAPACITY.md`;
- common-S row closure;
- `alpha(H)<=3`.

Purpose: provide the d=2 analogue of `GLOBAL_D3_PATTERN_CHARGE_BARRIERS.md` and turn the final three-class common-hub equality pattern into a scalar total-charge obstruction.

## 1. Setup

Let H be an n-vertex core with

`alpha(H)<=3`.

Work in a d=2 exact one-loss common-S pattern family.

Suppose the common-hub family has exactly three distinct support classes

`D_i={x,u_i}`, `i=1,2,3`,

where, by `GLOBAL_D2_ONE_LOSS_PATTERN_CAPACITY.md`,

- the common hub x has `w_x=0`;
- each D_i is a target K2;
- every private leaf u_i has `w_(u_i)=1`;
- the three private leaves are pairwise target-nonadjacent.

Write

`W=sum_(v in H) w_v`.

## 2. Every outside core vertex has positive charge

Take

`v in H\{x,u_1,u_2,u_3}`.

Suppose v were target-nonadjacent to all three leaves.

Since the leaves are pairwise target-nonadjacent,

`{v,u_1,u_2,u_3}`

would be an independent4-set in H, contradicting `alpha(H)<=3`.

Therefore v is target-adjacent to at least one private leaf, say u_i.

Because v lies outside support

`D_i={x,u_i}`, 

common-S row closure gives

`e_H(v,D_i)<=w_v`.

The edge `v u_i` is already one target edge into D_i. Hence

> `w_v>=1`.                                                   (D1)

## 3. Total charge barrier

The three private leaves contribute exactly3 units of charge.

The common hub contributes0.

There are

`n-4`

vertices outside the four-point pattern, and each has charge at least1 by (D1).

Therefore

> **d2 three-class charge barrier**
>
> `W>=3+(n-4)=n-1`.                                         (D2)

For the r=12 35-core:

> **`W>=34`.**                                                (D3)

Thus any 35-core common-S d2 one-loss subsystem with

`W<=33`

cannot contain three distinct common-hub support classes.

## 4. Equality rigidity

If equality holds in (D2), then every outside vertex has charge exactly1.

Moreover every outside vertex must meet the independent leaf triple `{u_1,u_2,u_3}` in at least one target edge, and row closure limits its adjacency to each support D_i by exactly its unit charge.

Hence equality produces a global three-leaf covering geometry rather than arbitrary residual structure.

This is the correct object to combine with hereditary packing or core-excess concentration if the numerical boundary W=n-1 is actually attained.

## 5. E334 q32/core211 interaction

`GLOBAL_COMMON_S_CHARGE_LOCALIZATION.md` gives, in the source-reported q32/core211 channel,

`W<=K+q+C(2,2)=2+32+1=35`.

Therefore a three-class d2 one-loss equality pattern in that channel is confined to the two-value window

> `W in {34,35}`.                                             (D4)

All lower-charge states have at most two distinct common-hub support classes.

This replaces a broad geometry by a narrow scalar equality frontier.

## 6. Generalization

The proof of (D2) uses only

- three pairwise target-nonadjacent private leaves;
- row closure;
- `alpha(H)<=3`.

Thus the same covering argument applies in any analogous residual core and yields the symbolic lower bound W>=n-1.