# Progress log — E408 global incidence / witness capacity -> fixed-r=12 root closure

## 2026-10-26 — intake and Q33 local repairs

- Created isolated branch `workstream/r12-twochat-e408-global-20261026`.
- Audited Q33/Q32/unified witness-capacity sibling heads; siblings remain read-only.
- Replayed the Q33 `(6,2,1^5)` verifier: 571,394 cases, zero failures.
- Repaired and excluded `(7,1^6)` conditionally.
- Identified the two locally open all-component-edge-present P49 profiles `(4,4,1^5)` and `(4,3,2,1^4)`.

## 2026-10-27 — Q33 global bypass

- Excluded m=10 exact-129 colors in the Q33 31-point/56-witness terminal.
- Established h<=4 selected gadget witnesses.
- Proved
  `26(11-m)<=delta+6h<=41`.
- Remaining m=9 and m=8 require52 and78 U-edges respectively. Contradiction.
- Registered Q33 terminal closed without proving the two remaining local P49 profiles individually.

Key commit: `5328f7ac5302836f96f4a24cefdbef748dc9c9ed`.

## 2026-10-27 — historical Q32 closure later retracted

A former branch state claimed an exact-color-count closure of Q32 and then promoted E408/the fixed-r root. That route used a supposed universal color-degree9 exceptional vertex in the Kang--Pikhurko exact-129 Type-I cell.

**2026-10-28 primary-source correction:** the source gadget has variable degrees `(4+a,9-a)`, `a=1,2,3,4`, so no degree9 vertex exists. Accordingly:

- the former Q32 exact-color-count closure is RETRACTED;
- the whole-layer E408 promotion based on it is RETRACTED;
- the corresponding fixed-r root promotion is RETRACTED;
- Q33 and E407 closures that do not use degree9 remain available under their named inputs.

Historical commits remain in the repository for audit but are not load-bearing.

## 2026-10-27 — E407 Q31/Q32 audit remains valid

### Q31
Original V10/V11 packages were independently replayed; the common-K10 support theorem excludes the finite families under the registered inputs.

### Q32
The registered terminal has U of size29 and49 selected independent four-blocks in seven exact colors. The blocks own294 distinct non-target U-edges. At least one unselected non-target color D remains and needs

`e_D(U)>=p_12(29)=22`.

But `e(bar(H[U]))<=310`, so `294+22=316>310`. This short closure is independent of the retracted degree9 premise.

## 2026-10-28 — Q32 reopened with source-correct 285-edge contract

Frozen live contract:

- `|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`;
- total core degree excess6;
- `q=32`, `22<=e(M)<=32`, `e(M)+G_A=32`;
- exact-color count `m in {8,9,10}`;
- at least ten disjoint core-four witnesses per exact color;
- pairwise linearity across colors;
- witness support `|U|>=44`.

Corrected non-full-support multiplicity gives `n_w>=m-6`. In Case I, matching capacity strengthens this to `n_w>=m-3` and closes v=44,45.

## 2026-10-28 — source-correct v=44,m=9 shell floor

For W of size3 and m=9, all nine special exact vertices lie in W, three labels per W-point, and at most one exact color is triple-outside.

Using the actual Type-I gadget:

- t=0 all-double gives `e(M)>=25`, `G_A<=7`;
- t=1 gives `e(M)>=28`, `G_A<=4`, plus at least two core-excess units on W.

Commit at intake HEAD: `271024a8db3cd41817cdad6ec2c8b92815be2dc9`.

## 2026-10-28 — new all-color U-reserve theorem

Added `Q32_U_COLOR_RESERVE.md`.

For an exact color on U containing ten disjoint witness K4s, with `alpha<=12`, `omega<=4`:

- v=44: `e_C(U)>=62`, stronger than ordinary `p_12(44)=60`;
- v=45: `e_C(U)>=64`, stronger than ordinary63;
- v=46: at least66;
- v=47: at least69.

At v=44 the 61-edge layer is excluded by splitting the complement into non-12-partite (Brouwer) and 12-partite cases; in the latter, part-size/cross-edge counting shows at most nine disjoint K4s. At v=45, Turan equality contains only nine K4s.

If h exact colors provide at least eleven witnesses:

- v=44: `e(bar(H[U]))>=660+2m+4h`;
- v=45: `e(bar(H[U]))>=693+m+2h`.

This is a true multicolor reserve coupling, not an UNSAT certificate.

Commit: `cbfa7eebcbb4300b441a8e827e50a033cd598d3f`.

## 2026-10-28 — stale Q32 closure and firewall repaired

- `Q32_CORE285_TERMINAL.md` was rewritten from the stale degree9-based CLOSED claim to the current OPEN source-correct 285-edge terminal.
- `CONTRACT_FIREWALL.md` was corrected so the valid KP degree pairs and Q32/Q33 separation are explicit.

Commits:
- `56d7ea9979b35c002a294aafb5bcf88d397d59be`;
- `4dfbaa35a0f4ce9668ba959b9c97b126df309df7`.

## 2026-10-28 — 131-edge minimum degree three

Added `Q32_131_MINDEG3_V46_M9_CLOSURE.md`.

For a 61-point non-target color C with

`e(C)=131`, `alpha(C)<=12`, `omega(C)<=5`,

proved

`delta(C)>=3`.

If a degree-two vertex existed, its 58-point non-neighborhood would have `alpha<=11`, `omega<=5`; Brouwer forces at least129 internal edges. Together with the two incident edges this exhausts all131 edges and forces both neighbors to have degree one. A second non-neighborhood argument at order59 gives at least135 total edges from a degree-one vertex, contradiction.

Therefore the correct m=9 nonexact pointwise floor is

`L_9=3+3=6`,

not5.

### Consequence: Case I / v=46 / m=9 CLOSED

At the unique W-point, Case I gives `n_w>=6`. Hence the target contributes at least13, the nine exact colors at least `36+6=42`, and the 130/131 pair at least6, for a total at least61>60.

Thus this formerly live rigid equality terminal is empty.

Commit: `cfda84c31c5155676b9cd352f314e90075be6f84`.

## 2026-10-28 — canonical frontier synchronized

`CANONICAL_STATE.md` now records:

### Case I
- v=44 closed;
- v=45 closed;
- v=46,m=10 closed;
- v=46,m=9 **closed** by the new 131-edge theorem;
- v=46,m=8 open (`n_w=5 or6`);
- v=47 open.

### Case II
- v=44,m=10 closed;
- v=44,m=9 open, but with three special labels per W-point and t=0/1 shell floors;
- v=44,m=8 open;
- v=45,46,47 open.

For m=9, every W-point now has only two total degree-slack units over the baseline `13+39+6=58`. If its three special Type-I source parameters are `a_1,a_2,a_3`, then

`sum(4-a_i)<=2`, hence `a_1+a_2+a_3>=10`.

The only sorted parameter triples are

`(4,4,4)`, `(4,4,3)`, `(4,4,2)`, `(4,3,3)`.

Canonical commit: `b2d06bb90e532556ba203f559d85d8fcfb257fd4`.

## Current status

`E408 Q33`: closed under its registered 284-edge global reserve contract.

`E408 Q32`: **OPEN**, but the Case-I frontier has been reduced to `v=46,m=8` and `v=47`; the main low-support Case-II frontier is `v=44,m=9` / `m=8` plus larger supports.

`EG617(r=12)`: **OPEN / NOT_CERTIFIED** until the source-correct Q32 terminal and every dependency in the final chosen DAG are closed/audited.


## 2026-10-29 — root-promotion fail-closed audit

- Re-read actual target branch HEAD 937a905ed26e54ec10e9bdade1d9b655da8f6176 and the current root/dependency files.
- Searched all 30 repository branch trees for the V12 archive, matching manifest, verifier, and V12-named certificate artifacts. None were found. The only V12-named file was consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md, which explicitly states SOURCE_REPORTED / INDEPENDENT_REPLAY_PENDING. GitHub releases count is 0; commits for exact path T61_H13_V12.zip count is 0.
- Re-read the latest dedicated E407 sibling at 0192807d1f3b2193aa65c25b9f671b36821aaded. FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md, OPEN_CONTRACTS.md, and PROOF_DEPENDENCY_AUDIT.md remain OPEN / NOT_CERTIFIED. The local 29-point/49-block arithmetic is sound, but promotion to all E407 parents remains OPEN.
- Re-read the Q33 nonexact-U reserve and support theorem. The former is conditional on the exact 31-point/56-witness contract; the latter proves lower support, not equality at 31. Larger-support parent coverage remains OPEN.
- Independently executed verify_q33_high_support_u_reserve.py in a clean standard-library process with command python -S -B /mnt/data/verify_q33_high_support_u_reserve.py; exit code 0, no stderr, SHA256 9a47974a1e5ac461caa5313e6551b73765a1954102e83ff59ffd540d8851ee66. It certifies arithmetic only, not graph realization or parent coverage.
- Added ROOT_DEPENDENCY_DAG.md, ROOT_AUDIT_INPUT_MANIFEST.json, ROOT_AUDIT_REPLAY_LOG.md, Q33_HIGH_SUPPORT_U_RESERVE_AUDIT.md, and verify_q33_high_support_u_reserve.py. Updated this workstream's canonical state, dependency audit, root receipt, and historical root-audit supersession notice. No sibling workstream was modified.
- Root status remains OPEN / NOT_CERTIFIED. No promotable receipt is issued.


## 2026-10-29 — dependency-edge precision correction

- Distinguished the conditional template-local 29-point/49-block support/anchor interface from the missing V12 finite-survivor-to-template mapping. The former is recorded in the E407 sibling under the registered minimum-support and exact-129 assumptions; the latter remains OPEN because the V12 archive, manifest, and verifier are unavailable.
- Updated the dependency DAG and root-facing summaries to avoid conflating the two edges. Root status remains OPEN / NOT_CERTIFIED.


## 2026-10-29 — audit artifact integrity and historical V12 claim correction

- Rewrote Sections 8–10 of the historical root-promotion audit to distinguish the conditional template-local support contract from the unverified finite V12 survivor mapping.
- Corrected ROOT_AUDIT_INPUT_MANIFEST.json so it distinguishes pre-audit source blobs from committed output blobs, records the audit commits, and includes the selected-support anchor-identity source.
- No mathematical closure status changed: V12 parent mapping OPEN, Q33 high-support promotion OPEN, Q32 OPEN, root OPEN / NOT_CERTIFIED.


## 2026-10-29 — replay command provenance correction

- Clarified that the clean-process verifier run executed against the local runtime copy at /mnt/data/verify_q33_high_support_u_reserve.py. The committed GitHub file was created from the same source text and has the recorded SHA256; no claim is made that a repository checkout was available locally.


## 2026-10-29 — source-correct Q32 support-layer reconciliation

- Read-only audited the latest low-support sibling at \`9afd7c1a59056052974f9dc78933010d10e88bba\` and high-support sibling at \`92c9086c8b6ac554ed74b48a5d608aa546bcb977\`.
- Imported the conditional closures of all non-full support rows \(v=44,45,46\) for \(m=8,9,10\), with proof references and blob IDs recorded in Q32_NONFULL_SUPPORT_SIBLING_IMPORT_AUDIT.md.
- Refined the full-support frontier: \(v=47,m=8,9\) remain open; \(m=10\) has its \(\chi(\overline{H[R]})\ge5\) residual subcase closed, while \(\chi(\overline{H[R]})\le4\) remains open.
- Updated the canonical state, Q32 terminal, dependency audit, DAG, and root receipt. Sibling branches were read-only and unchanged.
- No root promotion: EG617(r=12) remains OPEN / NOT_CERTIFIED; E407 V12 parent coverage and Q33 support promotion are also OPEN.


## 2026-10-29 — full-support CSP contract audit

- Read the latest high-support sibling at HEAD 92c9086c8b6ac554ed74b48a5d608aa546bcb977, including Q32_FULLSUPPORT_VERTEX_LABELLED_CSP.md, q32_fullsupport_vertex_labelled_csp.py, and verify_q32_fullsupport_candidate.py.
- Found an E408 count-vector mismatch: the code fixes e_0=398+m, colors 1..m at 129, colors m+1..10 at 130, and color 11 at 132. This gives target count 406 for m=8 and 407 for m=9, whereas E408 requires 408 and sum s_C=3 for all m. Correct E408 vectors are m=8: three 130-edge colors; m=9: one 130-edge and one 131-edge color; m=10: one 132-edge color.
- Found the independent verifier forces every factor 0–9 to have exactly one O-vertex, contradicting the source-correct outside-count normal form that allows surplus outside incidences in isolated factors.
- Recorded both defects in Q32_FULLSUPPORT_CSP_SOURCE_AUDIT.md. No solver run or UNSAT result was claimed by the sibling; no sibling file was changed.
- Full-support Q32 remains OPEN / NOT_CERTIFIED; E407 V12 parent coverage and Q33 support promotion also remain OPEN.


## 2026-10-29 — follow-up audit of latest sibling CSP revision

The high-support sibling advanced to HEAD 92c9086c8b6ac554ed74b48a5d608aa546bcb977 and integrated pivot K4 packing into the CSP. I re-read the updated model and confirmed the E408 count-vector mismatch remains in expected_total, while the candidate verifier still uses the old expected_counts and forces comps[0:10] to have exactly one O-vertex. The root audit now pins this latest source version. No solver result is imported.


## 2026-10-29 — refreshed full-support CSP source audit at sibling HEAD 384b314

- Re-fetched the live high-support sibling branch and confirmed its actual HEAD is 384b31478668ebccde32f13a9ae391bbff494c86, newer than the prior root audit's pinned 92c9086c8b6ac554ed74b48a5d608aa546bcb977.
- The latest candidate verifier now uses source_outside_profile_errors and source-profile regression fixtures; the old blanket requirement that factors 0..9 each have exactly one O vertex is no longer present. Defect B is closed at the source-check level.
- Defect A persists in both model and independent candidate verifier: expected target count remains 398+m and color 11 remains fixed at 132. This is incompatible with E408 for m=8,9.
- Added verify_q32_fullsupport_count_vector_contract.py and ran it in a clean standard-library process. All three corrected vectors pass: m=8 has 8×129 plus 3×130 and target 408; m=9 has 9×129, 130, 131 and target 408; m=10 has 10×129 plus 132 and target 408. Each sums to C(61,2)=1830.
- No Z3 solve was performed in this runtime (z3-solver is not installed); no SAT/UNSAT claim is made. Q32 full support and the fixed-r root remain OPEN / NOT_CERTIFIED.


## 2026-10-29 — latest full-support CSP recheck at sibling HEAD c6500b24

- The high-support sibling advanced beyond 384b314 to c6500b24dc78cd4c56cd90219080003aeb8e3cb5, with intervening commits hardening malformed candidate witnesses and wiring the monochromatic-K6 separator into the model.
- The latest model and independent verifier still encode target count 398+m, with color 11 fixed at 132. The count-vector defect therefore remains for m=8,9.
- Current source blobs: model 03e4d2ce98ab399ffafa53af016efd3c434150bc; verifier 5708b7541b44cfc46bd82cf3d50b1e350472617b; CSP specification 4f73ca96eb43512e94c72f05266462ba949eead4.
- The verifier's source-outside-profile check remains corrected. The K6 separator and malformed-witness checks are useful model hardening, but no full Z3 solve or independently replayed UNSAT proof has been reported.
- The standalone count-vector regression remains PASS for the correct vectors only. Root status remains OPEN / NOT_CERTIFIED.


## 2026-10-30 — latest sibling refresh and z=3 dual-fiber switch-cost theorem

### Current source state

- Re-fetched high-support sibling branch workstream/r12-q32-highsupport-root-20261028 at HEAD 1de8a37556ba98ccbb8651f39a5192629453f0f1.
- The old count-vector mismatch reported by this root branch is superseded. The current model imports expected_color_counts(m) from the independent verifier; both encode target count 408 for every m, with nonexact excess vectors (130,130,130), (130,131), and (132) for m=8,9,10 respectively.
- The source-mode outside-profile correction, malformed-witness guard, and complement-dual K6 separator are present in the latest source.
- The full-support CSP remains FORMULATION ADDED / execution and proof replay pending. This runtime has no z3, ortools, or pysat; no full CSP solve or SAT/UNSAT claim is made.

### Exact z=3 partition-pair enumeration

- Added Q32_Z3_DUAL_FIBER_SWITCH_COST_AUDIT.md and verify_q32_z3_dual_fiber_switch_cost.py under this root workstream only.
- Enumerated every four-labelled clique partition F and G of each of the six registered seven-vertex residual graph types, and all 13 local common-label multisets (one aligned pattern plus 12 synchronized-switch patterns).
- Replayed 91,584 ordered labelled partition pairs. The exact minimum incidence-mismatch cost is zero for 23,040 pairs; 16,704 of these have F=G as unlabelled partitions. The only 6,336 zero-cost mismatches are the three profile cases recorded in the audit.
- Analytically, for every no-double-track outer block D, y_D >= eta_D. A positive eta costs at least one unit, so sum_D y_D=2 leaves at most two positive-eta blocks. The endpoint-load cap allows at most five zero-cost switches; hence exactly five zero-cost switches and two positive blocks.
- Each zero-cost switch duplicates the unique empty small-map fiber s and omits the unique split fiber j. Five such switches saturate e_i(s)<=5 in each small block, consuming both endpoint-load slack units. Therefore the two positive blocks cannot be switches; they are aligned and have y_D=eta_D=1.
- The outer weighted-heavy graph has weighted degree 2-y_D, so the two aligned blocks are exactly the endpoints of its unique path component. The five other blocks are degree-two switch blocks.
- The mismatch branch is narrowed to a five-switch/two-aligned-endpoint normal form, not closed. Double-track cases, the aligned F=G branch, the other m=10 cells, and full-support m=8,9 remain OPEN / NOT_CERTIFIED.


## 2026-10-30 — pointwise switch-partner blocker closes z=3 no-double-track mismatch

- Revisited the five-switch/two-aligned-endpoint normal form using the exact normalized 4,5,5 switch, rather than only the common-label incidence lower bound.
- In the synchronized 3+7 switch, normalize the three small-to-outer base matchings as A-D=id, B-D=id, C-D=(s j), with extra edges A_sD_j, B_sD_j, C_sD_s. The outer vertex q=D_j has k(q)=2 extra small-component incidences, common label s, and label j in both A and B.
- Every r in F_j is adjacent to A_j and B_j, so q is adjacent to all of F_j; it is also adjacent to all of F_s. Hence d_R(q)>=n_s+n_j. But e_Q(q)>=k(q)=2 and e_Q(q)+d_R(q)=3, so d_R(q)<=1. Therefore every synchronized switch must satisfy n_s+n_j<=1.
- The three nontrivial zero-cost F/G mismatch profiles from the 91,584-pair enumeration have partner fiber sizes 3, 2, and 3 respectively, with duplicated fiber empty. All violate the pointwise bound. Thus F!=G is impossible in the no-double-track z=3 branch.
- If F=G, a switch can only transpose an empty fiber with a singleton fiber; among the registered profiles this occurs only in (3,3,1,0), where a size-three fiber is fixed by the transposition and produces a forbidden K13. Profiles (3,2,2,0) and (3,2,1,1) have no allowed switch and also produce K13.
- Result: the no-double-track m=10, 3+7, z=3 branch is reduced to F=G with profile (2,2,2,1), and every outer block aligned. This is a substantial reduction, not a full z=3 or Q32 closure. Double-track and aligned-2221 branches remain open.
- Added Q32_Z3_SWITCH_PARTNER_DEGREE_BLOCKER.md and its 12-case normalized switch verifier. The existing five-switch endpoint-saturation result is retained as an intermediate audit, now superseded by this stronger pointwise contradiction for F/G mismatch.
