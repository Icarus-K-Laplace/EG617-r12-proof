# Graph Symmetry Witness Schema

Schema: `eg617-graph-symmetry-witness-v1`.
Object schema: `eg617-colored-incidence-object-v1`.

## Object

A colored-incidence object contains a finite vertex universe, a finite color universe, a partition of vertices into role classes, a partition of colors into permutation classes, a simple undirected edge set with exactly one color per edge, and global, vertex-indexed, and color-indexed constraints.

The role partition prevents a distinguished pivot from being mapped to a shell/core vertex. Color classes prevent a distinguished color from being permuted with an ordinary color. Constraint records are mapped together with their indexed vertex/color, and every other field must be preserved exactly.

## Witness record

Each eliminated state binds its state ID and retained representative ID, the complete vertex bijection, the complete color bijection, the original canonical encoding, and the representative canonical encoding. Batch receipts also bind pre-quotient and post-quotient state-set digests.

The verifier checks that vertex and color maps are bijections, preserve role/color classes, map every colored edge exactly, preserve all declared constraints, and produce equal canonical encodings.

## Canonical encoding and limitations

The reference verifier computes canonical encodings by exhaustive permutations inside each vertex-role class and color-class class. It is intentionally limited to small objects (at most 8 vertices and a bounded group-action count). It is an executable specification for the witness format, not a scalable canonical-labeling backend.

A batch certificate can claim complete orbit coverage only if it binds a complete pre-quotient state catalog and deterministic state-generation specification. The verifier independently enumerates the bounded test fixture, checks that the catalog equals the full assignment space, checks one witness per state, verifies that every state maps to the correct representative, and checks that retained representatives are pairwise inequivalent.

The committed test fixture enumerates all (2^3=8) two-colorings of the three edges of (K_3), with one distinguished pivot and a two-vertex shell role. It has 3 orbits under shell-vertex swap and global color swap.

## Explicit limitations

- No graph-level EG617 symmetry reduction is currently certified.
- The toy test proves only that this bounded verifier implementation handles the fixture correctly.
- Large instances require a separately pinned canonical-labeling algorithm or a checkable full group/orbit trace.
- Solver symmetry-breaking clauses remain prohibited as proof evidence without independent witnesses.
