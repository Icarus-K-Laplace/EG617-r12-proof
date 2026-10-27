# E407 Q32 — shell-only list relaxation is feasible

Date: 2026-10-27  
Status: **PROVED relaxation-feasibility audit. This disproves a shell-only closure route; it is not a graph realization and E407 Q32 remains OPEN.**

## 1. Question audited

The two newest exact-color constraints are:

1. every exact-129 color has a selected anchor set with at least five B labels and at most one S label;
2. every exact-129 color owns at least two shell missing edges whose endpoints are both unselected by that color.

Could these two facts alone contradict one of the five V12 shell templates by a Hall/SDR argument on the 13 shell labels?

The answer is no. In fact the coarse shell-label relaxation is feasible for every shell missing graph M with at least fourteen edges.

## 2. Feasibility theorem

Let A=S disjoint-union B with |S|=3 and |B|=10. Let M be any graph on A with at least fourteen edges. Then one can assign seven abstract exact-color labels c=1,...,7 such that, for every c,

- its selected outside-core anchor set has the allowed type {p} union B_c with |B_c|=6;
- it is assigned two distinct M-edges e_c^1,e_c^2;
- the fourteen assigned M-edges are pairwise distinct across colors;
- neither endpoint of e_c^1 or e_c^2 belongs to B_c.

Thus both assigned edges lie in M[A minus B_c], exactly as required by the shell-edge localization theorem for the anchor type b_c=6 with p selected.

### Proof

Choose any fourteen distinct edges of M and partition them into seven unordered pairs E_c={e_c^1,e_c^2}.

For a fixed pair E_c, at most four endpoints occur altogether, and because B has size ten, at most four B labels are endpoints of those two edges. Hence at least six B labels are not endpoints. Choose any six of them as B_c.

Then A_c^sel={p} union B_c has seven distinct anchors, has the permitted b_c=6,p-selected type, and both edges in E_c have endpoints outside the selected shell anchors. Since the chosen fourteen M-edges are globally distinct, the seven exact colors can own these edge pairs without violating edge-color uniqueness at the shell-label level. QED.

The proof uses only |B|=10 and e(M)>=14; it does not depend on the detailed A-E row pattern.

## 3. Application to the five V12 templates

The retained V12 templates have e(M)>=22, so all five pass this relaxation automatically. Therefore the following information, even taken together, is **insufficient** for a terminal E407 contradiction:

- b_c in {5,6,7};
- at most one selected S-anchor per exact color;
- at least two residual shell edges per exact color;
- edge uniqueness among the seven exact colors.

Any proof that closes E407 must use at least one genuinely non-shell ingredient: the selected support blocks in U, the row sets D_a in the same 284-edge core, exact component/gadget placement, W-side transversal structure, or a stronger color-factor constraint.

## 4. Why this is only a relaxation countermodel

The construction does **not** claim that the seven selected support K5 components exist, that same-anchor support blocks can be packed in U, that row-transversal requirements hold, that the residual 3K5+G11 factor can be realized, or that the 47-vertex core exists.

It proves only that a future argument cannot obtain a contradiction from the shell anchor cardinalities and the two-edge list constraints alone. Treating this relaxation as a graph realization would be invalid.

## 5. Updated unique global blocker

After the selected-anchor floor and shell-edge localization, the primary missing implication is now sharper:

> **Same-core labelled support-row incompatibility.** Show that no one of the five V12 shell row systems can support seven exact-color classes of selected K5 components on the same 29-point U and 284-edge H, with at least five selected B anchors per color, at most one selected S anchor per color, the exact row-transversal requirements, and the residual 3K5+G11 factor.

This is the next target. Shell-only Hall matching is certified insufficient.
