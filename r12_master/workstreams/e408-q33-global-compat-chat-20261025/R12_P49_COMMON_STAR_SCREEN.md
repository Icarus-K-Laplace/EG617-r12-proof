# \(P_C=49\) boundary: common-star screen and six remaining profiles

Date: 2026-10-25  
Status: **PARTIAL / PROVED_CONDITIONAL**. Five of the eleven \(P_C=49\) budget profiles are excluded by the repaired common-star method. The full \(P_C=49\) boundary remains **OPEN / NOT CERTIFIED**.

## 1. Exact integer profiles

Since \(P_C+R_C=62\), the boundary \(P_C=49\) means \(R_C=13\). The positive seven-part profiles, up to permutation, are exactly
\[
\begin{gathered}
(2^6,1),\ (3,2^4,1^2),\ (3^2,2^2,1^3),\ (3^3,1^4),\\
(4,2^3,1^3),\ (4,3,2,1^4),\ (4^2,1^5),\\
(5,2^2,1^4),\ (5,3,1^5),\ (6,2,1^5),\ (7,1^6).
\end{gathered}
\]
Here exponent notation records repetition.

## 2. Five profiles closed

For each gadget normal form \(b\in\{1,2,3,4\}\), the finite common-star DP was extended from total budget at most 12 to each of the nine profiles with total 13 and maximum at most five. The independent replay enumerated 36 gadget/profile cases, 5,021,134 DP transitions, and at most 3,329 reachable intersection states. The only failures were:
\[
(4,4,1^5)\quad\text{for }b=1,4,\qquad
(4,3,2,1^4)\quad\text{for }b=2,3.
\]
Thus the common-star property holds for the other seven max-at-most-five profiles.

Among those seven, five profiles satisfy \(r_i+r_j\le6\) for every pair:
\[
(2^6,1),\quad (3,2^4,1^2),\quad (3^2,2^2,1^3),\quad
(3^3,1^4),\quad (4,2^3,1^3).
\]
For every selected no-component row, its partial component incidence satisfies
\[
p_i\le r_i-a_i\le r_i-1.
\]
Hence \(p_i+p_j\le4\) for every pair. The common-star alignment supplies a gadget \(K_5\) \(D\) and seven selected row-complements \(G_i\) sharing a point and disjoint from \(D\); the pairwise-blocker lemma then makes the seven outer rows pairwise \(C\)-adjacent. They and \(D\) form a \(C\)-colored \(K_{12}\).

The valid star-capacity bound says any outside vertex has at most one \(C\)-edge into this \(K_{12}\). But \(V'=U_C\setminus D\) has six vertices, and each \(G_i\subset V'\) is a proper subset because \(\omega(C[U_C])=5\). Therefore the seven nonempty omission sets \(V'\setminus G_i\) have total size at least seven, so some \(z\in V'\) is omitted by at least two \(G_i\). That \(z\) has at least two \(C\)-edges into the \(K_{12}\), contradiction.

Consequently, these five \(R_C=13\) profiles are excluded under the retained exact-129 factor, row-profile, pairwise-blocker, and gadget-normal-form contracts.

## 3. Six profiles still open

The remaining six profiles are
\[
(4,3,2,1^4),\quad (4,4,1^5),\quad
(5,2^2,1^4),\quad (5,3,1^5),\quad
(6,2,1^5),\quad (7,1^6).
\]

They divide into three proof obligations:

1. **No common-star certificate in two profiles:** \((4,3,2,1^4)\) and \((4,4,1^5)\). The finite DP has explicit failure witnesses; these require a pairwise-intersection alignment not dependent on a common point, or a different construction.
2. **Common star exists, but component-incidence budget is not automatically enough:** \((5,2^2,1^4)\) and \((5,3,1^5)\). The largest pair sums are 7 and 8, so \(p_i+p_j\le4\) is not guaranteed from budgets alone. Need incidence-sensitive row selection or a direct double-star argument.
3. **High-budget row cases:** \((6,2,1^5)\) and \((7,1^6)\). These need a corrected star-capacity proof based on Theorem 11.1 cases, not the withdrawn isolated-\(K_{12}\) inference.

The archived P49_BOUNDARY_EXCLUSION.md remains **NOT CERTIFIED** as a whole because its global argument uses the invalid claim that every monochromatic \(K_{12}\) has zero external edges of its own color. This note repairs only the five profiles above; it does not claim \(P_C\le48\), and it does not close E408 Q33 or EG617(\(r=12\)).

## 4. Reproduction

Run python verify_p49_common_star_screen.py from this workstream directory. It imports the exact gadget and row-pair enumerator from verify_high_p_common_star.py, asserts the expected pair counts and failure profiles, and reproduces the finite screen. This verifies only the finite gadget alignment; the mathematical row theorem and exact-129 factor remain explicit dependencies.
