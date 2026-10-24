# R12 dependency ledger

Audit date: 2026-10-24  
Branch: `workstream/r12-master-closure-20261024`  
Base: `b98bea36e36a033100b8bf09a599897cb5afd7de`  
Audit policy: theorem status is inherited only with its explicit contract and dependency closure.

## 1. Original K145 reduction and front-end recurrence

| Node | Required input / contract | Canonical evidence | Status boundary |
|---|---|---|---|
| Original balanced counterexample | A 12-edge-coloring of K145 with every color independent number at most12; least-edge target color chosen as in the reduction. | Root `PROOF_DAG.md`, `front_end/FRONTEND_BRIDGE_THEOREM.md`, `front_end/CONTEXTUAL_R449_FULL_COLOR_IMPOSSIBILITY.md`. | The reduction is valid only under its full least-edge / balanced-coloring assumptions. |
| Contextual recurrence | Exact state-transition and stopping contract, including all contextual conditions. | `front_end/RECURRENCE_PROOF.md`, machine recurrence/certificate assets, root `ASSET_LEDGER.md`. | 1752-node / 144-stop arithmetic certification is not by itself a graph-level contradiction. |
| Front-end dichotomy | Every original counterexample yields a legal R(4,49) residual or a T61 terminal. | `front_end/FRONTEND_BRIDGE_THEOREM.md` and recurrence certificate. | Must verify the stopping contract is exactly the one derived from the original counterexample; no missing states. |
| T61 h12 | The inherited T61 residual contract and h12 branch assumptions. | Canonical h12 assets referenced by `PROOF_DAG.md`. | Closed in the current canonical DAG under those assumptions. |
| T61 h13, E397--E406 | T61 contract, pivot/degree and inherited lower-order seed contracts used in each closure. | `front_end/E401_E404_CANONICAL_CLOSURE.md`, `E405_FULL_CLOSURE_CANONICAL.md`, `E406_FULL_CLOSURE.md`, linked lower-layer lemmas. | Closed in the canonical proof chain, but not to be detached from inherited assumptions. |
| T61 h13, E407 | V11/V12 retained-seed contracts, then shell/core completion. | `front_end/T61_H13_V11_SOURCE_AUDIT.md`, `consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md`, Cell-B closure files. | Q31 remains source-reported conditional; Q32 has five source-reported common-K11 templates and an open 284-core compatibility bridge. |
| T61 h13, E408 | V11 retained-seed contract and full Q32/Q33 completion constraints. | `front_end/T61_H13_V11_SOURCE_AUDIT.md`, `E408_GLOBAL_SEVEN_BLOCK_EQUALITY_SYSTEM.md`, `E408_EXACT129_BLOCKER_DUPLICATE_THEOREM.md`, `E408_Q33_CORE_ALMOST_REGULAR_NORMAL_FORM.md`, `E408_Q33_D3_EXACT_BUDGET.md`. | Q31 source-reported conditional; Q32/Q33 open. The d3 exact budget is a necessary-condition lemma only. |

## 2. R(4,49) backend chain

For a legal residual F, `E=91+q+e(H)`. CORE211 gives `e(H)>=211` under its full residual-core contract. The three-anchor theorem strengthens this to `e(H)>=214` when three independent degree-12 anchors are actually established.

| Node | Required input / contract | Canonical evidence | Status boundary |
|---|---|---|---|
| Legal backend reduction | A genuine 49-point induced residual with `alpha(F)<=4`, `omega(F)<=11`, `delta(F)=13`, and all inherited induced-set caps. | Root bridge / backend DAG assets. | The residual must be shown to satisfy every cap; an arbitrary 49-vertex graph is not enough. |
| CORE211 | 35-point core H with `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`. | `backend/CORE211.md` and the clean core proof it references. | Edge floor is conditional on the all-pivot minimum-degree-12 contract; the proof-completeness audit notes the inherited cap-two/23-neighbourhood argument as a self-containment gap. |
| q27/q28/q29 | Exact pivot/re-pivot identities, q-maximality and the specific equality/topology contracts. | `consolidation/Q27_ANALYTIC_EQUALITY_CLOSURE.md`, `backend/Q29_GOOD_REPIVOT_FULL_PROOF.md`, and the q28/q29 assets. | E329--E332 use these as dependencies; preserve their exact equality/topology assumptions. |
| E329--E332 | Legal backend residual and CORE211 plus the q27/q28/q29 chain. | `backend/E329_E332_CLOSURE.md`, `backend/E332_FULL_CLOSURE.md`. | Closed relative to the registered dependencies; not a raw-K145 standalone proof. |
| E333 | Legal E333 residual, all-pivot core floor, canonical V4 forcing to the five repeated-pair families, and V5 capacity/exact-ledger arguments. | `backend/E333_V5_CANONICAL_CLOSURE.md`. | Proof body and arithmetic replay support `PROVED_RELATIVE_TO_CANONICAL_V4`; V4 and upstream legality remain retained dependencies. |
| E334 | Legal E334 residual plus V7 forcing into the only reported q32/core211 channel and the connector-excess lemma, then the K>=8 graph theorem. | `consolidation/V12_V8_SOURCE_REPORTED_AUDIT.md`, `backend/GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`, `GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md`. | The K>=8 graph theorem is analytic. The V7/V8 extraction that every E334 survivor satisfies its three-anchor contract remains source-reported pending replay. |
| E335--E340 | Every legal maximal-pivot survivor must either yield three anchors, or satisfy the common-S support contract, or be eliminated in a finite higher-slack equality reduction. | `backend/GLOBAL_THREE_ANCHOR_BACKEND_ENVELOPE.md`, `GLOBAL_FORCING_TO_MASTER_ALLOWANCE_COVERAGE.md`, `GLOBAL_FORCING_TO_MASTER_V3_SYNTHESIS.md`, `GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md`. | OPEN: exhaustive extraction plus remaining higher-slack d2/d3 cases. |

## 3. Support-compatibility dependency graph

The reusable common-S stack is conditional, not an automatic theorem about every shell:

1. Exact common-S exchange / row-closure identities.
2. Lexicographic maximality of `(q,tau)`, giving the repeated-support strict-loss rule.
3. Zero-charge incidence signatures and the signature/anchor dichotomy.
4. If three signatures occur: three independent degree-12 anchors; `GLOBAL_THREE_ANCHOR_K6_FULL_CLOSURE.md` yields `K>=8), hence `q<=E-305`.
5. If at most two signatures occur: zero-skeleton/sunflower patterns, but only for the boundary one-loss contract.
6. Low-cross hypotheses imply matching/transversal bounds.
7. Hereditary packing bounds each canonical pattern's owner capacity.
8. Higher-slack rows must be descended or classified before steps 4--7 can be applied.

Key sources:

- `backend/GLOBAL_SUPPORT_COMPATIBILITY_THEOREM.md`;
- `backend/GLOBAL_SUPPORT_COMPATIBILITY_MASTER_THEOREM.md`;
- `backend/GLOBAL_ZERO_CHARGE_INCIDENCE_SIGNATURE_THEOREM.md`;
- `backend/GLOBAL_ZERO_SIGNATURE_ANCHOR_ALIGNMENT_THEOREM.md`;
- `backend/GLOBAL_FIRST_HIGH_SLACK_MASTER_REDUCTION.md`;
- `backend/GLOBAL_FORCING_TO_MASTER_ALLOWANCE_COVERAGE.md`;
- `backend/GLOBAL_FORCING_TO_MASTER_V3_SYNTHESIS.md`.

The new workstream theorem `r12_master/workstreams/master-closure-chat-20261024/R12_D3_MULTIS_EXTRACTION_BOUND.md` adds the exact class-size allowance bound `a_S<=q-30-N+n` for d3 owner families through q=38. It is derived from the V3 zero-gap identity and exact exchange formula; it does not close lower-owner or fully-decorated branches.

The master theorem's low-cross bounds and boundary one-loss equality are hypotheses. They cannot be inferred from signature count alone.

## 4. External theorem dependencies

The current assets explicitly use or cite, among others:

- Andrásfai–Erdős–Sós for the K4-free / minimum-degree 3-partite implication in CORE211-style arguments;
- Brouwer/Kang–Pikhurko second-Turán extremal/equality results for the T61 non-target colors and E407/E408 local classifications;
- Füredi-style quantitative Turán stability in the multicolor d3 stability theorem.

For each use, the eventual proof manuscript must retain the precise parameter range and equality/non-partite hypotheses. This ledger does not substitute for the bibliographic/source-scope audit noted in `PROOF_COMPLETENESS_AUDIT.md`.

## 5. Non-circularity check

The intended proof DAG is acyclic:

- original counterexample -> front-end dichotomy -> T61 or R(4,49);
- T61 -> E397--E408 case closures;
- R(4,49) -> E329--E340 case closures;
- local support/anchor lemmas are invoked only after their contracts have been established.

A circularity would arise if the forcing-to-master theorem assumed the same common-S extraction that it is supposed to prove, or if a T61 terminal closure were used to establish a backend extraction contract without an explicit independent reduction. No such circular step is certified by the current open assets; the extraction remains a genuine missing node.
