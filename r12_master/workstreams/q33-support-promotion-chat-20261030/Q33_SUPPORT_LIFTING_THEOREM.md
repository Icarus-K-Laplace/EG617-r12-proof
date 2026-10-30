# Q33 support-lifting theorem: all-color U/W/component-charge reduction

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

Support floors:
- m=8: v>=31, from the retained E408 Q33 56-block support theorem;
- m=9: v>=32, since 378>t_4(31)=360;
- m=10: v>=34, since 420>t_4(33)=408.

## 2. Turan functions

Let p_k(n) be the minimum number of edges in an n-vertex graph with independence number at most k, and t_k(n)=C(n,2)-p_k(n). Thus t_4(n) is the maximum number of edges in a K5-free graph.

## 3. U-side reserve with the sharp gadget overlap

Write epsilon_W=sum_{x in W}(d_H(x)-12)<=4 and e_W=e(H[W]). Degree-sum on W gives
\[
e_H(U,W)=12w+\epsilon_W-2e_W.
\]
Thus
\[
e(H[U])=284-12w-\epsilon_W+e_W.
\]
Since e_W>=p_4(w), for w>0:
\[
e(L_U)\le C(v,2)-280+12w-p_4(w)=:L_{\max}(v).
\]
For w=0, use e(L_U)=C(47,2)-284=797.

Each nonexact color D needs p_12(v) U-edges. The 7m selected witness blocks occupy42m distinct U-pairs; 42m-6h are component-witness edges owned by exact colors.

For each selected gadget witness Q inside the exceptional gadget of its exact color C, alpha(C[Q])<=2. Thus C[Q] has at least two edges. Since Q has six pairs and edge ownership is unique, all colors other than C together can use at most four edges in Q. In particular, all nonexact colors together can overlap the h selected gadget witnesses in at most4h edges.

All remaining nonexact U-edges must lie outside the 42m selected witness pairs, where at most L_max(v)-42m slots remain. Therefore
\[
\boxed{n p_{12}(v)\le L_{\max}(v)-42m+4h.}\tag{U}
\]

## 4. W-side reserve

A selected color without a gadget witness leaves three unselected isolated component four-sets; a selected color with one gadget witness leaves four. The seven selected disjoint witnesses cover28 points of U, so the total U-incidence among the unselected components of that color is at most v-28.

Define
\[
f_0(v)=\min_{\substack{k_i\in\{0,\ldots,4\},\,i=1,2,3\\\sum k_i\le v-28}}\sum_{i=1}^3 C(4-k_i,2),
\]
\[
f_1(v)=\min_{\substack{k_i\in\{0,\ldots,4\},\,i=1,\ldots,4\\\sum k_i\le v-28}}\sum_{i=1}^4 C(4-k_i,2).
\]
Their W-pairs are distinct component-owned edges, disjoint from nonexact-color W-edges. Since L_W is K5-free,
\[
\boxed{(m-h)f_0(v)+hf_1(v)+n p_{12}(w)\le t_4(w).}\tag{W}
\]

## 5. Component-pair charge

For each unselected component four-set Q, let k=|Q intersect U|. Its U-pair and W-pair costs satisfy
\[
\binom{4-k}{2}+2\binom{k}{2}\ge3
\qquad(k=0,1,2,3,4).
\]
There are exactly \(3(m-h)+4h=3m+h\) such unselected component four-sets. If X_U and X_W are their total U- and W-internal pair costs, then
\[
X_W+2X_U\ge3(3m+h).
\]
The reserve ledgers give
\[
X_U\le B_U:=L_{\max}(v)-42m-np_{12}(v)+4h,
\]
\[
X_W\le B_W:=t_4(w)-np_{12}(w).
\]
Consequently every parent must also satisfy
\[
\boxed{3(3m+h)\le B_W+2B_U.}\tag{C}
\]

## 6. Exact support-size screen

For each m,v, enumerate h=0,...,m and impose (U), (W), and (C). The exact table is in Q33_ALL_SUPPORT_SIZES.md; the committed verifier also checks the grouped per-color component-profile dynamic program.

New excluded cells:
- m=8: v=31,32,33 excluded; first scalar/profile-feasible cell v=34,h=7;
- m=9: v=32,33,34 excluded; first scalar/profile-feasible cell v=35,h in {5,6,7,8,9};
- m=10: v=34,35 excluded; first scalar/profile-feasible cell v=36,h in {3,...,10}.

## 7. Scope firewall

These are necessary inequalities, not sufficient conditions. A nonempty h-set is not a graph realization. All larger support sizes through47 remain open.

The excluded cells are **PROVED_CONDITIONAL** under the source contract; the arithmetic/profile screen is **COMPUTATION_CERTIFIED**. Global E408 Q33 support promotion and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
