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

- Read-only audited the latest low-support sibling at \`9afd7c1a59056052974f9dc78933010d10e88bba\` and high-support sibling at \`07c69f6b4b748124ea0cf72eb1dc39bc57df6a29\`.
- Imported the conditional closures of all non-full support rows \(v=44,45,46\) for \(m=8,9,10\), with proof references and blob IDs recorded in Q32_NONFULL_SUPPORT_SIBLING_IMPORT_AUDIT.md.
- Refined the full-support frontier: \(v=47,m=8,9\) remain open; \(m=10\) has its \(\chi(\overline{H[R]})\ge5\) residual subcase closed, while \(\chi(\overline{H[R]})\le4\) remains open.
- Updated the canonical state, Q32 terminal, dependency audit, DAG, and root receipt. Sibling branches were read-only and unchanged.
- No root promotion: EG617(r=12) remains OPEN / NOT_CERTIFIED; E407 V12 parent coverage and Q33 support promotion are also OPEN.
