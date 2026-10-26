# Contract firewall: Q33 versus Q32

## Q33: 284-edge core

All statements in Q33_P49_REMAINING_PROFILES.md and Q33_P49_R7_DOUBLE_STAR_EXCLUSION.md assume:
- \(|V(H)|=47\), \(e(H)=284\), \(\alpha(H)\le4\), \(\delta(H)\ge12\);
- total degree excess \(\sum_H(d_H-12)=4\);
- the registered 61-point target residual and seven-block equality ledger;
- exact-129 Type-I factorization and its 11-point exceptional gadget;
- the exact row-budget classification for the particular profile;
- the registered four gadget normal forms and universal-D family.

The profile \((7,1^6)\) proof uses the 284-edge/excess-four contract through the exact-129 row classification. It does not use the 285-edge support-capacity theorem.

## Q32: 285-edge core

All Q32 statements must independently satisfy:
- \(|V(H)|=47\), \(e(H)=285\), \(\alpha(H)\le4\), \(\delta(H)\ge12\);
- total degree excess \(\sum_H(d_H-12)=6\);
- \(q=32\), equivalently \(e(M)+G_A=32\);
- the registered E408 Q32 seven-block/exact-129 contract.

The current Q32 support floor \(|U|\ge44\) and \(v=44\) triple-pair terminal are read-only dependencies from workstream/r12-e408-q32-excess6-20261025. They cannot be applied to Q33.

## Outer incidence notation

For each non-target color \(C\):
\[
e_C(R)=129+s_C,\quad s_C\ge0,\quad \sum_Cs_C=3.
\]
The registered duplicate identity is
\[
P_C+R_C+s_C=62.
\]
For an exact-129 color, \(s_C=0\), so \(P_C+R_C=62\). Here \(P_C\) is the block-block duplicate budget; \(R_C\) is the residual-to-block duplicate budget. They are not witness counts, and baseline edges are not added to \(P_C\).

The profile \(r_i(C)\) refers to the seven block-to-residual budgets with \(\sum_i r_i(C)=R_C\). It must not be confused with the 21 block-pair duplicate incidences.

## Witness distinctions

Keep these separate:
1. the 56 labelled independent four-set witnesses on the Q33 support-31 boundary;
2. the ten exact-component four-set witnesses per exact color used in the full component-support union;
3. the Q32 ten-or-eleven witness sets per color in the 285-edge support theorem;
4. the size-five blocker occurrences \(M_C\) in the outer seven-block ledger.

They have different labels, support sets, and disjointness contracts. A theorem for one family cannot be transferred to another without a proved map.

## Star-capacity rule

For a \(C\)-colored \(K_{12}\) \(Q\) and an outside vertex \(z\), the valid consequence of the no-independent-13 condition is
\[
d_C(z,Q)\le1.
\]
One external C-edge is permitted. A contradiction requires at least two C-edges from the same outside vertex into the same \(Q\). Any source claim using “at least one external C-edge” as a contradiction is not accepted.

## Promotion rule

- PROVED: all hypotheses are stated and the proof is analytic.
- PROVED_CONDITIONAL: a complete derivation under named retained inputs.
- COMPUTATION_CERTIFIED: exact verifier coverage/output only.
- OPEN: no complete exclusion.
- RETRACTED: an inference has been found invalid.

A finite verifier may certify a gadget enumeration, but cannot establish that a scalar profile is realizable or that all legal parent graphs have been excluded.
