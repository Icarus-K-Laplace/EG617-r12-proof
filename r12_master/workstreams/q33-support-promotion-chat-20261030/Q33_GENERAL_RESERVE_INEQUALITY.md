# Q33 general reserve inequalities — derivation audit

Status: **PROVED_CONDITIONAL** under the registered seven-witness, exact-129 factor, gadget-independence, and 284-edge core contracts.

## U inequality

There are 7m selected four-sets, each contributing six edges to L_U, and their pair-edge sets are disjoint by within-color disjointness and cross-color linearity. Hence they occupy 42m edges. Exactly 42m-6h are component-witness edges owned by selected exact colors.

For each selected gadget witness Q, the exact color C whose gadget contains Q has alpha(C[Q])<=2. Thus overline(C[Q]) is triangle-free. Each other color contributes at most four edges on Q, and all nonexact colors together contribute at most six. Put rho_m=min(6,4(11-m)). Every nonexact color needs p_12(v) U-edges. Its edges can overlap selected gadget witnesses in at most rho_m h positions; all remaining U-edges must lie outside the 42m selected witness pairs. Thus
\[
(11-m)p_{12}(v)\le L_{\max}(v)-42m+\rho_mh.
\]
The sharper rho_10=4 uses the fact that there is only one nonexact color.

For w>0, degree-sum on W and e(H[W])>=p_4(w) give
\[
e(L_U)\le C(v,2)-280+12w-p_4(w).
\]
For w=0, e(L_U)=797 exactly.

## W inequality

Each selected color leaves either three or four isolated component K4s unselected. Their U-incidences total at most v-28. The exact minima of their W-internal edge contributions are f0(v) and f1(v). These component-owned W edges are disjoint across colors and from nonexact color edges. Since every nonexact color needs p_12(w) edges on W and L_W is K5-free,
\[
(m-h)f_0(v)+hf_1(v)+(11-m)p_{12}(w)\le t_4(w).
\]

## Limitation

The two inequalities are necessary only. A scalar-feasible h is not a graph witness. No larger support is declared closed.
