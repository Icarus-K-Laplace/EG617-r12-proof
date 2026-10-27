# E408 global incidence / witness-capacity — canonical state

Updated: 2026-10-27  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Dedicated branch: workstream/r12-twochat-e408-global-20261026  
Allowed write scope: r12_master/workstreams/twochat-e408-global-20261026/

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED.**

Within this workstream:

- **E408 Q33 registered 31-point / 56-witness terminal: PROVED_CONDITIONAL impossible.**
- **E408 Q32 nonfull supports v=44,45,46: PROVED_CONDITIONAL impossible.**
- **E408 Q32 unique surviving support terminal: v=47, U=H, OPEN.**

The Q33 contradiction is conditional on the retained T61/Q33 reduction, exact-129 factor theorem, shell-label classification, and the registered 31-point/56-witness minimum-support terminal. It does not by itself prove the original K145 statement.

## Branch isolation and source heads

The following sibling workstreams are read-only inputs:

| Workstream | HEAD checked |
|---|---|
| workstream/r12-e408-q33-global-compat-20261025 | 0cb2ff3968f005c9cb255958df7c02b220678701 |
| workstream/r12-e408-q32-excess6-20261025 | a0ba6db26c7e8b00a4217dcbcbf298895dff93ce |
| workstream/r12-unified-witness-capacity-20261025 | faa8183c150dd78b000d0957fa8a63cebd52e146 |
| workstream/r12-witness-packing-chat-20261025 | f5d3daa07403877ede9885e1bd5c2f46b16d81da |
| workstream/r12-zero-excess-witness-20261025 | c8c4833c7830370a703d228ee23e3b88484d6baa |
| workstream/r12-ultimate-closure-20261024 | 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 |

Only files under this branch's dedicated path are modified here.

## Contract firewall

### Q33 — 284-edge / excess-four

\[
|V(H)|=47,\quad e(H)=284,\quad \alpha(H)\le4,\quad \delta(H)\ge12,\quad
\sum_{x\in H}(d_H(x)-12)=4.
\]
At the registered minimum-support boundary:
\[
|U|=31,\quad |W|=16,\quad e(L)=336+\delta,\quad \delta\le17,
\]
with 56 selected independent four-set witnesses.

### Q32 — 285-edge / excess-six

\[
|V(H)|=47,\quad e(H)=285,\quad \alpha(H)\le4,\quad \delta(H)\ge12,\quad
\sum_{x\in H}(d_H(x)-12)=6.
\]
The shell contract is \(q=32\), equivalently \(e(M)+G_A=32\). No Q33 284-edge identity is imported into Q32.

### Unified support-41 firewall

The unified witness-capacity support-41 theorem is a separate 284-edge / ten-exact-color / 41-point-support contract. It is **not** imported into Q33 support-31 or Q32 support-47 arguments unless its full hypotheses are independently derived.

## Q33 Phase A — local P_C=49 status

- \((6,2,1^5)\): PROVED_CONDITIONAL excluded.
- \((7,1^6)\): PROVED_CONDITIONAL excluded.
- \((4,4,1^5)\): all-component-edge-present branch locally OPEN.
- \((4,3,2,1^4)\): all-component-edge-present branch locally OPEN.

These last two local profiles no longer control the global Q33 terminal because the global U-edge reserve contradiction bypasses them. Therefore this branch does **not** claim the colorwise theorem \(P_C\le48\).

## Q33 Phase B — registered terminal contradiction

`Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md` proves \(m\ne10\), so \(m\in\{8,9\}\), and gives the preliminary gadget count \(h\le4\).

`Q33_NONEXACT_U_RESERVE_CLOSURE.md` then uses:

1. every non-target color on the 31-point U has at least \(p_{12}(31)=26\) U-edges;
2. the \(56-h\) exact-color component witnesses own \(336-6h\) distinct U-edges;
3. \(e(L)=336+\delta\), \(\delta\le17\).

Hence all nonexact colors must satisfy
\[
26(11-m)\le\delta+6h\le17+24=41.
\]
But \(m=9\) requires 52 edges and \(m=8\) requires 78. Contradiction.

Therefore the registered Q33 31-point/56-witness terminal is **PROVED_CONDITIONAL impossible**, simultaneously covering four-partite and non-four-partite L branches.

## Q32 Phase C — all nonfull supports eliminated

The sibling Q32 workstream supplies the support floor \(|U|\ge44\) and the exhaustive Type-I shell-support classification. This branch additionally proves global exceptional-vertex injectivity.

`Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md` gives the uniform closure:

- take any \(w\in H\setminus U\);
- for each exact color C, either \(w=x_C\), or w lies in the core part of C's multi-outside K5;
- exceptional injectivity allows \(w=x_C\) for at most one exact color;
- in every other exact color, the multi-outside K5 supplies at least two distinct C-neighbors of w in the 13-point shell A;
- these shell edges have distinct colors, so their shell endpoints are distinct across exact colors;
- therefore w would need at least \(2(m-1)\ge14\) shell neighbors in a 13-point shell.

Contradiction. Thus
\[
\boxed{U=H,\qquad |U|=47.}
\]

This subsumes the earlier v=44 closure and v=45 reduction. The only remaining Q32 support terminal is full support v=47.

## Q32 full-support v=47 exact ledger

The 285-edge core has
\[
e(\overline H)=\binom{47}{2}-285=796.
\]
Classify exact Type-I colors into A/B/C shell patterns with counts \(a,b,c\), \(a+b+c=m\), where A and C yield eleven single-outside K5 core witnesses and B yields ten. Then
\[
N=11m-b
\]
selected component K4 witnesses consume
\[
6N=66m-6b
\]
distinct non-target core edges. Their total omitted-point incidence is
\[
3a+7b+3c=3m+4b.
\]

The eleven non-target colors each have at least \(p_{12}(47)=69\) H-edges, so the entire coloring has only
\[
796-11\cdot69=37
\]
core edges above this baseline. The current attack is to force more than 37 excess edges by combining Type-I shell structure, omission multiplicities, nonexact-color near-Turan structure, and seven-block blocker incidence.

This is an exact reduction, not yet a contradiction.

## Current proof status

- Q33 registered terminal: **PROVED_CONDITIONAL impossible**.
- Q32 v=44,45,46: **PROVED_CONDITIONAL impossible**.
- Q32 v=47 full support: **OPEN**.
- Original K145-to-T61 bridge and other backend/front-end obligations retain sibling statuses.
- EG617(r=12): **OPEN / NOT_CERTIFIED**.

## Recent commit lineage

- Q33 nonexact U-reserve closure: `5328f7ac5302836f96f4a24cefdbef748dc9c9ed`
- Q32 nonfull-support shell-capacity closure: `709f5638d30dc867fbf0fe7b0361d2ab550e76c3`
- Q32 terminal frontier promotion to v=47 only: `59beb7116175db64ee37b5b440369dc08742fcef`
