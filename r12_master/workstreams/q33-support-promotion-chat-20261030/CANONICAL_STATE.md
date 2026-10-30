# Q33 support-promotion — canonical state

Updated: 2026-10-30  
Branch: \`workstream/r12-q33-support-promotion-20261030\`  
Exclusive write path: \`r12_master/workstreams/q33-support-promotion-chat-20261030/\`

## Headline

**E408 Q33 support promotion: OPEN / NOT_CERTIFIED.**

## New result

A source-conditional all-support scalar screen now selects seven witnesses from every exact-129 color and couples U- and W-side reserves.

- m=8: v=31,32 excluded; first scalar survivor v=33,h=5.
- m=9: v=32,33 excluded; first scalar survivor v=34,h=4,5,6.
- m=10: v=34 excluded; first scalar survivor v=35,h=2,...,8.

All support sizes through47 were checked. A second dynamic-programming implementation independently reproduced all47 cells.

## Status labels
- U/W reserve inequalities: **PROVED_CONDITIONAL** under the explicit source hypotheses.
- Exact finite arithmetic screen: **COMPUTATION_CERTIFIED**.
- Remaining cells: **OPEN**; no graph realization is asserted.
- Global E408 Q33: **OPEN / NOT_CERTIFIED**.
- EG617(r=12): **OPEN / NOT_CERTIFIED**.

## Next target

Attack the tightest remaining cell (m,v,h)=(8,33,5), where both U and W reserves have at most two unused edge units. Then attack (9,34,4--6) and (10,35,2--8) with full labelled component/gadget incidence.
