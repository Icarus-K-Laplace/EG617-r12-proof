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
- every high stop contains an induced `(r+1)`-critical core of order at least `3r-1`, whose order `lr+t` must satisfy the exact polynomial feasibility test `P_{l,t}(r)<=0` from `RECURRENCE_REPLACEMENT_POTENTIALS.md`.

Thus there is no second hidden front-end gap.

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

`a(a-1)/2-1`.

Thus at least one non-target colour is only O(a^2) edges above its exact `p_r(ar+1)` minimum; in fact a positive fraction of the non-target colours have O(a^2) excess by Markov.

The complement of such a colour is K_{r+1}-free and O(a^2) edges below the r-partite Turan maximum. The intended next step is an exact/stability partition theorem producing r near-blocks of size about a. Because different colour classes are edge-disjoint, many such near-partitions should behave like a partial resolvable design.

Target implication:

> either these near-partitions yield a `5r+1` induced alpha-5 subset, or they satisfy an exact resolvable-design contract that can be closed separately.

Status: `OPEN`; this is currently the preferred route.

## Candidate route D — critical-core residue potential

Every high stop contains an `(r+1)`-critical induced core `Q` with

`|Q|>=3r-1`.

Writing `|Q|=lr+t`, `0<=t<r`, the hereditary cap and Kostochka--Yancey imply

`P_{l,t}(r)<=0`.

For fixed l and large r, this excludes middle residues and confines the core order to bounded-width windows around multiples of r. This is a genuine bounded-width reduction and may be coupled to Route C.

Status: `PROVED_ANALYTIC` as a reduction; it does not by itself close GAP 1.

## GAP 2 — existence/closure of the 5r+1 terminal

Status: `OPEN`, but **not load-bearing for the extraction dichotomy** once GAP 1 is proved.

An irreducible terminal has the exact contract in `FIVE_R_TERMINAL.md`, including

- `alpha=5` automatically;
- independent-5 hypergraph transversal number `>=r+1`;
- `delta>=r`;
- hereditary cap;
- `e<=3r^2-2r`.

Next structural question: does this force a bounded 5-type / finite-geometric incidence system, or can the terminal be excluded outright?

## GAP 3 — finite range below 17

Status: `OPEN`.

The analytic residual-core theorem proves `delta(H)>=r` for `r>=17`. The boundary `6<=r<=16` is not addressed. This finite range is not relevant to an all-sufficiently-large-r theorem and should not distract from GAP 1 unless an all-r result is specifically required.