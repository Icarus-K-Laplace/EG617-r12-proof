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
