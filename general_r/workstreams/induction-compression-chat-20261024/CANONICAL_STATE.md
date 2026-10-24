# CHAT J — Induction / Compression in r

Branch: `workstream/general-r-induction-compression-20261024`

Scope: only parameter compression `r -> r-1` or `r-c`. Do not duplicate residual-core extraction or backend repivot work.

## Problem

Write `P(r)` for: every `r`-edge-coloring of `K_(r^2+1)` has an `(r+1)`-vertex set omitting at least one color.

A counterexample therefore has, for every color graph `G_i`,

`alpha(G_i) <= r`.

## Current status

**Level J1 reached.** The exact arithmetic deletion size is understood, and the first rigorous compression criteria/obstructions are proved.

The initial candidate iff criterion was audited and found too strong under fully adaptive recoloring: old edges of the eliminated color can be recolored to repair another color on an `r`-set. The canonical statements are therefore the corrected forms below.

A sharp-model obstruction is also proved: in the standard affine-plane lower-bound coloring on `r^2` vertices, a shell of size `2r-1` is far too small to lower the independence number of all but one of the exact parallel-class colors once `r>=5`. Hence any successful induction theorem must exploit the extra `r^2+1`st vertex or additional counterexample structure; purely hereditary deletion from an affine-like `r^2` core cannot work.

## Main proved statements

1. **Robust Compression Criterion.** Fix a color `c`. For `X subset V`, `|X|=2r-1`, put `U=V\X`. If

   `alpha(G_i[U]) <= r-1` for every `i != c`,

   then color `c` may be eliminated and its surviving edges recolored arbitrarily among the other `r-1` colors; the resulting coloring of `K_U`, where `|U|=(r-1)^2+1`, is a counterexample to `P(r-1)`.

   Equivalently, it is sufficient that `X` hit every independent `r`-set in every untouched color graph.

2. **Exact fixed-merge criterion.** If all color-`c` edges are merged into one fixed color `j`, compression succeeds iff

   - `alpha(G_i[U]) <= r-1` for all `i notin {c,j}`; and
   - `alpha((G_j union G_c)[U]) <= r-1`.

3. **Dominating maximum independent sets.** Every independent `r`-set in any color graph `G_i` of an `r`-counterexample dominates all outside vertices in `G_i`.

4. **Affine sharp-model obstruction.** In the standard affine-plane coloring of `K_(r^2)`, reducing the independence number of one exact parallel-class color from `r` to `r-1` requires deleting an entire line of that parallel class. For `t` distinct exact parallel classes, any common deletion set therefore contains one line from each class and has size at least

   `tr - C(t,2)`.

   If the eliminated color is the exceptional double-direction color, then `t=r-1` and this lower bound is `(r-1)(r+2)/2 > 2r-1` for every `r>=4`.

   Even if one exact-class color is eliminated, `t=r-2` gives `(r-2)(r+3)/2 > 2r-1` for every `r>=5`.

## Consequence for strategy

The arithmetic identity

`r^2+1-(2r-1)=(r-1)^2+1`

is exact but not by itself a mechanism. A conservative route to induction is a `2r-1`-vertex simultaneous transversal for maximum independent sets of the untouched colors. The affine model shows that such a transversal cannot come from a generic hereditary argument on an `r^2` core.

The next target is therefore a dichotomy:

> either the extra-vertex constraints of a genuine `K_(r^2+1)` counterexample force a compressible shell / fixed merge, or failure of all such shells forces an affine/design-like state that is itself nonextendable.