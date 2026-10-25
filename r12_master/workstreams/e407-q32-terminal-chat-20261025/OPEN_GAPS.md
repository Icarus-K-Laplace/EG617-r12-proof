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
The remaining low-\(\delta\) cases have not been converted into a finite, exhaustive structural classification. The four-partite arguments at \(\delta=14\) must not be silently reused: the U-part sizes, \(e(H[U])\), W-edge budget, and W-side excess all change with \(\delta\).

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

**First close the model-classification gap:** determine whether every 15-vertex, 49-edge, triangle-free, non-bipartite triangle-saturated \(J\) compatible with the two orthogonal near-perfect-matching decompositions must have a degree-4 vertex or be isomorphic to the explicit \((5,5,2,1,2)\) C5-blow-up. Until that is proved, do not promote the candidate-specific transversal result to the entire saturated branch. In parallel, finish the two explicit-candidate extension terminals \(\epsilon_U=1,2\). Then move to \(\delta\le13\) with a fresh exact ledger.

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
