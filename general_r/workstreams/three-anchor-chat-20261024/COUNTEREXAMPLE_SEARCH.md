# Counterexample search

## Verdict

**No genuine counterexample exists for any `r>=12` under the stated contract, by the analytic proof in this workstream.**

The former dependence on the parent project's independent `r=12` closure has been removed: `R12_UNIFIED_CLOSURE.md` closes all four anchor geometries directly in the same focus/rectangle language.

## Falsification discipline
A candidate was required to satisfy simultaneously:

- `|H|=3r-1`;
- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- `delta(H)>=r`;
- three pairwise nonadjacent degree-r anchors;
- `K_r<=7` (equivalently, by parity, `K_r<=6`).

No quotient skeleton or degree-feasible relaxation was promoted as a graph counterexample.

## Relaxed candidates that failed

Several low-budget quotient patterns appeared during exploration. Each exposed a missing structural inequality and was then eliminated analytically.

1. **c=2 concentration skeletons.** Aggregate degree sums permit a triple connector to concentrate its X-neighbours in one block, but exact-degree vertices then have cross-degree at most two. The independent-4 condition converts this into the tripartite transversal-cover lemma and kills the skeleton.
2. **c=3 mixed-focus r=13 boundary.** Aggregate rectangle accounting permits `K=6` with a `(2,2)` nonneighbour rectangle. Exactness forces the triple connector to cover all eleven vertices of the opposite zero-deficit block, exceeding its degree budget.
3. **c=4 (0,0,2), r=14 overlap boundary.** Two same-group nonfocused connectors can share a formal `K=6` rectangle only when both use the same `(10,1)` support. The unique short-block vertex is then saturated and cannot be adjacent to the required focused connectors.
4. **c=4 (0,1,1), r=13 boundary.** Two nonadjacent type-U connectors can formally spend exactly six connector excess units with `(3,3)` rectangles, but focused connectors already consume one external slot on every rectangle vertex, destroying exactness.
5. **r=12, c=3 mixed-focus layers.** Effective `R22` accounting allows several formal `K<=6` signatures. Every such signature contains a saturated rectangle vertex; independent-4 forcing then makes the triple or focused connector cover all/almost all of the opposite 10-clique, yielding a degree or clique contradiction.
6. **r=12, c=4, two-focus equality.** Both c=4 geometries admit formal `(1,8)` or `(8,1)` `R22` overlap skeletons with all six excess units on one exclusive vertex. The `(1,8)` orientation creates an independent 4-set; the `(8,1)` orientation creates either the same obstruction or an oversized common-nonneighbour clique demand.

These were not counterexamples; they are precisely the equality layers eliminated in the final proof.

## Computation status

No theorem claim in this workstream is marked `COMPUTATION_CERTIFIED`. Small integer checks were used privately only to discover sharp equality patterns. Every promoted statement is expressed as a finite analytic threshold/equality argument in `PROOF_ATTEMPTS.md` or `R12_UNIFIED_CLOSURE.md`.

Therefore there is no source/verifier/checksum obligation attached to the final theorem.

## Final falsification status

The conjectured threshold `K_r>=8` survived all direct symbolic and low-budget equality attacks and is now proved for the entire target range `r>=12`.
