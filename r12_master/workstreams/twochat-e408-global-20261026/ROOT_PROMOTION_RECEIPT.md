# EG617 fixed r=12 — root promotion receipt

Updated: 2026-10-27
Receipt class: **branch-local source-freeze / theorem-promotion audit**
Current theorem status: **PROVED_CONDITIONAL + COMPUTATION_CERTIFIED**
Unqualified `PROVED`: **NOT YET PROMOTED**

This receipt freezes the shortest currently known root chain and separates mathematical closure from publication/formalization obligations. It does not overwrite historical OPEN ledgers in sibling or front-end branches.

## 1. Root statement under audit

Assume a balanced 12-edge-coloring of `K_145` were a counterexample to EG617 at `r=12`. The audited root chain reduces it to the contextual `R(4,49)` branch or T61; the former is impossible, and every T61 branch is now excluded under the named analytic/external/certificate interfaces.

Branch snapshot immediately before this receipt:

`6e359743fe35bcc7c745764d1a6f12b691eb7a2a`

## 2. Front-end gate

### F7 bridge

Source:

- path: `front_end/FRONTEND_BRIDGE_THEOREM.md`
- blob SHA: `52b2f4af102ceba1671dc7d0e7ed36a512458e77`

Proved interface:

`balanced K145 counterexample -> contextual R(4,49) OR embedded T61`.

Finite Line-A receipt:

- package SHA256: `8f34097f195f53a6aac2999a655d3dc6a4ebc7c74f5764aedea65a79235a98ac`
- recurrence nodes: 1,752
- stopping comparisons: 144
- manifest files checked: 73
- errors: 0
- independent replay: PASS
- unique no-R(4,49) stop: `(d,j,a,n)=(11,6,5,61)`, `397<=E<=408`.

Historical `F8/T61=OPEN` inside this source is a then-current terminal status, not a premise used by the present closure.

### Contextual R(4,49) exclusion

Source:

- path: `front_end/CONTEXTUAL_R449_FULL_COLOR_IMPOSSIBILITY.md`
- blob SHA: `dd072ce9ef703b56e9184f2ede992988fce9f86e`
- status in source: `PROVED_RELATIVE_TO_BROUWER SECOND-TURAN + F5`.

This leaves T61 as the only root terminal.

## 3. Historical assumption-ledger firewall

Source:

- path: `front_end/ASSUMPTION_LEDGER.md`
- blob SHA: `eb1c0911291faa96bf74009017072fb6b6010466`.

The ledger predates the new branch-local root closure and still records `T61=OPEN` and `MAIN=OPEN`. It also contains OPEN candidate bridges `K7`, `K8`, `S31MAP`, `S31NEXT`, `S27MAP`, `S30MAP`, `S30REM`.

**None of those OPEN candidate bridges is load-bearing in the shortest root chain recorded here.** They must not be imported merely because the root is now closed by another route.

## 4. T61 low layers

The branch-local root audit imports the registered closures:

- h12;
- h13 E397--E400;
- E401--E404;
- E405;
- E406.

Promotion class: analytic registered closures under their explicit source contracts. A publication-grade bundle must still freeze each individual source theorem/blob and any external theorem statement it consumes.

## 5. E408 whole-layer gate

Source:

- path: `r12_master/workstreams/twochat-e408-global-20261026/E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md`
- blob SHA: `1da5220f5c587f4a3a392cf06f68cca5042dc4e3`
- status: `PROVED_CONDITIONAL E408 ENERGY-LAYER CONTRADICTION`.

Shortest interface does not use Q32/Q33, seven outer blocks, or a 284/285-edge core.

Load-bearing analytic inputs include the exact-129 Type-I equality structure, pointwise residual degree floors, and the registered Brouwer/Kang--Pikhurko/Turan extremal bounds.

Promotion gate: **PASS_CONDITIONAL**.

## 6. E407 low-charge gate

For a degree-13 pivot,

`407 = 91 + q + e(H)` with `e(H)>=284`, hence `q<=32`.

The audited V9 chain leaves maximum charge `Q in {31,32}` under its registered seed interface.

Small Ramsey/core seeds consumed by that chain are marked `PROVED` in the frozen front-end assumption ledger; V9 finite tables remain computation-certified.

Promotion gate: **PASS_CONDITIONAL + COMPUTATION_CERTIFIED**.

## 7. E407 Q31 gate

Source:

- path: `r12_master/workstreams/twochat-e408-global-20261026/V10_V11_Q31_INDEPENDENT_REPLAY_AUDIT.md`
- blob SHA: `8a1e7b5cbac408b531037e6ad0dfb54f9683543d`.

Frozen package hashes:

- V10 archive SHA256: `e83e2907d541b38304746e855af52b5e21b6500a35cb0fdb676a4f6a7601303a`
- V11 archive SHA256: `27ecec92d43a27fb132c60aa7b374131a860547c236d8ed3d83d3cf0eab9f0a4`
- V11 certificate SHA256: `0baffc39ee481b27af53fda36a8fe40b8cd8c527103b5126060857c4eaacd09b`.

Fresh manifests passed. Exact replay recovered V10 labelled-cut/local-neighbourhood/row-budget coverage and V11 `684 -> 349 -> 259 = 252+7` terminal-state coverage. Analytic common-K10 support capacity excludes both terminal families.

Promotion gate: **PASS_CONDITIONAL + COMPUTATION_CERTIFIED**.

## 8. E407 Q32 finite-coverage gate

Frozen V12 package:

- archive SHA256: `0c3c69a7baf94a816eff29f3a079b97ac7750d0e8b8fd2773330469c4b8c5e36`
- certificate SHA256: `cab4e67bc501fe51c06f8fc008443b870aebf8794528af1a3045e83be7d6db30`.

Independent replay recovered:

- 8,677 kernel weight vectors;
- 17,957 count states;
- 1,984 labelled necessary shells;
- 90 d3/rho1 exclusions;
- 1,192 near-K12 exclusions;
- 148 K9 pair-row refinements;
- 554 finite-screen survivors;
- all 554 mapped to five V12 rho=0 d3 shell templates.

The finite certificate does not itself claim those 554 states impossible.

Promotion gate to five templates: **COMPUTATION_CERTIFIED**.

## 9. E407 Q32 common-support gate — read-only sibling freeze

Frozen sibling branch:

`workstream/r12-twochat-e407-closure-20261026`

Observed source head:

`b36538e27dce89dfcba2aa2bfdfc29d6611a96ec`

Load-bearing sibling blobs:

1. `FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md`
   - blob SHA: `8b95bbf59e7a9232eff6cc27c9f50177533e5e21`
   - establishes the same `|U|=29`, 49-block support contract for legal completions of every one of the five V12 templates.

2. `SUPPORT_BLOCK_ANCHOR_IDENTITY.md`
   - blob SHA: `50447a9931b9b51a21a979dc61d834389abd4e3a`
   - proves every selected support block is the four-core part of a selected monochromatic exact-color K5, under the registered exact-129 factor/minimum-support identity.

3. `PROOF_DEPENDENCY_AUDIT.md`
   - blob SHA: `4b6c8ef85dce38003591c1aa712b7f9b637a68cb`
   - records the distinction between pure graph, labelled exact-129, external-input, and original-problem bridge dependencies.

This workstream does not rewrite those sibling files.

Promotion gate: **PASS_CONDITIONAL**, with exact-129 factor/support source provenance still requiring final publication-grade freeze.

## 10. E407 Q32 terminal contradiction — one-color reserve

Source:

- path: `r12_master/workstreams/twochat-e408-global-20261026/E407_FOUR_COLOR_U_RESERVE_CLOSURE.md`
- blob SHA: `b3a6a81e76cc524847a3a922c5b8b2a70029627b`.

Independent arithmetic verifier:

- path: `r12_master/workstreams/twochat-e408-global-20261026/verify_e407_four_color_u_reserve.py`
- blob SHA: `b397a57515db2112eaa9ce53405e59f8bad407e9`.

Despite the historical filename, the current theorem needs only **one** unselected non-target color.

Exact arithmetic:

- selected block edges: `49*C(4,2)=294`;
- complement cap: `294+delta <= 294+16 = 310`;
- non-target colors total: 11;
- selected colors: 7;
- therefore at least one unselected non-target color exists;
- Turan independence floor on 29 vertices: `p_12(29)=22`;
- required complement edges: `294+22=316`;
- contradiction gap: `316-310=6`.

The verifier recomputes `p_12(29)` from the balanced-partition formula rather than hard-coding 22. It also retains the older four-color `382>310` calculation as a regression check.

Promotion gate: **PASS_CONDITIONAL ANALYTIC**, arithmetic independently replayable.

## 11. Root composition

Once the gates above are accepted with their named interfaces, every branch of the root dichotomy is empty:

- contextual R(4,49): impossible;
- T61 h12: impossible;
- T61 h13 E397--E406: impossible;
- E408: impossible;
- E407 Q31: impossible;
- E407 Q32: impossible.

Therefore there is no remaining graph-theoretic terminal in the audited fixed-r=12 chain.

Current promotion:

`EG617(r=12) = PROVED_CONDITIONAL + COMPUTATION_CERTIFIED`.

## 12. Why unqualified promotion is blocked

The current blockers are **not known graph cases**. They are certification/source obligations:

1. freeze the exact source theorem and bibliographic statement for the exact-129 Type-I equality/factor theorem consumed by E408 and by the E407 selected-support identity;
2. freeze exact statements/parameter checks for every external Brouwer/Kang--Pikhurko/Andrasfai--Erdos--Sos-type theorem actually used by the shortest root chain;
3. freeze every low-layer E397--E406 theorem blob consumed by the root composition;
4. rerun all load-bearing finite packages in an independently reproduced clean environment and record verifier/source hashes;
5. line-audit V9/V12 analytic-screen assumptions against the exact finite domains;
6. reconcile stale historical `T61=OPEN` / `MAIN=OPEN` ledgers through a new canonical promotion layer rather than rewriting history.

If these gates pass without exposing a hidden premise, the natural next label is **COMPUTER-ASSISTED PROOF / publication audit passed**, not “new graph case solved.”

## 13. Fail-closed rule

Any source theorem whose exact statement/provenance cannot be frozen, any finite package whose clean replay does not reproduce the recorded certificate, or any mismatch between V12's 554-state coverage and the five-template common-support interface reopens the corresponding gate automatically.

No current receipt entry is permitted to convert a missing source audit into an unconditional theorem claim.
