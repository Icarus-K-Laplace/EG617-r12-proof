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


## 2026-10-30 update — component-pair charge
No new upstream source was introduced. The new lemma charges the already registered unselected isolated component K4s by their U- and W-internal pair counts. It uses the same 284-edge core, seven-witness, exact-129 component, gadget-independence, and unique-edge-ownership assumptions listed above. The pointwise inequality is elementary and exact for k=0,...,4. Global root status remains OPEN.


## 2026-10-30 correction — aggregate gadget overlap cap 4

The selected gadget witness Q is a four-set inside G_C, and the retained exact-129 gadget contract gives alpha(C[G_C])<=2. Hence alpha(C[Q])<=2 and e_C(Q)>=2. Because the six Q-pairs have unique colors, all colors other than C combined can occupy at most four pairs. This source fact is recorded in Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md Section 3 and Q33_CROSS_COLOR_GADGET_INTERSECTION.md Section 1/2. The current U-reserve coefficient is therefore 4 uniformly for m=8,9,10, superseding the coarser allowance in the first support-screen commit.


## 2026-10-30 variable-core source correction

The fixed c_i=4 profile is not treated as source-universal. The current screen uses only:
- exact-129 factor: ten isolated K5s plus an 11-vertex gadget;
- each K5 has at least one shell vertex, since five core vertices would be an independent 5-set in H; hence c_i<=4;
- gadget core size g=47-sum c_i lies in [7,11];
- seven-witness interface: either seven component K4s, or six component K4s plus one gadget four-set;
- alpha(C[G_C])<=2.

Primary source files read:
- \`KANG_PIKHURKO_EXACT129_SOURCE_AUDIT.md\`, Section 5;
- \`Q33_CROSS_COLOR_GADGET_INTERSECTION.md\`, Sections 1,4,5;
- \`R12_WITNESS_PACKING_BOUNDARY_KERNEL.md\`, Sections 2 and 7.2;
- \`R12_ZERO_EXCESS_WITNESS_THEOREM.md\`, Section 4;
- \`Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md\`, Section 3 for the gadget independence/capacity fact.

The stronger all-ten-components-have-four-core-vertices premise appears in the M10 local note under a retained shell-label theorem, but is not separately registered in the audited global root DAG. It is not used by the current variable-core model.


## 2026-10-30 canonical component-only selection update

Source path checked: branch workstream/r12-e408-q33-global-compat-20261025, commit 0cb2ff3968f005c9cb255958df7c02b220678701, files:
- r12_master/workstreams/zero-excess-witness-chat-20261025/R12_HIGH_SUPPORT_COLOR_WITNESS.md, Section 2;
- r12_master/workstreams/zero-excess-witness-chat-20261025/R12_WITNESS_PACKING_BOUNDARY_KERNEL.md, Sections 2–3.

For every exact-129 color, the source gives at least seven K5 components avoiding S. Six yield B-labelled four-point core witnesses. If the seventh contains pivot p, p is target-adjacent to all B, so that component cannot contain B; because it avoids S, its other four vertices lie in H. Hence the seventh also supplies a component K4 witness. The seven selected Q sets are disjoint within color and linear across colors.

For the support family now used in Q33_INDEPENDENT_VERIFIER.py, select those seven component witnesses in each exact color, so h=0. This is a constructive selection, not an assumption that gadget witnesses do not exist. It supersedes the need to model a gadget witness among these selected seven. The 7-witness support floors remain m=8:v>=31, m=9:v>=32, m=10:v>=34 (the last follows from 70*6>t4(33)).

The new U/W reserve screen uses:
- selected component edge reserve 42m;
- B_U=L_max(v)-42m-(11-m)p_12(v);
- B_W=t_4(47-v)-(11-m)p_12(47-v);
- exactly three unselected K5 components per exact color, with variable core sizes 0..4 and total core size 8..12.

No gadget witness or +4h overlap allowance is used. The previous all-h verifier is archived as Q33_VARIABLE_CORE_ALL_H_VERIFIER.py.

New screen result:
- m=8 excludes v=31..38; aggregate survivors v=39..47;
- m=9 excludes v=32..39; aggregate survivors v=40..47;
- m=10 excludes v=34..40; aggregate survivors v=41..47.

This remains a necessary aggregate profile test, not a graph-level UNSAT certificate. Root status remains OPEN.


## 2026-10-30 gadget-shell nonempty lemma

For each exact color, after choosing seven components avoiding S, seven shell vertices remain. Each of the three unselected K5 components contains at most one B vertex and at most three S vertices; p cannot share a non-target K5 with any point of A. Hence these three components can contain at most six shell vertices. At least one remaining shell vertex lies in the 11-vertex gadget. The gadget has at most ten core vertices, so the three unselected component core sizes satisfy 9<=sum c_i<=12.

This corrects the earlier profile interval 8..12. The component-only verifier and all-support table now use 9..12. The support exclusion ranges remain unchanged.

## 2026-10-30 first-survivor W equality

The component-only profile enumeration gives min W costs 3,2,1 at (m,v)=(8,39),(9,40),(10,41), respectively. The first two exactly saturate Turán W budgets 24 and18, forcing H[W]=4K2 and H[W]=3K2 union K1. Every exact-color W edge set is then a matching of size3 or2. The m=10 case has three units of W slack. Full details are in Q33_W_BOUNDARY_EQUALITY.md.
