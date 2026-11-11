# Paper theorem mapping — exact frozen domains

Frozen paper commit c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2. Verified Lean checkpoint ee2dbe9d6d0c5298dc6cfc8a4f8c91e5d8bcdf06. Paper prose status PROVED is not Lean certification. Standard three-axiom list is abbreviated S = propext, Classical.choice, Quot.sound; see AXIOM_AUDIT.md for each declaration.

| Paper theorem | Lean declaration | Exact statement / domain | Dependencies | Kernel status | Axioms | Counterexample audit |
|---|---|---|---|---|---|---|
| K145 statement | EG617R12Statement; originalProblem_iff_missingColor | No 12-coloring of K145 has all 12 colors in every 13-set; equivalent missing-color formulation | Basic definitions | Equivalence PASS; truth unproved | S | Definition preserved; no weaker graph substituted |
| CAP | tau12_le_colorEdgeCount; hereditary_color_cap; sum_colorEdgeCount | Every induced set in every color graph under ValidColoring satisfies D; all color edge counts sum to choose(n,2) | Independent bound, Turan, unique color edge partition | PASS | S | 146 arithmetic cases checked independently; not imported into Lean |
| Least color | exists_least_color_with_hereditary_cap | Some minimizing color has at most 870 edges and all induced D caps | Complete edge ledger 10440, 12 colors | PASS | S | Minimum existence and integer bound proved |
| R(a,n) contract | CoreAdmissible; core_admissible_induce | alpha <= a, omega <= 11 and EVERY finite induced subset satisfies D | Exact graph definitions; induced-image edge isomorphism | Definition and inheritance PASS | S | Cap omission refuted by K11 + K11 + C5[K5] |
| Frozen low M1 | core_R224_empty | Every graph on Fin24 fails CoreAdmissible 2 | Complement count, core_triangleFree24_edges_lt_132, kernel-proved AES | PASS | S | D24=144 and complement total276 audited; no classification assumption |
| Frozen low M1 helper | core_triangleFree24_edges_lt_132 | Triangle-free 24-vertex graph with alpha <= 11 has fewer than132 edges | Neighbor independence, handshake, degree bound, AES, 2-color independent classes | PASS | S | Strict AES threshold floor(48/5)=9 < 11; no E286 premise |
| LOWER remaining | none | R223 >=131; delta R335 >=12; delta R336 >=13 | Frozen low M2-M5 | FORMALIZATION GAP | not audited | 121/122 classification and 12-set lemma still pending |
| R337 / frozen low M5 | core_R337_empty; core_R337_empty_of_card | No37-vertex graph satisfies R(3,37) | R224, nonneighbors, handshaking481<=2e, D37=237 | PASS | S | Full exact contract; no R335 sharp bound assumed |
| GATE47 low-degree case | core_R447_degree_ge_10 | Every R447 graph has all degrees>=10; NOT the target12 | R337 and nonneighbor inheritance | PASS, proper subcase only | S | d10 and d11 remain open in Lean |
| R335 weak first step | core_R335_degree_ge_11 | Every R335 graph has all degrees>=11 | Generic R224 and nonneighbors | PASS, proper subcase only | S | Sharp12 still unproved |
| CORE211 | none | Every R335 has at least211 edges | LOWER and AES | FORMALIZATION GAP | not audited | Not promoted from R224 |
| GATE47 | Gate47Statement (definition only) | R447 and e<=286 imply every degree>=12 | Frozen low M1-M6 | FORMALIZATION GAP | Definition S; no proof | Hereditary caps indispensable; no exact-theorem counterexample found |
| LOW285 | none | No47 graph with e<=285, delta>=12, alpha<=4, omega<=11 | Frozen direct proof | FORMALIZATION GAP | not audited | No completed support classification audit |
| EX286 | none | Same graph contract and e=286 impossible | Frozen equality classification | FORMALIZATION GAP | not audited | Ten-orbit completeness and shared-center accounting unformalized |
| FLOOR47 | none | Every R447 has e>=287 | GATE47 then LOW285 and EX286 | FORMALIZATION GAP | not audited | E286 not applied to 287-edge graphs |
| Q32 / Q33 | none | Abstract e285 / e284 exclusions | LOW285 implies them | FORMALIZATION GAP | not audited | Not needed separately in frozen ledger |
| CTX49 | none | No induced R449 in a balanced original coloring | Contextual frontend second Turan | FORMALIZATION GAP | not audited | No promotion to generic uncolored statement |
| D48 | none | Every R448 has delta>=12 | h12 Section1 | FORMALIZATION GAP | not audited | Pending |
| Q20 | none | 12-shell q>=20 and exactly five equality families | h12 Section2 | FORMALIZATION GAP | not audited | Exhaustiveness unproved in Lean |
| FLOOR48 | none | Every R448 has e>=310 | D48, CORE211, Q20, inserted center | FORMALIZATION GAP | not audited | Pending |
| C29 | none | 61 vertices, delta13, alpha5, omega11, caps imply maximum regular q>=29 | Frozen COVER | FORMALIZATION GAP | not audited | Energy independence unformalized |
| C407 / C408 | none | Same contract and E407/E408 imply Q>=30/31 | Frozen COVER | FORMALIZATION GAP | not audited | Pending |
| H12 | none | 61 vertices, delta12, alpha5, omega11, caps, E<=408 impossible | h12 Sections3-5 | FORMALIZATION GAP | not audited | Pending |
| H13LOW | none | 61 vertices, delta13, same contract, E<=406 impossible | C29, FLOOR47 | FORMALIZATION GAP | not audited | Pending |
| H13TOP | none | Same61 contract at E407/E408 impossible | Final h13 certificates | FORMALIZATION GAP | not audited | No verified Lean certificate checker |
| STOP | none | Original coloring has residual61 graph with397<=E<=408 | Frontend and all144 stops | FORMALIZATION GAP | not audited | Search completeness unproved in Lean |
| REPLAY | none | Three recurrences agree at1752 nodes | External frozen verifier | NOT LEAN FORMALIZED | external result not trusted as theorem | Computational report only |
| K145 conclusion | MainTheorem ABSENT | EG617R12Statement | Full frontend and all core results | FORMALIZATION GAP | no theorem | No full-proof claim |
| GEN49 | none | Abstract uncolored high-energy R449 obstruction | Outside final frozen path | OPEN / unformalized | not audited | Contextual-to-generic transfer forbidden |

Finite-set alpha/omega bounds quantify all subsets; on finite vertex types this is the ordinary maximum independent/clique size condition. SimpleGraph excludes loops; edgeFinset counts unordered pairs once. CoreAdmissible includes all induced caps, not just total edges. The R224 and R337 exclusions are proved for arbitrary finite vertex types with exact cardinalities24 and37, and also specialized to Fin24 and Fin37. Full source types, paper attribution and axioms for EVERY declaration are in DECLARATION_STATEMENTS.md; full machine-printed types are in logs/statement-inspection.txt. There are no uncompiled candidates in this release.


Dependency order remains R224 -> hereditary nonneighbors -> R337 -> GATE low-degree case. The missing 23-point classification and 12-set lemma feed the sharp R335/R336 bounds, then the d10/d11 shell transport. GATE47 must precede LOW285/E286 promotion to FLOOR47. AES and Turan are kernel-proved Mathlib dependencies, not oracle calls.
