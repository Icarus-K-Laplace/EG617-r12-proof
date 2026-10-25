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

**Proof.** For each \(\ell\), \(K_\ell\) and its seven representatives form a \(C\)-colored \(K_{12}\). If a component \(K_\ell\) is contained in two different row-neighborhoods of the same target block, the unselected outer vertex has a \(C\)-edge to the \(K_{12}\) built using the other representative, contradicting Lemma 2.1. The same contradiction applies if one row-neighborhood contains two full \(K_5\) components: its outer vertex has a \(C\)-edge to the second component outside the \(K_{12}\) built from the first. Thus, unless already contradictory, each component has exactly one representative per block and each row contains at most one full component. The ten \(K_{12}\)'s are then vertex-disjoint. Lemma 13.2 gives the displayed bound. \(\square\)

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
3. For any \(K_5\) omitted set \(E\) and any disjoint omitted pair \((F,G)\) with \((|F|,|G|)=(5,5)\) or \((5,4)\), there exists \(D\in\mathcal D_s\) disjoint from \(E\) and from at least one of \(F,G\).

Thus if a block has a gadget-only row with omitted \(K_5\) \(E\), and another block has omitted pair \((F,G)\) of type \((5,5)\) or \((5,4)\), one can choose a common \(D\) contained in a row-neighborhood of both blocks and also in a row-neighborhood of every \(r=1\) block. All selected omitted sets have size at least four and lie in \(U_C\setminus D\), a six-set; they therefore pairwise intersect. The pairwise blocker theorem forces the selected outer vertices to be pairwise \(C\)-adjacent. Together with \(D\) they form a \(C\)-colored \(K_{12}\). The gadget-only row has an external \(C\)-edge to the unique vertex in \(U_C\setminus(D\cup E)\), contradicting Lemma 2.1.

**Verification contract.** The file GADGET_ALIGNMENT_VERIFIER.js enumerates all \(2^{11}\) subsets of the exact normal-form gadget for each \(s\), checks clique status by every internal pair, and exhausts every \(K_5\), disjoint \(K_5/K_5\) pair, and disjoint \(K_5/K_4\) pair. Expected counts and all 380 alignment checks are asserted in the script. The four gadget cases are exhaustive by Theorem 12.1; this is a finite 11-vertex check, not a search whose size grows with \(r\).

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

Let \(i,j\) be the unique pair with \(r_i+r_j=8\); both values are at most five. If a component-label edge across this pair were missing, blocker compatibility again forces a second full component in the union. Theorem 10.1 ensures that each component row contains exactly one full component, so this costs at least five extra component incidences:
\[
t_i+t_j\ge5.
\]
Consequently
\[
a_i+a_j+e_i+e_j=8-(t_i+t_j)\le3.
\]
Since \(a_i,a_j\ge1\), one block has \(a=1\) and the other has \(a\le2\). The \(a=1\) block has two disjoint \(K_5\) omitted sets and therefore a row containing either canonical \(D\in\mathcal D_s\). The \(a\le2\) block has at least one omitted \(K_5\), disjoint from one of the canonical \(D\)'s. Choose that \(D\); the five \(r=1\) blocks also have rows containing it. Lemma 2.3 gives the external-edge contradiction. Thus the unique pair-sum-eight edge cannot be missing. All other pairs have sum at most six, so Lemma 2.2 applies.

### Case IV: type \((6,2,1^5)\)

Let \(i,j\) be the \(r_i=6,r_j=2\) blocks. We first show that no component-label edge can be missing between them.

Suppose one were missing. The two row-neighborhoods must cover a second full \(K_5\) component. In Case A or B of Theorem 11.1, the \(r_i=6\) block already has a gadget-only row with exactly six gadget neighbors, whose omitted set is a \(K_5\). In Case C, each component row contains exactly one full component, so the second component costs \(t_i+t_j\ge5\). Since \(t_j\le1\), we have \(t_i\ge4\); the gadget excess in the \(r_i=6\) block is therefore at most two, and its two gadget-only rows have at least six neighbors each but at most thirteen gadget incidences in total. At least one has exactly six neighbors, again giving an omitted \(K_5\).

The \(r_j=2\) block has omitted pair of type \((5,5)\) or \((5,4)\) by Theorem 10.1. Lemma 2.3 aligns the \(r_i=6\) omitted \(K_5\), that pair, and the five \(r=1\) blocks to a common \(D\), yielding a \(K_{12}\) with an external \(C\)-edge. Contradiction.

Now consider any pair consisting of the \(r_i=6\) block and an \(r=1\) block. If a component-label edge were missing, the \(r=1\) row is exactly one \(K_\ell\), so the \(r_i=6\) row itself would have to contain a second full \(K_5\). Cases A and C of Theorem 11.1 and Case B with \(m=10\) forbid such a row. The only remaining subcase is Case B with \(m=11\), where Theorem 11.1 gives two six-neighbor gadget-only rows with omitted \(K_5\)'s; Lemma 2.3, using the \(r=2\) block's \((5,5)\) or \((5,4)\) pair, gives the same external-edge contradiction.

All edges across the \(6+2\), \(6+1\), and remaining low-budget block pairs are therefore forced. If any row repeats a component or contains two components, Lemma 2.2 gives an immediate external-edge contradiction; otherwise the ten \(K_{12}\)'s are disjoint and \(P_C\le42\). Both alternatives contradict \(P_C=49\).

### Case V: type \((7,1^6)\)

Let \(B_i\) be the \(r_i=7\) block. If an edge between its representative of \(K_\ell\) and a representative in an \(r=1\) block were missing, the latter row would be exactly \(K_\ell\); hence the \(r_i=7\) row would have to contain a second full \(K_5\).

Let \(n\) be the number of gadget-only rows in \(B_i\). Every such row has at least six gadget neighbors, while the total gadget incidence is at most \(11+7=18\), so \(n\le3\). Let \(M\) be the number of full-component occurrences across the other \(12-n\) rows, counting a double-component row twice, and let \(q\le10\) be the number of component labels appearing in at least one full-component row. The assumed double row gives \(M\ge13-n\). Each of the \(10-q\) missing labels still contributes at least five partial component incidences. Therefore the component excess satisfies
\[
t_i\ge5M+5(10-q)-50=5(M-q)\ge5(M-10).
\]
For \(n=0\) or \(1\), this gives \(t_i\ge15\) or \(t_i\ge10\), impossible since \(r_i=7\). Hence \(n\in\{2,3\}\). If \(n=2\), then \(M\ge11\), so \(t_i\ge5\), and gadget excess is at most two; the two gadget-only rows have at most thirteen gadget incidences total, so one has exactly six. If \(n=3\), all three rows have exactly six gadget neighbors because the total is at most eighteen. In either case there is a gadget-only row whose omitted set is a \(K_5\).

Every \(r=1\) block has a disjoint pair of \(K_5\) omitted sets. Theorem 12.1 supplies a canonical \(D\) disjoint from the high-block omitted \(K_5\) and a row containing \(D\) in each \(r=1\) block. Their omitted sets are 5-subsets of \(U_C\setminus D\), so they pairwise intersect; the seven outer vertices and \(D\) form a \(K_{12}\) with an external \(C\)-edge. Contradiction. Therefore no edge can be missing across any \(7+1\) pair, and all component labels are adjacent across all block pairs. Lemma 2.2 finishes the contradiction.

All possible \(R_C=13\) profiles have been excluded. Thus \(P_C\ne49\), completing the proof that \(P_C\le48\). \(\square\)

## 4. Scope and dependency firewall

- This is a colorwise result conditional on the exact-129 factor theorem and the retained seven-block equality contract.
- The only new finite computation is the exhaustive 11-vertex gadget alignment verifier; no growing-in-\(r\) graph search is used.
- The result improves \(R_C\ge13\) to \(R_C\ge14\) for every exact-129 color.
- It does not prove a contradiction for the full eleven-color budget, does not close the non-four-partite or four-partite 56-witness branches, and does not prove EG617(r=12).
