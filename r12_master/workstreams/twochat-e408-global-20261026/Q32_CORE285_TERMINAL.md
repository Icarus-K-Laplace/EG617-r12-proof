# E408 Q32 — independent 285-edge terminal

Updated: 2026-10-30  
Status: **OPEN / NOT_CERTIFIED.**

## 1. Retraction notice

The previous version of this file claimed that the registered E408-Q32 residual was impossible via `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`. That closure used a false source statement: a universal color-degree9 exceptional vertex in the Kang--Pikhurko Type-I exact-129 equality construction.

Primary-source audit shows that the relevant variable gadget degrees are

`(4+a,9-a)`, `a in {1,2,3,4}`,

namely `(5,8),(6,7),(7,6),(8,5)`. There is no universal degree9 vertex.

Therefore the old exact-color-count closure and every step using degree9 exceptional-vertex injectivity are **RETRACTED as Q32 closure theorems**. Historical files remain for audit only.

## 2. Frozen live Q32 contract

Only the 285-edge contract is used here:

`|V(H)|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`,

`sum_H(d_H-12)=6`.

For a maximum-Q32 degree-13 pivot,

`q=32`, `22<=e(M)<=32`, `e(M)+G_A=32`.

The E408 outer ledger gives eleven non-target colors with

`e_C(R)=129+s_C`, `s_C>=0`, `sum_C s_C=3`,

so the number `m` of exact-129 colors belongs to `{8,9,10}`.

No 284-edge/Q33 identity is imported.

## 3. Source-correct witness interface

For each exact-129 color, the valid Type-I equality structure gives twelve disjoint color-K5s plus the special vertex x. The registered Q32 capacity theorem therefore supplies at least ten disjoint independent core-four witnesses per exact color, pairwise-linear across colors.

If U is the union of all such witnesses and W=H\U, then

`|U|>=44`.

The corrected non-full-support theorem gives, for `w in W`, with `n_w` the number of exact colors whose special vertex equals w,

`n_w>=m-6`,

and

`|W|(m-6)<=m`.

At `|U|=44` this already excludes `m=10`; for `m=9`, all nine special vertices lie in W, exactly three at each W-point, and at most one exact color is triple-outside.

## 4. Current support frontier after sibling reconciliation

The source-correct sibling proofs now close the entire non-full-support layer:

- \(v=44\): \(m=8,9,10\) closed;
- \(v=45\): \(m=8,9,10\) closed;
- \(v=46\): \(m=8,9,10\) closed.

The low-support branch is \`workstream/r12-q32-caseII-v44-final-20261028\` at HEAD \`9afd7c1a59056052974f9dc78933010d10e88bba\`; the high-support branch is \`workstream/r12-q32-highsupport-root-20261028\` at HEAD \`92c9086c8b6ac554ed74b48a5d608aa546bcb977\`. The root-facing import and exact proof references are recorded in \`Q32_NONFULL_SUPPORT_SIBLING_IMPORT_AUDIT.md\`.

This import remains conditional on the registered source-correct Type-I factorization and named extremal inputs. It does not use the retracted degree-nine premise or the injectivity-dependent \`Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md\`.

### Full support \(v=47\)

- \(m=8\): OPEN.
- \(m=9\): OPEN.
- \(m=10\): OPEN overall; the high-chromatic residual subcase \(\chi(\overline{H[R]})\ge5\) is closed by the high-support branch, while the \(\chi(\overline{H[R]})\le4\) cell remains open.

No 284-edge/excess-four Q33 identity is imported.

## 5. New all-color U-reserve theorem

`Q32_U_COLOR_RESERVE.md` proves a source-correct coupling between exact witness K4s and the nonexact color floors in the *same* complement-edge pool.

If an exact color contains ten disjoint witness K4s in U, then

- v=44: `e_C(U)>=62` (ordinary `p_12(44)=60`);
- v=45: `e_C(U)>=64` (ordinary `p_12(45)=63`);
- v=46: `e_C(U)>=66`;
- v=47: `e_C(U)>=69`.

If an exact color supplies at least eleven witness K4s, then at v=44,45 it uses at least66 U-edges.

With h the number of exact colors supplying at least eleven witnesses:

### v=44

`e(bar(H[U])) >= 660+2m+4h`,

hence

`E_U+e(H[W])+2m+4h <=43`.

For the rigid m=9 branch:

- all-double t=0: `e(bar(H[U]))>=678`;
- one-triple t=1: `e(bar(H[U]))>=682`.

### v=45

`e(bar(H[U])) >= 693+m+2h`,

hence

`E_U+e(H[W])+m+2h <=42`.

These are necessary conditions, not contradictions.

## 6. Additional v=44,m=9 shell floor

`Q32_V44_M9_SHELL_EDGE_FLOOR.md` gives independently:

- t=0: `e(M)>=25`, `G_A<=7`;
- t=1: `e(M)>=28`, `G_A<=4`, and at least two core-excess units lie on W.

This theorem uses the corrected Type-I gadget and does not assume Case I.

## 7. Exact remaining mathematical terminal

The current shortest Q32 gap is not a scalar capacity inequality. It is the graph-level compatibility of:

1. the 285-edge / six-excess core;
2. the exact-color witness K4 packing and the new U-edge reserve;
3. the corrected Type-I double/triple multi-outside placements;
4. the 13-point shell color-edge budget;
5. the seven outer K12 blocker/duplicate system.

Highest-priority local terminals are:

- Case-II v=44,m=9 (three W points, three special labels per W, t=0 or1);
- Case-II v=44,m=8;
- Case-I v=46,m=9 and m=8;
- full support v=47.

No finite integer table satisfying only the scalar inequalities is treated as a graph realization, and no absence of candidates is treated as UNSAT without a complete verifier/reduction.

## 8. Global scope

E408 Q33 remains locally closed only under its separate exact 31-point / 56-witness contract; global support promotion remains OPEN. E408 Q32 is **OPEN** after the source correction, with all non-full supports v=44,45,46 conditionally closed by read-only sibling imports and full support v=47 still open. Therefore this workstream does not certify EG617(r=12).


## 9. Sibling integration note — 2026-10-29

This file supersedes its earlier non-full-support frontier list. The earlier listed \(v=44,45,46\) rows are no longer live terminals after the conditional closures recorded by the low-support and high-support sibling branches. Q32 remains OPEN solely because full support \(v=47\) is not closed.


## 10. Full-support CSP source-contract audit — 2026-10-29

The read-only audit in Q32_FULLSUPPORT_CSP_SOURCE_AUDIT.md found two defects in the not-yet-executed sibling CSP:
1. Its edge-count vector e_0=398+m, with the final non-target color fixed at 132 and other nonexact colors fixed at 130, represents target counts 406/407/408 for m=8/9/10. The E408 contract requires target count 408 for all three m cases and excess sum three.
2. The candidate verifier forces each of factors 0–9 to have exactly one O-vertex, despite the source-correct outside-count profile permitting excess outside incidences in isolated factors.

No solver result is imported. The full-support v=47 frontier remains OPEN; the CSP must be repaired and independently checked before use.


## 11. Latest CSP audit refresh — superseded 2026-10-29

The former note pinned sibling HEAD 92c9086c8b6ac554ed74b48a5d608aa546bcb977 and listed two defects. The latest high-support sibling is now HEAD c6500b24dc78cd4c56cd90219080003aeb8e3cb5. Its candidate verifier's source-mode check has been corrected, but the target-count formula 398+m remains wrong for m=8,9 in both model and verifier.

## 12. Current full-support CSP status — 2026-10-29

The source-mode overrestriction and E408 count-vector mismatch are both fixed in the latest sibling HEAD 1de8a37556ba98ccbb8651f39a5192629453f0f1. The model imports the independent verifier's canonical expected_color_counts helper. The full CSP remains formulation-only; no solver execution or SAT/UNSAT result is imported. Full support v=47 and EG617(r=12) remain OPEN / NOT_CERTIFIED.


## 13. 2026-10-30 supersession and z=3 no-double-track reduction

The previous count-vector warning is historical and superseded by the high-support sibling at HEAD 1de8a37556ba98ccbb8651f39a5192629453f0f1; the model and independent verifier now use target count 408 for all m. Execution and proof replay remain pending.

For the m=10, 3+7, z=3 branch with no double-track outer vertex, the root-side exact dual-fiber audit proves that a nontrivial mismatch between the small residual partition F and outer-track partition G can occur only in three split-fiber profiles. The endpoint-load ledger then forces exactly five zero-cost switches duplicating the same empty F fiber, and two aligned blocks with y_i=1 at the endpoints of the unique outer-heavy path. See Q32_Z3_DUAL_FIBER_SWITCH_COST_AUDIT.md. The z=3 terminal remains OPEN; no global Q32 closure is claimed.
