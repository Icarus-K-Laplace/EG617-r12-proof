# Affine Sharp-Model Obstruction to Naive Exact Induction

Status: **PROVED as a model obstruction; not itself a counterexample to `P(r)`**.

## Setup

Assume an affine plane of order `r` exists. On its `r^2` points, consider the standard lower-bound coloring used in the general-r architecture: `r-1` colors are single parallel classes, and the last color is the union of the remaining two parallel classes.

For a single-class color `i`, its graph is exactly a disjoint union of `r` cliques `K_r`, namely the lines of one parallel class.

## Lemma J.3 — Killing one unit of independence requires deleting a whole line

Let `G_i` be such a single-class color graph and let `X` be any deletion set. Then

`alpha(G_i[V\X]) <= r-1`

iff `X` contains every vertex of at least one line in the parallel class of color `i`.

### Proof

The connected components of `G_i` are the `r` line-cliques. An independent set can choose one vertex from each nonempty component, so the independence number of the induced graph after deletion equals the number of line-cliques not completely deleted. This is at most `r-1` exactly when at least one whole line was deleted.

## Lemma J.4 — Multi-direction deletion lower bound

Suppose `t` distinct single-class colors must all have their independence number lowered from `r` to at most `r-1`. Then any deletion set `X` contains one full line from each of `t` distinct parallel classes. Since two lines from distinct parallel classes intersect in at most one point,

`|X| >= tr - C(t,2)`.

This follows from the first two terms of inclusion-exclusion.

## Corollary J.5 — A `2r-1` shell cannot generically compress the affine model

If the eliminated color is the exceptional double-direction color, then all `t=r-1` exact single-class colors must survive. Hence

`|X| >= r(r-1)-C(r-1,2) = (r-1)(r+2)/2`.

For every `r>=4`,

`(r-1)(r+2)/2 > 2r-1`.

If instead one single-class color is eliminated, then at least the other `t=r-2` single-class colors must survive, so

`|X| >= r(r-2)-C(r-2,2) = (r-2)(r+3)/2`.

For every `r>=5`,

`(r-2)(r+3)/2 > 2r-1`.

Therefore the exact arithmetic shell size

`2r-1 = (r^2+1)-((r-1)^2+1)`

is not sufficient for any compression argument that merely deletes vertices from an affine-like `r^2` core and tries to lower all untouched color independence numbers by one.

## Strategic meaning

This does **not** refute a theorem `counterexample(r) => counterexample(r-1)`, because the affine-plane coloring is only the sharp lower-bound model on `r^2` vertices and is known to be nonextendable to `r^2+1`.

It does show that any successful induction must use the extra vertex in an essential way. Failure of a `2r-1` simultaneous transversal should be treated as evidence for design-like structure, not as a reason to keep searching for a purely hereditary shell lemma.

## Finite-geometry connection

Choosing one full line from many distinct directions is a partial Kakeya/Besicovitch configuration. Thus quantitative lower bounds for finite-plane Kakeya sets are directly relevant to proving that affine-like states resist small-shell compression.