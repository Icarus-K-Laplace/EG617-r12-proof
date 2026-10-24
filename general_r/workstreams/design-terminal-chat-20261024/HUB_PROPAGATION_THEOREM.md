# Hub propagation: conditional core lemma and explicit hub-assisted obstruction

Date: 2026-10-24  
Branch: `workstream/general-r-design-terminal-20261024`

## Status summary

- **PROVED_ANALYTIC:** exact repeated-incidence bookkeeping.
- **PROVED_CONDITIONAL:** a linear edit charge when a repeated-group pair has a full ordinary same-group transversal core.
- **DISPROVED:** the earlier unconditional low-incidence claim that (d_i\le5) forces Ω(r) edits for every off-hub repeated pair. A single target-deleted edge incident to a hub can participate in a constant-size non-target cylinder cover.
- **OPEN:** full Hub Propagation under simultaneous edge-disjointness, target cross-cover, and all inherited density caps.

The counterexample below is a local one-color block system, **not** a full terminal coloring. It identifies the missing global interaction rather than disproving EG617.

## HP1. Exact incidence bookkeeping

Let (Q_i=\bigcup_{a=1}^rK(C_a)) be a non-target ideal partition, and let (B_1,\ldots,B_5) be the target ideal groups. Define
[
d_i=\sum_{a=1}^r\bigl(|C_a|-|\{j:C_a\cap B_j\ne\varnothing\}|\bigr),
\qquad
m_{ij}=r-|\{a:C_a\cap B_j\ne\varnothing\}|.
]
Then every (m_{ij}\ge0) and
[
\boxed{\sum_{j=1}^5m_{ij}=d_i-1.}
]
This follows because the total number of distinct group incidences across the (r) blocks is (5r+1-d_i). In particular (d_i\ge1).

## HP2. Conditional core-complete label lemma

**Lemma (ordinary-label cylinder charge).** Suppose (u,v\in B_j\setminus X) lie in the same ideal block (C_a), (uv\notin E(G_i)), and there is a label (k\ne j) such that every other block (C_b\ne C_a) contains a point of (B_k\setminus X). Then
[
\boxed{|E(G_i)\triangle E(Q_i)|\ge r-1.}
]
If (c) labels (k\ne j) satisfy this condition, the bound is (c(r-1)).

**Proof.** For each other block choose any (x_b\in C_b\cap(B_k\setminus X)). All selected (B_k\setminus X) pairs are target-colored, because every target internal deletion touches (X); (uv) is also target-colored. The ((r+1))-set consisting of (u,v) and one such point from each other block must contain a color-(i) edge. The only possible such edges join (u) or (v) to a selected (B_k\setminus X) point. Since the choice in each block is arbitrary, every ordinary (B_k)-point in every other block must be adjacent in (G_i) to (u) or (v). These are (r-1) distinct cross-block edits relative to (Q_i). Different labels charge disjoint edges. **Status: PROVED_CONDITIONAL.**

The condition that every block has an **ordinary** (B_k)-point is essential; (d_i\le5) alone does not imply it.

## HP3. Explicit obstruction to unconditional propagation

Take (r\ge6), target groups of sizes ((r,r,r,r,r+1)), and an ideal partition (Q_i) with one 6-block (C_a) containing (u,v\in B_j) as its repeated-group pair, and (r-1) size-5 transversals. Thus (Q_i) has exactly (r) blocks, (d_i=1), and
[
e(Q_i)=p_r(5r+1)=10r+5.
]

Choose another transversal block (C_b) containing a point (w\in B_j\cap X), and denote its other four points by (x_k\in B_k), (k\ne j). Assume the internal target edge (uw) is deleted from the actual target graph and owned by color (i). Define (G_i) by:
- retaining all ideal edges except (uv);
- adding the five edges from (u) to every vertex of (C_b), namely (uw) and the four (ux_k).

Then (uv) is target-colored, (uw) is a target-deleted edge incident to the hub (w), and
[
d_i=1,\quad \Delta_i=0,\quad R_i=1,\quad A_i=5,\quad s_i=4,
\quad |E(G_i)\triangle E(Q_i)|=6.
]
Also (\alpha(G_i)\le r): an independent set of size (r+1) must use the only non-edge (uv) inside (C_a) and one vertex from every other block; but the selected vertex from (C_b) is always adjacent to (u).

Therefore an off-hub repeated pair can be supported by **constant** non-target edit/slack when a target-deleted hub edge participates in a one-block cylinder cover. This disproves the proposed inference
[
d_i\le5\text{ and an off-hub repeated pair}
\;\Longrightarrow\;
\Omega(r)\text{ non-target edits}
]
under the local assumptions alone.

This is not a full terminal counterexample: the target cross-cover for the deleted pair (uw), the remaining colors, and global pair-ownership are not completed. Those global conditions are precisely what may rule the pattern out.

## HP4. Second high-incidence obstruction

The separate (d_i=6) local pattern remains a useful scalar-budget audit: six 6-blocks, one singleton, one 4-block, and (r-8) 5-transversals; group sizes ((r,r,r,r,r+1)); six repeated-group pairs; four added edges between the singleton (label 1) and the 4-block (labels 2,3,4,5). It has
[
\Delta_i=11,\quad R_i=6,\quad A_i=4,\quad s_i=9,
\quad |E(G_i)\triangle E(Q_i)|=10,\quad
\sum_C(|C|-5)^2=23,
]
and (\alpha(G_i)\le r). Again, this is only a local one-color system, not a globally completed terminal.

## HP5. Exact remaining task

The hub propagation theorem must couple the non-target cylinder cover to the **target** cylinder cover. In particular, for each target-deleted edge (uw) used by a non-target trap, the target-color edges needed to cover every tuple from the other four groups cannot be counted as though the five edges (uC_b) were still available to the target color.

The current missing theorem is a **joint two-color cylinder-cover inequality**: a target deletion and a non-target cover block cannot simultaneously cover the same transversal product without exceeding the combined target/non-target edge budget or producing an omitted-color ((r+1))-set. No such inequality is proved yet.
