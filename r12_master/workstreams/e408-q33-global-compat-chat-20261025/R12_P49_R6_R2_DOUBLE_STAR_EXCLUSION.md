# Conditional double-star exclusion of \(P_C=49\), profile \((6,2,1^5)\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** under the registered \(r_i=6\) row classification, \(r_i=2\) row theorem, exact gadget normal form, and universal-\(D\) alignment contract.  
Scope: excludes the single profile \((6,2,1^5)\). The other remaining \(P_C=49\) profile is \((7,1^6)\).

## 1. Row structure and alignment

There is one block with \(r=6\), one with \(r=2\), and five with \(r=1\). The \(r=1\) blocks each have a \(55\) pair of disjoint omitted gadget \(K_5\)'s. The registered universal family \(D_b\) has the property that every \(D\in D_b\) has a disjoint member in each such \(55\) pair.

For the \(r=2\) block, the omitted-pair profile is \(55\) or \(54\). For the \(r=6\) block:
- Case A of the row classification has one no-component row with omitted gadget set a \(K_5\) and zero partial-component incidence in that row;
- Cases B/C have two no-component rows whose omitted-pair profile is among
\[
55,\ 54,\ 53,\ 44,\ 52,\ 43,\ 51,\ 42,\ 33.
\]

The verifier selects a high-block complement \(H\) with \(|H|\ge3\), a middle-block complement \(J\) with \(|J|\ge4\), and a \(D\in D_b\) disjoint from both. Since \(H,J\subset U_C\setminus D\) and \(|U_C\setminus D|=6\), these complements intersect. The same holds for every selected \(r=1\) complement of size five.

## 2. Incidence safety

Let \(p\) and \(q\) be the partial component incidences in the selected \(r=6\) and \(r=2\) rows. A selected no-component row has at most four vertices from any isolated \(K_5\); the row identity gives \(p+p'\le6-a\) in the \(r=6\) pair and \(q+q'\le2-a'\) in the \(r=2\) pair. The exact finite verifier enumerates all these integer allocations and requires
\[
p+q\le4.
\]
Thus the selected high and middle rows cannot jointly cover a full isolated \(K_5\). All other selected-row pairs are automatically safe: the five \(r=1\) rows have no component vertices, and the selected high/middle rows individually contain no full component.

The pairwise-blocker lemma now forces all seven selected outer rows to be pairwise \(C\)-adjacent. Since every selected complement avoids \(D\), all seven rows are \(C\)-adjacent to the five vertices of \(D\). Together they form a monochromatic \(K_{12}\).

## 3. Double-star contradiction

Each of the seven selected omitted sets is a proper subset of the six-point set \(U_C\setminus D\): the selected high complement has size at least three, the middle complement at least four, and the five low complements have size five. Hence the seven omission sets have total size at least seven. By pigeonhole, some gadget vertex \(z\notin D\) is omitted by at least two selected row complements, so it is \(C\)-adjacent to at least two vertices of the constructed \(K_{12}\).

The valid star-capacity lemma says \(d_C(z,K_{12})\le1\): the twelve edges from \(z\) to a monochromatic \(K_{12}\) must include each of the other eleven colors. Thus \(d_C(z,K_{12})\ge2\) is a contradiction. No isolation assumption is used.

## 4. Finite verification

The checker is verify_p49_r6_r2_double_star.py. It enumerates:
- 452 Case-A single-row / \(r=2\) alignment configurations;
- 570,942 Case-B/C pair-type and incidence-allocation configurations;
- **571,394 total configurations, zero failures**.

This is exact gadget/incidence verification, conditional on the upstream row classifications and universal-\(D\) contract.

**Conclusion:** the \(P_C=49\) profile \((6,2,1^5)\) is excluded under the stated contracts. Combined with R12_P49_LOW_BUDGET_PROFILES_EXCLUSION.md, the remaining unresolved cases are the all-component-edges-present branches of \((4,4,1^5)\) and \((4,3,2,1^4)\), plus the profile \((7,1^6)\). The full \(P_C=49\) boundary and EG617(\(r=12\)) remain **OPEN / NOT_CERTIFIED**.
