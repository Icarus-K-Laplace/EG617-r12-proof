# Incidence-sensitive closure of two \(P_C=49\) profiles

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** for the two profiles below, under the retained exact-129 factor, row-profile theorem, and gadget-normal-form contract. This does not close the entire \(P_C=49\) boundary.

## 1. Shared incidence constraint

For a block budget \(r_i\le5\), the two no-component rows have disjoint clique complements \(H_i,H_i'\subset U_C\). Put
\[
a_i=11-|H_i|-|H_i'|.
\]
The exact row identity is \(r_i=a_i+e_i+t_i\), and the selected no-component rows' partial component incidences \(p_i,p_i'\) satisfy
\[
p_i+p_i'\le t_i\le r_i-a_i.
\]
The finite verifier enumerates every disjoint clique pair with every nonnegative allocation satisfying this bound. It therefore over-approximates the actual row system.

For a selected complement with incidence \(p_i\), a common-star candidate \((D,w)\) is admissible when \(D\) is a gadget \(K_5\), \(w\notin D\), and the selected complement contains \(w\) while avoiding \(D\). If every selected pair of rows has \(p_i+p_j\le4\), the pairwise-blocker theorem forces all seven selected outer rows to be pairwise \(C\)-adjacent. The common \(D\) then yields a \(C\)-colored \(K_{12}\), and the seven nonempty omission sets in \(U_C\setminus D\) force a vertex with at least two external \(C\)-edges, contradicting \(d_C(z,K_{12})\le1\).

## 2. Profile \((5,2,2,1^4)\)

Use a single threshold mode:
\[
p_5\le3,\qquad p_2\le1,\qquad p_1=0.
\]
This is sufficient because the pairwise sums are at most \(3+1=4\); all other pairs are smaller. If the \(r=5\) block has an incidence allocation \((4,0)\), the threshold filters out the \(p=4\) row and retains the \(p=0\) complement. Otherwise every selected \(r=5\) row has \(p\le3\).

The verifier checks every row-complement pair and every allowed incidence allocation across all four gadget normal forms. Results:
- \(b=1,4\): 173,512 transitions each, maximum 3,329 states;
- \(b=2,3\): 78,362 transitions each, maximum 1,937 states.
No reachable state has an empty common-star candidate set.

Thus this profile is excluded by the double-star contradiction.

## 3. Profile \((5,3,1^5)\)

Three modes cover every possible pairwise-safe incidence pattern:
\[
\begin{array}{c|cc}
\text{mode} & p_5 & p_3\\ \hline
A & \le2 & \le2\\
B & \le3 & \le1\\
C & \le4 & 0
\end{array}
\]
Each mode also requires \(p_1=0\). Any selected incidences satisfying \(p_5+p_3\le4\) belong to at least one of these modes. The verifier carries all three common-star intersections simultaneously and checks that no row-pair tuple can make all three empty.

Results:
- \(b=1,4\): 475,799 transitions each, maximum 16,860 states;
- \(b=2,3\): 233,080 transitions each, maximum 10,009 states.
No reachable state has all three mode intersections empty.

Thus one of the three modes supplies a common star with pairwise selected incidence sums at most four, yielding the same \(K_{12}\) double-star contradiction.

## 4. Updated \(P_C=49\) boundary

Together with the five profiles closed in R12_P49_COMMON_STAR_SCREEN.md, the following seven profiles are now excluded:
\[
(2^6,1),\ (3,2^4,1^2),\ (3^2,2^2,1^3),\ (3^3,1^4),\
(4,2^3,1^3),\ (5,2^2,1^4),\ (5,3,1^5).
\]
Four profiles remain open:
\[
(4,3,2,1^4),\quad (4,4,1^5),\quad (6,2,1^5),\quad (7,1^6).
\]

Reproduction: run verify_p49_incidence_sensitive.py in this workstream directory. The verifier imports the gadget definitions from verify_high_p_common_star.py and independently enumerates all complement-pair types and all allowed partial-component-incidence allocations. The result remains conditional on the mathematical row and gadget contracts. It does not prove \(P_C\le48\), E408 Q33, or EG617(\(r=12\)).
