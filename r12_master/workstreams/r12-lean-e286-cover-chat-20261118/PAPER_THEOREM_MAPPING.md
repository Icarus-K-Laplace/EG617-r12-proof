# Frozen-paper theorem mapping

Full theorem names and earlier reductions are detailed in THEOREM_MAPPING.md.
Exact source declarations are in DECLARATION_STATEMENTS.md; the successful CI log
contains elaborated statements with all implicit binders.

| Frozen E286 part | Lean result | Coverage |
|---|---|---|
| Introduction, degree excess8 | e286_excess_sum | Complete |
| Section1, no alpha2 set of25 | e286_no_induced_alpha_two_25 | Complete |
| Section1, common-neighbor bound | e286_common_neighbors_excess_bound | Complete |
| Section2, actual regular seeds | e286_exists_regular_independent_four | Complete |
| Section2, actual partition/surplus | e286_seed_support_reduction | Complete |
| Section2, complete ten count orbits | e286_support_counts_complete | Complete |
| Section2, graph realization | e286_actual_oriented_support_orbit | Complete |
| Section3, pair blocker | e286_pair_blocker_complete | Complete |
| Section3, f11 local charge | e286_k11_pair_local_charge | Complete |
| Section3, concentrated equation2 | e286_private_pair_concentrated_charge | Complete |
| Section3, mixed/shared-center charges | No complete theorem | Open |
| Section4, triple on three K11s | e286_private_triple_k11_charge | Complete |
| Section5, first h3 orbit | e286_first_support_orbit_impossible | Complete |
| Section5, second h3 orbit | e286_second_support_orbit_impossible | Complete |
| Sections2+5, exhaustive residual cases | e286_actual_support_eight_remaining | Complete |
| Section6, three h4 orbits | No exclusion theorem | Open |
| Section7, small-budget double pair | No theorem | Open |
| Sections8-12, five h5 orbits and E286 | No exclusion theorem | Open |
| Consequent287-edge floor | core47_edge_floor_287 absent | Open |
| COVER source, h12/h13/root K145 | COVER_verified/MainTheorem absent | Open |

Complete claims refer to51358b4, CI44890957575. All graph correspondences retain
actual vertex sets and adjacency; compatible types are never assumed adjacent.
The inherited GATE47 theorem keeps its full CoreAdmissible4 contract.
