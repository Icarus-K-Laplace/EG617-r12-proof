# EG617 fixed r=12 — canonical state of this workstream

Updated: 2026-10-30  
Repository: `Icarus-K-Laplace/EG617-r12-proof`  
Branch: `workstream/r12-twochat-e408-global-20261026`  
Write scope: `r12_master/workstreams/twochat-e408-global-20261026/`

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.**

The uniquely identified live graph terminal in the current audited shortest chain is

`E408 / h13 / Qmax=32 / e(H)=285 / core excess6`.

**Independent root-promotion audit (2026-10-29):** the root also has two separately OPEN promotion gates: E407 Q32 V12 parent coverage and E408 Q33 support promotion beyond the exact 31-point contract. The root receipt is not promotable.

The former E408-Q32 exact-color-count closure is **RETRACTED** because it used a false universal degree-nine exceptional vertex. The source-correct Kang--Pikhurko Type-I factorization remains valid.

## Root branches closed relative to named inputs

- contextual `R(4,49)`: closed;
- T61 h12: closed;
- h13 E397--E406: closed;
- E407 Q31: closed through the registered V10/V11 route;
- E407 Q32: the 29-point/49-block reserve contradiction is **PROVED_CONDITIONAL locally**; the template-local support/anchor contract is **PROVED_CONDITIONAL** under the registered minimum-support and exact-129 assumptions, but mapping every legal parent/survivor into the five templates is **OPEN** pending V12 source/replay;
- E408 Q31: closed under the V11 route;
- E408 Q33: the 31-point/56-witness reserve contradiction is **PROVED_CONDITIONAL locally**; parent support promotion for |U|>31 is **OPEN**.

No statement above promotes the full theorem while Q32 remains open.

## Q33 status

The requested four old `P_C=49` profiles no longer form the load-bearing frontier. Two were locally excluded; two all-component-edge-present profiles remain locally open, but the exact 31-point/56-witness Q33 terminal is locally bypassed by `Q33_NONEXACT_U_RESERVE_CLOSURE.md`.

Thus only the registered 284-edge, |U|=31, 56-witness Q33 terminal is **PROVED_CONDITIONAL impossible**. The upstream support bound |U|>=31 does not prove equality, so no global Q33 closure is claimed for |U|>31. No Q32 statement is imported into that local proof.

## Source-correct exact-129 interface

For each exact-129 non-target color C on the 61-point residual,

`C = 10 isolated K5 dot-union G11`,

where `G11` contains two further disjoint K5s and the special vertex x. Excluding x, the other60 vertices partition into twelve C-colored K5s.

For source parameter `a in {1,2,3,4}`, the variable gadget degrees are

`(4+a,9-a) in {(5,8),(6,7),(7,6),(8,5)}`.

There is no universal degree-nine vertex.

## Frozen live Q32 contract

For E408-Q32,

`|H|=47`, `e(H)=285`, `alpha(H)<=4`, `delta(H)>=12`,

`sum_H(d_H-12)=6`.

For the 13-point shell A and `M=bar(F[A])`,

`22<=e(M)<=32`, `e(M)+G_A=32`.

The number m of exact-129 colors lies in `{8,9,10}`. Each exact color supplies at least ten disjoint independent core-four witnesses; across colors the witness family is pairwise linear. If U is the union of witnesses and W=H\U, then

`|U|>=44`.

## Corrected non-full-support theorem

For `w in W`, let `n_w` be the number of exact colors whose special vertex equals w. The source-correct multi-outside K5 argument proves

`n_w>=m-6`,

and therefore

`|W|(m-6)<=m`.

At `|U|=44`:

- m=10 is impossible;
- for m=9 every W-point is special for exactly three exact colors, all nine special vertices lie in W, at most one exact color is triple-outside, and the other exact colors are double-outside;
- if the triple-outside color occurs, at least two core-excess units lie on W;
- m=8 remains open.

## Case-I shell theorem

Case I means M has an independent10-set B. Put S=A\B, `|S|=3`; every M-edge meets S.

For fixed `w in W`, each exact color with special vertex different from w supplies an M-edge in its multi-outside K5. Across colors these selected edges form a matching, so

`nu(M)>=m-n_w`.

Since every M-edge touches S, `nu(M)<=3`, hence

`n_w>=m-3`.

Consequences:

- v=44: closed;
- v=45: closed;
- v=46,m=10: closed.

## New 131-edge minimum-degree theorem

`Q32_131_MINDEG3_V46_M9_CLOSURE.md` proves:

> if a non-target residual color C has `e(C)=131`, `alpha(C)<=12`, `omega(C)<=5`, then `delta(C)>=3`.

Proof: a hypothetical degree-two vertex has a 58-point non-neighborhood with `alpha<=11`, `omega<=5`; the registered Brouwer bound forces at least129 internal edges. Together with the two incident edges this exhausts all131 edges, forcing its two neighbors to have degree one. A second non-neighborhood application excludes degree one.

Therefore the correct nonexact pointwise degree-floor sums are

- `L_8=9` for three 130-edge colors;
- **`L_9=6`** for the 130+131 pair;
- `L_10=2` for one132-edge color.

### Immediate closure: Case I / v=46 / m=9

At the unique W-point, Case I gives `n_w>=6`. Hence

`target >=13`,

`nine exact colors >=4*9+6=42`,

`130+131 colors >=3+3=6`.

The sum is at least61, impossible at a 60-edge vertex. Thus

> **Case I / v=46 / m=9 is CLOSED.**

## New all-color U-reserve theorem

`Q32_U_COLOR_RESERVE.md` couples exact witness K4s and nonexact color floors inside the same complement-edge pool.

An exact color containing ten disjoint witness K4s satisfies

| v=|U| | ordinary p12(v) | exact-color floor |
|---:|---:|---:|
|44|60|**62**|
|45|63|**64**|
|46|66|66|
|47|69|69|

At v=44 the extra two edges are proved by excluding both the Turan equality layer and the 61-edge layer; the latter splits into a non-12-partite Brouwer branch and a direct 12-partition/cross-edge count. At v=45 ordinary equality has only nine disjoint K4s.

If h exact colors supply at least eleven witnesses, then:

- v=44: `e(bar(H[U]))>=660+2m+4h`;
- v=45: `e(bar(H[U]))>=693+m+2h`.

These are necessary reserve bounds, not closure.

## v=44,m=9 shell floor

The corrected Type-I shell-edge theorem gives:

- all-double `t=0`: `e(M)>=25`, `G_A<=7`;
- one-triple `t=1`: `e(M)>=28`, `G_A<=4`, and at least two core-excess units lie on W.

With the new 131-edge theorem, every W-point in this m=9 branch has only two total degree-slack units above the baseline

`target13 + exact39 + nonexact6 =58`.

In particular, if the three special exact colors at w have source parameters `a_1,a_2,a_3`, then

`sum_i (4-a_i) <=2`,

so

`a_1+a_2+a_3>=10`.

Thus each W-point has special-parameter profile among

`(4,4,4)`, `(4,4,3)`, `(4,4,2)`, `(4,3,3)`

up to order. This is a strict source-correct reduction, not yet a contradiction.

## Current exact Q32 frontier — sibling-import audit 2026-10-29

The low-support and high-support sibling canonical states now close all non-full supports \(v=|U|=44,45,46\) for \(m=8,9,10\), conditional on their registered Type-I and extremal-theorem inputs. This root workstream has read and reconciled the source documents; it has not independently re-proved every imported analytic lemma. See \`Q32_NONFULL_SUPPORT_SIBLING_IMPORT_AUDIT.md\`.

| \(v=|U|\) | \(m=8\) | \(m=9\) | \(m=10\) |
|---:|---|---|---|
| 44 | CLOSED | CLOSED | CLOSED |
| 45 | CLOSED | CLOSED | CLOSED |
| 46 | CLOSED | CLOSED | CLOSED |
| 47 | OPEN | OPEN | OPEN overall; \(\chi(\overline{H[R]})\ge5\) subcase CLOSED, \(\chi(\overline{H[R]})\le4\) remains OPEN |

### Full-support structural ledger

For \(v=47\), the exact multicolor near-Turán ledger is \(\sum_C g_C=37\), where \(g_C=e_C(H)-69\). The pivot-neighborhood reduction gives \(m\) disjoint independent \(K_4\) blocks and a 253-edge baseline against \(e(H)=285\), leaving 32 units of slack. The scalar relaxation has feasible states and cannot by itself close Q32.

Highest-priority target is therefore the full-support \(v=47\) case: \(m=8,9\), and the remaining low-chromatic-residual \(m=10\) branch. The old degree-nine exceptional-vertex claim and injectivity-dependent closure are excluded by the retraction firewall.

**CSP status refresh (2026-10-30, read-only sibling HEAD 1de8a37556ba98ccbb8651f39a5192629453f0f1):** both previously reported source-contract defects are now corrected in the sibling model/verifier. The solver imports the canonical expected_color_counts(m) helper: target color 0 has 408 edges for every m; the exact colors have 129 each; the nonexact vectors are (130,130,130) for m=8, (130,131) for m=9, and (132) for m=10. The source-outside-profile verifier also accepts the registered aggregate profiles. The monochromatic-K6 separator and malformed-witness checks are wired in. However, the sibling CSP specification still records execution/proof replay as pending; Z3 is unavailable in this runtime, and no SAT/UNSAT result is imported.

**New z=3 no-double-track reduction:** in the m=10, 3+7 cell, an exact enumeration of 91,584 ordered pairs of labelled small/outer clique partitions shows that any nontrivial F/G mismatch must be one of three empty-fiber split modes. Combining the per-block incidence-slack inequality with the small-block endpoint-load budget forces exactly five zero-cost synchronized switches duplicating the same empty fiber, and exactly two aligned blocks with y_i=1 at the endpoints of the unique outer-heavy path. See Q32_Z3_DUAL_FIBER_SWITCH_COST_AUDIT.md and its verifier. This is a conditional local reduction only; z=3, full-support Q32, and EG617(r=12) remain OPEN / NOT_CERTIFIED.

## Status policy

No root promotion is allowed until E408-Q32 is closed from valid premises. Any source mismatch fail-closes the affected theorem immediately.


## Independent root audit addendum — 2026-10-29

- V12 is OPEN for this root certification: the reported archive and certificate hashes/counts have not been independently replayed from available source artifacts. The repository's 30 branch trees were searched; none contains T61_H13_V12.zip, a matching V12 manifest, or a V12 verifier. The only V12-named file found is consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md, which explicitly says INDEPENDENT_REPLAY_PENDING. The releases endpoint has zero releases and the exact archive path has zero commit-history matches.
- E407 Q32: 49*C(4,2)=294 and p12(29)=22, so 316>310 is valid under the exact 29-point/49-block support contract. The local arithmetic is not the missing step; V12 finite coverage and analytic parent-to-contract coverage remain OPEN.
- E408 Q33: the exact 31-point/56-witness reserve is valid conditionally. For supports v=32..47, the independent scalar reserve audit excludes only m=8 at v=32; it does not exclude m=9 or m=10 there, nor m=8,9,10 for v>=33. This is a necessary-capacity check, not a graph-realization counterexample.
- E408 Q32 remains OPEN / NOT_CERTIFIED under the source-correct 285-edge/excess-six contract. No degree-nine or exceptional-injectivity premise is restored.
- Current root status: OPEN / NOT_CERTIFIED. No promotable receipt is issued.


## 2026-10-30 — z=3 no-double-track alignment reduction

The exact dual-fiber partition-pair enumeration first narrowed every nontrivial F/G mismatch to three empty-fiber split profiles. A stronger pointwise switch-partner degree blocker now rules out all three: in a synchronized 4,5,5 switch with transposition partner j, the outer vertex receiving two extra small-component edges has k(q)=2 and is adjacent to every residual vertex in F_j. The degree identity e_Q(q)+d_R(q)=3 therefore forces |F_s|+|F_j|<=1. Every nontrivial mismatch mode has |F_s|+|F_j|>=2, contradiction.

Consequently, in the m=10, 3+7, z=3 cell with no double-track vertex, the small residual partition F equals the outer-track partition G. The same pointwise blocker permits a switch only between an empty fiber and a singleton fiber; the only registered profile allowing that is (3,3,1,0), where a size-three fiber remains fixed and yields a forbidden monochromatic K13. Profiles (3,2,2,0) and (3,2,1,1) likewise have a size-three fiber and no permitted switch. Thus the no-double-track z=3 branch reduces to the fully aligned profile (2,2,2,1), with every outer block aligned.

The double-track z=3 branch, the aligned (2,2,2,1) terminal itself, the other m=10 light-block cells, and full-support m=8,9 remain OPEN / NOT_CERTIFIED. See Q32_Z3_SWITCH_PARTNER_DEGREE_BLOCKER.md and verify_q32_z3_switch_partner_degree_blocker.py.
