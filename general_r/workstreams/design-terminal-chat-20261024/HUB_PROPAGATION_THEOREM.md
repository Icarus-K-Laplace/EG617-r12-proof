# Hub propagation: conditional cylinder lemma and K6 audit

Date: 2026-10-24  
Branch: `workstream/general-r-design-terminal-20261024`

## Status summary

- **PROVED_ANALYTIC:** exact repeated-incidence bookkeeping.
- **PROVED_CONDITIONAL:** a linear edit charge when a repeated-group pair has a full ordinary same-group transversal core.
- **PROVED_ANALYTIC:** the target condition (\alpha(G_0)\le5) makes every non-target color graph (G_i) (K_6)-free; hence a full star from one vertex to a clean 5-clique block is forbidden.
- **DISPROVED:** the earlier unconditional claim that (d_i\le5) alone forces Ω(r) non-target edits. A target-deleted hub edge can be used in a one-block cylinder cover at constant cost if the target-α constraint is ignored.
- **OPEN:** full Hub Propagation under simultaneous target-α, target cross-cover, edge-disjointness, and all inherited density caps.

The earlier (d_i=6) local pattern was also withdrawn as a valid one-color counterexample: it has multiple missing within-block pairs, and an independent set can double two such pairs while omitting the special cover block. Do not use that pattern as a proof obstruction.

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

## HP2. Conditional ordinary-label cylinder lemma

**Lemma.** Suppose (u,v\in B_j\setminus X) lie in the same ideal block (C_a), (uv\notin E(G_i)), and there is a label (k\ne j) such that every other block (C_b\ne C_a) contains a point of (B_k\setminus X). Then
[
\boxed{|E(G_i)\triangle E(Q_i)|\ge r-1.}
]
If (c) labels (k\ne j) satisfy this condition, the bound is (c(r-1)).

**Proof.** For each other block choose any (x_b\in C_b\cap(B_k\setminus X)). All selected (B_k\setminus X) pairs are target-colored, because every target internal deletion touches (X); (uv) is also target-colored. The ((r+1))-set consisting of (u,v) and one such point from each other block must contain a color-(i) edge. The only possible such edges join (u) or (v) to a selected (B_k\setminus X) point. Since the choice in each block is arbitrary, every ordinary (B_k)-point in every other block must be adjacent in (G_i) to (u) or (v). These are (r-1) distinct cross-block edits relative to (Q_i). Different labels charge disjoint edges. **Status: PROVED_CONDITIONAL.**

The condition that every block has an **ordinary** (B_k)-point is essential. It does not follow from (d_i\le5): a bounded hub may be the only (B_k)-point in a block.

## HP3. One-block cover: what works locally and what fails globally

Take a balanced ideal partition with one 6-block (C_a) containing (u,v\in B_j) as its repeated-group pair and (r-1) 5-transversals. Then (d_i=1) and (e(Q_i)=p_r(5r+1)=10r+5).

Choose another transversal block (C_b=\{w,x_2,x_3,x_4,x_5\}), where (w\in B_j\cap X) and (x_k\in B_k) for (k\ne j). Suppose (uw) is a target-deleted edge owned by color (i). Define a local graph (G_i) by deleting (uv) from (Q_i) and adding the five edges from (u) to all vertices of (C_b). Then
[
d_i=1,\quad \Delta_i=0,\quad R_i=1,\quad A_i=5,\quad s_i=4,
\quad |E(G_i)\triangle E(Q_i)|=6.
]
Also (\alpha(G_i)\le r): the only missing pair inside any ideal block is (uv), and any ((r+1))-set using it must select one point from (C_b), all of which are adjacent to (u).

However, this does **not** satisfy the full terminal contract: (u\cup C_b) is a (K_6) in (G_i), so it is an independent 6-set in the target graph (G_0), contradicting (\alpha(G_0)\le5). This example therefore only disproves an attempted propagation lemma based on (G_i)'s independence and scalar budgets alone. It is **not** a terminal counterexample.

## HP4. Joint target/non-target cylinder lemma

**Lemma (K6 exclusion).** Under the full terminal contract, every non-target (G_i) is (K_6)-free. In particular, if (C) is a 5-point ideal block inducing a clique in (G_i), no outside vertex (u) can be adjacent in (G_i) to all five vertices of (C).

**Proof.** Otherwise (C\cup\{u\}) is a (K_6) in (G_i), hence an independent 6-set in (G_0), contrary to (\alpha(G_0)\le5). **Status: PROVED_ANALYTIC.**

This forces every one-block star cover of a missing pair to create at least one further defect inside the cover block. If the cover block is a clean 5-transversal, the defect is a target cross edge (or another non-target edge mismatch); that new missing pair must itself be protected against an independent transversal. This is a genuine propagation mechanism, but the current work has not proved that the resulting chain/cycle of defects exceeds the (O(r)) budget.

## HP5. Exact remaining task

Prove a **joint cylinder-cover propagation theorem**: starting from a repeated-group pair outside (X), every cover of all transversal choices by non-target edges must either
1. force a (K_6) in a non-target color;
2. create a new target/non-target defect whose own cover continues the chain; or
3. spend enough globally distinct cross-pair capacity to exceed the exact budget.

The target cross-cover and non-target cover must be counted together; the same pair cannot be charged twice. No complete propagation or nonextension theorem is claimed.


## HP6. Exact two-defect local closure: a counterexample to naive propagation

The claim “a cheap cylinder cover must create a further defect” is false at the abstract one-color block level. Here is an exact finite gadget.

Let (r\ge3). Let the ideal partition (Q_i) have one 6-block
[
C=\{u,v,z_1,z_2,z_3,z_4\},
]
one 5-block
[
D=\{w,x,y_1,y_2,y_3\},
]
and (r-2) further 5-clique blocks. In the actual graph (G_i):
- (C) is complete except for (uv);
- (D) is complete except for (wx);
- all other blocks remain cliques;
- the only cross-block edges are
[
uw, vx, uy_1, uy_2, uy_3, z_1w, z_2w, z_3x, z_4x.
]

Then:
1. every vertex of (D) is adjacent to (u) or (v), so an independent transversal doubling (C) at (uv) is blocked;
2. every vertex of (C) is adjacent to (w) or (x), so an independent transversal doubling (D) at (wx) is blocked;
3. if an independent set doubles both blocks, it contains (u,v,w,x), and the edges (uw) and (vx) block it;
4. therefore (\alpha(G_i)\le r);
5. (G_i) is (K_6)-free: (C) has only the two 5-cliques (C\setminus\{u\}) and (C\setminus\{v\}), no vertex of (D) is adjacent to either full 5-clique, and common neighborhoods of pairs from (D) in (C) have size at most one. No other block has cross edges.

The ideal edge count is (p_r(5r+1)=10r+5). Exactly two ideal edges are deleted and nine cross-block edges are added, so
[
R_i=2,\quad A_i=9,\quad s_i=A_i-R_i=7,
\quad |E(G_i)\triangle E(Q_i)|=11.
]
This gadget closes two defects with slack (7), without creating a third missing edge inside (C\) or (D). It disproves any local lemma claiming that α\((G_i)\le r) and (K_6)-freeness alone force indefinite defect propagation or a per-color slack cost (>8).

**Important limitation:** the gadget is not a full terminal coloring and has not been assigned target-group labels. It may fail the target cross-star and pair-ownership constraints; those are now the essential global conditions.

## HP7. Target-label obstruction to using the same two-block gadget

Suppose (w\in B_j), (x\in B_k), (j\ne k), and the target cross correction contains the full star (wB_k\subseteq E(G_0)). Let (D\in Q_i) contain (w,x), and let (C\in Q_i) be a candidate cover block. Write (z_k\in C\cap B_k).

If (z_k\notin X), then:
- (wz_k\in E(G_0)), by the target star;
- (xz_k\in E(G_0)), because it is an internal (B_k)-edge and all target internal deletions touch (X).

Thus neither (wz_k) nor (xz_k) can be a (G_i)-edge. Consequently, a cover using only edges between (C) and (D) cannot block the transversal choice (z_k) unless (z_k\in X). If (z_k\notin X), the proof must use edges involving other selected blocks.

This is a rigorous target-label obstruction, but it does not alone force the cover block to contain a hub: a multi-block transversal barrier can cover the choices with (z_k) fixed.

### Cheap multi-block barrier audit

For a fixed vertex (z), two clean 5-clique blocks (E,F), and nonneighbors (e\in E,f\in F), the following 9-edge pattern blocks every choice from (E\times F):
- join (z) to the other four vertices of (E);
- join (z) to the other four vertices of (F);
- add the edge (ef).

Every pair chosen from (E,F) either includes a neighbor of (z), or is exactly ((e,f)) and uses the edge (ef). The pattern is (K_6)-free locally: (z) has only four neighbors in either 5-clique, and there is only one edge between (E,F).

Therefore, after a target-label obstruction, a second-coordinate barrier can cost only 9 edges locally; it is not automatically quadratic. A valid global proof must show that such barriers cannot be chained/overlapped compatibly across all colors under the (27r+15) total edit budget and exact pair ownership.


## HP8. Destination-injectivity theorem for the exact hub-star model

This is a **conditional symbolic theorem** for an exact hub-star model, not yet a theorem that every terminal lies in that regime. The exactness matters: assume that every target cross-group edge is contained in the specified hub stars (no additional target cross edges between ordinary vertices or to other groups from these hubs). An (O(r))-edge perturbation of this model is not covered by the lemma.

Assume five target groups (B_1,\ldots,B_5). For each group (j), suppose there is a hub (a_j\in B_j) with an internal target nonneighbor (y_j\in B_j) and a full target cross-star
[
a_jB_{f(j)}\subseteq E(G_0),\qquad f(j)\ne j.
]
Assume also (a_jy_j\notin E(G_0)). If (alpha(G_0)\le5), then
[
\boxed{f:\{1,\ldots,5\}\to\{1,\ldots,5\}\text{ is a derangement permutation}.}
]

**Proof.** If (f(j)=f(k)=\ell) for distinct (j,k), then (\ell\notin\{j,k\}). Choose one ordinary point from each of the two remaining groups outside ({j,k,\ell}). Together with
[
a_j,y_j,a_k,y_k
]
these give six points. The only possible within-group pairs (a_jy_j,a_ky_k) are target nonedges; the two hub stars point to the omitted group (B_\ell); and all other chosen points are ordinary, so no target cross-star is incident to them. This is a target-independent 6-set, contradiction. Thus (f) is injective; on five groups it is a permutation, and (f(j)\ne j) makes it a derangement. **Status: PROVED_CONDITIONAL.**

### Extra hub in the oversized group

Suppose (B_h) has a second hub (b_h\ne a_h), with an internal target nonneighbor and a full target star (b_hB_g\subseteq E(G_0)). The same argument shows
[
\boxed{g=f(h).}
]
Indeed, if (g\ne f(h)), the permutation (f) has some (j\ne h) with (f(j)=g), and the two internal nonedges in groups (h,j) plus one point from each of the two groups outside ({h,j,g}) give an omitted-color 6-set.

This is a useful restriction: the two hubs in the oversized group must have the **same destination group**, while the five group-level destinations form a derangement. The proof relies on the exact hub-star model; extra target cross edges may block the witness six-set and require a stability/exceptional-edge version.

## HP9. Triangle obstruction for co-locating the two oversized-group hubs

Let (a_h,b_h\in B_h) be the two hubs, with (a_hb_h\in E(G_0)), and suppose both target-star to (B_k), where (k=f(h)). If a non-target ideal block (C\in Q_i) contains (a_h,b_h) and its (B_k)-representative (x_k), then all three pairs
[
a_hb_h,quad a_hx_k,quad b_hx_k
]
are target-colored and absent from (G_i). Thus the missing-edge graph (Q_i[C]\setminus G_i[C]) contains a triangle, and ({a_h,b_h,x_k}) is independent in (G_i[C]).

If all cross-block additions of (G_i) are incident to a single cover block (D), this is impossible: omit (D) and choose one vertex from each of the other (r-2) blocks to obtain an independent ((r+1))-set. Hence in this regime the two hubs cannot share a block that also contains the destination-group representative. They must either:
- lie in different ideal blocks; or
- share a nontransversal block omitting (B_k), while the extra-point constraint forces another defective block.

Status: **PROVED_CONDITIONAL**. Without the single-cover-block hypothesis, a multi-block barrier could still block the independent triple; its cost remains open.


## HP10. Robust pair-of-nonedges coverage inequality

This lemma permits arbitrary additional target cross edges, but it is conditional on the four endpoints of the two internal nonedges having no target-colored cross edge between the source groups.

Let (P_j=\{a_j,y_j\}\subset B_j) and (P_k=\{a_k,y_k\}\subset B_k), (j\ne k), be two internal target nonedges. Assume all four cross pairs between (P_j) and (P_k) are absent from (G_0). For each remaining group (ell\notin\{j,k\}), define the common ordinary-safe set
[
U_\ell=B_\ell\setminus\bigl(N_{G_0}(a_j)\cup N_{G_0}(y_j)\cup N_{G_0}(a_k)\cup N_{G_0}(y_k)\bigr).
]
Let (A=e_{G_0}(W;B_1,\ldots,B_5)) be the total number of target cross-group edges. Then for any two distinct remaining groups (ell,m),
[
\boxed{|U_\ell|\,|U_m|\le A.}
]

**Proof.** If the product exceeded (A), there would be more than (A) pairs in (U_\ell\times U_m), while only (A) target cross edges exist in total. Hence some (x\in U_\ell,y\in U_m) satisfy (xy\notin E(G_0)). By the definitions of the (U)-sets, neither (x) nor (y) has a target edge to any of the four endpoints in (P_j\cup P_k); the four cross pairs between (P_j,P_k) are also target nonedges by hypothesis. Thus
[
P_j\cup P_k\cup\{x,y\}
]
is a target-independent 6-set, contradiction.

Consequently, among the three groups outside ({j,k}), at most one can have (|U_\ell|>\sqrt A). At least two groups are therefore covered up to at most (\sqrt A) exceptional points by the target neighborhoods of the four endpoints.

Since (A\le27r+15), the exceptional threshold is (O(\sqrt r)). This is a genuine robust statement, but the condition that the two source nonedges have no target-colored cross edge between their endpoints is not yet guaranteed for a useful family of pairs. The missing next step is to either find many such compatible pairs or charge the endpoint-conflict edges to the global (O(r)) budget.


## HP11. Withdrawn shortcut: target internal deletions are not (O(1))

The attempted shortcut “(|X|=O(1)) and (alpha(G_0)\le5) imply (D=O(1))” is **DISPROVED as a proof step**. It incorrectly treated five vertices in (B_j\setminus X), which form a clique, as an independent set.

A hub can have (Theta(r)) nonneighbors inside its ordinary target clique without violating the target independence cap. The clique cap (omega(G_0)\le r-1) limits its number of neighbors in that clique to at most (r-2), but this is not an (O(1)) bound on missing edges.

The valid surviving lower bound is: some (B_h) has size at least (r+1), and every non-target color must own an edge inside a fixed ((r+1))-subset of (B_h). By unique color ownership,
[
D_h:=\left|\binom{B_h}{2}\setminus E(G_0)\right|\ge r-1.
]
This is compatible with the current (O(r)) budget. The claimed (r\ge6212) terminal closure is withdrawn; full terminal nonextension and multi-block cover accounting remain **OPEN**. See `JOINT_DEFECT_PROPAGATION.md` for the correction audit.
