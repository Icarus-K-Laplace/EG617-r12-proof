# Elaborated dependency traversal

The initial audit at efda572 compiled, but only traversed the public import view:
it omitted imported theorem bodies. Its success marker is NOT complete dependency
evidence. Kernel builds and the independent transitive axiom audit are unaffected.
The corrected audit uses legacy import mode to load private bodies transitively
and fails unless seven required load-bearing proof nodes are actually reached.
It is VERIFIED at efff7bd, CI44675114460, visiting177 project constants.

EG617/Audit/E286Dependencies.lean traverses the actual elaborated types and proof
terms starting at the eight-remaining and nine-remaining support theorems and the
actual triple-K11 charge. At51358b4, CI44890957575, it visits245 project constants.
It records all
reachable project constants, including private constants, rather than scanning
source text for theorem names. Each constant is visited once, including recursive
definitions. The full emitted graph is retained in the successful CI log and
logs/e286-elaborated-dependencies.txt when that audit succeeds.

This graph is restricted to project constants. Transitive dependencies outside
the project are covered by the complete #print axioms audit, not by a claim that
the dependency graph contains every Mathlib declaration.

The load-bearing chain is:

1. Original E286 hypotheses -> excess8 -> actual regular independent four seeds.
2. Private-clique partition -> exact surplus5 -> complete finite count domain.
3. Kernel orbit certificate -> actual counts -> inverse reindexing of actual seeds.
4. Alpha4 -> actual blocker edges; omega11 -> nonempty missing subsets.
5. Clique neighbor counts -> six-unit local cost -> complementary-pair contradiction.
6. First canonical representative -> actual complementary pairs -> exclusion.
7. Complete ten-representative membership -> membership in the remaining nine.
8. Actual triple charge3 + concentrated pair charge6 -> second h3 orbit exclusion.
9. Nine-representative membership -> membership in the remaining eight.

The graph does not contain an E286 nonexistence,287-edge floor,COVER or MainTheorem
proof. No terminal exclusion is supplied as an undeclared premise.
