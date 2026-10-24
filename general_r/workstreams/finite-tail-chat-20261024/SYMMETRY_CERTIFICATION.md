# Symmetry Certification Protocol

## Current verified reduction: scalar missing-degree reflection

For the necessary inequality
`f_r(d)=d(r+1-d)`, we have
`f_r(d)=f_r(r+1-d)`.

The legal missing-degree domain is `d in {0,...,r}`. A paired reflection is used only when both d and r+1-d are in that domain. Every admissible d is represented exactly once by a listed reflection class.

Important boundary detail: d=0 maps to r+1, which is outside the legal domain. Therefore d=0 is retained as an unpaired singleton; it is not discarded on symmetry grounds. The certificate records this rule explicitly. A fixed point, when it lies in the candidate set, is recorded as a singleton fixed-point class.

The verifier checks that:
- every candidate degree belongs to exactly one class;
- every two-member class is exactly {d,r+1-d};
- every paired member satisfies the same exact quadratic bound;
- every singleton has the stated reason;
- the class representatives and certificate hash match the independent reconstruction.

This is a quotient of the scalar necessary-domain list only. It does not imply that graph states with the same d are isomorphic.

## Graph-level symmetry: not yet implemented

The following reductions remain reserved and must not be applied as hard symmetry breaking until a witness checker exists:

1. color permutation;
2. vertex permutation fixing the distinguished pivot;
3. canonical colored-incidence labeling;
4. support-degree and degree-sequence refinement;
5. stabilizer-based orbit branching.

## Required graph symmetry witness

Each removed graph-level branch must carry a witness record containing:

- a canonical encoding of the original colored-incidence object;
- a canonical encoding of the retained representative;
- the explicit vertex and color permutations, or a checkable canonical-labeling witness;
- a check that incidence, colors, pivot role, and all theorem constraints are preserved;
- the stabilizer subgroup or orbit-generation trace used at that node;
- the set of branches removed by the orbit step;
- a deterministic digest of the pre-quotient and post-quotient state sets.

The independent verifier must establish:
1. the original and representative objects are isomorphic under the supplied allowed action;
2. the action preserves the exact constraint language and all distinguished roles;
3. every removed branch is in the representative's orbit;
4. all orbit representatives are pairwise inequivalent;
5. the union of represented orbits equals the complete pre-quotient state set.

For a canonical-labeling implementation, pin the algorithm and version and include enough data for the verifier to recompute the canonical form. A solver's built-in symmetry-breaking clauses are not evidence unless their full group-theoretic soundness and completeness are independently checked.

## Current status

- Scalar reflection: **IMPLEMENTED AND CHECKED** for the endpoint-domain certificate.
- Graph witness schema and bounded exhaustive verifier: **IMPLEMENTED** in `GRAPH_SYMMETRY_WITNESS_SCHEMA.md` and `GRAPH_SYMMETRY_VERIFIER.py`.
- Toy K3/two-color fixture: 8 states, 3 orbit representatives, 8 explicit witnesses; state-set digests independently reconstructed in Python.
- Direct CLI replay of the committed graph verifier: **PENDING**; the current cross-check does not certify any EG617 graph-level reduction.
- No graph-level search branch may currently be removed on the basis of these interfaces until the committed verifier replay and a complete theorem-specific state catalog are available.
