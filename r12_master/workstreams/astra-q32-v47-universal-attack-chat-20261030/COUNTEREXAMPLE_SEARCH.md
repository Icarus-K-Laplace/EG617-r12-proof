# Counterexample-first audit

Status: COMPUTATION_CERTIFIED failed diagnostics. The bounded search found no valid core; that fact alone is not evidence of exhaustive infeasibility. The later analytic theorem U6 proves nonexistence independently of this search.

## Executed experiment

search_core.py performed one deterministic30,000-proposal degree-preserving search for each of D and P, using seeds61712 and61713. Each starting graph fixes the theorem's210 edges and realizes the remaining75 edges. This experiment fixes six distinct private vertices of degree13 and all other vertices of degree12; it does NOT search every possible distribution of the six excess units. The exceptional five-point graph starts as a cycle but is allowed to change under switches.

Only the75 variable edges can move. A switch preserves every vertex degree and every distinguished support. The energy is the number of independent5-sets plus100 times the number of K12s. An exact incremental update was used during search; the independent verifier recomputes both counts directly from the final edge lists.

| Template | Accepted switches | Best independent5 count | Best K12 count | Result |
|---|---:|---:|---:|---|
|P / double|780|3256|0|fails alpha<=4|
|D / diamond|973|1901|2|fails both constraints|

The graphs are recorded in core_search_results.json for falsifiability. For P, an explicit forbidden independent set is[0,13,20,32,45]. For D it is[0,15,20,33,46]; an explicit K12 is[0,1,2,3,4,5,6,7,8,9,42,43]. Both have47 vertices,285 edges, minimum degree12 and total excess6. They are degree-feasible diagnostic graphs, not valid core counterexamples.

No unrun experiment, background process, external solver or UNSAT proof log is claimed.

## Independent verification

INDEPENDENT_VERIFIER.py does not import the search implementation. It reads full edge lists, checks degrees and fixed structure, counts independent5-sets by direct5-subset enumeration, and counts K12s using their least vertex and its neighborhoods. The counts agree with the search output.

The same verifier checks the elementary support-orbit classification and integer inequalities in the analytic proof, and reconstructs all four legal61-point Type-I source graphs. These checks support specific proof ingredients. The final full-family conclusion follows from the analytic reduction and the 8>6 / 10>6 contradictions, not from search failure.

## Adversarial interface retained for falsifiability

A zero-energy output would establish only a core witness. It would still require extension by O, target F of408 edges and minimum degree13, all eleven non-target graphs with the correct edge counts and independence conditions, source-correct factor/gadget assignments, and the genuine parent's additional embedding requirements. No partial assignment will be reported as a completed E408/Q32 configuration.

After the two searches, the mixed-pair and simultaneous diamond inequalities closed both templates analytically. A future zero-energy output would therefore challenge the proof or the checker and must be independently audited; it would not automatically establish a full colored counterexample.
