# CHAT J — Induction / Compression in r

Branch: `workstream/general-r-induction-compression-20261024`

Scope: only parameter compression `r -> r-1` or `r-c`. Do not duplicate residual-core extraction or backend repivot work.

## Problem

Write `P(r)` for: every `r`-edge-coloring of `K_(r^2+1)` has an `(r+1)`-vertex set omitting at least one color.

A counterexample therefore has, for every color graph `G_i`,

`alpha(G_i) <= r`.

## Current status

**Level J1 reached.** We have an exact criterion for when a counterexample at parameter `r` can be compressed to parameter `r-1` by deleting exactly `2r-1` vertices and eliminating one color.

The criterion turns exact induction into a simultaneous transversal problem for maximum independent sets of `r-1` color graphs.

A sharp-model obstruction is also proved: in the standard affine-plane lower-bound coloring on `r^2` vertices, a shell of size `2r-1` is far too small to lower the independence number of all but one of the exact parallel-class colors once `r>=5`. Hence any successful induction theorem must exploit the extra `r^2+1`st vertex or additional counterexample structure; purely hereditary deletion from an affine-like `r^2` core cannot work.

## Main proved statements

1. **Exact Compression Criterion.** Fix a color `c`. For `X subset V`, `|X|=2r-1`, put `U=V\X`. There exists a recoloring of only the old `c`-edges on `U` into the other `r-1` colors that yields a counterexample to `P(r-1)` iff

   `alpha(G_i[U]) <= r-1` for every `i != c`.

   Equivalently, `X` hits every independent `r`-set in every `G_i`, `i != c`.

2. **Dominating maximum independent sets.** Every independent `r`-set in any color graph `G_i` of an `r`-counterexample dominates all outside vertices in `G_i`.

3. **Affine sharp-model obstruction.** In the standard affine-plane coloring of `K_(r^2)`, reducing the independence number of one exact parallel-class color from `r` to `r-1` requires deleting an entire line of that parallel class. For `t` distinct exact parallel classes, any common deletion set therefore contains one line from each class and has size at least

   `tr - C(t,2)`.

   If the eliminated color is the exceptional double-direction color, then `t=r-1` and this lower bound is `(r-1)(r+2)/2 > 2r-1` for every `r>=4`.

   Even if one exact-class color is eliminated, `t=r-2` gives `(r-2)(r+3)/2 > 2r-1` for every `r>=5`.

## Consequence for strategy

The arithmetic identity

`r^2+1-(2r-1)=(r-1)^2+1`

is exact but not by itself a mechanism. The load-bearing object is a `2r-1`-vertex **simultaneous maximum-independent-set transversal** across `r-1` color graphs.

The next target is to use the extra-vertex constraints of a genuine `K_(r^2+1)` counterexample to force such a transversal, or else prove that failure of such a transversal forces affine/design-like structure that is already nonextendable.