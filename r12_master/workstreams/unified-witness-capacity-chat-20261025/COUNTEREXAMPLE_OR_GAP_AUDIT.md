# Counterexample / gap audit for the unified witness-capacity route

Date: 2026-10-25  
Status: **No graph counterexample found or claimed.** The integer relaxations below show that the present scalar ledgers are mutually consistent; they are not graph-realization certificates.

## 1. The edge-ownership identity is correct but not yet sharp enough

For \(N=7c\) linear independent four-sets, the exact crossing load is
\[
\sum_{xy\in E(H[U])}r_xr_y
=\sum_{i<j}e_H(Q_i\setminus Q_j,Q_j\setminus Q_i)
\ge4\binom N2-\sum_x\binom{r_x}{2}.
\]
At the two support boundaries, the lower bounds are 4122 (E407) and 5412 (E408 Q33) after the omission-capacity refinements. A valid generic upper bound is
\[
\sum_{xy\in E(H[U])}r_xr_y\le c^2e(H[U]).
\]
The current ledgers allow \(e(H[U])=112-\delta\) for E407 and \(129-\delta\) for E408 Q33; these upper bounds remain above the crossing lower bounds. Therefore the crossing inequality alone does not close either terminal.

## 2. Explicit integer omission relaxations that survive

### E407 Q32, \(S=\epsilon_U+2\delta=9\)

Take omission multiplicities
\[
(o_x)=(4,2,1,0^{26}).
\]
They sum to 7, each is at most 6, and \(\Omega=\sum_x\binom{o_x}{2}=6+1=7\). Hence \(r_x=7-o_x\) sums to 196 and the support has 29 points. The row-degree lower bound is
\[
5n_0+2n_1=5\cdot26+2=132\le e_H(U,W)=124+9=133.
\]
Choose the scalar core ledger \(\epsilon_U=3,\delta=3\): then \(\epsilon_U+2\delta=9\), \(\epsilon_U+\delta=6\le16\), \(e(H[U])=109\), \(e_H(U,W)=133\), and \(e(H[W])=42\ge p_4(18)=32\). The capacity bound is \(e(\overline{H[U]})=297\le307=310-\epsilon_U\). All stated scalar inequalities are consistent.

### E408 Q33, \(S_0=\epsilon_U+2\delta=12\)

Take
\[
(o_x)=(6,2,2,2,2,2,2,2,2,2,0^{21}).
\]
These 31 values sum to 24, with \(\Omega=15+9=24\). Thus \(r_x=8-o_x\) sums to 224. The row-degree lower bound is
\[
6n_0+3n_1=6\cdot21=126=e_H(U,W)=114+12.
\]
Choose \(\epsilon_U=4,\delta=4\): then \(S_0=12\), \(\epsilon_U+\delta=8\le17\), \(e(H[U])=125\), \(e_H(U,W)=126\), and \(e(H[W])=33\ge p_4(16)=24\). Also \(e(\overline{H[U]})=340\le349=353-\epsilon_U\). All scalar ledgers and the new omission-capacity inequality are consistent.

These profiles do **not** specify the 4-uniform witness blocks, the graph \(H\), shell rows, or color assignments. They are not counterexamples to EG617 and do not show that the terminal exists. They establish only that further work must use incidence geometry or labelled row structure, not these scalar inequalities alone.

## 3. Label-count relaxation is also feasible

For E408, the new pivot-label capacity forces at least 49 B-labelled witnesses among 56 selected witnesses. A 0–1 label-incidence matrix can have row sums \((7,6,6,6,6,6,6,6)\) and column sums
\[
(6,6,5,5,5,5,4,4,5,4),
\]
so each color uses six or seven distinct B labels, every label occurs at most seven times, and the total is 49. This meets the known label-count capacities. It does not construct witness blocks with the required intersections.

## 4. Exact missing proposition

The zero-excess theorem proves that every pair of regular B rows has some common independent four-set avoiding both rows. It does not make that set a component of any exact-129 non-target color. The exact-129 factor theorem certifies only its own monochromatic components.

A complete unified contradiction needs at least one of the following new results:

1. **Label-transfer/component-realization lemma:** a common zero-excess independent four-set for specified regular rows can be assigned to an exact-129 color component while preserving edge ownership; or
2. **Hub-capacity theorem:** an upper bound on the number of distinct shell rows/hubs that can be hit by the labelled zero-excess witnesses, counting each shell-core edge and each core vertex only once; or
3. **Incidence-design exclusion:** prove that the omission profiles and same-label disjointness constraints cannot be realized by a linear 4-uniform family whose blocks are transversals of every core vertex in \(W\).

No such proposition is established in this workstream yet. The smallest failure is the label-transfer gap: the graph-theoretic witness is unlabelled, while the colour-unique edge-ownership argument applies only to actual monochromatic \(K_5\) components.


## 5. Cross-workstream audit: four-partite Q33 has a stricter labelled profile

The latest E408 Q33 global-compatibility workstream proves, under its explicit four-partite contract, \(S_0\ge22\) and hence \(9\le\delta\le17\). This workstream adds the following exact consequences:

- The 56 transversals force \(r=8\) on the size-seven part and \(r=7\) on each size-eight part.
- The color omission triples partition the 24 large-part vertices, so \(\Omega=0\).
- A shell label \(b\) occurring in \(n_b\) selected witnesses has at most \(7-n_b\) target neighbors in the size-seven part and at most \(8-n_b\) in each size-eight part. In particular, if \(n_b=7\), its target neighborhood in U is confined to at most three vertices, one per large part.
- At each vertex of the size-seven part, the eight incident witness labels are distinct; it has at most three B-row target neighbors, or at most two if no pivot-labelled witness contains it. Thus \(e_F(B,D)\le14+P\le21\).

The earlier scalar Q33 relaxation \((o_x)=(6,2^9,0^{21})\), with \(\Omega=24\), therefore cannot lie in the four-partite branch. It remains only a witness that the *unlabelled scalar inequalities* do not exclude the non-four-partite branch; it is not a graph or hypergraph counterexample.

## 6. Why the edge-charge route is not enough in the four-partite branch

For any four-partite witness system, the within-part target edges contribute exactly \(4-s_{ij}\) edges for every pair of witnesses with intersection size \(s_{ij}\). Thus the generic pairwise crossing lower bound is attained by those within-part edges. In Q33 the exact weighted crossing load is \(5460+49(24-\delta)\), while the lower bound is exactly \(5460\). The current \(\delta\in[9,17]\) leaves this inequality consistent.

**Minimal obstruction recorded:** the current proof has no theorem forcing an additional *labelled* incompatibility among the 24 unused cross-part pair slots or the B-row neighborhoods. Re-summing the same unlabelled crossing costs cannot close the four-partite branch. The non-four-partite branch still requires a packing/stability theorem beyond the second-Turán bound.


## 7. Shell-row pair multiplicity audit

For a fixed independent four-set Q, let \(\mu(Q)\) be the number of regular B rows to which Q is anticomplete. It can certify at most \(\binom{\mu(Q)}2\le45\) unordered row pairs. The regular-row bound \(|T_b|\le3\) does not improve this to a smaller universal number: it controls each row's neighborhood size, not the union of rows avoided by Q.

If Q is a selected exact-129 witness with label b, the component label anchors it directly only to pairs containing b; there are at most \(\mu(Q)-1\le9\) such pairs. The zero-excess existence theorem does not turn its arbitrary pair witness \(Q_{bc}\) into one of these labelled components. This is a separate multiplicity/label-transfer gap, not an arithmetic gap.


## 8. Explicit label-array relaxation that survives

The Q33 four-partite label constraints alone are feasible. Index the eight exact-129 colors by \(0,\ldots,6,*\), the seven D-points by \(0,\ldots,6\), and seven of the ten B labels by \(b_0,\ldots,b_6\). Define the 7-by-7 pivot-color subarray by
\[
\lambda(i,j)=
\begin{cases}
p,&i=j,\\
b_{i+j\pmod 7},&i\ne j,
\end{cases}
\]
and the non-pivot color row by \(\lambda(*,j)=b_{2j\pmod7}\).

This array has the required label-only properties:
- each of the seven pivot rows contains p once and six distinct B labels;
- the non-pivot row contains seven distinct B labels;
- each D column contains p once and all seven B labels once;
- each B label occurs exactly seven times, and p occurs exactly seven times.

Thus the row/column no-repeat conditions and the label-capacity bound are not contradictory. This is **only a label-array relaxation**: it does not assign the actual A1/A2/A3 coordinates of the 56 K4s, so it is not a witness-hypergraph or colored-graph construction. The unresolved geometric condition is that every label class, every color class, and every D-column must simultaneously form the required disjoint transversal systems with all pairwise coordinate pairs unique.


## 9. New outer exceptional-row coupling bound

For any exact-129 color C and block pair (i,j) with both \(r_i(C),r_j(C)\le3\), the ten isolated K5 components force ten C-colored matching edges between the blocks. The two exceptional rows on each side have complementary gadget cliques \(A_i,B_i\) and \(A_j,B_j\). Every nonempty intersection among these four cliques forces the corresponding exceptional-row edge to be C-colored. If the 2x2 intersection mask has k nonempty cells, ell occupied rows and c occupied columns, then
\[
d_{ij}(C)\ge k+\max(2-\ell,2-c)-2.
\]
This is zero for a single cell or a two-cell matching, one for an adjacent two-cell mask or any three-cell mask, and two for the full mask. Hence the sum of these forced costs over all exact colors low-slack on the same block pair is at most 12.

**Gap remains:** no proof yet excludes the one-cell / matching patterns simultaneously across the seven blocks. The new inequality is a branch filter, not an UNSAT certificate.


## 10. Exceptional-row graph alpha-two constraint

For one exact-129 color C, take both exceptional rows from every low-slack outer block. Their induced C-graph has independence number at most two. Any independent triple would have pairwise-disjoint complementary cliques in the 11-point gadget; this forces at least22 gadget incidences but the three rows have at most24 total incidences, leaving at most two incidences in the ten isolated K5 components. Thus no K5 component can be fully covered, and one vertex from each component plus the triple contradicts alpha(C)<=12.

For k low-slack blocks, the exceptional-row graph has at least k(k-1) C-edges. If equality holds, it is exactly two disjoint K_k cliques, with the two exceptional rows in every block on opposite sides. This identifies the exact zero-excess pattern; deviations consume duplicate budget but are not yet ruled out.


## 11. Near-complete component matching under \(r_i,r_j\le5\)

For an exact-129 color C, each outer block with \(r_i(C)\le5\) has one row containing each isolated K5 component \(K_\ell\). The total extra row-neighborhood incidence beyond the ten K5 baselines and two six-incidence exceptional baselines is \(r_i(C)-1\).

If the same-label representatives of \(K_\ell\) in blocks i,j are nonadjacent, then unless their extra neighborhoods cover a second K5 component (five incidences), at least six gadget vertices must be covered to leave at most five vertices in the 11-point gadget. Thus each missing diagonal costs at least five extra incidences. Across distinct labels the charges use distinct row incidences, so
\[
m_{ij}(C)\le \left\lfloor\frac{r_i(C)+r_j(C)-2}{5}\right\rfloor\le1.
\]
This extends the full matching result from \(r_i+r_j\le6\) to a near-matching result for every pair with \(r_i,r_j\le5\).

Boundary refinement (2026-10-25): Theorem 8.1 now proves that a missing diagonal does imply \(d_{ij}(C)\ge1\). If \(d_{ij}=0\), the 12 edges form a perfect matching; with one missing component diagonal, this forces an independent triple of exceptional rows. The missing diagonal uses at least five of the at-most-eight extra row incidences, leaving at most three, too few to cover any K5 component; one vertex from each of the ten components plus the triple contradicts \(\alpha(C)\le12\). This closes the previous edge-ownership gap for \(r_i,r_j\le5\), but does not yet yield a global terminal contradiction.


## 12. Explicit scalar relaxation: aggregate budgets do not force a high-P exact color

To audit the tempting inference “\(\sum_{C\text{ exact}}P_C\ge69\), therefore some exact color has \(P_C\ge36\),” an explicit integer relaxation was constructed. It satisfies all of the following **aggregate ledgers** simultaneously:

- eight exact colors each have \((P_C,R_C,s_C)=(9,53,0)\);
- three nonexact colors have \((P_C,R_C,s_C)=(59,2,1),(60,1,1),(61,0,1)\);
- every color satisfies \(P_C+R_C+s_C=62\);
- \(\sum_C P_C=252\), \(\sum_C R_C=427\), and \(\sum_C s_C=3\);
- the seven block-column totals satisfy \(\sum_C r_i(C)=61\) for every outer block;
- an explicit 11-by-21 nonnegative integer \(d_{ij}(C)\) ledger exists with \(\sum_C d_{ij}(C)=12\) for every block pair and the stated \(P_C\) row sums.

For the eight exact colors, the seven \(r_i(C)\) values can all be chosen in \(\{7,8\}\) (four 8s and three 7s), so no pair falls under the \(r_i,r_j\le5\) near-matching theorem. The aggregate bound \(P_{\rm exact}\ge69\) therefore does not force a single exact color into the low-budget structural regime.

The verifier independently checks this integer relaxation. It is **not** a graph-level counterexample: it does not realize the K5 components, gadget neighborhoods, target-core witness sets, or all graph constraints. Its role is to prove that scalar edge budgets alone cannot close the theorem; the missing ingredient must couple the nonexact colors or witness geometry to the exact-color block rows.
