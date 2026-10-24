# R12 independent audit — first pass

Date: 2026-10-24. Scope: source contracts and arithmetic, not a full independent replay of every archived certificate.

## 1. Repository / branch audit

- Main HEAD at branch creation: 22cc93df4fab06ac9761e682ac06746ac42f69f4.
- Created branch workstream/r12-ultimate-closure-20261024 from main.
- The branch was absent before creation.
- Astra D-low branch exists and is 5 commits behind main with no commits ahead; its current branch head is b98bea36e36a033100b8bf09a599897cb5afd7de.
- Astra A-ext near-anchor branch exists but is divergent from main (66 ahead, 15 behind at comparison time) and its fetched workstream is a general-r theorem, not an r=12 T61 closure. Its own canonical status says A_ext* remains OPEN. No result from that branch is imported into this fixed-r proof without a matching contract.

## 2. Contextual R(4,49) count: checked

Given a legal contextual F with alpha(F)<=4 and delta(F)>=13:
- e(F)>=ceil(49*13/2)=319.
- For each non-target C, alpha(C)<=12 by the original balanced-coloring condition.
- A K5 in C would be an independent 5-set in F, so omega(C)<=4.
- The complement of C is K13-free and not 12-partite: if 12-partite, its parts are cliques in C of size at most4, covering at most48 vertices.
- The second-Turan lower bound gives e(C)>=p_12(49)+floor(49/12)-1=76+4-1=79.
- The eleven non-target colors use at least869 edges, so e(F)<=1176-869=307.
- Contradiction 319>307.

This is a valid conditional exclusion under the stated F5 contract and cited second-Turan theorem. It does not independently rerun the F7 recurrence certificate.

## 3. Three-anchor bound reconciliation

The later GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md proves K>=8, hence e(H)>=214, for three independent degree-12 anchors in a 35-core with alpha<=3, omega<=11, delta>=12. The older support master theorem uses e(H)>=213 / q<=E-304. The old implication is weaker, not contradictory; it should be superseded by the stronger bound when the anchor contract is actually met.

## 4. E407 local Cell-B closure: proof audit

Under the exact Cell-B contract, every independent 4-set Q in O has four disjoint target 3-neighbourhoods in W partitioning B union {x} or A union {y}. The color-factor certificate shows:
- qw cannot have the special P3 color;
- equality in the 20 non-target incidence budget forces nine ordinary matching-edge certificates and exactly one special certificate qx or qy;
- therefore every q in Q has at least one target neighbour in each side A and B.
Four disjoint triples each meeting both sides cannot partition B union {x} (only one A vertex) or A union {y} (only one B vertex). Contradiction.
This verifies the local Cell-B elimination algebraically. It does not prove all E407 Q32 templates fall into Cell-B.

## 5. E408 exact129 blocker arithmetic

The E408 seven-block theorem gives P_C+R_C+s_C=62 and sum s_C=3. The exact129 blocker theorem states that at most ten of the twelve vertices of any B_i can have a size-5 blocker; the other two need at least six C-neighbours in R. Hence e_C(B_i,R)>=10*5+2*6=62, so r_i(C)>=1, R_C>=7, and P_C<=55. This is consistent with the aggregate equations; no contradiction follows from this inequality alone.

## 6. Unverified items

- F7 recurrence generator/verifier replay and the exact archive.
- V11/V12 finite package replay is now complete; analytic rule applicability and the same-core completion theorem remain conditional/open.
- V8 package-level E334 forcing bridge replay.
- Universal extraction from arbitrary shell survivors to the common-S support master contract.
- Full E407 Q32 and E408 Q32/Q33 terminal exclusion.

## 7. V11/V12 finite certificate replay

Fresh local replays were run from the Library-delivered archives after SHA256SUMS checks passed:
- V11: 684 kernel weight assignments, 349 outside-count states, 259 labelled necessary shells; status COMPUTATION_CERTIFIED; certificate hash 0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b.
- V12 E407 Q32: 8,677 weight vectors, 17,957 count states, 1,984 labelled shells; 90 D3/rho=1, 1,192 near-K12, 148 K9-pair-row entries screened; 554 remain OPEN; certificate hash cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30.
- Neither verifier used a SAT/ILP solver; neither claims a completed parent graph. See R12_V11_V12_REPLAY.md for archive hashes and commands.

## 8. Witness-capacity audit

The new cross-cut theorem derives a three-shell-row support condition, a hub vertex-cover condition, and a defect-sensitive triple-extension rule. It also proves the E408 Q33 exact-129 component packing lower bounds. These constraints do not contradict the five E407 templates or the E408 seven-block system by scalar counting alone. The actual adjacency-sensitive packing theorem remains open.

Conclusion: current state remains OPEN / NOT_CERTIFIED.