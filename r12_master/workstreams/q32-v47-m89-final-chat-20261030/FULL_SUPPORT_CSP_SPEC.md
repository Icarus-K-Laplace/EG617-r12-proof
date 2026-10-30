# Full-support CSP specification — m=8,9

## 1. Domain and variables

The solver is a complete labelled edge-coloring model on V={0,...,60}, with H={0,...,46}, pivot p=47, A={48,...,60}, and O={47,...,60}.

- `col[u,v] in {0,...,11}` for every unordered pair uv of V; color 0 is the target color.
- For every exact color C=1,...,m: a special point x_C, distinguished point y_C, twelve component labels `comp[C,v]` with one vertex omitted at x_C, and the special subset A0_C.
- Derived Booleans: membership in each of the twelve K5 factors, membership in G11, and pivot block membership `qblock[C,v]`.
- The pivot blocks Q_C are the four H-vertices in the C-neighborhood of p supplied by the Type-I source construction.
- `residual[v]` marks H\Q.

The implementation is in `q32_fullsupport_m89_solver.py`. It is copied into this isolated workstream and does not modify the sibling model.

## 2. Canonical color vector

For m=8:
`[408,129,129,129,129,129,129,129,129,130,130,130]`.

For m=9:
`[408,129,129,129,129,129,129,129,129,129,130,131]`.

Every edge receives exactly one color and the vector sums to 1830.

## 3. Exact Type-I source constraints

For each exact color:
- the twelve K5 factors partition V\{x_C};
- each factor is a K5 in that color;
- every factor meets O;
- if x_C is in O, the total outside occupancy is 13 and each factor has at most two outside vertices;
- if x_C is in H, the total outside occupancy is 14 and each factor has at most three outside vertices;
- the two special K5 factors and the special gadget edges are encoded exactly;
- the source graph's edges are equivalent to the corresponding color-edge variables;
- total color size is exactly129.

These sum-and-cap constraints imply the only legal outside profiles:
`(2,1^11)` when x_C is in O; and `(3,1^11)` or `(2,2,1^10)` when x_C is in H. The exceptional factor indices are unrestricted, including the special K5 factors.

## 4. Core, degree, and full-support constraints

- `e(H)=285`, `delta(H)>=12`, and `sum_H(d_H-12)=6`.
- `alpha(H)<=4`, enforced by exact independent-5-set separation.
- For every exact color C, `alpha(G_C)<=12`, enforced by independent-13-set separation.
- For every color, `omega(G_C)<=5`, enforced by K6 separation.
- The target color has exactly408 edges; exact colors have129; nonexact colors have the canonical 130/131 counts.
- For each nonexact 130-edge color, minimum degree is at least4; for the 131-edge color, at least3.
- Every core vertex belongs to at least one single-outside K5 factor of an exact color, so `U=H`.
- Each exact color has at least ten single-outside K4 witnesses. The verifier explicitly checks this.
- Cross-color witness families are pairwise linear; the verifier explicitly checks intersections and unique edge ownership.
- The unconditional residual gadget reserve caps are `(4,5,5)`; stronger `(3,4,4)` caps are conditional on the separately proved `d_F(z)>=13` case.

## 5. Pivot pair matching system (new)

For every pair C<D:
- count all target edges between Q_C and Q_D, with both endpoint orientations included;
- require at least four;
- exact alpha(H)<=4 separation is the authority that guarantees a perfect matching: the induced graph on Q_C union Q_D is bipartite with alpha<=4, so Kőnig gives a matching of size four;
- the independent candidate verifier explicitly recomputes and checks a perfect matching for every pair;
- if the pair has exactly four target edges, that matching is unique and equals the entire pair graph.

No redundant per-edge matching-choice Booleans are introduced. The matching is reconstructed from a model/candidate when needed.

## 6. Matching-composition and multi-projection cuts (new)

A lazy separator identifies every pair of light pivot pairs through a common anchor. It composes their unique perfect matchings and forces the resulting matching into the third pair. If multiple anchors force t distinct matchings, it also adds the finite lower bound `e_H(Q_C,Q_D)>=mu_4(t)`.

This is valid for all source placements and does not use an aligned target-track partition.

## 7. Per-block degree-ledger constraints (new)

For every Q_C, the solver explicitly asserts:
`X_C + Y_C = 5 + epsilon_C`,
where X_C is the excess target-edge count to other pivot blocks, Y_C is the excess target-edge count to R beyond one per residual vertex, and epsilon_C is the total degree excess on Q_C.

## 8. Deliberately not encoded

The aligned m=10 six-common-P factorization, its pair-projection normal form, and its residual-signature injectivity are not added. Those constraints depend on the aligned 3+7 track normal form and have not been proved for the m=8/9 full-support terminal. The global edge-color variables and source-edge equivalences already enforce actual edge ownership; a stronger track-specific encoding would be unsafe without a separate reduction theorem.
