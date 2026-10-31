# Low-edge, equality, and source-gate audit

Status: PROVED for the precise contracts below, by the inspected analytic proofs; finite checks are supplementary. Frozen sources and exact blob identities are listed in SOURCE_MANIFEST.json.

## Hypotheses and transfer

The abstract low-edge theorem excludes all simple H with |H|=47, delta>=12, alpha<=4, omega<=11, e<=285. The 286 theorem excludes the SAME graph class at e=286. Neither theorem needs D caps. Handshake first gives e>=282, so no smaller-edge exception is hidden.

For a parent-induced J in R(4,47), caps are inherited from the other eleven colors, as proved in K145_TO_T61_FRONTEND_AUDIT.md. The separate gate J in R(4,47), e(J)<=286 => delta>=12 is proved in frozen/low/MINIMUM_DEGREE_GATE_SELF_CONTAINED.md, not assumed from order or energy alone. Its decisive chain is R(2,24) empty; a complete 121/122-edge triangle-free classification on23 points; the12-set cost<=6 lemma; delta R(3,35)>=12; delta R(3,36)>=13; R(3,37) empty. Degree10 in J forces e>=289 and degree11 forces e>=287. Applying this gate BEFORE the abstract obstructions proves every R(4,47) has e>=287.

The root verifier rechecks the explicit23-point families (61 representatives,49 admissible,263 maximal independent sets), type cases, and cap arithmetic. It does not re-search 284/285/286 graphs.

## Low-edge route and distinct exact contracts

The direct uniform proof in frozen/low/DIRECT_UNIFORM_PROOF.md covers total excess T=2e-564<=6. It is sufficient by itself; safe augmentation to285 is an optional independent route. Augmentation preserves only the abstract five hypotheses, not full-color realization or every cap; the proof correctly does not require those extra properties of the augmented graph.

Q32: exact e=285, T=6. Original c5062fcdf5ac83ea9d0d51b9bc34a8f9f3619c0f is an ancestor of inspected head f56cc9eba646e71d63c4b55f468a2340bcdd64c2 (10 later commits). The exact theorem's eight steps and parent-gate issue are separately recorded in frozen/low/Q32_285_THEOREM_INDEPENDENT_AUDIT.md.

Q33: exact e=284, T=4. Original 2e8160200dcf21431221aa453fb49b952d6d52d0 is an ancestor of inspected head bdc2046ea08f12455a37fd412fe2e19514118ada (51 later commits). Its source classification is reconstructed in the present frozen lower-order proof; no unavailable127-row archive is needed. See frozen/low/Q33_284_THEOREM_DEPENDENCY_AUDIT.md.

These exact theorems remain independent checkpoints. Neither is borrowed as the other theorem, and neither is a required node on the final direct-uniform route.

## Exhaustive 286 support quotient

At T=8 the nonedge common-neighbor bound is c(u,v)<=3+epsilon(u)+epsilon(v)<=11. The old upper bound9 is not valid here. Two exterior completions of a K10 cost combined excess>=7; they are not simply declared unique.

The independent regular four-set is licensed by the degree/excess count in frozen/eq286/286_EDGE_EQUALITY_CLASSIFICATION.md Section2. Its private cliques and five surplus seed incidences imply h=3,4,5, with respectively2,3,5 support orbits. The new verifier reconstructs just this tiny quotient from all multisets of supports of size2..4 with total incidence h+5 and each seed incidence>=2.

|h|All orbits|Elimination in frozen equality proof|
|---|---|---|
|3|{0123,01,23}; {01,023,123}|two disjoint pair charges; concentrated pair charge plus disjoint triple cost|
|4|{01,01,023,23}; {01,012,03,23}; {01,02,03,123}|double completion cost; mixed blocker with extra completer; additive star accounting|
|5, sizes9/11/11/11|{01,01,02,03,23}|small-budget double-pair lemma then four K9 completers|
|5, sizes10/10/11/11|P={01,02,02,13,13}; D={01,02,03,12,13}; B={01,01,02,13,23}; C={01,01,01,23,23}|P equality saturation; D pointwise inequality; opposite K10 completions; double K11-pair lemma|

## Shared excess audit

Star: at a center K10 vertex, internal degree9 plus three supported-point incidences gives baseline12. A missed point replaces its own incidence by forced neighbors in its leaf's missing set; the increment is b-1. Different leaves lie in different cliques, so these forced neighbors are disjoint. Since a pair point cannot complete a K11, b>=1. Add the increments at each vertex before summing over center vertices. This justifies formula(3); it does not spend the center's entire excess three times.

D: at a K10 vertex the same baseline12 has three incidences, but at most one increment can be negative, from the opposite K10. For any chosen missing incidences with at most one a=0,
max(0,sum(a-1))>=sum max(0,a-2).
Every positive term on the right leaves a spare unit to absorb the possible -1. At K11 there are two incidences and the two-term version holds even if both opposite missing sets are empty. Opposite cliques are distinct; each point's own excess is charged once. The verifier checks all bounded scalar instances, while the argument proves the inequality generally.

The small-budget double-pair lemma retains both-complete and one-complete cases. The final double K11-pair proof separates opposite/same small sides and disjoint/contained/equal missing singletons; the common-neighbor bound at the equal-singleton case is the T8 bound, not T6. No exceptional support remains.

## Frozen commits

Low/gate: 783c72090205d4bd1a6eefce1dec09e15f78e319.
Equality: c3d07b2ca5912b1b0c1c6998303c19c3c2911340.
Both are separate descendants of global b0459807acd4b7e386148056ddf77d7998918893; neither sibling proof is assumed to be merged into the other.
