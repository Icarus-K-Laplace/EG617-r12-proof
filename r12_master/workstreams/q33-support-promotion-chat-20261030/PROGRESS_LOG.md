# Q33 support-promotion progress log

## 2026-10-30 — sharp gadget-overlap correction

Auditing Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md Section 3 and Q33_CROSS_COLOR_GADGET_INTERSECTION.md revealed that the aggregate nonexact overlap on one selected gadget witness is at most four, not six: alpha(C[Q])<=2 forces at least two of the six pairs to be colored C itself.

Replaced the coarse coefficient min(6,4(11-m)) by the sharp uniform coefficient4 for m=8,9,10.

With the component-pair charge, the all-support screen now excludes:
- m=8: v=31,32,33;
- m=9: v=32,33,34;
- m=10: v=34,35.

First survivors:
- m=8,v=34,h=7;
- m=9,v=35,h=5,...,9;
- m=10,v=36,h=3,...,10.

The verifier was updated and cross-checked against a grouped-profile DP on all47 (m,v) cells. Global root status remains OPEN.
