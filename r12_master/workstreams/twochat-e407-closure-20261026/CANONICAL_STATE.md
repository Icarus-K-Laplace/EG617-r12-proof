# Canonical state — E407 Q32 terminal-closure sprint

Date: 2026-10-28  
Branch: `workstream/r12-twochat-e407-closure-20261026`  
Write scope: `r12_master/workstreams/twochat-e407-closure-20261026/`

## Headline

**E407 Q32: OPEN / NOT_CERTIFIED. EG617(r=12): OPEN / NOT_CERTIFIED.**

The full `delta=13` layer is **PROVED_CONDITIONAL / CLOSED** under the registered external-theorem ledger. The saturated subproofs retain the unaudited Didin 2026 dependency.

The `delta=12` non-four-partite depth-2 frontier has now been materially compressed:

- `epsilon_U=2`: **PROVED_CONDITIONAL / CLOSED**;
- `epsilon_U=3`: both q=0 profiles are **PROVED_CONDITIONAL / CLOSED**; only the q=1 `(4,4,5,5)` W-profile remains;
- `epsilon_U=4`: the endpoint/excess ledger has exactly seven aggregate profiles, three equality-slack profiles are excluded, leaving exactly four aggregate profiles;
- `epsilon_U=0,1`: still OPEN;
- depth 3 and the delta=12 four-partite-U branch remain OPEN.

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

The five-template same-core labelled compatibility theorem remains OPEN.

# Delta=13 layer

\[
\boxed{\delta=13\Longrightarrow\bot}
\]
under the complete registered dependency ledger. Four-partite epsilon_U=0,1,2,3 and the non-four-partite augmentation/saturated branches are all discharged. Saturated reductions invoking the Didin component-count theorem remain `PROVED_CONDITIONAL`, not unconditional.

# Delta=12 non-four-partite augmentation frontier

At delta=12, `e(L_U)=306`. Greedy K5-safe augmentation has depth `k in {0,1,2,3}`.

- depth0: conditionally excluded under the registered saturated Didin/Brouwer ledger;
- depth1: conditionally excluded under the registered saturated ledger;
- depth2: classified 308-edge C5-blowup kernel; active subfrontier described below;
- depth3: 309-edge Kang-Pikhurko equality terminal remains OPEN.

## Depth2, epsilon_U=2 — CLOSED

`DELTA12_DEPTH2_EPS2_TERMINAL_REDUCTION.md` forced
\[
H[W]=K_3\dot\cup K_4\dot\cup K_5\dot\cup K_6,
\]
with `N_W(d0)=K4`, two restored J-endpoints with common `K3` neighbourhood, and all excess on d0.

`DELTA12_DEPTH2_EPS2_TERMINAL_CLOSURE.md` forces every non-exceptional point of the two K7 components to be complete to K5 or K6. Cross-K7 nonadjacency forces opposite labels; clique number at most11 then yields K12/K13 in every restored-endpoint pattern.

Status: **PROVED_CONDITIONAL / CLOSED** on the registered 308-edge saturated-kernel classification. Didin is not used in this terminal closure.

## Depth2, epsilon_U=3 — q=0 CLOSED

The two q=0 W profiles were
\[
K_3\dot\cup3K_5,
\qquad 3K_4\dot\cup K_6.
\]
`DELTA12_DEPTH2_EPS3_Q0_CLOSURE.md` first proves, in either profile,
\[
t_0=0,\qquad \epsilon_{d0}=3,
\]
so all three excess units lie on d0, the two restored J-endpoints are distinct C/E points of W-degree three, and all A/B vertices have W-degree at most six.

For `K3+3K5`, the d0-endpoint pairs force `N_W(d0)` to be one whole K5 and both endpoint neighbourhoods to be the K3. The two K7 components then acquire opposite binary K5 labels and produce K12.

For `3K4+K6`, the same exact degree-eight pair structure forces a fixed pair of K4s. Any A/B vertex satisfying both d0 and endpoint pair rules must be complete to the third K4 plus one common mandatory point; a cross-K7 pair then has at most three vertices outside that K4 and cannot cover a second W-component.

Thus both q=0 profiles are impossible. The only remaining epsilon_U=3 profile is `(4,4,5,5)` with one W-cross edge (`q=1`).

## Depth2, epsilon_U=4 — four aggregate profiles remain

Here
\[
H[W]=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5.
\]
Let `t0` count restored edges incident with d0, `epsilon0=epsilon(d0)`, `E_C` total excess on the four C/E points, and `E_rest=4-epsilon0-E_C`.

`DELTA12_DEPTH2_EPS4_ENDPOINT_SLACK_REDUCTION.md` proves
\[
4\epsilon_0+E_C\ge10+3t_0
\]
and enumerates exactly seven aggregate profiles. Three pair-cover equality profiles
\[
(0,2,2,0),\quad(1,3,1,0),\quad(2,4,0,0)
\]
for `(t0,epsilon0,E_C,E_rest)` are excluded by a complementary-K4 / binary-K5 argument.

Exactly four aggregate profiles remain:
\[
\boxed{
(0,3,0,1),\ (0,3,1,0),\ (0,4,0,0),\ (1,4,0,0).
}
\]
These are necessary aggregate profiles, not asserted graph realizations.

# Current low-delta status

- delta=16: excluded.
- delta=15: excluded under registered contracts.
- delta=14: four-partite excluded; saturated non-four-partite remains conditional on Didin.
- delta=13: PROVED_CONDITIONAL / CLOSED.
- delta=12: PARTIAL:
  - non-four-partite depth0/1 conditionally excluded;
  - depth2 eps2 closed;
  - depth2 eps3 only q=1 remains;
  - depth2 eps4 reduced to four aggregate profiles;
  - depth2 eps0/1 open;
  - depth3 open;
  - four-partite-U open.
- delta<=11: OPEN.

# Contract firewall

1. **Pure graph:** core/U/W ledgers, alpha/omega constraints, support linearity, W-transversal rules, common-nonneighbour pair rule.
2. **Labelled exact-129:** selected K5 anchors, `b_c in {5,6,7}`, residual `3K5+G11`, shell-colour ownership.
3. **Registered extremal inputs:** Brouwer and Kang-Pikhurko only where explicitly invoked.
4. **Conditional external input:** Didin 2026 remains unaudited. Every result depending on it remains `PROVED_CONDITIONAL`.
5. **Parent bridge:** V12 exhaustiveness and the original K145-to-T61/legal-residual chain remain separate dependencies.

# Highest-leverage next targets

1. eliminate the epsilon_U=3 q=1 `(4,4,5,5)` depth2 terminal using a one-defect version of the component-cover pair rule;
2. close the four remaining epsilon_U=4 aggregate profiles;
3. then attack depth2 epsilon_U=0,1, depth3, and delta=12 four-partite-U;
4. independently continue the five-template same-core labelled incompatibility theorem;
5. replace/audit Didin before any unconditional E407 claim.

No E407-Q32 or EG617(r=12) closure is claimed.
