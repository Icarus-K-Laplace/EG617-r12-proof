# Q33 variable-component-core profile theorem

Status: **PROVED_CONDITIONAL** for the reserve inequalities under the registered exact-129 factor and seven-witness interface; **COMPUTATION_CERTIFIED** for the finite profile screen. Global Q33 remains OPEN.

## 1. Exact-color factor and component core sizes

For each exact-129 color C, the source-verified factorization has ten isolated C-colored K5 components and an 11-vertex gadget G_C^full. Let c_i in {0,1,2,3,4} be the number of H-core vertices in component i. The upper bound c_i<=4 follows because five core vertices in one C-colored K5 would be an independent 5-set in H, contradicting alpha(H)<=4.

Let g_C be the number of core vertices in the exceptional gadget. Since the ten components and gadget partition the 47-point core,
\[
g_C=47-\sum_{i=1}^{10}c_i.
\]
The ten components contain at most40 core vertices, so g_C>=7; the gadget has only11 vertices, so g_C<=11. Thus 36<=sum c_i<=40.

This explicitly allows components with multiple shell vertices and core size below four.

## 2. Selected witnesses and residual component groups

The registered seven-witness interface selects seven disjoint four-sets per exact color. Within one color they are disjoint; across colors they are linear.

Let h be the number of selected gadget witnesses among the m selected exact colors.
- A color with no selected gadget witness has seven selected component K4s. The remaining three K5 components have core sizes c_1,c_2,c_3 with
\[
8\le c_1+c_2+c_3\le12.
\]
- A color with one selected gadget witness has six selected component K4s and one four-set Q_C inside its gadget core. The remaining four K5 components have core sizes c_1,...,c_4 with
\[
12\le\sum c_i\le16.
\]

These ranges follow from g_C in [7,11]. They do not assume the remaining components are four-core sets.

For each remaining component let k_i be the number of its core vertices in U. Then 0<=k_i<=c_i.

## 3. Gadget-core split

Put v=|U|, w=47-v. The selected seven witnesses cover28 distinct U vertices.

For a no-gadget selected color, if K=sum k_i over its three unselected components, then
\[
s_U=|G_C\cap U|=v-28-K,\qquad
r_W=|G_C\cap W|=g_C-s_U.
\]
For a gadget-selected color, the selected six component witnesses cover24 U vertices and Q_C contributes four U vertices inside G_C. For K=sum k_i over its four unselected components,
\[
s_U=v-24-K,\qquad r_W=g_C-s_U.
\]
The feasible profile requires 0<=s_U<=g_C in the first case and 4<=s_U<=g_C in the second.

Since alpha(C[G_C])<=2, the exact color C has at least p_2(s_U) edges inside G_C∩U and p_2(r_W) edges inside G_C∩W. If a gadget witness Q_C was selected, at most six of the U-side gadget edges can lie inside the already-counted six pairs of Q_C; therefore the additional U reserve cost is max(0,p_2(s_U)-6). With no selected gadget witness, the U-side gadget cost is p_2(s_U).

## 4. Group costs

For one color group with remaining component core sizes c_i and U-splits k_i, define
\[
X_U^{comp}=\sum_i\binom{k_i}{2},\qquad
X_W^{comp}=\sum_i\binom{c_i-k_i}{2}.
\]
Add the gadget-core costs:
- no gadget: \(X_U=X_U^{comp}+p_2(s_U)\), \(X_W=X_W^{comp}+p_2(r_W)\);
- gadget selected: \(X_U=X_U^{comp}+\max(0,p_2(s_U)-6)\), \(X_W=X_W^{comp}+p_2(r_W)\).

All counted edges are non-H edges. Unique color ownership makes component/gadget edges of distinct colors disjoint; within a color the gadget is disjoint from its ten K5 components.

## 5. Global reserve budgets

Let n=11-m. The sharp gadget-witness overlap bound is four per selected gadget witness: alpha(C[Q_C])<=2 forces at least two of its six pairs to be C-colored, leaving at most four pairs for all other colors combined.

The U-side budget is
\[
\boxed{B_U=L_{\max}(v)-42m-np_{12}(v)+4h.}
\]
The W-side budget is
\[
\boxed{B_W=t_4(w)-np_{12}(w).}
\]
A necessary profile completion exists only if the m-h no-gadget group costs and h gadget group costs can be chosen so that their total U-cost is at most B_U and total W-cost at most B_W.

## 6. Exact finite profile screen

The verifier exhausts every:
- unselected component count (3 or4);
- core size c_i in {0,1,2,3,4};
- U-incidence k_i in {0,...,c_i};
- component-core sum in [8,12] or [12,16];
- gadget U/W split;
- h in {0,...,m};
- support size v from its registered lower bound through47.

A product enumerator and a separate recursive state enumerator independently produce identical per-color option sets and identical global feasible h sets on all47 (m,v) cells.

Results:
- m=8: v=31,32,33,34 excluded; first profile-feasible v=35,h=6,7,8.
- m=9: v=32,33,34 excluded; first profile-feasible v=35,h=9.
- m=10: v=34,35,36,37 excluded; first profile-feasible v=38,h=10.

A feasible profile is only a necessary scalar/profile survivor, not a graph realization.

## 7. Scope

This model repairs the stronger fixed-four-core assumption. It is still a relaxation: it does not encode the actual vertex labels, pairwise intersections, cross-color edge ownership at the pair level, or the full degree sequence. Q33 and the root theorem remain OPEN.


## 8. Source-correct component-only support selection

The seven-witness source lemma supplies seven isolated-K5 component four-sets in every exact-129 color. For the support set in this theorem, choose those seven in each of the m exact colors. This fixes h=0 by construction and removes the need for a selected gadget witness. See Q33_COMPONENT_ONLY_SUPPORT_SCREEN.md for the full derivation and the stronger finite screen.

The resulting exclusions are m=8:v=31..38, m=9:v=32..39, and m=10:v=34..40. First aggregate survivors are m=8:v=39, m=9:v=40, and m=10:v=41. These are not graph realizations; all remaining support sizes through47 remain OPEN at the labelled-structure level.
