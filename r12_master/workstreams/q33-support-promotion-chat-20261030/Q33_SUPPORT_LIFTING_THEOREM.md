# Q33 support-lifting theorem: all-color U/W reserve reduction

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL** for the necessary inequalities under the registered Q33 source contract; **COMPUTATION_CERTIFIED** for the finite integer screen; global Q33 promotion remains **OPEN**.

## 1. Frozen parent contract

Let H be the E408 Q33 core:
\[
|V(H)|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \delta(H)\ge12,\quad
\sum_{x\in H}(d_H(x)-12)=4.
\]
There are m in {8,9,10} exact-129 non-target colors and n=11-m nonexact non-target colors.

For each exact-129 color C, select seven labelled independent four-sets Q_{C,1},...,Q_{C,7} in H. Within a color they are pairwise disjoint; across colors they intersect in at most one vertex. At most one selected witness per color is a gadget witness. Let h be the total number of selected gadget witnesses, so 0<=h<=m.

Put U=union Q_{C,j}, v=|U|, W=H\\U, w=47-v. The 7m selected blocks occupy 42m distinct edges of L_U=overline(H[U]).

The support lower bounds are:
- m=8: v>=31, from the retained E408 Q33 56-block support theorem;
- m=9: v>=32, since 42m=378>t_4(31)=360;
- m=10: v>=34, since 42m=420>t_4(33)=408.

## 2. Turan functions

Let p_k(n) be the minimum number of edges in an n-vertex graph with independence number at most k, and t_k(n)=C(n,2)-p_k(n). Thus t_4(n) is the maximum number of edges in a K5-free graph.

## 3. U-side reserve

Write epsilon_W=sum_{x in W}(d_H(x)-12)<=4 and e_W=e(H[W]). The degree sum on W gives
\[
e_H(U,W)=12w+\epsilon_W-2e_W.
\]
Consequently
\[
e(H[U])=284-e_W-e_H(U,W)=284-12w-\epsilon_W+e_W.
\]
Since e_W>=p_4(w), for w>0:
\[
e(L_U)\le C(v,2)-280+12w-p_4(w)=:L_{\max}(v).
\]
For w=0, use the exact value e(L_U)=C(47,2)-284=797.

Every nonexact color D has alpha(D[U])<=12, hence e_D(U)>=p_12(v). Of the 42m selected witness edges, 42m-6h are component-witness edges owned by selected exact colors and unavailable to nonexact colors.

For a selected gadget witness Q in the exceptional gadget of color C, alpha(C[Q])<=2, so overline(C[Q]) is triangle-free. Each other single color has at most four edges inside Q; all nonexact colors together have at most six because Q has six pairs. Hence their aggregate overlap with h gadget witnesses is at most rho_m h, where rho_m=min(6,4n). Therefore
\[
\boxed{n p_{12}(v)\le L_{\max}(v)-42m+\rho_m h.}\tag{U}
\]
In particular rho_8=rho_9=6 and rho_10=4.

## 4. W-side reserve

If a selected color has no gadget witness, seven component witnesses are selected and three isolated component four-sets remain. If it has one gadget witness, six component witnesses and the gadget witness are selected, leaving four isolated component four-sets. The seven selected disjoint four-sets cover 28 points of U, so the total U-incidence among the remaining component four-sets is at most v-28.

Define
\[
f_0(v)=\min_{\substack{k_i\in\{0,\ldots,4\},\,i=1,2,3\\\sum k_i\le v-28}}\sum_{i=1}^3 C(4-k_i,2),
\]
\[
f_1(v)=\min_{\substack{k_i\in\{0,\ldots,4\},\,i=1,\ldots,4\\\sum k_i\le v-28}}\sum_{i=1}^4 C(4-k_i,2).
\]
The W-parts of these unselected component K4s contribute distinct edges to L_W. Every nonexact color needs at least p_12(w) W-edges. Since L_W is K5-free,
\[
\boxed{(m-h)f_0(v)+hf_1(v)+n p_{12}(w)\le t_4(w).}\tag{W}
\]

## 5. Exact support-size screen

For each (m,v), let H_W be the h in {0,...,m} satisfying (W), and H_U the h satisfying (U). A parent must have h in H_W intersect H_U. Empty intersection excludes the cell.

The exact arithmetic replay gives:
- m=8: v=31,32 excluded; first scalar-feasible cell v=33,h=5;
- m=9: v=32,33 excluded; first scalar-feasible cell v=34,h in {4,5,6};
- m=10: v=34 excluded; first scalar-feasible cell v=35,h in {2,...,8}.

## 6. Scope firewall

These are necessary inequalities, not sufficient conditions. A nonempty h-set is not a graph realization. Larger supports are not declared closed.

The excluded cells are **PROVED_CONDITIONAL** under the source contract; the arithmetic table is **COMPUTATION_CERTIFIED**. Global E408 Q33 support promotion and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
