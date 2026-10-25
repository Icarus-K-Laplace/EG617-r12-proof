# E407 Q32 — five-template / common-core compatibility

Date: 2026-10-25  
Status: **OPEN**. The five \(\rho=0\) templates have not been eliminated.

## 1. Frozen common-core contract

All five V12 templates A–E are tested against the same hypothetical 47-vertex core \(H\):
\[
e(H)=284,\quad \delta(H)\ge12,\quad \alpha(H)\le4,\quad
\sum_{x\in H}(d_H(x)-12)=4.
\]
The seven exact-129 colors in the residual edge profile \(129^7,130^4\) give 49 linear independent 4-sets \(Q\), seven per exact-129 color. The witness support boundary under review is \(|U|=29, |W|=18\). The exact ledger is
\[
e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,\quad
e(H[W])=48-\epsilon_U-\delta.
\]
The independently checked transversal/excess inequality is
\[
\epsilon_U+2\delta\ge9,\quad \delta+\epsilon_U\le16,
\]
so \(\delta\ge3\). This is conditional on the retained T61 reduction and exact-129 Kang–Pikhurko equality contract.

## 2. What the latest sibling work actually supplies

The emergency-sprint branch at f4c3b06891d29238d4f9cca2588f442004b6dc97 proves the stronger E407 transversal/excess bound \(\epsilon_U+2\delta\ge9\), hence \(\delta\ge3\), without assuming four-partiteness.

The ultimate-closure branch at 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 contains the exact-129 color-factor crosscut. Under its template contracts, it gives:
- A/B: at least 28 hub-complete independent 4-sets across the seven exact-129 colors;
- C/D: at least 35 hub-complete independent 4-sets;
- E with at least one full B-row: at least 35 hub-complete sets;
- E with no full B-row: at least 42 independent 4-sets hitting both endpoints of the \(P_3\).

The witness-packing branch at f5d3daa07403877ede9885e1bd5c2f46b16d81da confirms the union-size boundary and explicitly warns that the high-multiplicity witness-star dichotomy is not proved by its stated second-Turán step. This workstream does not use that unsupported dichotomy.

## 3. New common-core restriction

The \(\delta=16\) four-partite boundary is **EXCLUDED** by FOUR_PARTITE_TERMINAL.md:
- \(U\)-parts are \(7,7,7,8\);
- the five cross edges in \(H[U]\) form a matching;
- \(H[W]=K_5\cup K_5\cup K_4\cup K_4\);
- the \((4,1)\) and \((3,2)\) endpoint splits violate the four-unit excess budget;
- in the \((5,0)\) split, the endpoint \(K_4\) is forced complete to \(D\), producing a forbidden \(K_{12}\).

This closes only \(\delta=16\), not E407 Q32 overall. The \(\delta=15\) non-four-partite branch is also excluded under the retained core/witness contract by DELTA15_SECOND_TURAN_PACKING.md.

The entire \(\delta=15\) four-partite branch is now EXCLUDED by DELTA15_FOUR_PARTITE_TERMINAL.md: the final \(K_3\cup K_5^3\) profile forces all three small-part label counts to equal five, so any cross-edge endpoint has a forbidden \(K_{12}\) neighbourhood.


## 3A. Delta-14 cover-capacity result
The proofs DELTA14_EPS0_K4_PROFILE_EXCLUSIONS.md, DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md, and DELTA14_EPS0_K3K5K5K5_CROSS_EDGE_CLOSURE.md now exclude all four W profiles in the \(\delta=14,\epsilon_U=0\), four-partite row. The last profile \(K_3\cup K_5^3\) with one W-cross-edge is excluded by a common-neighbour capacity bound of 27, below \(|U|=29\). This remains a common-core structural result; it does not close any of templates A–E.

## 4. Template-by-template status

| Template | Existing witness consequence | New result in this line | Status |
|---|---|---|---|
| A | \(\ge28\) hub-complete \(Q\)'s | \(\delta=16\) excluded; lower-\(\delta\) cases open | OPEN |
| B | \(\ge28\) hub-complete \(Q\)'s | \(\delta=16\) excluded; lower-\(\delta\) cases open | OPEN |
| C | \(\ge35\) hub-complete \(Q\)'s | \(\delta=16\) excluded; lower-\(\delta\) cases open | OPEN |
| D | \(\ge35\) hub-complete \(Q\)'s | \(\delta=16\) excluded; lower-\(\delta\) cases open | OPEN |
| E, at least one full row | \(\ge35\) hub-complete \(Q\)'s | \(\delta=16\) excluded; lower-\(\delta\) cases open | OPEN |
| E, no full row | \(\ge42\) witnesses hitting both \(P_3\) endpoints | \(\delta=16\) excluded; endpoint-row compatibility for lower \(\delta\) remains open | OPEN |

## 5. What is not claimed

- No one of the five templates is closed by this theorem.
- The \(\delta=15\) non-four-partite case is **excluded**: the Kang–Pikhurko equality reduction and incompatible (x,y) degrees into (W) rule out all three base profiles.
- At \(\delta=14,\epsilon_U=0,1,2\), all four-partite W profiles are excluded. The \(\epsilon_U=1\) list is exhaustive by DELTA14_EPS1_W_PROFILE_CLASSIFICATION.md and Brouwer's second-Turán bound; the \(\epsilon_U=2\) profile is forced by Turán equality and excluded by DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md, Section 5. The \(\delta=14\) non-four-partite branch remains open. The \(\delta=15\) four-partite branch is excluded.
- The \(\delta\le14\) non-four-partite cases remain open.
- No proof is claimed that the residual incidence design can or cannot be realized.
- E408 Q32/Q33 and the original \(K_{145}\)-to-T61 bridge are outside this line's closure claim.


## 3B. Delta-14, \(\epsilon_U=1\) profile

DELTA14_EPS1_K3K5K5K5_NO_CROSS_EDGE.md excludes the no-cross-edge \(K_3\cup K_5^3\) profile at \(e(H[W])=33\) by a cover bound of 28. This is one profile only; the \((4,4,4,6)\) and \((4,4,5,5)\)+one-cross-edge profiles remain open at this row.


## 3C. Delta-14, \(\epsilon_U=1\), second no-cross-edge profile

DELTA14_EPS1_K4K4K4K6_NO_CROSS_EDGE.md excludes \(H[W]=K_4^3\cup K_6\). Its key invariant is the exact number \(R\) of D-to-W edges outside each D vertex's assigned W-component:
\(R=1-2q+\sum_{d\in D}\epsilon_d\), where \(q\) is the number of D vertices assigned to \(K_6\). This forces every \(K_4\) to receive at most two D assignments, contradicting the need to assign seven or eight D vertices among three \(K_4\) components.


## 3D. Delta-14, \(\epsilon_U=1\), exact W-profile closure

The exact W-profile classification is in DELTA14_EPS1_W_PROFILE_CLASSIFICATION.md. Its three possibilities are all excluded by the no-cross-edge \(K_3\cup K_5^3\) theorem, the no-cross-edge \(K_4^3\cup K_6\) theorem, and DELTA14_EPS1_K4K4K5K5_ONE_CROSS_EDGE.md. This closes the full four-partite \(\epsilon_U=1\) row under the retained contracts and Brouwer's second-Turán theorem.


## 3E. Delta-14, \(\epsilon_U=2\), unique W profile

At \(\epsilon_U=2\), the exact edge ledger gives \(e(H[W])=32\), the minimum allowed by \(\alpha(H[W])\le4\). Turán equality forces \(H[W]=K_4\cup K_4\cup K_5\cup K_5\), with no cross-edge. Section 5 of DELTA14_EPSU1_2_ANTICOMPL_COMPONENT_PROFILES.md excludes this profile by the common-neighbour cover bound 24<29. The mention of \(K_3\cup K_5^3\) for \(\epsilon_U=2\) in that note's Section 3 is not an admissible profile here because it has 33 rather than 32 edges.


## 3F. Round 15 — non-four-partite \(\delta=14\) augmentation fork

The new theorem DELTA14_NONPARTITE_AUGMENTABLE_EDGE_REDUCTION.md splits the non-four-partite \(\delta=14\) case into two explicit routes:
1. If \(L\) has an augmentable nonedge, it reduces to the unique \(\epsilon_U=1\), \(K_3\cup K_5^3\) balanced-KP terminal, with \(x,y\) both complete to the \(K_3\) and the added edge disjoint from \(\{x,y\}\).
2. If \(L\) has no augmentable nonedge, then \(L\) is \(K_5\)-saturated; this branch is not covered by the equality classification and remains open.

This is not a template closure. All five shell templates A–E remain OPEN, and the reduction remains conditional on the retained T61/49-witness contract.


## 3G. Round 16 — augmentable-edge subcase excluded

DELTA14_NONPARTITE_AUGMENTABLE_TERMINAL_CLOSURE.md closes the augmentable-edge route of the non-four-partite \(\delta=14\) branch. The sole terminal from Round 15 is eliminated by a four-component common-neighbour capacity proof. The only remaining non-four-partite \(\delta=14\) possibility is a \(K_5\)-saturated \(L\). No shell template A–E is thereby closed, and the \(\delta\le13\) branch remains open.


## Round 23 — delta-13 no-cross-edge W profiles

Under the four-partite-U branch of the shared 49-witness contract, all no-cross-edge W profiles at \(\delta=13\) with \(\epsilon_U=1,2,3\) are now excluded. The exact profiles are \(K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6\), \(K_3\dot\cup3K_5\), \(3K_4\dot\cup K_6\), and \(2K_4\dot\cup2K_5\). Their common-neighbour capacities sum to at most 27, 28, 28, and 23, respectively, below \(|U|=29\). See DELTA13_FOUR_PARTITE_NO_CROSS_W_PROFILES.md.

This does not exclude any W-cross-edge profile, \(\epsilon_U=0\), non-four-partite U-complement at \(\delta=13\), or \(\delta\le12\). Templates A–E remain OPEN because the residual shell-label compatibility has not been eliminated.


## Round 24 — delta-13 \(\epsilon_U=1\), \(K_3\cup3K_5\) plus one edge

The \(K_3\dot\cup3K_5\) W-profile with one cross-edge is now excluded for \(\delta=13,\epsilon_U=1\), under the four-partite-U contract. If the edge joins two K5s, no U-vertex can be W-unsaturated. If it joins K3 to K5, the only possible unsaturated U-vertex has \(d_H(u,W)=7\), \(\epsilon_u=1\), and \(t_u=0\); there can be at most one such vertex. The component common-neighbour capacity is at most 26, below the required 28.

Still open at \(\delta=13\) in the four-partite-U branch: \(3K_4\dot\cup K_6\) plus one edge and \(2K_4\dot\cup2K_5\) plus two edges for \(\epsilon_U=1\), and \(2K_4\dot\cup2K_5\) plus one edge for \(\epsilon_U=2\), as well as the \(\epsilon_U=0\) row. All five shell templates A–E remain OPEN.


## Round 25 — delta-13 \(3K_4\dot\cup K_6\), cross-edge K4–K6

The \(\delta=13,\epsilon_U=1\) W-profile \(3K_4\dot\cup K_6\) plus one cross-edge is now excluded when that edge joins \(K_4\) to \(K_6\). The four common-neighbour sets have capacities at most \(9,9,9,1\), totalling 28, while all 29 U-vertices must be W-saturated. See DELTA13_EPS1_3K4_K6_K4K6_EDGE.md.

Still open: the same profile with its edge between two K4s; \(2K_4\dot\cup2K_5\) plus two edges at \(\epsilon_U=1\); \(2K_4\dot\cup2K_5\) plus one edge at \(\epsilon_U=2\); and all other \(\delta=13\) and lower branches. Templates A–E remain OPEN.


## Round 26 — delta-13 \(3K_4\dot\cup K_6\) plus one cross-edge, both placements

The K4–K4 placement is excluded by DELTA13_EPS1_3K4_K6_K4K4_EDGE.md. The only possible unsaturated U vertex has degree seven into W, excess one, and no U-cross-edge; all other U vertices are saturated. A common-neighbour cover of at least 28 vertices would require total capacity 28. If all three K4 capacities equal nine, each must have a common small-part label; the exceptional vertex's part cannot be one of these labels, so two components share one of the other two labels and overlap on a seven-vertex part. This contradicts coverage. Together with Round 25, both cross-edge placements for this W-profile are excluded.

Still open at \(\delta=13\) in the four-partite-U branch: \(2K_4\dot\cup2K_5\) plus two edges at \(\epsilon_U=1\), \(2K_4\dot\cup2K_5\) plus one edge at \(\epsilon_U=2\), the \(\epsilon_U=0\) row, non-four-partite U-complements, and \(\delta\le12\). Templates A–E remain OPEN.
