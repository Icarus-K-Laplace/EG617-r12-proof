# Q33 universal 284-edge core attack — canonical state

Date: 2026-10-30  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Branch: workstream/r12-q33-v47-excess4-universal-core-attack-20261030  
Write scope: r12_master/workstreams/q33-v47-excess4-universal-core-chat-20261030/

## Headline

<PROVED> **Universal 284-edge core nonexistence.**

There is no simple graph H satisfying
\[
|V(H)|=47,\quad e(H)=284,\quad\delta(H)\ge12,\quad
\alpha(H)\le4,\quad\omega(H)\le11.
\]
This local theorem uses only the five displayed graph hypotheses; it does not require hereditary density caps.

<PROVED> **Source-complete minimum-degree gate.**

For every J in R(4,47), with all inherited induced-density caps retained,
\[
e(J)\le286\Longrightarrow\delta(J)\ge12.
\]
The proof is independent of V11 and uses the audited R(2,24), R(3,35), R(3,36), R(3,37) seed chain.

<PROVED_CONDITIONAL> **E408 / Qmax=33 parent contradiction.**

A genuine E408 h13 T61 parent with Qmax=33 has a degree-13 pivot with q=33, hence an induced 47-core with284 edges in R(4,47). The minimum-degree theorem supplies delta>=12, and the universal core theorem gives a contradiction. See Q33_PARENT_PROMOTION_RECEIPT.md.

## Certified components

- Independent degree-12 four-set: PROVED.
- Four private cliques and exact Z support identity: PROVED.
- Universal common-neighbour bound c<=3+epsilon(u)+epsilon(v): PROVED.
- K10 completion capacity: PROVED.
- K11-K11 two-support charge>=6: PROVED.
- All |Z|=3,4,5 support templates, including P and D mixed matrices: PROVED.
- Degree<=9 / degree10 / degree11 minimum-degree exclusions: PROVED.
- R(3,35) lower-order seed: PROVED under the explicit hereditary-cap class.
- 127-row rational certificate: COMPUTATION_CERTIFIED; exact Fraction replay passed in both retained copies.
- Independent source-complete arithmetic replay: PASS_EXACT_ARITHMETIC_REPLAY.

## Corrections made during audit

1. Replaced the old universal 2+epsilon common-neighbour claim with the valid 3+epsilon bound. The stronger 2+ bound is cap-dependent and not used.
2. Repaired the archived b=5 capacity count: the exact residual size is at least 21-b+s_i>=25, which justifies the subsequent sorted-size bounds.
3. Expanded the degree-10 pivot count to show explicitly that N(v) need not be a clique.
4. Kept finite verifier claims separate from analytic proof claims.

## Dependency firewall

Not used:
- V11 minimum-degree or completion theorem;
- Q32 285-edge/excess-six theorem;
- Kang–Pikhurko;
- degree-nine exceptional-vertex claims;
- universal Type-I, K6-free, or omega(H)<=5 assumptions;
- SAT/ILP UNSAT output or failed graph search.

Historical archives inspected and hashed are listed in MINDEG12_47_SOURCE_COMPLETE_AUDIT.md and INDEPENDENT_REPLAY_LOG.md.

## Global status boundary

This workstream closes only the E408 Qmax=33 charge layer under its explicit parent contract. E408 Q31/Q32 and E407 Q32 remain separate. Full EG617(r=12) remains **OPEN / NOT_CERTIFIED**.

No global canonical file or sibling branch has been modified.