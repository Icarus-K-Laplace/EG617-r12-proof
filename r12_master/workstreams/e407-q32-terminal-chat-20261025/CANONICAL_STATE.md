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
- unified witness capacity: c6461a4ef3f3ff3624e23334c17ade3cd56bf470
- Astra dlow terminal: c71b29d3c5b661cdcf00404e545933893c44598b
- Astra aext near-anchor: ad6e4ebe152e3918b9c5fe67f461ba402b1445d8
- base main at branch creation: 3f42fcce5761ca2372140618adda56f95fcbe253
These are the latest heads observed in the repository at the time of this update; they are provenance references, not merged dependencies.
## Established under retained contracts
- The E407 Q32 boundary has 49 linear independent 4-set witnesses on a 29-point support, with \(e(H)=284\), \(\alpha(H)\le4\), \(\delta(H)\ge12\), and total core excess 4.
- The exact ledger gives \(3\le\delta\le16\), \(\delta+\epsilon_U\le16\), and the sibling transversal/excess lemma gives \(\epsilon_U+2\delta\ge9\).
- The \(\delta=16\) four-partite branch is **EXCLUDED**. The 4+1 and 3+2 endpoint splits violate the excess budget; the 5+0 split forces its endpoint \(K_4\) to be complete to the 8-part, creating a forbidden \(K_{12}\). See FOUR_PARTITE_TERMINAL.md and DELTA16_K12_CLIQUE_OBSTRUCTION.md for the standalone one-exception proof.
- The \(\delta=15\) four-partite branch is **EXCLUDED** in DELTA15_FOUR_PARTITE_TERMINAL.md: after eliminating three W-profiles, the last \(K_3\cup K_5^3\) profile forces \(k_A=k_B=k_C=5\), so any cross-edge endpoint has a forbidden \(K_{12}\) neighbourhood.
- The \(\delta=15\) non-four-partite branch is **excluded** under the retained core/witness contract: Kang–Pikhurko equality reduces it to a balanced \((7,7,7,7)\) base, and the exceptional vertices \(x,y\) have incompatible required degrees into \(W\). The full reduction and contradiction are in DELTA15_SECOND_TURAN_PACKING.md.
- The final \(\delta=15\) contradiction compares \(d_H(x,W)=a-1+\epsilon_x\) and \(d_H(y,W)=6-a+\epsilon_y\). Whole-part saturation in \(W\) forces incompatible lower bounds on \(a\), for both \(\epsilon_U=0\) and \(\epsilon_U=1\).
- In that case, \(U\)-part sizes are \(7,7,7,8\), \(H[W]=K_5\cup K_5\cup K_4\cup K_4\), and the five cross edges in \(H[U]\) form a matching between the 8-part and the three 7-parts.
- For \(\delta=16\), a reverse-saturation lemma proves every \(w\in W\) is complete to exactly one \(U\)-part; it is used in the endpoint-split proof.
- New exact witness-array identity: for each D-vertex d, its number of missing small-part partners equals the number of exact-129 color classes omitting d. These multiplicities sum to 7; the five endpoint D-labels contribute at least 5, so at least three have multiplicity exactly 1 and at least one non-endpoint D-label has multiplicity 0. See DELTA16_WITNESS_ARRAY.md.
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
| \(\delta=14\) four-partite | ε_U=0: three W-profiles excluded; one cross-edge profile remains; ε_U=1,2 open |
| \(\delta\le14\) non-four-partite | OPEN |
| E407 Q32 overall | OPEN / NOT_CERTIFIED |
| EG617(r=12) | OPEN / NOT_CERTIFIED |
## Verification status
The local arithmetic verifier checks exact ledgers and the finite excess inequalities only. The analytic endpoint-split proof in FOUR_PARTITE_TERMINAL.md excludes the full \(\delta=16\) branch under the retained core/witness contract; this verifier is not a graph-realization certificate.
## New Round 9 result — delta=14, epsilon_U=0 cover-capacity exclusion
- Added DELTA14_EPS0_K3K4K5K6_COVER_CAPACITY.md: the no-cross-edge \(H[W]=K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6\) profile is excluded by a common-neighbour cover bound. Defining \(S_s\) as the U-vertices complete to \(C_s\), the four components must cover all 29 U-vertices, but exact extra-edge/excess accounting gives \(\sum_s|S_s|\le28\).
- Together with DELTA14_EPS0_K4_PROFILE_EXCLUSIONS.md, this excludes three of the four \(\delta=14,\epsilon_U=0\) W profiles. The sole remaining profile in that row is \(K_3\cup K_5^3\) plus one W-cross-edge.
- Arithmetic replay: verify_delta14_eps0_cover_capacity.py; all 35 excess partitions with \(E_3+E_4+E_5+E_6=4\) give a cover upper bound at most 28.
- Remaining: \(\delta=14,\epsilon_U=0\) one-cross-edge profile; \(\epsilon_U=1,2\); \(\delta=14\) non-four-partite; \(\delta\le13\). E407 Q32 and EG617 remain OPEN / NOT_CERTIFIED.
