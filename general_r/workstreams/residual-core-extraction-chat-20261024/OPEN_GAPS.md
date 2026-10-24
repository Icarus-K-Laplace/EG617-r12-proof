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

**Uniform partition stability is now proved.** By Füredi's quantitative Turán theorem, every non-target complement with deficit (x_i) can be made (r)-partite by deleting at most (x_i) edges. If (I_i) is the internal-edge defect and (M_i) the missing cross-pair defect, then
`I_i<=x_i`, `M_i<=2x_i`, and the edit distance to a complete multipartite graph on that partition is `<=3x_i`. The part sizes (s_j), with (q=a), satisfy `sum_j (s_j-a)^2<=4x_i+1`.

Applying the same theorem to the target complement (with (k=a), (q=r)) and summing over all colors yields a **global near-resolvable design**: at most `3S_a(r)` vertex pairs fail to be represented by exactly one block of their actual color and by no block of any other color. For fixed (a), this is (O(r)) bad pairs among (O(r^2)) total pairs.

**Remaining gap:** turn this (O(r))-defect near-design and the predecessor-interface constraint into an (r)-vertex transversal of independent 6-sets, an earlier (R_5/R_4), or a contradiction. The exceptional-pair incidence pattern is not yet classified.

Status: concentration `PROVED_SYMBOLIC`; uniform partition stability and global near-design `PROVED_ANALYTIC`; design trimming / partition incompatibility `OPEN`.

**Stronger fixed-a target rigidity is proved:** for `r>=binom(a,2)+a+1`, the target ideal parts have constant width `r-binomial(a,2)+2 <= s_j <= r+binom(a,2)-1`. Brouwer's non-partite Turán bound further gives `x_0>=r` and `x_i>=a-1`, sharpening `x_0` and `M_0`. For `a=6`, `r>=22` gives `r-8<=s_j<=r+9`, and `r>=1000` gives `|X|<=74`. The predecessor identity now also yields a partial resolvable `TD(6,r)` with at least `r^2-(29/2)r^(3/2)-67r` blocks for `r>=1000`. The remaining gap is to align the small-defect Brouwer templates with the exact predecessor classes and prove hub propagation or contradiction.

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

**Stronger exact conclusion:** for every non-target color `i`, `z_i>=1`. The vertices with a unique `i`-colored neighbor `b` in `B` split into `r` classes `S_{i,b}` of size at most `a`, because any two vertices in one class must be joined by color `i`. Hence `ar+1-z_i<=ar`, so `z_i>=1`, `sum_i z_i>=r-1`, and `q_0<=(a-1)r+2`. The exact hole identity is `sum_b(a-|S_{i,b}|)=z_i-1`; if `z_i=1`, all `r` classes have size exactly `a`.

**Stronger exact conclusion:** for every non-target color `i`, `z_i>=1`. The vertices with a unique `i`-colored neighbor `b` in `B` split into `r` classes `S_{i,b}` of size at most `a`, because any two vertices in one class must be joined by color `i`. Hence `ar+1-z_i<=ar`, so `z_i>=1`, `sum_i z_i>=r-1`, and `q_0<=(a-1)r+2`. The exact hole identity is `sum_b(a-|S_{i,b}|)=z_i-1`; if `z_i=1`, all `r` classes have size exactly `a`.

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
- The excess ledger plus Füredi's theorem gives simultaneous uniform partition stability and a global near-resolvable design with at most `3S_a(r)` bad pairs.
- In the predecessor interface, every non-target color has `z_i>=1`, so at least `r-1` vertices duplicate a non-target color and `q_0<=(a-1)r+2`.
- Brouwer's non-partite Turán bound gives `x_0>=r` and `x_i>=a-1` for every non-target color. Hence `x_0<=(binom(a,2)-a)r+2a-1` and `sum_{i>0}(x_i-(a-1))<=(binom(a,2)-a-1)r+2a-1`.
- The exact predecessor interface now yields `M_i+H_i+K_i=x_i+(a-1)z_i+1-Q_i`, plus the two-label complete-bipartite obstruction `A_b(v) x A_c(v) subset E(G_i)`. For `z_i=1`, this strengthens the excess floor to `x_i>=a-1+(|A_b|-1)(|A_c|-1)`.
- The predecessor classes are now proved to align with Füredi stability parts except for `O_a(r)` classes globally. Consequently every fixed-a high stop contains a partial resolvable `TD(a,r)` with `r^2-O_a(r)` blocks; for `a=6,r>=1000`, at least `r^2-112r` blocks.
- For fixed `a`, target ideal groups have absolute width and all internal target-complement edges localize to `|X|<=4M_0/(L-M_0/L)` hubs; after the Brouwer tightening, for `a=6` the groups have sizes `r-8` through `r+9` and at most 74 hubs suffice when `r>=1000`.
- The exact predecessor label-capacity identity gives at least `r^2-(29/2)r^(3/2)-67r` clean blocks in a partial resolvable `TD(6,r)` for `r>=1000`.
- An approximate resolvable-design skeleton with `O(a^2 r)` bad pairs is proved; an exact skeleton or design-trimming theorem is not.
- The abstract ledger assignment in `NO_HIGH_STOP_ROUND2_LEMMAS.md` passes the exact scalar ledger, predecessor increments, target partition identity, hub-count and cross-pair budgets. It is not a graph counterexample, but certifies that scalar-only rearrangements cannot close the gap.
- The local Kang–Pikhurko extremal template attains `a=6,x_i=5,z_i=6,Q_i=10`; hence neither `z_i=1` nor a uniform small-duplicate assumption is valid. A joint cross-color incidence theorem remains necessary.
- The `r^2-112r` partial-design theorem still allows `O(r)` exceptional classes; no completion theorem shows these exceptions can be removed or force an earlier stop. A finite-field `TD(6,r)` with one parallel class removed gives a design-only model with `r^2-r` blocks, so density alone cannot be the contradiction.
- New slot accounting improves the hub kernel to `7<=|X|<=28` for `a=6,r>=26272`, and the clean partial design to at least `r^2-66r` blocks. This does not yet contradict the design-only model.
- If a target group has size `r+9`, then `sum_{i>0}(x_i-5)<=20+Z_j-m_j`, where `Z_j` is its duplicate-vertex count and `m_j` its number of colors with a nonhub duplicate. Thus low duplicate concentration forces almost all non-target colors to attain the KP floor `x_i=5`.
- For `x_i=5`, KP's exact equality construction has all base parts of size six. When also `z_i=1`, the predecessor label classes form that six-set partition except for at most two explicit exceptional blocks. The `z_i>1` interface remains unclassified.
- In an `r+9` target part, at most `2 binom(k_j,2)<=756` collision units can lie in classes with at least three vertices in the part; all remaining collision units are hub–nonhub doubletons. If duplicate concentration is zero, at least `9r-765` such edges form a colored matching system.
- `NO-HIGH-STOP` remains **`OPEN`** for every claimed threshold `r>=r0`; no such `r0` has been established.

## Next highest-leverage target

Prove a **cross-group matching/KP interface theorem** for the `a=6` terminal. The most rigid subcase is a target group of size `r+9`: its hub kernel has 10–28 vertices; the collision count obeys `C_j>=9(r-1)-Z_j`; all but at most `2 binom(k_j,2)<=756` collision units are hub–nonhub doubletons; and `sum(x_i-5)<=20+Z_j-m_j`. The remaining gap is to classify `z_i>1` in the exact KP equality graph and show that the colored matchings cannot be extended consistently through the other five groups. The abstract scalar/design models show that density and local matching capacity alone are insufficient. Either derive an earlier valid `R_5` or contradict the critical-core residue windows.