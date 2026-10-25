# Corrected double-star exclusions for the remaining high \(P_C=50\) profiles

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained exact-129 factor theorem, seven-block row-incidence contract, and exact 11-vertex gadget normal form.  
Scope: excludes the profiles \((5,2,1^5)\) and \((4,3,1^5)\) at \(P_C=50\). It does not yet exclude all \(P_C=50\) cases.

## 1. Profile reduction

For every exact-129 color \(C\),
\[
P_C+R_C=62,\qquad R_C=\sum_{i=1}^7r_i(C),\qquad r_i(C)\ge1.
\]
If \(P_C=50\), then \(R_C=12\). The seven positive integer profiles are
\[
(6,1^6),\ (5,2,1^5),\ (4,3,1^5),\
(4,2,2,1^4),\ (3,3,2,1^4),\
(3,2,2,2,1^3),\ (2^5,1^2).
\]
The first profile is excluded by R12_P50_R6_DOUBLE_STAR_EXCLUSION.md. This note excludes the next two profiles.

## 2. Row-complement and component-incidence accounting

For a block with budget \(r\), let \(H,H'\) be the disjoint clique complements in the 11-point gadget of its two no-component rows. The exact row theorem gives an allowed size profile \((s,t)=(|H|,|H'|)\) from the registered list for that \(r\), and
\[
a=11-s-t,\qquad t_{\mathrm{comp}}\le r-a.
\]
Here \(t_{\mathrm{comp}}\) is the total component-vertex incidence beyond the mandatory single occurrence of each of the fifty component vertices. If the two no-component rows have partial component incidences \(p,p'\), then
\[
p+p'\le t_{\mathrm{comp}}\le r-a.
\]
The verifier enumerates all nonnegative allocations consistent with these bounds in the only cases where they matter.

Each \(r=1\) block supplies a disjoint pair of \(K_5\) complements, and its two no-component rows contain no component vertices. For a chosen row from a high block and a chosen row from the middle-budget block, if their partial component incidences sum to at most four, their neighborhoods cannot jointly cover a full isolated \(K_5\). The same is automatic for a high/middle row paired with an \(r=1\) row: the latter contributes zero component vertices and a no-component row never contains a full \(K_5\).

## 3. Finite double-star alignment predicate

Fix one of the four exact gadget normal forms and an actual complement pair \(H,H'\) from the high-budget block, an actual pair \(Q,Q'\) from the middle-budget block, and the set of low-block pair types appearing among the five \(r=1\) blocks. The verifier seeks:
- a gadget \(K_5\) clique \(D\) disjoint from the selected complements;
- one selected complement \(H\) and one \(Q\), with \(H\cap Q\ne\varnothing\);
- for each low-block pair type, a complement \(L\) disjoint from \(D\) and intersecting \(H\);
- an external gadget vertex \(z\in U_C\setminus(D\cup H)\) which either has a \(C\)-edge to \(D\), or lies outside \(Q\) or one selected \(L\).

All selected complements lie in the six-set \(U_C\setminus D\). Low complements have size five; the middle complement has size at least three. Hence low-low and middle-low complement pairs intersect automatically, and the explicit conditions give high-middle and high-low intersections. The pairwise blocker argument then forces the seven selected no-component rows to be pairwise \(C\)-adjacent: otherwise ten vertices chosen one from each isolated \(K_5\), a common missed gadget vertex, and the two nonadjacent rows form a \(C\)-independent 13-set. Thus \(D\) and the seven rows form a \(C\)-colored \(K_{12}\).

Because \(z\notin H\), it is \(C\)-adjacent to the selected high row. The verifier's final predicate gives it a second \(C\)-edge into \(D\) or a selected low row, so \(d_C(z,K_{12})\ge2\), contradicting the valid star-capacity bound \(d_C(z,K_{12})\le1\).

## 4. The only incidence-budget-sensitive subcases

For \((5,2,1^5)\), the high and middle row-complement budgets are
\[
b_H=5-(11-|H|-|H'|),\qquad
b_Q=2-(11-|Q|-|Q'|).
\]
Their sum exceeds four only when both complement profiles are \((5,5)\), giving \(b_H=4,b_Q=1\). In that case the verifier enumerates every allocation \(p_1+p_2\le4\), \(q_1+q_2\le1\) and requires an aligned choice with \(p_H+q_Q\le4\). For all other complement-profile pairs, the total budget is already at most four.

For \((4,3,1^5)\), the only sensitive case is again the pair \((5,5)\) in both blocks, with budgets \(3\) and \(2\). The verifier enumerates every allocation \(p_1+p_2\le3\), \(q_1+q_2\le2\), and requires an aligned choice with \(p_H+q_Q\le4\). All other complement-profile pairs have combined budget at most four.

## 5. Finite verification and scope

The committed verifier is verify_p50_remaining_high_profiles.py. It enumerates all four gadget normal forms, all actual disjoint complement pairs allowed for \(r=5,2,4,3\), every nonempty set of low \(K_5/K_5\) pair types that can occur among five blocks, and all incidence allocations in the two sensitive cases. Independent in-session replay passed:
- \((5,2,1^5)\): 512,618 non-sensitive configurations and 150 sensitive configurations;
- \((4,3,1^5)\): 1,143,930 non-sensitive configurations and 150 sensitive configurations;
- **1,656,848 base configurations, zero failures**, with every sensitive configuration expanded over all allowed component-incidence allocations.

The verifier checks finite gadget alignment and the stated incidence-budget split only. It does not machine-verify the upstream graph/row theorems.

Combining this result with the \(P_C=50,r_i=6\) exclusion leaves the four correct remaining profiles with \(\max_i r_i\le4\):
\[
(4,2,2,1^4),\quad (3,3,2,1^4),\quad
(3,2,2,2,1^3),\quad (2^5,1^2).
\]
The earlier list with \((4,2,2,2,1^3)\) and \((3,2,2,2,2,1^2)\) was an arithmetic transcription error: both sum to 13, not 12. These four profiles are now excluded by R12_HIGH_P_COLOR_CAP_COMMON_STAR.md. Together, the three double-star exclusions and the common-star theorem establish the conditional colorwise cap \(P_C\le49\). The stronger cap \(P_C\le48\), E408 Q33, and EG617(\(r=12\)) remain **OPEN / NOT_CERTIFIED**.
