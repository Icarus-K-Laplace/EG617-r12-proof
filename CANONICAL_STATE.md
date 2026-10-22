# Canonical state — 2026-10-22

## The theorem is not certified

Target: prove the `r=12` case of Erdős Problem 617. Current status: **NOT_CERTIFIED**.

## Backend

For every legitimate residual `F in R(4,49)`, a degree-13 pivot gives

`e(F)=91+q+e(H)`, with `H in R(3,35)` and clean core floor `e(H)>=211`.

Reusable assets:

- q28 profitable repivot;
- generic q29 good-repivot, independent of the special 211-edge equality value;
- uniform q27 contradiction with explicit Type-I/II dependency.

E329, E330 and E331 are closed. Any E332 survivor reduces to

`q=30, e(H)=211`,

with 211-core degree multiset `14,12^34` or `13^2,12^33`.

### Major E332 reduction

The old q30 equality frontier has been sharply reduced.

- undecorated degrees4..9 are profitable and impossible;
- the full d10 equality branch is `PROVED EMPTY`;
- the full d3 equality branch is `PROVED EMPTY`;
- every remaining undecorated missing degree lies in `{0,1,2,11,12}`;
- at most two undecorated degree11/12 vertices exist.

A strengthened zero-gap repivot theorem is proved. If `u` is undecorated and `uv` is a missing-shell edge, then

`|N_M(u) union N_M(v)| + g_v >= 13 + |D_u intersect D_v|`.

In particular, if both endpoints are undecorated, their missing-neighbourhoods cover the full 13-shell and their core rows are disjoint.

The decoration layers

- `G=4`,
- `G=5`,
- `G=6`

are all `PROVED EMPTY`.

The full `G=7,h=0` branch is now also `PROVED EMPTY`. Its closure eliminates k=3,4,5 directly and then all high-incidence k=6,7 cells by active/inactive support counting, degree1/2 low-repivot inequalities, pair-row coverage, and the triangle-row union lemma.

Therefore the active E332 frontier is now exactly:

- `G=7,h=1`;
- the exact `H2-G7-K4minusE` cell;
- `G=8,h=0`;
- `G=8,h=1`.

There is no h=2,G=8 state.

The high backend layers E333..E340 remain open.

## Front-end master reduction

The certified front-end dichotomy is

`least-edge K145 colour G -> induced R(4,49) OR embedded T61`.

The contextual recurrence is computation-certified at 1752 nodes and 144 stopping comparisons.

Within T61:

- residual independence is exactly5;
- anchor defect `z=0`;
- exact outer ledger `E+sigma+g+x6+y6=408`;
- six additional genuine K12 blocks remain in the anchor nonneighbourhood.

A q20 leaf-rotation theorem gives

`R(4,48) => e>=310`

and closes the entire T61 minimum-degree12 branch. Therefore T61 has minimum degree13.

Repository-canonical proved h13 layers are currently E397--E400.

A newer Line-A V6 package reports a unified proof closing E401--E404 and shrinking the package-level front-end window to

`E405..E408`.

The package also reports a corrected complete repivot identity and removes `(q,z,G)=(25,21,4)` as an illegal cell via `D(14)=69`. The source package reports a 127-row rational certificate replayed successfully. Because the uploaded ZIP could not be independently unpacked in the current chat runtime, this result remains separately marked `SOURCE_REPORTED_PROVED / INDEPENDENT_REPLAY_PENDING` rather than silently represented as independently replayed here.

## High backend live state

A newer Line-B V2 package reports:

- the complete adjacent two-pivot exchange system;
- exact q and tau difference identities;
- proof that reverse-pivot equality is not an independent second inequality;
- q34--q35 true-twin compression to 76 necessary quotient rows;
- elimination of the triangle-free non-bipartite quotient branch;
- four exact q30--q33 local certificates showing naive one-step Phi monotonicity is false.

No high edge layer is closed by V2. E333--E340 all remain OPEN.

## Current independent research obligations

- Front-end: repository-canonical E401..E408, with a newer source package reporting E401..E404 closed; package-level remaining window E405..E408;
- Low backend: close `G=7,h=1`, `H2-G7-K4minusE`, `G=8,h=0`, `G=8,h=1`;
- High backend: eliminate legal R(4,49) layers E333..E340 using third-pivot/joint-row/nonadjacent-pivot constraints rather than naive local Phi monotonicity.

## Certification warning

EG617 r=12 remains OPEN. It may be declared proved only after both the T61 front-end and every legal R(4,49) backend layer are closed.
