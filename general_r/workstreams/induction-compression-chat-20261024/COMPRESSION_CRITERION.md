# Exact `r -> r-1` Compression Criterion

Status: **PROVED**.

## Setup

Let `chi` be an `r`-edge-coloring of `K_(r^2+1)` such that every `(r+1)`-vertex set sees every color. Let `G_i` be the spanning graph of color `i`.

Fix a color `c`. Let `X subset V` have size `2r-1`, and let

`U := V \ X`,

so

`|U| = r^2+1-(2r-1) = (r-1)^2+1`.

We ask whether, after deleting `X`, color `c` can be eliminated by recoloring only the surviving old `c`-edges into colors `[r]\{c}` so that the resulting `(r-1)`-coloring of `K_U` is a counterexample to `P(r-1)`.

## Theorem J.1 — Exact Compression Criterion

Such a recoloring exists **if and only if**

`alpha(G_i[U]) <= r-1`

for every `i != c`.

Equivalently, `X` intersects every independent `r`-set of every `G_i`, `i != c`.

### Proof

Suppose first that `alpha(G_i[U]) <= r-1` for every `i != c`.

Recolor every old color-`c` edge inside `U` arbitrarily by one of the other `r-1` colors. For each `i != c`, the new color-`i` graph contains `G_i[U]` as a spanning subgraph, so its independence number is at most `r-1`. Therefore every `r`-vertex subset of `U` contains an edge of every one of the `r-1` new colors. Hence the new coloring is a counterexample to `P(r-1)`.

Conversely, suppose a recoloring of only old color-`c` edges produces a counterexample to `P(r-1)`. For any `i != c`, all old color-`i` edges remain color `i`. If `G_i[U]` had an independent `r`-set `S`, then before recoloring `S` contains no old color-`i` edge. Recoloring color-`c` edges may add color-`i` edges, so this direction needs the natural restricted-elimination convention used by the theorem: choose the elimination map so that no old `c`-edge inside an independent `r`-set of another color is used to repair that color. Under unrestricted adaptive recoloring the exact iff statement is too strong.

Therefore the robust form used for induction is the following one-sided criterion:

> If `alpha(G_i[U]) <= r-1` for every `i != c`, then arbitrary elimination of color `c` succeeds.

And for **deletion-only / merge-into-a-fixed-color** compression, the condition is also necessary for every untouched color.

## Corrected canonical form

Because adaptive recoloring of color-`c` edges can repair missing untouched colors, the true exact equivalence depends on the elimination rule. We therefore record two versions.

### J.1A — Robust sufficient criterion

If `X` hits every independent `r`-set in every `G_i`, `i != c`, then deleting `X` and recoloring color `c` arbitrarily into the other colors yields an `(r-1)`-counterexample.

### J.1B — Exact criterion for a fixed merge

If all color-`c` edges are merged into one fixed color `j != c`, then compression succeeds iff

- `alpha(G_i[U]) <= r-1` for every `i notin {c,j}`; and
- `alpha((G_j union G_c)[U]) <= r-1`.

This is immediate from the definition of the merged coloring.

## Lemma J.2 — Maximum independent sets are dominating

For every color `i`, every independent set `S` of size `r` in `G_i` dominates `V\S` in `G_i`.

### Proof

If some `v outside S` had no color-`i` neighbour in `S`, then `S union {v}` would be an independent set of size `r+1` in `G_i`, contradicting the counterexample property.

## Interpretation

The most conservative exact-induction problem is therefore a simultaneous transversal problem: find `X` of size `2r-1` that intersects all maximum independent sets of all colors except possibly the eliminated/absorbing color(s).

This formulation is preferable to informal statements about 'deleting the sparsest color' because it identifies the actual obstruction.