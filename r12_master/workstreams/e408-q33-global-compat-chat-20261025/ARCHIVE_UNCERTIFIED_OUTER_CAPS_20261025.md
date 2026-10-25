# Archived outer-cap proof attempts — NOT CERTIFIED

Date: 2026-10-25

**Important:** This is a preservation copy of the former Sections 13–16 of `SEVEN_BLOCK_INCIDENCE_LEDGER.md`. These sections rely on the invalid inference that a monochromatic (K_{12}) cannot have even one external edge of its own color. Do not use any claimed (P_Cle49), (P_Cle48), or (P_C=50,r_i=6) exclusion here as a proved dependency. The valid star condition is only (d_C(z,K_{12})le1) for each outside vertex (z).

---

## 13. Isolated-\(K_{12}\) duplicate cap and exclusion of \(P_C=50,r_{\max}=6\)

**Lemma 13.1 (a monochromatic \(K_{12}\) is an isolated component).** In any balanced 12-coloring, if \(Q\) is a \(C\)-colored \(K_{12}\), then every edge from \(Q\) to a vertex \(z\notin Q\) has a color different from \(C\). Indeed, \(Q\) is independent in every color \(D\ne C\); each of the twelve edges from \(z\) to \(Q\) must contain all eleven colors \(D\ne C\), leaving exactly one duplicated color and no edge of color \(C\). Consequently, any two disjoint \(C\)-colored \(K_{12}\)'s are \(C\)-anticomplete.

**Lemma 13.2 (isolated-clique duplicate cap).** Suppose a fixed exact-129 color \(C\) contains \(m\) vertex-disjoint \(C\)-colored \(K_{12}\)'s, each containing exactly one vertex from each of the seven target blocks \(B_0,\ldots,B_6\). Then
\[
\boxed{P_C\le21(12-m).}
\]

**Proof.** Each selected \(K_{12}\) is an isolated component by Lemma 13.1. For any block pair \(B_i,B_j\), the \(m\) selected cliques contribute exactly \(m\) disjoint \(C\)-edges, one per clique, and no \(C\)-edges from their representatives to any other vertex. Put \(k=12-m\). The remaining \(k\) vertices in each block must have at least one \(C\)-neighbor in the opposite block, by the one-or-two rule; their \(C\)-neighbors can only lie among the remaining \(k\) vertices on the other side. Their bipartite \(C\)-graph therefore has minimum degree at least one and maximum degree at most two, so it has \(k\le e'\le2k\) edges. Hence
\[
e_C(B_i,B_j)=m+e'=12+d_{ij}(C),\qquad
d_{ij}(C)=e'-k\le k.
\]
Summing over the 21 block pairs proves the bound. \(\square\)

**Theorem 13.3 (the \(P_C=50\), \(r_i(C)=6\) corner is impossible).** Under the retained exact-129 and seven-block contracts, no exact-129 color \(C\) can satisfy
\[
P_C=50,\qquad r_i(C)=6
\]
for any target block \(B_i\).

**Proof.** Since \(R_C=62-P_C=12\) and all seven \(r_j(C)\ge1\), the other six blocks have \(r_j(C)=1\). Each therefore supplies, for each of \(D_1,D_2\), a gadget-row representative whose neighborhood is \(U_C\setminus E_j\), where \(E_j\) is a five-clique disjoint from that \(D\).

First suppose the \(r_i=6\) block is in Case A or Case B of Theorem 11.1. It has at least one no-component row with a six-vertex gadget neighborhood \(U_C\setminus E\), where \(E\) is a five-clique. By Theorem 12.1, \(E\) is disjoint from one of \(D_1,D_2\); call it \(D\). Then \(E\) and each low-block omitted set \(E_j\) are five-subsets of the six-set \(U_C\setminus D\), so they intersect. Pairwise blocker compatibility forces the high-block row to be \(C\)-adjacent to all six low-block representatives of type \(D\). Together with \(D\), these seven outer vertices form a \(C\)-colored \(K_{12}\). But the high-block row also has a \(C\)-edge to the unique vertex in \(U_C\setminus(D\cup E)\), which lies outside this \(K_{12}\), contradicting Lemma 13.1. Hence Cases A and B are impossible.

It remains to consider Case C. The two no-component neighborhoods \(X,Y\subset U_C\) cover \(U_C\) and have overlap \(a=|X\cap Y|\ge1\). Write \(e_i\) for the gadget incidences in the ten component-containing rows beyond their mandatory full \(K_5\)'s, and \(t_i\) for component-vertex incidences beyond the mandatory one occurrence per component. The gadget excess is \(d_U=a+e_i\), the component excess is \(d_K=t_i\), and \(d_U+d_K=6\); hence
\[
e_i+t_i=6-a\le5.
\]
Each of the ten component rows contains one full \(K_\ell\) and at most five additional vertices. For each label \(\ell\), its row and the six exact \(K_\ell\)-rows in the \(r_j=1\) blocks are forced C-adjacent by pairwise blocker compatibility, so they form a \(C\)-colored \(K_{12}\). If any of the ten high-block rows has an additional \(C\)-neighbor outside its full \(K_\ell\), this \(K_{12}\) has an external \(C\)-edge, contradicting Lemma 13.1. Otherwise all ten label-based \(K_{12}\)'s are isolated. Lemma 13.2 then gives \(P_C\le21(12-10)=42\), again contradicting \(P_C=50\). \(\square\)

**Historical scope note.** The \(P_C=50,r_i=6\) corner is excluded by Theorem 13.3. The \(P_C=49,r_i=6\) packing statement above was a conditional packing result, not a contradiction; Section 15 later excludes the entire \(P_C=49\) layer, including every \(r_i=6\) profile.


## 14. Global exact-129 duplicate cap: \(P_C\le49\)

**Theorem 14.1.** Under the retained exact-129 and seven-block contracts, every exact-129 non-target color satisfies
\[
\boxed{P_C\le49.}
\]

**Proof.**

**Step 1: \(P_C\ge51\) is impossible.** Here \(R_C=62-P_C\le11\). Since every \(r_i(C)\ge1\), for every pair \(i\ne j\),
\[
r_i(C)+r_j(C)\le R_C-5\le6.
\]
Corollary 10.2 therefore forces the two representatives of each component \(K_\ell\) to be \(C\)-adjacent across every pair of target blocks. Thus, for each of the ten labels \(\ell\), \(K_\ell\) plus its seven outer representatives forms a \(C\)-colored \(K_{12}\). If any representative row has a \(C\)-neighbor outside its \(K_\ell\), Lemma 13.1 is contradicted. Otherwise the ten \(K_{12}\)'s are isolated, and Lemma 13.2 gives \(P_C\le21(12-10)=42\). Either way, \(P_C\ge51\) is impossible.

**Step 2: \(P_C=50\) with a block \(r_i=6\) is impossible.** This is Theorem 13.3.

**Step 3: \(P_C=50\) with all \(r_i\le5\) is impossible.** Now \(R_C=12\). The only positive seven-tuples with sum 12 that have a pair sum exceeding six are
\[
(5,2,1,1,1,1,1),\qquad (4,3,1,1,1,1,1),
\]
up to permutation. In every other profile, Corollary 10.2 forces all ten label-based \(K_{12}\)'s, and the same isolated-clique argument gives a contradiction.

Consider either exceptional profile and let \(B_i,B_j\) be its unique high-budget pair, with \(r_i+r_j=7\). Every pair other than \((i,j)\) has sum at most six, so for a fixed component label \(\ell\), the seven representatives form a \(C\)-clique of size eleven with the only possibly missing edge being \(x_i(\ell)x_j(\ell)\). If that edge is present, the clique is a \(K_{12}\). If any of its seven representative rows has an extra \(C\)-neighbor outside its designated \(K_\ell\), Lemma 13.1 gives an immediate contradiction. Otherwise all ten label-based \(K_{12}\)'s are isolated, and Lemma 13.2 gives \(P_C\le42\).

Suppose instead \(x_i(\ell)x_j(\ell)\) is absent. Pairwise blocker compatibility then requires \(X_{x_i(\ell)}\cup X_{x_j(\ell)}\) to contain a second full \(K_5\) component: without it, at most \(r_i+r_j-2=5\) extra vertices leave at least six gadget vertices, which cannot have independence number at most one. Covering the second component requires at least five extra component incidences, so equality forces
\[
a_i=a_j=1,\qquad e_i=e_j=0,\qquad t_i+t_j=5.
\]
The \(a_i=a_j=1\) profiles give each of the two high-budget blocks a pair of no-component rows whose complements are disjoint \(K_5\)'s. Thus both high-budget blocks, as well as the five \(r=1\) blocks, have a row whose neighborhood contains the same fixed \(D\in\{D_1,D_2\}\). Their omitted \(K_5\)'s are all five-subsets of \(U_C\setminus D\), so they pairwise intersect. Pairwise blocker compatibility forces all seven selected outer vertices to be \(C\)-adjacent; together with \(D\) they form a \(C\)-colored \(K_{12}\), while each high-block row has an extra \(C\)-neighbor outside \(D\). This contradicts Lemma 13.1.

Therefore every label's high-pair representatives are adjacent. All ten label-based \(K_{12}\)'s follow, and the isolated-clique duplicate cap again gives \(P_C\le42\), contradiction.

The cases \(P_C\ge51\) and \(P_C=50\) are both excluded, proving \(P_C\le49\). \(\square\)

**Consequence.** For each exact-129 color, the outer residual duplicate budget obeys \(R_C\ge13\). This is a colorwise theorem; it does not yet close the aggregate E408 Q33 ledger or establish the original \(K_{145}\) result.


## 15. Exclusion of the \(P_C=49\) boundary

Under the retained seven-block equality contract and exact-129 factor theorem,
\[
\boxed{P_C\le48,\qquad R_C\ge14.}
\]
The proof is recorded in P49_BOUNDARY_EXCLUSION.md. It exhausts all positive seven-tuples with \(R_C=13\), using Theorems 10.1, 11.1 and 12.1, the isolated-\(K_{12}\) budget cap (Lemma 13.2), and the finite 11-vertex gadget alignment certificate. The exact budget profiles \((5,2,2,1^4)\), \((4,3,2,1^4)\), \((7,1^6)\), \((6,2,1^5)\), \((5,3,1^5)\), and \((4,4,1^5)\) are all excluded, as are profiles with every pair-sum at most six.

The finite verifier checks 2,156 alignment cases over the four exact gadget normal forms, with zero failures. This strengthens the colorwise duplicate-budget interface but does not close the aggregate eleven-color ledger, the 56-witness global compatibility, E408 Q33, or EG617(r=12).


## 16. Exclusion of the \(P_C=48\) boundary

Under the retained exact-129 factor theorem and seven-block equality contract,
\[
\boxed{P_C\le47,\qquad R_C\ge15.}
\]
The proof is recorded in P48_BOUNDARY_EXCLUSION.md. It assumes \(R_C=14\) and exhausts the positive seven-tuples:
\[
\begin{aligned}
&r_i\le5\ \text{for all }i;\\
&(6,3,1^5),\ (6,2,2,1^4),\ (7,2,1^5),\ (8,1^6).
\end{aligned}
\]
For the all-low case, a missing component edge either incurs at least five component-excess incidences or requires at least six gadget incidences; the resulting omitted-pair types are covered by the finite pair/pair and triple alignment certificates. The high-budget profiles are excluded using Theorem 11.1 and full-component occurrence counts.

The expanded fixed-gadget verifier checks 467,696 alignment cases across the four exact 11-vertex normal forms, with zero failures. The \(53+53\) pair/pair exception is not universally alignable and is not used as an alignment lemma: the all-low occurrence is excluded by the pair-sum budget, while the \((6,3,1^5)\) occurrence is handled directly by its component/gadget excess inequalities. The proof also does not assert that every high \(K_4\) aligns with every low \(53\) pair. The audited P48 proof now distinguishes total repeated gadget incidence \(d_U\), component-row gadget incidence \(e_i\), and overlap/uncovered vertices; it no longer assumes that the two gadget-only rows cover \(U_C\) in the \(r_i=6\) Case C. The \(r_i=7,8\) cases also allow \(t_i>0\) when all ten component labels occur once, and split the \(n=2\) branch by \(t_i+e_i\).

**Scope:** \(P_C\le47\) is a colorwise conditional result. It does not close the aggregate eleven-color ledger, the 56-witness support geometry, E408 Q33, or EG617(r=12).
