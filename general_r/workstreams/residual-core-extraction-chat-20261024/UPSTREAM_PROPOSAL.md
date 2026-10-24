# Upstream proposal — general residual-core minimum degree

Status: **`PROVED_ANALYTIC`**, proposed for review/merge upstream. This file does not modify canonical general-r state.

## Proposed theorem

### General Residual-Core Minimum-Degree Theorem

Let `r>=17`. Let `H` be a graph on `3r-1` vertices satisfying

1. `alpha(H)<=3`;
2. `omega(H)<=r-1`;
3. every induced subgraph `X` satisfies the least-colour hereditary cap

   `e_H(X)<=D_r(|X|)=C(|X|,2)-(r-1)p_r(|X|)`.

Then

> **`delta(H)>=r`.**

This is the load-bearing minimum-degree clause previously missing from the general-r residual-core contract.

Full proof: `CORE_MINDEG_BOUNDARY_THEOREM.md`.

## Stronger residual consequence

For the same range `r>=17`, if `F` is a graph on `4r+1` vertices satisfying

- `alpha(F)<=4`;
- `omega(F)<=r-1`;
- the same hereditary cap,

then

> `delta(F)=r+1`.

Hence a degree-`(r+1)` pivot exists automatically, and for

`H=F-N[p]`

the complete contract follows:

`|H|=3r-1`,
`alpha(H)<=3`,
`omega(H)<=r-1`,
`delta(H)>=r`.

Full proof: `RESIDUAL_BRANCH_CLOSURE.md`.

## Proof architecture

The proof is seed-free and does not replay r=12 recurrence arithmetic.

1. The hereditary cap excludes a `2r` graph with `alpha<=2`, `omega<=r-1` by a triangle-free complement argument plus Andrasfai--Erdos--Sos.
2. Therefore any candidate `3r-1` core has minimum degree at least `r-1`.
3. If a degree-`r-1` vertex exists, its `2r-1` nonneighbors have a triangle-free non-bipartite complement whose edge count is forced to `(r-1)^2` or `(r-1)^2+1`.
4. A shortest-odd-cycle argument forces `C5`; all remaining vertices form a near-complete bipartite graph with total defect at most one.
5. Applying the full hereditary cap to `C5 + one side + one boundary-row vertex` gives a uniform row-defect bound `<=8`.
6. Every complement edge among the `r-1` neighbors of the boundary vertex demands two row defects summing to at least `r`.
7. Such an edge must exist from `omega(H)<=r-1`, giving `r<=16`, contradiction when `r>=17`.

## External inputs

- Andrasfai--Erdos--Sos triangle-free and K4-free minimum-degree theorems.
- Classical Erdos extremal bound for non-bipartite triangle-free graphs:
  `e<=floor((n-1)^2/4)+1`.

No exact Ramsey-number seed is used.

## Why this is upstream-worthy

The previous general-r architecture treated `delta(H)>=r` as the central load-bearing gap and all backend symbolic machinery was conditional on it. This theorem closes that clause for all sufficiently large r (`r>=17`) under exactly the hereditary conditions already inherited from a full balanced-colouring counterexample.

It also proves that once a `4r+1` residual is extracted, no separate pivot-existence or residual-minimum-degree argument is required.

## Remaining upstream caveat

This does **not** yet prove extraction of the `4r+1` residual from the full `K_{r^2+1}` counterexample. The only remaining workstream blocker is the `NO-HIGH-STOP` lemma described in `CANONICAL_STATE.md` / `OPEN_GAPS.md`.