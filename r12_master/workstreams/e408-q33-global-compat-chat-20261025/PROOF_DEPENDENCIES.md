# Proof dependencies and contract firewall

Updated: 2026-10-25  
Workstream branch: workstream/r12-e408-q33-global-compat-20261025

## 1. Source branches read before this line was started

The following sibling workstreams were treated as read-only inputs. No sibling files were edited.

| Workstream | Branch head read | Relevant files / conclusion |
|---|---|---|
| Emergency r=12 sprint | f4c3b06891d29238d4f9cca2588f442004b6dc97 | emergency canonical state; E407 Q32 and E408 Q32/Q33 remain OPEN |
| Emergency sprint chat | 5258c5fe17af3bf17eb7a2bfb08315c9be9116cd | R12 E407/E408 compatibility; corrects the distinction between 284-edge Q33/E407 cores and the 285-edge Q32 core |
| Ultimate closure | 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 | shell/core witness lemma and witness-capacity cross-cut |
| Witness packing | f5d3daa07403877ede9885e1bd5c2f46b16d81da | universal Q33 boundary theorems S0>=11 and S0>=12; seven Q-sets but only six guaranteed B-labelled per exact-129 color |
| Zero-excess witness | 07d19abfd6c1c749c7360526e4a04a3eb865fb2e | zero-excess witness theorem and overlap-capacity identity; scalar-only closure explicitly remains insufficient |

## 2. Exact file dependencies and their scope

- Emergency canonical state, file blob SHA 0a15e83eef91937cbf1df6e303a6bec095278adc: root theorem remains NOT_CERTIFIED; the T61 reduction is a separate dependency.
- E407/E408 compatibility audit, file blob SHA 8142b72ebcedce235e443316568428bc23ce94ad: E407 Q32 and E408 Q33 have e(H)=284 and total core excess 4; E408 Q32 has e(H)=285 and excess 6. No Q32 result is imported into Q33.
- Universal Q33 S0>=12 theorem, file blob SHA 291d8bec834d6876ce6c5b952734d136a9d1a4d6: conditional on the T61, exact-129 factor, and 31-point/56-witness boundary contracts. It removes S0=11 but does not exclude S0>=12.
- Universal Q33 S0>=11 theorem, file blob SHA 44ebddfffefcf8924d73b1eb4b5658a50e1ac6eb: prior lower boundary; used only as context for the stronger S0>=12 result.
- Zero-excess witness theorem, file blob SHA 557936d1396424b7034654621b39d1f9e65141aa: graph lemma is analytic; applications to exact-129 factors are conditional.
- Witness overlap-capacity identity, file blob SHA 6fa6f5bd04d96d880a6fc991c525559f8e32c511: the edge-load identity is a necessary inequality, and its scalar upper bound is explicitly shown insufficient.
- Shell/core witness lemma, file blob SHA 02b4c867a2bd2264fb45c51d2ab77cc57c488b0b: applies only under the retained T61 contextual contract.
- Outer seven-block system, source file front_end/E408_GLOBAL_SEVEN_BLOCK_EQUALITY_SYSTEM.md on the emergency sprint branch: exact global color edge counts, one-or-two row rule, and 62-unit duplicate budget.

The new theorem in FOUR_PARTITE_GLOBAL_COMPATIBILITY.md is proved directly from the 31-point/56-witness four-partite contract, the partition of the eight witnesses through each d in D, the core degree ledger, and alpha(H)<=4 / omega(H)<=11. It does not use the star lemma noted below.

## 3. Proof correction discovered during the audit

The earlier sibling file r12_master/workstreams/emergency-sprint-chat-20261024/R12_WITNESS_OVERLAP_STAR_LEMMA.md states, for a ten-witness star on 30 vertices, that
\[
e(H[U])=135\quad\text{or}\quad e(H[U])\ge144.
\]
Its argument is not sufficient for that dichotomy. It applies the second-Turán bound to \(L=\overline{H[U]}\) and then says that because \(L\) has at least 292 edges it “must be complete tripartite.” The second-Turán bound only forces \(L\) to be tripartite in that edge range; a tripartite graph may have missing cross-part edges and need not be complete tripartite. Thus the stated dichotomy does not follow from the argument as written.

This workstream does not use that dichotomy. It is recorded here so downstream proofs do not silently treat the 135-or-144 claim as certified. No sibling file was modified.

## 4. Scope and assumptions that remain conditional

The following are not promoted to unconditional theorems here:

1. The original \(K_{145}\) counterexample-to-T61 reduction and its lower-order seed dependencies.
2. The exact-129 factor theorem on the 61-point residual.
3. The 31-point union / 56-witness minimum-support boundary.
4. The outer seven-block near-Latin embedding for E408 equality.
5. Any finite shell screen that only proves local necessary conditions.

The exact 284-edge contract applies to E407 Q32 and E408 Q33. E408 Q32 has a 285-edge core and is excluded from this workstream.

## 5. Current result status

- **PROVED_CONDITIONAL:** under the four-partite Q33 boundary contract, \(S_0\ge22\), hence \(\delta\ge9\).
- **PROVED_CONDITIONAL:** exact outer duplicate ledger and its labeled blocker consequences, as in SEVEN_BLOCK_INCIDENCE_LEDGER.md.
- **OPEN:** non-four-partite L terminal, four-partite terminal with \(S_0\ge22\), and their joint compatibility with the outer seven-block system.
- **NOT_CERTIFIED:** the full E408 Q33 exclusion and the original EG617(r=12) theorem.


## 6. Newly integrated pairwise-blocker theorem

Read-only source: branch workstream/r12-ultimate-closure-20261024, file r12_master/workstreams/ultimate-closure-chat-20261024/R12_E408_PAIRWISE_BLOCKER_COMPATIBILITY.md, blob SHA b49421769477461ed26b3418a5cfd1a851cbb52d.

The source theorem is stated for two rows in the same target block. Its proof uses only that the two outer vertices are nonadjacent in color C, so it extends to a cross-block pair whenever those two vertices are assumed C-nonadjacent. For two such blocker neighborhoods X,Y of one exact-129 color, if k is the number of isolated K5 components fully covered by X union Y, then
\[
\alpha(C[U_C\setminus(X\cup Y)])\le k.
\]
It also proves the exact r_i(C)=1 profile: ten distinct K5-component blockers plus two six-point subsets of the 11-point gadget whose union is the gadget and whose intersection has size one.

This workstream extends that theorem for r_i(C)<=3 in SEVEN_BLOCK_INCIDENCE_LEDGER.md. It does not edit the source branch. The new consequence is: all ten K5 components are represented in exactly one row neighborhood, exactly two rows contain no full component, and each component row has size at most seven. Between any two blocks with r_i(C)<=3, the ten same-component representatives are forced C-edges, forming a matching. These are baseline-compatible edges; the result does not itself force positive d_ij(C).

## 7. Scope caution

A forced same-component edge across two outer blocks is not automatically a duplicate-color edge. It can be one of the baseline 12 edges of color C between those blocks. The new theorem is a structural compatibility constraint, not a contradiction and not a claim that the global seven-block system is UNSAT.

## 8. Extended low-duplicate blocker theorem

Theorem 10.1 and Corollary 10.2 are proved in SEVEN_BLOCK_INCIDENCE_LEDGER.md under the same exact-129 factor and seven-block equality contracts. The proof uses the one-or-two rule, the individual blocker lower bound, and the pairwise blocker compatibility theorem from ultimate-closure blob `b49421769477461ed26b3418a5cfd1a851cbb52d`.

The extension is valid for \(r_i(C)\le5\), not asserted for \(r_i(C)=6\). At \(r_i=6\), the two no-component rows can in principle split the five vertices of a K5 component between them, so the \(k=0\) step needs a separate boundary analysis. Cross-block matching is proved only when \(r_i(C)+r_j(C)\le6\); its ten edges are not automatically duplicate-budget charges.


## 9. Exact \(r_i(C)=6\) boundary and cross-block interface

Theorem 11.1 and Corollary 11.2 are recorded in SEVEN_BLOCK_INCIDENCE_LEDGER.md and depend only on the frozen exact-129 row contract:
- each of the 61 residual vertices has color-C degree one or two into every target block;
- a row without a full isolated \(K_5\) has at least six gadget vertices;
- each \(K_5\) component is fully contained in at most two rows;
- pairwise blocker compatibility: for two outer vertices assumed nonadjacent in C, the gadget independence number after deleting their two neighborhoods is at most the number of full \(K_5\) components covered by their union.

The proof splits the duplicate budget as \(r_i=d_K+d_U=6\). The number of no-component rows is at most two because the 11-vertex gadget has at most 17 row incidences; zero is impossible because twelve full-component rows would exceed the ten labels plus the single permitted repeated full component. The \(n=1\) case forces \(d_K=5,d_U=1\); the \(n=2\) cases are divided by whether a full \(K_5\) repeats.

Corollary 11.2 additionally uses Theorem 10.1 at \(r_j=1\), which gives exact row neighborhoods \(K_\ell\). At least eight component labels in the \(r_i=6\) block have a single-component row with at most five extra vertices; pairwise blocker compatibility then forces adjacency to the corresponding exact \(K_\ell\) row in the \(r_j=1\) block.

**Scope firewall:** these forced edges are not automatically duplicate-budget contributions. No global incompatibility, terminal exclusion, or original \(K_{145}\) proof is claimed.


## 10. High-\(P_C\) maximum-clique packing corollary

Corollary 11.3 in SEVEN_BLOCK_INCIDENCE_LEDGER.md is a consequence of Theorem 11.1 / Corollary 11.2 and the exact duplicate identity \(R_C=62-P_C\):
- if \(P_C=50\) and some \(r_i=6\), all other six block budgets equal one and at least eight vertex-disjoint \(C\)-colored \(K_{12}\) cliques are forced;
- if \(P_C=49\) and some \(r_i=6\), the other budgets are five ones and one two; intersecting the at-least-eight clean labels with the at-least-nine exact blockers in the \(r=2\) block forces at least seven vertex-disjoint \(K_{12}\) cliques.

Each clique consists of one isolated \(K_5\) component and one outer representative from each block. This is a structural packing consequence, not an exclusion: \(\omega(C)\le12\) allows maximum cliques, and no contradiction with the remaining 870-edge budget has been proved.


## 11. Live sibling refresh (2026-10-25)

The following sibling heads were re-read after the local \(r_i=6\) work; all were read-only:

| Branch | Current head | Relevant update |
|---|---|---|
| workstream/r12-e407-q32-terminal-20261025 | dfdfe9a15b156b29f11579e072879d14bc224aad | E407 Q32 non-four-partite \(\delta=15\) branch excluded under its retained contract; E407 Q32 overall remains OPEN. |
| workstream/r12-emergency-sprint-chat-20261025 | 5258c5fe17af3bf17eb7a2bfb08315c9be9116cd | Reconfirmed the exact-129 blocker theorem and the outer seven-block equality system; Q32/Q33 terminal remains open. |
| workstream/r12-emergency-sprint-20261024 | f4c3b06891d29238d4f9cca2588f442004b6dc97 | The global proof DAG still has E407/E408 as the active T61 window; no original \(K_{145}\) closure. |
| workstream/r12-ultimate-closure-20261024 | 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 | Pairwise blocker compatibility remains the dependency used in Theorems 10.1 and 11.1. |
| workstream/r12-witness-packing-chat-20261025 | f5d3daa07403877ede9885e1bd5c2f46b16d81da | Universal Q33 minimum-support bound \(S_0\ge12\); no global labelled terminal contradiction. |
| workstream/r12-zero-excess-witness-20261025 | 07d19abfd6c1c749c7360526e4a04a3eb865fb2e | The labelled overlap-capacity route remains open; its scalar edge-load bound is explicitly insufficient. |

These updates do not invalidate the new row-budget theorems. The Q33 non-four-partite support interval and the four-partite \(S_0\ge22\) branch both remain open; this workstream's next global obligation is still to combine the outer row/component labels with the 56 inner witness labels without charging baseline edges as duplicates.


## 12. Isolated-\(K_{12}\) budget cap and \(P_C=50\) exclusion

Lemma 13.1 / Lemma 13.2 / Theorem 13.3 in SEVEN_BLOCK_INCIDENCE_LEDGER.md use:
1. The original balanced-coloring contract: for every color \(D\), \(\alpha(D)\le12\).
2. The seven-block one-or-two rule: for each \(x\in B_i\) and \(B_j\), every non-target color occurs at least once on the 12 edges \(xB_j\), and one color occurs twice.
3. The exact-129 row classification in Theorem 11.1 and the gadget normal form in Theorem 12.1.

A monochromatic \(C\)-colored \(K_{12}\) is isolated in \(C\): each outside vertex must see all eleven colors \(D\ne C\) on its twelve edges to the clique, so none of those edges can be \(C\). If \(m\) disjoint such cliques each meet all seven target blocks once, the remaining \(k=12-m\) vertices per target block can only connect in color \(C\) to the remaining \(k\) vertices of another block. Their bipartite graph has minimum degree one and maximum degree two, giving \(d_{ij}(C)\le k\) and \(P_C\le21k\).

For \(P_C=50\), \(R_C=12\) forces the row-budget vector \((6,1,1,1,1,1,1)\). The four cases in Theorem 11.1 each yield at least ten isolated \(C\)-colored \(K_{12}\)'s, so \(P_C\le42\), contradiction. The case split is:
- \(n=1\): 10 label-based plus at least 1 gadget-based \(K_{12}\);
- \(n=2,k=1,m=10\): 9 label-based plus 2 gadget-based;
- \(n=2,k=1,m=11\): at least 8 label-based plus 2 gadget-based;
- \(n=2,k=0\): all 10 component labels clean.

This excludes only the exact \(P_C=50,r_i=6\) corner. The \(P_C=49,r_i=6\) branch and E408 Q33 overall remain open; no upstream dependency is closed by this result.
