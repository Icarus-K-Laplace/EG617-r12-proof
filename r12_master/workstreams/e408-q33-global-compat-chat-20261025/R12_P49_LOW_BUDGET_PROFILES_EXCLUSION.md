# Conditional exclusion of all \(P_C=49\) profiles with \(\max_i r_i\le5\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the exact-129 factor theorem, seven-block row-profile contract, exact gadget normal form, and pairwise-blocker theorem.  
Scope: excludes nine of the eleven \(P_C=49\) budget profiles. The only remaining profiles are \((6,2,1^5)\) and \((7,1^6)\); this theorem alone does not establish \(P_C\le48\).

## 1. Correct \(P_C=49\) profile partition

Since \(P_C+\sum_{i=1}^7r_i=62\), the \(P_C=49\) boundary has \(\sum_i r_i=13\). Its eleven positive integer profiles, up to permutation, are
\[
\begin{split}
&(7,1^6),\ (6,2,1^5),\ (5,3,1^5),\ (5,2,2,1^4),\\
&(4,4,1^5),\ (4,3,2,1^4),\ (4,2,2,2,1^3),\\
&(3,3,3,1^4),\ (3,3,2,2,1^3),\\
&(3,2,2,2,2,1^2),\ (2^6,1).
\end{split}
\]
The present result excludes every profile in this list with maximum entry at most five. It leaves only the two profiles containing an \(r_i=6\) or \(r_i=7\) block.

## 2. Gadget and incidence contract

For every block with \(r_i\le5\), the row theorem gives two no-full-component rows. Their omitted gadget sets \(H_i,H_i'\subset U_C\) are disjoint cliques with the registered size profiles. Let \(p_i\) denote the number of component vertices in the selected no-component row. The row identity gives
\[
p_i\le r_i-a_i\le r_i-1,\qquad
a_i=11-|H_i|-|H_i'|\ge1.
\]
If \(p_i+p_j\le4\), two selected rows cannot jointly cover a full isolated \(K_5\). Under the pairwise-blocker theorem, intersecting omitted sets then force the corresponding outer vertices to be \(C\)-adjacent.

The exact 11-point gadget has four normal forms. The fixed universal \(K_5\) families \(D_b\) are the ones registered in GADGET_ALIGNMENT_CERTIFICATE.md. Every \(D\in D_b\) has a disjoint member in every low-block \(55\) complement pair.

## 3. Five profiles with automatic incidence safety

The profiles
\[
(4,2,2,2,1^3),\ (3,3,3,1^4),\
(3,3,2,2,1^3),\ (3,2,2,2,2,1^2),\ (2^6,1)
\]
have \(r_i+r_j\le6\) for every pair. Therefore \(p_i+p_j\le(r_i-1)+(r_j-1)\le4\). The basic common-\((D,w)\) dynamic program verifies that for every allowed row-complement pair tuple, there is a gadget \(K_5\), \(D\), and a common \(w\notin D\) such that each block has a selected complement \(G_i\) with \(w\in G_i\) and \(G_i\cap D=\varnothing\).

The selected rows are pairwise \(C\)-adjacent, and together with \(D\) form a monochromatic \(K_{12}\). Each \(G_i\) is a proper subset of the six-set \(U_C\setminus D\); the seven omission sets therefore have total size at least seven. Pigeonhole gives an outside gadget vertex omitted by at least two selected complements, hence \(C\)-adjacent to at least two vertices of the \(K_{12}\), contradicting the valid star-capacity bound \(d_C(z,K_{12})\le1\).

## 4. Incidence-sensitive common-star exclusions

The two profiles
\[
(5,3,1^5),\qquad (5,2,2,1^4)
\]
also admit a common-\((D,w)\) selection, but their largest two block budgets do not by themselves imply \(p_i+p_j\le4\). The incidence-aware dynamic program enumerates every allowed disjoint complement pair and every integer allocation \(p,p'\le4\) satisfying \(p+p'\le r_i-a_i\). For each candidate \((D,w)\), it tracks the two largest selected partial-component incidences. A candidate is discarded if it is unavailable in any block or if the two largest incidences sum to more than four.

For all four gadget normal forms, no reachable state kills every candidate. The finite replay checks eight profile/form cases and 5,343,724 transitions, with at most 27,714 reachable states. Hence every permitted row-pair/allocation tuple has a common \((D,w)\) and a selection with \(p_i+p_j\le4\) for all pairs. The same double-star contradiction from Section 3 applies.

## 5. Fixed-\(D\) alignment for \((4,4,1^5)\)

Assume a missing \(C\)-edge between component representatives in the two \(r=4\) blocks. If their union covers a second isolated \(K_5\), then
\[
a_i+a_j+e_i+e_j\le3,
\]
so the two omitted-pair profiles are \(55/55\) or \(55/54\). If no second component is covered, the blocker condition requires at least six gadget vertices in the union; the exact row identity forces \(a_i=a_j=1\) and \(t_i=t_j=0\), so both profiles are \(55\).

The verifier exhausts all \(55/55\), \(55/54\), \(54/55\), and \(54/54\) pair types and all partial-incidence allocations allowed by \(r=4\). For each it finds \(D\in D_b\) and one omitted clique from each pair, both disjoint from \(D\), with partial-incidence sum at most four. All selected omitted cliques have size at least four and lie in \(U_C\setminus D\), a six-set, so they intersect pairwise. The five low \(r=1\) blocks can also be aligned to \(D\). Thus the seven selected rows plus \(D\) form a monochromatic \(K_{12}\), and the seven omission sets force an external vertex with at least two \(C\)-edges into it.

The finite verifier checks 117,608 pair-type/allocation tuples, with zero failures.

## 6. Fixed-\(D\) alignment for \((4,3,2,1^4)\)

Consider a missing \(C\)-edge between representatives in the \(r=4\) and \(r=3\) blocks. If no second component is covered, their union leaves at least six gadget vertices, contradicting the \(k=1\) blocker condition. Hence a second component is covered and the exact budget identity forces both omitted-pair profiles to be \(55\), with combined partial-component incidence five.

The verifier enumerates every \(55\) pair in the \(r=4\) block, every \(55\) pair in the \(r=3\) block, every \(55/54\) pair in the \(r=2\) block, and all allowed incidence allocations. It finds \(D\in D_b\) and one selected complement from each pair, all disjoint from \(D\), with every pairwise partial-incidence sum at most four. These selected complements have sizes \(5,5,\ge4\), so they intersect pairwise; the four \(r=1\) blocks align to \(D\) as well. The same \(K_{12}\) double-star contradiction follows.

The finite verifier checks 52,440 triple-pair/allocation tuples, with zero failures.

## 7. Reproducible verification and status

The complete checker is verify_p49_low_budget_double_star.py. It combines:
- 20 basic common-star profile/form cases, 2,779,700 DP transitions;
- 8 incidence-aware common-star profile/form cases, 5,343,724 DP transitions;
- 117,608 fixed-\(D\) allocations for \((4,4,1^5)\);
- 52,440 fixed-\(D\) allocations for \((4,3,2,1^4)\).

All finite checks pass. The checker verifies gadget alignment and integer incidence bookkeeping; it does not machine-verify the upstream graph-theoretic contracts.

**Conclusion:** every \(P_C=49\) profile with \(\max_i r_i\le5\) is excluded under the stated contracts. The only remaining \(P_C=49\) profiles are
\[
\boxed{(6,2,1^5)\quad\text{and}\quad(7,1^6).}
\]
The full \(P_C=49\) boundary, the stronger cap \(P_C\le48\), E408 Q33, and EG617(\(r=12\)) remain **OPEN / NOT_CERTIFIED** until these two high-block profiles are closed.
