# Q33 284-edge theorem and minimum-degree dependency audit

Date: 2026-10-30. Status: **PROVED** for the abstract theorem and the reconstructed minimum-degree gate.

Reference commit supplied by the task: 2e8160200dcf21431221aa453fb49b952d6d52d0.
Actual Q33 branch head read: bdc2046ea08f12455a37fd412fe2e19514118ada.
The intervening51 commits include source recovery, minimum-degree proof expansion, parent audit and exact replay corrections. The current theorem and source gate were read; historical status labels were not treated as proof.

## Abstract exact284 result

Q33_UNIVERSAL_284_NONEXISTENCE.md assumes only |H|=47, e(H)=284, delta>=12, alpha<=4, omega<=11. Its total excess is four. The private-clique support reduction is valid; any K11/K11 pair already costs six and is impossible. The star, P and D inequalities retain their minima6,4,5. The D proof controls overlapping missing sets at each vertex before summing. No illegal omega(H)<=5 premise is present.

The independent verifier in this directory recomputes those finite ingredients. DIRECT_UNIFORM_PROOF.md covers this theorem with T=4 as one value of T<=6. The exact284 theorem is therefore a consistent independent checkpoint; it is NOT a dependency of either low-edge proof.

## Scope of the minimum-degree gate

MINDEG12_47_SOURCE_COMPLETE_AUDIT.md states the general implication

    J in R(4,47), e(J)<=286 => delta(J)>=12.

Its hypotheses explicitly include EVERY induced D-cap. No Q33 charge, E408 energy, pivot, full-color factorization or selected support appears. Accordingly it may be used for E407/Q31, E407/Q32 and E408/Q32 after those graph-class hypotheses are separately proved.

The longest dependency is delta(R(3,35))>=12. The source text summarizes a121/122-edge triangle-free classification and refers to retained archive excerpts. We independently filled in that classification in MINIMUM_DEGREE_GATE_SELF_CONTAINED.md: shortest C5, exterior K9,9 / K8,10 / K9,9 minus one edge; all compatible type-set and singleton/missing-edge cases; and the explicit12-set cost argument. This removes dependence on possession of those archive excerpts for the new proof.

The new verifier checks20 complete type-set pairs,55 singleton extensions,10 exceptional endpoint cases, and61 actual graph-family representatives. Of the61,12 violate alpha<=11 and are discarded; for the49 valid representatives it enumerates263 maximal independent sets and verifies maximum12-set cost6, hence a forbidden14-set with at least72 edges versus D(14)=69.

The127-row weighted-transversal certificate is NOT used in the source gate, the low-edge theorem or the new parent transfer. We do not claim to have recovered or executed the original archives in this turn. The new proof and finite checks are wholly within this workstream.

## Small source corrections retained in this audit

Q33_PARENT_SOURCE_MAP.md says "Since d_F(a)=13" immediately before t_a=d_M(a)+g_a. For an arbitrary shell vertex the correct statement is d_F(a)=13+g_a. The identity itself is correct; our parent audit derives it from the correct equation without assuming every shell vertex is regular.

A bipartite complement partitions the target into two cliques but does not require absence of target cross edges. Our common-neighbor proof uses only the clique-cover bound, so this verbal overstatement in the task outline is not imported.

## Promotion boundary

The Q33 parent's support-promotion route is bypassed once its original47-core lies in R(4,47). The same general gate applies to all four requested parent rows. This is a checked theorem-domain match, not copying a Q33-only minimum-degree assertion into E407.
