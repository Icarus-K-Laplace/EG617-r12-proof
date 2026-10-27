# Canonical state — E407 Q32 terminal-closure sprint

Date: 2026-10-27  
Branch: `workstream/r12-twochat-e407-closure-20261026`  
Write scope: `r12_master/workstreams/twochat-e407-closure-20261026/`

## Headline

**E407 Q32: OPEN / NOT_CERTIFIED. EG617(r=12): OPEN / NOT_CERTIFIED.**

The delta=13 frontier has materially contracted: every four-partite-U branch is excluded, and the entire non-four-partite branch admitting two successive K5-safe augmentations is now excluded. The only delta=13 non-four-partite survivors are the two K5-saturated forks described below.

## Frozen core/support contract

\[
|H|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \omega(H)\le11,\quad \delta(H)\ge12,
\]
\[
\sum_{x\in H}(d_H(x)-12)=4.
\]
There is `U subset H`, `|U|=29`, and `W=H\U`, `|W|=18`. There are 49 independent support blocks, seven in each of seven exact-129 colours, disjoint within a colour and pairwise linear.

Put
\[
L_U=\overline{H[U]},\qquad \delta=e(L_U)-294,
\qquad \epsilon_U=\sum_{u\in U}(d_H(u)-12).
\]
Then
\[
e(H[U])=112-\delta,\qquad e_H(U,W)=124+\epsilon_U+2\delta,
\qquad e(H[W])=48-\epsilon_U-\delta,
\]
with
\[
3\le\delta\le16,\quad 0\le\epsilon_U\le4,\quad
\delta+\epsilon_U\le16,\quad \epsilon_U+2\delta\ge9.
\]
Every feasible profile has `alpha(H[W])=4`.

## Exact selected-component structure

Every one of the 49 support blocks `Q` is the H-four-set of a selected isolated exact-colour `K5`, `Q union {a(Q)}`, with anchor in `{p} union A`. For every exact colour `c`, the number `b_c` of selected B anchors satisfies
\[
\boxed{b_c\in\{5,6,7\}}.
\]
At most one selected S anchor occurs per exact colour, at least 35 of the 49 selected blocks are B-anchored, and deleting the seven selected K5s leaves exactly `3K5 + G11` in that colour.

## Five-template global forcing

### Actual selected hub-complete blocks

If the shell template contains a full B row `f` (`k_f=3`), every selected B-anchored support block that is not hub-complete must meet `D_f`. Since `|D_f|=3` and same-colour selected blocks are disjoint, every exact colour has at least
\[
b_c-3\ge2
\]
actual selected hub-complete support blocks.

Thus A/B/C/D, and E whenever `n3>=1`, have at least 14 actual selected hub-complete blocks globally. In the E no-full-row branch the row equations force all ten B rows to be the P3 ends-pair type, and at least 35 actual selected B blocks hit both endpoint rows.

### Full-row linearity capacity

If `h` is the number of full B rows and `N_bad` the global number of selected B blocks that are not hub-complete, support linearity plus pointwise anchor injectivity gives
\[
\boxed{N_{bad}\le C(h):=\min\{21,\lfloor 9+60/h\rfloor\}.}
\]
Since `B_sel=sum_c b_c>=35`,
\[
N_{hub}^{sel}\ge B_{sel}-C(h).
\]
In particular A and C have `h>=6`, hence
\[
\boxed{N_{hub}^{sel}\ge16.}
\]

### Exact shell cross-load with S anchors

Let `sigma` be the number of selected S-anchor occurrences and `beta=e(M[S])`. Every exact colour owns at least one exact-coloured S-B shell edge, and a colour with a selected S anchor owns at least two. Hence
\[
\boxed{|E_{exact}(S,B)|\ge\max\{14-\beta,\ 7+\sigma\}.}
\]

Primary files: `SELECTED_SUPPORT_HUB_COMPLETENESS.md`, `FULL_ROW_LINEARITY_CAPACITY.md`, `S_ANCHOR_CROSS_LOAD_REFINEMENT.md`.

## Delta=13 four-partite U: CLOSED

All `epsilon_U=0,1,2,3` four-partite-U branches are excluded. The last `epsilon_U=0` case was reduced, using the registered Brouwer/Kang-Pikhurko equality theorem, to five 18-vertex W kernels and eliminated by W-to-U saturation-label capacity.

Files: `DELTA13_EPS0_KP_KERNEL_REDUCTION.md`, `DELTA13_EPS0_KP_KERNEL_CLOSURE.md`.

## Delta=13 non-four-partite: augmentation trichotomy

Here
\[
e(L_U)=307.
\]
The augmentation split is now exact:

1. **two K5-safe augmentations exist** — CLOSED;
2. **exactly one K5-safe augmentation exists, and the resulting 308-edge graph is K5-saturated** — OPEN;
3. **the original 307-edge graph is already K5-saturated** — OPEN.

### Two-step branch: CLOSED

Adding two K5-safe nonedges gives a 309-edge non-four-partite K5-free graph, so the registered Kang-Pikhurko equality structure applies. The earlier reduction left four W terminals.

`DELTA13_TWO_STEP_EPS1_EPS2_CLOSURE.md` excludes:

- `epsilon_U=1`, `K3 + K4 + K5 + K6`;
- `epsilon_U=1`, `(3,5,5,5)` with one W-cross edge;
- `epsilon_U=2`, `K3 + 3K5`.

The common mechanism is that the KP exceptional pair `x,y` remains a target nonedge, while their forced small W-neighbourhoods leave one common nonneighbour in each of three mutually anticomplete W components, producing an independent five-set.

`DELTA13_TWO_STEP_EPS3_CLOSURE.md` excludes the final `epsilon_U=3`, `2K4 + 2K5` terminal. The proof first forces `x,y` to saturate the two different K4 components. Every vertex of the KP parts `P3 union P4` must then saturate one of the two K5 components. Each of `P3,P4` must use both K5 labels to avoid a target K12, while `P3-P4` is target-anticomplete; two vertices in different parts sharing a K5 label then have enough common W nonneighbours to create an independent five-set.

Therefore
\[
\boxed{\delta=13,\ L_U\text{ non-four-partite and two-step K5-safe augmentable }\Longrightarrow\bot.}
\]

Latest closure commits:

- `03db399f1c767783de898e1b5cf8c1c53baa7e28` — epsilon_U=1,2 terminals excluded;
- `857196fac63f83dbecbf7c70980cf47a8253a254` — final epsilon_U=3 terminal excluded.

## Current low-delta status

- `delta=16`: excluded.
- `delta=15`: registered four-partite and non-four-partite branches excluded.
- `delta=14`: four-partite excluded; saturated non-four-partite branch remains **PROVED_CONDITIONAL** on the unaudited Didin dependency.
- `delta=13`: all four-partite branches excluded; non-four-partite two-step-augmentable branch excluded; only the **307-edge saturated** and **one-step-to-308 saturated** forks remain.
- `delta<=12`: OPEN.

## Contract firewall

1. Pure graph: core/U/W ledgers, alpha/omega bounds, support linearity and W-transversal consequences.
2. Labelled exact-129: selected K5 anchors, `b_c in {5,6,7}`, residual `3K5+G11`, exact shell-colour ownership.
3. Published external extremal input: Brouwer/Kang-Pikhurko only where explicitly registered.
4. Conditional external input: the delta=14 saturated branch still depends on the unaudited Didin 2026 preprint theorem; it is not promoted to unconditional.
5. Parent bridge: V12 exhaustiveness and the original K145-to-T61 chain remain separate dependencies.

## Highest-leverage next targets

1. **Delta=13 saturated fork theorem:** exclude a 29-vertex, non-four-partite, K5-free K5-saturated graph with 307 edges, or the 308-edge saturated graph reached by one K5-safe augmentation, while respecting the 49-block support packing and four-unit H excess. Prefer a direct proof independent of Didin.
2. **Five-template same-core incompatibility:** combine the actual selected hub-complete blocks, exact S-B colour load, U/W support multiplicities, residual `3K5+G11`, and four-unit core excess to exclude templates A–E.
3. `delta<=12` remains an independent later frontier.

No E407-Q32 or EG617(r=12) closure is claimed.
