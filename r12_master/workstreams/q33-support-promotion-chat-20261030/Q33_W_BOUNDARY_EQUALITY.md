# Q33 first-survivor W-boundary equality theorem

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL** under the registered Q33 parent contract; the per-color profile facts are **COMPUTATION_CERTIFIED** by the companion verifier. This is a structural reduction, not a contradiction.

## 1. The gadget has at least one shell vertex

Use the shell partition
\[
R=\{p\}\dot\cup S\dot\cup B\dot\cup H,\quad
|S|=3,\ |B|=10,\ |H|=47,
\]
with \(S\dot\cup B=A=N_F(p)\). In each exact-129 color, choose seven isolated K5 components avoiding S. Six are B-labelled; if the seventh contains p, p cannot share its K5 with B because p is target-adjacent to all B, and it cannot share with S because p is target-adjacent to S. Thus the seventh is \(\{p\}\cup Q\) with Q⊂H. The selected seven components use exactly seven shell vertices.

Seven shell vertices remain. Each of the three unselected K5 components contains at most one B vertex because B is a target clique; across all three they contain at most three B vertices. They contain at most the three S vertices. The pivot p cannot share a non-target K5 component with any vertex of A. Hence the three unselected components contain at most six shell vertices. At least one of the seven remaining shell vertices lies in the 11-vertex gadget.

The gadget therefore has at most ten core vertices. With the seven selected components contributing 28 core vertices,
\[
g_C=19-\sum_{i=1}^3c_i,\qquad 7\le g_C\le10,
\]
so
\[
\boxed{9\le\sum_{i=1}^3c_i\le12.}
\]

## 2. Exact W budgets at the first aggregate survivors

Let W=H\\U and w=47-v. The component-only verifier gives:

- m=8, v=39: per-color minimum W cost 3, total W budget 24;
- m=9, v=40: per-color minimum W cost 2, total W budget 18;
- m=10, v=41: per-color minimum W cost 1, total W budget 13.

The first two are exact equalities:
\[
8\cdot3=t_4(8)=24,\qquad
9\cdot2=t_4(7)=18.
\]
Since \(\overline{H[W]}\) is K5-free, Turán's theorem bounds its edges by t4(w). Equality forces the balanced complete four-partite graph.

Thus:
- m=8, v=39, W has 8 vertices and \(\overline{H[W]}=K_{2,2,2,2}\), so \(H[W]=4K_2\);
- m=9, v=40, W has 7 vertices and \(\overline{H[W]}=K_{2,2,2,1}\), so \(H[W]=3K_2\dot\cup K_1\).

The exact-color W costs sum to the full Turán capacity. Therefore nonexact colors have no W-edges, and every exact color attains its per-color minimum W cost.

## 3. Why each exact-color W graph is a matching

For the m=8,v=39 and m=9,v=40 minimum-W profiles, exact enumeration shows:
- each of the three unselected component W-parts has size at most 2;
- the gadget W-part has size at most 4.

A component W-part of size at most2 contributes either no edge or one K2 edge. The gadget graph has independence number at most2. Since global W equality forces its edge count to attain p2(r), and r≤4, its extremal graph is respectively empty (r=2), K2 plus an isolated vertex (r=3), or 2K2 (r=4). In every case its edges form a matching. Component and gadget parts are vertex-disjoint, so each exact color's W-edge set is a matching: size3 for m=8, size2 for m=9.

For m=10,v=41 the aggregate W slack is 13-10=3. No equality claim is made.

## 4. Remaining task

The first-survivor cases have now been reduced to:
- an edge decomposition of K_{2,2,2,2} into eight 3-edge matchings, with the per-color component/gadget partition constraints;
- an edge decomposition of K_{2,2,2,1} into nine 2-edge matchings, with the corresponding partition constraints;
- a six-vertex W case for m=10 with at most three units of W slack.

These local W decompositions are not themselves contradictions. The next proof step must couple them to the labelled U-incidence system, shell labels, and the full degree/excess ledger.
