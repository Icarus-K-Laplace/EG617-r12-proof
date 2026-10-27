# Q33 seven-block / labelled-witness global contradiction

Updated: 2026-10-27
Status: OPEN / NOT_CERTIFIED.

## Contract

Q33 uses a 47-vertex core H with e(H)=284, alpha(H)<=4, delta(H)>=12, and total degree excess four. For each non-target color C, the outer ledger is P_C+R_C+s_C=62, with e_C(R)=129+s_C and sum_C s_C=3. Let m in {8,9} be the certified remaining number of exact-129 colors; the m=10 branch is excluded by Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md.

The retained blocker theorem gives M_C >= 15+P_C. Summing yields sum_exact P_C >= 62m-427 and sum_exact M_C >= 77m-427. The lower bounds for m=8,9,10 are 189, 266, and 343. These do not exceed the available 70m occurrences, so the scalar sum alone is not a contradiction.


## New cross-layer capacity theorem: m=10 excluded

**Status: PROVED_CONDITIONAL** under the Q33 284-edge / 31-point / 56-witness contract and the exact-129 factor theorem.

Let h be the number of the 56 selected witnesses that are gadget witnesses. For the eight selected exact colors, the unselected component four-sets contribute at least \(72+6h\) distinct edges to \(\overline{H[W]}\). Since \(e(\overline{H[W]})=79+\delta+\epsilon_U\le96\), \(h\le3\).

If m=10, the two exact colors outside the selected eight supply 20 component four-sets. Their total U-incidence is at least \(2(31-7)=48\). Their pair-cost \(\sum\binom{k}{2}\) is at most \(\delta+4h\le33\): at most four edges per selected gadget witness can overlap, because the complement of its color graph is triangle-free on four vertices. The exact integer inequality \(k\le3/2+\binom{k}{2}/2\) then bounds their total U-incidence by 46, contradiction. Thus m is not 10. If m=9, h=0 similarly gives a capacity of at most 23 against a required 24, so h is at least one. The h=4 equality endpoint is then excluded by the OA(4,4,2,2) obstruction in Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md, so the final bound is h<=3.

The standalone arithmetic verifier verify_q33_exact_color_count_capacity.py passes. This narrows the global search to m=8,9 but does not close either branch.

### Refined \(m=9\) terminal

For the ninth color, the component four-sets have both \(U\)-pair cost \(c_U=\sum\binom{k_\ell}{2}\le\delta+4h\) and \(W\)-pair cost \(c_W=\sum\binom{4-k_\ell}{2}\le7+\delta+\epsilon_U-6h\). The required \(U\)-incidence is at least 24.

- \(h=1\): \(\delta\ge14\). If \(\delta=14\), the \(k\)-profile is \(2^6,3^4\).
- \(h=2\): \(\delta\ge10\). If \(\delta=10\), then \(\epsilon_U\ge1\), and the \(k\)-profile is \(2^6,3^4\); at \(\epsilon_U=1\), the W-edge capacity is exactly saturated.
- \(h=3\): \(\delta\ge11\). If \(\delta=11\), then \(\epsilon_U=4\) and the \(k\)-profile is \(2^4,3^6\); the four W-edges from the \(k=2\) sets exactly exhaust the remaining W-edge capacity.

The \(h=4\) endpoint is excluded. It would force \(H[W]=4K_4\) and \(\overline{H[W]}=K_{4,4,4,4}\), with the selected component witnesses edge-partitioning this graph into four \(K_4\)'s and 24 triangles. This induces an impossible \(OA(4,4,2,2)\). Therefore \(h\le3\) globally. The listed \(m=9\) endpoints are residual incidence contracts, not contradictions.

## P_C=49 frontier

For an exact-129 color, P_C=49 means R_C=13 and the seven block budgets r_i(C) sum to 13.

- (6,2,1^5): PROVED_CONDITIONAL by the independently replayed double-star theorem.
- (7,1^6): PROVED_CONDITIONAL by Q33_P49_R7_DOUBLE_STAR_EXCLUSION.md.
- (4,4,1^5): OPEN only in the all-component-representative-edges-present branch.
- (4,3,2,1^4): OPEN only in the all-component-representative-edges-present branch.

For the two open profiles, the registered incidence-sensitive screen excludes a missing component-label edge across the exceptional high-budget pair. Thus the remaining branch has all ten component-label representatives C-adjacent across all seven blocks.

## Exact ledger if ten C-colored K12s exist

Each of the ten isolated K5 components K_l has one representative in each outer block, so K_l plus its seven representatives forms a C-colored K12. The ten cliques are vertex-disjoint and account for 660 C-edges:
- 100 edges inside the ten K5 components;
- 350 edges from seven representatives per component to its K5;
- 210 diagonal representative edges across block pairs.

The exact-129 color has 870 edges total. The remaining 210 edges split by location into 29 gadget edges inside R, 90 outer-block-to-R edges not going to the component's own K5, and 91 outer-block edges outside the ten diagonal matchings. The 91 count is 42+P_C=42+49, from the 252 baseline outer-block edges plus 49 duplicate units.

This accounting is consistent; it is not a contradiction. The 49 duplicate units can include off-diagonal edges between distinct component cliques. Star capacity permits at most one external C-edge from a fixed outside vertex into a fixed C-colored K12; it does not prohibit all such edges.

## Next theorem required

A complete result must add a constraint beyond the current scalar ledger. The most promising interfaces are:
1. label-pair matching constraints for off-diagonal edges across all seven blocks;
2. a proved map between the full ten-component witness family and the 56 labelled four-set witnesses;
3. the 284-edge core's support/omission ledger and four units of degree excess;
4. exceptional-row gadget complements coupled to core witness packing.

The support-41 theorem applies only under its ten-exact-color/41-point contract. It cannot be transferred to m=8 or 9, nor to the separate support-31 witness family.

Current status: Q33 global compatibility OPEN; P_C<=48 for all exact colors not established; original EG617(r=12) OPEN / NOT_CERTIFIED.
