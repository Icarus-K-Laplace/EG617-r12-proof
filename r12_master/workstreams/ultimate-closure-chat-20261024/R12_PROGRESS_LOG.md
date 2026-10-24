# R12 progress log

## 2026-10-24 — Round 1: source audit and proof-DAG correction

### Repository actions
- Confirmed private repository Icarus-K-Laplace/EG617-r12-proof; default branch main.
- Main HEAD at workstream creation: 22cc93df4fab06ac9761e682ac06746ac42f69f4.
- Verified the target branch did not exist, then created workstream/r12-ultimate-closure-20261024 from main.
- Astra D-low branch is an ancestor of main (0 ahead / 5 behind); its comparison-time HEAD is b98bea36e36a033100b8bf09a599897cb5afd7de.
- Astra A-ext branch is divergent (66 ahead / 15 behind at comparison time). Its fetched theorem is a general-r result, explicitly PARTIAL / OPEN, and is not imported into the fixed-r=12 proof.
- All writes in this round are confined to this workstream directory.

### Mathematical audit
1. Independently checked the contextual R(4,49) edge contradiction under the exact F5 contract:
   - target floor 319;
   - each non-target color floor 79;
   - total edge count forces target at most307;
   - contradiction.
   Status: PROVED_CONDITIONAL on F5 and the cited second-Turan theorem. The 1752-node / 144-stop recurrence itself was not rerun.
2. Independently checked the E407 sharp |W|=23 Cell-B color-certificate contradiction. It closes that Cell-B subcase only, not all Q32 templates.
3. Checked the E408 exact129 blocker arithmetic: R_C>=7 and P_C<=55 follow, but these inequalities alone do not contradict the global duplicate equations.
4. Reconciled the three-anchor bound: the latest K=6 full closure gives e(H)>=214 / q<=E-305 under three independent degree-12 anchors. Older source summaries with 213 / E-304 are weaker; the support master theorem's weaker statement remains valid but should be superseded when the stronger anchor contract is met.
5. Confirmed the universal forcing-to-master extraction bridge is still OPEN: the support master theorem does not itself derive its common-S / one-loss / low-cross hypotheses from every historical shell survivor.

### Files created
- R12_CANONICAL_STATE.md — commit 0a6147cc008d5eeef4e5496881e3ad6079cbfb7d
- R12_OPEN_FRONTIERS.md — commit 11201e1c4ab455f38d3a57a315dfd4705169785a
- R12_DEPENDENCY_LEDGER.md — commit 39cb7f336276c39c3b72c8a3ee7122bf7d1ef336
- R12_PROOF_DAG.md — commit 541458ac8e1403df67d2959e0f1e6400231fa18e
- R12_FORCING_TO_MASTER.md — commit 2d471759a06684eef0b312e01e8efad3aed871b6
- R12_E407_E408_COMPATIBILITY.md — commit 9dced3393c655198ad68fc99b95875a5b1073642
- R12_FINAL_CONTRADICTION.md — commit d9384bce20de59f1fbf1a990029ba18ea95478e5
- R12_INDEPENDENT_AUDIT.md — commit 6b133f100bd0d13aacb3e31f8eacfb42cd46d757

### Current result
No open terminal contract has been eliminated in this round. The proof DAG is cleaner: the abstract R(4,49) E333–E340 program must not be mistaken for a necessary original-proof branch if the contextual F5 contract applies. The actual fixed-r=12 blocker remains T61, specifically E407 Q32 and E408 Q32/Q33.

### Next attack
Prove a joint T61 shell/core incompatibility theorem that uses the original no-R(4,49) condition on every 49-subset together with the 284-edge core and exact color-factor constraints. Do not promote source-reported V12/V8 statements without replay.

## 2026-10-24 — Round 2: shell/core witness-capacity theorem

### New proved statement
Committed R12_SHELL_CORE_WITNESS_LEMMA.md at 020b64d5fdf3a4aa3abe66d86be3489565760b22.

1. **Small-row lemma.** For a T61 shell vertex a, t_a<=7 implies alpha(H\N_H(a))=4. If alpha were <=3, the induced n=47-t_a vertex graph has n in [40,47], alpha<=3 and omega<=11. Brouwer's second-Turan lower bound exceeds the inherited target-edge cap D(n) for each of these eight n-values.
2. **Pair-extension lemma.** Every target edge ab in F[A] has at least one good endpoint, since H union {a,b} is a 49-set and must have alpha>=5. Hence at most five shell rows are bad and at least eight are good.
3. **Q33/d3 consequence.** The exact budget beta+X+G_B=3 gives g_b<=3, and k_b<=3, so t_b<=6 for every b in B. All ten B-rows therefore have independent-4 witnesses Q_b. If ab is a missing target edge, Q_b must intersect N_H(a); otherwise Q_b union {a,b} is an independent 6-set. The scalar budget guarantees at least five B-vertices with k_b>=2, so at least five witnesses hit at least two S-rows.

### Quantified impact
- New proved interface constraints: 1 theorem with 3 consequences.
- Open terminal contracts eliminated: **0**.
- E407 Q32 / E408 Q32/Q33 range: narrowed only by an added witness-incidence condition; no terminal exclusion claimed.
- Independent arithmetic check: exact values p_3(n)+floor(n/3)-1 versus D(n), n=40..47, all strictly exceed the cap (minimum gap 7 at n=40).
- GitHub commit: 020b64d5fdf3a4aa3abe66d86be3489565760b22 for the theorem file; follow-up state updates are being committed in this sequence.
- Next attack: turn the Q33 witness condition into a capacity contradiction using the four-unit core excess and seven-block near-Latin completion. Do not assume Q_b coincide or that aggregate defects vanish.
