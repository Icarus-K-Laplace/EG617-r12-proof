# EG617 fixed r=12 — canonical state of this workstream

Updated: 2026-10-28  
Repository: `Icarus-K-Laplace/EG617-r12-proof`  
Branch: `workstream/r12-twochat-e408-global-20261026`  
Write scope: `r12_master/workstreams/twochat-e408-global-20261026/`

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.**

The current uniquely identified live graph terminal in the audited root chain is

\[
\boxed{E408\;/\;h13\;/\;Q_{\max}=32\;/\;e(H)=285\;/\;\text{core excess }6.}
\]

The earlier E408-Q32 exact-color-count closure is **RETRACTED** because primary-source audit of the Kang--Pikhurko Type-I equality construction proved that there is no universal color-degree9 exceptional vertex. The exact-129 factorization itself remains valid.

## Root branches still closed relative to named inputs

- contextual `R(4,49)` branch: closed;
- T61 h12: closed;
- h13 E397--E406: closed;
- E407 Q31: closed through the registered V10/V11 route;
- E407 Q32: closed by the one-unselected-color U-edge reserve contradiction;
- E408 Q31: closed under the V11 route;
- E408 Q33: closed by the component-capacity/nonexact-U reserve route.

No statement above promotes the full r=12 theorem while E408-Q32 remains open.

## E407 Q32 short closure remains valid

The registered E407 terminal has `|U|=29`, 49 selected independent four-blocks, seven selected exact colors, pairwise block linearity, and

\[
e(\overline{H[U]})=294+\delta\le310.
\]

The selected blocks are genuine monochromatic exact-color K4s, so they own 294 distinct complement edges. At least one of the eleven non-target colors is not among those seven. For such a color D,

\[
\alpha(D[U])\le12\Longrightarrow e_D(U)\ge p_{12}(29)=22.
\]

Color uniqueness therefore forces

\[
e(\overline{H[U]})\ge294+22=316>310.
\]

This closes the registered E407-Q32 terminal without the retracted degree9 premise.

## Valid Kang--Pikhurko exact-129 interface

For an exact-129 non-target color C on the 61-point residual:

\[
C=10K_5\;\dot\cup\;G_{11},
\]

where `G11` contains two further disjoint K5s and the added vertex x. Equivalently, excluding x, the other 60 vertices are partitioned into twelve color-C K5s.

For the source parameter `a in {1,2,3,4}`, the two variable gadget degrees are

\[
(4+a,9-a)\in\{(5,8),(6,7),(7,6),(8,5)\}.
\]

There is no universal degree9 vertex. Files depending on degree9 injectivity remain historical/retracted artifacts.

## Live E408-Q32 contract

For a maximum-Q32 degree-13 pivot in E408,

\[
|H|=47,\qquad e(H)=285,\qquad \alpha(H)\le4,\qquad \delta(H)\ge12,
\]

and

\[
\sum_{x\in H}(d_H(x)-12)=6.
\]

The shell A has 13 vertices. With `M=bar(F[A])`,

\[
22\le e(M)\le32,\qquad e(M)+\sum_{a\in A}g_a=32.
\]

The number m of exact-129 colors is in `{8,9,10}`. Every exact color supplies at least ten disjoint independent core-4 witnesses, witness families across colors are pairwise linear, and if U is their global support then the source capacity theorem gives

\[
|U|\ge44.
\]

Write W=H\U.

## Corrected non-full-support theorem — 2026-10-28

`Q32_CORRECTED_NONFULL_SUPPORT_MULTIPLICITY.md`, commit
`6e6dab1a59b03bcbfb07cafe3f2ee71ab5d4e1f2`, proves without degree9:

For `w in W`, let `n_w` be the number of exact colors whose Type-I special vertex x_C equals w. If x_C is not w, then w lies in a multi-outside exact-color K5. Such a K5 contains at least two shell vertices, and different exact colors use disjoint shell neighbors at fixed w. Hence

\[
\boxed{n_w\ge m-6},\qquad
\boxed{|W|(m-6)\le m}.
\]

Consequences at `|U|=44`, `|W|=3`:

- `m=10`: impossible;
- `m=9`: `n_w=3` at all three W-points, all nine special vertices lie in W;
- in that `m=9` equality branch, at most one exact color is triple-outside and at least eight are double-outside;
- if the one triple-outside color occurs, at least two of the six core-excess units lie on W.

`m=8` remains open at v=44.

## Case-I shell reduction

The source shell classification splits:

- **Case I:** M has an independent 10-set B; with S=A\B, `|S|=3` and `M[B]=empty`;
- **Case II:** `alpha(M)<=9`.

`Q32_CASEI_LOW_SUPPORT_MATCHING_EXCLUSION.md`, commit
`ef2915c60c055868bc0a31a4db1da4b0af1667d4`, proves:

For fixed `w in W`, every exact color with `x_C != w` provides an M-edge inside its multi-shell K5. These chosen edges are pairwise vertex-disjoint across colors, so

\[
\nu(M)\ge m-n_w.
\]

In Case I every M-edge touches the three-point set S, hence `nu(M)<=3` and

\[
n_w\ge m-3.
\]

Summing over W excludes `|W|=3` and `|W|=2` for every `m>=8`. Therefore

\[
\boxed{\text{Case I}\Longrightarrow |U|\ge46.}
\]

Thus Case-I support sizes v=44 and v=45 are closed.

## Case-I v=46 full-degree rigidity

`Q32_CASEI_V46_FULL_DEGREE_RIGIDITY.md`, commit
`8ea6fbb3e83403bea2a83104f6a21f9ef4350fce`, combines `n_w>=m-3` with the correct full-color degree floors at the unique point `W={w}`.

If `L_m` is the nonexact degree-floor sum,

\[
L_8=9,\qquad L_9=5,\qquad L_{10}=2,
\]

then

\[
13+(4m+n_w)+L_m\le60.
\]

Consequences:

- `m=10`: impossible;
- `m=9`: necessarily `n_w=6`; target degree=13; six special exact degrees=5; three non-special exact degrees=4; nonexact degrees are exactly3 and2. The six special colors all have KP parameter `a=4`. The three non-special colors use double-shell K5s whose shell pairs form a matching from all three S vertices to three distinct B vertices;
- `m=8`: `n_w in {5,6}`. If `n_w=6`, all degree floors are equalities; if `n_w=5`, exactly one total degree-slack unit remains. In the `n_w=5` subcase the three non-special shell pairs again form an S-to-distinct-B matching.

Arithmetic regression file:
`verify_q32_corrected_support_reductions.py`, commit
`247bdd66fa901401e7e019e210712dd4aeaa8f7e`.
The same integer implications were independently recalculated during this audit.

## Current exact Q32 frontier

### Case I — shell target contains K10

- v=44: **PROVED_CONDITIONAL impossible**;
- v=45: **PROVED_CONDITIONAL impossible**;
- v=46,m=10: **PROVED_CONDITIONAL impossible**;
- v=46,m=9: OPEN rigid equality terminal described above;
- v=46,m=8: OPEN with `n_w=5 or6`;
- v=47: OPEN.

### Case II — no shell target K10

- v=44,m=10: **PROVED_CONDITIONAL impossible**;
- v=44,m=9: OPEN but rigid: all special vertices lie in the three W-points, exactly three labels per W-point, at most one triple-outside color;
- v=44,m=8: OPEN;
- v=45,46,47: OPEN.

No 284-edge/excess-four statement is imported into these Q32 reductions.

## Front-end computation boundary

Line-A remains computation-certified with the registered package and replay:

- package SHA256 `8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac`;
- 1,752 recurrence nodes;
- 144 outer comparisons;
- unique no-R(4,49) stop `(11,6,5,61)` with energy397..408;
- independent replay PASS.

Historical assumption ledgers are not silently upgraded.

## Highest-leverage next targets

1. Case-II v=44,m=9: join the three-point special-label equality system to the 13-point shell graph and seven-block incidence ledger.
2. Case-II v=44,m=8: classify the remaining special-vertex multiplicities and multi-outside K5 placements.
3. Case-I v=46,m=9 and m=8: exploit the exact full-degree equalities, the S-to-B shell matching, and the correct `(5,8)` gadget pair forced in the m=9 special colors.
4. v=47 full support: use all-color near-Turan edge slack on H and exact Type-I placement rather than any false special-vertex injectivity.

## Status policy

No root theorem promotion is allowed until E408-Q32 is closed from valid premises. Any source mismatch fail-closes the affected theorem immediately.
