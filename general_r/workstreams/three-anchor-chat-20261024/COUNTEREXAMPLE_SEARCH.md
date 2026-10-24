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

## Computation status and limitations

No theorem claim in this workstream is marked `COMPUTATION_CERTIFIED`. The committed ARITHMETIC_AUDIT.py script was executed and its local inequality/equality checks passed; the exact output is preserved in ARITHMETIC_AUDIT_RESULTS.md. CONNECTOR_SKELETON_AUDIT.py was also executed: it enumerates all labelled connector adjacency graphs, connector-excess allocations with total at most six, and allowed focus-owner assignments for r=12,13,14,15 under local rectangle relaxations. Its output is preserved in CONNECTOR_SKELETON_AUDIT_RESULTS.md. These checks cover local arithmetic and connector skeletons only.

**No full graph-level SAT/ILP counterexample search was run.** No Z3, OR-Tools, or PySAT backend was installed in the execution environment. Thus this file must not be read as a report of exhaustive graph enumeration. No source/verifier/checksum obligation for a graph search is claimed. The theorem is certified by the analytic proof in PUBLICATION_VERSION.md, not by computation.

## Final falsification status

The analytic proof and the local arithmetic cross-checks found no surviving equality configuration. The Exact Three-Anchor Excess Theorem is marked INDEPENDENTLY_VERIFIED by the analytic audit; full graph-level counterexample search remains unperformed, and external human referee review remains advisable.


---

# Round 2 — \(K=8\) falsification status

## Analytic boundary result

The new analytic audit proves \(K=8\Rightarrow r\le13\), hence \(K\ge10\) for all \(r\ge14\). The remaining \(K=8\) strata are enumerated in EQUALITY_K8_CLASSIFICATION.md. The \(r=12,13\) equality layer remains OPEN.

## Reproducible local profile search

K8_LOCAL_PROFILE_AUDIT.py enumerates the exact connector-degree equations and \(R_{22}\) charges in the delicate mixed-focus/overlap branches. Its assertions verify:
- the complete 23-row \(c=3,r=14\) local profile list;
- the sole \(c=3,r=15\) local profile and the empty \(r=16\) local profile set;
- the one-sided local profiles at \(r=13\) under the global \(k\le1\) overlap restriction;
- the two \((10,1)/(1,10)\) \(r=14\) equality orientations in both \(c=4\) overlap branches.

Exact output and limitations are recorded in K8_LOCAL_PROFILE_AUDIT_RESULTS.md.

## Explicit search limitation

This remains an integer/rectangle relaxation, not a whole-graph generator. It does not enforce every independent-four or clique constraint simultaneously, and it does not establish graph realizability. No graph-level SAT/ILP search was run. No candidate has been promoted to an actual \(K=8\) graph, and no conclusion \(K\ge10\) is asserted for \(r=12,13\).
