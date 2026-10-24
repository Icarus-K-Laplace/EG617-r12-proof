# Hub propagation: proved low-incidence lemma and obstruction

Date: 2026-10-24  
Branch: `workstream/general-r-design-terminal-20261024`

## Status summary

- **PROVED_ANALYTIC:** low-incidence off-hub propagation lemma below.
- **DISPROVED:** the naive local claim “every non-target nontransversal ideal block must meet the target hub set” does not follow from the one-color independence constraint and the scalar stability budgets alone.
- **OPEN:** full Hub Propagation Theorem under simultaneous edge-disjointness of all colors and the complete target-color contract.

All uses of the stability contract retain its exact hypotheses. In particular, `X` is the existing bounded target hub set; it is not silently enlarged to include non-target defects.

## HP1. Exact incidence bookkeeping

Fix a non-target color (i), and let its ideal clique partition be
[
Q_i=K(C_1)\cup\cdots\cup K(C_r).
]
The five target ideal groups are (B_1,\ldots,B_5). Define
[
d_i=\sum_{a=1}^r\bigl(|C_a|-|\{j:C_a\cap B_j\ne\varnothing\}|\bigr),
]
the total repeated-group incidence count. Also let
[
n_{ij}=|\{a:C_a\cap B_j\ne\varnothing\}|,\qquad
m_{ij}=r-n_{ij}.
]
Every (m_{ij}\ge0), and the exact identity is
[
\boxed{\sum_{j=1}^5m_{ij}=d_i-1.}
]
Indeed, the total number of distinct group incidences across the (r) blocks is (5r+1-d_i), so the total missing incidences relative to (5r) are (d_i-1). In particular, every non-target partition has (d_i\ge1).

## HP2. Low-incidence off-hub propagation lemma

**Theorem (HP-LI).** Assume (r\ge44) and the frozen terminal/stability contract. Suppose a non-target ideal block (C_a) contains distinct (u,v\in B_j\setminus X), and (uv\notin E(G_i)). Then either (d_i\ge6), or
[
\boxed{|E(G_i)\triangle E(Q_i)|\ge (6-d_i)(r-1).}
]
Consequently, at most 27 non-target colors can have a repeated-group pair outside (X) with (d_i\le5).

### Proof

Since both endpoints are outside (X), the target-side deletion-cover theorem says (uv\in E(G_0)). Thus (uv\notin E(G_i)) is a genuine target-colored pair inside the ideal block (C_a).

First (m_{ij}\ge1). Otherwise every ideal block contains a point of (B_j); choose (u,v) and one (B_j)-point from every other block. This is an ((r+1))-set with no color-(i) edge, contradicting (\alpha(G_i)\le r).

Since (\sum_k m_{ik}=d_i-1), at most (d_i-2) of the four labels (k\ne j) can be missing from any block. If (d_i\le5), at least (6-d_i) labels (k\ne j) occur in every one of the (r) blocks.

Fix such a label (k). For every block (C_b\ne C_a), choose a point (x_b\in C_b\cap B_k). The set
[
\{u,v\}\cup\{x_b:C_b\ne C_a\}
]
has size (r+1). All pairs among its (B_k)-points, and the pair (uv), are target-colored, so any color-(i) edge must join (u) or (v) to a selected (B_k)-point. Since the choice of (x_b) is arbitrary, **every** (B_k)-point in every other block must be adjacent in (G_i) to (u) or (v). There is at least one such edge for each of the (r-1) other blocks. These are all cross-block edges relative to (Q_i), hence each contributes one distinct unit to (E(G_i)\triangle E(Q_i)). Different labels (k) give disjoint edges. This proves the bound.

Summing over colors with such a pair gives
[
|I|(r-1)\le27r+15.
]
For (r\ge44), ((27r+15)/(r-1)<28), hence (|I|\le27). The weighted form is
[
\boxed{\sum_{i\in I}(6-d_i)\le27.}
]
No edge is double-counted: each charged edge has one endpoint in (C_a), the other in a different (Q_i)-block, and a unique target-group label for the second endpoint.

**Status: PROVED_ANALYTIC.**

## HP3. Why this does not yet prove full propagation

HP-LI leaves the high-incidence regime (d_i\ge6). The following exact local block-system audit shows why the current scalar bounds do not eliminate that regime.

### Explicit local obstruction, valid for every (r\ge8)

Take five labels (1,\ldots,5) and (r) ideal blocks:

- six blocks of size 6, each containing all five labels and one repeated label; duplicate counts are ((1,1,1,1,2));
- one singleton with label 1;
- one 4-block with labels (2,3,4,5);
- (r-8) size-5 transversals.

The five label classes then have sizes exactly
[
(r,r,r,r,r+1).
]
The partition has
[
\sum_C(|C|-5)^2=23,\quad d_i=6,\quad e(Q_i)=10r+16,
]
so its ideal-partition excess above (p_r(5r+1)=10r+5) is (11).

Define a single color graph (G_i) by taking every within-block pair whose labels differ, omitting the six repeated-label pairs, and adding all four edges between the singleton and the 4-block. Then
[
e(G_i)=10r+14,\quad s_i=9,\quad |E(G_i)\triangle E(Q_i)|=10.
]
Moreover (\alpha(G_i)\le r): a set of size (r+1) must double a block; the only possible non-edge within a block is a repeated-label pair in a 6-block, and such a set necessarily chooses one point from both the singleton and the 4-block, which are completely joined in (G_i).

All six repeated-label pairs can be placed on ordinary vertices outside the target hub set. This local pattern uses only constant defect and constant slack; it is compatible with the *numerical per-color bounds* (size energy, edit budget, repeated-pair budget, and (s_i\le8r+5) in aggregate for up to (\lfloor(8r+5)/9\rfloor) such colors).

This is **not** a full terminal coloring: the other colors, target cross-cover, and global pair-disjointness have not been completed. It is therefore not a counterexample to EG617 or to the full Hub Propagation Theorem. It is a counterexample to any proof that tries to derive full propagation from one-color independence plus scalar budgets alone.

## HP4. Exact remaining task

The global theorem must use an ingredient not yet extracted from the current stability inequalities:

> **High-incidence trap exclusion.** Show that a linear family of the above (d_i\ge6) local traps cannot be completed into pairwise edge-disjoint non-target color classes while satisfying the target (\alpha\le5), target (\omega\le r-1), target cross-cover, and the exact edge partition.

Alternatively, construct such a completion. This is the current sharp obstruction; it cannot be skipped by calling the (O(r)) defects “concentrated.”
