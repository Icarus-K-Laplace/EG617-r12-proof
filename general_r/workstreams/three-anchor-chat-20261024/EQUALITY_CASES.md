# Equality and near-equality cases

The parity lemma removes the entire apparent `K=7` layer: every `K_r` is even, so a counterexample has `K<=6`.

## c=2
No equality layer survives. The degree-2 tripartite transversal-cover proof closes the geometry for every `r>=12`.

## c=3
For `r>=14`, all focus/nonfocus inequalities are strict enough to force `K>=8`.

At `r=13`, the only mixed-focus arithmetic boundary under `K<=6` is one focused pair connector and one nonfocused pair connector with

- connector excess `6`;
- connector-degree `0`;
- a `(2,2)` nonneighbour rectangle;
- every other vertex exact.

The triple connector would then have to see all eleven vertices of the opposite zero-deficit block, impossible.

At `r=12`, both-nonfocus and both-focus branches are impossible. In the mixed-focus branch the effective rectangle is `R22`. The low-budget layers reduce to:

- `gamma=1`: uniquely `(k,a,b)=(6,2,2)`;
- `gamma=0`: either `a+b+k=9`, so the nonfocused connector has no neighbour in the opposite 10-block, or the single `(6,2,2)` layer with exactly one such neighbour.

Every layer contains a saturated rectangle vertex. That vertex forces the triple connector or the focused connector to cover all/almost all of the opposite 10-clique, producing a forbidden 12-clique or an impossible degree count. Hence no `r=12` equality survives.

## c=4, deficits (0,0,2)
For `r>=13`, the previous boundary classification remains valid:

- `r=16`: a single nonfocused connector can attain local cost six, but two required nonfocused connectors cannot coexist;
- `r=15`: adjacency forces connector excess `k=6` on each required nonfocused connector;
- `r=14`: the only overlap escape is an identical `(10,1)` rectangle, whose short-block vertex is saturated and cannot meet the focused pair;
- `r=13`: cross-group equality forces `(k,a,b)=(3,4,2)` and is incompatible with required focus; the same-group branch is killed after focus reduces the short-block effective capacity to two.

At `r=12`, let `f` be the number of connectors focused on the size-8 block.

- `f=0`: additive `R24` charges close unless both same-group pairs are adjacent. In that last arithmetic layer every connector would have to realize the unique `gamma=1`, `k=3`, `(a,b)=(4,2)` local equality, already contributing total connector excess 12.
- `f=1`: the three nonfocused connectors have effective `R23` charge at least `3+gamma`; additivity forces at least 9.
- `f=2`: the two nonfocused connectors must be an adjacent same-group pair. Under `K<=6`, the only overlap skeletons are identical `R22` rectangles of orientation `(1,8)` or `(8,1)`, with both connectors exact and all six excess units on one exclusive vertex.

The `(1,8)` skeleton creates an independent 4-set. The `(8,1)` skeleton makes a common-nonneighbour clique demand at least nine cross-neighbours from an exact rectangle vertex. Thus the equality set is empty.

## c=4, deficits (0,1,1)
For `r>=13`, no two connectors can focus on the same deficit-1 block and all earlier boundary layers are closed.

At `r=12`, classify by the number `s` of occupied focus slots among the two size-9 deficit-1 blocks.

- `s=0`: the two `(0,1)` rectangles add to at least 8.
- `s=1`: an additive `R23/R22` pair costs at least 7.
- `s=2`: every focus-owner pattern except `V` owning one block and `W` the other costs at least 9. In the remaining pattern the two type-U connectors are nonfocused. If nonadjacent their supports are disjoint and cost at least 8; if adjacent, the only `K<=6` overlap skeletons are again identical `(1,8)` or `(8,1)` `R22` rectangles with all six excess units on one exclusive vertex.

Each orientation gives an independent 4-set using one exact focused connector, one exact type-U connector, the saturated six-excess vertex, and a suitable vertex of the size-10 block. Hence no equality survives.

## Final equality status

For every `r>=12`, there are **no surviving `K=0,2,4,6` configurations** in any of the four exact-anchor geometries.

Therefore the Exact Three-Anchor Excess Theorem is closed analytically on the full stated range, with no separate fixed-`r=12` residue.


---

# Round 2 — Exact \(K=8\) layer (separate from the frozen \(K\le6\) closure)

## Proved rigidity

The new analytic boundary result is
\[
K=8\implies r\le13,\qquad\text{hence }K\ge10\text{ for }r\ge14.
\]
This does not follow from the old \(K\le6\) proof alone; it uses new equality-layer analysis.

- \(c=2\): \(r\ge13\) is excluded at \(K=8\). At \(r=13\), equality in the transversal-cover count forces \(E_1=E_2=2,E_3=11\), complete \(E_1-E_2\) adjacency, no positive exclusive excess, and an impossible degree requirement for the second connector. The \(r=12\) layer remains open.
- \(c=3\): both-focused and both-nonfocused branches are excluded. Mixed-focus \(r=14\) has 23 exact local profiles of cost at most eight; all are eliminated by common-nonneighbour cliques and saturated rectangle vertices. \(r=15\) has one local profile and is eliminated by a clique of size 15; \(r\ge16\) is excluded by the charge threshold. Mixed-focus \(r=12,13\) remain open.
- \(c=4,(0,0,2)\): \(f=0\) and \(f=1\) are excluded for \(r\ge13\). The \(f=2\) branch is excluded for \(r\ge13\) by local profile and external-incidence counting, and for \(r\ge14\) independently by the overlap bound plus saturation. Only \(r=12\) remains, with \(f=0\) and a same-group adjacency, \(f=1\), or \(f=2\).
- \(c=4,(0,1,1)\): \(s=0,1\) are excluded. The \(s=2\) owner patterns reduce to \(V/W\) owning both deficit-one focus slots. The \(r=14\) equality is excluded by the opposite size-12 block's external-incidence requirement; \(r=12,13\) remain open.

## Exact remaining necessary strata

| Geometry | Remaining \(K=8\) layer |
|---|---|
| \(c=2,(0,0,0)\) | \(r=12\), empty-part exceptional layer or nonempty \((1,2)/(2,2)\) transversal-cover layer |
| \(c=3,(0,0,1)\) | \(r=12,13\), mixed-focus only |
| \(c=4,(0,0,2)\) | \(r=12,f=0\) with same-group adjacency; \(r=12,f=1\); \(r=12,f=2\) |
| \(c=4,(0,1,1)\) | \(r=12,13,s=2\), \(V/W\) own both deficit-one focus slots |

These are necessary-condition strata, not known realizable graphs. No \(K=8\) graph has been constructed, and the classification is still OPEN. See EQUALITY_K8_CLASSIFICATION.md for the proofs and exact equality constraints.
