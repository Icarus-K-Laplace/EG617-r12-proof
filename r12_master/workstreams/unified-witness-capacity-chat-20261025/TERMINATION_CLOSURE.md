# Unified witness-capacity termination closure

Date: 2026-10-25  
Status: **OPEN / NOT_CERTIFIED**. No complete E407 Q32, E408 Q33, or original EG617(r=12) contradiction is claimed.

## 1. Conditional results established in this workstream

1. **Zero-excess common witness (graph-theoretic only).** In a 284-edge, 47-vertex core with \(\alpha(H)\le4\), \(\delta(H)\ge12\), and total excess four, deleting all positive-excess vertices and then at most six more vertices leaves an independent four-set. For two regular shell rows, this yields a common independent four-set when the union of their zero-excess neighborhoods has size at most six. It does not assign an exact-129 color label to that four-set.
2. **Exact-129 exceptional-row incidence.** Under the Type-I exact-129 factor theorem and seven-block equality ledger, every block has \(e_C(B_i,R)=61+r_i(C)\), and its row-neighborhood excess above the \(10\cdot5+2\cdot6=62\) baseline is \(r_i(C)-1\).
3. **Exceptional-row graph constraints.** For \(r_i(C)\le3\), the exceptional-row graph has independence number at most two. For any pair with \(r_i+r_j\le6\), all ten same-component diagonals are present.
4. **Near-complete component matching.** For any exact-129 color and any pair \(r_i,r_j\le5\), at most one of ten same-component representative edges can be missing:
   \[
   m_{ij}(C)\le\left\lfloor\frac{r_i+r_j-2}{5}\right\rfloor\le1.
   \]
5. **Duplicate charging.** A missing same-component diagonal must consume at least one unit of the block-pair duplicate \(d_{ij}(C)\); hence \(m_{ij}(C)\le d_{ij}(C)\) and the sum of missing diagonal labels across low-budget pairs is at most \(P_C\).
6. **Duplicate-budget-to-clique packing.** For every exact-129 color,
   \[
   \nu_{12}(C)\ge\max(0,P_C-45).
   \]
   In particular, \(P_C\ge51\) forces ten vertex-disjoint monochromatic \(K_{12}\) cliques; \(P_C=50\) forces at least eight; \(P_C=49\) forces at least four, with stronger profile-specific cases.

All of these statements depend on the retained exact-129 factor/blocker theorem and outer seven-block equality contract. They do not apply to an arbitrary color graph without those hypotheses.

## 2. Explicitly identified non-closure

The graph-theoretic common-witness theorem does not label an arbitrary independent four-set by a monochromatic K5 component. Counting those common witnesses as exact-129 components would be an invalid label transfer.

An explicit scalar relaxation satisfies all aggregate equalities
\[
P_C+R_C+s_C=62,\quad \sum_C P_C=252,\quad
\sum_C R_C=427,\quad \sum_C s_C=3,
\]
as well as all seven block-column totals and all 21 block-pair duplicate totals, while all eight exact colors have \(P_C=9\) and \(r_i(C)\in\{7,8\}\). It is not a graph-level counterexample, but it proves aggregate budgets alone do not force a high-\(P_C\) exact color into the near-matching branch.

## 3. Minimal missing mathematical bridge

A complete closure still needs at least one of the following:

- a **label-transfer/component-realization lemma** that assigns a valid exact-129 component label to common graph-theoretic witnesses, with edge ownership checked; or
- a **near-exact-color structural theorem** for the three colors with \(s_C>0\), strong enough to prevent them from absorbing the entire duplicate budget; or
- a **global labelled incidence inequality** that couples the seven-block duplicate variables \(d_{ij}(C)\), the residual row variables \(r_i(C)\), and the core witness multiplicities without double counting.

The present inequalities do not rule out all three options. In particular, the scalar relaxation above is not promoted to a colored-graph realization and does not establish that a counterexample exists.

## 4. Dependencies and scope

- Conditional core contract: 47 vertices, \(\alpha(H)\le4\), \(\delta(H)\ge12\), and 284 edges with total degree excess four.
- Exact-129 color factor theorem: ten isolated K5 components plus an 11-point gadget with clique number five and independence number two.
- Seven-block equality system: \(P_C+R_C+s_C=62\), \(\sum_C d_{ij}(C)=12\), and \(\sum_C r_i(C)=61\).
- The original \(K_{145}\) reduction and the core/shell contracts remain external dependencies; no unconditional EG617 result follows here.
- This workstream covers the shared 284-edge E407 Q32 / E408 Q33 setting. It does not close the separate 285-edge E408 Q32 branch.

## 5. Verification and repository hygiene

- Exact integer profile checks for \(R_C=11,12,13\): PASS (210, 455, 875 profiles; maximum high-sum pair counts 0, 1, 2).
- Scalar budget relaxation replay: PASS.
- Exceptional-row mask replay: PASS (15 nonempty masks).
- Missing-diagonal incidence arithmetic replay: PASS for all 25 pairs \(r_i,r_j\in\{1,\ldots,5\}\).
- No full graph-realization SAT/ILP certificate has been generated.
- All changes are confined to r12_master/workstreams/unified-witness-capacity-chat-20261025/.


## 6. Labelled witness extension

The seven selected witness components of an exact-129 color lie among the ten isolated K5 components. The common size-five blocker set across all seven outer blocks has size at least \(P_C-45\); inclusion-exclusion therefore forces at least \(\max(0,P_C-48)\) selected witness components to be common blockers. If \(P_C\ge49\), at least one selected witness-labelled K5 extends with its seven outer representatives to a monochromatic K12; if \(P_C=50\), at least two extend. If \(P_C\ge51\), the stronger all-ten-component alignment result applies.

This makes the high-\(P_C\) branch explicitly label-aware. The scalar relaxation still permits \(P_C=9\) for all eight exact colors, so no such branch is forced by aggregate budgets alone.


## 7. Top-cell-A exact cross-edge defect identity

Under the retained T61 Cell-A contract \(|W|=23\), \(|O|=38\), \(e_F(W)=132\), and \(e_C(W)=11\) for every non-target color, define \(K_W=\sum_{w\in W}(d_F(w)-13)\) and \(t_C=e_C(O)-42\). Since every \(C[O]\) has independence number at most 12, \(t_C\ge0\). Exact cross-edge accounting gives
\[
\sum_C t_C=K_W+411-E-3.
\]
Therefore E408 has \(\sum t_C=K_W\), and E407 has \(\sum t_C=K_W+1\).

For exact-129 colors, the K5-factor/gadget intersection with W is forced to profile \(2^{10}\) or \(2^9,1\), and \(0\le t_C\le6\). If \(t_C=0\), equality in Turan forces \(C[O]\) to be ten disjoint triangles and two disjoint K4s. Thus a possible closure route is now precise: prove that the eleven edge-disjoint near-Turan partitions of O cannot coexist with the target graph's degree, shell and witness constraints, or force a positive defect distribution inconsistent with the exact sum above.

This is a new conditional structural theorem, not a terminal contradiction. The T61 reduction and top-cell-A contract remain dependencies; E408 Cell B is already excluded separately by the sibling theorem.


## 8. Zero-defect Type-A gadget degree profile

If an exact-129 color has \(t_C=0\) and Type-A W-intersection, then \(U[O]=K_4\cup K_4\), \(U[W]=K_2\cup K_1\), and the 16 cross edges are rigid up to the parameter \(a\in\{0,1,2,3\}\). The gadget degree multiset is \(5^{10},8\) or \(5^9,6,7\), so every gadget vertex has degree at least five. In particular, a Type-A zero-defect gadget contributes at least one unit of vertex degree above the generic exact-color floor four for each of its eleven gadget vertices.

The four-value degree-profile arithmetic was independently checked. This local rigidity can be combined with the vertexwise degree equation, but the present aggregate budget has enough slack to accommodate it; no contradiction is claimed.


## 9. Low-slack duplicate ownership

For an exact-129 color with \(r_i(C)=1\) in top-cell A, the exact row theorem forces ten exact K5 rows and two six-vertex gadget rows. The W-incidence profile gives \(e_C(B_i,W)=23\) or 24. Since every \(w\in W\) must see all eleven non-target colors among its 12 edges to \(B_i\), exactly one non-target color is repeated at each \((w,B_i)\). Therefore the unique repeated-C incidence in this block lies in W iff \(e_C(B_i,W)=24\), and in O iff it is 23.

This gives a local interface between the exact gadget-pair choice and the global duplicate ledger. It still does not determine the seven-block location pattern, so it must be combined with the target degree vector and the exact cross-edge defect identity rather than treated as closure.


## 10. Sibling external-edge theorem: eliminate \(P_C=50,r_i=6\)

The latest E408 Q33 sibling proof establishes that every monochromatic \(K_{12}\) is isolated in its color and that \(m\) disjoint such cliques, each using one representative from every outer block, imply \(P_C\le21(12-m)\). It then excludes the exact-129 corner \(P_C=50,r_i(C)=6\) by the three cases in the \(r_i=6\) classification.

This sharpens the high-budget branch: any exact-129 color with \(P_C=50\) has \(r_i(C)\le5\) for all seven blocks, and the existing low-budget alignment result gives at least nine common component labels. The \(P_C=49,r_i=6\) corner remains open because one of the six other blocks has \(r_i=2\), so the all-six-\(r_i=1\) external-edge argument does not transfer verbatim.
