# Q33 support-promotion — canonical state

Updated: 2026-10-30  
Branch: \`workstream/r12-q33-support-promotion-20261030\`  
Exclusive write path: \`r12_master/workstreams/q33-support-promotion-chat-20261030/\`

## Headline
**E408 Q33 support promotion: OPEN / NOT_CERTIFIED.**

## New result
Added the component-pair charge inequality
\[
3(3m+h)\le B_W+2B_U
\]
by summing \(\binom{4-k}{2}+2\binom{k}{2}\ge3\) over all unselected component K4s.

Together with the U- and W-reserve inequalities, it excludes:
- m=8: v=31,32,33;
- m=9: v=32,33,34;
- m=10: v=34,35.

First scalar/profile survivors:
- m=8,v=34,h=4,...,7;
- m=9,v=35,h=3,...,9;
- m=10,v=36,h=3,...,10.

The committed verifier exhausts all support sizes and h values and cross-checks the three inequalities against a grouped-profile DP for all47 cells.

## Status
- Reserve and charge inequalities: **PROVED_CONDITIONAL** under explicit source hypotheses.
- Integer/profile screen: **COMPUTATION_CERTIFIED**.
- Remaining support cells: **OPEN**.
- Global E408 Q33: **OPEN / NOT_CERTIFIED**.
- EG617(r=12): **OPEN / NOT_CERTIFIED**.
