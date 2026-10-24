# Canonical state — general-r residual-core extraction

Workstream branch: `workstream/general-r-residual-core-extraction-20261024`

Directory: `general_r/workstreams/residual-core-extraction-chat-20261024/`

Last major mathematical state: 2026-10-24.

## PROVED

### 1. R12 provenance map

Status: `PROVED_SYMBOLIC` / `SOURCE_REPORTED`.

- `r^2+1`, `5r+1`, `4r+1`, `3r-1`, `r+1` are genuinely structural orders.
- The r=12 proof of residual minimum degree depends on lower-order Ramsey seeds and is not itself an all-r proof.
- File: `R12_TO_GENERAL_DEPENDENCY_MAP.md`.

### 2. Outer-ray invariant and trimming normalization

Status: `PROVED_SYMBOLIC`.

For anchor degree `d=r-s`, after `j` extracted `K_r` blocks with `a=r-1-j`,

`n=ar+s`, so `n-ra=s` is invariant.

Induced-subgraph averaging collapses every `s>=1` state to the critical `s=1` state `ar+1` without worsening the canonical edge budget.

Files:

- `OUTER_RAY_INVARIANT.md`;
- `ANCHOR_NORMALIZATION_AND_GREEDY_EXTRACTION.md`.

### 3. Minimum-degree anchor source

Status: `PROVED_ANALYTIC`.

For `r>=3`, the least-color graph has a minimum-degree anchor with `d<=r-1`.

Proof: averaging plus Brooks; `delta>=r` would make the graph r-regular while `alpha<=r` forces chromatic number at least `r+1`.

### 4. General residual-core minimum degree — LEVEL A

Status: **`PROVED_ANALYTIC`**.

For every `r>=17`, any graph `H` on `3r-1` vertices satisfying

- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- the inherited least-color hereditary cap

must satisfy

> **`delta(H)>=r`.**

Key chain:

- exact `2r` exclusion;
- boundary `d=r-1` compressed to a non-bipartite triangle-free graph on `2r-1` with edge count `(r-1)^2` or `(r-1)^2+1`;
- shortest odd cycle forced to `C5`;
- remainder forced to one of three near-complete-bipartite forms;
- hereditary cap gives every boundary row defect at most 8;
- any complement edge inside the `r-1` neighbor set requires two row defects summing to at least `r`;
- clique cap forces such an edge;
- contradiction for `r>=17`.

File: `CORE_MINDEG_BOUNDARY_THEOREM.md`.

External inputs: Andrasfai--Erdos--Sos and the classical Erdos non-bipartite triangle-free edge bound.

### 5. Full 4r+1 residual branch

Status: **`PROVED_ANALYTIC`** for `r>=17`.

Any induced `F` on `4r+1` vertices satisfying

- `alpha(F)<=4`;
- `omega(F)<=r-1`;
- hereditary cap

automatically has

> `delta(F)=r+1`.

Hence it has a degree-`(r+1)` pivot `p`, and

`H=F-N[p]`

satisfies the complete residual-core contract

`|H|=3r-1`,
`alpha(H)<=3`,
`omega(H)<=r-1`,
`delta(H)>=r`.

File: `RESIDUAL_BRANCH_CLOSURE.md`.

### 6. Canonical greedy block extraction

Status: `PROVED_SYMBOLIC` plus `PROVED_ANALYTIC` for the low end when `r>=17`.

After anchor normalization, states have

`|R_a|=ar+1`,
`alpha(R_a)<=a`,
`e(R_a)<=B_a=r((a+1)r-a+1)/2`.

If `R_a` contains a target-colour `K_r`, deleting it yields the next canonical state `R_{a-1}`.

For `r>=17`, a canonical process cannot pass below `a=4`; reaching `R_4` forces it to be `K_r`-free and therefore gives the residual branch.

### 7. Recurrence-replacement scalar potentials

Status: `PROVED_SYMBOLIC` / `PROVED_ANALYTIC`.

File: `RECURRENCE_REPLACEMENT_POTENTIALS.md`.

#### Exact all-colour excess ledger

For a canonical state on `ar+1` vertices, if `x_0` is the target-colour excess above `p_a` and `x_i` are the other colours' excesses above `p_r`, then

> `x_0 + sum_{i=1}^{r-1} x_i = S_a(r)`

with

> `S_a(r)=[a(a-1)r+2a-2r]/2`.

Moreover

`S_a-S_{a-1}=(a-1)r+1`.

This is a genuine all-r scalar potential replacing much of the recurrence bookkeeping.

#### Alpha saturation

Every canonical state has

> `alpha(R_a)=a`,

not merely `<=a`.

#### Critical-core potential

Every canonical stop contains an induced `(r+1)`-critical graph `Q`. At a `K_r`-free stop,

> `|Q|>=3r-1` for `r>=4`.

Writing `|Q|=lr+t`, `0<=t<r`, compatibility with the hereditary cap and the Kostochka--Yancey critical-graph bound is exactly the single scalar inequality

`P_{l,t}(r)<=0`

recorded in `RECURRENCE_REPLACEMENT_POTENTIALS.md`.

Thus candidate critical-core orders lie in bounded-width residue windows rather than a 1752-node arithmetic tree.

### 8. Exact 5r+1 terminal

Status: `PROVED_SYMBOLIC` as a terminal definition/reduction.

If the first `K_r`-free canonical stop is `a=5`, then `T_r` has

- `5r+1` vertices;
- **`alpha(T_r)=5`**;
- `omega(T_r)<=r-1`;
- hereditary cap;
- `e(T_r)<=3r^2-2r`;
- no `K_r`.

If irreducible to Branch A, the independent-5 hypergraph has transversal number at least `r+1`, `delta(T_r)>=r`, and every degree-r row satisfies an explicit independent-4 witness condition.

File: `FIVE_R_TERMINAL.md`.

## CONDITIONAL

### Complete desired front-end dichotomy

Status: `PROVED_CONDITIONAL` on one remaining structural lemma.

For `r>=17`, if the first `K_r`-free canonical greedy stop cannot occur at `a>=6`, then every hypothetical counterexample yields exactly:

- Branch A: a `4r+1` residual with the fully proved `3r-1` core contract; or
- Branch B: the exact irreducible `5r+1` terminal.

No backend d2/d3/support theorem is used.

## OPEN

### Single highest-leverage blocker

> **NO-HIGH-STOP LEMMA.** For all sufficiently large `r`, a first `K_r`-free canonical state cannot occur at `a>=6`.

This is now the only obstacle to the requested `4r+1 residual OR 5r+1 terminal` extraction theorem.

The blocker is no longer an unstructured recurrence problem. Any counterexample must simultaneously satisfy:

1. exact alpha saturation `alpha=a`;
2. the exact all-colour excess ledger `S_a(r)`;
3. a `K_r`-free target colour;
4. a large `(r+1)`-critical core whose order passes `P_{l,t}(r)<=0`;
5. the full hereditary cap on every induced subgraph.

Secondary open questions:

- lower the current `r>=17` threshold in the Level-A core theorem;
- decide whether the irreducible `5r+1` terminal exists;
- turn the near-minimal non-target colours forced by `S_a(r)` into a resolvable-design classification.

## DISPROVED

No mathematical theorem has been marked `DISPROVED` in this workstream.

Rejected proof shortcuts:

- substituting `r` into the r=12 47/48-vertex edge seeds;
- claiming r=12 recurrence certification proves all-r extraction;
- assuming `delta(H)>=r` without the analytic theorem;
- treating numerical matching at r=12 as symbolic provenance.

## NEXT HIGHEST-LEVERAGE TARGET

Prove the **NO-HIGH-STOP LEMMA** by combining the all-colour slack potential with near-Turan stability of one or more non-target colours.

Preferred formulation:

> show that a first `K_r`-free canonical stop with `a>=6` forces enough of the other `r-1` colours to be O(a^2)-close to their balanced `r`-block minimum that the induced block systems either (i) yield a `5r+1` alpha-5 subset, or (ii) satisfy an exact resolvable-design contract that can be independently excluded.

Do not return to a parameterized replay of the r=12 recurrence.