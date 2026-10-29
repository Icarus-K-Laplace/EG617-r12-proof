# Dependency audit — fixed r=12 after KP source correction

Updated: 2026-10-29  
Status: **EG617(r=12) OPEN / NOT_CERTIFIED. Live graph terminal: E408-Q32. Additional root-promotion gates: E407-Q32 V12 parent coverage OPEN; E408-Q33 support promotion OPEN.**

## 1. Source correction and retraction boundary

Primary-source verification of Kang--Pikhurko `(61,12)` confirms the exact-129 Type-I factorization but refutes the former project claim of a universal color-degree9 exceptional vertex.

The source-correct degree pairs are

`(4+a,9-a)`, `a in {1,2,3,4}`,

namely `(5,8),(6,7),(7,6),(8,5)`.

Therefore any Q32 theorem whose contradiction requires degree9 exceptional-vertex injectivity is retracted. In particular the following are not load-bearing closure nodes:

- `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
- `Q32_EXACT_COLOR_COUNT_COLLAPSE.md` as a whole;
- the injectivity step of `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md`;
- the Q32 part of the historical E408 whole-layer closure/root promotion.

The source-verified factorization `10 isolated K5 dot-union G11` remains valid and is used only through explicitly audited consequences.

## 2. Root/front-end boundary

The Line-A recurrence remains computation-certified at 1,752 nodes and 144 outer comparisons under its registered inputs. The contextual `R(4,49)` alternative remains closed under its named extremal inputs.

Relative to their registered contracts, the following T61 branches remain closed:

- h12;
- h13 E397--E406;
- E407 Q31;
- E407 Q32 local 29-point reserve only (parent mapping OPEN);
- E408 Q31.

Thus the live E408 charges are Q32/Q33 before the color-incidence arguments below.

## 3. E407 firewall — local contradiction versus parent coverage

The local reserve arithmetic is valid under the frozen contract: 49 selected independent four-blocks own 294 distinct complement edges; one unselected non-target color needs at least p_12(29)=22; and the registered ledger gives e(L_U)<=310. Thus 294+22=316>310. This route does not use the retracted degree-nine premise.

However, the V12 source report remains SOURCE_REPORTED / INDEPENDENT_REPLAY_PENDING. The reported archive, manifest, and verifier are absent from all 30 searched branch trees and from GitHub releases; the exact archive path has no commit history. The template-local 29-point/49-block support and selected-component anchor identity are recorded as PROVED_CONDITIONAL under the registered minimum-support and exact-129 inputs in FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md and SUPPORT_BLOCK_ANCHOR_IDENTITY.md. What remains OPEN is the composite edge from every legal parent through the complete V12 finite screen to one of templates A-E; the absent archive prevents independent replay of the reported survivor-to-template mapping. The broader same-core compatibility workstream remains OPEN but is not needed for the local reserve contradiction if that parent mapping is established.

## 4. Q33 — local P_C=49 profile status

This is the independent 284-edge / excess-four contract.

At `P_C=49`, the four profiles singled out for the emergency sprint now have status:

- `(6,2,1^5)`: **PROVED_CONDITIONAL excluded** by the audited double-star theorem;
- `(7,1^6)`: **PROVED_CONDITIONAL excluded** by `Q33_P49_R7_DOUBLE_STAR_EXCLUSION.md`;
- `(4,4,1^5)`: **OPEN locally** only in the branch where all ten relevant component-representative edges are present;
- `(4,3,2,1^4)`: **OPEN locally** only in the analogous all-component-edge-present branch.

The two remaining local branches are genuine: the current double-star/blocker arguments are triggered by a missing component-representative edge. When all ten are present, the valid monochromatic-K12 star rule gives only

`d_C(z,K12)<=1`,

so a single external same-color edge is legal. The historical stronger isolation claim was false. Consequently **`P_C<=48` is not proved** and must not be used.

## 5. Q33 — exact 31-point local closure bypass; parent support promotion OPEN

The local P49 gap is not load-bearing for the registered Q33 terminal.

The valid global route is:

1. `Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md` excludes `m=10` without degree9;
2. in the 31-point/56-witness terminal, let `h` be the number of selected gadget witnesses;
3. selected exact-color component witnesses occupy `336-6h` edges of `L=bar(H[U])`, whose total size is `336+delta`;
4. every nonexact color needs at least `p_12(31)=26` U-edges;
5. hence

   `26(11-m)<=delta+6h`.

With `m in {8,9}`, `delta<=17`, and `h<=4`, the right side is at most41 while the left side is78 or52.

Therefore only the registered 284-edge, exact 31-point / 56-witness Q33 terminal is PROVED_CONDITIONAL impossible by Q33_NONEXACT_U_RESERVE_CLOSURE.md, independently of the two open local P49 profiles. The upstream support theorem establishes a lower bound |U|>=31, not equality. No complete support-promotion theorem for v=32,...,47 was located. The high-support scalar audit excludes m=8 at v=32 only; it does not close m=9,10 at v=32 or m=8,9,10 at v>=33. Global E408 Q33 parent closure remains OPEN.

No Q33 identity is imported into Q32.

## 6. Frozen Q32 285-edge contract

For E408-Q32:

- `|H|=47`, `e(H)=285`;
- `alpha(H)<=4`, `delta(H)>=12`;
- `sum_H(d_H-12)=6`;
- `q=32`, `22<=e(M)<=32`, `e(M)+G_A=32`;
- exact-color count `m in {8,9,10}`;
- every exact-129 color supplies at least ten disjoint independent core-four witnesses;
- different exact-color witness families are pairwise linear;
- their support U satisfies `|U|>=44`.

The corrected non-full-support theorem gives, for `w in W=H\U`,

`n_w>=m-6`,

and hence `|W|(m-6)<=m`.

## 7. New Q32 all-color U-reserve theorem

`Q32_U_COLOR_RESERVE.md` is a new valid dependency.

For any exact color on U containing ten disjoint witness K4s:

| v=|U| | ordinary `p_12(v)` | exact-color floor |
|---:|---:|---:|
|44|60|**62**|
|45|63|**64**|
|46|66|66|
|47|69|69|

At v=44, the 60-edge Turan equality layer has only eight disjoint K4s. The 61-edge layer is excluded by a non-12-partite Brouwer branch or, if the complement is 12-partite, by direct part-size/cross-edge counting. At v=45, equality has only nine disjoint K4s.

If `h` exact colors supply at least eleven witnesses, then

- v=44: `e(bar(H[U]))>=660+2m+4h`;
- v=45: `e(bar(H[U]))>=693+m+2h`.

These are necessary reserve inequalities, not complete contradictions.

## 8. New 131-edge minimum-degree theorem

`Q32_131_MINDEG3_V46_M9_CLOSURE.md` proves:

> any 61-point non-target color C with `e(C)=131`, `alpha(C)<=12`, `omega(C)<=5` satisfies `delta(C)>=3`.

A hypothetical degree-two vertex has a 58-point non-neighborhood with `alpha<=11`, `omega<=5`; Brouwer forces at least129 internal edges. With the two incident edges all131 edges are exhausted, forcing its neighbors to have degree one. A second non-neighborhood bound at order59 gives at least135 total edges from a degree-one vertex, contradiction.

Thus the correct m=9 nonexact pointwise floor is

`L_9=3+3=6`.

This theorem uses no exact-129 gadget degree statement.

## 9. Case-I Q32 consequence

Case I means M has an independent10-set B and every M-edge meets `S=A\B`, `|S|=3`.

The source-correct matching theorem gives

`nu(M)>=m-n_w`,

while `nu(M)<=3`, hence

`n_w>=m-3`.

Current Case-I frontier:

- v=44: **CLOSED**;
- v=45: **CLOSED**;
- v=46,m=10: **CLOSED**;
- v=46,m=9: **CLOSED** by the new 131-edge degree theorem, since at the unique W-point
  `13+(4*9+6)+(3+3)=61>60`;
- v=46,m=8: **OPEN**, with `n_w in {5,6}`;
- v=47: **OPEN**.

## 10. Case-II Q32 frontier

Case II means `alpha(M)<=9`.

- v=44,m=10: **CLOSED**;
- v=44,m=9: **OPEN** rigid three-W-point terminal;
- v=44,m=8: **OPEN**;
- v=45,46,47: **OPEN**.

For v=44,m=9, source-correct shell-edge accounting gives:

- all-double t=0: `e(M)>=25`, `G_A<=7`;
- one-triple t=1: `e(M)>=28`, `G_A<=4`, and at least two core-excess units lie on W.

The new 131-edge floor leaves only two pointwise degree-slack units at each W-point above the baseline58. If its three special exact colors have KP parameters `a_1,a_2,a_3`, then

`sum(4-a_i)<=2`,

so the only sorted parameter triples are

`(4,4,4)`, `(4,4,3)`, `(4,4,2)`, `(4,3,3)`.

This is a reduction, not a contradiction.

## 11. Current root status

Closed relative to named inputs or exact local contracts:

- contextual R449;
- h12;
- h13 E397--E406;
- E407 Q31;
- E408 Q31;
- E407 Q32 local 29-point reserve theorem only (parent coverage OPEN);
- E408 Q33 local 31-point reserve theorem only (support promotion OPEN).

Open:

- E408 Q32, 285-edge / excess-six graph terminal;
- E407 Q32 V12 source/replay/exhaustiveness and parent-to-contract coverage;
- E408 Q33 support promotion for v=|U|>31.

Therefore

`EG617(r=12) = OPEN / NOT_CERTIFIED`.

## 12. Next load-bearing targets

1. Case-II `v=44,m=9`: combine the three-W KP parameter profiles, shell-edge floor, U-edge reserve, and seven-block blocker labels.
2. Case-II `v=44,m=8`: derive the corresponding special-multiplicity/multi-outside normal forms.
3. Case-I `v=46,m=8`: exploit `n_w in {5,6}` plus the three 130-edge equality/stability structures.
4. `v=47`: use all-color near-Turan/equality structure on the full core.

No branch-local root promotion is allowed until all Q32 terminals are eliminated from valid premises.


## 13. Independent root-promotion audit — 2026-10-29

### E407 Q32 / V12 artifact gate

The V12 figures remain historical source reports: archive SHA256 0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36; certificate SHA256 cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30; 8,677 kernel weights; 17,957 count states; 1,984 necessary shells; 554 reported survivors. No corresponding T61_H13_V12.zip, manifest, or verifier was found in the 30 repository branch trees. The only V12-named file is consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md, which explicitly records SOURCE_REPORTED / INDEPENDENT_REPLAY_PENDING. GitHub releases: 0; commits for exact path T61_H13_V12.zip: 0. Therefore these counts are not marked COMPUTATION_CERTIFIED in this audit.

The local reserve identity is still valid under its contract:
49*C(4,2)=294, p12(29)=22, 294+22=316>310.
The missing edge is the independently auditable proof that every legal E407 Q32 parent survives the complete V12 screen and satisfies the 29-point/49-block contract.

### E408 Q33 support gate

Q33_NONEXACT_U_RESERVE_CLOSURE.md is explicit that its theorem is conditional on the 284-edge / 31-point / 56-witness minimum-support contract. The upstream zero-excess witness theorem proves existence/lower bounds, including |U|>=31, but does not force |U|=31. The independent arithmetic replay covers v=31,...,47 as a necessary scalar inequality. It excludes m=8,9 at v=31 (with the separate m=10 theorem valid on that same contract) and m=8 at v=32; remaining higher-support cases are OPEN.

### Retraction firewall

The Kang--Pikhurko exact-129 factorization remains PROVED_CONDITIONAL under its cited source hypotheses. The universal degree-nine exceptional-vertex claim and exceptional-injectivity deductions remain RETRACTED. No excess-four identity is transferred into E408 Q32's 285-edge/excess-six terminal.

### Root decision

Root status remains OPEN / NOT_CERTIFIED. The root receipt is a fail-closed status record, not a theorem certificate.


## 14. Q32 support-layer import update — 2026-10-29

Read-only reconciliation of sibling branch heads:
- \`workstream/r12-q32-caseII-v44-final-20261028\` at \`9afd7c1a59056052974f9dc78933010d10e88bba\`;
- \`workstream/r12-q32-highsupport-root-20261028\` at \`07c69f6b4b748124ea0cf72eb1dc39bc57df6a29\`.

Their current canonical states close \(v=44,45,46\) for all \(m\in\{8,9,10\}\) under the source-correct 285-edge contract. The remaining Q32 support is \(v=47\). Within \(v=47,m=10\), the \(\chi(\overline{H[R]})\ge5\) subcase is closed, while \(\chi(\overline{H[R]})\le4\) remains open; \(m=8,9\) remain open.

This is a conditional proof import, not a claim of independent replay of all sibling analytic arguments. The high-support branch's retracted global matching-map rigidity claim and all degree-nine exceptional-vertex arguments remain excluded. Root status remains OPEN / NOT_CERTIFIED.


## 15. Full-support CSP source-contract audit — 2026-10-29

Read-only audit of the latest high-support sibling HEAD \`5f1cccb917f0d13c27f9e3fc2dfa77418dc1abff\` found two formulation defects in its not-yet-executed CSP:

1. **Wrong E408 edge-count family for m=8,9.** The model and verifier both impose \`e_0=398+m\`, with exact colors at 129, colors \(m+1,\ldots,10\) at 130, and color 11 at 132. For m=8, this gives target count 406 and non-target total 1424; for m=9, target count 407 and non-target total 1423. The fixed E408 contract instead has target count 408, non-target total 1422, and excess sum \(\sum_C s_C=3\): m=8 has three 130-edge colors; m=9 has 130- and 131-edge colors; m=10 has one 132-edge color. The present count parameterization matches E408 only at m=10.
2. **Verifier rejects valid Type-I placements.** \`verify_q32_fullsupport_candidate.py\` requires every factor in \`components[:10]\` to contain exactly one O-vertex. The source-correct placement theorem and the CSP specification itself permit an excess outside vertex to lie in an isolated factor, including the isolated-double mode. Thus the independent verifier is stricter than the registered source contract and is not yet a complete verifier for the model's allowed source modes.

The CSP has not been executed for a full solve according to the sibling's current progress log. Therefore this is a preventive model audit, not a retraction of a solver result. Any future SAT/UNSAT result must be generated after fixing the count family and verifier mismatch, then replayed with the exact final model and independent verifier. Root status remains OPEN / NOT_CERTIFIED.
