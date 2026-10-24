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
