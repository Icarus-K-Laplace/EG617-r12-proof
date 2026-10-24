# Multicolor defect budget: exact accounting and what it does not buy

Date: 2026-10-24  
Scope: only the frozen `(5r+1)` terminal contract.

## 1. Frozen aggregate bounds

Write (W) for the terminal, (Q_0=\bigcup_{j=1}^5K(B_j)) for the target ideal partition, and (Q_i=\bigcup_{a=1}^rK(C_{ia})) for a non-target ideal partition. Under the existing stability theorem:
[
\sum_{i=0}^{r-1}|E(G_i[W])\triangle E(Q_i)|\le27r+15,
\qquad
\sum_{i=1}^{r-1}s_i\le8r+5.
]
For each non-target color let
[
d_i=\sum_a\bigl(|C_{ia}|-|\{j:C_{ia}\cap B_j\ne\varnothing\}|\bigr).
]
If (P_i) is the number of same-target-group pairs contained in all blocks of (Q_i), then
[
d_i\le P_i,\qquad \sum_iP_i\le27r+15,
]
because every such pair is also an edge of (Q_0), so each occurrence in a non-target ideal partition contributes one unit to ideal pair-multiplicity excess. Hence
[
\boxed{\sum_{i>0}d_i\le27r+15.}
]
This is a linear total budget, not a constant bound per color.

## 2. Exact per-color ledger

Let
- (\Delta_i=e(Q_i)-p_r(5r+1)\ge0) be the ideal block-size imbalance;
- (R_i=|E(Q_i)\setminus E(G_i)|) be deleted ideal edges;
- (A_i=|E(G_i)\setminus E(Q_i)|) be added cross-block edges.

Then the exact identity is
[
\boxed{s_i=\Delta_i-R_i+A_i.}
]
No term may be dropped: a target-colored edge inside a non-target ideal block contributes to (R_i); a target-deleted pair actually owned by color (i) does not.

The same-group pair count and (d_i) are not interchangeable: if a block contains three points of one target group, it contributes (2) to (d_i) but (3) same-group pairs to (P_i).

## 3. Low-incidence charge is rigorous

For a non-target ideal block containing a repeated-group pair (uv\subset B_j\setminus X), if (d_i\le5), the HP-LI lemma gives
[
|E(G_i)\triangle E(Q_i)|\ge(6-d_i)(r-1).
]
Therefore for (r\ge44), at most 27 colors can have such a low-incidence off-hub pair. This charge is edge-disjoint across the labels (k\ne j), and across colors the global symmetric-difference sum counts each color-edge separately, as required.

## 4. High-incidence pattern survives all scalar tests

The explicit local pattern in `HUB_PROPAGATION_THEOREM.md` has
[
d_i=6,\quad \Delta_i=11,\quad R_i=6,\quad A_i=4,\quad s_i=9,
]
[
|E(G_i)\triangle E(Q_i)|=10,\quad
\sum_C(|C|-5)^2=23,\quad
\#\text{nonclean blocks}=8.
]
Thus a family of (q) such local patterns obeys all the *scalar upper bounds* whenever
[
q\le\left\lfloor\frac{8r+5}{9}\right\rfloor
]
for the non-target slack, and the edit/energy/overlap bounds are looser still. This permits (q=\Theta(r)), not (O(1)).

Important qualification: this calculation does **not** construct (q) globally edge-disjoint color classes. Cross-color pair compatibility is exactly the missing condition. It shows that the current numerical budgets alone cannot prove bounded-hub propagation.

## 5. Budget route to pursue next

A valid global contradiction must combine the local high-incidence trap with at least one genuinely multicolor constraint:

1. each cross-group pair can be assigned to at most one actual color;
2. target cross edges needed to cover target internal deletions are unavailable to every non-target color;
3. a local trap's added edges must be chosen from the same global cross-pair universe as the (r^2-O(r)) clean transversal blocks;
4. target deleted edges are also a finite resource, and a target-deleted pair can be owned by only one actual color.

The needed theorem is not merely (\sum d_i=O(r)). It is a **pair-disjointness / completion inequality** showing that the high-incidence traps consume more cross-pair capacity or target-cover capacity than is available.

Status: the accounting identities are **PROVED_ANALYTIC**; the required completion inequality is **OPEN**.
