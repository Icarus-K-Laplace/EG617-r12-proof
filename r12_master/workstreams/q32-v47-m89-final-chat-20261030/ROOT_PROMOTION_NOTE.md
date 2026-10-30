# Parent root promotion note — WITHDRAWN

> **DO NOT PROMOTE.** The previous proposed Q32 closure is invalid for EG617 because it assumes omega(H)<=5, omega(C)<=5 and universal Type-I exact-color factors. The actual balanced-coloring hypothesis gives only omega(C)<=12, and the Q32 47-core has omega(H)<=11. See AUDIT_RETRACTION_BALANCED_PREMISES.md. This file is retained as a historical record of the withdrawn proposal.

# Historical proposal — E408/Q32 Type-I partition obstruction

Date: 2026-10-30  
Origin: isolated workstream/r12-q32-v47-m89-final-20261030  
Write firewall: this note is only in the isolated m=8/9 workstream; no parent or sibling branch was modified.

## Historical result (conditional only)

The theorem V47_TYPEI_PARTITION_OBSTRUCTION.md proves only under the extra clique caps and Type-I source factorization:

> A graph H on 47 vertices with e(H)=285, delta(H)>=12, alpha(H)<=4, and omega(H)<=5 cannot be partitioned into any of 11K4+K3, 10K4+2K3+K1, or 11K4+K2+K1.

For every exact-129 non-target color C on the 61-point residual, the published Kang–Pikhurko equality classification (Theorem 1, Theorem 4, Lemma 5 of Kang–Pikhurko 2005) forces twelve disjoint C-colored K5 factors partitioning the 60 vertices other than a special point x. Since alpha(H)<=4, each factor meets O=V(K61)\H. The outside occupancy sum then forces exactly one of the three forbidden H-partitions, according as x lies in O, or x lies in H with two double factors, or x lies in H with one triple factor.

Therefore **no exact-129 color can coexist with the Q32 H-core contract**.

## Withdrawn parent-level consequence

The following claimed consequence is withdrawn because the parent does not supply the required clique caps or Type-I source coverage. The parent E408/Q32 ledger has m in {8,9,10} exact-129 colors. The old proposal had claimed it excluded all Q32 rows:
- v=44,45,46,47;
- m=8,9,10.

This is stronger than the isolated full-support m=8/9 task. The root workstream should audit and import the theorem rather than independently repeat the former scalar/CSP search.

## Exact dependency checklist

1. **H-core:** |H|=47, e(H)=285, alpha(H)<=4, delta(H)>=12, from Q32_CORE285_TERMINAL.md.
2. **Target K6-free:** omega(H)<=5, inherited from the global hypothetical coloring having no monochromatic K6. This is load-bearing and should be made explicit in the parent Q32 terminal/DAG.
3. **Every color alpha<=12:** the balanced-coloring property says every 13-set contains every color, hence alpha(C)<=12 for each color C. See front_end/FRONTEND_BRIDGE_THEOREM.md.
4. **Every color K6-free:** omega(C)<=5, again from the global no-monochromatic-K6 premise.
5. **Exact color existence:** m in {8,9,10} from the E408 outer ledger, so at least one C has e(C)=129.
6. **Published exact-129 source:** parent KANG_PIKHURKO_EXACT129_SOURCE_AUDIT.md. The complement has 1701 edges, is K13-free and non-12-partite; t_12(61)=1705 and p_12(61)=1701. Theorem 4/Lemma 5 leave only the (5^12) part-size sequence after the two size-six cases are excluded by omega(C)<=5.

## Verification status

- The proof artifact contains the complete Hall/tight-part argument and the primary-source parameter translation.
- The independent verifier reconstructs the source-induced partition, runs augmenting-path matchings, and emits an independent 5-set or clique of size at least six.
- A standalone replay of the helper logic on the embedded synthetic 285-edge, minimum-degree-12 fixture returned clique witnesses of sizes 7, 6, and 7 for the three shapes.
- The committed full verifier was not executed in this environment.
- No SMT run, SAT result, UNSAT result, or solver proof log is claimed or needed.
- The Kang–Pikhurko source audit and parent root documents are read-only dependencies; this workstream did not edit them.

## Scope firewall

This note proposes closure of the E408/Q32 graph terminal only. It does not close E407 Q32/V12, E408 Q33 support promotion, the front-end bridge, or the original EG617(r=12) theorem.


## Corrected promotion status

- The tight-part lemma is a valid conditional theorem: the three independent-part shapes force an independent 5-set or a clique of size at least six.
- Since the actual H core permits omega(H)<=11, the clique conclusion is not contradictory.
- The Type-I source factorization is not available for every exact-129 color from the balanced-coloring hypotheses alone.
- The local m=8/9 Q32 terminal remains OPEN / NOT_CERTIFIED.
- The parent root branch was not modified and remains OPEN / NOT_CERTIFIED.
