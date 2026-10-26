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


## 6. Labelled witness extension — corrected transfer floor

The seven graph-theoretic witnesses of an exact-129 color are not automatically seven isolated K5 components. Each labelled witness K5 lies either in one of the ten isolated components or wholly in the 11-point gadget \(U_C\). Since its four-set \(Q\) is part of seven pairwise disjoint four-sets and \(|U_C|=11\), at most two witnesses lie in the gadget. Hence at least five selected witnesses are isolated components, including at least four of the six B-labelled witnesses.

The common exact size-five blocker set across all seven outer blocks has size at least \(P_C-45\). The valid intersection bound is therefore
\[
|\mathcal W_C\cap\mathcal K_C^*|\ge\max(0,P_C-50),
\]
not \(\max(0,P_C-48)\). A labelled witness component is guaranteed to extend to a monochromatic K12 by this argument only for \(P_C\ge51\). The stronger seven-component transfer needed for a \(P_C\ge49\) threshold remains OPEN.

This does not turn a monochromatic K12 into a contradiction. The scalar relaxation still permits low \(P_C\) for all exact colors, so a global labelled incidence inequality or a component-realization theorem remains necessary.

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


## 10. Corrected external-star audit and current local closure

The sibling statement that every monochromatic \(K_{12}\) is isolated is false as stated. The 12-edge star from an outside vertex must contain all eleven other colors, so the correct bound is \(d_C(z,K_{12})\le1\), not zero. A single external \(C\)-edge is allowed. Therefore sibling \(P_C\le49\), \(P_C\le48\), and \(P_C=50,r_i=6\) arguments that rely only on one external \(C\)-edge are not certified until repaired. They are not dependencies of the current local theorem.

**Conditional local closure:** Section 12 of OUTER_EXCEPTIONAL_ROW_COUPLING.md excludes \(P_C=49,r_i(C)=6\) by forcing an outside vertex to have at least two \(C\)-edges into a constructed \(C\)-colored \(K_{12}\). The finite checker uses the exact Case-C complement profiles and the safe-row incidence split. The in-session predicate replay passed 2,132 Case-A/B configurations and 512,768 exact-profile Case-C configurations. Dependencies remain the exact-129 factor theorem, the seven-block row contract, the exact 11-vertex gadget normal form, and the \(r=1,2,6\) row classifications.

This local result does not establish \(P_C\le49\) for all exact-129 colors and must not be used to prune the global budget profiles without a separately certified colorwise cap. The labelled witness/core capacity theorem and the aggregate eleven-color ledger remain open. EG617(r=12) is **OPEN / NOT_CERTIFIED**.


## 11. Witness label-transfer obligation

The graph-theoretic shell witness family and the exact-129 factor components are distinct structures. A labelled witness K5 is either one of the ten isolated components or lies wholly in the 11-point gadget. Pairwise disjointness of seven four-sets and the gadget size 11 imply at most two gadget witnesses, hence at least five isolated-component witnesses (and at least four B-labelled component witnesses). No stronger seven-component transfer is certified.

Combining this floor with the all-block exact-blocker bound \(|\mathcal K_C^*|\ge P_C-45\) gives only \(|\mathcal W_C\cap\mathcal K_C^*|\ge\max(0,P_C-50)\). Therefore the label-based K12 extension is guaranteed only at \(P_C\ge51\), not \(P_C\ge49\). The stronger label-transfer theorem and the aggregate core/witness contradiction remain OPEN.


## 7. Latest correction: S-avoiding witness transfer floor is six

The earlier generic \(|U_C|=11\) argument gave only five isolated-component witnesses. The selected witnesses all avoid \(S\), and the ten isolated K5 components avoid \(S\), so \(S\subseteq U_C\) and \(|U_C\setminus S|=8\). Two selected gadget witnesses would use disjoint four-sets covering these eight vertices, while a witness label outside \(H\) would require a ninth non-S gadget vertex. Hence at most one selected witness is in the gadget and at least six of seven selected witnesses are isolated K5 components.

Combining \(|\mathcal W_C|\ge6\) with the all-block component bound \(|\mathcal K_C^*|\ge P_C-45\) gives
\[
|\mathcal W_C\cap\mathcal K_C^*|\ge\max(0,P_C-49).
\]
Thus \(P_C\ge50\) forces at least one selected component to extend to a monochromatic K12, and \(P_C=51\) forces at least two. This improves the label-aware threshold but is not a contradiction; all full-terminal and root-bridge obligations remain OPEN / NOT_CERTIFIED.


## 13. Exact-component reservoir: ten witnesses per exact color

Every isolated K5 component of an exact-129 color avoids S. It must contain a vertex outside H because \(\alpha(H)\le4\). The outside-H vertices in such a component lie in \(B\cup\{p\}\), and any two such vertices are target-adjacent; therefore each component has exactly one outside-H label and four core vertices. All ten components are shell witnesses, with ten distinct labels and at least nine B-labelled witnesses per exact color.

For the union \(U_{\rm comp}\) of all ten component four-sets per exact color, \(|U_{\rm comp}|\ge40\). If there are \(m=10\) exact colors, \(|U_{\rm comp}|=40\) is impossible: the 100 component K4s require 600 distinct complement edges, but the core degree ledger and Turán bound on the seven-point complement \(W\) give at most 581. Hence \(m=10\Rightarrow |U_{\rm comp}|\ge41\). At \(v=41\), the 100 component K4s use 600 of at most 610 complement edges, leaving a near-decomposition problem.

The full-component support is distinct from the seven-witness minimum-support union; it does not close the latter's \(v=29/31\) terminal. \(m=8,9\) and \(m=10,v\ge41\) remain OPEN / NOT_CERTIFIED.


## 11. Support-41 omission floor

Under the exact-129 factor theorem and the 284-edge core contract, the support-41 full-component terminal now satisfies \(k\ge8\), where \(k\) is the number of distinct omitted points among ten exact colors. The proof excludes \(k=5\) by forcing a residual \(K_5\), \(k=6\) by forcing an independent \(K_4\) with no \(W\)-edges, and all three possible \(k=7\) multiplicity patterns by exact residual-degree equalities.

The analytical proof is in M10_SUPPORT41_OMISSION_FLOOR.md; the integer verifier is verify_m10_support41_omission_floor.py. The surviving omission counts are \(k=8,9,10\). The support-41 near-decomposition, seven-witness minimum-support terminal, aggregate eleven-color ledger, T61-to-\(K_{145}\) bridge, and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## 12. Further support-41 reduction

At k=8, the omission patterns are (3,1^7) and (2,2,1^6). The e_W=5 case is impossible. In the (3,1^7), e_W=4 branch, the exact inequalities force a rigid terminal with one triple-omitted point, one H-edge from it into W, no other omitted-point edges into W, all residual complement edges incident to that point, and H[W] = K3 disjoint union K2 disjoint union K1. The terminal remains OPEN. The other k=8 cases with e_W<=4 and k=9,10 are still open.


## 13. k=8, e_W=4 refinement

The (2,2,1^6) omission pattern is now excluded at e_W=4. The residual complement edges on O must all touch one of the at most two points with H-edges to W; degree sums force those points to be the two double-omitted points, and their required degrees contradict the six single-omitted points. Thus only the (3,1^7) rigid star terminal remains at k=8, e_W=4. The k=8, e_W=2,3 branches and k=9,10 remain OPEN / NOT_CERTIFIED.
