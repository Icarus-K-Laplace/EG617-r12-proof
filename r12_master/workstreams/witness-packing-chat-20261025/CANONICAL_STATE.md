# Canonical state — R12 witness-packing line

Date: 2026-10-25  
Branch: workstream/r12-witness-packing-chat-20261025  
Repository: Icarus-K-Laplace/EG617-r12-proof

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.**

This workstream attacks the E407 Q32 and E408 Q33/d3 common 284-edge core using exact-129 K5-component witnesses and linear four-set packing. It does not close E407/E408 or the original K145 theorem.

## Proved under retained contracts

1. Every exact-129 color supplies at least seven independent four-sets Q in H from K5 components avoiding S; at least six are B-labelled. The seventh may be p+Q.
2. Since the 284-edge core has total degree excess four, each exact-129 color has at least two B-labelled witness sets all of whose vertices have core degree 12.
3. The total witness family is linear: any two Q-sets from distinct colors intersect in at most one vertex; within a color the selected component Q-sets are disjoint.
4. Turán plus the exact core edge budget proves union-size floors: E407 Q32 has v>=29; E408 Q33 has v>=31. If E407 has at least eight exact-129 colors, v>=31; if E408 has at least nine, v>=32.
5. The exact residual edge-count boundary is E407 129^7,130^4 and E408 Q33 129^8,130^3.

## Imported from live sibling branches

- E408 Q33/d3: at least one high-k (k_b>=2) no-S witness per exact-129 color, and at least two for beta=0 or1, under the retained Q33 budget.
- Outer E408 seven-block system: M_C>=15+P_C for exact-129 colors, with outer-block labels kept separate from inner shell labels.
- Zero-excess core theorem: H_0 minus any set of at most six vertices still has independence number four in the 284-edge case; this supports pairwise common zero-excess witnesses for regular rows.

Exact branch heads and qualifications are in CROSS_BRANCH_SYNC_20261025.md.

## Independent audit warning

The emergency sibling's m=10 witness-star dichotomy e(H[U])=135 or >=144 is not established by its stated second-Turán argument. The proved conclusion from that step is only three K10 parts in H[U] plus at most eight cross-part edges. This line does not rely on the stronger unsupported dichotomy.

## Latest transversal-boundary update

- The linear witness family has transversal number at least seven in the two support-boundary kernels. Every vertex outside the witness support therefore has at least seven neighbors into it.
- E407 boundary budget is delta+epsilon_U<=16 and epsilon_U+2delta>=2. Do not claim delta<=15 unless non-four-partiteness is independently proved.
- E408 Q33 boundary budget is delta+epsilon_U<=17; the transversal floor adds no tighter inequality there.
- A separate audit found the same logical gap in two sibling arguments: tripartite/four-partite does not imply complete multipartite. The four-partite boundary branches remain open.

## Open obligations

- E407 Q32: eliminate the v=29, 49-witness boundary under the five template row-transversal systems.
- E408 Q33: eliminate the v=31, 56-witness boundary using the zero-excess witnesses, high-k labels, and seven-block duplicate system.
- E408 Q32: still separate; its core has 285 edges and excess six. No excess-four theorem is transferred without proof.
- Preserve the original K145-to-T61 bridge and all inherited Ramsey/extremal input contracts.

## Audited shell-incidence theorem

SHELL_INCIDENCE_UNION_LEMMA.md proves the exact identity e(A,H)-47=e(M)-15, but the original comparison omitted possible core vertices with zero shell support. With z<=4 such vertices, the valid full-row union floors are at least 7 in E407 template A and 6 in template C. Both exceed three, but the stronger 11/10 floors are withdrawn unless z=0 is separately proved.

## New E408 Q33 theorem

R12_E408_Q33_UNIVERSAL_S0_11.md proves under the 31-point/56-witness minimum-support contract that S0=epsilon_U+2delta>=11, without assuming L is four-partite. The proof first shows every 7-transversal is unique and can be the U-neighbourhood of at most four W vertices; equality S0=10 then forces a (4,3,3) family of R-only 8-neighbourhoods, which creates a K12 and contradicts omega(H)<=11. Arithmetic checks passed. This removes the S0=10 boundary, not the whole E408 Q33 terminal.

## Verification assets

- WITNESS_PACKING_INCOMPATIBILITY.md — packing proof and boundary derivations.
- verify_witness_packing.py — standard-library arithmetic checks only.
- R12_E408_Q33_UNIVERSAL_S0_11.md and verify_e408_q33_universal_s0_11.py — new conditional theorem and arithmetic verifier.
- CROSS_BRANCH_SYNC_20261025.md — live sibling head SHAs and reconciliation.

No finite arithmetic script is represented as a graph-completion or root-theorem certificate.
