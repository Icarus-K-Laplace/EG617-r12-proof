# Q33 support-promotion — canonical state

Updated: 2026-10-30  
Branch: \`workstream/r12-q33-support-promotion-20261030\`  
Exclusive write path: \`r12_master/workstreams/q33-support-promotion-chat-20261030/\`

## Headline
**E408 Q33 support promotion: OPEN / NOT_CERTIFIED.**

## New result
The gadget-witness overlap coefficient is sharpened to four for every m: each selected gadget witness Q lies in G_C with alpha(C[Q])<=2, so C owns at least two of its six pairs. All other colors together can use at most four.

With this sharp U reserve and the component-pair charge, excluded support cells are:
- m=8: v=31,32,33;
- m=9: v=32,33,34;
- m=10: v=34,35.

First scalar/profile survivors:
- m=8,v=34,h=7;
- m=9,v=35,h=5,...,9;
- m=10,v=36,h=3,...,10.

The committed verifier cross-checks all support cells against a grouped-profile DP.

## Status
- Sharp gadget-overlap lemma, U/W reserves, component-pair charge: **PROVED_CONDITIONAL** under explicit source hypotheses.
- Integer/profile screen: **COMPUTATION_CERTIFIED**.
- Remaining support cells: **OPEN**.
- Global E408 Q33: **OPEN / NOT_CERTIFIED**.
- EG617(r=12): **OPEN / NOT_CERTIFIED**.
