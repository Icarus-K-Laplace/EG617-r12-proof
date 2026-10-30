# Q33 component-only variable-core support theorem

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL** for the reserve inequalities under the registered E408 Q33 parent contract; **COMPUTATION_CERTIFIED** for the finite aggregate profile screen. Global Q33 remains **OPEN / NOT_CERTIFIED**.

## 1. Canonical choice of seven component witnesses: h=0

Let the 61-point T61 residual be decomposed as
\[
R=\{p\}\dot\cup S\dot\cup B\dot\cup H,
\qquad |S|=3,\quad |B|=10,\quad |H|=47,
\]
where \(S\dot\cup B\) is the 13-point target shell \(A=N_F(p)\), so \(p\) is target-adjacent to every point of \(B\).

Fix an exact-129 non-target color \(C\). The source-verified Kang–Pikhurko factorization gives ten vertex-disjoint isolated \(C\)-colored \(K_5\) components and an 11-vertex exceptional gadget.

At most three of the ten \(K_5\) components can meet \(S\), so at least seven avoid \(S\). At most one of those seven contains \(p\).

For each of the at least six components avoiding both \(S\) and \(p\), all five vertices lie in \(B\cup H\). It contains at most one \(B\)-vertex because \(B\) is a target clique, and it cannot lie entirely in \(H\) because that would give a target-independent 5-set in \(H\), contrary to \(\alpha(H)\le4\). Thus it has the form \(\{b\}\cup Q\), where \(b\in B\) and \(Q\subset H\), \(|Q|=4\).

If the seventh component contains \(p\), it cannot contain a vertex of \(B\), since \(p\) is target-adjacent to \(B\). It also avoids \(S\), so its other four vertices lie in \(H\); it has the form \(\{p\}\cup Q\) with \(Q\subset H\), \(|Q|=4\).

Therefore every exact-129 color supplies seven pairwise-disjoint component witnesses \(Q\subset H\), each a four-set whose six pairs are edges of \(L=\overline H\). Within one color they are disjoint because the \(K_5\) components are vertex-disjoint. Across distinct colors they intersect in at most one vertex, since sharing two vertices would assign their common pair two colors.

For the present support construction, choose these seven component witnesses in every one of the \(m\) exact-129 colors. Hence the selected-witness count is \(7m\), all \(7m\) witnesses are component witnesses, and
\[
\boxed{h=0.}
\]
This is a choice of the support family; it does not assert that the exceptional gadget has no independent four-set. It avoids needing any gadget-witness existence or overlap allowance.

## 2. Support lower bounds

Let \(U\) be the union of the \(7m\) selected component witnesses and \(v=|U|\). Pairwise linearity gives \(42m\) distinct edges in \(L[U]\). Since \(\alpha(H)\le4\), \(L[U]\) is \(K_5\)-free and
\[
42m\le e(L[U])\le t_4(v).
\]

The registered seven-witness support theorem gives \(v\ge31\) when \(m=8\). For \(m=9\), \(42m=378>t_4(31)=360\), so \(v\ge32\). For \(m=10\), \(42m=420>t_4(33)=408\), so \(v\ge34\). Thus the screen must cover
\[
(m,v)\in\{(8,31\ldots47),(9,32\ldots47),(10,34\ldots47)\},
\]
which is 47 cells.

## 3. Variable core sizes of the three unselected components

For each exact color \(C\), seven of its ten isolated \(K_5\) components have been selected. The remaining three components may contain multiple shell vertices. Let \(c_i\in\{0,1,2,3,4\}\) be the number of core vertices in the \(i\)-th unselected component. The upper bound \(c_i\le4\) follows because five core vertices in a \(C\)-colored \(K_5\) would be a target-independent 5-set in \(H\).

Let \(g_C\) be the number of core vertices in the 11-vertex gadget. The selected seven components contribute 28 core vertices, so
\[
g_C=47-28-\sum_{i=1}^3c_i=19-\sum_i c_i.
\]
Since \(7\le g_C\le10\),
\[
\boxed{9\le\sum_i c_i\le12.}
\]

Let \(k_i\in\{0,\ldots,c_i\}\) be the number of core vertices of the \(i\)-th unselected component lying in \(U\). Put \(K=\sum_i k_i\). The gadget core splits as
\[
s_U=|G_C\cap U|=v-28-K,\qquad
s_W=|G_C\cap W|=g_C-s_U,
\]
where \(W=H\setminus U\). Feasibility requires \(0\le s_U\le g_C\).

## 4. Exact-color pair costs

The unselected component \(i\) contributes
\[
\binom{k_i}{2}
\quad\text{edges in }L[U],\qquad
\binom{c_i-k_i}{2}
\quad\text{edges in }\overline{H[W]}.
\]

The exact-129 factor theorem gives \(\alpha(C[G_C])\le2\) on the gadget. Therefore its induced U- and W-parts contribute at least \(p_2(s_U)\) and \(p_2(s_W)\) edges, respectively, where \(p_k(n)\) is the minimum edge count for an \(n\)-vertex graph with independence number at most \(k\).

Thus one exact color has the necessary pair-cost option
\[
X_U=\sum_{i=1}^3\binom{k_i}{2}+p_2(s_U),
\qquad
X_W=\sum_{i=1}^3\binom{c_i-k_i}{2}+p_2(s_W).
\]
The component and gadget vertex sets are disjoint. Across colors, all counted edges are disjoint by unique edge ownership.

## 5. Global U/W reserve inequalities

Let \(n=11-m\) be the number of nonexact non-target colors. Each such color \(D\) satisfies \(\alpha(D[U])\le12\) and \(\alpha(D[W])\le12\), hence contributes at least \(p_{12}(v)\) U-edges and \(p_{12}(w)\) W-edges, where \(w=47-v\).

The selected component witnesses contribute exactly \(42m\) distinct U-edges, all in their respective exact colors. No unselected component/gadget edge or nonexact-color edge can reuse those pairs. Therefore
\[
\boxed{B_U(v,m)=L_{\max}(v)-42m-(11-m)p_{12}(v)}
\]
is an upper bound for the sum of all \(m\) exact colors' unselected-component/gadget U-costs.

Here, for \(w>0\),
\[
L_{\max}(v)=\binom v2-280+12w-p_4(w),
\]
because the 284-edge core degree ledger gives
\[
e(\overline{H[U]})
=\binom v2-284+12w+\epsilon_W-e(H[W])
\le\binom v2-280+12w-p_4(w).
\]
For \(w=0\), \(L_{\max}(47)=\binom{47}{2}-284=797\).

Since \(H[W]\) has independence number at most four, \(\overline{H[W]}\) has at most \(t_4(w)\) edges. Reserving at least \(p_{12}(w)\) edges for each nonexact color gives
\[
\boxed{B_W(v,m)=t_4(w)-(11-m)p_{12}(w).}
\]

A necessary profile completion exists only if one can choose one of the per-color \((X_U,X_W)\) options for each of the \(m\) exact colors so that the total U-cost is at most \(B_U\) and the total W-cost is at most \(B_W\).

## 6. Exact finite screen and result

The companion verifier generates each exact-color option set in two independent ways:
1. Cartesian product over all 15^3 possible \((c_i,k_i)\) assignments;
2. recursive state enumeration over \((\sum c_i,\sum k_i,\sum\binom{k_i}{2},\sum\binom{c_i-k_i}{2})\).

The option sets agree for every \(v=31,\ldots,47\). A global dynamic program combines \(m\) exact-color options under the two reserve budgets for all 47 registered \((m,v)\) cells.

The source-correct component-only screen excludes:
- \(m=8:\ v=31,\ldots,38\);
- \(m=9:\ v=32,\ldots,39\);
- \(m=10:\ v=34,\ldots,40\).

The first aggregate profile-feasible cells are:
- \(m=8,\ v=39\);
- \(m=9,\ v=40\);
- \(m=10,\ v=41\).

Every larger \(v\) through 47 has at least one aggregate cost-pair survivor in this relaxation. Such a survivor is not a graph realization or a Q33 counterexample.

## 7. Scope

This strengthens the earlier all-h variable-core screen by fixing a source-guaranteed choice of seven component witnesses per exact color. It uses no gadget witness and no +4h overlap allowance. It still omits actual vertex labels, cross-color witness intersections beyond linearity, detailed edge ownership, and the full degree/excess incidence matrix. Thus it is a stronger necessary-condition filter, not a full Q33 UNSAT certificate.

Status: reserve inequalities **PROVED_CONDITIONAL** under the registered Q33 parent contract; finite profile screen **COMPUTATION_CERTIFIED**; remaining graph-level cases and root promotion **OPEN / NOT_CERTIFIED**.


## 8. Nonempty gadget-shell correction and first-survivor W equality

The three unselected K5 components can contain at most three B-vertices in total, since B is a target clique and each non-target K5 contains at most one B. They can contain at most the three S-vertices. The pivot p cannot share a non-target K5 with any vertex of A=S union B, because p is target-adjacent to all of A. Thus the three unselected components can contain at most six shell vertices altogether. After the seven selected components have used seven of the fourteen shell vertices, seven shell vertices remain; at least one of them must lie in the 11-vertex gadget.

Consequently the gadget has at most ten core vertices. Since
\[
g_C=47-28-\sum_i c_i=19-\sum_i c_i,
\]
the correct source profile is
\[
7\le g_C\le10,\qquad \boxed{9\le\sum_i c_i\le12}.
\]
The verifier now imposes this stronger lower bound.

At the first aggregate survivor for m=8, v=39, the per-color minimum W-cost is 3 and the total W budget is 24=8·3. Therefore every exact color attains its minimum W-cost and the W reserve is saturated. Turán equality gives \(\overline{H[W]}=K_{2,2,2,2}\), equivalently \(H[W]=4K_2\). The exact-color W-edge set for each color is a matching of size 3.

At m=9, v=40, the per-color minimum W-cost is 2 and the total W budget is 18=9·2. Hence \(\overline{H[W]}=K_{2,2,2,1}\), equivalently \(H[W]=3K_2\dot\cup K_1\), and each exact-color W-edge set is a matching of size 2.

For these matching conclusions, the finite profile enumeration shows that every per-color minimum-W profile has each of the three component W-parts of size at most 2 and gadget W-part of size at most 4. Global equality forces the gadget graph to attain \(p_2(r)\); for r<=4 its extremal form is a matching (or empty). These are exact structural consequences, not contradictions.

At m=10, v=41, the per-color minimum W-cost is 1 while the W budget is 13, leaving at most three units of aggregate W slack. No Turán equality or matching conclusion is asserted there.
