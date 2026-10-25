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


## 12. Outer exact-129 cap proofs — NOT CERTIFIED

The former sections 12–15 claimed a \(P_C=50,r_i=6\) exclusion, a universal \(P_C\le49\) cap, a \(P_C=49\) exclusion, and a \(P_C=48\) exclusion. Cross-branch audit found that the key isolation lemma is false: a monochromatic \(K_{12}\) can have one external edge of its own color. The valid condition is only \(d_C(z,K_{12})\le1\) for each outside vertex \(z\). Therefore any subcase whose sole contradiction is one external \(C\)-edge is not valid.

These four outer-cap claims are **NOT CERTIFIED** and must not be used as dependencies. The detailed P49/P48 drafts remain available but are marked audit hold; their previous text is preserved in ARCHIVE_UNCERTIFIED_OUTER_CAPS_20261025.md. A repaired proof must force at least two external \(C\)-edges from the same outside vertex or give another independent contradiction. The local row-normal-form results through Theorem 12 remain separate from this withdrawn global inference.

## 2026-10-25 audit correction and new inner-core result

### Outer star correction — mandatory dependency firewall

For a monochromatic \(K_{12}\) of color \(C\) in a balanced 12-coloring, any outside vertex \(z\) has twelve edges to the clique. These edges must include each of the eleven colors other than \(C\), hence
\[
d_C(z,K_{12})\le1.
\]
The conclusion \(d_C(z,K_{12})=0\) is invalid: one external \(C\)-edge is allowed. Therefore the former proofs of the \(P_C\le49\) and \(P_C\le48\) caps remain **NOT CERTIFIED**, and the former single-edge proof of the \(P_C=50,r_i=6\) corner is withdrawn. That specific \(P_C=50,r_i=6\) corner is now excluded independently by R12_P50_R6_DOUBLE_STAR_EXCLUSION.md, using a verifier that forces \(d_C(z,K_{12})\ge2\). A read-only sibling theorem also excludes the local \(P_C=49,r_i=6\) corner via a double-star. These local corner exclusions do not imply a universal cap. The historical attempts are preserved in ARCHIVE_UNCERTIFIED_OUTER_CAPS_20261025.md; the P49/P48 drafts remain on audit hold. Do not cite those caps as dependencies.

The exact-129 row-normal-form results through Theorem 12 and the finite gadget alignment certificate are separate local claims. Their own incidence assumptions still need to be respected, but they do not imply the withdrawn isolation statement.

### New conditional inner-core theorem

R12_E408_Q33_S0_12_EXCLUSION.md excludes \(S_0=12\) in the 31-point/56-witness E408 Q33 minimum-support boundary. It assumes the previously established conditional theorem \(S_0\ge12\) and its unique seven-point transversal structure, then uses the row identity
\[
s_r=3+g_r-a_r
\]
to enumerate the 14 possible outside-degree profiles. Each profile is contradicted by the multiplicity of the three R-only 8-transversals, the special-incidence budget, or a \(K_{12}\) **inside \(H\)**. These are valid contradictions to \(\omega(H)\le11\) and do not use the invalid outer isolation lemma.

The arithmetic verifier verify_s0_12_exclusion.py checks:
- all 14 degree profiles under \(\sum_Wq_w=126\), \(0\le\epsilon_T\le4\), and the zero-excess \(T\)-degree constraints;
- the row-sum identity \(8m=84-\epsilon_T-A\);
- all multiplicity partitions of \(m=8,9,10\) into three positive parts of size at most four;
- the incidence thresholds for multiplicity-one/two/four parts and the uncovered-point bounds.

The verifier checks arithmetic only. The graph-theoretic lemmas and upstream T61/exact-129/witness-packing contracts remain proof dependencies. The new conclusion is
\[
S_0\ge13,\qquad \delta\ge5,
\]
while the four-partite subcase retains its separate stronger bound \(S_0\ge22\). This does not close E408 Q33, E407 Q32, E408 Q32, or EG617(\(r=12\)).


### Repaired local double-star corner

The \(P_C=50,r_i=6\) corner has a new conditional proof in R12_P50_R6_DOUBLE_STAR_EXCLUSION.md. Its reduction is \(R_C=12\), so the other six block budgets are all one. It selects one no-component row from each block and uses the exact gadget alignment predicate to form a \(K_{12}\) with an outside gadget vertex having at least two \(C\)-edges into the clique. The dedicated verifier checks 49,212 gadget configurations (204 Case A/B and 49,008 Case C), with zero failures in the independent in-session replay. The graph-level proof still depends on the stated row classifications and exact-129 factor theorem.

The sibling result for \(P_C=49,r_i=6\) is in workstream/r12-unified-witness-capacity-20261025, OUTER_EXCEPTIONAL_ROW_COUPLING.md §12; verifier blob SHA 23cd4ef874faadbd5931c5e3553a1a55415c7a79. It remains a local corner exclusion and does not itself establish a universal cap.

### Additional \(P_C=50\) high-profile exclusions

R12_P50_REMAINING_HIGH_PROFILES_EXCLUSION.md and verify_p50_remaining_high_profiles.py exclude the profiles \((5,2,1^5)\) and \((4,3,1^5)\). The proof selects one no-component row from each of the two non-\(r=1\) blocks and one from each of the five \(r=1\) blocks. A finite gadget alignment yields a \(K_{12}\) and an external vertex with at least two \(C\)-edges into it. The only incidence-sensitive subcases are when both non-\(r=1\) blocks have complement profile \((5,5)\); the verifier exhausts all allowed partial-component allocations and finds an aligned pair with at most four partial component incidences. The independent replay passed 1,656,848 base configurations, zero failures.

### Common-star theorem and arithmetic correction

The correct seven positive integer profiles summing to \(R_C=12\) are
\[
(6,1^6),\ (5,2,1^5),\ (4,3,1^5),\ (4,2,2,1^4),\
(3,3,2,1^4),\ (3,2,2,2,1^3),\ (2^5,1^2).
\]
Earlier progress notes mistakenly listed \((4,2,2,2,1^3)\) and \((3,2,2,2,2,1^2)\); both sum to 13, not 12. The canonical state, high-profile theorem, and active ledger have been corrected.

R12_HIGH_P_COLOR_CAP_COMMON_STAR.md and verify_high_p_common_star.py establish a finite common-\((D,w)\) property for every allowed row-complement pair tuple with seven budgets \(1\le r_i\le5\) and total \(\sum_i r_i\le12\). The checker covers 18 budget profiles, four gadget normal forms, 72 profile/form cases, and 2,405,684 DP transitions; no empty common-candidate intersection occurs.

If every pair of selected no-component rows has partial component incidence sum at most four, the common point \(w\) forces pairwise \(C\)-adjacency, and the seven rows plus \(D\) form a monochromatic \(K_{12}\). Seven proper omitted subsets of the six-point set \(U_C\setminus D\) then force an outside vertex with at least two \(C\)-edges into that clique, contradicting the valid star-capacity lemma.

- If \(P_C\ge51\), then \(R_C\le11\) and every pair satisfies \(r_i+r_j\le6\), so the common-star argument excludes the profile.
- If \(P_C=50\) and \(\max_i r_i\le4\), the four profiles \((4,2,2,1^4)\), \((3,3,2,1^4)\), \((3,2,2,2,1^3)\), and \((2^5,1^2)\) satisfy the same pairwise budget condition and are excluded.
- The other three \(P_C=50\) profiles are excluded by the \(r_i=6\) double-star theorem and the two high-profile double-star theorems.

Therefore the conditional colorwise cap
\[
\boxed{P_C\le49\quad\text{for every exact-129 color }C}
\]
is now established under the retained exact-129 factor, row-profile, pairwise-blocker, gadget-normal-form, and seven-block equality contracts. The stronger cap \(P_C\le48\) remains **NOT CERTIFIED**. E408 Q33 and EG617(\(r=12\)) remain **OPEN / NOT_CERTIFIED**.

Verifier commit: c413b1065e9926d00ad1319f2e8d8a815e4850b5. Theorem commit: 04b5ec6f9a1e118faee2216208e1f13361fb8d43.

## 13. \(P_C=49\) common-star screen — partial closure only

The new files R12_P49_COMMON_STAR_SCREEN.md and verify_p49_common_star_screen.py extend the finite common-star DP to the exact boundary \(R_C=13\). An independent in-session reimplementation reproduced the committed verifier's arithmetic for the \(R_C\le12\) theorem and then checked all nine profiles with \(R_C=13\) and \(\max r_i\le5\) across four gadget normal forms.

Five profiles are excluded conditionally:
\[
(2^6,1),\ (3,2^4,1^2),\ (3^2,2^2,1^3),\ (3^3,1^4),\ (4,2^3,1^3).
\]
Their pairwise budget sums are at most six, so the selected no-component rows have component-incidence sum at most four. The common-star alignment yields a monochromatic \(K_{12}\), and seven nonempty omission sets in a six-point set force a vertex with at least two external \(C\)-edges, contradicting the valid star-capacity bound.

The common-star DP fails for \((4,4,1^5)\) in gadget forms \(b=1,4\) and for \((4,3,2,1^4)\) in forms \(b=2,3\). The remaining six \(P_C=49\) profiles are:
\[
(4,3,2,1^4),\ (4,4,1^5),\ (5,2^2,1^4),\ (5,3,1^5),\ (6,2,1^5),\ (7,1^6).
\]
The first two require an alignment method without a common point; the next two require incidence-sensitive row selection; the last two require separate high-budget case analysis.

**Scope firewall:** this is a partial exclusion of five integer profiles, not a proof that \(P_C\ne49\). The historical P49_BOUNDARY_EXCLUSION.md remains NOT CERTIFIED as a whole. No conclusion \(P_C\le48\) is authorized; E408 Q33 and EG617(\(r=12\)) remain OPEN / NOT_CERTIFIED.


## 14. Incidence-sensitive closure of \((5,2^2,1^4)\) and \((5,3,1^5)\) at \(P_C=49\)

The theorem note R12_P49_INCIDENCE_SENSITIVE_SCREEN.md and verifier verify_p49_incidence_sensitive.py refine the common-star screen by retaining the partial component-incidence count \(p\) attached to each of the two no-component rows in a block. The exact row identity gives \(p_H+p_J\le r-a\), where \(a=11-|H|-|J|\). The checker enumerates all nonnegative allocations within this bound, so it covers every actual row system under the registered row theorem.

For profile \((5,2^2,1^4)\), the threshold mode \(p_5\le3,p_2\le1,p_1=0\) is sufficient. The verifier checks all four gadget normal forms, 503,748 transitions in total, with no empty common-star state.

For profile \((5,3,1^5)\), the three modes \((p_5,p_3)\in(\le2,\le2),(\le3,\le1),(\le4,0)\), with \(p_1=0\), cover every incidence assignment satisfying \(p_5+p_3\le4\). The multi-mode verifier checks all four gadget forms, 1,417,758 transitions in total, and no reachable state makes all three mode intersections empty.

In each profile a mode supplies a common \(D,w\) star with every selected pair's partial component-incidence sum at most four. The pairwise-blocker lemma makes the selected rows pairwise \(C\)-adjacent; the seven omission sets then force an outside vertex with at least two \(C\)-edges into the resulting \(K_{12}\). This excludes both profiles conditionally.

The P49 boundary is now reduced to four profiles:
\[
(4,3,2,1^4),\ (4,4,1^5),\ (6,2,1^5),\ (7,1^6).
\]
This does not close \(P_C=49\), and no \(P_C\le48\) claim is authorized. E408 Q33 and EG617(\(r=12\)) remain OPEN / NOT_CERTIFIED.
