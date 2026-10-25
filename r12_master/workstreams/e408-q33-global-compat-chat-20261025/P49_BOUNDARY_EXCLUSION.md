# Exact-129 budget boundary: exclusion of \(P_C=49\)

Date: 2026-10-25  
Status: **PROVED_WITH_FINITE_GADGET_CERTIFICATE**, conditional on the retained E408 seven-block equality contract and exact-129 factor theorem.  
Scope: a colorwise improvement from \(P_C\le49\) to \(P_C\le48\). It does not close E408 Q33.

## 1. Statement

Fix an exact-129 non-target color \(C\). Under the retained seven-block contract,
\[
P_C+R_C=62,\qquad R_C=\sum_{i=0}^6 r_i(C),
\]
and every \(r_i(C)\ge1\). The exact-129 factor contract gives
\[
C[R]=K_1\dot\cup\cdots\dot\cup K_{10}\dot\cup U_C,
\quad |K_\ell|=5,\quad |U_C|=11,\quad
\alpha(C[U_C])=2,\quad \omega(C[U_C])=5.
\]
Theorem 14.1 already gives \(P_C\le49\). We prove the equality boundary impossible:
\[
\boxed{P_C\ne49,\quad\text{hence }P_C\le48,\ R_C\ge14.}
\]

The proof uses only the exact-129 component labels, the established row-neighborhood theorems (Theorems 10.1 and 11.1), and the finite 11-vertex alignment certificate below. It does not use the inner 56-witness family or assume the support is four-partite.

## 2. Two reusable lemmas

### Lemma 2.1 — isolated monochromatic \(K_{12}\)

Every \(C\)-colored \(K_{12}\) is an isolated component of the color-\(C\) graph.

**Proof.** For any outside vertex \(z\), every other color \(D\ne C\) must appear on at least one of the twelve edges from \(z\) to the clique; otherwise the clique plus \(z\) is a \(D\)-independent 13-set. These twelve edges therefore contain all eleven colors \(D\ne C\), leaving no edge of color \(C\). \(\square\)

### Lemma 2.2 — component-clique dichotomy

Suppose that, for every component label \(\ell\) and every pair of target blocks \(B_i,B_j\), the selected representatives \(x_i(\ell),x_j(\ell)\) are \(C\)-adjacent. Then either the coloring is already contradictory, or there are ten vertex-disjoint \(C\)-colored \(K_{12}\)'s meeting each target block once. In the latter case,
\[
P_C\le21(12-10)=42.
\]

**Proof.** For each \(\ell\), \(K_\ell\) and its seven representatives form a \(C\)-colored \(K_{12}\). If a component \(K_\ell\) is contained in two different row-neighborhoods of the same target block, the unselected outer vertex has a \(C\)-edge to the \(K_{12}\) built using the other representative, contradicting Lemma 2.1. The same contradiction applies if one row-neighborhood contains two full \(K_5\) components: its outer vertex has a \(C\)-edge to the second component outside the \(K_{12}\) built from the first. More generally, if a row-neighborhood contains any vertex of a component \(K_m\) outside its own selected full-\(K_m\) representative, the row's outer vertex gives an external \(C\)-edge to the \(K_{12}\) for \(K_m\), again contradicting Lemma 2.1. Thus, unless already contradictory, every row has only its own full component's vertices (if any) plus gadget vertices, each component has exactly one representative per block, and the ten \(K_{12}\)'s are vertex-disjoint and isolated. Lemma 13.2 gives the displayed bound. \square\)

### Lemma 2.3 — finite gadget alignment

Let \(U_C\) be in the exact normal form of Theorem 12.1. Call a row *gadget-only* if its neighborhood contains no full \(K_\ell\); its omitted set is \(E=U_C\setminus X\), a clique of size at most five.

For each \(s\in\{1,2,3,4\}\), define the universal \(K_5\)-family
\[
\mathcal D_1=\{A,B\},\quad
\mathcal D_2=\mathcal D_3=\{A,B,A'\},\quad
\mathcal D_4=\{A',B\},
\]
where \(A'=(A\setminus\{a_0\})\cup\{x\}\) in the notation of Theorem 12.1. The finite alignment certificate proves:

1. Every \(K_5\) clique \(E\subset U_C\) is disjoint from some \(D\in\mathcal D_s\).
2. Every disjoint pair of \(K_5\)'s (the two omitted sets of an \(r_i=1\) block) has a member disjoint from each \(D\in\mathcal D_s\).
3. For every clique \(E\subset U_C\) of size four or five and every disjoint omitted pair \((F,G)\) with \((|F|,|G|)=(5,5)\) or \((5,4)\), there exists \(D\in\mathcal D_s\) disjoint from \(E\) and from at least one of \(F,G\). In addition, every \(K_5\) omitted set \(E\) is disjoint from some \(D\in\mathcal D_s\), and every disjoint \(K_5/K_5\) pair has a member disjoint from each \(D\in\mathcal D_s\).

Thus if a block has a **gadget-only** row with omitted clique \(E\) of size four or five, and another block has omitted pair \((F,G)\) of type \((5,5)\) or \((5,4)\), one can choose a common \(D\) contained in a row-neighborhood of both blocks and also in a row-neighborhood of every \(r=1\) block. All selected omitted sets have size at least four and lie in \(U_C\setminus D\), a six-set; they therefore pairwise intersect. Since every selected row is gadget-only, the pairwise blocker theorem forces the selected outer vertices to be pairwise \(C\)-adjacent. Together with \(D\) they form a \(C\)-colored \(K_{12}\). The high-block row has an external \(C\)-edge to at least one vertex in \(U_C\setminus(D\cup E)\), contradicting Lemma 2.1.

**Verification contract.** GADGET_ALIGNMENT_VERIFIER.js enumerates all \(2^{11}\) subsets of the exact normal-form gadget for each \(s\), checks clique status by every internal pair, and exhausts every high omitted clique of size four or five, every disjoint \(K_5/K_5\) pair, and every disjoint \(K_5/K_4\) pair. The script asserts the expected counts and all 2,156 alignment checks. The four gadget cases are exhaustive by Theorem 12.1; this is a finite 11-vertex check, not a search whose size grows with \(r\).

## 3. Integer boundary \(P_C=49\)

Assume \(P_C=49\), so \(R_C=13\). Sort the seven positive integers \(r_i\). Their two largest entries sum to at most eight, because the other five entries are at least one. The only possible types with largest-pair sum seven are
\[
(5,2,2,1,1,1,1),\qquad (4,3,2,1,1,1,1),
\]
and the only types with largest-pair sum eight are
\[
(7,1,1,1,1,1,1),\quad
(6,2,1,1,1,1,1),\quad
(5,3,1,1,1,1,1),\quad
(4,4,1,1,1,1,1).
\]
All other types have every pair-sum at most six. For any pair with \(r_i+r_j\le6\), Corollary 10.2 forces the ten component-representative edges across that pair.

### Case I: every pair-sum is at most six

All ten labels have adjacent representatives across every block pair. Lemma 2.2 gives a contradiction to \(P_C=49\).

### Case II: the largest pair-sum is seven

The pair has both entries at most five, so Theorem 10.1 applies to both blocks. If a component-label edge across this pair were missing, pairwise blocker compatibility would force the union of its two row-neighborhoods to cover a second full \(K_5\) component. With no second component, at most
\[
(r_i-1)+(r_j-1)=5
\]
vertices of \(U_C\) can be deleted by the two neighborhoods, leaving at least six gadget vertices; but the \(k=1\) blocker condition would require the remainder to have independence number at most one, impossible because \(\omega(U_C)=5\).

Covering a second component requires \(t_i+t_j\ge5\). Since
\[
r_i+r_j=a_i+a_j+e_i+e_j+t_i+t_j=7,\qquad a_i,a_j\ge1,
\]
equality follows: \(a_i=a_j=1\), \(e_i=e_j=0\), and \(t_i+t_j=5\). Each of the two blocks therefore has the rigid pair of gadget-only rows whose omitted sets are disjoint \(K_5\)'s. The remaining five blocks consist of one \(r=2\) block and four \(r=1\) blocks. The \(r=2\) block has at least one omitted \(K_5\) (Theorem 10.1); choose \(D\) from the universal family to align with that \(K_5\). Both high blocks have rows containing this \(D\), as do all four \(r=1\) blocks. The resulting seven outer vertices and \(D\) form a \(K_{12}\) with an external \(C\)-edge, by Lemma 2.3. Thus no component-label edge can be missing across any pair-sum-seven block pair.

All other block-pairs have sum at most six. Hence every label is adjacent across every pair, and Lemma 2.2 again contradicts \(P_C=49\).

### Case III: largest-pair sum eight, type \((5,3,1^5)\) or \((4,4,1^5)\)

Let \(i,j\) be the unique pair with \(r_i+r_j=8\); both values are at most five. Suppose a component-label edge across this pair is missing. The pairwise blocker condition says that if the union contains no second full \(K_5\) component, then the remaining gadget vertices must form a clique of size at most five, so the two row-neighborhoods must cover at least six vertices of \(U_C\).

There are two cases.

- **A second component is covered.** Since each component row contains exactly one full component under Theorem 10.1, its five vertices are extra component incidences, so \(t_i+t_j\ge5\). Hence
  \[
  a_i+a_j+e_i+e_j=8-(t_i+t_j)\le3.
  \]
  Thus one block has \(a=1\) and the other has \(a\le2\). The \(a=1\) block has two disjoint \(K_5\) omitted sets; the other has at least one \(K_5\) omitted set. Choose a common \(D\in\mathcal D_s\) using Lemma 2.3, and select gadget-only rows containing \(D\) in these two blocks and all five \(r=1\) blocks. Their omitted sets pairwise intersect, so the selected outer vertices and \(D\) form a \(K_{12}\) with an external \(C\)-edge.
- **No second component is covered.** The two component rows must cover at least six gadget vertices. Since every gadget vertex is already covered by the two gadget-only rows in each block, gadget incidences in component rows are duplicate gadget incidences counted by \(e_i,e_j\). Therefore \(e_i+e_j\ge6\). But
  \[
  8=r_i+r_j=a_i+a_j+e_i+e_j+t_i+t_j,\qquad a_i+a_j\ge2.
  \]
  Equality forces \(e_i+e_j=6\), \(a_i=a_j=1\), and \(t_i=t_j=0\). Both blocks then have the rigid pair of disjoint \(K_5\) omitted sets, so the same gadget-only-row \(K_{12}\) contradiction applies.

Thus the unique pair-sum-eight edge cannot be missing. All other pairs have sum at most six, so Lemma 2.2 applies.

### Case IV: type \((6,2,1^5)\)

Let \(B_i,B_j\) be the \(r_i=6,r_j=2\) blocks. Theorem 11.1 Case A and Case B both give a gadget-only row in \(B_i\) with exactly six gadget neighbors, hence an omitted \(K_5\). The \(r_j=2\) block has an omitted pair of type \((5,5)\) or \((5,4)\), and the other five blocks have the rigid \((5,5)\) pairs from \(r=1\). Lemma 2.3 aligns these rows to a \(K_{12}\) with an external \(C\)-edge. Therefore Cases A and B are impossible in this budget profile.

It remains to consider Case C of Theorem 11.1. Here every component-containing row contains exactly one full component, each of the ten components has a unique representative in \(B_i\), and there are two gadget-only rows. Their total gadget incidence is \(11+u_i\le17\).

Suppose a component-label edge between \(B_i\) and another block is missing.

- **Across a \(6+1\) pair.** The \(r=1\) row is exactly \(K_\ell\), with no gadget neighbors. If no second component is covered, the blocker condition requires the \(r_i=6\) row to have at least six gadget neighbors. Together with at least six gadget incidences in each of the two gadget-only rows, this would require at least eighteen, exceeding seventeen. A second component cannot be covered either: the low row contains only \(K_\ell\), while every component-containing row in Case C contains exactly one full component. Thus a missing edge is impossible.
- **Across the \(6+2\) pair.** If a second component is covered, then \(t_i+t_j\ge5\). Since \(t_j\le1\), \(t_i\ge4\), so \(u_i\le2\); the two gadget-only rows have at most thirteen gadget incidences total and at least twelve, hence one has six or seven neighbors. If no second component is covered, the blocker condition requires at least six gadget vertices in the union of the two neighborhoods. The \(r_j=2\) row contributes at most one gadget neighbor, so the high row contributes at least five. Together with the two gadget-only rows, this uses at least seventeen gadget incidences, forcing equality and making both gadget-only rows six-neighbor rows. In either subcase Lemma 2.3 gives the same contradiction.

Therefore no edge can be missing across any \(6+1\) or \(6+2\) pair. All remaining block pairs have sum at most six, so every component label has adjacent representatives across every pair. Lemma 2.2 then yields either an immediate external-edge contradiction or ten disjoint \(K_{12}\)'s and \(P_C\le42\). Both contradict \(P_C=49\).

### Case V: type \((7,1^6)\)

Let \(B_i\) be the \(r_i=7\) block. Write \(t_i\) for its component-incidence excess and \(u_i\) for its gadget-incidence excess, so \(t_i+u_i=7\). Let \(n\) be the number of gadget-only rows; each such row has at least six gadget neighbors, while total gadget incidence is \(11+u_i\le18\), hence \(n\le3\). Let \(M\) be the number of full-component occurrences in the other \(12-n\) rows, counting a row containing two full components twice, and let \(q\le10\) be the number of labels appearing in at least one full-component row. Each of the \(10-q\) labels with no full row still contributes at least five partial component incidences, so
\[
t_i\ge5M+5(10-q)-50=5(M-q).
\]

**Subcase V.a: some row contains two full components.** Then \(M\ge13-n\). For \(n=0,1\), \(t_i\ge5(M-10)\ge15,10\), impossible. If \(n=2\), then \(M\ge11\), \(t_i\ge5\), and \(u_i\le2\); the two gadget-only rows have at most thirteen gadget incidences total, so one has exactly six neighbors and its omitted set is a \(K_5\). If \(n=3\), then \(M\ge10\). If \(q\le9\), then \(t_i\ge5\), so \(u_i\le2\), contradicting the 18 gadget incidences required by three rows of size at least six. Thus \(q=10\), and all three gadget-only rows have exactly six neighbors. In either surviving case there is a gadget-only row with omitted \(K_5\) \(E\). Lemma 2.3 aligns it with the six \(r=1\) blocks to form a \(K_{12}\) with an external \(C\)-edge. Contradiction. Hence no row contains two full components.

**Subcase V.b: no row contains two full components.** Then \(M=12-n\), with one full component per non-gadget-only row.

- \(n=0\) is impossible because \(M=12\) forces \(t_i\ge10>7\).
- \(n=3\) forces all three gadget-only rows to have exactly six gadget neighbors, since their total incidence is at most 18. Any one of their omitted sets is a \(K_5\); Lemma 2.3 gives the external-edge contradiction.
- \(n=1\) gives \(M=11\). If \(q\le9\), then \(t_i\ge10>7\), so \(q=10\) and one component label is repeated. The total gadget incidence is 13, so the gadget-only row has at least six neighbors and the component-containing rows together have at most seven gadget incidences. If any component-containing row has at least six gadget neighbors, then it has six or seven; correspondingly, the gadget-only row has seven or six. Its omitted set is therefore a clique of size four or five, and Lemma 2.3 gives the external-edge contradiction. If every component-containing row has at most five gadget neighbors, no edge from a full-component representative to an \(r=1\) representative of the same component can be missing: otherwise the pairwise blocker condition would require the remaining gadget to be a clique of size at most five, but at least six gadget vertices remain. All component labels are then matched across every block pair; the repeated component gives an external \(C\)-edge to a \(K_{12}\), contradiction.
- \(n=2\) gives \(M=10\). If \(q\le9\), then \(t_i\ge5\), \(u_i\le2\), and total gadget incidence is at most 13. The two gadget-only rows each have at least six gadget neighbors, so at least one has six or seven; its omitted set is a clique of size five or four. Lemma 2.3 gives the external-edge contradiction. Thus \(q=10\), so all ten components are represented exactly once and \(t_i=0\). Total gadget incidence is 18. If any component-containing row has at least six gadget neighbors, the two gadget-only rows must each have exactly six, and Lemma 2.3 gives the external-edge contradiction. If every component-containing row has at most five gadget neighbors, no component-label edge to an \(r=1\) block can be missing, by the same \(k=1\) blocker argument as in the \(n=1\) case. All ten component cliques are then vertex-disjoint, and Lemma 13.2 gives \(P_C\le42\), contradiction.

This excludes type \((7,1^6)\) as well. Together with Cases I–IV, every possible \(R_C=13\) profile is impossible. Therefore \(P_C\ne49\), completing the proof that \(P_C\le48\). \(\square\)

## 4. Scope and dependency firewall

- This is a colorwise result conditional on the exact-129 factor theorem and the retained seven-block equality contract.
- The only new finite computation is the exhaustive 11-vertex gadget alignment verifier; no growing-in-\(r\) graph search is used.
- The result improves \(R_C\ge13\) to \(R_C\ge14\) for every exact-129 color.
- It does not prove a contradiction for the full eleven-color budget, does not close the non-four-partite or four-partite 56-witness branches, and does not prove EG617(r=12).
