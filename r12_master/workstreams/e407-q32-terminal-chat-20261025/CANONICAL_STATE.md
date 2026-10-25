# Canonical state — E407 Q32 terminal workstream
Date: 2026-10-25  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-e407-q32-terminal-20261025  
Directory: r12_master/workstreams/e407-q32-terminal-chat-20261025/
## Headline
**EG617(r=12): OPEN / NOT_CERTIFIED. E407 Q32: OPEN.**
## Live sibling heads read
- emergency sprint: 5258c5fe17af3bf17eb7a2bfb08315c9be9116cd
- ultimate closure: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40
- witness packing: f5d3daa07403877ede9885e1bd5c2f46b16d81da
- zero-excess witness: 07d19abfd6c1c749c7360526e4a04a3eb865fb2e
- unified witness capacity: 9935e0d2343fc08d9e65d51ff495cfb260d6de95
- E408 Q33 global compatibility: cf2782082643af46403865c5d66744ea8fe03dd9
- Astra dlow terminal: c71b29d3c5b661cdcf00404e545933893c44598b
- Astra aext near-anchor: ad6e4ebe152e3918b9c5fe67f461ba402b1445d8
- base main at branch creation: 3f42fcce5761ca2372140618adda56f95fcbe253
These are the latest heads observed in the repository at the time of this update; they are provenance references, not merged dependencies.
## Established under retained contracts
- The E407 Q32 boundary has 49 linear independent 4-set witnesses on a 29-point support, with \(e(H)=284\), \(\alpha(H)\le4\), \(\delta(H)\ge12\), and total core excess 4.
- The exact ledger gives \(3\le\delta\le16\), \(\delta+\epsilon_U\le16\), and the sibling transversal/excess lemma gives \(\epsilon_U+2\delta\ge9\).
- The \(\delta=16\) four-partite branch is **EXCLUDED**. The 4+1 and 3+2 endpoint splits violate the excess budget; the 5+0 split forces its endpoint \(K_4\) to be complete to the 8-part, creating a forbidden \(K_{12}\). See FOUR_PARTITE_TERMINAL.md and DELTA16_K12_CLIQUE_OBSTRUCTION.md for the standalone one-exception proof.
- The \(\delta=15\) four-partite branch is **EXCLUDED** in DELTA15_FOUR_PARTITE_TERMINAL.md: after eliminating three W-profiles, the last \(K_3\cup K_5^3\) profile forces \(k_A=k_B=k_C=5\), so any cross-edge endpoint has a forbidden \(K_{12}\) neighbourhood.
- The \(\delta=14\) non-four-partite augmentable-edge branch is **excluded**. The saturated branch is now **PROVED_CONDITIONAL**: DELTA14_SATURATED_KERNEL_CLASSIFICATION.md proves every admissible 15-vertex kernel J is the explicit \((1,2,5,5,2)\) C5 blow-up, and DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md excludes every full-core extension for \(\epsilon_U\in\{0,1,2\}\). This relies on the retained alpha-critical kernel reduction, including the unaudited Didin-preprint component-count dependency.
- The \(\delta=15\) non-four-partite branch is **excluded** under the retained core/witness contract: Kang–Pikhurko equality reduces it to a balanced \((7,7,7,7)\) base, and the exceptional vertices \(x,y\) have incompatible required degrees into \(W\). The full reduction and contradiction are in DELTA15_SECOND_TURAN_PACKING.md.
- The final \(\delta=15\) contradiction compares \(d_H(x,W)=a-1+\epsilon_x\) and \(d_H(y,W)=6-a+\epsilon_y\). Whole-part saturation in \(W\) forces incompatible lower bounds on \(a\), for both \(\epsilon_U=0\) and \(\epsilon_U=1\).
- In that case, \(U\)-part sizes are \(7,7,7,8\), \(H[W]=K_5\cup K_5\cup K_4\cup K_4\), and the five cross edges in \(H[U]\) form a matching between the 8-part and the three 7-parts.
- For \(\delta=16\), a reverse-saturation lemma proves every \(w\in W\) is complete to exactly one \(U\)-part; it is used in the endpoint-split proof.
- New exact witness-array identity: for each D-vertex d, its number of missing small-part partners equals the number of exact-129 color classes omitting d. These multiplicities sum to 7; the five endpoint D-labels contribute at least 5, so at least three have multiplicity exactly 1 and at least one non-endpoint D-label has multiplicity 0. See DELTA16_WITNESS_ARRAY.md.
- New Round 23 theorem: when \(\delta=13\), \(L=\overline{H[U]}\) is four-partite, and \(H[W]\) is a disjoint union of four cliques, every case with \(\epsilon_U\in\{1,2,3\}\) is excluded by DELTA13_FOUR_PARTITE_NO_CROSS_W_PROFILES.md. The common-neighbour cover capacities are at most 27, 28, 28, and 23 for the profiles \((3,4,5,6)\), \((3,5,5,5)\), \((4,4,4,6)\), and \((4,4,5,5)\), respectively.
- New Round 24 theorem: at \(\delta=13,\epsilon_U=1\), the four-partite-U profile \(H[W]=K_3\dot\cup3K_5\) plus one cross-edge is also **EXCLUDED** by DELTA13_EPS1_K3K5K5K5_ONE_CROSS_EDGE.md. The proof allows at most one unsaturated U-vertex; its common-neighbour cover capacity is at most 26, below 28.
- New Round 25 theorem: at \(\delta=13,\epsilon_U=1\), the \(3K_4\dot\cup K_6\) W-profile with its unique cross-edge joining \(K_4\) to \(K_6\) is **EXCLUDED** by DELTA13_EPS1_3K4_K6_K4K6_EDGE.md. All U vertices are W-saturated, and the four common-neighbour capacities sum to at most 28 < 29.
- New Round 26 theorem: the remaining \(\delta=13,\epsilon_U=1\), \(3K_4\dot\cup K_6\)-plus-one-edge placement, where the edge joins two \(K_4\)'s, is **EXCLUDED** by DELTA13_EPS1_3K4_K6_K4K4_EDGE.md. The possible degree-seven U exception is handled by a capacity-equality overlap argument. Together with Round 25, both placements of the single cross-edge are closed.
- New Round 31 theorem: the complete \(\delta=13,\epsilon_U=1\), four-partite-\(L\), \(H[W]=2K_4\cup2K_5\) plus two-cross-edge profile is **EXCLUDED**. The four formerly open same-pair placements are closed by the \(k\ge5\) exception floor, exact Type-I/Type-II blocker classification, and an independent-5-set contradiction. See DELTA13_EPS1_TWO_CROSS_EDGE_TERMINAL_CLOSURE.md; the arithmetic verifier is separate from the analytic proof.
## Status by case
| Case | Status |
|---|---|
| E407 template A | OPEN |
| E407 template B | OPEN |
| E407 template C | OPEN |
| E407 template D | OPEN |
| E407 template E | OPEN |
| \(\delta=16\) four-partite extreme | EXCLUDED by endpoint-split analysis and forbidden \(K_{12}\) |
| \(\delta=15\) four-partite | EXCLUDED by W-profile saturation and forbidden \(K_{12}\) |
| \(\delta=15\) non-four-partite | EXCLUDED under KP equality + core-to-\(W\) degree contradiction |
| \(\delta=14\) four-partite | \(\epsilon_U=0,1,2\): all W profiles excluded; \(\epsilon_U=1\) exhaustiveness uses Brouwer, \(\epsilon_U=2\) is Turán equality |
| \(\delta=14\) non-four-partite, saturated \(L\) | PROVED_CONDITIONAL excluded: every admissible J is the C5 blow-up, and its full-core extension is impossible |
| \(\delta=13\), four-partite \(L\), no-cross-edge \(H[W]\), \(\epsilon_U\in\{1,2,3\}\) | EXCLUDED by common-neighbour cover capacity |
| \(\delta=13\), four-partite \(L\), \(\epsilon_U=1\), \(K_3\dot\cup3K_5\) plus one W-cross-edge | EXCLUDED by common-neighbour cover capacity |
| \(\delta=13\), four-partite \(L\), \(\epsilon_U=1\), \(3K_4\dot\cup K_6\) plus a \(K_4\)-\(K_6\) edge | EXCLUDED by common-neighbour cover capacity |
| \(\delta=13\), four-partite \(L\), \(\epsilon_U=1\), \(3K_4\dot\cup K_6\) plus a \(K_4\)-\(K_4\) edge | EXCLUDED by saturation/capacity overlap |
| \(\delta=13,\epsilon_U=1\), four-partite \(L\), \(2K_4\cup2K_5\) plus two W-cross-edges | EXCLUDED under retained core/witness contract |
| \(\delta\le13\) other cases | OPEN |
| E407 Q32 overall | OPEN / NOT_CERTIFIED |
| EG617(r=12) | OPEN / NOT_CERTIFIED |
## Verification status
The local arithmetic verifier checks exact ledgers and the finite excess inequalities only. The analytic endpoint-split proof in FOUR_PARTITE_TERMINAL.md excludes the full \(\delta=16\) branch under the retained core/witness contract; this verifier is not a graph-realization certificate.
## New Round 9 result — delta=14, epsilon_U=0 cover-capacity exclusion
- Added DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md: the no-cross-edge \(H[W]=K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6\) profile is excluded by a common-neighbour cover bound. Defining \(S_s\) as the U-vertices complete to \(C_s\), the four components must cover all 29 U-vertices, but exact extra-edge/excess accounting gives \(\sum_s|S_s|\le28\).
- At the time of Round 9, three of the four \(\delta=14,\epsilon_U=0\) W profiles were excluded; this historical frontier was closed in Round 10 below.
- Arithmetic replay: verify_delta14_eps0_cover_capacity.py; all 35 excess partitions with \(E_3+E_4+E_5+E_6=4\) give a cover upper bound at most 28.
- Round 9 remaining frontier (superseded by Round 10): \(\epsilon_U=0\) one-cross-edge profile; \(\epsilon_U=1,2\); \(\delta=14\) non-four-partite; \(\delta\le13\). E407 Q32 and EG617 remain OPEN / NOT_CERTIFIED.


## New Round 10 result — close the final \(\delta=14,\epsilon_U=0\) four-partite W-profile

- Added DELTA14_EPS0_K3K5K5K5_CROSS_EDGE_CLOSURE.md: excludes \(H[W]=K_3\cup K_5^3\) plus one cross-edge by exact common-neighbour capacity.
- The only possible failure of U-to-W-component saturation is a small-part non-endpoint \(u\), and only when the W-cross-edge joins \(K_3\) to \(K_5\). Its exact non-neighbour pattern forces \(|S_2\cup S_3|\ge15-\epsilon_y\), while the two K5 capacities give \(|S_2|+|S_3|\le14-\epsilon_y\), a contradiction.
- Once all 29 U-vertices are saturated, the four component capacities sum to at most \(27\), contradicting the required cover of \(U\).
- Added verify_delta14_eps0_k3k5_cross_edge.py; arithmetic replay passed locally: all 35 W-excess allocations yield cover cap 27, and the exceptional-vertex lower/upper bounds differ by exactly one.
- Therefore the entire \(\delta=14,\epsilon_U=0\), four-partite branch is EXCLUDED under the retained contracts. This does not close \(\epsilon_U=1,2\), \(\delta=14\) non-four-partite, \(\delta\le13\), any full V12 template, E407 Q32, or EG617(r=12).


## New Round 11 result — exclude \(\delta=14,\epsilon_U=1\), \(H[W]=K_3\cup K_5^3\) without a cross-edge

- Added DELTA14_EPS1_K3K5K5K5_NO_CROSS_EDGE.md. Because the four W clique components are pairwise anticomplete, every \(u\in U\) is complete to at least one component; hence their four common-neighbour sets cover \(U\).
- Every \(d\in D\) is also complete to a W component, forcing \(t_d\le2+\epsilon_d\le3\). The resulting reverse-saturation bound is \(d_H(w,U)\ge11\) for any W vertex not complete to a U-part.
- For each \(K_5\) component, either all vertices admit U-part labels and extra-edge counting gives \(|S_i|\le5+E_i\), or one unsaturated vertex has excess 3 and a zero-excess companion gives the same bound. For \(K_3\), \(|S_0|\le10+\lfloor E_0/3\rfloor\).
- Since \(E_0+E_1+E_2+E_3=3\), the total cover capacity is at most \(28-E_0+\lfloor E_0/3\rfloor\le28\), contradicting \(|U|=29\).
- The verifier replayed all 20 component-excess allocations. This excludes only this \(\epsilon_U=1\) W-profile, not the entire \(\epsilon_U=1\) row.
- Still open: other \(\delta=14,\epsilon_U=1\) W profiles, \(\epsilon_U=2\), non-four-partite \(\delta=14\), and \(\delta\le13\). E407 Q32 and EG617 remain OPEN / NOT_CERTIFIED.


## New Round 10 result — delta=14 K5--K5 cross-edge exclusion
- Added DELTA14_EPS0_K3K5X1_K5K5_EDGE.md. If the single W-cross-edge in the \(K_3\cup K_5^3\) profile joins two \(K_5\) components, every \(u\in U\) is still complete to a whole W-component: otherwise it would need at least eight W-neighbours, while \(d_H(u,W)\le6\).
- The four common-neighbour sets therefore cover all 29 U vertices. Component/excess accounting gives \(\sum |S_s|\le26+\mathbf1_{\{E_T=0\}}\le27\), contradiction.
- Arithmetic replay: verify_delta14_k5_cross_edge_capacity.py; 35 excess allocations checked, maximum bound 27.
- The only \(\delta=14,\epsilon_U=0\) four-partite W-profile remaining is \(K_3\cup K_5^3\) with the cross-edge between \(K_3\) and a \(K_5\). This placement remains OPEN. Other \(\epsilon_U\), non-four-partite, and \(\delta\le13\) branches remain open; E407 Q32 and EG617 remain OPEN / NOT_CERTIFIED.


## New Round 11 result — complete \(\delta=14,\epsilon_U=0\) four-partite W-row closure
- Added DELTA14_EPS0_K3K5X1_K3K5_EDGE.md, excluding the final \(K_3\cup K_5^3\) profile with the cross-edge joining \(K_3\) to a \(K_5\).
- The proof splits by whether \(T=K_3\) is complete to \(D\). If not, degree excess forces \(h=|N_D(T)|=4\), all four excess units into \(T\), and exact U-neighbourhoods \(D_0\cup A_i\); the common-neighbour cover is at most 25. If \(T\) is complete to \(D\), the \(X\)-exception set plus component cover capacity is at most 28 after the equality-case correction.
- Arithmetic replay: verify_delta14_k3_k5_cross_edge.py checked all 35 excess allocations; corrected maximum cover bound is 28.
- Result: every four-partite \(W\)-profile at \(\delta=14,\epsilon_U=0\) is excluded under the retained core/witness contract. The \(\epsilon_U=1,2\), non-four-partite \(\delta=14\), and all \(\delta\le13\) cases remain open. E407 Q32 and EG617 remain OPEN / NOT_CERTIFIED.


## New Round 12 result — exclude \(\delta=14,\epsilon_U=1\), no-cross-edge \(K_4^3\cup K_6\)

- Added DELTA14_EPS1_K4K4K4K6_NO_CROSS_EDGE.md. Every D-vertex is assigned to exactly one W-component; a D-vertex assigned to \(K_6\) must have \(\epsilon_d=1,t_d=0\). The exact external-incidence identity is \(R=1-2q+\sum_{d\in D}\epsilon_d\), giving \(R\le2\) if no D-vertex is assigned to \(K_6\), and \(R=0\) otherwise.
- If a \(K_4\) component receives \(k\ge3\) D-assignments, its external-incidence budget limits how many vertices can be complete to all of D. The remaining vertices must be complete to small U-parts, forcing total W-excess greater than 3. Hence every \(K_4\) receives at most two D-assignments, impossible for seven or eight D-vertices distributed across three \(K_4\)'s.
- Added verify_delta14_eps1_k4k4k4k6.py; arithmetic replay passed. A verifier bookkeeping error was caught and fixed before replay.
- The \(\epsilon_U=1\) no-cross-edge \(K_3\cup K_5^3\) and \(K_4^3\cup K_6\) profiles are now excluded. The \((4,4,5,5)\)+one-cross-edge profile remains open, as does \(\epsilon_U=2\), non-four-partite \(\delta=14\), and \(\delta\le13\). E407 Q32 remains OPEN / NOT_CERTIFIED.


## New Round 13 result — close the final \(\delta=14,\epsilon_U=1\) W-profile

- Added DELTA14_EPS1_K4K4K5K5_ONE_CROSS_EDGE.md. Every D-vertex is assigned to a unique W-component; the exact external-incidence count \(R=1-q_5+\sum_D\epsilon_d\le2\) forces at least six D-vertices to be assigned to the two K4 components.
- A K4 receiving \(k\ge3\) D assignments would need too much W-excess: external incidence limits the number of vertices complete to all of D, and every remaining vertex must be complete to a small U-part. The minimum excess demand is \(4,8,12,12,10\) for \(k=3,4,5,6,7\); \(k=8\) gives a forbidden K12.
- Added DELTA14_EPS1_W_PROFILE_CLASSIFICATION.md. Applying Brouwer's second-Turán bound to \(\overline{H[W]}\) (18 vertices, 120 edges, K5-free) forces four-partiteness; exact integer partition enumeration leaves precisely the three profiles handled by the three epsilonU=1 theorems.
- Both arithmetic verifiers were replayed locally. The complete \(\delta=14,\epsilon_U=1\), four-partite row is now EXCLUDED under the retained core contracts and Brouwer's theorem.
- Still open: \(\delta=14,\epsilon_U=2\), non-four-partite \(\delta=14\), and \(\delta\le13\). E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## New Round 12 result — four additional \(\delta=14\), \(\epsilon_U=1,2\) profiles excluded
- Added DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md.
- Excluded: \(K_3\cup K_5^3\) for \(\epsilon_U=1,2\); \(K_4^3\cup K_6\) for \(\epsilon_U=1\); \(K_4\cup K_4\cup K_5\cup K_5\) for \(\epsilon_U=2\).
- The proofs use the generalized reverse-saturation threshold \(d_H(w,U)\ge9+m-\epsilon_U\), where \(m\) is the smallest W-component size, and component-specific label-load bounds. Arithmetic replay: verify_delta14_epsilonU1_2_profiles.py.
- The only \(\delta=14\) four-partite W-profile still open is \(\epsilon_U=1\), \(H[W]=K_4\cup K_4\cup K_5\cup K_5\) with one cross-edge. The \(\delta=14\) non-four-partite branch and all \(\delta\le13\) cases remain open; E407 Q32 and EG617 remain OPEN / NOT_CERTIFIED.


## New Round 14 result — close the full \(\delta=14,\epsilon_U=2\) four-partite row

- Added DELTA14_EPS2_W_PROFILE_CLASSIFICATION.md. The exact ledger gives \(e(H[W])=34-\epsilon_U=32\); since \(\alpha(H[W])\le4\), Turán's bound is met with equality. Thus \(H[W]\) must be \(K_4\cup K_4\cup K_5\cup K_5\) with no cross-edges.
- The retained common-neighbour capacity proof in DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md, Section 5, applies to this exact profile and gives \(\sum_s|S_s|\le24<29\). Hence the unique profile is impossible.
- Added verify_delta14_eps2_w_profile.py; exact arithmetic replay passed.
- Audit note: Section 3 of DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md mentions \(K_3\cup K_5^3\) for \(\epsilon_U=2\), but that graph has 33 edges and violates the exact \(e(H[W])=32\) ledger. It is not used as an admissible profile.
- The full \(\delta=14\), four-partite branch is now EXCLUDED for every allowed \(\epsilon_U\in\{0,1,2\}\), under the retained core/witness contracts and the stated Turán/Brouwer dependencies.
- Still open: \(\delta=14\) non-four-partite and \(\delta\le13\). E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## Round 15 — \(\delta=14\) non-four-partite augmentable-edge reduction

Added DELTA14_NONPARTITE_AUGMENTABLE_EDGE_REDUCTION.md and verify_delta14_nonpartite_augmentable_edge.py.

Let \(L=\overline{H[U]}\) be non-four-partite with \(e(L)=308\). If there exists a nonedge \(uv\) for which \(L+uv\) remains \(K_5\)-free, then \(L+uv\) is a 309-edge non-four-partite \(K_5\)-free graph. Brouwer's second-Turán theorem and the Kang–Pikhurko equality classification apply. The 49 edge-disjoint witness blocks exclude the two unbalanced equality profiles, forcing the balanced \((7,7,7,7)\) base.

Using the exact exceptional-vertex degrees and the exhaustive \(W\)-profile list, the sum
\[
d_H(x,W)+d_H(y,W)=5+\epsilon_x+\epsilon_y-I_x-I_y\le5+\epsilon_U
\]
eliminates every profile except one strict terminal:
- \(\epsilon_U=1\);
- \(H[W]=K_3\dot\cup K_5^3\), with no cross edges;
- \(x,y\) both have exactly three \(W\)-neighbours and are complete to the \(K_3\);
- \(uv\) is incident to neither \(x\) nor \(y\);
- \((a,\epsilon_x,\epsilon_y)=(3,1,0)\) or \((4,0,1)\).

The added edge \(uv\) must be one of the balanced KP leave types \(P_1P_2,P_1P_3,P_1P_4,P_2P_3,P_2P_4\), not \(P_3P_4\). Hence at least one endpoint lies in \(P_1\) or \(P_2\setminus\{y\}\); its \(W\)-degree is four, so it too is complete to the \(K_3\). This gives a third vertex in the \(K_3\)'s common neighbourhood.

The verifier enumerates all integer values of \(a,\epsilon_x,\epsilon_y,I_x,I_y\) and both saturated/unsaturated statuses under the proven component thresholds. It returns exactly the two terminals above. This is arithmetic replay only, not a graph-realization certificate.

**Status:** PROVED_CONDITIONAL strict reduction for the augmentable-edge subcase. Still OPEN: eliminate the two residual terminals above, or prove that \(L\) must have an augmentable nonedge; separately handle the case where \(L\) is \(K_5\)-saturated. The \(\delta\le13\) branch and the five shell templates remain open; E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


- The \(\delta=14\) non-four-partite augmentable-edge branch is **excluded**. For the explicit C5-blow-up local candidate only, DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md excludes \(\epsilon_U=0\) and reduces \(\epsilon_U=1,2\) to two exact W-extension terminals. This was the pre-Round-22 frontier; it is superseded by DELTA14_SATURATED_KERNEL_CLASSIFICATION.md, which conditionally forces every admissible J to this blow-up and excludes its full-core extension.

Added DELTA14_NONPARTITE_AUGMENTABLE_TERMINAL_CLOSURE.md and verify_delta14_augmentable_terminal.py.

The preceding augmentable-edge reduction left only \(\epsilon_U=1\), \(H[W]=K_3\dot\cup K_5^3\), with \(x,y,z\) complete to the \(K_3\), and a balanced KP base on four 7-vertex parts plus one exceptional vertex. The new proof assigns every \(u\in U\) to the unique W-component to which it is complete: every \(u\) must be complete to at least one component by \(\alpha(H)\le4\), and \(d_H(u,W)\le6<3+5\) prevents it from being complete to two components. Hence the four common-neighbour sets partition all 29 vertices of \(U\).

The key new capacity improvement is that a U-part-saturated \(K_5\) component has common-neighbour capacity \(n_i\le4+E_i\), not merely \(5+E_i\): equality in the coarser bound would force four of the five labels to one base part and the fifth label to carry \(5+E_i\) extra edges, exceeding its available \(1+\epsilon_w\le1+E_i\). An unsaturated \(K_5\) component has \(n_i\le7\); its unsaturated vertex has positive excess, and a zero-excess companion is complete to a 7-part, giving the intersection cap 6+1.

The excess split \(E_0+E_1+E_2+E_3=3\) now rules out: all three \(K_5\) components saturated; exactly one star-only unsaturated component; the exceptional mixed \(P_1P_2\) pattern; and two or more unsaturated components. In the last case, the shared set \(R=(P_1\\setminus A)\\cup(P_2\\setminus\\{y\\})\) would have to lie in the common neighbourhood of the \(K_3\), forcing at least 12 common neighbours despite a zero-excess \(K_3\) vertex of U-degree 10.

**Result:** the entire \(\delta=14\), non-four-partite augmentable-edge subcase is excluded under the retained contracts. The only remaining case at this boundary is \(K_5\)-saturated \(L\), with no augmentable nonedge. This is a genuine conditional theorem, not a closure of E407 Q32 or EG617(r=12).


## Round 17 — \(\delta=14\) saturated branch reduced to one labelled kernel

Added DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md and verify_delta14_saturated_alpha_critical.py.

Under the retained 29-point/49-witness core contract, if the non-four-partite \(L=\overline{H[U]}\) is \(K_5\)-saturated, then \(G=H[U]\) is \(\alpha\)-critical with \(\alpha(G)=4\). Conditional on Didin's 2026 author-prepared preprint theorem for graphs with prescribed independence number, the number of components of \(G\) must be exactly three; the four-component case would make \(L\) complete four-partite.

The component split is forced to \(K_a\dot\cup K_b\dot\cup C\) with \(\alpha(C)=2\). Brouwer's second-Turán bound and the 49 edge-disjoint \(K_4\) witnesses then leave exactly one arithmetic profile:
\[
(a,b,|C|,e(C),e(\overline C))=(7,7,15,56,49).
\]
All 49 witnesses exhaust both \(A\times B\) and \(E(\overline C)\). Hence \(\overline C\) must be a triangle-free, non-bipartite, triangle-saturated graph on 15 vertices with 49 edges whose edge set admits two orthogonal decompositions into seven near-perfect matchings. At Round 17 this was only a strict reduction; it is superseded by Round 22's general kernel classification and conditional exclusion.

External theorem status is explicit: Didin's 2026 preprint was listed as under review; its proof has not been independently audited in this workstream. The arithmetic verifier checks the integer enumeration only. The remaining saturated kernel, \(\delta\le13\), all five shell templates, and the \(K_{145}\)-to-T61 bridge remain OPEN / NOT_CERTIFIED.

### Cross-branch refresh
- E408 Q33 global compatibility branch: d70b6a2b9c4929b6b9315fcfd4bd29848920323b. It now reports the conditional universal minimum-support improvement \(S_0\ge13\) (hence \(\delta\ge5\)); its terminal remains open.
- Unified witness-capacity branch: 9935e0d2343fc08d9e65d51ff495cfb260d6de95.
- Emergency sprint chat: 5258c5fe17af3bf17eb7a2bfb08315c9be9116cd.
- Witness packing: f5d3daa07403877ede9885e1bd5c2f46b16d81da.
- Zero-excess witness: 07d19abfd6c1c749c7360526e4a04a3eb865fb2e.
- E408 Q32 excess-six branch remains separate at a0ba6db26c7e8b00a4217dcbcbf298895dff93ce.


## Round 18 — the saturated 29-point local model is explicitly realizable

Added DELTA14_SATURATED_LOCAL_MODEL.md and verify_delta14_saturated_local_model.py. A blow-up \(J\) of \(C_5\) with part sizes \((5,5,2,1,2)\) has 15 vertices, 49 edges, is triangle-free and triangle-saturated, and is non-bipartite. The graph \(L\) formed by joining \(J\) to two independent 7-sets is \(K_5\)-free, \(K_5\)-saturated, non-four-partite, and has 308 edges. Its complement \(H_U\) has 29 vertices, 98 edges, and independence number four.

The explicit \(\mathbb Z_7^2\) cell labeling maps all 49 cells bijectively to \(E(J)\). The third color \(\kappa=x+y\bmod7\) gives seven classes of seven vertex-disjoint independent 4-sets; globally the 49 witnesses are pairwise linear and cover all of \(U\). The standard-library verifier checks the graph counts, saturation, cell bijection, and witness packing.

This **invalidates the proposed local-only contradiction target** from Round 17. It does not construct \(W\), the full 47-vertex core, or the shell-row labels. For \(\epsilon_U=0\), the model imposes \(U\)-to-\(W\) degree sequence \(6^{14},5^{10},4^4,2^1\) (sum 152), which becomes a concrete next interface target. E407 Q32 and EG617(\(r=12\)) remain OPEN / NOT_CERTIFIED.


### Latest sibling read after Round 18
- E408 Q33 global compatibility branch head: 6f2a350d043aed41b8bb551449cae54a159a3cfe. Its latest canonical state reports the conditional colorwise cap \(P_C\le49\), hence \(R_C\ge13\); the stronger \(P_C\le48\) remains NOT CERTIFIED. The E408 Q33 terminal and original \(K_{145}\) theorem remain OPEN.
- This is a separate seven-block/color-factor constraint and has not been imported as an E407 closure.


## Round 19 — candidate-specific independent-transversal reduction

Added DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md and verify_delta14_saturated_transversal_reduction.py. The theorem is **conditional on the explicit C5-blow-up local candidate** in DELTA14_SATURATED_LOCAL_MODEL.md. It is not universal over all saturated J graphs.

For that candidate, the distinguished singleton \(d_0\in J\) has \(d_J(d_0)=4\), hence \(d_{H[U]}(d_0)=10\). Brouwer's second-Turán bound forces \(\overline{H[W]}\) to be four-partite, with four clique parts of size at least three and at most \(2-\epsilon_U\) cross edges in \(H[W]\). Independent-transversal capacity excludes this candidate when \(\epsilon_U=0\); for \(\epsilon_U=1,2\), it forces the two stated W profiles and \(d_0\)'s complete neighborhood into the smallest clique component.

The saturated-branch reduction has **not** shown that every allowed \(J\) is this blow-up. Thus the general saturated branch, the five shell templates, \(\delta\le13\), and the original \(K_{145}\)-to-T61 bridge remain OPEN / NOT_CERTIFIED.


## Round 20 — explicit saturated local candidate has no full-core extension

Added DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md and verify_delta14_saturated_candidate_extension_exclusion.py. Independent arithmetic replay returned \`DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION_ARITHMETIC_OK\`.

For the explicit (5,5,2,1,2) blow-up local model, the remaining W-extension terminals are now excluded:
- \(\epsilon_U=1\): for \(K_3\dot\cup3K_5\), assignment-to-component plus the independent triple \(d_0,a,b\) shows A/B vertices cannot be assigned to the \(K_3\), and cannot share a \(K_5\); each side then needs two disjoint \(K_5\) parts although only three exist. The \(3K_4\dot\cup K_6\) profile is impossible because \(d_0\) has at most three W-neighbours while every part has size at least four. The \((4,4,5,5)\) plus one-cross-edge profile admits an independent transversal avoiding \(N_W(d_0)\).
- \(\epsilon_U=2\): \(d_0\) must be complete to one \(K_4\). Independent-set constraints force the A/B assignments to disjoint W parts; one side fills the other \(K_4\), and the other splits across the two \(K_5\)'s. The four C/E vertices must be complete to \(d_0\)'s \(K_4\). Every vertex of the two \(K_5\)'s must be complete to A or B; at least four in each must be A-complete. Degree/excess counting then forces at least 12 W-excess units, exceeding the available two.
- Together with the \(\epsilon_U=0\) independent-transversal exclusion, the explicit candidate has no full 47-core extension for any \(\epsilon_U\in\{0,1,2\}\).

The verifier checks W-profile arithmetic, transversal forbidden fractions, and the 12 finite A/B assignment patterns. It does not machine-check the graph-theoretic independent-set arguments. This is not a universal closure: the 15-vertex saturated graph J has not been classified, and the alpha-critical reduction only gives necessary conditions for J. The general delta=14 saturated branch, delta<=13, the five shell templates, and the K145-to-T61 bridge remain OPEN / NOT_CERTIFIED.


## Round 21 — classify the entire C5-blow-up subclass

Added DELTA14_C5_BLOWUP_PROFILE_CLASSIFICATION.md and verify_c5_blowup_profile.py. Independent exact enumeration passed: seven dihedral classes of positive five-part C5 blow-ups have 15 vertices and 49 edges, but only one satisfies the witness-forced maximum-degree condition Delta(J)<=7, namely (1,2,5,5,2), equivalent to (5,5,2,1,2). The explicit candidate is already excluded from all full-core extensions by Round 20.

This closes the C5-blow-up subfamily only. It does not prove that every admissible saturated kernel J is a C5 blow-up. The remaining general terminal consists of potential non-C5-blow-up triangle-free, non-bipartite, triangle-saturated 15-vertex, 49-edge graphs compatible with the two orthogonal near-perfect matching decompositions. E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## Round 22 — general \(\delta=14\) saturated-kernel classification

Added DELTA14_SATURATED_KERNEL_CLASSIFICATION.md and verify_delta14_saturated_kernel_classification.py. The finite arithmetic verifier passed with the unique solution \(d=4\), a \(7+7\) bipartition of \(J-v\), and exactly a missing \(K_{2,2}\); this reconstructs the C5 blow-up \((1,2,5,5,2)\).

The argument is now general within the retained kernel contract:
1. The AES equality case forces \(\delta(J)\le5\), since otherwise a non-bipartite triangle-free 15-vertex graph with minimum degree at least six would be \(C_5(3)\), with only 45 edges.
2. Brouwer/Kang–Pikhurko gives at most 43 edges for a non-bipartite triangle-free 14-vertex graph. Thus deleting a degree-\(d\le5\) vertex leaves a bipartite graph.
3. Saturation forces the missing cross-edges of \(J-v\) to be exactly \(K_{a,b}\), where \(a+b=d\). The maximum-degree bound \(\Delta(J)\le7\) forces the bipartition to be \(7+7\), so \(ab=d=a+b\), giving \(a=b=2,d=4\).

Combining with the already verified candidate-specific extension exclusion closes the **general \(\delta=14\), non-four-partite, \(K_5\)-saturated terminal conditionally**. The condition is essential: the upstream component-count reduction still depends on Didin's 2026 preprint theorem, not independently audited here. The \(\delta\le13\) cases, five shell templates A–E, E407 Q32 overall, and the \(K_{145}\)-to-T61 bridge remain OPEN / NOT_CERTIFIED.


## Round 23 — delta-13 four-partite U / no-cross W closure

Added DELTA13_FOUR_PARTITE_NO_CROSS_W_PROFILES.md and verify_delta13_four_partite_no_cross_w_profiles.py. Under the retained 49-witness contract, a four-partite \(L=\overline{H[U]}\) forces U-part sizes \((7,7,7,8)\), all small-small pairs to be used by witnesses, and at most one H[U] cross-edge at each small-part vertex. For \(\delta=13\), the no-cross W profiles are exactly \((3,4,5,6)\) at \(\epsilon_U=1\), \((3,5,5,5)\) or \((4,4,4,6)\) at \(\epsilon_U=2\), and \((4,4,5,5)\) at \(\epsilon_U=3\).

The component common-neighbour sets must cover all 29 U vertices. Exact label/excess accounting bounds their total sizes by at most 27, 28, 28, and 23, respectively, so every listed profile is impossible. The finite arithmetic verifier passed with output DELTA13_FOUR_PARTITE_NO_CROSS_W_PROFILES_ARITHMETIC_OK; it checks profile enumeration and numeric capacity ceilings only, not the analytic graph lemmas.

Remaining: \(\delta=13,\epsilon_U=0\); W-cross-edge profiles; non-four-partite U-complement cases; \(\delta\le12\); all five templates as a global compatibility problem; and the upstream \(K_{145}\)-to-T61 bridge. E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## Round 24 — delta-13 epsilonU=1, K3 plus three K5s with one W-cross-edge

Added DELTA13_EPS1_K3K5K5K5_ONE_CROSS_EDGE.md and verify_delta13_eps1_k3k5_one_cross_edge.py. The proof corrects for the possibility that a nonsaturated U-vertex has degree seven into W: in the \(K_3\)-\(K_5\) edge placement this can happen for at most one U-vertex, and the \(d_H(u,W)=6\) alternative is ruled out by a strict common-neighbour lower/upper bound. In the \(K_5\)-\(K_5\) edge placement every U-vertex is W-saturated.

The component common-neighbour capacities sum to at most \(23+E_W=26\). At least 28 U-vertices must be covered by those sets, contradiction. The arithmetic replay passed with DELTA13_EPS1_K3K5K5K5_ONE_CROSS_EDGE_ARITHMETIC_OK; it checks only the capacity totals and the strict integer gap, not the analytic graph lemmas.

Remaining \(\delta=13\) four-partite-U profiles include \((4,4,4,6)\) plus one W-cross-edge and \((4,4,5,5)\) plus two W-cross-edges at \(\epsilon_U=1\), and \((4,4,5,5)\) plus one W-cross-edge at \(\epsilon_U=2\). The \(\epsilon_U=0\), non-four-partite, \(\delta\le12\), five-template global compatibility, and upstream bridge gaps remain open.


## Round 25 — delta-13 epsilonU=1, 3K4+K6 with K4-K6 cross-edge

Added DELTA13_EPS1_3K4_K6_K4K6_EDGE.md and verify_delta13_eps1_3k4_k6_k4k6_edge.py. The transversal bound forces every U-vertex to be W-saturated: any nonsaturated U-vertex would need W-degree at least eight, while the degree ledger gives at most seven on small U-parts and six on D. The same bound forces every D vertex to be W-saturated, giving \(t_d\le2\) and a reverse-saturation lower bound \(d_H(w,U)\ge12\) for any W-vertex not complete to a U-part.

This yields component capacities at most 9 for each of the three K4 components and at most \(\lfloor E_6/2\rfloor\le1\) for K6. Their sum is at most 28, contradicting the required cover of 29 U vertices. Arithmetic replay passed with DELTA13_EPS1_3K4_K6_K4K6_EDGE_ARITHMETIC_OK.

Remaining in this local profile family: the single edge joining two K4 components. Other open cases include the \(\epsilon_U=1\), \(2K_4\dot\cup2K_5\)-plus-two-edge profile; \(\epsilon_U=2\), \(2K_4\dot\cup2K_5\)-plus-one-edge profile; \(\epsilon_U=0\); non-four-partite U-complements; \(\delta\le12\); five-template global compatibility; and the upstream bridge.


## Round 26 — delta-13 epsilonU=1, 3K4+K6 with K4-K4 cross-edge

Added DELTA13_EPS1_3K4_K6_K4K4_EDGE.md and verify_delta13_eps1_3k4_k6_k4k4_edge.py. The D-vertex saturation proof uses the exact eight-edge U-cross-edge ledger: a nonsaturated D vertex would have excess one and no U-cross-edges, leaving at most seven cross-edges among the other seven D vertices. Hence all D vertices are saturated and \(t_d\le2\); reverse saturation gives \(d_H(w,U)\ge12\) for W vertices not complete to a U-part.

For U vertices, the degree-six nonsaturation case contradicts the cover capacity of the nonincident K4 and K6; the only remaining possible exception is one degree-seven vertex with \(\epsilon_u=1,t_u=0\). The total component capacity is at most 28. If this one exception exists, equality would force all three K4 capacities to be nine; each would then be labelled by one small U-part, but the exceptional vertex's own part is forbidden as a label. Two K4 components must share one of the other two small-part labels, creating an overlap of at least seven vertices and preventing coverage of 28. Thus the profile is excluded.

Arithmetic replay passed with DELTA13_EPS1_3K4_K6_K4K4_EDGE_ARITHMETIC_OK. Both placements of the unique W-cross-edge in the \(\epsilon_U=1\), \(3K_4\dot\cup K_6\) profile are now excluded.


## Round 27 — independent robust closure of the delta-13 \(3K_4\dot\cup K_6\) one-cross-edge profile

Added DELTA13_EPS1_K4K4K4K6_ONE_CROSS_EDGE.md and verify_delta13_eps1_k4k4k4k6_one_cross_edge.py. The finite label/load replay passed: DELTA13_EPS1_K4K4K4K6_ONE_CROSS_EDGE_ARITHMETIC_OK.

This proof independently covers both placements of the W-cross-edge and does not rely on ruling out degree-six U exceptions one at a time:
- For a K4–K6 cross-edge, any U vertex not complete to a W part would need at least eight W neighbours, exceeding the degree cap seven. All 29 U vertices are covered; K4 capacities are at most nine and K6 capacity at most one, giving \(29\le28\), contradiction.
- For a K4–K4 cross-edge, let E be the full set of U vertices not complete to any W part, with \(k=|E|\). Every exception is adjacent to the six non-endpoint vertices of the two incident K4s and nonadjacent to both cross-edge endpoints. No singleton-exception assumption is made. Every W vertex except possibly one non-endpoint K4 vertex with excess three has a unique U-part label. Component label-load bounds give \(|S_i|\le9\) for every K4 and \(|S_6|\le\lfloor E_6/2\rfloor\le1\). For each incident K4, the three non-endpoint vertices see all k exceptions and all vertices in its common-neighbour set, yielding \(|S_i|\le9-k+\lfloor E_i/3\rfloor\). Therefore \(\sum_i|S_i|\le29-2k\), while the \(29-k\) nonexceptional U vertices require \(\sum_i|S_i|\ge29-k\), contradiction.

The finite verifier exhausts 8,925 valid K4 label/excess assignments in each endpoint regime, the corresponding one-unlabelled cases, and 107,325 non-endpoint / 30,615 endpoint K6 label/excess assignments. It checks finite load arithmetic, not the analytic saturation and degree lemmas.

This confirms the entire \(\delta=13,\epsilon_U=1\), \(3K_4\dot\cup K_6\)-plus-one-edge profile is excluded under the four-partite-U/core contract. Next target remains \(2K_4\dot\cup2K_5\) plus two W-cross-edges at \(\epsilon_U=1\); E407 Q32 overall remains OPEN / NOT_CERTIFIED.


## Round 28 — exact two-cross-edge reduction for the delta-13, epsilon_U=1 W-profile

Added DELTA13_EPS1_TWO_CROSS_EDGE_PROFILE_REDUCTION.md and verify_delta13_eps1_two_cross_edge_profile.py.

The new result does not close the profile, but it replaces a broad two-cross-edge case with a strict terminal contract:

- Exact blocker classification: every U-vertex not complete to a W clique is either blocked by one edge whose endpoint non-neighbour sets are singletons, or by a two-edge star between the same pair of W components with non-neighbour-set sizes 2 and 1. The only alternative cylinder-cover pattern would force at least nine W-neighbours, exceeding the degree cap seven.
- Component capacity: every K4 common-neighbour set has size at most 9; every K5 common-neighbour set has size at most 2+E_i. The finite load arithmetic is replayed by the new verifier.
- Global consequence: sum_i |S_i|<=25, so at least four of the 29 U-vertices are W-unsaturated. If a W-cross-edge meets a K4, the sharper capacity is at most 24, so at least five U-vertices are W-unsaturated.
- If both W-cross-edges lie between the two K5 parts, the blocker classification allows at most one unsaturated U-vertex, contradicting the global capacity floor. That placement is therefore excluded entirely.

The verifier is an arithmetic check, not a graph-realization certificate. The surviving blocker patterns with k>=5 remain OPEN; E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## Round 29 — audited saturated-kernel extension closure and proof correction

A critical proof audit found that an earlier draft's inference `|S_P|<=11-|P|` for the total common-neighbour set of a clique (P), based only on (omega(H)le11), was invalid. That draft has been withdrawn. The replacement proof in DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md no longer uses that inference.

The corrected incidence/independent-set argument now excludes all three (epsilon_U) cases for the explicit ((5,5,2,1,2)) local model:
- (epsilon_U=0): the independent-transversal argument remains valid for every W profile with at most two cross-edges.
- (epsilon_U=1): (3K_4dotcup K_6) is impossible because (d_0) has at most three W-neighbours but must be complete to a W component; the ((4,4,5,5))+one-cross-edge profile is excluded by an independent transversal avoiding (N_W(d_0)); the (K_3dotcup3K_5) profile is excluded by a 15-versus-13 incidence count. Each K5 W vertex must be complete to A, B, or all of (Ccup E), but at most 6 can be complete to A, at most 6 to B, and at most 1 to all four (C/E) vertices.
- (epsilon_U=2): the exact W profile is (2K_4dotcup2K_5). The independent-set argument forces A/B assignment supports to be disjoint, with one side filling the other K4. Then at most two K5 W vertices can be complete to A (only 14 A-edges leave that K4) and at most two can be complete to B (both B-assignment groups are nonempty and each B vertex has only one edge outside its assigned K5). But all ten K5 W vertices must be complete to A or B, contradiction.

The kernel classification file was also audited: the first draft of its balance step omitted the cases (X=A) and (Y=B). The proof now handles these boundary cases by the exact edge equation and verifies the unique ((7,7)) split. The arithmetic verifier was expanded to enumerate all bipartition sizes.

**Current status:** the (delta=14), non-four-partite, (K_5)-saturated terminal is conditionally excluded under the retained alpha-critical reduction and its external Didin-preprint dependency. This does not close the remaining (delta=13) W-cross-edge profiles, (deltale12), the five shell templates as a global compatibility problem, or the (K_{145})-to-T61 bridge. E407 Q32 and EG617((r=12)) remain OPEN / NOT_CERTIFIED overall.


## Round 30 — close the same-pair disjoint K4–K5 two-cross-edge placement

Added DELTA13_EPS1_TWO_CROSS_EDGE_K4K5_DISJOINT_CLOSED.md and its arithmetic verifier. In this placement, Type-II blockers are impossible because the two W-cross-edges are disjoint. Every unsaturated U-vertex must therefore be Type I across a K4–K5 edge, forcing at least (3+4=7) W-neighbours. The degree ledger then forces (epsilon_u=1,t_u=0), so at most one such U-exception exists. But the component-capacity theorem gives at least five exceptions whenever a W-cross-edge meets a K4. Contradiction.

The placement frontier is reduced from five same-pair cases to four: K4–K4 matching, K4–K4 star, K4–K5 star centred in the K4, and K4–K5 star centred in the K5. The final case remains especially delicate because degree-six Type-II exceptions may occur. The overall (delta=13,epsilon_U=1) two-cross-edge profile, E407 Q32, and EG617((r=12)) remain OPEN / NOT_CERTIFIED.
