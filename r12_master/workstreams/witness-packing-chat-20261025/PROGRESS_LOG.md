# Progress log — R12 witness-packing line

## 2026-10-25 — initial witness-packing theorem

- Inspected the repository's fixed-r=12 emergency, ultimate-closure, master-closure, and zero-excess branches.
- Proved a labelled witness-packing support theorem from exact-129 K5 components: at least seven independent Q-sets per exact-129 color (including a possible p+Q component), pairwise-linear across colors.
- Derived the Turán support floor v>=29 for E407 Q32 and v>=31 for E408 Q33; identified the remaining exact color profiles.
- Published initial theorem at commit c6b4c81dd7899835c08b3c2e701b762ec4fb2148, then moved the substantive artifact to the isolated workstream branch.

## 2026-10-25 — live cross-branch reconciliation and correction

- Read latest emergency head 87a58429070cffbd90991045e0375102fcc4ec0d, ultimate head 28f47fb7c8f273e6a70bf19f4ee961e8023f5981, zero-excess head 95255a82f126fadbc8834c799df1374e5fc86fca, and master-closure head e46da35aedce7bbaaf11756b50192bd157956239. Also checked general-r/Astra branch status; these remain separate contracts and were not imported as fixed-r=12 theorems.
- Corrected the count distinction: at least seven total Q-sets but only six guaranteed B-labelled Q-sets per exact-129 color.
- Combined the six disjoint B-labelled witnesses with total core excess four to prove at least two zero-excess B-labelled witnesses per exact-129 color, hence at least 14 in E407 and 16 in E408 Q33.
- Imported the Q33 high-k packing and the outer-block blocker-occurrence inequality with notation kept separate.
- Audited the emergency witness-star proof: the second-Turán step forces tripartiteness, not completeness. Recorded the precise gap and the corrected local structural conclusion without claiming the full core theorem is false.
- Added verify_witness_packing.py; the standard-library arithmetic verifier was independently run and all assertions passed.
- Added CROSS_BRANCH_SYNC_20261025.md and CANONICAL_STATE.md.

## Current status

**EG617(r=12): OPEN / NOT_CERTIFIED.**

Next mathematical target: classify the E407 v=29 / 49-witness and E408 Q33 v=31 / 56-witness boundary kernels with actual shell-row incidence and core degree/excess constraints. Scalar overlap bounds alone are insufficient.


## 2026-10-25 — shell-incidence union theorem

- Derived the exact identity e(A,H)=32+e(M) for E407 Q32, then the duplicate shell-incidence budget \(\sum_{x\in H}(d_F(x,A)-1)=e(M)-15\).
- Proved \(|\cup_{b\in B_3}D_b|\ge15-\beta-c_{\rm rest}\) for the full-row supports. Under the retained V12 row profiles, this gives at least 11 distinct core vertices in template A and at least 10 in template C.
- This rules out the all-full-rows/same-three-core-neighbours escape without assuming row supports are disjoint. It does not close partial-overlap configurations.
- Added the arithmetic checks to verify_witness_packing.py and reran the full assertion set successfully.
- New proof asset: SHELL_INCIDENCE_UNION_LEMMA.md; commit 73d8882b3d923c3d2406b215580d0cbc4f922c47.
- Verifier update: commit 1bf54e51ddd6860ec800afe1f22fd7d41d85594e.


## 2026-10-25 — transversal boundary audit and live branch refresh

- Re-read latest ultimate-closure head 78c30e86b0f432464ca5375695da97a27b230878 and zero-excess head f3c9ef6b3a4bfadad4f70a16bb0e7c6434bb0777 after branch heads advanced.
- Independently verified the linear-family transversal bound tau(Q)>=7 for (v,m)=(29,49) and (31,56), giving at least seven core cross-neighbours for every vertex outside the witness support.
- Recomputed exact E407 and E408 boundary budgets. E407 has delta+epsilon_U<=16 and epsilon_U+2delta>=2; E408 has delta+epsilon_U<=17.
- Found the latest boundary note again infers non-four-partiteness from ruling out complete four-partiteness. Corrected the logical scope: a near-complete four-partite design-like branch remains possible; Brouwer's non-partite bound applies only conditionally.
- Imported pair-indexed zero-excess common witnesses and the high-support exact-129 dichotomy, preserving the distinction between labelled pair certificates and distinct witness sets.
- Flagged an unsupported stronger component-count claim for templates C/D/E; retained only the universally proved six B-labelled component count.
- Added TRANSVERSAL_BOUNDARY_AUDIT.md and extended the standard-library verifier; all arithmetic assertions passed.

Current status: **OPEN / NOT_CERTIFIED**.


## 2026-10-25 — universal E408 Q33 S0=10 exclusion

- Refreshed live branch heads: emergency ad56a91c644458cb16dd590b7a4ed0e800978a81, ultimate closure 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40, zero-excess 98167ec779850a2ff57b1ec7113f939df42c35f4, master closure e46da35aedce7bbaaf11756b50192bd157956239.
- Proved a universal capacity bound for the E408 Q33 v=31 / 56-witness boundary: any 7-transversal T is a K7, there is at most one such T, and at most four W-vertices can have U-neighbourhood T. Thus N7<=4 and S0>=10.
- Excluded S0=10 without a four-partite assumption. Equality forces four degree-seven W vertices with a common K7 neighbourhood, twelve degree-eight vertices, exactly two T-type neighbourhoods, and ten R-only eight-set neighbourhoods. Their distinct-set intersection bound and multiplicity ledger force three disjoint sets with multiplicities (4,3,3); alpha(H)<=4 makes each set and its corresponding W group a clique, yielding K12, contrary to omega(H)<=11.
- Added R12_E408_Q33_UNIVERSAL_S0_11.md and verify_e408_q33_universal_s0_11.py. The verifier was executed locally and returned E408_Q33_UNIVERSAL_S0_11_ARITHMETIC_OK; it checks arithmetic/case tables only, not the graph-theoretic proof.
- Cross-audited and corrected this line's earlier shell-incidence union lemma: the exact identity is valid, but its original 11/10 support-union floors omitted up to four zero-shell-support core vertices. The safe floors are 7/6. Updated SHELL_INCIDENCE_UNION_LEMMA.md and verify_witness_packing.py; retracted the stronger unsupported numerical claim.
- This theorem is conditional on the retained T61 / exact-129 / Q33 shell contract. The full E408 Q33 terminal, E407 Q32, E408 Q32, and original K145 theorem remain OPEN / NOT_CERTIFIED.


## 2026-10-25 — third live sibling refresh

- Read emergency head 70d050655f0d03c38f3fef40c4a9f936e9ed1463 and zero-excess head c1604037ab9045543dcb0bad805a37459b907906; checked the general-r architecture/asymptotic heads remained a922c4d7646eb8d0087bde8547562c8aace02ee2 and fa6a5f2b8b5d2a0fe821d50a4421884a69dc5366.
- Imported the latest conditional result: the four-partite E408 Q33 minimum-support branch also excludes S0=11, giving S0>=12 if L is four-partite. This line's universal theorem only guarantees S0>=11; the non-four-partite S0=11 branch is still open.
- Corrected the E407 branch ledger after the zero-excess audit withdrew the distinguished-unused-point / TD(4,7) claim. Retained only the valid E407 inequalities delta>=2, delta+epsilon_U<=16, epsilon_U+2delta>=2.
- Updated CROSS_BRANCH_SYNC_20261025.md with exact current sibling heads and the combined frontier.
- No full E407/E408 terminal or original K145 theorem is closed.


## 2026-10-25 — universal E408 Q33 S0=11 exclusion

- Extended the prior universal S0>=11 boundary theorem to prove S0>=12 without a four-partite assumption; added R12_E408_Q33_UNIVERSAL_S0_12.md and verify_e408_q33_universal_s0_12.py.
- Under S0=11, the cross-edge sum is 125 and N7 is either 3 or 4. The N7=3 profile forces 13 degree-eight W-neighbourhoods, exactly three T-type and ten R-only. The N7=4 profile forces eleven degree-eight neighbourhoods and one degree-nine neighbourhood; exact T-incidence leaves only b=7,1,0 cases.
- In every case, the special-incidence ledger leaves at most one uncovered R-point. The linear 8-set family then has exactly three distinct sets partitioning R. Multiplicity cases either violate special-incidence capacity, yield a K12, or force the degree-nine neighbourhood to equal/contain one partition part and then create a K12.
- Executed the arithmetic verifier locally: E408_Q33_UNIVERSAL_S0_12_ARITHMETIC_OK. It verifies arithmetic/profile tables only, not the graph-theoretic argument.
- Latest fixed-r=12 sibling refresh also found: E407 Q32 minimum-support bound strengthened to epsilon_U+2delta>=9 and delta>=3 (emergency head f4c3b06891d29238d4f9cca2588f442004b6dc97); E407 |W|=23 Cell-B completion is empty relative to the stated Brouwer/Kang–Pikhurko and saturation inputs (branch workstream/r12-e407-q32-terminal head 3f42fcce5761ca2372140618adda56f95fcbe253).
- E408 Q33 minimum-support ledger is now S0>=12 and delta+epsilon_U<=17. It still does not eliminate S0>=12 or larger support sizes. E407 Q32 common-core completion, E408 Q32, the T61-to-K145 bridge, and EG617(r=12) remain OPEN / NOT_CERTIFIED.
