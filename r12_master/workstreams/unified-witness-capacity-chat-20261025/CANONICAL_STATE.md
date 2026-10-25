# Unified witness-capacity workstream — canonical state

Updated: 2026-10-25  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-unified-witness-capacity-20261025  
Allowed directory: r12_master/workstreams/unified-witness-capacity-chat-20261025/

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.** This workstream has proved a reusable conditional labelled-incidence theorem and a finite omission-capacity refinement, but has not excluded the remaining E407/E408 terminal candidates.

## Latest sibling source heads re-read for this continuation

- Emergency sprint: f4c3b06891d29238d4f9cca2588f442004b6dc97
- E407 Q32 terminal: 4ac46745e862571e96cf488b67f6ce2d0ff99afe
- E408 Q32 excess-six (285-edge core): a0ba6db26c7e8b00a4217dcbcbf298895dff93ce
- E408 Q33 global compatibility: a8cf20bdb7d40458df456980c34c370244a838c3
- Witness-packing: f5d3daa07403877ede9885e1bd5c2f46b16d81da
- Zero-excess witness: 07d19abfd6c1c749c7360526e4a04a3eb865fb2e
- Ultimate closure: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40

All sibling reads were read-only. The Q33 canonical state still contains an external-star inference that is invalid as stated; see the audit below. No sibling branch or directory was modified.

## Canonical mathematical results

1. **Exact-129 labels:** each selected exact-129 color has seven independent four-point witnesses under the retained witness contract, at least six B-labelled. Same-label witnesses across colors are disjoint; all distinct witnesses are linear.
2. **New label-capacity theorem:** a pivot-labelled witness can occur in at most floor(v/4) colors. At E408 Q33, v=31 and c=8, so at least one color has seven B-labelled witnesses. Combining this with total excess four gives at least 17 zero-excess B-labelled witnesses across the eight colors. E407 has at least 14.
3. **Zero-excess graph theorem audited:** for a 284-edge core, after deleting the positive-excess vertices and then any further at most six vertices, an independent four-set remains. This gives a common unlabelled witness for any pair of regular B rows with at most three zero-excess neighbours each. For a 285-edge core the deletion threshold is only four.
4. **Omission-capacity theorem:** at the minimum-support boundary, with r_x witness multiplicity and o_x=c-r_x, e_H(U,W) is at least the sum of max(0,13-v+3(c-o_x)). It gives the verified profile tables in LABELLED_WITNESS_CAPACITY_THEOREM.md; in E408 Q33, Omega=sum binom(o_x,2)<=48 (and Omega<=24 when S0 is 12, 13, or 14).
5. **Edge multiplicity:** the exact crossing-edge load is sum over xy in E(H[U]) of r_x r_y, not the unweighted number of crossing edges. Its lower bound remains compatible with the available upper bound, so it does not close a terminal.

## Status by obligation

- E407 Q32, 49 witnesses / 29 support points: **OPEN**. Inherited S=epsilon_U+2delta>=9, delta>=3, epsilon_U+delta<=16. The labelled omission-capacity table correlates Omega with S but leaves profiles.
- E408 Q33, 56 witnesses / 31 support points: **OPEN**. Inherited universal S0=epsilon_U+2delta>=12, epsilon_U+delta<=17. The new omission bound excludes highly concentrated omission profiles but leaves the S0=12 relaxation.
- E408 Q32, 285-edge / excess-six core: **OPEN** and separate. The zero-excess theorem permits only four further deletions, so the pairwise row-union conclusion does not apply automatically when the union has size five or six.
- Original K145 reduction bridge and full EG617 theorem: **OPEN / NOT_CERTIFIED**.

## Minimum unresolved proposition

A pair of regular rows has a common independent four-set in H0, but this set is not necessarily a monochromatic component of an exact-129 color. The exact-129 label/edge-ownership theorem cannot be applied to an arbitrary independent set. The next advance must prove a label-transfer/component-realization lemma, a sharper hub-capacity theorem, or a finite incidence-design exclusion.

See the four theorem/audit files in this directory and verify_unified_witness_capacity.py.


## Verification note — 2026-10-25

The finite arithmetic and omission-profile enumerations were independently replayed in local Python and matched the checked-in verifier's expected tables. Result: R12_UNIFIED_WITNESS_CAPACITY_ARITHMETIC_OK. This is arithmetic verification only, not a graph search or witness-design realization certificate.

Latest progress-log commit: 6e374337ccf90fdb56de93669420f130bd3cdc5b.


## 2026-10-25 continuation — labelled partite capacity

### New proved-conditional results

1. **Per-part label-row capacity.** If the witness complement L is four-partite and every selected Q is a transversal, then a shell label b occurring in n_b selected components has at most |V_j|-n_b target neighbors in each part V_j, hence at most |U|-4n_b target neighbors in U. This follows because the n_b same-label witness sets are disjoint and b is target-anticomplete to each.
2. **Q33 four-partite exact incidence.** Under the eight-color / 56-transversal contract with parts (8,8,8,7), every size-seven-part vertex has witness multiplicity 8 and every large-part vertex multiplicity 7. Thus the omission profile is exactly (0^7,1^24), Omega=0, and the eight color omission triples partition the 24 large-part points.
3. **Labelled seven-point-part cap.** At each point of the size-seven part, the eight incident witness labels are distinct; at least seven are B labels. Hence each such point has at most three B-row target neighbors, or at most two if it has no pivot-labelled witness. Globally e_F(B,D)<=14+P<=21. Combined with the retained K_B>=22-beta, this gives e_F(B,H\\D)>=max(0,8-beta+G_B-P). It is a necessary constraint, not a contradiction.
4. **Four-partite edge-charge saturation.** In any four-partite witness branch, within-part H-edges contribute exactly 4-|Q_i intersection Q_j| for every witness pair. Therefore the generic pairwise crossing inequality is sharp on the within-part edges. For Q33 the exact weighted load is 5460+49(24-delta); the lower bound is 5460 and only implies delta<=24, compatible with the current delta in [9,17].

### Current sibling results incorporated (read-only)

- E408 Q33 global compatibility: workstream/r12-e408-q33-global-compat-20261025, head df396de8ffc1f9c390fe3e240d0d085715f86b5b; its four-partite theorem proves S0>=22, hence delta>=9.
- Row-transversal / pairwise hub-cover: workstream/r12-ultimate-closure-20261024, head 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40.
- Witness-packing / universal Q33 S0>=12: workstream/r12-witness-packing-chat-20261025, head f5d3daa07403877ede9885e1bd5c2f46b16d81da.

No sibling workstream was modified.

## Refined obstruction

The Q33 scalar relaxation with Omega=24 cannot be four-partite; it is only evidence that the scalar inequalities do not eliminate the non-four-partite branch. The four-partite branch now has exact incidence and label caps, but these remain compatible with the current edge budgets. The non-four-partite branch still requires a packing/stability theorem using the 56 labelled K4s beyond the second-Turán bound.


## Shell-row multiplicity audit — 2026-10-25

For a fixed common independent-four set Q, define \(\mu(Q)\) as the number of regular B rows it avoids. It can serve at most \(\binom{\mu(Q)}2\le45\) graph-theoretic pair certificates. The current \(|T_b|\le3\) condition does not imply a smaller universal cap. If Q is an actual selected exact-129 witness labelled b, the directly label-anchored pairs containing b are at most \(\mu(Q)-1\le9\); arbitrary \(Q_{bc}\) from the zero-excess existence theorem are not automatically labelled components. Thus the pairwise hub-cover count cannot be summed as though each pair had a distinct witness.


## Additional terminal-state refresh — 2026-10-25

Read-only canonical sources also refreshed during this continuation:

- E407/Q32 branch: workstream/r12-e407-q32-terminal-20261025, head 3f42fcce5761ca2372140618adda56f95fcbe253. Root canonical state still says E407/E408 are the only active T61 frontier and NOT_CERTIFIED.
- E408/Q32 excess-six branch: workstream/r12-e408-q32-excess6-20261025, head 23f020eaf8b9924da8e7a4841c370bae658bea41. Its 285-edge/excess-six contract is separate; no 284-edge conclusion from this workstream is transferred to it.
- E408/Q33 global compatibility branch: workstream/r12-e408-q33-global-compat-20261025, head df396de8ffc1f9c390fe3e240d0d085715f86b5b. Its four-partite branch has \(S_0\ge22\), while the non-four-partite terminal remains open.

All three sources were read-only; the only changed files remain in this workstream directory.


## Label-only feasibility check — 2026-10-25

The Q33 four-partite row/column label constraints admit an explicit 8-by-7 array: seven rows each contain p once and six distinct B labels, the eighth row contains seven B labels, each D column contains p plus all seven B labels, and every B label and p occurs seven times. This is only a label-incidence relaxation, not a realization of the 56 labelled K4s; it confirms that label counts alone are insufficient.


## 2026-10-25 continuation — outer exceptional-row coupling

### New conditional theorem

Added OUTER_EXCEPTIONAL_ROW_COUPLING.md. For an exact-129 color and two outer blocks both satisfying \(r_i(C),r_j(C)\le3\):

1. Each block has ten unique K5-component rows and two exceptional rows.
2. The two exceptional-row complements \(A_i,B_i\) and \(A_j,B_j\) are disjoint cliques in the 11-point gadget, with profiles (5,5), (5,4), (5,3), or (4,4).
3. Every nonempty intersection among these four complement pairs forces the corresponding exceptional-row edge to have color C.
4. Let k be the number of nonempty cells in the 2x2 intersection matrix and let \(\ell,c\) be its nonempty row/column counts. The block-pair duplicate budget obeys
   \[
   d_{ij}(C)\ge k+\max(2-\ell,2-c)-2.
   \]
   Therefore an adjacent two-cell pattern or any three-cell pattern costs at least one duplicate unit; a full 2x2 pattern costs at least two.
5. Summing over low-slack block pairs yields a lower bound on \(P_C\); summing over colors for a fixed block pair gives the cross-color constraint \(\sum_C\eta_{ij}(C)\le12\).

### Independent finite replay

Enumerated all 15 nonempty 2x2 masks in JavaScript. The exact duplicate-cost distribution is 6 masks at cost 0, 8 at cost 1, and 1 at cost 2; all four allowed complement-size profiles pass. Output: EXCEPTIONAL_ROW_MASK_REPLAY_OK. The Python verifier was updated to include the same exhaustive mask checks.

### Refreshed sibling status (read-only)

The latest E408 Q33 branch head is fec0100abbb6124d1efdad39f2f4b352e1c8bc76 (commit: exceptional-row refinement and duplicate thresholds). It independently records the two-exceptional-row gadget coverage and the low-slack thresholds. Its terminal remains OPEN / NOT_CERTIFIED. No sibling workstream was modified.

### Remaining gap

The new inequality does not force a positive duplicate cost when the intersection cells form one cell or a two-cell matching. Identical exceptional complement pairs across all low-slack blocks remain a compatible relaxation. A further theorem must show that the actual gadget and seven-block labels force non-matching patterns often enough, or couple them to the core K4 coordinates. EG617(r=12) remains OPEN / NOT_CERTIFIED.


## 2026-10-25 continuation — exceptional-row alpha-two theorem

Strengthened the outer coupling result. For any exact-129 color C, collect the two exceptional rows from every block with \(r_i(C)\le3\). The induced C-graph on this collection has
\[
\boxed{\alpha\le2.}
\]

Proof: a pairwise nonadjacent triple has pairwise-disjoint complementary gadget cliques, each of size at least three. The three rows have at least 22 incidences into the 11-point gadget but at most 24 total neighborhood incidences (at most 22 if two rows are from one block). Hence at most two incidences lie outside the gadget, too few to cover a K5 component. Choosing one vertex from each of the ten isolated K5 components and adding the three rows would give a C-independent 13-set.

Consequences:
- Between any two low-slack blocks, the C-nonedges among their four exceptional rows form a matching; hence there are at least two C-edges among the four rows.
- For k low-slack blocks, the exceptional-row graph has at least \(k(k-1)\) edges. Equality in the alpha<=2 Turan bound forces it to be \(K_k\dot\cup K_k\), so the two exceptional rows in each block occupy opposite cliques.
- This equality structure is compatible with the two-type exceptional-row pattern. Extra edges cost duplicate budget, but no contradiction has yet been derived from the current global budgets.

The updated verifier includes finite arithmetic checks for the alpha-two argument and Turan equality. Independent replay passed: EXCEPTIONAL_ROW_ALPHA2_REPLAY_OK. EG617(r=12) remains OPEN / NOT_CERTIFIED.


## 2026-10-25 continuation — near-complete component matching

### New cross-block theorem

Added Section 7 to OUTER_EXCEPTIONAL_ROW_COUPLING.md. Under the exact-129 Type-I row theorem, if two outer target blocks have duplicate parameters \(r_i(C),r_j(C)\le5\), each contains ten distinct rows representing the ten isolated K5 components. For any component label \(\ell\), if the two corresponding rows are nonadjacent in color C, their extra neighborhood incidences must either cover another full K5 component (at least five incidences) or cover at least six gadget vertices (at least six incidences). The total extra-incidence budget across the two blocks is \(r_i+r_j-2\le8\). Different missing labels use disjoint row-incidence charges. Therefore at most one same-component diagonal can be missing:
\[
m_{ij}(C)\le\left\lfloor\frac{r_i(C)+r_j(C)-2}{5}\right\rfloor\le1.
\]
Thus every such block pair has at least nine of the ten same-component representative edges. If \(r_i+r_j\le6\), all ten are forced, recovering the sharper known case. If \(r_i+r_j=7\) and one diagonal is missing, all five extra-incidence units must cover a second K5 component; none can be spent in the gadget.

### Independent finite arithmetic check

The verifier now checks all \(25\) integer pairs \(r_i,r_j\in\{1,\ldots,5\}\), the zero-missing threshold \(r_i+r_j\le6\), and the four sum-seven boundary pairs. This is an arithmetic consistency check; the graph-theoretic proof is the incidence argument above.

### Latest sibling heads refreshed

- E407 Q32 terminal: 7cced6ef1a4a8716aff95b3d704b579c3c0af859 — the \(\delta=15\) non-four-partite branch excludes two KP base profiles, but the balanced \((7,7,7,7)\) base remains open.
- E408 Q33 global compatibility: 131a362d2aa759a828bbd572a69aeff5e2062dfe — the exact-129 row theorem extends to \(r_i\le5\), and \(r_i+r_j\le6\) forces a ten-component matching.
- Ultimate closure: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 — the four-partite Q33 \(S_0=10\) equality kernel is excluded; the four-partite branch has \(S_0\ge22\), while the non-four-partite branch remains open.
- E408 Q32 remains a separate 285-edge core and is not covered by the 284-edge conclusions here.

No sibling workstream was modified. The new theorem is a structural strengthening, not a complete terminal contradiction. EG617(r=12) remains OPEN / NOT_CERTIFIED.


## 2026-10-25 continuation — mismatch-to-duplicate charging

The near-complete matching theorem now has a stronger edge-ownership corollary. For any exact-129 color C and any pair of outer blocks with \(r_i(C),r_j(C)\le5\), let \(m_{ij}(C)\) count missing same-component diagonal edges. Then
\[
m_{ij}(C)\le1,\qquad \boxed{m_{ij}(C)\le d_{ij}(C)}.
\]
The second inequality is proved by contradiction: if one diagonal were missing while \(d_{ij}=0\), the block-pair C graph would be a perfect matching. The remaining rows force an independent triple of exceptional rows. The missing diagonal consumes at least five of the at-most-eight extra row-neighborhood incidences, leaving at most three—insufficient to cover any full K5 component. One vertex from each of the ten components plus the triple gives a C-independent 13-set.

Thus the exact global duplicate budget pays for every missing component-label alignment:
\[
\sum_{\{i,j\}\subseteq\mathcal I_C}m_{ij}(C)\le P_C,
\quad \mathcal I_C=\{i:r_i(C)\le5\}.
\]
The Python arithmetic replay independently checked all 25 row-budget pairs and the sum-seven boundary. Result: PASS. This is a conditional cross-block theorem; it does not yet bound \(P_C\) tightly enough to eliminate the remaining terminals.


## 2026-10-25 continuation — aggregate-budget relaxation audit

Added a reproducible scalar relaxation in COUNTEREXAMPLE_OR_GAP_AUDIT.md and the verifier. It satisfies \(P_C+R_C+s_C=62\) for all 11 colors, \(\sum P_C=252\), \(\sum R_C=427\), \(\sum s_C=3\), every block-column sum \(\sum_C r_i(C)=61\), and every block-pair duplicate column sum \(\sum_C d_{ij}(C)=12\). Yet all eight exact colors can have \(P_C=9\) and \(r_i(C)\in\{7,8\}\), with the three nonexact colors absorbing \(P=(59,60,61)\).

This is an explicit **aggregate relaxation**, not a graph-level counterexample. It establishes that the aggregate \(P_{\rm exact}\ge69\) inequality cannot force any exact color to satisfy \(P_C\ge36\), so the new near-matching theorem cannot be activated from aggregate budgets alone. A terminal proof must add a genuine graph/witness constraint coupling the three nonexact colors or the component-label geometry to these scalar variables.


## 2026-10-25 continuation — duplicate budget forces common component cliques

Added Theorem 9.1 in OUTER_EXCEPTIONAL_ROW_COUPLING.md. For every exact-129 color C, let \(n_i(C)\) be the number of size-five blocker rows in outer block \(B_i\). The exact blocker theorem says each such row corresponds to one distinct K5 component; the incidence ledger yields \(n_i(C)\ge11-r_i(C)\). Therefore the number of K5 component labels represented by size-five blockers in all seven blocks is at least
\[
10-\sum_i(10-n_i)\ge17-R_C=P_C-45.
\]
Each common label has seven outer representatives with C-neighborhood exactly that K5 component. Any pair of representatives must be adjacent or else the two rows, one vertex from each of the other nine components, and an independent pair in the gadget form a C-independent 13-set. Hence each common label extends to a vertex-disjoint monochromatic K12:
\[
\boxed{\nu_{12}(C)\ge\max(0,P_C-45).}
\]

The same file records the stronger high-budget cases:
- \(P_C\ge51\): all ten K5 components extend to ten disjoint K12s.
- \(P_C=50\): at least eight disjoint K12s.
- \(P_C=49\): at least four disjoint K12s, with stronger bounds when the row profile is more regular.

The verifier now exhausts all positive \(r\)-profiles with \(r_i\le5\) and \(R_C=11,12,13\), confirming the maximum number of block pairs with sum at least seven is 0, 1, and 2, respectively. This is exact finite arithmetic supporting the branch split; the clique-packing theorem is conditional on the exact-129 factor/blocker contract.


## 2026-10-25 latest sibling synchronization

Refreshed all six sibling branches again before finalizing this round:

- E407 Q32 terminal: f4b0e246e8f8f2dade3763c4c9dbd2bfffe18b0e. Latest update excludes the \(\delta=15\) non-four-partite branch and two \(\delta=15\) four-partite W-profiles; the remaining \(\delta=15\) four-partite \(K_3\cup3K_5\) / \(D\cup K_3=K_{11}\) profile is still open. E407 overall remains OPEN.
- E408 Q33 global compatibility: a6bbb918c3484bedd1a4eafb410901288cdff085. Latest update finalizes the \(r_i=6\) row classification and high-\(P_C\) clique-packing branches; the Q33 terminal remains OPEN.
- E408 Q32 excess-six: a0ba6db26c7e8b00a4217dcbcbf298895dff93ce. This is the separate 285-edge core and is not closed by the 284-edge witness-capacity results.
- Witness-packing: f5d3daa07403877ede9885e1bd5c2f46b16d81da.
- Zero-excess witness: 07d19abfd6c1c749c7360526e4a04a3eb865fb2e.
- Ultimate closure: 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40.

Created TERMINATION_CLOSURE.md with the conditional theorem ledger, the scalar-relaxation obstruction, the minimal missing bridge, dependencies, and verification scope. All reads of sibling branches were read-only.


## 2026-10-25 continuation — selected-witness extension (corrected, S-avoidance strengthening)

The graph-theoretic witness family does not automatically consist of seven isolated K5 components. However, the earlier five-component transfer floor can be strengthened to six.

The exact-129 factorization has ten isolated K5 components avoiding the three-point set \(S\), plus an 11-point gadget \(U_C\). Hence \(S\subseteq U_C\) and \(|U_C\setminus S|=8\). Every selected witness \(\{\lambda\}\cup Q\) avoids \(S\), with \(Q\subseteq H\setminus S\) a four-set and \(\lambda\in B\cup\{p\}\) outside \(H\). If two selected witnesses lay in \(U_C\), their disjoint four-sets would occupy all eight points of \(U_C\setminus S\), leaving no room for the first witness's shell label. Thus at most one selected witness lies in the gadget and at least six of seven are distinct isolated-component witnesses. At least five of the six B-labelled witnesses are isolated components.

The common exact size-five blocker set across the seven outer blocks has size at least \(P_C-45\). Inclusion-exclusion across the ten isolated components now gives
\[
|\mathcal W_C\cap\mathcal K_C^*|
\ge\max(0,6+(P_C-45)-10)
=\max(0,P_C-49).
\]
Therefore \(P_C\ge50\) guarantees at least one selected witness component extends by exact blocker rows from all seven outer blocks to a monochromatic \(K_{12}\); \(P_C=51\) guarantees at least two. This is a structural packing constraint, not a terminal contradiction, because a monochromatic \(K_{12}\) is allowed.

## 2026-10-25 sibling refresh correction

A later read supersedes the E407 head recorded in the previous section. The latest E407 Q32 branch is now bd385f7dfe102deb426810baf1999a8e94dd488f. Its newest commit clarifies the standalone \(\delta=16\) clique obstruction; the current canonical state now records both the \(\delta=16\) four-partite extreme and the \(\delta=15\) four-partite branch as EXCLUDED under their retained contracts. E407 overall remains OPEN because templates A–E, the \(\delta=14\) compatibility branch, and the low-excess non-four-partite branch are still open.

Other latest sibling heads are unchanged: E408 Q32 a0ba6db26c7e8b00a4217dcbcbf298895dff93ce; E408 Q33 a6bbb918c3484bedd1a4eafb410901288cdff085; witness-packing f5d3daa07403877ede9885e1bd5c2f46b16d81da; zero-excess witness 07d19abfd6c1c749c7360526e4a04a3eb865fb2e; ultimate closure 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40.


## 2026-10-25 continuation — E407/E408 top-cell-A cross-layer rigidity

Added Theorems 11.1–11.2 and Corollary 11.3 to OUTER_EXCEPTIONAL_ROW_COUPLING.md, conditionally combining the sibling T61 top-cell-A theorem with the exact-129 factor theorem.

**Exact intersection pattern.** Since each non-target color is a near-perfect matching on the 23-point set W, every isolated K5 component of an exact-129 color intersects W in at most two vertices. The 11-point gadget U must intersect W in 3 or 4 vertices because alpha(U)<=2. Consequently the ten K5 components meet W in exactly one of two profiles: \(2^{10}\), or \(2^9,1\). The gadget restriction is respectively one edge plus an isolate, or a two-edge perfect matching. Thus every exact color contributes at least nine component edges to its W matching.

**Global defect identity.** Let O=V(F)\\W (38 vertices), \(\kappa_v=d_F(v)-13\), \(K_W=\sum_{w\in W}\kappa_w\), and \(t_C=e_C(O)-42\). The Turan floor gives \(t_C\ge0\). The exact cross-edge ledger is
\[
e_C(W,O)=76+s_C-t_C,\qquad
e_F(W,O)=35+K_W.
\]
Summing over colors and using \(\sum_C s_C=411-E\) yields
\[
\sum_C t_C=K_W+411-E-3.
\]
Hence E408 gives \(\sum_C t_C=K_W\), and E407 gives \(\sum_C t_C=K_W+1\).

**Exact-color defect cap.** In either intersection profile, the ten K5 components and the gadget degree floor imply \(42\le e_C(O)\le48\), so \(0\le t_C\le6\) for exact-129 colors. When \(t_C=0\), equality in Turan forces \(C[O]\) to be ten K3s plus two K4s. This creates a near-Turan decomposition problem on O shared by all eleven non-target colors.

The arithmetic replay passed for all \(K_W\in[0,23]\) in E408 and \(K_W\in[0,21]\) in E407. This is a conditional exact ledger, not a contradiction. The next gap is to exploit simultaneous edge-disjoint 10-triangle/2-K4 partitions when many colors have \(t_C=0\), or to show the \(t_C\) distribution cannot meet the target shell/core geometry.


## 2026-10-25 continuation — zero-defect Type-A gadget rigidity

Added Corollary 11.4. In the exact-129 Type-A intersection profile with \(t_C=0\), \(U[O]=K_4\cup K_4\), \(U[W]=K_2\cup K_1\), and the gadget has exactly 16 cross edges. The independence-number cap forces the two adjacent W-gadget vertices to be complete to opposite K4s. The isolated W-gadget vertex must be complete to one K4 and to all but \(a\) vertices of the other, while the adjacent endpoint on the latter side covers those \(a\) missed vertices. The 16-edge budget then leaves no additional cross edges and forces \(a\in\{0,1,2,3\}\).

The resulting gadget degree multiset is either \(5^{10},8\) or \(5^9,6,7\). In particular, every gadget vertex has degree at least five, and the W vertex unmatched by \(C[W]\) has degree \(5\)–\(8\). The verifier's degree-profile arithmetic passed for all four values of \(a\). This strengthens the zero-defect structural case but does not by itself force a contradiction with the target degree ledger.


## 2026-10-25 continuation — low-slack duplicate location

Added Corollary 11.5 in OUTER_EXCEPTIONAL_ROW_COUPLING.md. Under top-cell A, if an exact-129 color has \(r_i(C)=1\), the exact row theorem forces ten component rows of size five and two exceptional rows of size six. The K5-component W incidences are 20 in Type A and 19 in Type B; disjoint exceptional gadget K5s cover all but one gadget vertex, so their two complement rows contribute 3/4 W-incidences in Type A and 4/5 in Type B. Thus \(e_C(B_i,W)\in\{23,24\}\).

Every \(w\in W\) has at least one edge of each of the eleven non-target colors to \(B_i\), because otherwise \(B_i\cup\{w\}\) is a 13-set missing that color. The 12 edges from w to B_i therefore contain exactly one repeated non-target color and no target-color edge. Consequently \(e_C(B_i,W)=23+r_i^W(C)\): value 23 means the unique repeated-C vertex lies in O; value 24 means it lies in W. This identifies the duplicate location from the exact gadget-pair profile and avoids treating baseline edges as duplicates.

Latest sibling refresh: E408 Q33 advanced to c01f7dc6951b2bb7ea5209f252b1644ca0ecd40a with Theorem 12.1 gadget normal form and stronger \(P_C=49,50\) clique packings. E407 Q32 remains bd385f7dfe102deb426810baf1999a8e94dd488f; E408 Q32 remains a0ba6db26c7e8b00a4217dcbcbf298895dff93ce; witness-packing f5d3daa07403877ede9885e1bd5c2f46b16d81da; zero-excess 07d19abfd6c1c749c7360526e4a04a3eb865fb2e; ultimate closure 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40.


## 2026-10-25 sibling audit — external-edge claims are not certified

The sibling E408 Q33 argument that \(P_C=50,r_i=6\) is excluded relies in places on the assertion that a single external \(C\)-edge from a monochromatic \(K_{12}\) is impossible. That assertion is false as stated: the star condition gives only \(d_C(z,K_{12})\le1\). The sibling \(P_C\le49\) and \(P_C\le48\) proofs similarly use the invalid isolation lemma and must not be used as certified budget caps until repaired.

## 2026-10-25 continuation — conditional local exclusion of \(P_C=49,r_i=6\)

The local theorem in OUTER_EXCEPTIONAL_ROW_COUPLING.md is independent of the invalid isolation lemma. It now constructs a \(C\)-colored \(K_{12}\) and forces one external vertex to have at least two \(C\)-edges into it. The exact verifier uses all four gadget normal forms, exact Case-C complement profiles, and the safe-row component-incidence split. The revised predicate replay passed 2,132 Case-A/B configurations and 512,768 exact-profile Case-C configurations (514,900 total).

This proves only the local corner \(P_C=49,r_i=6\), conditional on the exact-129 factor theorem, seven-block contract, gadget normal form, and row classifications. It does not prove \(P_C\le49\), does not close the aggregate eleven-color ledger, and does not prove EG617(r=12).

## 2026-10-25 proof audit — external edge versus double-star; P49/r=6 verifier strengthened

**Important correction to prior notes:** the sibling E408 Q33 Lemma 2.1 claims that a monochromatic \(K_{12}\) has no external edge of its own color. That inference is invalid. The twelve edges from an outside vertex must contain all eleven other colors, so the correct conclusion is only \(d_C(z,K_{12})\le1\). A single external \(C\)-edge is allowed. Therefore sibling conclusions whose sole contradiction is one external \(C\)-edge—including the current \(P_C\le49\) and \(P_C\le48\) boundary proofs—must be treated as **NOT CERTIFIED until repaired**. Do not use those caps as dependencies in this workstream.

The local \(P_C=49,r_i(C)=6\) result in Section 12 of OUTER_EXCEPTIONAL_ROW_COUPLING.md has been rewritten to use the valid **double-star** condition \(d_C(z,K_{12})\ge2\), not the false isolation claim. Its finite checker now uses the exact Case-C complement-size profiles and distinguishes high-row profiles where both candidate high rows must be checked from profiles where either row is incidence-safe. The component-incidence argument is explicit: the selected high gadget-only row has at most two partial component incidences in the risky profiles and at most three otherwise; the selected \(r=2\) row has at most one. Hence no pair of selected rows covers a full isolated \(K_5\), which is needed for the pairwise blocker step.

The in-session replay of the revised finite predicates passed 2,132 Case-A/B configurations and 512,768 exact-profile Case-C configurations, 514,900 total. This is a conditional local theorem under the exact-129 factor, gadget normal form, and row contracts. It **does not** prove \(P_C\le49\), does not close the aggregate eleven-color ledger, and does not solve EG617(r=12).


## 2026-10-25 label-transfer audit — S-avoidance strengthens the component floor

The previous generic estimate \(\lfloor 11/4\rfloor=2\) gadget witnesses ignored that all selected witnesses avoid \(S\). The ten isolated components avoid \(S\), so all three vertices of \(S\) belong to \(U_C\). Thus \(|U_C\setminus S|=8\). Two gadget witnesses would have disjoint four-sets filling these eight vertices, while the shell label of either witness is an additional non-S gadget vertex outside \(H\), impossible. At most one selected witness can lie in the gadget.

Corrected transfer floor: at least six of the seven selected witness K5s are isolated components; at least five of the six B-labelled witnesses are isolated components. With \(|\mathcal K_C^*|\ge P_C-45\) among ten components,
\[
|\mathcal W_C\cap\mathcal K_C^*|\ge\max(0,P_C-49).
\]
Thus the selected-witness extension threshold improves from \(P_C\ge51\) to \(P_C\ge50\). This remains a labelled packing constraint only; it does not itself contradict the K145 coloring or close EG617(r=12).


## 2026-10-25 continuation — all ten exact components are shell witnesses

A stronger exact-factor argument is now recorded in LABELLED_WITNESS_CAPACITY_THEOREM.md, Theorem 12.1. Every isolated K5 component avoids S and must meet \(V(R)\setminus H\), since \(\alpha(H)\le4\). Its outside-H vertices lie in \(B\cup\{p\}\); because \(B\) is a target-color clique and \(p\) is target-adjacent to every vertex of \(B\), a C-colored component contains at most one such vertex. Therefore every isolated component has exactly one shell label and four core vertices. The ten component labels are distinct, so every exact-129 color has ten component-backed shell witnesses, at least nine B-labelled.

This does not identify the particular seven witnesses minimizing support with seven of these ten components. The selected minimum-support family still has at least six component-backed witnesses by the S-avoidance lemma, but its support union may be smaller than the union of all ten components per color.

New independent high-support reduction: let \(U_{\rm comp}\) be the union of all ten component four-sets per exact color. Then \(|U_{\rm comp}|\ge40\). If \(m=10\) exact colors and \(|U_{\rm comp}|=40\), the 100 component K4s require 600 distinct edges in \(\overline{H[U_{\rm comp}]}\), while the 284-edge core ledger and \(\alpha(H[W])\le4\) give at most 581. Contradiction. Hence \(m=10\Rightarrow |U_{\rm comp}|\ge41\). At support 41, the 100 K4s leave at most ten additional complement edges; this is the next near-decomposition terminal, not yet closed.

The original seven-per-color support boundary \(v=29/31\), the \(m=8,9\) full-component supports \(v\ge40\), the \(m=10,v\ge41\) terminal, the global eleven-color ledger, and the K145-to-T61 bridge remain OPEN / NOT_CERTIFIED.
