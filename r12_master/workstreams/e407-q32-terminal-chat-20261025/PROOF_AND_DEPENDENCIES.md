# E407 Q32 terminal — proof and dependency ledger

Date: 2026-10-25  
Status: **E407 Q32 OPEN / NOT_CERTIFIED; all four-partite \(\delta=14\) branches (\(\epsilon_U=0,1,2\)) and the retained \(\delta=15,\delta=16\) branches are excluded under their stated contracts.**

## 1. Dependency chain currently supported

1. **T61 shell reduction** (inherited, conditional on the registered V12 retained-seed contract) gives a 61-vertex residual, pivot, shell, and 47-point core.
2. **Exact-129 factor theorem** (inherited Kang–Pikhurko equality-classification contract) gives seven disjoint independent 4-set witnesses per exact-129 color on the minimum-support boundary.
3. **Linearity** follows because two witnesses sharing two core vertices would assign their common edge two non-target colors; within a color, selected \(K_5\) components are disjoint.
4. **Support boundary** gives \(|U|=29, |W|=18\) in the unresolved \(129^7,130^4\) profile.
5. **Exact core ledger** gives
   \[
   e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,\quad e(H[W])=48-\epsilon_U-\delta.
   \]
6. **Sibling transversal/excess theorem** gives \(\epsilon_U+2\delta\ge9\) and \(\delta\ge3\), under the same boundary contract.
7. **Four-partite reduction at \(\delta=16\)**: \(L=\overline{H[U]}\) has 310 edges, exceeding the non-four-partite Brouwer threshold 309, so it is four-partite. The 49 linear witnesses force \(U\)-part sizes \(7,7,7,8\); the exact ledger forces \(H[W]=K_5\cup K_5\cup K_4\cup K_4\).
8. **Reverse saturation**: under this structure, every \(w\in W\) is adjacent to all vertices of exactly one \(U\)-part. This is proved from \(\alpha(H)\le4\), the matching structure of the five \(U\)-cross-edges, and the total excess budget.
9. **Endpoint-split terminal exclusion**: the \(4+1\) and \(3+2\) allocations contradict the four-unit excess budget. In the \(5+0\) allocation, at most one endpoint-\(K_4\) vertex can fail to be complete to the 8-part; the one-exception case contradicts the requirement that each \(U\)-vertex be complete to a whole \(W\)-clique component. Hence all four endpoint-\(K_4\) vertices are complete to the 8-part, producing a forbidden \(K_{12}\). See DELTA16_K12_CLIQUE_OBSTRUCTION.md for the standalone proof.

## 2. Exact external/input dependencies

- The V12 finite certificate is COMPUTATION_CERTIFIED / independently replayed, not an analytic proof of every screen rule and not a completed-core certificate.
- The exact-129 \(K_5\)-component structure is conditional on the registered constrained second-Turán/Kang–Pikhurko classification. This line does not reprove that extremal theorem.
- Brouwer's second-Turán bounds are used with the exact \(K_5\)-free/non-four-partite hypotheses stated at each application.
- The arithmetic verifier checks exact ledgers, partition profiles, and excess inequalities only. It is not a graph-realization certificate and does not independently verify the combinatorial lemmas.

## 3. Open edges in the proof DAG

\[
\begin{aligned}
&\text{Original }K_{145}\text{ counterexample}\\
&\Downarrow\ \text{T61 reduction + retained lower-order inputs}\\
&\text{E407 Q32 shell template A/B/C/D/E}\\
&\Downarrow\ \text{49 linear independent }K_4\text{ witnesses}\\
&|U|=29,\ |W|=18,\ 3\le\delta\le16\\
&\Downarrow\\
&\begin{cases}
\delta=16:\ \text{excluded by endpoint-split excess + forbidden }K_{12},\\
\delta=15,\ L\text{ non-four-partite}:\ \text{excluded by KP equality + incompatible }x,y\text{ degrees into }W,\\
\delta=15,\ L\text{ four-partite}:\ \text{excluded by final }K_3\cup K_5^3\text{ label-count contradiction},\\
\delta=14,\ L\text{ four-partite},\ \epsilon_U=0:\ \text{all four W profiles excluded},\\
\delta=14,\ L\text{ non-four-partite},\ \epsilon_U\in\{1,2\},\ \delta\le13:\ \text{OPEN}.
\end{cases}\\
&\Downarrow\ \text{remaining }K_{11}\text{ shell incompatibility at }\delta=15\text{, plus all }\delta\le14\text{ cases}\\
&\text{E407 Q32 excluded}\quad\text{(NOT YET PROVED).}
\end{aligned}
\]

There is no circular dependency in the \(\delta=16\) exclusion: it uses only the E407 core contract, 49-block linearity, the exact ledger, Turán/Brouwer bounds, \(\alpha(H)\le4\), and the inherited \(\omega(H)\le11\) bound from the T61 parent. The \(\delta=15\) non-four-partite exclusion additionally depends on the Kang–Pikhurko equality classification and W-side Brouwer bound. All remaining cases depend on the upstream validity of the 49-witness boundary.

### Delta-14 four-partite closures

The proofs DELTA14_EPS0_K4_PROFILE_EXCLUSIONS.md, DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md, and DELTA14_EPS0_K3K5K5K5_CROSS_EDGE_CLOSURE.md close the entire \(\delta=14,\epsilon_U=0\), four-partite row. The last profile is excluded by a common-neighbour capacity bound of 27, below \(|U|=29\).

DELTA14_EPS1_K3K5K5K5_NO_CROSS_EDGE.md additionally excludes the no-cross-edge \(K_3\cup K_5^3\) profile at \(\epsilon_U=1\). Other \(\epsilon_U=1\) W profiles, \(\epsilon_U=2\), non-four-partite \(L\), and \(\delta\le13\) remain open.

### Round 10 — final \(\delta=14,\epsilon_U=0\) four-partite profile

DELTA14_EPS0_K3K5K5K5_CROSS_EDGE_CLOSURE.md proves the last W-profile impossible. It first uses \(\alpha(H)\le4\) and the unique W-cross-edge to show every \(D\)-vertex is complete to a W-component, hence \(t_d\le2\). This yields the reverse-saturation bound \(d_H(w,U)\ge12\) for any W-vertex not complete to a U-part. The only possible unsaturated U-vertex has the exact endpoint singleton pattern in the \(K_3\)-to-\(K_5\) edge case; its induced common-neighbour demand exceeds the two other K5 capacities by one. With all U-vertices saturated, the four component capacities total at most 27, contradicting \(|U|=29\). The arithmetic verifier checks the finite excess and capacity arithmetic but does not replace the analytic proof.

### Round 11 — \(\delta=14,\epsilon_U=1\) no-cross-edge profile

DELTA14_EPS1_K3K5K5K5_NO_CROSS_EDGE.md gives a conditional contradiction by covering \(U\) with the four common-neighbour sets. It proves \(t_d\le3\), a reverse-saturation floor \(d_H(w,U)\ge11\), the K5 capacity \(|S_i|\le5+E_i\), and the K3 cap \(|S_0|\le10+\lfloor E_0/3\rfloor\). The total capacity is at most 28, less than \(|U|=29\). The arithmetic verifier checks all 20 nonnegative W-excess allocations.

### Delta-14 cross-edge placement refinement
The theorem DELTA14_EPS0_K3K5X1_K5K5_EDGE.md excludes the \(K_3\cup K_5^3\) W-profile when its single cross-edge joins two \(K_5\) components. In that placement the four W-component common-neighbour sets must cover all 29 U vertices, but the excess-budget upper bound is at most 27. Only the placement joining \(K_3\) to a \(K_5\) remains in the \(\delta=14,\epsilon_U=0\), four-partite row. The latter remains OPEN.


### Complete delta-14, epsilon_U=0 four-partite W-row exclusion
DELTA14_EPS0_K3K5X1_K3K5_EDGE.md excludes the last profile \(K_3\cup K_5^3\) with the cross-edge between \(K_3\) and \(K_5\). Together with the preceding three profile exclusions, this eliminates every four-partite \(H[W]\) profile at \(\delta=14,\epsilon_U=0\), under the retained support-boundary and witness contract. It does not eliminate \(\delta=14,\epsilon_U=1,2\), the non-four-partite branch, or \(\delta\le13\).


### Round 12 — \(\delta=14,\epsilon_U=1\), no-cross-edge \(K_4^3\cup K_6\)

DELTA14_EPS1_K4K4K4K6_NO_CROSS_EDGE.md excludes this profile using D-component assignments and the exact external-incidence identity \(R=1-2q+\sum_{d\in D}\epsilon_d\). This gives \(R\le2\) and forces every K4 component receiving at least three D assignments to have too many non-D-complete vertices; the four-unit W-excess contradiction follows. Together with the prior \(K_3\cup K_5^3\) exclusion, only the \((4,4,5,5)\)+one-cross-edge W-profile remains in the four-partite \(\delta=14,\epsilon_U=1\) row.


### Round 13 — complete \(\delta=14,\epsilon_U=1\) four-partite W-row

DELTA14_EPS1_K4K4K5K5_ONE_CROSS_EDGE.md excludes the remaining \((4,4,5,5)\)+one-cross-edge profile. The exact D-assignment count gives \(q_5\le2\), so at least six D vertices are assigned to the two K4 components. The external-incidence budget \(R=1-q_5+\sum_D\epsilon_d\le2\) prevents a K4 receiving \(k\ge3\) D assignments from having enough vertices complete to all of D; its remaining vertices force more than the three available W-excess units.

DELTA14_EPS1_W_PROFILE_CLASSIFICATION.md proves the W-profile list is exhaustive under Brouwer's second-Turán theorem: \(\overline{H[W]}\) is K5-free with 120 edges; the non-four-partite cap is 118, below 120; the only four-partite profiles are \(K_3\cup K_5^3\), \(K_4^3\cup K_6\), and \((4,4,5,5)\) with one missing cross-edge in the complement. Each of these three H[W] profiles has now been excluded. Hence the full \(\delta=14,\epsilon_U=1\), four-partite row is closed under the retained contracts and Brouwer's theorem.


### Delta-14 no-W-cross-edge profiles at \(\epsilon_U=1,2\)
DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md excludes four further profiles by cover-capacity contradictions: \(K_3\cup K_5^3\) for both \(\epsilon_U=1,2\), \(K_4^3\cup K_6\) for \(\epsilon_U=1\), and \(K_4\cup K_4\cup K_5\cup K_5\) for \(\epsilon_U=2\). The only remaining four-partite W-profile at \(\delta=14\) is \(\epsilon_U=1\), \(K_4\cup K_4\cup K_5\cup K_5\) with one W-cross-edge. This is conditional on the retained support-boundary/witness contract and the listed W-profile classification.


### Round 14 — full \(\delta=14\), four-partite row

DELTA14_EPS2_W_PROFILE_CLASSIFICATION.md closes the \(\epsilon_U=2\) case. The exact ledger gives \(e(H[W])=34-\epsilon_U=32\), and \(\alpha(H[W])\le4\) forces equality in Turán's bound. Thus the only profile is \(K_4\cup K_4\cup K_5\cup K_5\) with no cross-edges. Section 5 of DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md proves the common-neighbour capacity is at most 24, contradicting \(|U|=29\).

The source note's Section 3 mention of \(K_3\cup K_5^3\) at \(\epsilon_U=2\) is inconsistent with the exact ledger (that profile has 33 edges); it is explicitly excluded from this branch's admissible profile list and is not used.

**Current structural frontier under the retained core/witness contract:** all four-partite cases at \(\delta=14\) are excluded for \(\epsilon_U=0,1,2\); \(\delta=15\) and \(\delta=16\) are excluded in their retained branches. The open front-end cases are \(\delta=14\) non-four-partite and \(\delta\le13\). E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


### Round 15 — \(\delta=14\) non-four-partite augmentable-edge reduction

DELTA14_NONPARTITE_AUGMENTABLE_EDGE_REDUCTION.md proves a strict conditional reduction. If a non-four-partite \(L\) with \(e(L)=308\) has any nonedge \(uv\) whose addition preserves \(K_5\)-freeness, then \(L+uv\) is a 309-edge Brouwer/Kang–Pikhurko equality graph. The 49-witness packing rules out the two unbalanced base profiles, forcing the balanced \((7,7,7,7)\) base. The exact exceptional-vertex \(W\)-degree sum and the exhaustive \(\epsilon_U\)-dependent \(W\)-profile list then leave only \(\epsilon_U=1\), \(H[W]=K_3\cup K_5^3\), \(x,y\) both complete to the \(K_3\), \(uv\cap\{x,y\}=\varnothing\), and \((a,\epsilon_x,\epsilon_y)\in\{(3,1,0),(4,0,1)\}\). The added edge also forces a third vertex into the \(K_3\)'s common neighbourhood.

The standard-library verifier checks the finite integer degree/status enumeration. The proof remains conditional on the retained T61/49-witness contract and the cited Brouwer/Kang–Pikhurko results. It does not eliminate the residual terminal or the \(K_5\)-saturated case.


### Round 16 — close the \(\delta=14\) augmentable-edge branch

DELTA14_NONPARTITE_AUGMENTABLE_TERMINAL_CLOSURE.md closes the sole augmentable-edge terminal from Round 15. The four common-neighbour sets of \(C_0\cong K_3\) and \(C_1,C_2,C_3\cong K_5\) partition \(U\), since every \(u\in U\) must be complete to a W-component and \(d_H(u,W)\le6<8\). The new label-capacity lemma gives \(n_i\le4+E_i\) for a U-part-saturated \(K_5\) component, with equality in the former \(5+E_i\) bound impossible; an unsaturated \(K_5\) component has \(n_i\le7\). The \(E_0+E_1+E_2+E_3=3\) case split excludes all saturated, single-unsaturated, exceptional mixed, and multi-unsaturated patterns. The finite arithmetic bounds are replayed by verify_delta14_augmentable_terminal.py.

**Dependency boundary:** this closes only the augmentable-edge subcase, conditional on the balanced KP equality reduction, the 49-witness contract, the exact U/W degree ledger, \(\alpha(H)\le4\), and \(\omega(H)\le11\). The \(K_5\)-saturated branch remains open, as do \(\delta\le13\), all five shell templates, and the original \(K_{145}\)-to-T61 bridge.


## Round 17 dependency addition — \(\delta=14\) saturated alpha-critical reduction

The new file DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md introduces one explicit external dependency:

- Maksim Didin, *A Generalization of Turán's Theorem for Graphs with a Given Independence Number*, author-prepared preprint, Zenodo record 22831382, version 1 dated 2026-09-18. The Zenodo description states that the manuscript was submitted to the Journal of Graph Theory and was under review at that date.
- Used statement: for a graph with \(n\) vertices, \(m\) edges, independence number \(\alpha\), and \(p\) the maximum number of components among spanning \(\alpha\)-critical subgraphs with the same independence number, put \(s=\alpha-p\). Then \(m\ge t(n+s,\alpha)-s\).
- This statement is **not independently reproved or audited** in this workstream; any conclusion using it remains conditional until the theorem is independently checked or accepted as a trusted external result.

With that dependency, the \(\delta=14\) \(K_5\)-saturated non-four-partite branch reduces to \(K_7\dot\cup K_7\dot\cup D\), where \(D\) is a connected \(\alpha\)-critical graph with independence number two and 56 edges. The complement of \(D\) must be triangle-free, non-bipartite, triangle-saturated, have 49 edges, and admit the two orthogonal near-perfect matching decompositions forced by the witness family. This remains an open terminal, not a proof of EG617.


## Round 18 local-model update

DELTA14_SATURATED_LOCAL_MODEL.md and its standard-library verifier give an explicit local realization of the 29-point saturated non-four-partite boundary. No new external theorem is used in that construction. The verifier checks \(e(H_U)=98\), \(e(L)=308\), \(K_5\)-freeness and \(K_5\)-saturation of \(L\), the 49-cell bijection to \(E(J)\), and the seven classes of seven pairwise-disjoint witnesses.

This refutes any proposed contradiction based solely on the 29-point saturated graph and its 49-witness packing. It does **not** provide the 18-vertex \(W\), full 47-core, or shell-row extension. The Didin preprint dependency in DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md remains explicit and unaudited; the global terminal remains open.


## Round 20 — candidate-specific full-core extension exclusion

DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md proves, under the retained core contract and the explicit local model in DELTA14_SATURATED_LOCAL_MODEL.md, that no W-extension exists for epsilon_U=1 or 2. Combined with the independent-transversal exclusion of epsilon_U=0 in DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md, the explicit (5,5,2,1,2) blow-up has no full 47-core extension.

The new arithmetic verifier checks only finite profile enumeration, forbidden-transversal fractions, and A/B assignment-count patterns; it does not machine-check the analytic independent-set arguments. The Didin preprint dependency in DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md remains unaudited. Most importantly, the saturated-kernel reduction does not prove all admissible J's are the explicit blow-up. Therefore this does not close the general delta=14 saturated branch, any of the five shell templates, delta<=13, or the K145-to-T61 bridge.


## Round 21 — C5-blow-up subclass

DELTA14_C5_BLOWUP_PROFILE_CLASSIFICATION.md classifies the C5-blow-up subclass by exact finite enumeration of positive five-part compositions with total 15, edge count 49, and Delta(J)<=7. Seven dihedral classes satisfy the vertex/edge ledger before the degree cap; exactly one survives the cap, the (1,2,5,5,2) profile. The verifier confirms the finite enumeration only. Combining with Round 20 excludes every full-core extension in this subclass. The general J terminal remains open because triangle-free saturated graphs need not be C5 blow-ups.


## Round 22 — general 15-vertex saturated-kernel classification

DELTA14_SATURATED_KERNEL_CLASSIFICATION.md proves that every triangle-free, non-bipartite, triangle-saturated \(J\) with \(n=15,e=49,\Delta\le7\) is the C5 blow-up with part sizes \((1,2,5,5,2)\). The proof uses:
- the AES equality case: a triangle-free graph with minimum degree at least \(2n/5\) is bipartite or the balanced C5 blow-up (for \(n=15\), \(C_5(3)\) has 45 edges);
- the Brouwer/Kang–Pikhurko bound \(e(G)\le t_2(14)-7+1=43\) for a non-bipartite triangle-free graph on 14 vertices;
- the saturation and \(\Delta\le7\) deductions in the new note.

References:
- Keevash and Sudakov, “Sparse halves in triangle-free graphs,” JCTB 96 (2006), Section 3, p. 617: https://people.maths.ox.ac.uk/keevash/papers/sparse-halves-journal.pdf
- Kang and Pikhurko, “Maximum \(K_{r+1}\)-free graphs which are not \(r\)-partite,” Matematychni Studii 24 (2005), Theorem 1: https://matstud.org.ua/texts/2005/24_1/24_1_012_020.pdf

Combining this classification with DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md conditionally excludes the entire saturated non-four-partite delta=14 terminal. The arithmetic verifier checks the finite numerical deductions only. The upstream reduction to the 15-vertex kernel still depends on Didin's 2026 preprint theorem in DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md; its proof has not been independently audited in this workstream. E407 Q32 overall, delta<=13, the five shell templates, and the K145-to-T61 bridge remain open.
