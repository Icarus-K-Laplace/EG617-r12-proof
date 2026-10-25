# Exact-129 boundary exclusion: \(P_C=48\)

Date: 2026-10-25  
Status: **PROVED_WITH_FINITE_GADGET_CERTIFICATE**, conditional on the retained exact-129 factor theorem and seven-block equality contract.  
Scope: excludes the next integer layer after P49_BOUNDARY_EXCLUSION.md; it does not close E408 Q33.

## 1. Statement

For an exact-129 color \(C\), retain the seven-block contract
\[
P_C+R_C=62,\qquad R_C=\sum_{i=1}^7 r_i(C),
\]
where each \(r_i(C)\ge1\). Theorem 14.1 gives \(P_C\le49\), and P49_BOUNDARY_EXCLUSION.md excludes \(P_C=49\). We now exclude the next boundary:
\[
\boxed{P_C\ne48,\qquad\text{hence }P_C\le47,\ R_C\ge15.}
\]

Assume for contradiction \(P_C=48\), so \(R_C=14\). The positive seven-tuple \((r_1,\ldots,r_7)\) has one of the following forms:
- every \(r_i\le5\);
- \((6,3,1^5)\) or \((6,2,2,1^4)\);
- \((7,2,1^5)\);
- \((8,1^6)\).

If every \(r_i\le5\), Theorem 10.1 supplies two gadget-only rows per block and an omitted-clique pair of type \(55,54,53,\) or \(44\) whenever the corresponding overlap parameter is at most three. For \(r_i=1,2,3\), the possible pair types are respectively \(55\), \(55/54\), and \(53/44\). The \(r_i=6\) blocks are handled by Theorem 11.1, Cases A/B/C.

## 2. Finite alignment facts used below

Write \(U=U_C\), with \(|U|=11\), \(\alpha(C[U])=2\), and \(\omega(C[U])=5\). A gadget-only row with neighborhood \(X\subseteq U\) has omitted set \(E=U\setminus X\), which is a clique.

The expanded GADGET_ALIGNMENT_VERIFIER.js checks all four exact normal forms and certifies the following fixed-size facts:

1. A fixed omitted \(K_4\) or \(K_5\) aligns with any low pair of type \(55\) or \(54\). A fixed omitted \(K_3\) aligns with a \(55\) pair.
2. A fixed omitted \(K_5\) aligns with a low pair of type \(53\) or \(44\).
3. A fixed omitted \(K_5\) aligns simultaneously with two low pairs of type \(55/54\).
4. For two omitted pairs whose types are in \(\{55,54,53,44\}\), there is a common \(D\in\mathcal D_s\) disjoint from a member of size at least four in each pair, **unless both pairs have type \(53\)**.
5. For one omitted pair of type \(55/54/53/44\) and two low pairs of type \(55/54\), there is a common \(D\) disjoint from a member of size at least four in all three pairs.
6. Every \(D\in\mathcal D_s\) has a disjoint member in every \(55\) pair.

All alignment claims above were exhaustively checked over the four 11-vertex normal forms: 467,696 checks, zero failures. The \(53+53\) pair/pair exception is not used in a feasible missing-edge branch below: two \(53\) profiles would require \(a_i=a_j=3\), incompatible with the incidence budget.

Whenever a common \(D\) is found, the selected omitted sets lie in the six-set \(U\setminus D\). The selected sets have size at least four (or, in the explicitly noted \(K_3\)-versus-\(55\) case, sizes three and five), so they pairwise intersect. The pairwise blocker theorem then forces the selected gadget-only outer vertices to be pairwise \(C\)-adjacent. Together with \(D\), they form a \(C\)-colored \(K_{12}\). Since the high row omits at most five vertices and \(D\) is disjoint from its omitted set, that \(K_{12}\) has an external \(C\)-edge, contradicting the isolated-\(K_{12}\) lemma.

## 3. Case I: every \(r_i\le5\)

If \(r_i+r_j\le6\), Corollary 10.2 forces all same-component representatives across blocks \(i,j\) to be \(C\)-adjacent.

Consider a pair with \(s=r_i+r_j\ge7\). Since \(R_C=14\) and the other five entries are positive, \(s\le9\). Theorem 10.1 applies to both blocks. Suppose a same-component representative edge across this pair were missing. Let \(a_i,a_j\) be the two gadget-row overlaps, \(e_i,e_j\) the gadget incidences in component rows beyond baseline, and \(t_i,t_j\) the component-incidence excesses. Then
\[
r_i+r_j=a_i+a_j+e_i+e_j+t_i+t_j.
\]

The pairwise blocker theorem gives two alternatives:

- **A second full component is covered.** Then \(t_i+t_j\ge5\), so
  \[
  a_i+a_j+e_i+e_j\le s-5\le4.
  \]
  Thus each omitted pair has type \(55,54,53,\) or \(44\), and the two pairs cannot both have type \(53\). The pair/pair alignment certificate supplies a common \(D\), giving the external-edge contradiction.
- **No second full component is covered.** The remaining gadget must have independence number at most one. Since \(\omega(C[U])=5\), the two neighborhoods must cover at least six gadget vertices, hence \(e_i+e_j\ge6\). Therefore
  \[
  a_i+a_j+t_i+t_j\le s-6\le3.
  \]
  When \(s=7\), this would force \(a_i+a_j+t_i+t_j\le1\), impossible because \(a_i,a_j\ge1\); so the no-second-component branch cannot occur. When \(s=8\), both omitted pairs have type \(55\); when \(s=9\), both have type \(55\) or \(54\). The same alignment argument gives a contradiction.

For completeness, the five remaining budgets have sum \(14-s\le7\):
- if \(s=7\), they are either \((3,1^4)\) or \((2,2,1^3)\);
- if \(s=8\), they are \((2,1^4)\);
- if \(s=9\), they are \((1^5)\).

The corresponding extra pair types are respectively one \(53/44\) pair or two \(55/54\) pairs, one \(55/54\) pair, or all \(55\) pairs. These are covered by the pair/pair or triple alignment checks; for \(s=7\), the missing-edge budget forces the two high pairs to be \(55/55\), so every chosen \(D\) also aligns with the other \(55\) pair. Thus no same-component edge can be missing across any block pair. Lemma 2.2 then gives either an immediate isolated-\(K_{12}\) contradiction or ten disjoint \(K_{12}\)'s and \(P_C\le42\), contradicting \(P_C=48\).

## 4. Case II: budget profile \((6,3,1^5)\)

Let \(B_i\) be the \(r_i=6\) block and \(B_j\) the \(r_j=3\) block.

**Theorem 11.1, Cases A/B.** The \(r_i=6\) block has a gadget-only row with omitted \(K_5\) \(E\). The \(r_j=3\) block has an omitted pair of type \(53\) or \(44\). Alignment fact 2 gives a common \(D\), and the five \(r=1\) blocks align with every \(D\). This creates a \(K_{12}\) with an external \(C\)-edge, contradiction.

**Theorem 11.1, Case C.** Let \(a_i\) be the gadget-row overlap in the \(r_i=6\) block. If \(a_i\ge4\), then \(e_i+t_i=6-a_i\le2\). The \(r_j=3\) block has \(e_j+t_j=3-a_j\le2\). A missing edge could cover at most four gadget vertices and cannot cover a second full component, so the blocker condition forces the edge. All other block pairs have budget sum at most six; hence all component edges are forced and Lemma 2.2 applies.

If \(a_i\le3\), the high omitted pair has type \(55,54,53,\) or \(44\). If both high and low omitted pairs have type \(53\), then \(a_i=a_j=3\), \(e_j=t_j=0\), and \(e_i+t_i=3\). A missing edge would require either \(t_i+t_j\ge5\) or \(e_i+e_j\ge6\), both impossible. In every other type combination, alignment fact 4 gives the external-edge contradiction. Thus all edges are forced or a contradiction is immediate.

## 5. Case III: budget profile \((6,2,2,1^4)\)

There are two \(r=2\) blocks and four \(r=1\) blocks.

**Theorem 11.1, Cases A/B.** The \(r=6\) block has a gadget-only row with omitted \(K_5\) \(E\). Alignment fact 3 aligns \(E\) with the omitted pairs of both \(r=2\) blocks; the four \(r=1\) pairs align with every \(D\). This yields the external-edge contradiction.

**Theorem 11.1, Case C.** If \(a_i\ge4\), then \(e_i+t_i\le2\). Each \(r=2\) block has at most one extra component/gadget incidence, so a same-component row pair covers at most three gadget vertices and cannot cover a second full component. All such edges are forced, as are all low-budget block-pair edges.

If \(a_i\le3\), the high omitted pair has type \(55,54,53,\) or \(44\). Alignment fact 5 aligns this pair with the two \(r=2\) omitted pairs simultaneously. The four \(r=1\) pairs align with every \(D\), giving a \(K_{12}\) with an external \(C\)-edge. This excludes the profile.

## 6. Case IV: budget profile \((7,2,1^5)\)

Let \(B_i\) be the \(r_i=7\) block, and let \(n\) be its number of gadget-only rows. Write \(t_i+u_i=7\), where \(t_i\) is component-incidence excess and \(u_i\) gadget-incidence excess. Total gadget incidence is \(11+u_i\le18\), so \(n\le3\). If \(M\) is the number of full-component occurrences in the component rows and \(q\) the number of labels represented by a full component, then
\[
t_i\ge5(M-q).
\]

- **\(n=0\) is impossible:** \(M\ge12\), \(q\le10\), so \(t_i\ge10>7\).
- **\(n=3\):** the three gadget-only rows each have exactly six gadget neighbors. Any omitted \(K_5\) aligns with the \(r=2\) pair and the five \(r=1\) pairs, contradiction.
- **\(n=2\):** if a component row contains two full components, or if \(q\le9\), then \(t_i\ge5\), \(u_i\le2\), and total gadget incidence is at most 13. One gadget-only row has six or seven neighbors, so its omitted set is a \(K_5\) or \(K_4\); alignment fact 1 gives a contradiction. Otherwise \(q=10\), no row contains two full components, \(t_i=0\), and total gadget incidence is 18. The two gadget-only rows cover \(U\). Let \(e_i\) be the gadget incidences in component rows. If \(e_i\ge5\), their overlap is \(a_i=7-e_i\in\{1,2\}\), so the omitted pair has type \(55/54\) and aligns with the \(r=2\) pair. If \(e_i\le4\), every component row has at most four gadget neighbors; together with at most one extra vertex in an \(r=2\) row, the blocker condition forces every same-component edge.
- **\(n=1\):** a double-component row would force \(t_i\ge10>7\). Thus there are 11 component rows, all ten labels appear, and one label is repeated; \(t_i\ge5\), so total gadget incidence is at most 13. If any component row has at least six gadget neighbors, the sole gadget-only row has an omitted clique of size at least four and alignment fact 1 applies. Otherwise, if the \(r=2\) omitted pair is type \(54\), its component rows have no extra vertices, and all same-component edges are forced. If it is type \(55\), each component row in the \(r=2\) block has at most one extra vertex: high rows with at most four gadget neighbors force the edge; if a high component row has five gadget neighbors, the gadget-only row omits a clique of size at least three and alignment fact 1 (including the \(K_3\)-versus-\(55\) check) gives an external-edge contradiction.

In the forced-edge subcases, the repeated component yields an isolated-\(K_{12}\) contradiction. Thus \((7,2,1^5)\) is impossible.

## 7. Case V: budget profile \((8,1^6)\)

Let \(B_i\) be the \(r_i=8\) block and \(n\) its number of gadget-only rows. Total gadget incidence is at most 19, so \(n\le3\). With \(M,q,t_i\) as above, \(t_i\ge5(M-q)\).

- **\(n=0\) is impossible:** \(M\ge12\) gives \(t_i\ge10>8\).
- **\(n=3\):** each gadget-only row has six or seven gadget neighbors, so one has an omitted \(K_4\) or \(K_5\). It aligns with all six \(r=1\) pairs.
- **\(n=2\):** if a row contains two full components or \(q\le9\), then \(t_i\ge5\), total gadget incidence is at most 14, and one gadget-only row has six or seven neighbors; align it with the \(r=1\) pairs. Otherwise \(q=10\), no double row occurs, and \(t_i=0\). If a component row has at least six gadget neighbors, one gadget-only row has six or seven neighbors and aligns. If not, let \(e_i\) be total gadget incidence in component rows. The two gadget-only rows cover \(U\), and their overlap is \(a_i=8-e_i\). If \(e_i\ge5\), then \(a_i\le3\) and the omitted pair is type \(55,54,53,\) or \(44\); pair/pair alignment with a \(55\) pair gives the contradiction. If \(e_i\le4\), every component row has at most four gadget neighbors, so every same-component edge to an \(r=1\) block is forced; Lemma 2.2 applies.
- **\(n=1\):** a double-component row would give \(t_i\ge10>8\). Otherwise one component is repeated, \(t_i\ge5\), and total gadget incidence is at most 14. If a component row has at least six gadget neighbors, the gadget-only row omits a clique of size at least three and the \(K_3/K_4/K_5\)-versus-\(55\) alignment applies. If all component rows have at most five gadget neighbors, the \(r=1\) rows are exact \(K_5\) blockers; no second component can be covered, because the repeated component accounts for five of \(t_i\) and at most three additional component incidences remain. Hence every same-component edge is forced, and the repeated component yields an isolated-\(K_{12}\) contradiction.

All possible \(R_C=14\) profiles are excluded. Therefore \(P_C\ne48\), proving \(P_C\le47\). \(\square\)

## 8. Dependency firewall

- The theorem depends on the retained exact-129 factor theorem, Theorems 10.1 and 11.1, the exact 11-vertex normal form of Theorem 12.1, and the isolated-\(K_{12}\) budget lemma.
- The new finite verification is fixed-size: 467,696 alignment checks across four 11-vertex normal forms, zero failures.
- This is a colorwise conditional result. It does not close the aggregate eleven-color ledger, the 56-witness global compatibility, E408 Q33, or EG617(r=12).
