# R12 progress log

## 2026-10-24 — Round 1: source audit and proof-DAG correction

### Repository actions
- Confirmed private repository Icarus-K-Laplace/EG617-r12-proof; default branch main.
- Main HEAD at workstream creation: 22cc93df4fab06ac9761e682ac06746ac42f69f4.
- Verified the target branch did not exist, then created workstream/r12-ultimate-closure-20261024 from main.
- Astra D-low branch is an ancestor of main (0 ahead / 5 behind); its comparison-time HEAD is b98bea36e36a033100b8bf09a599897cb5afd7de.
- Astra A-ext branch is divergent (66 ahead / 15 behind at comparison time). Its fetched theorem is a general-r result, explicitly PARTIAL / OPEN, and is not imported into the fixed-r=12 proof.
- All writes in this round are confined to this workstream directory.

### Mathematical audit
1. Independently checked the contextual R(4,49) edge contradiction under the exact F5 contract:
   - target floor 319;
   - each non-target color floor 79;
   - total edge count forces target at most307;
   - contradiction.
   Status: PROVED_CONDITIONAL on F5 and the cited second-Turan theorem. The 1752-node / 144-stop recurrence itself was not rerun.
2. Independently checked the E407 sharp |W|=23 Cell-B color-certificate contradiction. It closes that Cell-B subcase only, not all Q32 templates.
3. Checked the E408 exact129 blocker arithmetic: R_C>=7 and P_C<=55 follow, but these inequalities alone do not contradict the global duplicate equations.
4. Reconciled the three-anchor bound: the latest K=6 full closure gives e(H)>=214 / q<=E-305 under three independent degree-12 anchors. Older source summaries with 213 / E-304 are weaker; the support master theorem's weaker statement remains valid but should be superseded when the stronger anchor contract is met.
5. Confirmed the universal forcing-to-master extraction bridge is still OPEN: the support master theorem does not itself derive its common-S / one-loss / low-cross hypotheses from every historical shell survivor.

### Files created
- R12_CANONICAL_STATE.md — commit 0a6147cc008d5eeef4e5496881e3ad6079cbfb7d
- R12_OPEN_FRONTIERS.md — commit 11201e1c4ab455f38d3a57a315dfd4705169785a
- R12_DEPENDENCY_LEDGER.md — commit 39cb7f336276c39c3b72c8a3ee7122bf7d1ef336
- R12_PROOF_DAG.md — commit 541458ac8e1403df67d2959e0f1e6400231fa18e
- R12_FORCING_TO_MASTER.md — commit 2d471759a06684eef0b312e01e8efad3aed871b6
- R12_E407_E408_COMPATIBILITY.md — commit 9dced3393c655198ad68fc99b95875a5b1073642
- R12_FINAL_CONTRADICTION.md — commit d9384bce20de59f1fbf1a990029ba18ea95478e5
- R12_INDEPENDENT_AUDIT.md — commit 6b133f100bd0d13aacb3e31f8eacfb42cd46d757

### Current result
No open terminal contract has been eliminated in this round. The proof DAG is cleaner: the abstract R(4,49) E333–E340 program must not be mistaken for a necessary original-proof branch if the contextual F5 contract applies. The actual fixed-r=12 blocker remains T61, specifically E407 Q32 and E408 Q32/Q33.

### Next attack
Prove a joint T61 shell/core incompatibility theorem that uses the original no-R(4,49) condition on every 49-subset together with the 284-edge core and exact color-factor constraints. Do not promote source-reported V12/V8 statements without replay.

## 2026-10-24 — Round 2: shell/core witness-capacity theorem

### New proved statement
Committed R12_SHELL_CORE_WITNESS_LEMMA.md at 020b64d5fdf3a4aa3abe66d86be3489565760b22.

1. **Small-row lemma.** For a T61 shell vertex a, t_a<=7 implies alpha(H\N_H(a))=4. If alpha were <=3, the induced n=47-t_a vertex graph has n in [40,47], alpha<=3 and omega<=11. Brouwer's second-Turan lower bound exceeds the inherited target-edge cap D(n) for each of these eight n-values.
2. **Pair-extension lemma.** Every target edge ab in F[A] has at least one good endpoint, since H union {a,b} is a 49-set and must have alpha>=5. Hence at most five shell rows are bad and at least eight are good.
3. **Q33/d3 consequence.** The exact budget beta+X+G_B=3 gives g_b<=3, and k_b<=3, so t_b<=6 for every b in B. All ten B-rows therefore have independent-4 witnesses Q_b. If ab is a missing target edge, Q_b must intersect N_H(a); otherwise Q_b union {a,b} is an independent 6-set. The scalar budget guarantees at least five B-vertices with k_b>=2, so at least five witnesses hit at least two S-rows.

### Quantified impact
- New proved interface constraints: 1 theorem with 3 consequences.
- Open terminal contracts eliminated: **0**.
- E407 Q32 / E408 Q32/Q33 range: narrowed only by an added witness-incidence condition; no terminal exclusion claimed.
- Independent arithmetic check: exact values p_3(n)+floor(n/3)-1 versus D(n), n=40..47, all strictly exceed the cap (minimum gap 7 at n=40).
- GitHub commit: 020b64d5fdf3a4aa3abe66d86be3489565760b22 for the theorem file; follow-up state updates are being committed in this sequence.
- Next attack: turn the Q33 witness condition into a capacity contradiction using the four-unit core excess and seven-block near-Latin completion. Do not assume Q_b coincide or that aggregate defects vanish.


## 2026-10-24 — Round 3: independent certificate replay and witness-capacity cross-cut

### Replay
- Independently reran V11 SHA256SUMS and verify_kernel_certificate.py: 684 weight assignments, 349 outside-count states, 259 labelled shells, 252 Family-A and 7 Family-B states; no completed parent graphs claimed.
- Independently reran V12 SHA256SUMS and verify_q32_certificate.py: 8,677 weight vectors, 17,957 count states, 1,984 labelled shells; 90 D3/rho=1, 1,192 near-K12, 148 K9-pair-row screens; 554 remain OPEN under five rho=0 templates.
- Replay is COMPUTATION_CERTIFIED for finite coverage only, not a proof that the remaining templates have no parent completion.

### New theorem
Committed R12_WITNESS_CAPACITY_CROSSCUT.md:
1. Every independent 4-set in H hits at least three shell rows, using alpha(F)<=5 and omega(F)<=11.
2. The hub-hit set of Q_b contains every missing hub of b and covers M[S].
3. Every independent triple in H_b extends to an independent 4-set when t_b<=3; a nonextension for larger t_b requires t_b>=8-epsilon(X).
4. In E408 Q33, each exact-129 color has at least five no-S K5 components; any selected five labels have sum k_b>=7-beta; their Q sets are disjoint within a color and pairwise intersect at most one across colors.

### Impact
- New proved necessary-structure lemmas: 3.
- Open terminal contracts eliminated: 0.
- E407 Q32: finite state coverage is now independently replayed; same-core completion remains OPEN.
- E408 Q32/Q33: remains OPEN. Corrected arithmetic: Q32 gives e(H)=285 and excess6; Q33 gives e(H)=284 and excess4.
- No scalar-capacity contradiction is claimed: 40 Q sets contribute 160 core memberships, below the coarse 47*11=517 cap.
- Next attack: prove or disprove a labelled witness-packing incompatibility for the 284-edge core, while treating E408 Q32's 285-edge core separately.


## 2026-10-25 local continuation — Round 4: row-transversal theorem and high-k component packing

### New theorem file
Committed R12_ROW_TRANSVERSAL_AND_Q33_PACKING.md.

### Proof results
1. Re-established PAIR-13 and TRI-24 from the inherited R(3,35) / R(2,24) exclusions, with the exact contracts stated.
2. Proved the all-independent-4-set transversal theorem: for a missing shell edge ab, every independent 4-set in H\D_a hits D_b.
3. Specialized the theorem to all five E407 Q32 templates; full rows against t=10 hubs are 3-transversals, pair rows against t=11 hubs are 2-transversals, and singleton rows against t=12 hubs are 1-transversals. Added the applicable pair/triple row-overlap inequalities.
4. Strengthened exact-129 component packing: at least seven K5 components per color avoid S; since at most one can be the pivot-only component (five H vertices would violate alpha(H)<=4), at least six no-S components contain B.
5. Since the Q33/d3 exact budget forces at least five B rows with k_b>=2, every exact-129 color contains at least one high-k no-S component, and beta=0/1 gives at least two. Across >=8 exact-129 colors this yields >=8 / >=16 pairwise-linear Q witnesses, each hitting at least two S rows and three shell rows total.

### Impact
- New proved necessary-structure results: 2 theorem families (transversal + high-k packing).
- New E407/E408 terminal exclusions: 0.
- E407 Q32 same-284-core completion: OPEN.
- E408 Q32 threshold-29 exhaustive coverage: OPEN.
- E408 Q33 seven-block compatibility: OPEN.


### Exact count verifier
Added verify_row_transversal_counts.py (commit 3ee3d3213fec6136dea255a5cf5135bff0f9ab78) and ran it locally. All exact count checks passed:
- E407 A/B/C/D/E high-k minima: 6/8/6/7/5.
- Q33 beta 0/1/2/3 high-k minima: 6/6/5/5.
- Equality profiles are enumerated exactly, including the beta=3 profiles (0,5,0,5), (0,5,1,4), (1,4,0,5).
This verifies only the row-count arithmetic; the graph-theoretic terminal remains open.


### New theorem — E408 pairwise blocker compatibility (2026-10-24)

Added R12_E408_PAIRWISE_BLOCKER_COMPATIBILITY.md with an analytic proof and exact boundary cases.

- For any two vertices b,b' in the same outer target K12 block, their C-neighborhood blockers X_b,X_b' must leave no independent 11-set in R; otherwise b,b' extend it to an independent 13-set in the global exact-129 color C.
- If k isolated K5 components are fully covered by X_b∪X_b', then the remaining gadget must satisfy alpha(C[U\(X_b∪X_b')])<=k.
- Equality e_C(B_i,R)=62 is rigid: ten distinct exact K5 neighborhoods plus two six-subsets of U whose union is U and intersection has size one. This also proves exactly one duplicated core-to-block incidence.
- The exact global identity is sum_i(r_i(C)-1)=55-P_C. If P_C=55, all seven blocks are rigid equality cases and each isolated K5 component plus its seven representatives is a C-clique of size 12.
- Since sum_C P_C=252, at most four colors can have P_C=55; at least four of the at least eight exact-129 colors therefore have a strict-slack block.

### Impact and status firewall

- New proved local/global compatibility constraints: 1 theorem, 1 rigid equality characterization, 1 exact slack identity.
- Newly eliminated terminal contracts: 0.
- E408 Q32/Q33 remains OPEN; no scalar identity is treated as a contradiction.
- Next attack: classify allowed strict-slack neighborhood families under the per-core-vertex multiplicity cap 2, then intersect their block-pair extra-matchings with the seven-block duplicate ledger.


### Cross-branch audit + pair-indexed zero-excess theorem (2026-10-25)

- Read and reconciled latest sibling heads: emergency sprint 87a5842, emergency sprint chat 5258c5f, witness packing 38b5dce, zero-excess witness 8addc64, general-r architecture a922c4d, asymptotic fa6a5f2, and adversarial audit 7ea44fc. Sibling workstreams were not overwritten.
- Independently recomputed all ten endpoint gaps in the robust zero-excess theorem; exact gaps are 30,22,14,5 and 44,38,31,23,15,6.
- Proved the pair-indexed hub-cover strengthening: each pair of regular B rows in the 284-edge core has a common zero-excess independent-four witness; when the pair's missing-hub sets cover S, that witness must be hub-complete.
- Exact labelled pair floors: A/C=39, B=17, D/E with full row=9; E with no full row has 45 endpoint-complete pair certificates. The arithmetic verifier checks these floors.
- Audited exact-129 witness packing: preserve 7/8 total Q-set floors and support bounds v≥29/v≥31, but distinguish the possible pivot-containing {p}∪Q component from B-labelled {b}∪Q witnesses. Corrected safe global hub-complete labelled floors are A/B=21 each, C/D/E-full=28 each, and E-no-full endpoint-complete=49.
- No terminal excluded. E407 Q32, E408 Q32/Q33, and original K145 bridge remain OPEN / NOT_CERTIFIED.
