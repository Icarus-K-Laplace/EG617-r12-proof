# Independent E286 diagnostic attack

The diagnostic script is independent of Lean proof construction. Its output is
never read by a Lean theorem or trusted as an oracle. Kernel evidence is separate.

- All4290 support multisets of lengths3..5 over the eleven subsets of four seeds
  of sizes2..4 were checked. Exact surplus5 and each seed incidence>=2 leave97
  labeled multisets. All24 permutations produce exactly the ten frozen orbits.
- All611 scalar cases in the actual finite missing-set ranges were checked,
  including the claimed unique minima. All121 shared-leaf cases were checked.
- All nine possible exceptional-support sizes0..8 satisfy the regular-seed
  contradiction bound. The minimum lower bound is310>286.
- A realized47-vertex286-edge degree sequence21,11,12,...,12 has truncated
  excess9. This is a negative control showing that minimum degree12 is essential;
  it is not a counterexample to E286, whose minimum-degree hypothesis it violates.

No counterexample occurred in those explicitly bounded domains. No exhaustive
47-vertex graph search was performed. Shared-center graph charging, simultaneous
overlap and the remaining six terminal configurations still require kernel
proofs. The canonical-count to oriented-graph bridge, both h3 exclusions and the
first h4 exclusion are kernel-certified at ac68670b87e4c2114c27bd1ccd81c18ce7722a6a; no diagnostic result licenses
E286 or any parent theorem.

The actual pair-blocker argument constructs four independent vertices anticomplete
to the pair-support point if a forced cross edge is absent. Together they violate
alpha<=4. The K11/K11 charge uses three disjoint sets: that point and the two
missing subsets. Combining different blockers requires a separate disjointness
or shared-leaf accounting proof; the full excess of an overlapping vertex cannot
be charged twice.

The extended independent diagnostic checks all positive missing-size triples in
1..10 with total at least19, including ties: after choosing a smallest side, the
other sides each have size at least5 and total at least13. All deletions of at
most four neighbors are checked to leave both sides nonempty with total at least9.
The concentrated charge is checked on all positive sizes<=11 with correct
small-side orientation and scalar budget<=8.
There are352 qualifying size triples,450 residual capacity cases and13 oriented
small-budget scalar cases. These are tests only, not premises of the Lean proof.

A negative control shows that the orientation cannot be omitted: a=4,b=1 has
total scalar cost7 but first-side concentrated cost5. The formal parent covers
both orientations by an actual seed permutation. This negative control does not
satisfy the oriented lemma's hypotheses and is not a counterexample to E286.

The new mixed-blocker diagnostic checks all110 positive pairs a<=10,b<=11.
The minimum is4, uniquely at(2,3). With a=0,b=9 the scalar value is0: positivity
cannot be dropped. The formal dichotomy handles this by K10 completion.
No assumption that compatible labels force edges is used; actual blocker edges
are derived from alpha4. Multiplicity2 is converted to distinct vertices in the
kernel, and the first h4 proof separately proves disjointness of every cost sum.
No actual E286 counterexample was found; no exhaustive graph search is claimed.

The second h4 review is recorded in H4_SECOND_DISJOINTNESS_REVIEW.md.
