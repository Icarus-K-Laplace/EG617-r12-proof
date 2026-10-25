# Open gaps — E407 Q32 terminal workstream

Date: 2026-10-25  
Branch: workstream/r12-e407-q32-terminal-20261025

## 1. Headline status

**E407 Q32: OPEN / NOT_CERTIFIED. EG617(r=12): OPEN / NOT_CERTIFIED.**

The current workstream has substantially narrowed the front-end structural boundary, but it has not eliminated all five \(\rho=0\) shell templates A–E or certified the original \(K_{145}\) reduction.

## 2. Closed branches under their retained contracts

- \(\delta=16\), four-partite: excluded by the endpoint-split/excess argument and forbidden \(K_{12}\).
- \(\delta=15\), four-partite: excluded.
- \(\delta=15\), non-four-partite: excluded under the retained second-Turán/Kang–Pikhurko equality contract.
- \(\delta=14\), four-partite, \(\epsilon_U=0\): all four W profiles excluded.
- \(\delta=14\), four-partite, \(\epsilon_U=1\): all three W profiles excluded. Exhaustiveness uses Brouwer's second-Turán bound on \(\overline{H[W]}\), which has 18 vertices and 120 edges.
- \(\delta=14\), four-partite, \(\epsilon_U=2\): Turán equality forces \(H[W]=K_4\cup K_4\cup K_5\cup K_5\), and the common-neighbour capacity bound is at most 24, below \(|U|=29\).

These results remain conditional on the upstream 61-point residual/T61 bridge, the 49-witness minimum-support boundary, and the exact-129 factor theorem as recorded in the dependency ledger. They are not unconditional proofs from an arbitrary \(K_{145}\) coloring.

## 3. Remaining mathematical cases

### Gap A — \(\delta=14\), non-four-partite \(L=\overline{H[U]}\)

Here \(|U|=29\), \(e(H[U])=98\), and \(e(L)=308\). The Turán number is \(t_4(29)=315\); Brouwer's non-four-partite upper bound is 309. The augmentable-edge subcase is now excluded by DELTA14_NONPARTITE_AUGMENTABLE_TERMINAL_CLOSURE.md. The remaining saturated case is still OPEN. DELTA14_SATURATED_TRANSVERSAL_REDUCTION.md gives a strict extension reduction **only for the explicit C5-blow-up candidate** in DELTA14_SATURATED_LOCAL_MODEL.md: its \(\epsilon_U=0\) extension is impossible, and \(\epsilon_U=1,2\) force two exact W terminals. The local-model reduction does not prove that every admissible 15-vertex saturated graph \(J\) is this blow-up. The next general theorem must classify the admissible \(J\)'s or derive a degree/transversal property that holds for all of them.

### Gap B — \(\delta\le13\)

The current sibling transversal/excess contract gives
\[
3\le\delta,\qquad \epsilon_U+2\delta\ge9,\qquad \delta+\epsilon_U\le16.
\]
New Round 23 closes the \(\delta=13\), four-partite-U, no-cross-edge-W profiles for \(\epsilon_U=1,2,3\), with common-neighbour cover bounds 27, 28, 28, and 23. The remaining cases include \(\delta=13,\epsilon_U=0\), \(\delta=13\) W-cross-edge profiles, non-four-partite U-complements, and \(\delta\le12\). The argument is specific to the stated no-cross profiles; it does not silently extend to other structures.

### Gap C — five common-core shell templates A–E

The five templates still need a single shared-core compatibility contradiction. Excluding the four-partite \(\delta=14\) row does not show that the remaining non-four-partite or lower-\(\delta\) cores cannot realize a template. The proof must preserve labels and account for all core and shell-core edge multiplicities.

### Gap D — upstream reduction and source contracts

The chain
\[
K_{145}\text{ hypothetical counterexample}
\Longrightarrow \text{T61 residual}
\Longrightarrow \text{49-witness, 47-core boundary}
\]
remains an explicit dependency. A theorem conditional on the core contract cannot be promoted to an unconditional \(K_{145}\) proof until this bridge and the exact-129 equality classification are independently certified end-to-end.

## 4. Source/ledger audit warning

The inherited file DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md discusses \(K_3\cup K_5^3\) at \(\epsilon_U=2\) in one subsection. That graph has 33 edges, whereas the exact \(\delta=14,\epsilon_U=2\) ledger requires \(e(H[W])=32\). That profile is inadmissible for this contract and is not used in the current proof chain. The valid \(\epsilon_U=2\) W profile is the Turán-equality graph \(K_4\cup K_4\cup K_5\cup K_5\), treated in DELTA14_EPS2_W_PROFILE_CLASSIFICATION.md and Section 5 of the inherited component-capacity file.

## 5. Next highest-leverage target

**Current target: move to the remaining delta<=13 ledger and the five E407 shell templates.** The general delta=14 non-four-partite saturated terminal is now conditionally excluded by DELTA14_SATURATED_KERNEL_CLASSIFICATION.md together with DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md. This closure depends on the retained alpha-critical kernel reduction, especially the unaudited Didin-preprint component-count step. Do not promote the whole E407 Q32 boundary or EG617(r=12) to closed.

## Round 14 update — current live frontier

All four-partite cases at \(\delta=14\) are now excluded for every allowed \(\epsilon_U\in\{0,1,2\}\). The \(\epsilon_U=2\) case is forced to the unique Turán-equality W profile and excluded by the common-neighbour cap in DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md, Section 5.

The live structural gaps are now only:
1. \(\delta=14\) with \(L=\overline{H[U]}\) non-four-partite;
2. \(\delta\le13\), where the \(\delta=14\) four-partite profile arguments do not transfer unchanged.

E407 Q32, all five shell templates A–E, and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## Round 16 update — augmentable-edge branch closed

Under the retained T61/49-witness contract, the only \(\delta=14\) non-four-partite branch not excluded is now \(K_5\)-saturated \(L\). The augmentable-edge terminal has been eliminated by the partition \(U=S_0\dot\cup S_1\dot\cup S_2\dot\cup S_3\) and the common-neighbour capacity bounds \(n_i\le4+E_i\) for saturated \(K_5\) components and \(n_i\le7\) for unsaturated ones. The arithmetic verifier reports maxima 25, 27, and 25 for the all-saturated, one-star-unsaturated, and exceptional mixed cases, all below 29; the multiple-unsaturated case is ruled out structurally by the 9-point shared set \(R\).

The current highest-leverage target is the \(K_5\)-saturated case. The \(\delta\le13\) cases, five shell templates, and the \(K_{145}\)-to-T61 bridge remain OPEN / NOT_CERTIFIED.


## Round 17 update — the \(\delta=14\) saturated branch has one exact residual kernel

The augmentable-edge subcase remains excluded. For the remaining \(K_5\)-saturated non-four-partite case, the new conditional reduction in DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md proves that \(G=H[U]\) is \(\alpha\)-critical and, conditional on Didin's 2026 preprint theorem, has exactly three connected components. The 49 witness \(K_4\)'s and the exact 98-edge ledger force the unique profile
\[
H[U]=K_7\dot\cup K_7\dot\cup D,\quad
\alpha(D)=2,\quad e(D)=56.
\]
The complement of \(D\) is a triangle-free non-bipartite saturated graph with 49 edges, and the witness family induces two orthogonal near-perfect matching decompositions of its edge set.

This does **not** yet rule out the terminal graph. The external Didin preprint theorem is explicitly an unverified dependency, and the graph-realization problem for the 15-vertex kernel remains OPEN. The \(\delta\le13\) cases, five shell templates A–E, and upstream \(K_{145}\)-to-T61 bridge also remain OPEN / NOT_CERTIFIED.


## Round 18 update — local-only saturated obstruction is false

DELTA14_SATURATED_LOCAL_MODEL.md constructs and verifies a genuine local realization of the 29-point saturated non-four-partite graph and its 49 linear witnesses, partitioned into seven disjoint classes of seven. Thus one must **not** try to close the branch using only the 29-point graph, \(K_5\)-saturation, the 98-edge ledger, and the abstract 49-witness packing: those constraints are compatible.

The remaining task is to determine whether this local model—or any other surviving \(\delta=14\) model—can extend to the required 18-vertex \(W\), 47-vertex core, and shell-row labels. In the explicit model, if all degree excess lies in \(W\), the required \(U\)-to-\(W\) degrees are \(6^{14},5^{10},4^4,2^1\), totaling 152. The exact core independence/clique conditions and five shell templates must be enforced simultaneously. No global completion or counterexample has been constructed.


## Round 19 scope correction — explicit local candidate only

The transversal argument depends on the singleton \(d_0\) of the explicit C5-blow-up J, with \(d_J(d_0)=4\). That local graph is a verified realization, not a classification theorem for all saturated J graphs. Therefore:
- candidate-specific result: \(\epsilon_U=0\) is impossible; \(\epsilon_U=1,2\) force the stated W profiles;
- general saturated non-four-partite \(\delta=14\) branch: **OPEN** until the admissible J family is classified or the required low-degree property is proved universally.


## Round 20 update — explicit local candidate's extension terminals closed

DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md excludes epsilon_U=1,2 for the explicit C5-blow-up local graph; Round 19 already excluded epsilon_U=0. The local candidate therefore cannot extend to the full 47-core under the retained contracts.

This does not close the general non-four-partite saturated branch. The remaining saturated-kernel question is whether other 15-vertex triangle-free, non-bipartite, triangle-saturated graphs with 49 edges and the required witness-induced matching structure exist and, if so, whether any can extend. The delta<=13 cases, five shell templates, and upstream bridge remain OPEN / NOT_CERTIFIED.


## Round 22 update — general saturated delta=14 branch closed conditionally

DELTA14_SATURATED_KERNEL_CLASSIFICATION.md proves that any admissible J in the retained 15-vertex kernel contract must have a degree-4 vertex v; J-v is K7,7 minus K2,2, and J is the C5 blow-up with part sizes (1,2,5,5,2). The earlier candidate-extension theorem then rules out every W-extension for epsilon_U=0,1,2. Therefore this entire saturated delta=14 subcase is conditionally excluded.

The proof uses the AES equality case at minimum degree 2n/5 and the Brouwer/Kang–Pikhurko bound for non-bipartite triangle-free graphs on 14 vertices. The upstream extraction of the 15-vertex J remains conditional on the Didin-preprint component-count theorem. Remaining live gaps: delta<=13, all five E407 shell templates, and the original K145-to-T61 bridge.


## Round 23 update — delta-13 no-cross-edge W profiles

DELTA13_FOUR_PARTITE_NO_CROSS_W_PROFILES.md closes all four no-cross-edge W profiles compatible with \(\delta=13\), \(\epsilon_U\in\{1,2,3\}\), under the four-partite U-complement contract. The proof combines the 49 transversal witnesses, the exact eight U-cross-edge ledger, a reverse-saturation lemma, and componentwise common-neighbour capacities. The arithmetic verifier independently checks the profile list and capacity arithmetic.

Round 24 also excludes the \(\delta=13,\epsilon_U=1) profile (K_3cup3K_5) with one W-cross-edge. The next target is the remaining (epsilon_U=1) profiles: (3K_4cup K_6) plus one edge and (2K_4cup2K_5) plus two edges. Then handle the (epsilon_U=2) ((4,4,5,5))-plus-one-edge profile, (epsilon_U=0), non-four-partite (U)-complements, and (deltale12). Do not claim the entire (delta=13) row is closed.


## Round 24 update — delta-13 one-cross-edge profile

DELTA13_EPS1_K3K5K5K5_ONE_CROSS_EDGE.md excludes \(H[W]=K_3\dot\cup3K_5\) plus one edge for \(\delta=13,\epsilon_U=1\), under the four-partite-U contract. The exact transversal argument permits at most one nonsaturated U-vertex; the common-neighbour capacity sum is at most 26, while at least 28 U-vertices must be covered.

The immediate next target is the remaining \(\epsilon_U=1\) profiles with W-cross-edges: \(3K_4\dot\cup K_6\) plus one edge and \(2K_4\dot\cup2K_5\) plus two edges.
