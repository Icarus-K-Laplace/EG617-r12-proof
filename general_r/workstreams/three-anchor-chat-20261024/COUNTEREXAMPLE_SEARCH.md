# Counterexample search

## Verdict

**No genuine counterexample exists for `r>=13` under the stated contract, by the analytic proof in `PROOF_ATTEMPTS.md`.**

The parent project already contains the independent `r=12` closure. Thus no actual counterexample is known for any `r>=12`.

## Falsification discipline
A candidate was required to satisfy simultaneously:

- `|H|=3r-1`;
- `alpha(H)<=3`;
- `omega(H)<=r-1`;
- `delta(H)>=r`;
- three pairwise nonadjacent degree-r anchors;
- `K_r<=7` (equivalently, by parity, `K_r<=6`).

No quotient skeleton or degree-feasible relaxation was ever promoted as a graph counterexample.

## Relaxed candidates that failed

Several low-budget quotient patterns appeared during exploration. They were useful because each exposed a missing structural inequality:

1. **c=2 concentration skeletons.** Aggregate degree sums permit a triple connector to concentrate its X-neighbours in one block, but exact-degree vertices then have cross-degree at most two. The independent-4 condition converts this into the tripartite transversal-cover lemma and kills the skeleton.
2. **c=3 mixed-focus r=13 boundary.** Aggregate rectangle accounting permits `K=6` with a `(2,2)` nonneighbour rectangle. Exactness then forces the triple connector to cover all eleven vertices of the opposite zero-deficit block, exceeding its degree budget.
3. **c=4 (0,0,2), r=14 overlap boundary.** Two same-group nonfocused connectors can share a formal `K=6` rectangle only when both use the same `(10,1)` support. The unique `X3` vertex is then saturated and cannot be adjacent to the required focused connectors.
4. **c=4 (0,1,1), r=13 boundary.** Two nonadjacent type-U connectors can formally spend exactly six connector excess units with `(3,3)` rectangles, but focused connectors already consume one external slot on every rectangle vertex, destroying exactness.

These were not counterexamples; they are precisely the equality layers eliminated in the final proof.

## Computation status

No theorem claim in this workstream is marked `COMPUTATION_CERTIFIED`. Small integer checks were used only privately to discover sharp equality patterns; every promoted claim has been replaced by an analytic inequality/equality argument in `PROOF_ATTEMPTS.md`.

Therefore there is no source/verifier/checksum obligation attached to the final theorem.

## Remaining falsification target

Only Level-4 proof cleanup remains: test whether the new focus/rectangle proof itself can absorb `r=12` without invoking the historical fixed-r closure. A failure there would not disprove the theorem; it would only show that a separate `r=12` lemma remains necessary.
