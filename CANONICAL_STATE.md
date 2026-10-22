# Canonical state — 2026-10-22

## The theorem is not certified

Target: prove the `r=12` case of Erdős Problem 617. Current status: **NOT_CERTIFIED**.

## Backend

For every legitimate residual `F in R(4,49)`, a degree-13 pivot gives

`e(F)=91+q+e(H)`, with `H in R(3,35)` and clean core floor `e(H)>=211`.

Reusable assets include the q27/q28/q29 repivot machinery and the reconstructed E329--E331 closures.

### E332 is now closed

Any hypothetical E332 survivor reduces to

`q=30, e(H)=211`,

with core degree multiset `14,12^34` or `13^2,12^33`.

The full equality frontier is now eliminated analytically:

- undecorated degrees4..9 are profitable;
- d10 equality branch is empty;
- d3 equality branch is empty;
- surviving regular missing degrees reduce to `{0,1,2,11,12}`;
- the strengthened zero-gap theorem and triangle-row union lemma hold;
- decoration layers G=4,5,6 are empty;
- G=7 is empty (h0, h1 and the exact H2-G7-K4minusE cell all closed);
- G=8,h1 reduces to G=8,h0;
- G=8,h0 is empty for every decorated support size k=3..8.

Therefore

`E332 = EMPTY`.

The legal R(4,49) backend obligation is now exactly

`E333..E340`.

See `backend/E332_FULL_CLOSURE.md`.

## Front-end master reduction

The certified front-end dichotomy remains

`least-edge K145 counterexample -> induced legal R(4,49) OR embedded T61`.

The contextual recurrence is computation-certified at 1752 nodes and 144 stopping comparisons.

Within T61 the repository-canonical proved h13 layers currently run through E400.

A newer Line-A V6 source package reports a unified proof closing E401--E404, with corrected full repivot identity and a 127-row exact rational certificate. Because that ZIP has not been independently replayed in the current chat runtime, this remains marked `SOURCE_REPORTED_PROVED / INDEPENDENT_REPLAY_PENDING`.

Package-level front-end window:

`E405..E408`.

## High backend live state

Line-B V2 reports exact adjacent two-pivot exchange identities, q34/q35 compression to 76 necessary quotient rows, elimination of the triangle-free non-bipartite quotient branch, and four q30--q33 local certificates showing naive one-step `Phi=(q,tau)` monotonicity is false.

No high edge layer is closed by V2. `E333..E340` remain OPEN.

## Current independent research obligations

- Front-end: repository-canonical E401..E408; package-level E405..E408 if Line-A V6 replay is accepted;
- Backend: eliminate legal R(4,49) layers E333..E340.

There is no longer a separate low-backend E332 obligation.

## Certification warning

EG617 r=12 remains OPEN. It may be declared proved only after the remaining T61 front-end and all legal R(4,49) layers E333..E340 are closed.