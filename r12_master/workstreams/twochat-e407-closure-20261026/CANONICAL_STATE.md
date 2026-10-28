# Canonical state — E407 Q32 terminal-closure sprint

Date: 2026-10-28  
Branch: `workstream/r12-twochat-e407-closure-20261026`  
Write scope: `r12_master/workstreams/twochat-e407-closure-20261026/`

## Headline

**E407 Q32: OPEN / NOT_CERTIFIED. EG617(r=12): OPEN / NOT_CERTIFIED.**

The current workstream has now conditionally closed the entire **delta=12 non-four-partite augmentation depth 0–3** frontier under the registered extremal-kernel inputs. The delta=12 four-partite-U branch remains open for epsilon_U=0,1,2,3; epsilon_U=4 is closed by a new omission/excess theorem. All delta<=11 cases remain open. The five V12 shell templates A–E remain globally OPEN against the common 284-edge core/support system.

## Frozen core/support contract

\[
|H|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad \delta(H)\ge12,
\]
\[
\sum_{x\in H}(d_H(x)-12)=4.
\]
There is `U subset H`, `|U|=29`, `W=H\U`, `|W|=18`, and 49 independent support blocks, seven in each of seven exact-129 colours, disjoint inside each colour and pairwise linear globally.

Put
\[
L_U=\overline{H[U]},\qquad \delta=e(L_U)-294,
\qquad \epsilon_U=\sum_{u\in U}(d_H(u)-12).
\]
Then
\[
e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,
\quad e(H[W])=48-\epsilon_U-\delta,
\]
with
\[
3\le\delta\le16,\quad 0\le\epsilon_U\le4,\quad
\delta+\epsilon_U\le16,\quad \epsilon_U+2\delta\ge9.
\]
Every feasible profile has `alpha(H[W])=4`.

## Contract classes / firewall

1. **Pure graph:** core/U/W ledgers, alpha/omega constraints, support linearity, W-transversal rules, common-nonneighbour pair rules.
2. **Labelled exact-129:** selected K5 anchors, exact colour ownership, residual `3K5+G11`, selected-anchor multiplicities.
3. **Registered extremal inputs:** Brouwer and Kang–Pikhurko only where explicitly invoked.
4. **Conditional external input:** Didin 2026 remains unaudited; every branch using it remains `PROVED_CONDITIONAL`.
5. **Parent bridge:** V12 five-template exhaustiveness and the original K145-to-T61/legal-residual chain remain separate dependencies.

## Exact selected-component / five-template interface

Every support block `Q` is the H-four-set of a selected isolated exact-colour K5 `Q union {a(Q)}`, with anchor in `{p} union A`. For each exact colour c,
\[
\boxed{b_c\in\{5,6,7\}}.
\]
At most one selected S anchor occurs per exact colour, at least 35 of the 49 selected blocks are B-anchored, and deleting the seven selected K5s leaves exactly `3K5+G11` in that colour.

If a shell template contains a full B row (`k=3`), every exact colour has at least `b_c-3>=2` actual selected hub-complete support blocks. Hence A/B/C/D, and E whenever it has a full row, have at least14 actual selected hub-complete blocks globally. A/C satisfy the stronger full-row linearity floor `N_hub^sel>=16`. In the E no-full-row branch all ten B rows are the P3 ends-pair type and at least35 actual selected B blocks hit both endpoint rows.

With `sigma` selected S-anchor occurrences and `beta=e(M[S])`, exact-colour shell ownership gives
\[
|E_{exact}(S,B)|\ge\max\{14-\beta,\ 7+\sigma\}.
\]

**The five-template same-core labelled compatibility theorem remains OPEN.** No template A–E has been globally excluded by the labelled-support join.

# Low-delta status

## delta=16

Excluded.

## delta=15

Excluded under the registered contracts.

## delta=14

Four-partite branch excluded. The non-four-partite K5-saturated branch remains only `PROVED_CONDITIONAL` because its alpha-critical reduction invokes the unaudited Didin 2026 component theorem.

## delta=13

\[
\boxed{\delta=13\Longrightarrow\bot}
\]
under the complete registered dependency ledger. Four-partite epsilon_U=0,1,2,3 and non-four-partite augmentation/saturated branches are discharged. Saturated subproofs that invoke Didin remain conditional, not unconditional.

## delta=12 non-four-partite — CLOSED under registered augmentation kernels

At delta=12, `e(L_U)=306`. Greedy K5-safe augmentation has depth `k in {0,1,2,3}`.

- **depth0:** conditionally excluded under the registered saturated Didin/Brouwer ledger;
- **depth1:** conditionally excluded under the registered saturated ledger;
- **depth2:** all `epsilon_U=0,1,2,3,4` are `PROVED_CONDITIONAL / CLOSED` under the registered 308-edge C5-blowup kernel classification;
- **depth3:** all `epsilon_U=0,1,2,3,4` are `PROVED_CONDITIONAL / CLOSED` under the registered balanced 309-edge Kang–Pikhurko equality model.

The latest depth3 terminal proofs are:
- `DELTA12_DEPTH3_EPS0_CLOSURE.md`;
- `DELTA12_DEPTH3_EPS1_EPS2_CLOSURE.md`;
- `DELTA12_DEPTH3_EPS3_EPS4_PAIR_REDUCTION.md`;
- `DELTA12_DEPTH3_EPS3_CLOSURE.md`;
- `DELTA12_DEPTH3_EPS4_CLOSURE.md`.

For epsilon_U=3, the last `(K4,K4,K4,K6)` complementary-two-set survivor is killed by unpacking the exact P1/P2 equality-model adjacencies: P1 is forced to use both W labels, yielding at least six same-label P1–P2' pairs while only three restored edges exist.

For epsilon_U=4, restored xy is impossible by the W-component floor; every nonrestored exceptional-component placement is eliminated by binary component labels plus restored-edge incidence capacity. The hard AC branch ends with either a mixed P1 same-label count at least six or six restored endpoint incidences forcing at least nine A-A cross pairs against only three restored edges.

Thus the full **delta=12 non-four-partite branch is closed conditionally on its registered external kernel classifications.**

## delta=12 four-partite-U

`DELTA12_FOURPARTITE_SUPPORT_KERNEL.md` forces
\[
U=T_1\dot\cup T_2\dot\cup T_3\dot\cup R,
\qquad (|T_1|,|T_2|,|T_3|,|R|)=(7,7,7,8),
\]
with three seven-edge leave graphs and omission weights `(r_r)_{r in R}` summing to seven.

The epsilon_U=4 branch is now **PROVED / CLOSED** by `DELTA12_FOURPARTITE_EPS4_CLOSURE.md`: every R point with omission weight at most two must consume at least one core-excess unit; at least six of the eight R points have omission at most two, forcing epsilon_R>=6>4.

Current four-partite-U status:
- `epsilon_U=4`: **CLOSED**;
- `epsilon_U=0,1,2,3`: **OPEN**.

## delta<=11

All cases remain OPEN. The delta=12 classifications may not be extrapolated downward without a new reduction.

# Current exact open contracts

1. **Five-template same-core labelled compatibility A–E:** OPEN.
2. **delta=12 four-partite-U epsilon_U=0,1,2,3:** OPEN.
3. **delta<=11:** OPEN.
4. **delta=14 Didin-dependent saturated branch:** closed only conditionally until the external theorem is audited/replaced.
5. **V12 / original K145 bridge:** remains a parent dependency; even a complete E407 core closure is not itself the full EG617(r=12) theorem.

# Highest-leverage next targets

1. extend the four-partite omission/excess argument from epsilon_U=4 to epsilon_U=3,2,1,0;
2. use the actual selected hub-complete blocks and full-row linearity capacity to attack the five shell templates on the same support design;
3. build a new delta<=11 reduction rather than extrapolating the delta=12 augmentation classification;
4. separately replace/audit the Didin dependency before any unconditional E407 claim.

No E407-Q32 or EG617(r=12) closure is claimed.