# E408 global incidence / witness-capacity — canonical state

Updated: 2026-10-27  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Dedicated branch: workstream/r12-twochat-e408-global-20261026  
Allowed write scope: r12_master/workstreams/twochat-e408-global-20261026/

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.**

Within this workstream the E408 frontier is now:

- **E408 Q33 registered 31-point / 56-witness terminal: PROVED_CONDITIONAL impossible.**
- **E408 Q32 registered residual terminal: PROVED_CONDITIONAL impossible.**

Thus this branch has no remaining E408 Q32/Q33 terminal under the registered reductions. This is not promoted to the original K145 theorem until the upstream K145-to-T61/front-end reduction and every remaining sibling obligation are independently reconciled.

## Branch isolation and source heads

Read-only source heads checked during this sprint:

| Workstream | HEAD checked |
|---|---|
| workstream/r12-e408-q33-global-compat-20261025 | 0cb2ff3968f005c9cb255958df7c02b220678701 |
| workstream/r12-e408-q32-excess6-20261025 | a0ba6db26c7e8b00a4217dcbcbf298895dff93ce |
| workstream/r12-unified-witness-capacity-20261025 | faa8183c150dd78b000d0957fa8a63cebd52e146 |
| workstream/r12-witness-packing-chat-20261025 | f5d3daa07403877ede9885e1bd5c2f46b16d81da |
| workstream/r12-zero-excess-witness-20261025 | c8c4833c7830370a703d228ee23e3b88484d6baa |
| workstream/r12-ultimate-closure-20261024 | 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 |

Sibling workstreams remain read-only; only this dedicated directory is modified here.

## Contract firewall

### Q33 — 284-edge / excess-four

\[
|V(H)|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \delta(H)\ge12,\quad
\sum_{x\in H}(d_H(x)-12)=4.
\]
The registered minimum-support terminal has \(|U|=31,|W|=16\), 56 selected witnesses, and \(e(\overline{H[U]})=336+\delta\) with \(\delta\le17\).

### Q32 — 285-edge / excess-six

\[
|V(H)|=47,\quad e(H)=285,\quad \alpha(H)\le4,\quad \delta(H)\ge12,\quad
\sum_{x\in H}(d_H(x)-12)=6.
\]
The shell contract is q=32, equivalently \(e(M)+G_A=32\). No Q33 284-edge edge-count identity is used in the Q32 closure.

### Unified support-41 firewall

The unified support-41 theorem is a separate 284-edge / ten-exact-color / 41-point-support contract. It is not used in either closure below.

## Q33 — local P_C=49 status and global bypass

Local incidence-sensitive status remains:

- \((6,2,1^5)\): PROVED_CONDITIONAL excluded;
- \((7,1^6)\): PROVED_CONDITIONAL excluded;
- \((4,4,1^5)\): all-component-edge-present branch locally OPEN;
- \((4,3,2,1^4)\): all-component-edge-present branch locally OPEN.

This branch does not claim the colorwise theorem \(P_C\le48\). Instead, the global Q33 contradiction bypasses the final two profiles.

`Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md` proves m!=10 and h<=4. `Q33_NONEXACT_U_RESERVE_CLOSURE.md` then gives
\[
26(11-m)\le\delta+6h\le41.
\]
For m=9 the left side is52; for m=8 it is78. Both contradict the available U-edge capacity. Hence the registered Q33 31-point/56-witness terminal is impossible, with no four-partite/non-four-partite split remaining.

## Q32 — stronger exact-color-count contradiction

The earlier 285-edge support program proved |U|>=44 and this branch later proved every nonfull support v=44,45,46 impossible. Those results remain valid but are no longer load-bearing.

The decisive theorem is now `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`.

The outer equality ledger gives m in {8,9,10} exact-129 colors. Exact Type-I colors have one degree-nine exceptional vertex and ordinary degree at least four; `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md` makes those exceptional vertices distinct.

The full-color pointwise degree floors plus Brouwer/Kang--Pikhurko yield:

1. a 131-edge non-target color has minimum degree at least three;
2. degree-three vertices of a 130-edge color form isolated K4 components;
3. a 130-edge color has at most one isolated K4, hence at most four degree-three vertices;
4. degree-two vertices of a 132-edge color form isolated K3 components, and at most three such components can occur, hence at most nine degree-two vertices.

These close every m:

- m=10: ten distinct exact exceptional vertices force ten degree-two vertices in the unique 132-edge color, but at most nine exist;
- m=9: nine distinct exceptions force nine degree-three vertices in the 130-edge color, but at most four exist;
- m=8: every one of eight distinct exceptions needs at least two degree-three incidences among the three 130-edge colors, requiring at least16 incidences, while the three colors together can supply at most12.

Therefore
\[
\boxed{m\notin\{8,9,10\}},
\]
contradicting the E408 Q32 equality ledger. Hence the registered Q32 terminal is **PROVED_CONDITIONAL impossible**.

This Q32 closure does not use the 284-edge Q33 core, the support-41 theorem, an M[B]=empty shell split, or SAT/ILP output.

## Verification assets

- Q33 global proof: `Q33_NONEXACT_U_RESERVE_CLOSURE.md`
- Q33 arithmetic verifier: `verify_q33_nonexact_u_reserve.py`
- Q32 exact-count proof: `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`
- Q32 arithmetic verifier: `verify_q32_exact_color_count_collapse.py`
- Q32 support audit: `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md`

The computation scripts check exact arithmetic/case tables only; analytic theorem promotion remains tied to the stated proof contracts.

## Current proof status

- E408 Q33 registered terminal: **PROVED_CONDITIONAL impossible**.
- E408 Q32 registered terminal: **PROVED_CONDITIONAL impossible**.
- No live E408 terminal remains in this workstream under the registered reductions.
- E407/front-end/backend and K145-to-T61 obligations retain sibling statuses.
- EG617(r=12): **OPEN / NOT_CERTIFIED**.

## Recent commit lineage

- Q33 nonexact U-reserve closure: `5328f7ac5302836f96f4a24cefdbef748dc9c9ed`
- Q32 nonfull-support closure: `709f5638d30dc867fbf0fe7b0361d2ab550e76c3`
- Q32 exact-count proof initial version: `27d3f6a66f52a9aa0097270e76091b0c2e645904`
- Q32 all-m closure: `7148b910f0597e7082eebde21cec8a87d0b2b79a`
- Q32 arithmetic verifier: `d38f8614f3dc5b886f1473e27436cf2c426de80c`
- Q32 terminal promotion: `699f58ccf84aac0c14ad7f296d4c7e051ee9a0c5`
