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

A strengthened zero-gap repivot theorem is now proved. If `u` is undecorated and `uv` is a missing-shell edge, then

`|N_M(u) union N_M(v)| + g_v >= 13 + |D_u intersect D_v|`.

In particular, if both endpoints are undecorated, their missing-neighbourhoods cover the full 13-shell and their core rows are disjoint.

This stronger theorem closes the first two decoration layers completely:

- `G=4`: `PROVED EMPTY`;
- `G=5`: `PROVED EMPTY`.

Therefore any E332 survivor has

`G in {6,7,8}`.

Further proved reductions:

- the entire `G=6,h=0` branch is empty;
- all two-high (`h=2`) extreme shells are classified;
- no `h=2,G=8` shell exists;
- the only remaining h=2 cells are:
  - `H2-G6-K4`: two high regular vertices, two decorated vertices with total decoration6, nine lows, and the four support vertices form `K4` in M;
  - `H2-G7-K4minusE`: two high regular vertices, two decorated vertices with total decoration7, nine lows, and the support is `K4-e`, with the missing support edge between the high vertices.

Thus the active E332 frontier is now:

- `G=6,h=1` plus `H2-G6-K4`;
- `G=7,h=0 or1` plus `H2-G7-K4minusE`;
- `G=8,h=0 or1`.

The high backend layers E333..E340 remain open.

## Front-end master reduction

The certified front-end dichotomy is

`least-edge K145 colour G -> induced R(4,49) OR embedded T61`.

The contextual recurrence is computation-certified at 1752 nodes and 144 stopping comparisons.

Within T61:

- residual independence is exactly 5;
- anchor defect `z=0`;
- exact outer ledger `E+sigma+g+x6+y6=408`;
- six additional genuine K12 blocks remain in the anchor nonneighbourhood.

A q20 leaf-rotation theorem gives

`R(4,48) => e>=310`

and closes the entire T61 minimum-degree12 branch. Therefore T61 has minimum degree13.

The first four h13 edge layers are closed:

- E397: zero-decoration support contradiction;
- E398: exact q23 shell contradiction;
- E399: exact q24 cells;
- E400: uniform q25 shell theorem.

Thus the current front-end terminal is

`T61: delta=13, 401<=E<=408`.

For E401, the new shell cells are q26 with decoration G=1..4 plus the q25 `(21,4)` extension. The preferred next result is a uniform q26 / `q=22+r` stability theorem rather than unrelated casework.

## Current independent research obligations

- Front-end: close T61 h13, currently E401..E408.
- Low backend: close the reduced E332 extreme-shell frontier above.
- High backend: eliminate legal R(4,49) layers E333..E340.

## Certification warning

EG617 r=12 remains OPEN. It may be declared proved only after both the T61 front-end and every legal R(4,49) backend layer are closed.
