# Sharp R335 / R336 — LEAN VERIFIED

Frozen low minimum-degree gate M4/M5, commit
c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2. Exact statements are in
DECLARATION_STATEMENTS.md; complete build/type/axiom/hash evidence is in CI_STATUS.json.

Every sharp theorem assumes an arbitrary finite vertex type of the stated order
and the full CoreAdmissible 3 contract: alpha<=3, omega<=11, and D caps on EVERY
finite induced set. No terminal degree, Cost-6, or neighborhood condition is
assumed in the sharp bounds.

M4: core_R335_degree_eleven_nonneighbor_cost_six derives the exact Cost-6
input in the complement of the actual23-point nonneighborhood. The clique bound
provides distinct nonadjacent shell vertices x,y, outside that nonneighborhood.
Their common nonneighbors there form a clique in G, hence an independent set
in its complement, by alpha<=3. Certified Cost-6 supplies a twelve-point witness T.
Exact image, complement and cross-edge ledgers give
e(G[T union {x,y}]) >= 78-(e(complement[T])+|T intersect I|)>=72,
contradicting the retained cap D(14)=69. The distinctness/disjointness conditions
are proved, so the counted set really has14 vertices.

core_R335_degree_ne_eleven closes that case.
core_R335_degree_ge_twelve combines it with the existing weak bound.
core_R335_edges_ge_210 applies the degree sum identity.

M5: core_R336_degree_ge_thirteen deletes an actual neighbor, inherits all
CoreAdmissible conditions on the remaining35 vertices, and uses the exact
degree decrement with the R335 theorem. core_R336_edges_ge_234 follows by
the degree sum identity. Existing core_R337_empty_of_card is retained unchanged.

The fourteen-point helper has an explicit low-cost premise; its parent derives
that premise from r23_cost_six rather than introducing a new assumption.
The source mapping and actual dependency chain are retained in THEOREM_MAPPING.md.
