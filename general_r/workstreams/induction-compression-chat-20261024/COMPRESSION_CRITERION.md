# Exact r-to-(r-1) Compression Criterion

Status: **PROVED, with the adaptive-recoloring distinction explicit**.

## Setup

Let a hypothetical counterexample to P(r) be an r-edge-coloring of K_(r^2+1). Let G_i be its color graphs. Then every G_i satisfies alpha(G_i)<=r and omega(G_i)<=r.

Choose colors c,j with c != j, a shell X of size 2r-1, and U=V\X, so |U|=(r-1)^2+1.

## Theorem J.1A — Robust sufficient criterion

If

\[
\alpha(G_i[U])\le r-1 \qquad\text{for every }i\ne c,
\]

then deleting X and recoloring every surviving old c-edge arbitrarily into the other r-1 colors produces a counterexample to P(r-1).

Proof: each new color-i graph contains G_i[U] for every i != c, so its independence number remains at most r-1. Thus every r-set in U contains every one of the r-1 colors.

Equivalently, X must hit every independent r-set in every untouched color graph. This is a **sufficient** criterion for unrestricted adaptive recoloring; it is not claimed to be necessary.

## Theorem J.1B — Exact criterion for a fixed merge

If every old c-edge in U is recolored to one fixed color j, then the merge succeeds if and only if both conditions hold:

- alpha(G_i[U]) <= r-1 for every i not in {c,j};
- alpha((G_c union G_j)[U]) <= r-1.

The first family of colors is untouched. The merged color-j graph contains exactly the old c- and j-edges, so an r-set misses merged color j exactly when it is independent in both G_c and G_j.

## Hypergraph form

Let I_i be the r-uniform hypergraph whose edges are the independent r-sets of G_i.

- Robust compression after eliminating c succeeds whenever X is a transversal of the union of I_i over i != c.
- The fixed merge c -> j succeeds exactly when X is a transversal of

\[
\left(\bigcup_{i\notin\{c,j\}} I_i\right)\cup(I_c\cap I_j).
\]

Here I_c intersect I_j denotes the family of r-sets independent in both color graphs.

This formulation cleanly separates the two legal compression rules.

## Lemma J.2 — Maximum independent r-sets dominate

If S is an independent r-set in G_i, every vertex v outside S has at least one color-i edge to S. Otherwise S union {v} would be an independent (r+1)-set, contrary to the counterexample property.

## Audit warning

An unrestricted recoloring can add color-i edges to an old independent r-set of G_i, thereby repairing that set. Consequently, the robust condition above must not be promoted to an iff for adaptive recoloring. The exact iff statement in this file is only for the specified fixed merge.
