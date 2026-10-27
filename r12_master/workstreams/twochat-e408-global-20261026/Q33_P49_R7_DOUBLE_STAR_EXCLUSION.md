# E408 Q33: repaired double-star exclusion of the profile (7,1^6)

Date: 2026-10-26  
Status: **PROVED_CONDITIONAL** under the retained exact-129 factor theorem, seven-block row-budget contract, row blocker theorem, and exact 11-vertex gadget normal forms.  
Scope: excludes the single colorwise profile \(P_C=49,\ (r_i)=(7,1,1,1,1,1,1)\). It does not close the other two all-component-edge-present profiles or E408 Q33 globally.

## 1. Contract and the valid star-capacity rule

Fix an exact-129 non-target color \(C\). The seven-block ledger gives
\[
P_C+\sum_{i=0}^6 r_i(C)=62.
\]
At \(P_C=49\), the seven positive integers \(r_i(C)\) sum to 13. This note treats the profile \((7,1^6)\).

The retained exact-129 factor theorem says that \(C[R]\) consists of ten isolated \(K_5\) components \(K_1,\ldots,K_{10}\) and an 11-vertex gadget \(U_C\), with
\[
\alpha(C[U_C])=2,\qquad \omega(C[U_C])=5,
\]
and no \(C\)-edges between distinct components or between a component and \(U_C\).

The valid star-capacity lemma is:
\[
Q\text{ a }C\text{-colored }K_{12},\ z\notin Q
\quad\Longrightarrow\quad d_C(z,Q)\le1.
\]
Indeed, the twelve edges from \(z\) to \(Q\) must contain each of the eleven colors other than \(C\); otherwise \(Q\cup\{z\}\) is a 13-set independent in a missing color. Thus the proof below always constructs **at least two** external \(C\)-edges from one vertex, never merely one.

## 2. Row facts used

For a block with budget \(r_i(C)=1\), the registered row theorem gives:
- ten distinct rows whose \(C\)-neighborhoods in \(R\) are exactly the ten isolated \(K_5\) components;
- two no-component rows with six gadget neighbors each;
- those two rows have no component-vertex incidences.

For a row \(b\in B_i\) containing no full \(K_5\) component, define its omitted gadget set
\[
E_b=U_C\setminus (N_C(b)\cap U_C).
\]
This is a clique of \(C[U_C]\), hence \(|E_b|\le5\). Otherwise two nonadjacent vertices in \(E_b\), one vertex outside \(N_C(b)\) from each isolated component, and \(b\) would give a 13-set independent in \(C\).

Every vertex of \(U_C\) has \(C\)-degree one or two into a target block. Therefore, for any two no-component rows \(b,b'\) in the same \(r_i=7\) block, their common gadget-neighborhood vertices each contribute one repeated incidence to \(r_i(C)\), so
\[
|N_C(b)\cap N_C(b')\cap U_C|\le7.
\]
Equivalently, their omitted cliques satisfy
\[
\boxed{|E_b\cup E_{b'}|\ge4.} \tag{1}
\]

The exact row incidence budget can be split as
\[
r_i(C)=t_i+u_i,
\]
where \(t_i\) is the component-vertex excess and \(u_i\) is the gadget-vertex excess. If \(M\) is the number of full-component occurrences among the 12 row neighborhoods and \(q\) is the number of distinct component labels represented fully, then
\[
\boxed{t_i\ge5(M-q).} \tag{2}
\]
To see this, each unrepresented component still contributes at least five \(C\)-edges into the block, and each repeated full-component occurrence contributes five additional incidences.

## 3. Finite gadget alignment lemma

For each of the four registered 11-point gadget normal forms \(b=1,2,3,4\), let \(\mathcal D_b\) be the registered universal family of \(C\)-colored \(K_5\)'s:
- \(b=1\): \(A,B\);
- \(b=2,3\): \(A,B,A'\);
- \(b=4\): \(A',B\).

The independent verifier verify_q33_p49_r7_double_star.py establishes both finite facts:

1. For every disjoint pair \(F,G\) of gadget \(K_5\)'s and every \(D\in\mathcal D_b\), at least one of \(F,G\) is disjoint from \(D\).
2. For every pair of clique sets \(E,F\subseteq U_C\) with \(|E\cup F|\ge4\), at least one of \(E,F\) has size at least two and is disjoint from some \(D\in\mathcal D_b\).

The second property is deliberately stronger than checking only disjoint \(E,F\). It is exactly what (1) needs; it also covers the single-row case where the other no-component row is absent.

Independent replay:
- normal forms \(b=1,4\): 7,376 high-pair tests each;
- normal forms \(b=2,3\): 6,314 high-pair tests each;
- 48 low-pair/\(D\) tests;
- zero failures.

This is a finite gadget certificate, not a graph-realization proof. The exact-129 factor and row facts above remain explicit theorem dependencies.

## 4. Exclusion proof

Let \(n\) be the number of rows in the \(r_i=7\) block whose \(C\)-neighborhood contains no full isolated \(K_5\) component.

### Case A: \(n=0\) is impossible

All 12 rows contain at least one full component, so \(M\ge12\). Since \(q\le10\), (2) gives
\[
t_i\ge5(M-q)\ge10>7=r_i(C),
\]
a contradiction.

### Case B: \(n\ge2\)

Choose any two no-component rows \(b,b'\), with omitted cliques \(E_b,E_{b'}\). By (1), their union has at least four vertices. The finite alignment lemma supplies one of these omitted cliques, call it \(E\), and a gadget \(K_5\) \(D\in\mathcal D_b\) such that
\[
|E|\ge2,\qquad E\cap D=\varnothing.
\]

For each of the six \(r=1\) blocks, select one no-component row whose omitted \(K_5\) complement \(G_j\) is disjoint from the same \(D\). This is possible by property 1 of the universal family.

All seven omitted sets \(E,G_1,\ldots,G_6\) lie in the six-point set \(V'=U_C\setminus D\). Since \(|E|\ge2\) and \(|G_j|=5\), each \(E\cap G_j\ne\varnothing\); also \(G_j\cap G_k\ne\varnothing\) because \(5+5>6\).

No selected row pair can jointly cover a full isolated \(K_5\): the high row has no full component, and each selected \(r=1\) no-component row has zero component-vertex incidences. Hence the pairwise blocker theorem forces every pair of selected outer rows to be \(C\)-adjacent; otherwise their common missed gadget vertex, one vertex from each of the ten components, and the two nonadjacent rows form a \(C\)-independent 13-set.

The gadget clique \(D\) is \(C\)-adjacent to all seven selected rows, so they form a \(C\)-colored \(K_{12}\), say \(Q\).

Each selected omitted set is a proper subset of \(V'\), since it is a gadget clique of size at most five. Thus the seven nonempty omission sets \(V'\setminus E,V'\setminus G_1,\ldots,V'\setminus G_6\) have total size at least seven. By pigeonhole, some \(z\in V'\) belongs to at least two sets \(V'\setminus E,V'\setminus G_1,\ldots,V'\setminus G_6\). Thus \(z\) is not omitted by those two row complements and is \(C\)-adjacent to at least two selected rows of \(Q\), contradicting star capacity.

### Case C: \(n=1\)

Eleven rows contain a full component, so \(M\ge11\). Equation (2), \(q\le10\), and \(t_i\le7\) force
\[
M=11,\qquad q=10,\qquad t_i\ge5,\qquad u_i\le2.
\]
Thus the total gadget incidence into this block is \(11+u_i\le13\). Exactly one component label is represented twice.

If any component-containing row has at least six gadget neighbors, the unique no-component row has at most seven gadget neighbors. Its omitted clique \(E\) therefore has size four or five. By the finite alignment lemma, choose \(D\in\mathcal D_b\) disjoint from \(E\); property 1 again selects one \(r=1\) no-component row per other block with omitted \(K_5\) disjoint from \(D\). The same seven-row double-star argument from Case B gives a contradiction.

Otherwise every component-containing row has at most five gadget neighbors. For any full-component row \(x_\ell\) in the high block and the unique \(r=1\) representative \(y_\ell\) of the same component \(K_\ell\) in a low block, the pair must be \(C\)-adjacent. If not, their neighborhoods cover \(K_\ell\), but at most five gadget vertices and at most two partial component vertices outside \(K_\ell\); at least six gadget vertices and all other nine components remain available. Since \(\omega(C[U_C])=5\), the remaining gadget vertices contain a nonadjacent pair, and together with one vertex from each of the other nine components and \(x_\ell,y_\ell\) this gives a \(C\)-independent 13-set.

Across low-low block pairs, the registered \(r_i+r_j\le6\) component-representative theorem forces the corresponding edges. Therefore all ten component labels have \(C\)-adjacent representatives across the six low blocks and the high block. Choose one of the two high-block representatives of the repeated component \(K_\ell\) and one representative in each low block. Together with \(K_\ell\) they form a \(C\)-colored \(K_{12}\). The other high-block representative has \(C\)-edges to all five vertices of \(K_\ell\), contradicting \(d_C(z,Q)\le1\).

All cases are impossible. Hence the profile \((7,1^6)\) is excluded under the stated contracts. \(\square\)

## 5. Scope firewall

This closes one colorwise \(P_C=49\) profile only. It does not prove \(P_C\le48\) for every exact-129 color, does not close the all-component-edge-present branches of \((4,4,1^5)\) or \((4,3,2,1^4)\), and does not close E408 Q33 or the original \(K_{145}\) theorem.
