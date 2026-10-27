# E407 Q32 — labelled-incidence join

Date: 2026-10-26  
Status: **Necessary constraints recorded; no global infeasibility certificate.**

## Purpose

The complete E407 proof must use one 47-vertex core H, the 29-point support U, the 18-point complement W, the 49 support blocks, the shell rows, and the exact-129 color-factor components simultaneously. The 49 support blocks and the no-S component witnesses are kept as separate labelled families until a proof establishes their exact correspondence.

## Core and support constraints

The core has 284 target edges, minimum degree 12, independence number at most 4, clique number at most 11, and total degree excess 4. The 49 support blocks are 4-subsets of U, seven in each of seven exact-129 color classes. Blocks in one class are disjoint; all blocks are pairwise linear; their union is U, with |U|=29. Their 294 distinct point-pairs are nonedges of H[U]. The \(\delta\) additional nonedges of H[U] are exactly the pairs not covered by these blocks.

For each u in U, let r_u be the number of color classes omitting u, and let x_u be the number of additional nonedges incident to u. Then
\[
\sum_U r_u=7,\qquad \sum_U x_u=2\delta.
\]
Writing \(\epsilon_u=d_H(u)-12\) and \(d_W(u)=d_H(u,W)\), the exact pointwise identity is
\[
d_W(u)=5+\epsilon_u-3r_u+x_u.
\]
This identity is proved in FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md, Section 5.

The aggregate ledger is
\[
e(H[U])=112-\delta,\quad
e_H(U,W)=124+\epsilon_U+2\delta,\quad
e(H[W])=48-\epsilon_U-\delta.
\]

## Shell and template constraints

Let A be the 13-point shell, S its three special vertices, and B the remaining ten vertices. For each shell vertex a, \(D_a=N_F(a)\cap H\), with size \(t_a\). Each support block hits at least three distinct shell rows. If a block is anticomplete to b in B, it must hit every S-row missing to b. The stronger row-transversal theorem says that for any missing shell edge ab, every independent 4-set in \(H\setminus D_a\) intersects \(D_b\).

Templates A–E impose the exact row-size and B-row-type constraints listed in FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md and the source E407 canonical state.

## Exact-129 component family

Each exact-129 color has ten disjoint K5 components and an 11-point exceptional gadget under the registered extremal theorem contract. At least six components per color have form \(\{b\}\cup R\), where b is in B and R is an independent 4-set in H anticomplete to b. These R sets are disjoint within a color and pairwise linear across colors; sets with the same B label in different colors are disjoint.

The component family yields high-k witness floors 2, 4, 2, 3, 1 for templates A–E. For A/C, the registered row-transversal theorem supports the conditional floor max(3,h-4) hub-complete component witnesses per exact-129 color.

## Unresolved bridge

The frozen contract does not yet certify a bijection between the 49 support blocks and the at-least-six B-labelled component quadruples per color. They must remain separate until a component-identity lemma or an overlap-capacity theorem is proved. Identifying them by assumption would be an invalid shortcut.

The minimum next result is either:
1. prove which support blocks are the H-parts of specified K5 components, including their shell/pivot labels; or
2. prove that the support-block incidence system, shell-row constraints, component witnesses, exact color ownership, and four-unit excess budget are jointly infeasible without assuming such identity.

This is a strict reduction, not E407 Q32 closure. The original K145-to-T61 bridge remains open.


Round 5 correction: the claimed three-per-color hub-complete bound is withdrawn. Only the high-k label-intersection floor is certified; see PROOF_DEPENDENCY_AUDIT.md.


Round 6 correction: the direct six-set justification was incomplete, but the stronger A/C bound is reinstated using the row-transversal theorem under the retained R(3,35) exclusion and t_s<=12. See Theorem 4.3 in FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md. The Round 5 withdrawal is superseded by this corrected proof route.


## Round 7 — W-side support-block transversal capacity

The new theorem in SUPPORT_BLOCK_W_TRANSVERSAL_CAPACITY.md adds the following consequences without identifying the 49 support blocks with the separate exact-129 K5-component quadruples.

1. Every \(w\in W\) is adjacent to at least one point of every support block, so \(d_H(w,U)\ge7\).
2. With \(y_w=d_H(w,U)-7\), the exact slack is
   \[
   \sum_{w\in W}y_w=\epsilon_U+2\delta-2\ge7.
   \]
3. Every independent 4-set \(I\subset W\) has \(\sum_{w\in I}y_w\ge1\); hence the zero-slack set \(W_0=\{w:y_w=0\}\) has \(\alpha(H[W_0])\le3\).
4. For nonadjacent \(w,w'\in W\), the block incidence count forces
   \[
   |N_H(w,U)\cap N_H(w',U)|\le y_w+y_{w'}.
   \]
5. If an independent W-quadruple has total slack one, its four U-neighborhoods partition U into sizes \(7,7,7,8\); every support block meets all four parts exactly once. The three 7-parts are pairwise anticomplete K7s. If \(\epsilon_U+2\delta<16\), the 8-part induces a clique or a clique with at most one missing edge.

The minimum-slack profiles are exactly \((\delta,\epsilon_U)=(3,3),(4,1)\), with total W-side slack seven. In either profile there are at least eleven zero-slack W vertices, but **not necessarily exactly eleven**: positive \(y_w\) values may exceed one. No graph terminal is closed by this result.
