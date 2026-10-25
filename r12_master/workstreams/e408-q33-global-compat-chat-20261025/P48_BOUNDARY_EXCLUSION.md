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

If every \(r_i\le5\), Theorem 10.1 supplies two gadget-only rows per block. The omitted-pair type is determined by the overlap \(a\), not by \(r_i\) alone: \(a=1,2,3\) gives \(55\), \(54\), and \(53/44\), respectively, while \(r_i=a+e_i+t_i\). Thus an \(r_i=3\) block may have type \(55,54,53,\) or \(44\); the proof below handles all four. The \(r_i=6\) blocks are handled by Theorem 11.1, Cases A/B/C.

## 2. Finite alignment facts used below

Write \(U=U_C\), with \(|U|=11\), \(\alpha(C[U])=2\), and \(\omega(C[U])=5\). A gadget-only row with neighborhood \(X\subseteq U\) has omitted set \(E=U\setminus X\), which is a clique.

The expanded GADGET_ALIGNMENT_VERIFIER.js checks all four exact normal forms and certifies the following fixed-size facts:

1. A fixed omitted \(K_4\) or \(K_5\) aligns with any low pair of type \(55\) or \(54\). A fixed omitted \(K_3\) aligns with a \(55\) pair.
2. A fixed omitted \(K_5\) aligns with a low pair of type \(53\) or \(44\).
3. A fixed omitted \(K_5\) aligns simultaneously with two low pairs of type \(55/54\).
4. For two omitted pairs whose types are in \(\{55,54,53,44\}\), there is a common \(D\in\mathcal D_s\) disjoint from a member of size at least four in each pair, **unless both pairs have type \(53\)**.
5. For one omitted pair of type \(55/54/53/44\) and two low pairs of type \(55/54\), there is a common \(D\) disjoint from a member of size at least four in all three pairs.
6. Every \(D\in\mathcal D_s\) has a disjoint member in every \(55\) pair.

All alignment claims above were exhaustively checked over the four 11-vertex normal forms: 467,696 checks, zero failures. The \(53+53\) pair/pair assertion is deliberately not made. In the all-low pair-sum branch, two \(53\) profiles are ruled out by the incidence budget; in the \((6,3,1^5)\) branch, the \(53+53\) case is handled directly by the component/gadget excess inequalities rather than by this finite alignment lemma.

Whenever a common \(D\) is found, the selected omitted sets lie in the six-set \(U\setminus D\). In pair/pair and triple alignment, the selected sets have size at least four. In a high-\(K_5\)-versus-\(53\) alignment, the selected sizes may be \(5\) and \(3\); in the \(K_3\)-versus-\(55\) alignment they are \(3\) and \(5\). In each case their sizes sum to more than six, so they intersect. The pairwise blocker theorem then forces the selected gadget-only outer vertices to be pairwise \(C\)-adjacent. Together with \(D\), they form a \(C\)-colored \(K_{12}\). Since the high row omits at most five vertices and \(D\) is disjoint from its omitted set, that \(K_{12}\) has an external \(C\)-edge, contradicting the isolated-\(K_{12}\) lemma.

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

**Theorem 11.1, Cases A/B.** The \(r_i=6\) block has a gadget-only row with omitted \(K_5\) \(E\). By Theorem 10.1, the \(r_j=3\) block may have an omitted pair of any type \(55,54,53,\) or \(44\). Use alignment fact 1 for types \(55/54\) and fact 2 for types \(53/44\). The five \(r=1\) blocks align with every \(D\). This creates a \(K_{12}\) with an external \(C\)-edge, contradiction.

**Theorem 11.1, Case C.** Write \(d_U\) for the repeated gadget-incidence excess and \(t_i=6-d_U\) for the component-incidence excess in the \(r_i=6\) block. Let \(e_i\) be the total gadget incidences in its ten component-containing rows, and let \(E,F\) be the omitted cliques of its two gadget-only rows. Each of those rows has at least six gadget neighbors, so \(|E|,|F|\le5\). Counting gadget incidences gives
\[
|E|+|F|=11-d_U+e_i,\qquad e_i\le d_U-1.
\]
Also \(|E\cap F|\le e_i\), because every gadget vertex omitted by both gadget-only rows must occur in a component-containing row.

If \(d_U\ge4\), then \(t_i\le2\). For the \(r_j=3\) block, \(e_j+t_j\le2\). A missing edge cannot cover a second full component, since \(t_i+t_j\le4\). If \(e_i+e_j\le5\), it cannot cover six gadget vertices either, so the edge is forced. If \(e_i+e_j\ge6\), then \(e_i\ge4\), and the two gadget-only rows have total size \(11+d_U-e_i\le13\); at least one has exactly six gadget neighbors, so its omitted set is a \(K_5\). Align that \(K_5\) with the \(r_j=3\) pair (of any allowed type) and the five \(r=1\) pairs to obtain the external-edge contradiction.

If \(d_U\le3\), the omitted-pair size sum is \(11-d_U+e_i\in\{8,9,10\}\). A pair of type \(53\) or \(44\) can occur only when \(d_U=3,e_i=0\); then \(E,F\) are disjoint because no component-containing row has a gadget incidence. If the high pair has type \(55\) or \(54\), use one of its \(K_5\) omitted sets and align it with the low pair, whose type may be \(55,54,53,\) or \(44\). If the high pair has type \(53\) or \(44\), use pair/pair alignment unless both pairs have type \(53\). In that exceptional \(53+53\) case, \(d_U=3,t_i=3,e_i=0\), while the \(r_j=3\) block has \(a_j=3,e_j=t_j=0\); hence \(t_i+t_j=3<5\) and \(e_i+e_j=0<6\), so a missing edge is impossible. Thus every same-component edge to the \(r_j=3\) block is forced or an external-edge contradiction occurs. Edges to the five \(r=1\) blocks are forced by the same budget argument. In the forced-edge branch, the strengthened Lemma 2.2 gives either an immediate contradiction from a partial component incidence, or ten isolated \(K_{12}\)'s and \(P_C\le42\), contradicting \(P_C=48\).

## 5. Case III: budget profile \((6,2,2,1^4)\)

There are two \(r=2\) blocks and four \(r=1\) blocks.

**Theorem 11.1, Cases A/B.** The \(r=6\) block has a gadget-only row with omitted \(K_5\) \(E\). Alignment fact 3 aligns \(E\) with the omitted pairs of both \(r=2\) blocks; the four \(r=1\) pairs align with every \(D\). This yields the external-edge contradiction.

**Theorem 11.1, Case C.** Use the same notation \(d_U,t_i,e_i,E,F\) as in Case II. If \(d_U\ge4\), then \(t_i\le2\). Each \(r=2\) block has \(e_j+t_j\le1\). If \(e_i\le3\), then for either low block \(t_i+t_j\le3<5\) and \(e_i+e_j\le4<6\), so all same-component edges are forced. If \(e_i\ge4\), the two gadget-only rows have total size \(11+d_U-e_i\le13\), so one has six gadget neighbors and an omitted \(K_5\). Align that \(K_5\) simultaneously with the two \(r=2\) pairs using alignment fact 3; the four \(r=1\) pairs align with every \(D\).

If \(d_U\le3\), an omitted pair of type \(55,54,\) or \(53\) contains a \(K_5\) omitted set, which aligns with both \(r=2\) pairs by alignment fact 3. The remaining possibility is type \(44\); it forces \(d_U=3,e_i=0\), so the two \(K_4\) omitted sets are disjoint. Alignment fact 5 then aligns this pair with the two \(r=2\) pairs simultaneously. In every aligned case there is a \(K_{12}\) with an external \(C\)-edge. In the forced-edge case, the strengthened Lemma 2.2 gives either an immediate contradiction from a partial component incidence, or ten isolated \(K_{12}\)'s and \(P_C\le42\), contradicting \(P_C=48\).

## 6. Case IV: budget profile \((7,2,1^5)\)

Let \(B_i\) be the \(r_i=7\) block, and let \(n\) be its number of gadget-only rows. Write \(t_i+u_i=7\), where \(t_i\) is component-incidence excess and \(u_i\) gadget-incidence excess. Total gadget incidence is \(11+u_i\le18\), so \(n\le3\). If \(M\) is the number of full-component occurrences in the component rows and \(q\) the number of labels represented by a full component, then
\[
t_i\ge5(M-q).
\]

- **\(n=0\) is impossible:** \(M\ge12\), \(q\le10\), so \(t_i\ge10>7\).
- **\(n=3\):** the three gadget-only rows each have exactly six gadget neighbors. Any omitted \(K_5\) aligns with the \(r=2\) pair and the five \(r=1\) pairs, contradiction.
- **\(n=2\):** if a component row contains two full components, or if \(q\le9\), then \(t_i\ge5\), so total gadget incidence is at most 13. One gadget-only row has six or seven neighbors and its omitted clique has size at least four; alignment fact 1 gives a contradiction. Otherwise \(q=10\) and no row contains two full components, but partial component incidences may still make \(t_i>0\). Let \(e_i\) be the gadget incidences in component rows. The two gadget-only rows have total size \(18-t_i-e_i\). If \(t_i+e_i\ge4\), this total is at most 14, so one row has at most seven neighbors and omits a \(K_4\) or \(K_5\); align it with the \(r=2\) pair and the five \(r=1\) pairs. If \(t_i+e_i\le3\), then \(t_i+t_j\le4<5\) and \(e_i+e_j\le4<6\) for the \(r=2\) block, so the blocker condition forces every same-component edge. Edges to the \(r=1\) blocks are forced as well. In the forced-edge branch, the ten component labels yield disjoint \(K_{12}\)'s, contradicting \(P_C=48\).
- **\(n=1\):** a double-component row would force \(t_i\ge10>7\). Thus there are 11 component rows, all ten labels appear, and one label is repeated; \(t_i\ge5\), so total gadget incidence is at most 13. If any component row has at least six gadget neighbors, the sole gadget-only row has an omitted clique of size at least four and alignment fact 1 applies. Otherwise the repeated component accounts for five of \(t_i\), leaving at most two additional component incidences in the high block. If the \(r=2\) omitted pair is type \(54\), its rows have no extra incidences; a selected high row and low row therefore cannot cover a second full component, and their at-most-five gadget incidences cannot cover six gadget vertices, so every same-component edge is forced. If the \(r=2\) pair is type \(55\), each low row has at most one extra incidence: high rows with at most four gadget neighbors again force the edge, since component excess outside the repeated component is at most \(2+1<5\) and gadget incidence is at most \(4+1<6\). If a high component row has five gadget neighbors, the gadget-only row omits a clique of size at least three and alignment fact 1 (including the \(K_3\)-versus-\(55\) check) gives an external-edge contradiction.

In the forced-edge subcases, the repeated component yields an isolated-\(K_{12}\) contradiction. Thus \((7,2,1^5)\) is impossible.

## 7. Case V: budget profile \((8,1^6)\)

Let \(B_i\) be the \(r_i=8\) block and \(n\) its number of gadget-only rows. Total gadget incidence is at most 19, so \(n\le3\). With \(M,q,t_i\) as above, \(t_i\ge5(M-q)\).

- **\(n=0\) is impossible:** \(M\ge12\) gives \(t_i\ge10>8\).
- **\(n=3\):** each gadget-only row has six or seven gadget neighbors, so one has an omitted \(K_4\) or \(K_5\). It aligns with all six \(r=1\) pairs.
- **\(n=2\):** if a row contains two full components or \(q\le9\), then \(t_i\ge5\), total gadget incidence is at most 14, and one gadget-only row has at most seven neighbors; its omitted clique has size at least four and aligns with the \(r=1\) pairs. Otherwise \(q=10\) and no double row occurs, but partial component incidences may still give \(t_i>0\). Let \(e_i\) be the total gadget incidences in component rows. The two gadget-only rows have total size \(19-t_i-e_i\). If \(t_i+e_i\ge5\), this total is at most 14, so one row has at most seven neighbors and omits a \(K_4\) or \(K_5\); align it with the \(r=1\) pairs. If \(t_i+e_i\le4\), then \(t_i\le4<5\) and \(e_i\le4<6\), so no missing same-component edge to an \(r=1\) block can cover a second full component or six gadget vertices. All such edges are forced. The strengthened Lemma 2.2 gives either an immediate contradiction from a partial component incidence, or ten isolated \(K_{12}\)'s and \(P_C\le42\), contradicting \(P_C=48\).
- **\(n=1\):** a double-component row would give \(t_i\ge10>8\). Otherwise one component is repeated, so \(t_i\ge5\) and total gadget incidence is at most 14. If a component row has at least six gadget neighbors, the gadget-only row omits a clique of size at least three and the \(K_3/K_4/K_5\)-versus-\(55\) alignment applies. If every component row has at most five gadget neighbors, the repeated component accounts for five of \(t_i\), leaving at most three further component incidences; thus no selected high-block row and an \(r=1\) row can cover a second full component. They also cover at most five gadget vertices, since the \(r=1\) row has no gadget excess. Hence every same-component edge is forced, and the repeated component yields an isolated-\(K_{12}\) contradiction.

All possible \(R_C=14\) profiles are excluded. Therefore \(P_C\ne48\), proving \(P_C\le47\). \(\square\)

## 8. Dependency firewall

- The theorem depends on the retained exact-129 factor theorem, Theorems 10.1 and 11.1, the exact 11-vertex normal form of Theorem 12.1, and the isolated-\(K_{12}\) budget lemma.
- The new finite verification is fixed-size: 467,696 alignment checks across four 11-vertex normal forms, zero failures.
- This is a colorwise conditional result. It does not close the aggregate eleven-color ledger, the 56-witness global compatibility, E408 Q33, or EG617(r=12).
