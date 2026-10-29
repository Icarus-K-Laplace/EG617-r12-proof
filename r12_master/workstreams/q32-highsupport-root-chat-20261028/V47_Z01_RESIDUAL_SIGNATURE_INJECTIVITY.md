# E408 Q32 — residual six-set injectivity across source modes

Date: 2026-10-29  
Status: **PROVED conditional structural lemma** from the residual holonomy table, the isolated-double source audit, pair-projection injectivity, and the global T0 saturation cap. No Q32 closure claimed.

## Theorem

For any two distinct exact Type-I colors \(C,C'\), in any source modes, their six-vertex residual signatures cannot be equal. Write
\[
R_i(C)=G_{11}(C)\cap T_i,\qquad \Sigma(C)=R_1(C)\cup R_2(C)\cup R_3(C),
\]
where \(|R_i(C)|=2\) for each large track. Then
\[
\boxed{\Sigma(C)\ne\Sigma(C')\quad\text{for all }C\ne C'.}
\]

## Proof

For each large-track pair \(ij\), the selected color matching \(M_{C,ij}\) restricts to a perfect matching on the \(2\times2\) block \(R_i(C)\times R_j(C)\). The three restrictions form a 2-regular graph on the six residual vertices, hence either two disjoint transversal triangles or one six-cycle.

Suppose two distinct exact colors \(C,C'\) have the same residual six-set. On each pair \(ij\), both selected restrictions are perfect matchings on the same \(K_{2,2}\). They cannot share an edge because distinct colors have disjoint edge sets, so they must be the two complementary perfect matchings of that \(K_{2,2}\).

Encode each pairwise matching by a bit \(b_{ij}\), with 0 for the same-side matching and 1 for the crossed matching after fixing an arbitrary ordering of the two vertices in each track. The union is two triangles exactly when
\[
b_{12}\oplus b_{13}\oplus b_{23}=0;
\]
otherwise it is a six-cycle. Complementing all three pairwise matchings toggles all three bits and therefore toggles this parity. Thus one of \(C,C'\) has a six-cycle residual signature.

It remains to show that every exact color whose residual signature is a six-cycle owns a large-pair repeat edge.

1. **All ten isolated K5s single-outside.** The audited holonomy-cost table gives \(g_C\ge2\) for a six-cycle. Since \(t_C\le1\), the identity
   \[
   g_C=t_C+\sum_{i<j}(e_C(T_i,T_j)-12)
   \]
   forces at least one large-pair repeat edge.
2. **Isolated-double, two-K4 residual subcases.** The residual graph has two transversal K4 bases, and all additional edges form a star. On any large-pair \(K_{2,2}\) residual block, the alternative perfect matching to the two K4 baseline edges consists of two disjoint cross-K4 edges. A star cannot contain both, so the selected matching on each pair is forced to be the baseline matching. The residual signature is therefore two triangles, not a six-cycle.
3. **Exceptional isolated-double subcase \(x_C,y\in H\).** The source audit gives \(g_C=3,t_C=1\). Hence the large-pair surplus is \(g_C-t_C=2\), so this mode also owns at least one large-pair repeat edge if its selected residual signature is a six-cycle.

Thus the six-cycle color \(C\) has a large-pair repeat edge on some pair \(ij\). Pair-projection injectivity (V47_Z01_SHARED_P_FACTOR_PACKING.md, Section 4.2) says no other exact color may share \((R_i(C),R_j(C))\) on that pair, contradicting \(\Sigma(C)=\Sigma(C')\). \(\square\)

## What the theorem does and does not say

- It rules out repeated residual six-sets across all exact colors, provided the registered source-mode classification and selected-matching contracts hold.
- It does not rule out different six-sets that share one or two of their track-pair projections.
- It does not construct or exclude a complete common-P packing.
- The full-support \(v=47\), \(z=0,1\), \((2,2,2,1)\) cells remain **OPEN / NOT_CERTIFIED**.

## Finite parity replay

The companion script verify_v47_z01_residual_signature_injectivity.py checks all eight bit triples and confirms that complementing all three pairwise matchings toggles aligned/two-triangle versus nonaligned/six-cycle parity. This finite replay checks the orientation step only; the mathematical conclusion also depends on the cited source-mode and pair-projection lemmas.
