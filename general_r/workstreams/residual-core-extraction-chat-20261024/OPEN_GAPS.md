# Open gaps

Status date: 2026-10-24.

## GAP 1 — NO-HIGH-STOP LEMMA

Status: **`OPEN`**.

This is the only load-bearing gap remaining before the all-sufficiently-large-r front-end dichotomy.

### Exact statement to prove

For `r>=17` (or some explicit `r0`) there is no first `K_r`-free canonical state `R_a` with `a>=6` satisfying

- `|R_a|=ar+1`;
- **`alpha(R_a)=a`**;
- `omega(R_a)<=r-1`;
- every induced subgraph satisfies the least-color hereditary cap;
- `e(R_a)<=B_a`, where

  `B_a=r((a+1)r-a+1)/2`;

- the exact all-colour excess ledger

  `x_0+sum_{i=1}^{r-1}x_i=S_a(r)`

  with

  `S_a(r)=[a(a-1)r+2a-2r]/2`.

Equivalently, canonical greedy extraction must continue until at least `a=5`.

### Why this is now isolated

- arbitrary anchor defect `s` has already been removed by induced trimming;
- if the process reaches `a=4`, Branch A is completely proved;
- if it stops at `a=5`, an exact `5r+1` terminal is defined;
- it cannot pass below `a=4` for `r>=17`;
- alpha is automatically saturated at every canonical state;
- every high stop contains an induced `(r+1)`-critical core of order at least `3r-1`, whose order `lr+t` must satisfy the exact polynomial feasibility test `P_{l,t}(r)<=0`;
- at least half the non-target colors are within `a^2-1` edges of the exact Turán maximum in their complements;
- the predecessor clique interface is an exact near-permutation/duplicate-color condition.

Thus there is no second hidden front-end gap, but the structural theorem itself remains open.

## Candidate route A — weighted alpha-5 extraction

For `a>5`,

`B_a-B_5=(a-5) C(r,2)`.

Pure random induced trimming from `ar+1` vertices down to `5r+1` improves the edge budget strongly enough:

`B_a * C(5r+1,2)/C(ar+1,2) < B_5`.

After clearing denominators, the margin is

`r^2(a-5)(6ar^2-4ar+5r^2+6r+1)/2 >0`.

So **edge count alone is not the obstruction**. The only missing property is `alpha<=5`.

Equivalent deletion form:

> find a deletion set of size `(a-5)r` which hits every independent 6-set while retaining the already-available edge margin.

This is a weighted transversal problem for the independent-6 hypergraph.

Status: `OPEN`.

## Candidate route B — independent-6 transversal rigidity

If every `5r+1` induced subset has alpha at least 6, then the independent-6 hypergraph has transversal number at least

`(a-5)r+1`.

Combine this large transversal number with:

- exact alpha saturation;
- the hereditary cap;
- the critical-core lower order `>=3r-1`;
- the all-colour slack ledger.

The goal is an O(1)-condition design terminal, not a new case tree.

Status: `OPEN`.

## Candidate route C — multicolour near-Turan partitions

The exact ledger gives

`min_{i>=1} x_i <= floor(S_a(r)/(r-1))`.

For fixed a and large r this tends to

`a(a-1)/2 - 1`.

The new simultaneous-concentration theorem is stronger:

- at least `floor(r/2)` non-target colors have excess `x_i<=C_{a,r}`;
- `C_{a,r}=ceil(2S_a(r)/(r-1))<=a^2-1`;
- for `a=6,r>=41`, at least `floor(r/2)` colors have `x_i<=29`.

For each such color, the complement is `K_{r+1}`-free and has exactly `x_i` fewer edges than the Turán maximum.

**Remaining gap:** prove a uniform-in-`r` edit-distance stability lemma for `K_{r+1}`-free graphs on `ar+1` vertices with Turán deficit `O(a^2)`. Standard stability statements with constants depending on fixed clique parameter cannot be applied while silently letting that parameter grow with r.

If this is proved, then compare the resulting partitions. Pairwise intersections of exact color-clique blocks are at most one; for approximate partitions, all defect edges must be tracked explicitly.

Status: concentration `PROVED_SYMBOLIC`; uniform partition stability and partition incompatibility `OPEN`.

## Candidate route D — critical-core residue potential

Every high stop contains an `(r+1)`-critical induced core `Q` with

`|Q|>=3r-1`.

Writing `|Q|=lr+t`, `0<=t<r`, the hereditary cap and Kostochka--Yancey imply

`P_{l,t}(r)<=0`.

The new explicit residue-window theorem says that, for

`r>=R_l=l(l-1)^2(l-2)+2l+2`,

feasibility forces

`t<=l^2-3l+1` or `r-t<=l^2-l-1`.

For `a=6`, `r>=614`, this reduces the possible core order to

- `[3r-1,3r+1]`;
- `[4r-5,4r+5]`;
- `[5r-11,5r+11]`;
- `[6r-19,6r+1]`.

All middle residues are eliminated, but none of these surviving windows is yet eliminated. The critical-core potential alone does not prove A-N1.

Status: bounded-width reduction `PROVED_ANALYTIC`; surviving-window elimination `OPEN`.

## Candidate route E — predecessor clique / K_r-transversal interface

Let `B=K_r` be the target-color clique removed from predecessor `R_{a+1}` to form first stop `R_a`.

For each `v in R_a`, the edges `vB` must contain every non-target color. Therefore:

- either one edge has target color and every non-target color occurs exactly once;
- or no edge has target color and exactly one non-target color occurs twice.

If `q_0` is the number of target cross-edges and `z_i` counts the duplicated non-target color `i`, then

`sum z_i=ar+1-q_0`,

`x_0(R_{a+1})=x_0(R_a)+q_0`,

`x_i(R_{a+1})=x_i(R_a)+z_i`.

This is a new exact interface constraint and gives monotone excesses backward through the greedy process.

**Remaining gap:** turn the near-permutation interface and the clique-transversal property into an induced `R_{a-1}` theorem or an exact design-trimming contradiction.

Status: interface `PROVED_SYMBOLIC`; high-a induction `OPEN`.

## GAP 2 — existence/closure of the 5r+1 terminal

Status: `OPEN`, but **not load-bearing for the extraction dichotomy** once GAP 1 is proved.

An irreducible terminal has the exact contract in `FIVE_R_TERMINAL.md`, including

- `alpha=5`;
- independent-5 hypergraph transversal number `>=r+1`;
- `delta>=r`;
- hereditary cap;
- `e<=3r^2-2r`.

Next structural question: does this force a bounded 5-type / finite-geometric incidence system, or can the terminal be excluded outright?

## GAP 3 — finite range below 17

Status: `OPEN`.

The analytic residual-core theorem proves `delta(H)>=r` for `r>=17`. The boundary `6<=r<=16` is not addressed. This finite range is not relevant to an all-sufficiently-large-r theorem and should not distract from GAP 1 unless an all-r result is specifically required.

## Current verdict

- `a=6` is **not closed**.
- No induced `R_{a-1}` extraction theorem for arbitrary `a>=7` is proved.
- The excess ledger yields simultaneous near-extremality in edge count, but not yet simultaneous structural stability.
- No exact resolvable-design skeleton has been proved.
- `NO-HIGH-STOP` remains **`OPEN`** for every claimed threshold `r>=r0`; no such `r0` has been established.

## Next highest-leverage target

Prove the uniform Turán edit-stability lemma in Candidate C for the first case `a=6`, then combine it with the predecessor interface and the four critical-core residue windows. Do not return to fixed-r recurrence, and do not promote a necessary residue condition to a contradiction.