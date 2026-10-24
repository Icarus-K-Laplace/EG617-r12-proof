# R12 open frontiers

Status of the headline theorem: **OPEN / NOT_CERTIFIED**.

## F1. E407 Q32: common-K11 templates versus the same 284-edge core

**Contract.** A genuine 61-point T61 residual F in the original balanced coloring, with e(F)=407, delta(F)=13, alpha(F)<=5, omega(F)<=11. Choose a degree-13 pivot p, its 13-point shell A, and 47-point core H. The identity is 407=91+q+e(H). In the active Q32 cell, q=32 and e(H)=284.

**Available results.**
- V12 source-reports five rho=0 templates with a common regular K11, conditional on retained lower-order seeds.
- E407_CELL_B_FULL_CLOSURE.md eliminates the sharp |W|=23 Cell-B near-anchor design; it does not establish that every Q32 template lies in that cell.
- The 284-edge core has degree excess 2*284-47*12=4 when delta(H)>=12.

**Minimum gap.** Prove that no one of the five exact templates can coexist with the same legal 284-edge core, or prove a single joint incompatibility theorem eliminating all five. The template-to-core correspondence and all retained-seed dependencies must be explicit. V12's finite kernel certificate has now been independently replayed (8,677 weight vectors; 17,957 states; 1,984 labelled shells; 554 open entries). The analytic exclusions and the same-core completion theorem remain conditional/open; replay is not a parent-graph UNSAT proof.

## F2. E408 Q32 and Q33

**Contract.** e(F)=408; the outer equality ledger yields seven target K12 blocks anticomplete to a 61-point residual R with e(R)=408. Every color has 870 edges globally. For each non-target color C:
- e_C(R)=129+s_C, s_C>=0;
- sum_C s_C=3;
- P_C+R_C+s_C=62, with P_C the block-block duplicate count and R_C the block-R duplicate count.

For each exact-129 color, the blocker theorem gives R_C>=7 and P_C<=55. At least eight colors are exact-129 colors. These are global necessary constraints, not a contradiction.

For Q33/d3, the retained V11 interface yields the exact budget beta+X+G_B=3. The four beta cases and row-count consequences are necessary conditions only.

**Minimum gap.** Derive a joint incompatibility among all seven blocks, the same 284-edge core, the eleven non-target color factors, and the blocker-neighbourhood assignments. Do not infer individual defects vanish from the aggregate identity sum(h+kappa)=sum(eta+m).

## F3. Backend forcing Bridge A

**Contract needed.** Start with any legal maximum-q shell survivor arising from the original balanced coloring. Prove at least one of:
1. three pairwise nonadjacent degree-12 anchors in its legal 35-core;
2. a common-S owner subsystem satisfying the exact row-closure contract of GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md;
3. a fully enumerated finite shallow-loss / equality residue with a proved reduction from the original shell.

**What is missing.** The existing signature theorem starts after common-S row closure is assumed. The master theorem assumes boundary one-loss and, for its transversal consequence, the relevant low-cross bounds. The allowance-coverage theorem explicitly does not claim that every historical shell survivor has been extracted into such a common-S family.

**Minimum gap.** An exhaustive shell-to-owner extraction theorem with a conservation ledger and no unsupported jump from source-reported layer labels.

## F4. Backend shallow-loss Bridge B

After a valid common-S extraction, unresolved local regimes are:
- d2 higher-slack shallow-loss equality states;
- d3 common missing triples whose internal missing graph is not K3;
- any allowance >6 near-anchor equality actually permitted by the surviving layer ceiling.

d3 common-missing-triangle cases through allowance 6 are absorbed by GLOBAL_INDEPENDENT_TRIPLE_H3_THEOREM.md, provided its stated core contract holds.

## F5. Original-proof dependency check: contextual R(4,49)

CONTEXTUAL_R449_FULL_COLOR_IMPOSSIBILITY.md gives a short conditional contradiction: e(F)>=319 from delta(F)>=13, while the eleven non-target colors each have at least79 edges under alpha(F)<=4, alpha(C)<=12, omega(C)<=4; hence e(F)<=307. If the F5 contract is the exact original-coloring contract, the abstract R(4,49) branch is bypassed for the original theorem. The abstract E333–E340 classification can remain open without blocking the T61-only proof path. This contract correspondence must be preserved in the final DAG.

## F6. Shell/core maximum-independent-set witness capacity (new proved interface)

**Contract.** T61 residual F with alpha(F)<=5, omega(F)<=11; legal pivot and 13-shell A; 47-core H with alpha(H)<=4; every 49-subset has alpha at least5; inherited cap D(n)=binom(n,2)-11p_12(n).

**Proved.**
1. If a shell row has t_a<=7, then H\N_H(a) has alpha exactly4. Otherwise the second-Turan lower bound p_3(n)+floor(n/3)-1 for n=47-t_a in 40..47 exceeds D(n).
2. Every target edge ab in F[A] has at least one good endpoint. Thus at most five shell vertices are bad and at least eight are good.
3. Under E408 Q33/d3, the exact budget beta+X+G_B=3 forces every B-row to have t_b<=6, hence each b has an independent 4-set Q_b in H anticomplete to it. For every a in S with ab in M, Q_b intersects N_H(a). At least five B-vertices have k_b>=2, so at least five witnesses hit at least two S-rows.

**Minimum remaining gap.** Prove a witness-capacity / incidence incompatibility theorem for these maximum independent 4-sets against the same 284-edge core and the seven-block color constraints. The current lemma does not imply that witness sets coincide and does not eliminate Q33.


## F6. Witness-capacity cross-cut theorem (new proved interface)

See R12_WITNESS_CAPACITY_CROSSCUT.md.

- Every independent 4-set Q in the 47-core hits at least three distinct shell rows, by alpha(F)<=5 and omega(F)<=11.
- For each b-witness, its hit hubs contain T_b and cover every edge of M[S].
- Every independent triple in H_b extends to an independent 4-set when t_b<=3. For t_b=4,5,6, a failure to extend requires epsilon(X)>=8-t_b, so it must capture most/all of the four core-excess units.
- In E408 Q33, every exact-129 color has at least five no-S K5-component witnesses; the selected five labels have sum k_b>=7-beta. Their 4-sets are disjoint within a color and intersect in at most one vertex across colors.

**Remaining gap.** The resulting scalar capacity bounds do not contradict any of the five E407 templates or the E408 Q32/Q33 seven-block systems. The next proof must use the actual 284-edge H adjacency and the labelled row-hit patterns.


## F7. E407 template hub-complete escape versus high-B-degree witnesses

The row-count screen yields n3>=6 in templates A and C, n3>=2+2n0 in B, n3>=1+2n0 in D, and n2+n3>=5 for each end hub in E. Therefore:
- A/C: every independent-4 witness that misses any hub must hit at least six B rows, has parent target-degree excess at least2 on its four core vertices, and can witness at most four B labels.
- B/D/E: analogous but weaker hub-row capacities are specified in R12_WITNESS_CAPACITY_CROSSCUT.md.

The remaining escape is a hub-complete witness, or an overlap pattern in which the excess cost of high-B-degree witness sets is reused by shared core vertices. The proof cannot sum excess over overlapping witnesses. Next attack: classify the overlap graph of ten Q_b sets and use exact core degree 12+epsilon to control common triples/pairs.


## F7. Row-transversal and high-k witness packing (new)

See R12_ROW_TRANSVERSAL_AND_Q33_PACKING.md.

For every missing shell edge ab and shell row t_a<=12, the 4-sets in H\D_a have independence number exactly4 and all must hit D_b. The five E407 templates therefore induce minimum transversal systems (size3 for full rows against a t=10 hub, size2 for pair rows against a t=11 hub, size1 for singleton rows against a t=12 hub), with PAIR-13 / TRI-24 overlap restrictions.

For E408 Q33/d3, the exact-129 factor theorem yields at least six B-bearing K5 components with no S per exact-129 color. Combined with at least five high-k B rows, this forces at least one high-k no-S witness per exact-129 color, and at least two when beta is 0 or1. The resulting 8/16-witness packing is a necessary condition only; no terminal is excluded yet.


## F8. E408 exact-129 pairwise blocker compatibility (new theorem, 2026-10-24)

For each exact-129 color C and target block B_i, the twelve neighborhoods X_b=N_C(b)∩R satisfy the pairwise inequality
alpha(C[U\(X_b∪X_{b'})]) <= k(X_b,X_{b'}),
where k counts the isolated K5 components fully covered by the union. This is forced because b,b' are nonadjacent in C and an independent 11-set in R outside both neighborhoods would extend them to a forbidden independent 13-set in C.

Equality e_C(B_i,R)=62 has a rigid normal form: ten distinct exact K5 blockers plus two six-subsets of U covering U and intersecting in one vertex. Thus r_i(C)=1 is not just a scalar boundary; it fixes the entire local incidence pattern. Globally, sum_i(r_i(C)-1)=55-P_C; if P_C=55, all seven blocks have the equality form and each K5 component plus its seven representatives is a C-clique of size 12. At most four colors can have P_C=55 because sum_C P_C=252, so at least four exact-129 colors have a strict-slack block.

Remaining gap: exploit the strict-slack blocker families and cross-block duplicate matchings to contradict the E408 global system. This theorem does not itself eliminate E408 Q32 or Q33.


## F9. Pair-indexed zero-excess hub-cover system

Under the 284-edge/excess-four core contract, any two regular B rows have a common independent four-set in H_0, by the six-deletion zero-excess theorem. If their missing-hub sets jointly cover S, the common set must hit every hub. The E407 labelled-pair lower bounds are A/C=39, B=17, D/E-full-row=9; these are pair certificates, not distinct four-sets. E's no-full-row case forces all B rows to miss both P3 endpoints and yields endpoint-complete common-witness certificates for all 45 row pairs.

**Remaining limitation:** a single four-set can serve multiple row pairs. The theorem does not itself force a large family of distinct hub-complete witnesses and is not a terminal exclusion.


## F10. Corrected exact-129 zero-excess component packing

Every exact-129 color has at least six B-labelled no-S K5 components and at least two zero-excess labelled witnesses, giving 14 witnesses in E407 and 16 in E408 Q33. Do not use the withdrawn beta-sensitive 6/7/8 component count. If a full B row exists, each exact-129 color has at least three hub-complete B-labelled witnesses; E with no full row has at least six endpoint-complete witnesses per color.

## F11. Linear-witness transversal boundary

The valid transversal theorem proves tau(Q)>=7 for the E407 v=29,m=49 and E408 Q33 v=31,m=56 support-boundary families. Hence every vertex outside their union has at least seven neighbors into the union.

For E407 the unconditional window is delta+epsilon_U<=16 and epsilon_U+2delta>=2, with 0<=delta<=16. The sharper delta<=15 bound is conditional on proving L non-four-partite. If delta=16, L is forced four-partite but non-complete. For E408 Q33, delta+epsilon_U<=17; the non-complete four-partite branch remains arithmetically compatible.

The high-multiplicity star dichotomy e(H[U])=135 or >=144 is not accepted: its proof only forces the complement to be tripartite, not complete tripartite. Audit correction: the shell-incidence union proof has a zero-support gap; safe full-row support-union floors are >=7 in E407 template A and >=6 in C, not 11/10, unless one separately proves every core vertex has a shell neighbour. See R12_SHELL_INCIDENCE_UNION_AUDIT.md. These results do not yet close any terminal.


## F12. E407 g=16, epsilon_U=0 corner

The valid boundary identities give e(L)=310, e(H[U])=96, e(U,W)=156, e(H[W])=32; Brouwer forces L four-partite with part sizes (7,7,7,8). The 49 witnesses cover every pair between the three seven-point parts once, while 21 pair slots between the eight-point part and the three seven-point parts remain unused; five of these are missing from L.

A live audit constructed a modified TD(4,7) where the eighth point is used in one block, and a size-8 transversal T hits all 49 blocks without containing a whole part. Therefore “the eighth point is unused”, “all five missing edges meet one point”, and “every size-8/9 transversal contains a whole part” are not consequences of pairwise linearity alone. The full-core corner remains OPEN; additional degree, shell-support, or color-label constraints are needed.


## F13. Minimum-transversal boundary classification (new, 2026-10-25)

See R12_TRANSVERSAL_BOUNDARY_CLASSIFICATION.md and its arithmetic verifier.

- The witness family has no two distinct 7-transversals with a nonempty intersection; pair counting across color classes forces distinct transversals to be disjoint.
- E407 Q32's v=29, 49-witness boundary cannot have \(\delta\le1\); hence \(\delta\ge2\), where \(\delta=e(\overline{H[U]})-294\) counts complement edges not covered by the selected K4 witnesses.
- E408 Q33's v=31, 56-witness boundary must satisfy \(2\delta+\epsilon_U\ge8\), together with \(\delta+\epsilon_U\le17\).
- These are genuine exclusions of low-extra-edge integer profiles, but the remaining boundary kernels are OPEN. No result is transferred to E408 Q32's 285-edge core.


## F14. E408 Q33 four-partite equality kernel excluded (2026-10-25)

See R12_E408_Q33_FOUR_PARTITE_S0_10_EXCLUSION.md and verify_e408_q33_four_partite_s0_10.py.

- Under L four-partite and the 31-vertex/56-witness contract, the only possible S0=10 degree pattern reduces to six D-neighborhoods, three full-large-part neighborhoods per each of A/B/C, and one exceptional size-10 hitting set.
- The exceptional hitting set is impossible for s=0,1,2 selected D vertices, by pair-counting against the three large-part pair systems and the extra-edge budget delta<=5.
- Thus the four-partite E408 Q33 boundary satisfies S0=epsilon_U+2*delta>=11, strengthening the sibling result S0>=10.
- The non-four-partite E408 Q33 branch remains OPEN; no full E408 Q33 terminal is closed.
