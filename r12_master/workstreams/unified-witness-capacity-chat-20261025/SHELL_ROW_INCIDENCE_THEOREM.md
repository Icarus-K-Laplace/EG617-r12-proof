# Shell-row incidence theorem and the label-transfer barrier

Date: 2026-10-25  
Status: **PROVED_ANALYTIC** for the graph-theoretic zero-excess theorem and the incidence identities below; **PROVED_CONDITIONAL** for exact-129 colour-component consequences. No terminal is closed.

## 1. Zero-excess graph theorem: audit result

Let \(H\) be the 47-vertex core with \(\alpha(H)\le4\), \(\delta(H)\ge12\), and \(e(H)\in\{284,285\}\). Write
\[
\epsilon(x)=d_H(x)-12,\quad E=\sum_x\epsilon(x)\in\{4,6\},\quad
X=\{x:\epsilon(x)>0\},\quad H_0=H-X,\quad k=|X|.
\]
Every vertex in \(H_0\) has degree exactly 12 in \(H\). In the parent T61 residual \(F\), the pivot is anticomplete to \(H\) and \(\delta(F)\ge13\), so each \(x\in H_0\) has at least one target-colour edge to the shell \(A\).

**Robust zero-excess independent-four theorem.**
- If \(e(H)=284\), then for every \(T\subseteq V(H_0)\) with \(|T|\le6\), \(\alpha(H_0-T)=4\).
- If \(e(H)=285\), then for every \(T\subseteq V(H_0)\) with \(|T|\le4\), \(\alpha(H_0-T)=4\).

Proof audit: \(1\le k\le E\), and
\[
e(H_0)\le282-\frac E2-12k+\binom k2.
\]
Removing \(t\) vertices of \(H_0\) deletes at least \(t(12-k)-\binom t2\) edges, so
\[
e(H_0-T)\le U(E,k,t):=
282-\frac E2-12k+\binom k2-t(12-k)+\binom t2.
\]
If \(\alpha(H_0-T)\le3\), then \(H_0-T\) has at least \(p_3(n)\) edges, \(n=47-k-t\), where \(p_3(n)\) is the minimum edge count of a graph on \(n\) vertices with independence number at most three, equivalently the complement of a balanced complete 3-partite graph. The exact endpoint gaps \(p_3(n)-U(E,k,t_{\max})\) are:

| Core edges | \(E\) | \(k\) | \(t_{\max}\) | \(n\) | \(p_3(n)\) | \(U(E,k,t_{\max})\) | Gap |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 284 | 4 | 1 | 6 | 40 | 247 | 217 | 30 |
| 284 | 4 | 2 | 6 | 39 | 234 | 212 | 22 |
| 284 | 4 | 3 | 6 | 38 | 222 | 208 | 14 |
| 284 | 4 | 4 | 6 | 37 | 210 | 205 | 5 |
| 285 | 6 | 1 | 4 | 42 | 273 | 229 | 44 |
| 285 | 6 | 2 | 4 | 41 | 260 | 222 | 38 |
| 285 | 6 | 3 | 4 | 40 | 247 | 216 | 31 |
| 285 | 6 | 4 | 4 | 39 | 234 | 211 | 23 |
| 285 | 6 | 5 | 4 | 38 | 222 | 207 | 15 |
| 285 | 6 | 6 | 4 | 37 | 210 | 204 | 6 |

The gap decreases with \(t\), so these endpoint checks cover every smaller deletion size. All gaps are positive, contradiction. Since \(\alpha(H_0-T)\le\alpha(H)\le4\), equality follows. The verifier independently recomputes these tables.

## 2. What the theorem gives to shell rows

For a shell row \(a\), define \(T_a=N_F(a)\cap H_0\). In the regular B-row regimes, \(|T_a|\le3\).

For every pair of regular B rows \(a,b\) in the 284-edge cases,
\[
|T_a\cup T_b|\le6.
\]
The robust theorem therefore gives an independent four-set
\[
Q_{ab}\subseteq H_0\setminus(T_a\cup T_b)
\]
anticomplete to both \(a\) and \(b\). This is a **graph-theoretic common witness**, simultaneously valid for E407 Q32 and E408 Q33. It is not automatically a monochromatic \(K_5\)-component in any exact-129 color.

For the 285-edge E408 Q32 core, the deletion theorem only allows \(|T|\le4\). A common witness is certified by this route only when the actual union \(|T_a\cup T_b|\le4\), not merely because the two rows separately have at most three neighbours.

## 3. Exact labelled row-incidence ledger

Let \(\mathcal Q\) be the selected seven-witness-per-color family and let \(r_x\) be its core multiplicity. For any shell row \(a\), write \(N_a=N_F(a)\cap U\), and define
\[
I_a=\sum_{Q\in\mathcal Q}|Q\cap N_a|,\qquad
R_a=\#\{Q\in\mathcal Q:Q\cap N_a\ne\varnothing\}.
\]
Then the exact identity and valid inequalities are
\[
I_a=\sum_{x\in N_a}r_x,\qquad
R_a\le I_a\le c|N_a|.
\]
For a regular B row with \(|N_a\cap H_0|\le3\), the zero-excess subfamily satisfies \(I_a^{(0)}\le3c\), and at most three pairwise-disjoint zero-excess witnesses of any one color can hit that row. No analogous bound of three is asserted here for witnesses containing positive-excess vertices.

If \(Q\) is labelled by \(b\in B\), then \(Q\cap N_b=\varnothing\): the label is target-anticomplete to its four-point part. A core vertex \(x\) cannot occur in two witnesses with the same label, since the shell-core edge \(bx\) would be assigned two colours. Consequently, if \(L_x\subseteq B\) is the set of distinct B labels on witnesses containing \(x\), then
\[
|L_x|\ge r_x-1,\qquad N_F(x)\cap L_x=\varnothing,\qquad
d_F(x,B)\le10-|L_x|\le11-r_x.
\]
The \(-1\) allows for at most one pivot-labelled witness containing \(x\); pivot-labelled witness parts are mutually disjoint.

For every exact-129 color, at least six B-labelled witnesses are available. At least two of those six are zero-excess, since there are at most four positive-excess vertices and the six witness parts are disjoint. The labelled-capacity theorem further shows:
- E407: at least 14 zero-excess B-labelled witnesses across the seven colors;
- E408 Q33: at least 17 across the eight colors, because at least one color has seven B-labelled witnesses and hence at least three zero-excess labelled witnesses.

The total row-hit lower bound for the zero-excess labelled family is therefore at least \(3Z_B\), using the retained theorem that each zero-excess four-set hits at least three distinct shell rows. However, the available row capacities (three core neighbours per regular B row and unrestricted hub capacities under the present contract) do not make this lower bound contradictory.

## 4. The exact label-transfer barrier

The robust graph theorem gives \(Q_{ab}\) for any two regular rows. It proves only that \(Q_{ab}\) is an independent four-set in \(H_0\), anticomplete to both rows. It does **not** assign a non-target color \(i\) for which \(\{a\}\cup Q_{ab}\) or \(\{b\}\cup Q_{ab}\) is a monochromatic \(K_5\). The exact-129 factor theorem certifies only its own monochromatic components.

Therefore no valid edge-ownership argument may count the six internal pairs of \(Q_{ab}\) as belonging to a particular exact-129 color unless a separate **label-transfer/component-realization lemma** is proved. This is the minimal logical obstacle to converting pairwise common witnesses into a global labelled capacity contradiction.


## 5. Pair-certificate multiplicity: exact bound and the remaining gap

For an independent four-set \(Q\subseteq H_0\), define
\[
B(Q)=\{b\in B:Q\cap T_b=\varnothing\},\qquad \mu(Q)=|B(Q)|.
\]
The same \(Q\) is a valid common graph-theoretic witness for every unordered pair of rows from \(B(Q)\), so its exact pair-certificate multiplicity is
\[
\boxed{\binom{\mu(Q)}2\le\binom{10}{2}=45.}
\]
This is the only unconditional multiplicity cap supplied by the present row-size assumptions: each regular row has at most three zero-excess neighbors, but that is a bound on \(|T_b|\), not on how many row neighborhoods can avoid one fixed Q. Therefore the existence of 39, 17, or 9 hub-complete pair certificates in the five E407 templates does not imply that many distinct four-sets.

If \(Q\) is an *actual selected witness* labelled by \(b\), then it can only be directly attached to the component of its exact-129 color with label b. It can be a common witness for a pair \(\{b,c\}\) only if it also avoids \(T_c\), giving at most \(\mu(Q)-1\le9\) such label-anchored pairs. This is still not a label-transfer theorem for an arbitrary \(Q_{bc}\) produced by the graph-theoretic existence result.

## 6. Hub-complete consequence of the shell missing-set union

Write \(S_b=N_M(b)\cap S\). If \(S_b\cup S_c=S\) and \(Q_{bc}\) is any common independent four-set avoiding both rows, then Q must hit every hub row in S. Otherwise some hub s missed by Q is also missed by at least one of b,c, making \(Q\cup\{b,s\}\) or \(Q\cup\{c,s\}\) an independent six-set in F.

For the retained E407 row templates, the number of full rows \(n_3\) is at least 6/2/6/1 in templates A/B/C/D respectively; whenever \(n_3\ge1\), the number of labelled row-pair certificates forced to be hub-complete is
\[
\binom{10}{2}-\binom{10-n_3}{2}.
\]
These are **pair incidences, not distinct witnesses**. A single graph-theoretic Q can account for multiple pairs up to the multiplicity bound above, and the exact-129 factor theorem does not assign its label automatically.
