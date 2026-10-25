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

Here \(|U|=29\), \(e(H[U])=98\), and \(e(L)=308\). The Turán number is \(t_4(29)=315\); Brouwer's non-four-partite upper bound is 309. The augmentable-edge subcase is now excluded by DELTA14_NONPARTITE_AUGMENTABLE_TERMINAL_CLOSURE.md. The saturated case is now **PROVED_CONDITIONAL excluded** by DELTA14_SATURATED_KERNEL_CLASSIFICATION.md and DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md: under the retained alpha-critical kernel reduction, every admissible \(J\) is the \(C_5\)-blow-up with parts \((1,2,5,5,2)\), and it has no full-core extension for \(\epsilon_U\in\{0,1,2\}\). This still depends on the unaudited Didin-preprint component-count step.

### Gap B — \(\delta\le13\)

The retained transversal/excess contract gives
\[
3\le\delta,\qquad \epsilon_U+2\delta\ge9,\qquad \delta+\epsilon_U\le16.
\]
At \(\delta=13\), the four-partite-U, no-cross-edge-W profiles for \(\epsilon_U=1,2,3\) are excluded. At \(\epsilon_U=1\), both one-cross-edge placements of \(3K_4\dot\cup K_6\) and the \(K_3\dot\cup3K_5\)-plus-one-edge profile are also excluded. The \(\epsilon_U=1\), \(2K_4\dot\cup2K_5\)-plus-two-edge profile is now **EXCLUDED** by DELTA13_EPS1_TWO_CROSS_EDGE_TERMINAL_CLOSURE.md. Still open in this four-partite-U row is the \(\epsilon_U=2\), \(2K_4\dot\cup2K_5\)-plus-one-edge profile. The excluded profiles are conditional on the retained 49-witness/core contract; they do not close the whole \(\delta=13\) row.

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

Round 24 also excludes the \(\delta=13,\epsilon_U=1\) profile \(K_3\dot\cup3K_5\) with one W-cross-edge. The next target is the remaining \(\epsilon_U=1\) profiles: \(3K_4\dot\cup K_6\) plus one edge and \(2K_4\dot\cup2K_5\) plus two edges. Then handle the \(\epsilon_U=2\), \((4,4,5,5)\)-plus-one-edge profile, \(\epsilon_U=0\), non-four-partite U-complements, and \(\delta\le12\). Do not claim the entire \(\delta=13\) row is closed.

## Round 24 update — delta-13 one-cross-edge profile

DELTA13_EPS1_K3K5K5K5_ONE_CROSS_EDGE.md excludes \(H[W]=K_3\dot\cup3K_5\) plus one edge for \(\delta=13,\epsilon_U=1\), under the four-partite-U contract. The exact transversal argument permits at most one nonsaturated U-vertex; the common-neighbour capacity sum is at most 26, while at least 28 U-vertices must be covered.

The immediate next target is the remaining \(\epsilon_U=1\) profile \(2K_4\dot\cup2K_5\) plus two W-cross-edges, followed by the \(\epsilon_U=2\), \(2K_4\dot\cup2K_5\)-plus-one-edge profile.


## Round 25 update — delta-13 K4-K6 cross-edge

DELTA13_EPS1_3K4_K6_K4K6_EDGE.md excludes the \(\epsilon_U=1\), \(3K_4\dot\cup K_6\) W-profile when the unique W-cross-edge joins a \(K_4\) to the \(K_6\). All U-vertices are W-saturated, and common-neighbour capacities are at most \(9+9+9+1=28<29\).

The K4–K4 placement was closed in Round 26; the next local target is \(2K_4\dot\cup2K_5\) plus two W-cross-edges at \(\epsilon_U=1\).


## Round 26 update — both \(3K_4\dot\cup K_6\) edge placements

The K4–K4 placement is now excluded as well. If the only possible degree-seven unsaturated U-vertex exists, all but one U-vertex must be covered by the four common-neighbour sets. Equality in the total capacity forces all three K4 capacities to be nine and their labels to be small U-parts. The exceptional vertex's own part cannot be a label; by pigeonhole two K4 components share one of the other two small parts, so their common-neighbour sets overlap in at least seven vertices. Their union cannot cover 28 vertices.

Thus both placements of the unique W-cross-edge in the \(\delta=13,\epsilon_U=1\), \(3K_4\dot\cup K_6\) profile are closed.


## Round 27 audit update — independent proof and current frontier

The new DELTA13_EPS1_K4K4K4K6_ONE_CROSS_EDGE.md independently closes both K4–K6 and K4–K4 placements of the \(\delta=13,\epsilon_U=1\), \(3K_4\dot\cup K_6\)-plus-one-edge profile. Unlike a proof that assumes at most one nonsaturated U vertex, it permits an arbitrary exception set \(E\) and derives the strict cover inequality \(29-k>29-2k\) when \(k=|E|>0\). The finite verifier confirms the label/load arithmetic, not the analytic graph lemmas.

**Next target:** \(\delta=13,\epsilon_U=1\), \(2K_4\dot\cup2K_5\) plus two W-cross-edges. Then handle the \(\epsilon_U=2\), \((4,4,5,5)\)-plus-one-cross-edge profile, \(\epsilon_U=0\), non-four-partite U-complements, and \(\delta\le12\). The five shell templates and \(K_{145}\)-to-T61 bridge remain OPEN / NOT_CERTIFIED.


## Round 28 — remaining delta-13, epsilon_U=1, two-cross-edge profile

The profile H[W]=2K4 union 2K5 plus two cross-edges is reduced as follows. The exact transversal-blocker lemma classifies every W-unsaturated U-vertex as Type I (one-edge blocker with singleton endpoint non-neighbour sets) or Type II (same-pair two-edge star with non-neighbour-set sizes 2 and 1). The common-neighbour capacity proof gives |S_K4|<=9 and |S_K5|<=2+E_i, hence k>=4; if any cross-edge meets a K4, then k>=5. If both edges lie between the K5 parts, the blocker classification gives k<=1, so that placement is excluded.

**Remaining exact blocker:** at least five U-vertices are W-unsaturated, the two-edge graph has at least one endpoint in a K4 part, and each exception has one of the certified Type-I/Type-II forms. The next step is a joint labelled-incidence contradiction for this k>=5 family. This is a strict reduction, not full closure.


## Round 29 — saturated (delta=14) terminal closed conditionally; audit correction recorded

The earlier candidate-extension proof's total common-neighbour bound (|S_P|le11-|P|) was invalid and has been withdrawn. The replacement in DELTA14_SATURATED_CANDIDATE_EXTENSION_EXCLUSION.md uses valid independent-set and incidence-count arguments. Under the explicit local model, it excludes (epsilon_U=0,1,2); the separate kernel-classification theorem identifies every admissible saturated kernel (J) with that model, conditional on the alpha-critical reduction and its unverified external Didin-preprint dependency. Thus the general (delta=14), non-four-partite, (K_5)-saturated terminal is now conditionally closed.

**Next target:** (delta=13,epsilon_U=1), (2K_4dotcup2K_5) with two W-cross-edges, retaining the exact Type-I/Type-II blocker contract in DELTA13_EPS1_TWO_CROSS_EDGE_PROFILE_REDUCTION.md. Then handle the remaining (delta=13) profiles, (delta=13,epsilon_U=0), non-four-partite U-complements, and (deltale12). The five shell templates and (K_{145})-to-T61 bridge remain OPEN / NOT_CERTIFIED.


## Round 30 update — one more delta-13 placement excluded

DELTA13_EPS1_TWO_CROSS_EDGE_K4K5_DISJOINT_CLOSED.md excludes the same-pair disjoint K4–K5 placement. The two-edge blocker classification leaves only four same-pair placements open: K4–K4 matching, K4–K4 star, K4–K5 star centred in K4, and K4–K5 star centred in K5. The latter may support degree-six Type-II exceptions and remains open. All other branches listed in Round 29 remain OPEN / NOT_CERTIFIED.


## Round 31 — complete closure of the delta-13, epsilon_U=1, two-cross-edge profile

Added DELTA13_EPS1_TWO_CROSS_EDGE_TERMINAL_CLOSURE.md and verify_delta13_eps1_two_cross_edge_terminal_closure.py.

- The common component-capacity theorem gives \(\sum_i|S_i|\le24\) whenever a W-cross-edge meets a K4, hence at least five W-unsaturated U-vertices.
- The exact Type-I/Type-II transversal-blocker classification excludes the disjoint K4-K5 placement (already recorded in Round 30), and the new proof closes the four remaining same-pair placements.
- For K4-K4 matching/star, a zero-excess small-part exception and a D-part vertex of W-degree four yield an independent 5-set.
- For K4-K5 stars, at least six D-vertices have \(t_d=1,\epsilon_d=0\). A reverse-saturation argument forces some D-vertex to have W-neighbourhood exactly the incident K4; it need not be one of the \(t_d=1,\epsilon_d=0\) vertices. Pairing it with a zero-excess Type-II exception gives an independent 5-set.
- The arithmetic verifier checks all eight integer capacity profiles, the ledger, and the D-part \(t\)-vector lower bound. It does not certify the analytic blocker, reverse-saturation, or independent-set arguments.
- Remaining front-end gaps include the \(\delta=13,\epsilon_U=2\) one-cross-edge profile, \(\epsilon_U=0\), non-four-partite \(L\), \(\delta\le12\), the five shell templates globally, and the original \(K_{145}\)-to-T61 bridge. E407 Q32 and EG617(\(r=12\)) remain OPEN / NOT_CERTIFIED.
