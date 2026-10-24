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

The imported theorem states that for two outer-row blocker neighborhoods X,Y of one exact-129 color, if k is the number of isolated K5 components fully covered by X union Y, then
\[
\alpha(C[U_C\setminus(X\cup Y)])\le k.
\]
It also proves the exact r_i(C)=1 profile: ten distinct K5-component blockers plus two six-point subsets of the 11-point gadget whose union is the gadget and whose intersection has size one.

This workstream extends that theorem for r_i(C)<=3 in SEVEN_BLOCK_INCIDENCE_LEDGER.md. It does not edit the source branch. The new consequence is: all ten K5 components are represented in exactly one row neighborhood, exactly two rows contain no full component, and each component row has size at most seven. Between any two blocks with r_i(C)<=3, the ten same-component representatives are forced C-edges, forming a matching. These are baseline-compatible edges; the result does not itself force positive d_ij(C).

## 7. Scope caution

A forced same-component edge across two outer blocks is not automatically a duplicate-color edge. It can be one of the baseline 12 edges of color C between those blocks. The new theorem is a structural compatibility constraint, not a contradiction and not a claim that the global seven-block system is UNSAT.
