# Corrected local exclusion: \(P_C=50,\ r_i(C)=6\) via double-star

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the retained exact-129 factor theorem, seven-block row-incidence contract, exact 11-vertex gadget normal form, and the \(r=1,6\) row classifications.  
Scope: excludes only the corner \(P_C=50\) with a block budget \(r_i(C)=6\). It does not establish \(P_C\le49\).

## 1. Correct star-capacity lemma

Let \(Q\) be a \(C\)-colored \(K_{12}\) in a balanced 12-coloring, and let \(z\notin Q\). The twelve edges from \(z\) to \(Q\) must include every one of the eleven colors other than \(C\), or \(Q\cup\{z\}\) is an independent 13-set in a missing color. Therefore
\[
d_C(z,Q)\le1.
\]
A single external \(C\)-edge is allowed. A contradiction requires at least two external \(C\)-edges from the same \(z\).

## 2. Reduction to one high row and six \(r=1\) rows

Assume \(P_C=50\) and \(r_i(C)=6\) for one outer block \(B_i\). Since \(P_C+R_C=62\), we have \(R_C=12\), so the six other positive block budgets sum to six and hence are all \(r_j(C)=1\).

The \(r=6\) row theorem supplies at least one no-full-component row in \(B_i\). Let \(H\) be the clique complement of its gadget neighborhood in the 11-point gadget \(U_C\). In Cases A/B, \(|H|=5\); in Case C, the pair of no-component complements has one of the registered profiles
\[
(5,5),(5,4),(5,3),(4,4),(5,2),(4,3),(5,1),(4,2),(3,3).
\]
The \(r=1\) row theorem supplies, in each of the other six blocks, two no-component rows whose gadget complements are a disjoint pair of \(K_5\)'s.

Select one no-component row from the high block and one from each of the six \(r=1\) blocks. We will choose a \(K_5\) clique \(D\subset U_C\) disjoint from all seven omitted gadget sets, so all seven selected rows are \(C\)-adjacent to all vertices of \(D\).

## 3. Pairwise compatibility forces a \(C\)-colored \(K_{12}\)

For any pair of selected rows, their omitted gadget sets intersect:
- the verifier explicitly enforces that \(H\) intersects the selected \(K_5\) complement from the first low block and at least one selected complement from every other low-block pair;
- any two low-block complements are \(5\)-subsets of the six-point set \(U_C\setminus D\), so they intersect.

If two selected rows were not \(C\)-adjacent, choose one vertex from each of the ten isolated \(K_5\) components outside both row-neighborhoods, plus a common missed gadget vertex from the intersection of their omitted sets. This is possible because every selected row is a no-component row: the low \(r=1\) rows contain no component vertices, and the high row contains no *full* component, so no pair of selected rows covers a whole isolated \(K_5\). The ten component vertices, the missed gadget vertex, and the two nonadjacent outer rows would form a \(C\)-independent 13-set, contradiction.

Thus the seven selected rows are pairwise \(C\)-adjacent. Together with the \(C\)-clique \(D\), they form a monochromatic \(K_{12}\), call it \(Q\).

## 4. The double-star contradiction

The finite alignment predicate supplies a gadget vertex
\[
z\in U_C\setminus(D\cup H)
\]
with one of the following properties:
1. \(z\) is \(C\)-adjacent to a vertex of \(D\); or
2. \(z\) lies outside the omitted complement of a selected low-block row.

Because \(z\notin H\), it is also \(C\)-adjacent to the selected high-block row. Thus in either case
\[
d_C(z,Q)\ge2,
\]
contradicting the star-capacity lemma.

For the \(r=6\) Case A/B rows, the high complement \(H\) is a \(K_5\). For Case C, the finite checker enumerates every disjoint pair of complements with the nine exact size profiles above. In the \((5,5)\) and \((5,4)\) profiles it checks both high-row choices; in the other profiles it checks that at least one choice works.

## 5. Finite verification and scope

The dedicated verifier is verify_p50_r6_double_star.py. It enumerates the four exact 11-vertex gadget normal forms, every disjoint low-block \(K_5/K_5\) complement pair, every set of low-pair types that can occur among the remaining five \(r=1\) blocks, and all exact Case-C high-complement profiles. An independent in-session replay of the same predicate passed:
- 204 Case A/B configurations;
- 49,008 Case C configurations;
- **49,212 total configurations, zero failures**.

This finite check verifies gadget alignment only; it does not machine-verify the upstream row classifications or exact-129 factor theorem.

Therefore the specific corner \(P_C=50,r_i(C)=6\) is excluded under the stated contracts. The other \(P_C=50\) profiles \((5,2,1^5)\) and \((4,3,1^5)\) are **not** closed by this theorem alone; they are handled by R12_P50_REMAINING_HIGH_PROFILES_EXCLUSION.md. The conditional universal cap \(P_C\le49\) is now established separately by R12_HIGH_P_COLOR_CAP_COMMON_STAR.md. E408 Q33 / EG617(\(r=12\)) remain **OPEN / NOT_CERTIFIED**.
