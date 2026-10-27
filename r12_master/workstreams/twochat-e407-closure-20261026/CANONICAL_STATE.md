# Canonical state — E407 Q32 terminal-closure sprint

Date: 2026-10-27  
Branch: `workstream/r12-twochat-e407-closure-20261026`  
Write scope: `r12_master/workstreams/twochat-e407-closure-20261026/`

## Headline

**E407 Q32: OPEN / NOT_CERTIFIED. EG617(r=12): OPEN / NOT_CERTIFIED.**

The full `delta=13` layer is now **PROVED_CONDITIONAL / CLOSED under the registered external-theorem ledger**. The saturated subproofs inherit the unaudited Didin 2026 dependency from the old alpha-critical saturated-kernel classification. The remaining low-delta frontier is `delta<=12`; independently, the five V12 shell templates still require a global same-core labelled compatibility contradiction.

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

Files:
- `DELTA13_TWO_STEP_EPS1_EPS2_CLOSURE.md` — `03db399f1c767783de898e1b5cf8c1c53baa7e28`;
- `DELTA13_TWO_STEP_EPS3_CLOSURE.md` — `857196fac63f83dbecbf7c70980cf47a8253a254`.

## C. Non-four-partite already 307-edge K5-saturated: PROVED_CONDITIONAL / CLOSED

Let `G=H[U]=bar(L_U)`, so `e(G)=99` and `alpha(G)=4`. K5-saturation makes G alpha-critical. Under the registered Didin component-count theorem, G has three components `K_a dotcup K_b dotcup C`, with `alpha(C)=2`. The 49 support K4s force
\[
ab\ge49,\qquad e(\bar C)\ge49,
\]
and Brouwer gives
\[
e(C)\ge\lfloor c^2/4\rfloor-1.
\]
Together with `a+b+c=29` and `e(C)=99-C(a,2)-C(b,2)`, the exact integer survivor set is empty. Replacing 99 by 98 recovers the old unique `(7,7,15,56,49)` boundary kernel.

Files:
- `DELTA13_SATURATED_307_CONDITIONAL_CLOSURE.md` — `b1e3bfd678f0e88e6d83cd9b8fe8a32004377fda`;
- `verify_delta13_saturated_307.py` — `7193031b999dda1aecce3c9e2da182418fbb6a5c`.

## D. Exactly one safe augmentation to a 308-edge K5-saturated graph: PROVED_CONDITIONAL / CLOSED

Put `L'=L_U+e`, `G'=bar(L')`. The registered saturated-kernel classification gives
\[
G'=K_7^A\dot\cup K_7^B\dot\cup\overline J,
\]
where J is the 15-vertex saturated C5 blow-up with part sizes `(5,5,2,1,2)` and degree sequence `7^10,6^4,4^1`.

The 49 support K4s exhaust all 49 A-B edges and all 49 J-edges. They use 196 of 210 A/B-J cross edges, leaving exactly 14 uncovered. Hence the unique safe augmentation edge must be one of those 14; its J endpoint is one of the four degree-6 vertices `C union E` or the unique degree-4 point `d0`, never an X/Y vertex.

The full 47-core extension is then excluded for every `epsilon_U=0,1,2,3` using the exact U-W degrees, Brouwer-forced W four-clique profiles for epsilon>=1, and the rule that a nonadjacent core pair cannot have an independent triple among its common W nonneighbours. The epsilon=3 endpoint cases close by saturation capacity, `omega(H)<=11`, and the total four-unit core excess.

Files:
- `DELTA13_ONE_STEP_SATURATED_REDUCTION.md` — `1e9d69885f4c70034560ed55a98be45bfba7b726`;
- `DELTA13_ONE_STEP_SATURATED_EXTENSION_CLOSURE.md` — `f43f07d53639b7047e5834de8c2c75796ec30d15`;
- `verify_delta13_one_step_saturated.py` — `9d22c22ff81ae2559df2ea7d6d76e84e94e89489`.

Therefore
\[
\boxed{\delta=13\Longrightarrow\bot}
\]
**under the complete registered dependency ledger.** The saturated subproofs remain conditional on the unaudited Didin theorem.

# Current low-delta status

- `delta=16`: excluded.
- `delta=15`: excluded under registered contracts.
- `delta=14`: four-partite excluded; saturated non-four-partite branch remains **PROVED_CONDITIONAL** on Didin.
- `delta=13`: **PROVED_CONDITIONAL / CLOSED**.
- `delta<=12`: **OPEN**.

# Contract firewall

1. **Pure graph:** core/U/W ledgers, alpha/omega constraints, support linearity, W-transversal rules, common-nonneighbour pair rule.
2. **Labelled exact-129:** selected K5 anchors, `b_c in {5,6,7}`, residual `3K5+G11`, shell-colour ownership.
3. **Registered extremal inputs:** Brouwer and Kang-Pikhurko only where explicitly invoked.
4. **Conditional external input:** Didin 2026 remains unaudited. Every saturated result depending on it is labelled `PROVED_CONDITIONAL`.
5. **Parent bridge:** V12 exhaustiveness and the original K145-to-T61/legal-residual chain remain separate dependencies. Closing E407 Q32 alone would not certify EG617(r=12).

# Highest-leverage next targets

1. **Low-delta descent:** attack `delta=12` first, reusing the W-transversal / common-nonneighbour machinery and splitting by the number of K5-safe augmentations needed to reach a saturated/equality boundary.
2. **Five-template same-core incompatibility:** combine the actual hub-complete selected blocks, exact S-B colour load, U/W support multiplicities, residual `3K5+G11`, and four-unit core excess.
3. **Dependency cleanup:** independently audit or replace the Didin component-count theorem so the delta=13 and delta=14 saturated closures can be promoted from conditional to unconditional.

No E407-Q32 or EG617(r=12) closure is claimed.
