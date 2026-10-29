# E408 Q32 — residual six-set injectivity in the single-outside mode

Date: 2026-10-29  
Status: **PROVED conditional structural lemma** from the residual holonomy table, pair-projection injectivity, and the global T0 saturation cap. No Q32 closure claimed.

## Theorem

For an exact Type-I color \(C\) whose ten isolated K5 components are all single-outside, let
\[
R_i(C)=G_{11}(C)\cap T_i,\qquad i=1,2,3,
\]
so \(|R_i(C)|=2\). Then the six-vertex residual signature
\[
\Sigma(C)=R_1(C)\cup R_2(C)\cup R_3(C)
\]
cannot equal \(\Sigma(C')\) for any distinct exact color \(C'\) that is also in the single-outside mode.

More strongly, if \(C\) is in the single-outside mode and its three selected large-pair matchings induce a six-cycle on \(\Sigma(C)\), then no other exact color in any source mode can have the same six-vertex signature.

## Proof

For each large-track pair \(ij\), the selected color matching \(M_{C,ij}\) restricts to a perfect matching on the \(2\times2\) block \(R_i(C)\times R_j(C)\). The three restrictions form a 2-regular graph on the six residual vertices. Since each vertex has one selected edge to each of the other two tracks and the pairwise edge sets are disjoint, this graph is either two disjoint transversal triangles or one six-cycle.

Suppose two distinct exact colors \(C,C'\) have the same residual six-set. On each pair \(ij\), both selected restrictions are perfect matchings on the same \(K_{2,2}\). They cannot share an edge because distinct colors have disjoint edge sets, so they must be the two complementary perfect matchings of that \(K_{2,2}\).

Encode each pairwise matching by a bit \(b_{ij}\), with 0 for the same-side matching and 1 for the crossed matching after fixing an arbitrary ordering of the two vertices in each track. The union is two triangles exactly when
\[
b_{12}\oplus b_{13}\oplus b_{23}=0;
\]
otherwise it is a six-cycle. Complementing all three pairwise matchings toggles all three bits and therefore toggles this parity. Thus one of \(C,C'\) has a six-cycle residual signature.

Now assume \(C\) is the single-outside color with the six-cycle. The exact local holonomy classification in V47_Z01_RESIDUAL_HOLONOMY_COST.md gives \(g_C\ge2\). The global pointwise saturation theorem gives \(t_C\le1\), and the exact surplus identity
\[
g_C=t_C+\sum_{i<j}(e_C(T_i,T_j)-12)
\]
then forces at least one large-pair repeat edge owned by \(C\). By pair-projection injectivity in V47_Z01_SHARED_P_FACTOR_PACKING.md, Section 4.2, no other exact color may share the residual pair \((R_i(C),R_j(C))\) on the pair carrying that repeat edge. This contradicts \(\Sigma(C)=\Sigma(C')\).

This proves the first claim when both colors are single-outside, and the stronger claim when the six-cycle color \(C\) is single-outside and the other color may be in any source mode. \(\square\)

## What the theorem does and does not say

- It rules out repeated residual six-sets in the labelled owner-only construction whenever the repeated signature is assigned to single-outside colors.
- It does not rule out different six-sets that share one or two of their track-pair projections.
- It does not establish injectivity for two isolated-double colors whose selected residual signatures might require a separate source-incidence argument.
- It does not construct or exclude a complete common-P packing. The full-support \(v=47\), \(z=0,1\), \((2,2,2,1)\) cells remain **OPEN / NOT_CERTIFIED**.

## Finite parity replay

The companion script verify_v47_z01_residual_signature_injectivity.py checks all eight bit triples and confirms that complementing all three pairwise matchings toggles aligned/two-triangle versus nonaligned/six-cycle parity. This finite replay checks the orientation step only; the mathematical conclusion also depends on the cited local holonomy and pair-projection lemmas.
