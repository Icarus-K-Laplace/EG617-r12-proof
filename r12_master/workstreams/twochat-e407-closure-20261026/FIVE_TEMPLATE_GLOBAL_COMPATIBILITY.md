# E407 Q32 — five-template global compatibility

Date: 2026-10-27  
Status: **OPEN / NOT_CERTIFIED. Current file is the canonical same-core compatibility snapshot.**

## 1. Shared object

For each of the five alternative V12 shell templates A–E, a legal completion must use the same type of 47-vertex core H and the same exact E407 Q32 support contract:

- |H|=47, e(H)=284, alpha(H)<=4, omega(H)<=11, delta(H)>=12;
- total H degree excess four;
- U subset H, |U|=29, W=H\U, |W|=18;
- 49 independent support blocks Q, seven per exact-129 color, disjoint within color and pairwise linear across colors;
- exact support ledger recorded in CANONICAL_STATE.md.

The templates are **alternative shell states**, not simultaneous shell graphs.

Write A=S disjoint-union B with |S|=3, |B|=10, B a target clique, M=bar(F[A]), D_a=N_F(a) cap H, t_a=|D_a|, and k_b=|N_M(b) cap S|.

## 2. Audited V12 shell rows

| Template | S-row sizes | M[S] | retained high-k floor |
|---|---|---|---:|
| A | (12,10,10) | empty | at least 6 B rows with k=3 |
| B | (11,11,10) | empty | at least 8 B rows with k>=2 |
| C | (12,11,10) | one edge | at least 6 B rows with k=3 |
| D | (11,11,11) | one edge | at least 7 B rows of the two allowed pair-types or k=3 |
| E | (12,11,11) | P3 | at least 5 B rows with k>=2 |

The exact V12 inequalities, not this abbreviated table, remain the source of template exhaustiveness.

## 3. Selected support components are now genuinely labelled

For every exact-129 color c, the seven support blocks are the four-core-vertex parts of seven selected isolated color-c K5 components. Their seven anchors are distinct vertices of {p} union A.

Let b_c be the number of selected B anchors. The new exact factor argument gives

\[
\boxed{b_c\in\{5,6,7\}.}
\]

If b_c=5, the selected anchors are p, one S label, and five B labels. Hence every exact color has at most one selected S anchor.

Across all seven exact colors:

- at least 35 selected blocks are B-anchored;
- at most 7 are S-anchored.

This supersedes the old live lower bound b_c>=3. The old b=3 and b=4 residual branches are empty.

## 4. Template consequences on the actual selected 49 blocks

If h is the number of B labels with k_b>=2, a selected B-anchor set of size at least five meets the high-k set in at least h-5 labels. Therefore:

| Template | selected high-k blocks per exact color | seven-color floor |
|---|---:|---:|
| A | >=1 k=3 | >=7 |
| B | >=3 k>=2 | >=21 |
| C | >=1 k=3 | >=7 |
| D | >=2 high-k | >=14 |
| E | no positive floor from cardinality alone | 0 |

A/C selected k=3 blocks are hub-complete by the missing-hub lemma. B/D selected high-k blocks meet at least two S rows. These are constraints on the **actual selected support-block family**, not merely on auxiliary no-S component witnesses.

The older exact-129 component-packing theorem remains useful separately: each exact color has at least six B-labelled no-S K5 components, and the A/C conditional hub-complete component floor uses the registered row-transversal theorem and R(3,35) exclusion. The two families are not conflated beyond identities that have actually been proved.

## 5. Per-color shell-edge localization

For every exact color c,
\[
\boxed{e_c(M[A\setminus A_c^{sel}])\ge2.}
\]

Reason: after deleting the seven selected K5 components, the exact color factor is 3K5+G11 on the 26 residual vertices. Every unselected K5 must contain an outside-core label, and the residual factor/alpha-two gadget forces at least two color-c shell edges in all three pivot-location cases.

The seven exact colors therefore use at least 14 distinct shell missing edges, but the key information is the per-color induced-subgraph list condition, not the scalar 14.

## 6. Shell-only route audited and rejected

The anchor cardinality plus the two-edge list constraint is insufficient by itself. For any M with at least 14 edges, choose 14 distinct edges, pair them into seven colors, and for each pair select p plus six B labels avoiding the pair's B endpoints. This gives a legal coarse shell-label relaxation of type b_c=6,p-selected.

Since every V12 template has e(M)>=22, no template can be closed from these shell-only constraints alone.

This is not a graph realization. It proves that the next contradiction must use the same U/H and row structure.

## 7. Same-core row/support constraints still available

For every selected block Q anchored at a shell vertex a:

- Q cap D_a is empty;
- if ab is a missing shell edge and the row-transversal theorem's hypotheses hold, Q cap D_b is nonempty;
- same-anchor selected blocks in different exact colors are disjoint;
- every W vertex hits every one of the 49 support blocks;
- every independent W-four-set has positive total W-side slack;
- the support omission-degree identity is
  d_H(u,W)=5+epsilon_u-3r_u+x_u,
  with sum r_u=7 and sum x_u=2delta.

These constraints, together with the b_c>=5 theorem, are the live labelled incidence system.

## 8. Current template status

| Template | Status | Minimum unresolved compatibility |
|---|---|---|
| A | OPEN | >=7 actual selected k=3 B-blocks plus exact row/transversal/core compatibility |
| B | OPEN | >=21 actual selected high-k B-blocks plus exact row/transversal/core compatibility |
| C | OPEN | >=7 actual selected k=3 B-blocks plus M[S] edge and same-core compatibility |
| D | OPEN | >=14 actual selected high-k B-blocks plus allowed pair-type compatibility |
| E | OPEN | anchor cardinality alone gives no high-k selected floor; must use exact P3 row system and factor/core join |

No template has been shown realizable either.

## 9. Exact next theorem

> **Five-template same-core labelled support-row incompatibility:** no A–E shell row system can coexist with seven exact-color selected-component classes on one U/H satisfying b_c in {5,6,7}, at most one selected S anchor per color, support-block disjointness/linearity, row-transversal conditions, the residual 3K5+G11 factor, and the four-unit core excess ledger.

This is the unique global compatibility blocker after the shell-only route audit.

Primary proof files: `SUPPORT_BLOCK_ANCHOR_IDENTITY.md`, `SELECTED_COMPONENT_RESIDUAL_PARTITION.md`, `SELECTED_B_ANCHOR_FLOOR.md`, `SHELL_COLOR_EDGE_LOAD.md`, `SHELL_LIST_RELAXATION_AUDIT.md`, `SUPPORT_BLOCK_W_TRANSVERSAL_CAPACITY.md`, and `LABEL_JOIN_SYSTEM.md`.
