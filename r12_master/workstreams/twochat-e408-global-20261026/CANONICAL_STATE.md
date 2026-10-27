# EG617 fixed r=12 — canonical state of this workstream

Updated: 2026-10-27
Repository: `Icarus-K-Laplace/EG617-r12-proof`
Branch: `workstream/r12-twochat-e408-global-20261026`
Write scope: `r12_master/workstreams/twochat-e408-global-20261026/`

## Headline

**All registered fixed-r=12 graph terminals in the audited root chain are closed.**

Current promotion:

\[
\boxed{\text{EG617}(r=12):\ \textbf{PROVED_CONDITIONAL + COMPUTATION_CERTIFIED}}
\]

There is currently **no OPEN graph-theoretic T61/E407/E408 terminal** in this branch-local composition.

The qualifier is deliberate. The proof stack still consumes exact finite certificates, named external extremal/Ramsey theorems, the exact-129 Type-I factor theorem, and later selected-support identities. It is not yet an end-to-end formally verified proof. The next promotion target is a publication-grade computer-assisted-proof receipt with every load-bearing theorem statement and source hash frozen.

## Root chain

A hypothetical balanced 12-color counterexample is reduced by Line A to either:

1. a contextual induced `R(4,49)`; or
2. the embedded T61 terminal.

The contextual `R(4,49)` branch is eliminated by the registered full-color impossibility theorem. The T61 branch is exhausted as follows.

### Minimum degree

- h12: closed by `T61_H12_CLOSURE.md`.
- therefore every survivor has h13.

### Energy

- E397--E400: closed;
- E401--E404: closed;
- E405: closed;
- E406: closed;
- E408: closed as a whole energy layer by `E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md`;
- E407: only maximum charges Q31/Q32 survive the earlier V9 reduction.

### E407 Q31

The original V10/V11 packages were independently materialized and replayed.

- V10 archive SHA256: `e83e2907d541b38304746e855af52b5e21b6500a35cb0fdb676a4f6a7601303a`;
- V11 archive SHA256: `27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4`;
- both fresh package manifests passed before verifier execution;
- V10 replay: 12 labelled cuts, 16 local-neighbourhood cases, 14 row-budget cases;
- V11 replay: 684 kernel weights, 349 count states, 259 labelled necessary shells = 252 Family A + 7 Family B;
- V11 certificate SHA256: `0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b`.

The analytic common-K10 support-capacity theorem excludes both families. Hence E407 maximum Q31 is closed relative to the named core/extremal inputs.

### E407 Q32 — shortest terminal contradiction

The original V12 package was independently replayed.

- archive SHA256: `0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36`;
- fresh manifest passed;
- 8,677 kernel weights;
- 17,957 count states;
- 1,984 labelled necessary shells;
- 554 finite-screen survivors;
- all 554 map to the five V12 shell templates;
- certificate SHA256: `cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30`.

The later E407 workstream proves that every one of the five templates uses the same 29-point support U and 49 selected four-set blocks in seven distinct selected exact colors, and that every selected block is genuinely the H-four-set of a monochromatic selected-color K5.

For `L_U = overline(H[U])`:

\[
e(L_U)=294+\delta,\qquad \delta\le16,
\]

so

\[
e(L_U)\le310.
\]

The 49 selected blocks already own

\[
49\binom42=294
\]

distinct edges of `L_U`. Since there are eleven non-target colors and only seven selected colors, choose any non-target color `D` outside the selected seven. The balanced-coloring condition gives

\[
\alpha(D[U])\le12.
\]

Turan therefore forces

\[
e_D(U)\ge p_{12}(29)=22.
\]

Unique edge ownership makes these 22 edges disjoint from the selected 294, hence

\[
e(L_U)\ge294+22=316,
\]

contradicting `e(L_U)<=310` with a six-edge gap.

Thus **one unselected non-target color already closes all 554 V12 survivors and all five templates simultaneously**. The older four-color aggregate `294+4*22=382` remains a valid stronger regression check but is not load-bearing.

## E408 simplification

The earlier Q32/Q33 work remains valid but is no longer load-bearing for the shortest root chain.

`E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md` observes that the decisive exact-color-count argument only uses the 61-point E408 residual color ledger, not q=32/q=33 or a 284/285-edge core. Therefore all E408 h13 residuals are excluded directly.

The older Q33 31-point/56-witness U-reserve theorem and Q32 support-capacity theorems remain independent audits.

## Front-end machine boundary

The Line-A finite recurrence remains an explicit machine-certified step.

Receipt:

- package SHA256: `8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac`;
- 73 manifest files checked, 0 errors;
- 1,752 recurrence nodes;
- 144 outer comparisons;
- unique no-R(4,49) stop `(d,j,a,n)=(11,6,5,61)` with edge interval 397..408;
- independent replay PASS.

The historical receipt and `front_end/ASSUMPTION_LEDGER.md` still contain `T61=OPEN` / `MAIN=OPEN` because they predate this branch-local closure. They are retained as historical source state and are not the canonical status of this workstream. The root composition does not consume the old OPEN K7/K8/S31MAP/S30MAP implications.

## Contract firewall

- Q33 284-edge/excess-four identities were never imported into Q32 285-edge/excess-six proofs.
- The support-41 theorem remains a separate contract and is not needed by the root closure.
- The E407 Q32 contradiction uses the 284-edge V12 support contract, not E408 data.
- The decisive E407 contradiction does not use the Didin-dependent delta=14 subcase.
- The decisive E407 contradiction does not require the auxiliary `E407_SEVEN_EXACT_COLOR_EXCLUSION.md`.
- No floating-point optimization or heuristic solver output is load-bearing in the stated root chain.

## Current source provenance

Read-only sibling inputs were not overwritten. Important sources include:

- front-end/V9--V12 audit branch `workstream/r12-emergency-sprint-chat-20261025`;
- E407 active sibling `workstream/r12-twochat-e407-closure-20261026` (read only);
- E408 Q32/Q33 siblings (read only).

Sibling files that still say `OPEN / NOT_CERTIFIED` are historical states predating the new cross-workstream composition and are intentionally left unchanged.

## Principal new proof files

- `E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md`
- `V10_V11_Q31_INDEPENDENT_REPLAY_AUDIT.md`
- `E407_FOUR_COLOR_U_RESERVE_CLOSURE.md` — despite historical filename, current theorem uses one unselected color;
- `verify_e407_four_color_u_reserve.py` — independently recomputes the one-color six-edge gap and four-color regression;
- `R12_ROOT_CLOSURE_PROMOTION_AUDIT.md`.

## Remaining work

No new graph terminal is currently identified. Remaining work is certification and adversarial proof review:

1. freeze exact source hashes and theorem statements for every load-bearing analytic/external input, especially the exact-129 Type-I factor/support interface;
2. independently replay every load-bearing finite certificate from a clean environment;
3. audit V9/V12 analytic screens line-by-line against their finite domains;
4. reconcile the historical front-end OPEN ledger with this branch-local root receipt without erasing history;
5. merge the branch-local closure into a canonical root proof only after the dependency freeze passes;
6. ideally formalize the short root composition and the one-color U-edge reserve contradiction.
