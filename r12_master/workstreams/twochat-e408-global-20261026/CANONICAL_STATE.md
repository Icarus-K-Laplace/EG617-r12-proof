# EG617 fixed r=12 — canonical state of this workstream

Updated: 2026-10-29  
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
- E407 Q32: the 29-point/49-block reserve contradiction is **PROVED_CONDITIONAL locally**; parent coverage for every legal E407 Q32 survivor is **OPEN** pending V12 source/replay and template-to-contract coverage;
- E408 Q31: closed under the V11 route;
- E408 Q33: the 31-point/56-witness reserve contradiction is **PROVED_CONDITIONAL locally**; parent support promotion for |U|>31 is **OPEN**.

No statement above promotes the full theorem while Q32 remains open.

## Q33 status

The requested four old `P_C=49` profiles no longer form the load-bearing frontier. Two were locally excluded; two all-component-edge-present profiles remain locally open, but the entire registered Q33 terminal is globally bypassed by `Q33_NONEXACT_U_RESERVE_CLOSURE.md`.

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

## Current exact Q32 frontier

### Case I — shell target contains K10

- v=44: CLOSED;
- v=45: CLOSED;
- v=46,m=10: CLOSED;
- **v=46,m=9: CLOSED** by the 131-edge min-degree theorem;
- v=46,m=8: OPEN, with `n_w in {5,6}`;
- v=47: OPEN.

### Case II — no shell target K10

- v=44,m=10: CLOSED;
- v=44,m=9: OPEN rigid three-W-point terminal, with t=0 or1 and the parameter profiles above;
- v=44,m=8: OPEN;
- v=45,46,47: OPEN.

No 284-edge/excess-four statement is imported into these reductions.

## Highest-leverage next targets

1. Case-II v=44,m=9: combine the three-W source-parameter profiles, shell-edge floor, U-reserve, and seven-block blocker labels.
2. Case-II v=44,m=8: classify special multiplicities and multi-outside placements under the same corrected Type-I source.
3. Case-I v=46,m=8: exploit `n_w=5 or6`, the three 130-edge low-degree structures, and the S-to-B shell matching in the n=5 subcase.
4. v=47: use all-color near-Turan equality structure on the full core.

## Status policy

No root promotion is allowed until E408-Q32 is closed from valid premises. Any source mismatch fail-closes the affected theorem immediately.


## Independent root audit addendum — 2026-10-29

- V12 is OPEN for this root certification: the reported archive and certificate hashes/counts have not been independently replayed from available source artifacts. The repository's 30 branch trees were searched; none contains T61_H13_V12.zip, a matching V12 manifest, or a V12 verifier. The only V12-named file found is consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md, which explicitly says INDEPENDENT_REPLAY_PENDING. The releases endpoint has zero releases and the exact archive path has zero commit-history matches.
- E407 Q32: 49*C(4,2)=294 and p12(29)=22, so 316>310 is valid under the exact 29-point/49-block support contract. The local arithmetic is not the missing step; V12 finite coverage and analytic parent-to-contract coverage remain OPEN.
- E408 Q33: the exact 31-point/56-witness reserve is valid conditionally. For supports v=32..47, the independent scalar reserve audit excludes only m=8 at v=32; it does not exclude m=9 or m=10 there, nor m=8,9,10 for v>=33. This is a necessary-capacity check, not a graph-realization counterexample.
- E408 Q32 remains OPEN / NOT_CERTIFIED under the source-correct 285-edge/excess-six contract. No degree-nine or exceptional-injectivity premise is restored.
- Current root status: OPEN / NOT_CERTIFIED. No promotable receipt is issued.
