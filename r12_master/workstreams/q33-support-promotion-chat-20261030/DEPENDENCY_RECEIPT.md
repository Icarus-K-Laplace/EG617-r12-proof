# Q33 support-promotion dependency receipt

Date: 2026-10-30  
Exclusive write path: \`r12_master/workstreams/q33-support-promotion-chat-20261030/\`.

## Live sources read

| Source branch / HEAD | File | Blob SHA | Use |
|---|---|---|---|
| \`workstream/r12-twochat-e408-global-20261026\` / \`b0459807acd4b7e386148056ddf77d7998918893\` | \`ROOT_DEPENDENCY_DAG.md\` | \`09b4d5505d8b80839f2868aca1d427263158eab7\` | Q33 promotion is OPEN; exact remaining parent gate |
| same | \`ROOT_PROMOTION_RECEIPT.md\` | \`486806a58816e86cefa2c2a2aebb02927cb24d54\` | 31-point local theorem conditional; v>31 open |
| same | \`Q33_HIGH_SUPPORT_U_RESERVE_AUDIT.md\` | \`c62dd2ada346f034cfc24aaf3e7b2cd7c5b5d4ea\` | f0/f1 and general L_U bound |
| same | \`Q33_NONEXACT_U_RESERVE_CLOSURE.md\` | \`0dd507f77720f2481bbe79b66be695ffce5e6e8c\` | exact v=31 reserve |
| same | \`Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md\` | \`4802a9a867a248c8fb5b9e6541d7a0e87d74198f\` | gadget overlap fact, m=10 local theorem |
| same | \`front_end/E408_Q33_CORE_ALMOST_REGULAR_NORMAL_FORM.md\` | \`f911259f5d8b74d042d2ec16ad38bffcafe900ec\` | 284-edge/excess-four core |
| same | \`front_end/E408_Q33_D3_EXACT_BUDGET.md\` | \`68d4a774d336f6ad9e3275627c3720a3618e31f4\` | read for upstream shell identities; not used to strengthen scalar result |
| \`workstream/r12-e408-q33-global-compat-20261025\` / \`0cb2ff3968f005c9cb255958df7c02b220678701\` | \`.../R12_WITNESS_PACKING_BOUNDARY_KERNEL.md\` | \`d80655fa9e2768cf99f33fc8594ecca753eeee\` | seven witnesses/color, linearity, support floors |
| same | \`.../R12_HIGH_SUPPORT_COLOR_WITNESS.md\` | \`bf7f39b7b94e8496a44a015dbea57ac77c891d68\` | shell-label witness facts |
| root branch | \`Q33_CROSS_COLOR_GADGET_INTERSECTION.md\` | \`cb9f0bb0512151f9ff67f4d5438abf382ebdbc7f\` | reserved for next structural attack |

## Explicit assumptions

1. Q33 core has 284 edges and total degree excess four.
2. m is in {8,9,10}; n=11-m.
3. Each exact-129 color supplies seven pairwise-disjoint selected four-set witnesses.
4. Selected witnesses from different colors intersect in at most one vertex.
5. At most one selected witness per selected color is a gadget witness.
6. Unselected isolated components are four-core-vertex K4s under the retained factor/shell-label contract.
7. Every nonexact color has independence number at most12 on U and W.
8. Each other color is triangle-free on a selected gadget witness K4, since the exact color's gadget has alpha<=2.
9. Unique edge ownership holds.

If any parent hypothesis is not certified for a proposed Q33 completion, the relevant implication remains conditional.

## Not used
- No Q32 285-edge/excess-six identity.
- No degree-nine exceptional-vertex premise.
- No exceptional-vertex injectivity.
- No V12/E407 premise.
- No assumption |U|=31.
- No solver UNSAT output.

This workstream does not modify the global root receipt or global root status.
