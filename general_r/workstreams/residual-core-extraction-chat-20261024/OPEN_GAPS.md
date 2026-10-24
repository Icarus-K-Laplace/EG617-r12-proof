# Open gaps

Status date: 2026-10-24.

## GAP 1 — NO-HIGH-STOP LEMMA

Status: **`OPEN`**.

This is the only load-bearing gap remaining before the all-sufficiently-large-r front-end dichotomy.

### Exact statement to prove

For `r>=17` (or some explicit `r0`) there is no first `K_r`-free canonical state `R_a` with `a>=6` satisfying

- `|R_a|=ar+1`;
- `alpha(R_a)<=a`;
- `omega(R_a)<=r-1`;
- every induced subgraph satisfies the least-color hereditary cap;
- `e(R_a)<=B_a`, where

  `B_a=r((a+1)r-a+1)/2`.

Equivalently, canonical greedy extraction must continue until at least `a=5`.

### Why this is now isolated

- arbitrary anchor defect `s` has already been removed by induced trimming;
- if the process reaches `a=4`, Branch A is completely proved;
- if it stops at `a=5`, an exact `5r+1` terminal is defined;
- it cannot pass below `a=4` for `r>=17`.

Thus there is no second hidden front-end gap.

## Candidate route A — weighted alpha-5 extraction

For `a>5`, note the exact budget difference

`B_a-B_5=(a-5) C(r,2)`.

Also, pure random induced trimming from `ar+1` vertices down to `5r+1` improves the edge budget strongly enough:

`B_a * C(5r+1,2)/C(ar+1,2) < B_5`.

After clearing denominators, the surplus is

`r^2(a-5)(6ar^2-4ar+5r^2+6r+1)/2 >0`.

So **edge count alone is not the obstruction**: there always exists a `5r+1` induced subset with edge count below the terminal budget.

The only missing property is `alpha<=5`.

This suggests the clean reformulation:

> find a `5r+1` induced subset that simultaneously has `alpha<=5` and respects the already-available edge budget.

Equivalently, find a deletion set of size `(a-5)r` that

1. hits every independent 6-set; and
2. deletes enough incident edges to preserve `e<=B_5`.

This is a weighted transversal problem for the hypergraph of independent 6-sets.

Status: `OPEN`, but now a single precise combinatorial lemma.

## Candidate route B — hereditary-cap pressure on independent-6 transversals

If every `5r+1` induced subset has alpha at least 6, then every `(a-5)r`-vertex deletion misses some independent 6-set. In hypergraph language, the independent-6 hypergraph has transversal number at least

`(a-5)r+1`.

Try to combine this very large transversal number with the hereditary least-color cap. The cap is much stronger than ordinary Ramsey/Turan information and was exactly what closed the `delta(H)=r-1` boundary.

Status: `OPEN`.

## Candidate route C — analytic replacement of the recurrence

The r=12 recurrence at the critical `a=6` state proves an edge lower bound exactly one above the canonical budget (`475>474`). Seek an all-r inequality of the form

`e(R_6)>=B_6+1`

under the hereditary cap and `K_r`-free condition, then lift from `a>6` to `a=6` by a monotone deletion or transversal argument.

Do not parameterize all recurrence rows.

Status: `OPEN`.

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