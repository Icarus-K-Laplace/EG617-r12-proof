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

Here \(|U|=29\), \(e(H[U])=98\), and \(e(L)=308\). The Turán number is \(t_4(29)=315\); Brouwer's non-four-partite upper bound is \(315-\lfloor29/4\rfloor+1=309\). Thus the edge count alone does **not** rule out a non-four-partite \(L\): 308 lies one below the Brouwer cap. A structural classification of the \(K_5\)-free graphs at this near-extremal boundary, together with the 49 linear independent-4 witnesses and the W-degree ledger, is needed.

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

**Finish the δ=14 non-four-partite fork now isolated by DELTA14_NONPARTITE_AUGMENTABLE_EDGE_REDUCTION.md.** First eliminate the sole augmentable-edge terminal ε_U=1, H[W]=K_3∪ K_5^3 with x,y both complete to K_3; in parallel, prove that a non-four-partite L with the 49-witness packing cannot be K_5-saturated, or classify that saturated case. The edge-augmentation theorem does not cover the saturated branch.

Do not continue adding scalar inequalities unless they reduce one of these two explicit cases or yield a direct witness/core contradiction. Once δ=14 is closed, attack δ≤13 with a fresh exact ledger; do not reuse the δ=14 W-profile table without re-deriving its hypotheses.

Until these branches and the T61 bridge are certified, E407 Q32 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## Round 14 update — current live frontier

All four-partite cases at \(\delta=14\) are now excluded for every allowed \(\epsilon_U\in\{0,1,2\}\). The \(\epsilon_U=2\) case is forced to the unique Turán-equality W profile and excluded by the common-neighbour cap in DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md, Section 5.

The live structural gaps are now only:
1. \(\delta=14\) with \(L=\overline{H[U]}\) non-four-partite;
2. \(\delta\le13\), where the \(\delta=14\) four-partite profile arguments do not transfer unchanged.

E407 Q32, all five shell templates A–E, and EG617(r=12) remain OPEN / NOT_CERTIFIED.
