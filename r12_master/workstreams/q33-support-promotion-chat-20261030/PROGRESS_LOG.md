# Q33 support-promotion progress log

## 2026-10-30 — component-pair charge closes the first survivors

Starting from commit d79ef2eee7787331f308c1d2651f9d46e81f5f03, added a new analytic charge over every unselected component K4.

For k=|Q intersect U|:
\[
C(4-k,2)+2C(k,2)\ge3.
\]
There are 3m+h unselected component four-sets. Their U-pair and W-pair costs are bounded by the two reserve budgets B_U and B_W. Therefore:
\[
3(3m+h)\le B_W+2B_U.
\]

This eliminates the first scalar survivors from the previous commit:
- m=8,v=33,h=5;
- m=9,v=34,h=4,5,6;
- m=10,v=35,h=2,...,8.

New first survivors:
- m=8,v=34,h=4,...,7;
- m=9,v=35,h=3,...,9;
- m=10,v=36,h=3,...,10.

Verification:
- exact all-support arithmetic: PASS;
- grouped-profile DP over every per-color 3/4-component k-profile: PASS;
- scalar charge classification equals grouped-profile DP on all47 (m,v) cells.

Scope: conditional necessary constraints only. Larger-support graph cases remain OPEN; global root status unchanged.
