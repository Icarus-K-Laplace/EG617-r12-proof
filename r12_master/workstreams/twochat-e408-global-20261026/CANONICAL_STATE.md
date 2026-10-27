# E408 global incidence / witness-capacity — canonical state

Updated: 2026-10-27  
Repository: Icarus-K-Laplace/EG617-r12-proof  
Dedicated branch: workstream/r12-twochat-e408-global-20261026  
Allowed write scope: r12_master/workstreams/twochat-e408-global-20261026/

## Headline

**EG617(r=12): OPEN / NOT_CERTIFIED. E408 Q33 registered 31-point/56-witness terminal: PROVED_CONDITIONAL impossible. E408 Q32: OPEN / NOT_CERTIFIED.**

The new Q33 contradiction is conditional on the retained T61/Q33 reduction, exact-129 factor theorem, shell-label classification, and the fact that every surviving Q33 branch is in the registered 31-point/56-witness minimum-support contract. It does not by itself prove the original K145 statement.

## Branch isolation and source heads

This branch was created from main HEAD 3f42fcce5761ca2372140618adda56f95fcbe253. The following sibling workstreams were read-only:

| Workstream | HEAD checked |
|---|---|
| workstream/r12-e408-q33-global-compat-20261025 | 0cb2ff3968f005c9cb255958df7c02b220678701 |
| workstream/r12-e408-q32-excess6-20261025 | a0ba6db26c7e8b00a4217dcbcbf298895dff93ce |
| workstream/r12-unified-witness-capacity-20261025 | faa8183c150dd78b000d0957fa8a63cebd52e146 |
| workstream/r12-witness-packing-chat-20261025 | f5d3daa07403877ede9885e1bd5c2f46b16d81da |
| workstream/r12-zero-excess-witness-20261025 | c8c4833c7830370a703d228ee23e3b88484d6baa |
| workstream/r12-ultimate-closure-20261024 | 1aa47d10edd5ece2b73a0891af7ac2ce37ecbb40 |

Only files under this branch's dedicated path are modified by this workstream.

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
and there are 56 selected independent four-set witnesses, seven from each of eight selected exact-129 colors.

### Q32 — 285-edge / excess-six

\[
|V(H)|=47,\quad e(H)=285,\quad \alpha(H)\le4,\quad \delta(H)\ge12,\quad
\sum_{x\in H}(d_H(x)-12)=6.
\]
The Q32 shell contract is \(q=32\), equivalently \(e(M)+G_A=32\). No Q33 284-edge identity is imported into Q32.

## Q33 Phase A — local P_C=49 status

The local profile ledger remains mathematically correct:
- \((6,2,1^5)\): PROVED_CONDITIONAL excluded.
- \((7,1^6)\): PROVED_CONDITIONAL excluded.
- \((4,4,1^5)\): all-component-edge-present branch locally OPEN.
- \((4,3,2,1^4)\): all-component-edge-present branch locally OPEN.

However, these two local OPEN profiles no longer control the global Q33 terminal: the new nonexact-color U-edge reserve contradiction bypasses them entirely.

## Q33 Phase B — global compatibility is closed under the registered terminal contract

Two ingredients are now combined.

### Ingredient 1: exact-color count capacity

`Q33_M10_EXACT_COLOR_CAPACITY_EXCLUSION.md` proves
\[
\boxed{m\ne10}
\]
for the number \(m\) of exact-129 colors, and hence \(m\in\{8,9\}\). Its preliminary W-capacity step already gives \(h\le4\), where \(h\) is the number of selected gadget witnesses. The stronger OA audit later gives \(h\le3\), but the weaker \(h\le4\) is enough for closure.

### Ingredient 2: nonexact-color U-edge reserve

Every non-target color restricted to the 31-point set \(U\) has independence number at most 12, so by Turan
\[
e_D(U)\ge p_{12}(31)=26.
\]
Of the 56 selected witnesses, \(56-h\) are exact-color component witnesses. Their six edges each are already owned by exact colors, so they occupy
\[
6(56-h)=336-6h
\]
distinct edges of \(L=\overline{H[U]}\). Since \(e(L)=336+\delta\), all nonexact colors combined have at most
\[
\delta+6h
\]
U-edge slots available. Therefore
\[
\boxed{26(11-m)\le\delta+6h.}
\]
Using only \(\delta\le17\) and \(h\le4\), the right side is at most 41. But after \(m=10\) is excluded:
- \(m=9\) requires 52 U-edges from the two nonexact colors;
- \(m=8\) requires 78 U-edges from the three nonexact colors.

Both are impossible.

Hence the registered Q33 31-point/56-witness terminal has no realization.

Proof file: `Q33_NONEXACT_U_RESERVE_CLOSURE.md`.  
Arithmetic verifier: `verify_q33_nonexact_u_reserve.py`.

## Q32 Phase C — separate 285-edge terminal

The sibling Q32 workstream proves the strict support floor \(|U|\ge44\). At \(|U|=44\), \(W=H\setminus U\) has three vertices and the two triple witnesses per exact color impose the pair-uniqueness terminal. This remains OPEN and is now the next target for this chat.

## Current commit lineage

- R7 double-star theorem: d462fe568577e4ab9204ef155da18111000312f0
- R7 verifier: 6e896507bee2d91701b173b52678788f3dfcc826
- Q33 exact-color count exclusion: 50e4f7c2299f1cb21a410779a27fdd9fd7795438
- h=4 OA obstruction: 99d85042c32a87a27d56c321c025ec55a3f978f5
- Nonexact W reserve theorem: 6b63f3491f49e222221f410279e96c61975f7083
- Nonexact W verifier: 6beddb6bee7f3a8486b54f3b92474b0de563950a
- Abstract endpoint-kernel feasibility audit: 699b18dc0982aed83f30288ccffb81f87d9bd060
- Q33 nonexact U reserve closure: 5328f7ac5302836f96f4a24cefdbef748dc9c9ed
- Q33 U-reserve arithmetic verifier: f4a133898f5527db5fa385b477cfc120021f52dc

**Current certified status of this workstream:** Q33 terminal contradiction established conditionally; Q32 remains open; EG617(r=12) remains OPEN / NOT_CERTIFIED.