# Affine-Plane r^2 Construction Cannot Be Extended by One Vertex

Status: **PROVED_FOR_ALL_R for every r admitting the standard affine-plane construction**.

This theorem does not classify all colorings of K_(r^2). Its purpose is to identify a precise stability target around the known sharp-looking construction.

## 1. Standard construction

Assume an affine plane of order r exists. Its r^2 points are partitioned by each parallel class into r disjoint lines of size r, and any two lines from different parallel classes meet in exactly one point.

The Erdős–Gyárfás construction chooses r-1 parallel classes and assigns one class to each of colors `1,...,r-1`; the remaining two parallel classes are assigned to color r.

Thus for every color `i<r`, its color graph is exactly a disjoint union of r target cliques `K_r`, one for each line of its parallel class.

Every `(r+1)`-point set contains a monochromatic edge of every color.

## 2. Nonextension theorem

> **The standard affine-plane coloring on K_(r^2) cannot be extended to a coloring of K_(r^2+1) in which every `(r+1)`-set sees all r colors, for any r>=3.**

## 3. Proof

Add a hypothetical new vertex x.

Fix a color `i<r`. Its old color-i graph is the disjoint union of the r line-cliques in parallel class `P_i`.

Suppose every line of `P_i` contains at least one vertex v for which xv is not color i. Choosing one such non-i neighbour from each of the r lines produces r old vertices with no color-i edge among them. Together with x they form an `(r+1)`-set containing no color-i edge, contradiction.

Therefore for every `i<r` there exists a line

`L_i in P_i`

such that every edge from x to a vertex of L_i has color i.

Now choose distinct colors `i,j<r`; this is possible because r>=3.

The lines L_i and L_j belong to different parallel classes of the affine plane, so they meet in exactly one point v.

But then the single edge xv must simultaneously have color i and color j, impossible.

This proves nonextension.

## 4. Abstract two-partition version

The proof only needs two colors i,j whose old color graphs are disjoint unions of r K_r blocks and whose block partitions are cross-intersecting: every i-block meets every j-block.

Hence any K_(r^2) balanced coloring containing two such orthogonal clique partitions is nonextendable.

## 5. Stability target

A hypothetical counterexample on r^2+1 vertices restricts to a coloring of every r^2-subset in which every `(r+1)`-subset still sees all colors.

Therefore a high-leverage alternative to the pivot/backend programme is:

> prove that every such r^2 coloring, for sufficiently large r, contains two color classes which are exact or robustly close to orthogonal r-by-r clique partitions.

The present theorem then supplies the final exact nonextension contradiction.

This is compatible with Turán stability: each color graph has independence number at most r, so its complement is K_(r+1)-free and close-to-minimum color classes are close to complements of Turán graphs, i.e. unions of r cliques.
