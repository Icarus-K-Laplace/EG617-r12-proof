# Canonical state — E407 Q32 terminal-closure sprint

Date: 2026-10-28  
Branch: `workstream/r12-twochat-e407-closure-20261026`  
Write scope: `r12_master/workstreams/twochat-e407-closure-20261026/`

## Headline

**E407 Q32: OPEN / NOT_CERTIFIED. EG617(r=12): OPEN / NOT_CERTIFIED.**

The full `delta=13` layer is **PROVED_CONDITIONAL / CLOSED under the registered external-theorem ledger**. The saturated subproofs inherit the unaudited Didin 2026 dependency from the old alpha-critical saturated-kernel classification.

At `delta=12`, the non-four-partite augmentation-depth-2 branch with `epsilon_U=2` is now **PROVED_CONDITIONAL / CLOSED** under the registered 308-edge saturated-kernel classification. The remaining low-delta frontier is still substantial: delta=12 four-partite U; delta=12 non-four-partite depth-2 with epsilon_U in {0,1,3,4}; depth-3; and delta<=11. Independently, the five V12 shell templates still require a global same-core labelled compatibility contradiction.

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

## Exact selected-component structure

Every support block `Q` is the H-four-set of a selected isolated exact-colour K5 `Q union {a(Q)}`, with anchor in `{p} union A`. For each exact colour c,
\[
\boxed{b_c\in\{5,6,7\}}.
\]
At most one selected S anchor occurs per exact colour, at least 35 of the 49 selected blocks are B-anchored, and deleting the seven selected K5s leaves exactly `3K5+G11` in that colour.

If a shell template contains a full B row (`k=3`), every exact colour has at least `b_c-3>=2` actual selected hub-complete support blocks. Hence A/B/C/D, and E whenever it has a full row, have at least 14 actual selected hub-complete blocks globally. A/C satisfy the stronger full-row linearity floor `N_hub^sel>=16`. In the E no-full-row branch all ten B rows are the P3 ends-pair type and at least 35 actual selected B blocks hit both endpoint rows.

With `sigma` selected S-anchor occurrences and `beta=e(M[S])`, exact-colour shell ownership gives
\[
|E_{exact}(S,B)|\ge\max\{14-\beta,\ 7+\sigma\}.
\]

Primary global-join files: `SELECTED_SUPPORT_HUB_COMPLETENESS.md`, `FULL_ROW_LINEARITY_CAPACITY.md`, `S_ANCHOR_CROSS_LOAD_REFINEMENT.md`.

# Delta=13 layer — PROVED_CONDITIONAL / CLOSED

Here `e(L_U)=307`.

## A. Four-partite U: CLOSED

All `epsilon_U=0,1,2,3` four-partite-U branches are excluded. The final epsilon-zero case was reduced under the registered Brouwer/Kang-Pikhurko equality structure to five W kernels and eliminated by W-to-U saturation-label capacity.

Files: `DELTA13_EPS0_KP_KERNEL_REDUCTION.md`, `DELTA13_EPS0_KP_KERNEL_CLOSURE.md`.

## B. Non-four-partite with two K5-safe augmentations: CLOSED

Two safe augmentations reach the 309-edge Kang-Pikhurko equality graph. The resulting four W terminals are excluded:

- epsilon_U=1: `K3+K4+K5+K6`;
- epsilon_U=1: `(3,5,5,5)` plus one W-cross edge;
- epsilon_U=2: `K3+3K5`;
- epsilon_U=3: `2K4+2K5`.

## C. Non-four-partite saturated / one-step saturated: PROVED_CONDITIONAL / CLOSED

These branches use the registered saturated-kernel machinery; the direct 307-edge alpha-critical route retains the unaudited Didin 2026 component-count theorem. Status remains conditional.

Thus
\[
\boxed{\delta=13\Longrightarrow\bot}
\]
under the complete registered dependency ledger.

# Delta=12 non-four-partite augmentation frontier

At delta=12, `e(L_U)=306`. Greedy K5-safe augmentation has depth k in {0,1,2,3}.

- depth 0: PROVED_CONDITIONAL / EXCLUDED under the registered Didin+Brouwer ledger;
- depth 1: PROVED_CONDITIONAL / EXCLUDED under the same registered ledger;
- depth 2: classified 308-edge C5-blowup kernel; epsilon_U=2 is now CLOSED, epsilon_U in {0,1,3,4} remain OPEN;
- depth 3: 309-edge Kang-Pikhurko equality terminal remains OPEN.

## New closure — depth 2, epsilon_U=2

`DELTA12_DEPTH2_EPS2_TERMINAL_REDUCTION.md` had reduced this branch to a unique W-terminal:

- `H[W]=K3 dotcup K4 dotcup K5 dotcup K6`;
- `N_W(d0)=K4`;
- two distinct restored J-endpoints c1,c2 have `N_W(c1)=N_W(c2)=K3`;
- all U-excess two lies on d0.

`DELTA12_DEPTH2_EPS2_TERMINAL_CLOSURE.md` now eliminates it. Every vertex in the two K7 components, except possibly one common restored-edge endpoint, is forced by the nonadjacent-pair rule to be complete to exactly one of W's K5 or K6. Cross-K7 nonadjacency forces opposite K5/K6 labels on the two sides. The resulting K7+K5/K6 or K6+K6 clique has size at least 12, contradicting `omega(H)<=11`. The shared-endpoint boundary is included.

This terminal closure does not use Didin. It is conditional on the registered 308-edge saturated-kernel classification and the preceding terminal reduction.

# Current low-delta status

- delta=16: excluded.
- delta=15: excluded under registered contracts.
- delta=14: four-partite excluded; saturated non-four-partite branch remains PROVED_CONDITIONAL on Didin.
- delta=13: PROVED_CONDITIONAL / CLOSED.
- delta=12: PARTIAL. Non-four-partite depth2 epsilon_U=2 CLOSED; other depth2 epsilons, depth3, and four-partite-U remain OPEN.
- delta<=11: OPEN.

# Contract firewall

1. **Pure graph:** core/U/W ledgers, alpha/omega constraints, support linearity, W-transversal rules, common-nonneighbour pair rule.
2. **Labelled exact-129:** selected K5 anchors, `b_c in {5,6,7}`, residual `3K5+G11`, shell-colour ownership.
3. **Registered extremal inputs:** Brouwer and Kang-Pikhurko only where explicitly invoked.
4. **Conditional external input:** Didin 2026 remains unaudited. Every saturated result depending on it is labelled `PROVED_CONDITIONAL`.
5. **Parent bridge:** V12 exhaustiveness and the original K145-to-T61/legal-residual chain remain separate dependencies. Closing E407 Q32 alone would not certify EG617(r=12).

# Highest-leverage next targets

1. Continue delta=12 depth-2 with `epsilon_U=3,4` first, where W is already four-clique structured and the pair-rule method may extend.
2. Eliminate delta=12 depth-3 equality terminals and the delta=12 four-partite-U branch.
3. Prove the five-template same-core labelled incompatibility using the actual hub-complete selected blocks and exact colour loads.
4. Independently audit or replace the Didin dependency before any unconditional E407 claim.

No E407-Q32 or EG617(r=12) closure is claimed.
