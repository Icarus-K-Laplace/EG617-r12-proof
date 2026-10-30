# Q33 variable-component-core reserve inequalities

Status: **PROVED_CONDITIONAL** under the registered exact-129 factor and seven-witness interface.

For every exact color C, its ten isolated K5 components have core sizes c_i<=4, because a component with five core vertices would be an independent 5-set in H. If g_C is the core size of its 11-vertex gadget, then
\[
g_C=47-\sum c_i,\qquad 7\le g_C\le11.
\]

With seven selected witnesses per color:
- no selected gadget witness: seven component K4s selected, three remaining components with total core size in [8,12];
- one selected gadget witness: six component K4s plus one gadget four-set selected, four remaining components with total core size in [12,16].

For each remaining component, c_i is its core size and k_i its U-incidence. Its U/W pair costs are C(k_i,2), C(c_i-k_i,2). The gadget core has U/W sizes s_U,r_W determined by the selected witness type and the total K_U. Its induced C-graphs have alpha<=2, so contribute at least p2(s_U),p2(r_W) edges, with at most six U gadget edges subtracted when the selected gadget witness Q_C is already counted.

The global budgets are
\[
B_U=L_{\max}(v)-42m-(11-m)p_{12}(v)+4h,
\quad
B_W=t_4(47-v)-(11-m)p_{12}(47-v).
\]
The finite profile screen enumerates all (c_i,k_i) options and checks whether group costs can fit these budgets.


## 2026-10-30 — sharper component-only reserve specialization

For the support set chosen from seven isolated-K5 component witnesses per exact-129 color, all selected witness edges are component-owned and pairwise distinct. Thus h=0, and the correct budgets for this support set are
\[
B_U=L_{\max}(v)-42m-(11-m)p_{12}(v),\qquad
B_W=t_4(w)-(11-m)p_{12}(w).
\]
There is no gadget-witness overlap term. The three unselected components per color have variable core sizes c_i in [0,4], total 8<=sum c_i<=12, and U-incidences k_i in [0,c_i]. Their component pair costs plus the gadget-core p_2 costs are encoded by the component-only verifier.

The resulting finite screen excludes m=8,v=31..38, m=9,v=32..39, and m=10,v=34..40. The first aggregate survivors are v=39,40,41, respectively. The full proof and all rows are in Q33_COMPONENT_ONLY_SUPPORT_SCREEN.md and Q33_ALL_SUPPORT_SIZES.md. This remains a necessary-profile filter; it does not close the remaining labelled graph cases.


## 2026-10-30 correction — nonempty gadget shell

The three unselected K5 components can contain at most three B vertices in total and at most the three S vertices. The pivot p cannot share a non-target K5 with any point of A=S union B. After the seven selected components use seven shell vertices, seven shell vertices remain; at most six can lie in the three unselected components. At least one shell vertex therefore lies in the 11-vertex gadget.

Consequently the gadget has at most ten core vertices, so for the three unselected component core sizes:
\[
g_C=19-\sum_i c_i,\quad 7\le g_C\le10,\quad
\boxed{9\le\sum_i c_i\le12}.
\]
The component-only verifier now imposes this source-derived lower bound. The aggregate support exclusions do not change, but the per-color option sets shrink.
