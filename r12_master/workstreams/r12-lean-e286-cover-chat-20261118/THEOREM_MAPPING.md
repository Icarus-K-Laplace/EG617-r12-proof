# New theorem mapping

Frozen E286 exclusion corresponds to `EG617.E286_verified` (CI 45609105445).
The prior 287-edge floor used in frozen COVER Section 1 corresponds to
`EG617.core47_edge_floor_287` (CI 45610341669). Its low-edge extension proof
uses `core47_sparse_nonedge`, `core47_add_sparse_edge_clique` and
`core47_low_edges_impossible`.

Frozen E286 introduction / Section2 -> E286Hypotheses, E286Statement (definitions).
Degree sum572 -> e286_degree_sum.
Total excess8 -> e286_excess_sum; e286_support_sum.
Exceptional support<=8 -> e286_support_card_le_eight.
Degree upper bound20 -> e286_degree_le_twenty.
Regular complement / size>=39 -> e286_regular_complement; e286_regular_card_ge_39.
Exceptional degree total -> e286_support_degree_sum.
Regular induced-edge ledger -> e286_regular_edge_ledger.

The nine ledgers above are VERIFIED at2da427b, CI44194246540.
E286 Section2 regular four seeds -> e286_exists_regular_independent_four (VERIFIED).
E286 Section1 -> e286_induced_degree_budget; oddCycleBound_25;
alpha_two_25_edges_ge_155; e286_no_induced_alpha_two_25;
independenceBound_common_nonNeighbors; e286_common_antineighborhood_card_le_24.
These Section1 reductions are VERIFIED at80d1542, CI44195410389, with no D premise.
E286 Section1 equation1 -> e286_common_neighbors_excess_bound;
e286_common_neighbors_le_eleven; e286_ten_clique_completers_excess (VERIFIED).
E286 Section2 private cliques/surplus/partition -> e286_private_class_isClique;
e286_private_multiple_card; e286_seed_surplus_five; e286_seed_support_reduction
(VERIFIED at4ede035, CI44262022836). All are statements about actual graph sets.
Ten-orbit count classification -> e286_support_counts_complete (VERIFIED at505e87c,
CI44495273085). e286_weighted_profiles_complete proves finite-domain completeness;
e286_finite_support_orbit_check is kernel-reduced with decide, without external data.
Actual graph support orbit -> e286_actual_support_orbit (VERIFIED at86e9970).
Section3 pair blocker -> e286_pair_blocker_complete (VERIFIED at86e9970).
Section3 f11 actual local charge -> e286_k11_pair_local_charge (VERIFIED at86e9970).
Section5 complementary K11 pair obstruction ->
e286_complementary_k11_pairs_impossible (VERIFIED at86e9970, CI44498020540).
Section2 relabeling/Section5 first canonical orbit -> e286_actual_oriented_support_orbit;
e286_first_support_orbit_impossible; e286_actual_support_nine_remaining
(VERIFIED at90130d8, CI44498770093). The inverse seed permutation identity
e286_graph_support_counts_relabel proves equivalence with actual graph distributions.
No mapping claims E286 exclusion,287 floor,COVER or MainTheorem. Inherited source remains unchanged,
except the import root and generated audit entry points.

Frozen Section4's independent5 obstruction -> e286_independent_three_forces_edge;
ordered three-clique obstruction -> e286_ordered_three_cliques_obstruction
(VERIFIED at8b06204, CI44675832316).
Section4 local excess>=3 without ordering -> e286_three_k11_local_charge;
actual private seed-clique form -> e286_private_triple_k11_charge
(VERIFIED at2c0c87a, CI44676583725).
These preserve all actual adjacency and disjointness conditions; the wrapper
derives them from the seed definition rather than assuming a finite certificate.
Section3 equation2 -> e286_private_pair_concentrated_charge (VERIFIED at51358b4).
Section5 second h3 orbit -> e286_second_support_orbit_impossible;
both h3 orbits excluded -> e286_actual_support_eight_remaining
(VERIFIED at51358b4, CI44890957575). Both orientations are treated by actual seed
permutations. Positive count fibers yield actual witnesses; no terminal premise
is added to that theorem. This earlier milestone left eight representatives.

Frozen Section3 f10,11 -> e286_f10_11_minimum; actual mixed charge ->
e286_k10_k11_pair_local_charge; actual private-clique dichotomy ->
e286_private_mixed_pair_dichotomy (VERIFIED at415a947, CI45454651025).
Finite missing-size bounds come from actual clique inclusion; the zero K10
missing case is handled by completion, and the K11 missing set follows from omega11.

Frozen Section2 multiplicity2 -> e286_double_count_actual_witnesses.
Section6 first h4 configuration -> e286_doubled_mixed_opposite_pair_impossible;
exact first h4 count representative -> e286_third_support_orbit_impossible.
Sections2+5+6 -> e286_actual_support_seven_remaining.
All are VERIFIED at ac68670b87e4c2114c27bd1ccd81c18ce7722a6a, CI 45455564403.
The count fiber yields distinct actual vertices; clique cards follow from the
seed incidence ledger. Charges are combined only on proved disjoint actual sets.
The strongest theorem retains exactly the original E286 hypotheses and leaves
two h4 and five h5 cases. It does not prove E286 nonexistence.

## Second h4 orbit

Code db9f2848d77da0e484c9ba35ee965fe8cd683230, clean Linux CI 45555580430.

| Frozen result | Lean declaration |
|---|---|
| Section3, scalar formula (5) | e286_f10_11_extra_completer_minimum |
| Section3, actual extra completer next to K10 | e286_k10_k11_extra_completer_charge |
| Section3, three shared-leaf membership cases | e286_shared_leaf_pointwise |
| Section3, sum over the shared leaf | e286_shared_leaf_pair_charge |
| Section6, orbit {01,012,03,23} | e286_h4_second_orbit_impossible |
| Sections2,5,6, reduction to six actual representatives | e286_actual_support_six_remaining |

The two charges share only K3. The graph-level cost5 and the joint cost11
use the same split estimate (e286_extra_completer_split). The joint argument
counts K3 excess once. Exact missing sets come from adjacency filters and
the root theorem has no extra terminal hypothesis.
