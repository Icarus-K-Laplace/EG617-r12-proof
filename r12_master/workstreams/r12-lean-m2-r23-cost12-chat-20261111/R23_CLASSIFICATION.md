# 23-point classification — partial, not complete

Paper mapping: frozen low M2, all four exterior/type cases.
The original hypotheses remain card V=23, CliqueFree 3, CoreIndependenceBound 11,
and e>=121. No caps or terminal classification are silently added.

R23Reduction candidates derive a shortest C5, an exterior with exactly 18 vertices,
at least 80 induced edges, and a two-coloring of that exterior.
BipartiteExterior then gives an exact cross-edge description of K9,9, K8,10,
or K9,9 with exactly one deleted edge; it states every present/missing cross edge,
not just the part sizes or edge total. Current full CI status is recorded in CI_STATUS.json.

Still unformalized: the C5 two-neighbor type quotient as applied to arbitrary
graphs; exhaustive Case I blow-up identification; Case II singleton extension;
Case III alpha contradiction; Case IV ten ordered endpoint types and reduction
to C5(9,9,2,1,2). The full classification must not be marked LEAN VERIFIED.

Compatibility is a condition permitting an edge. It does not imply that the edge
already exists. For example C5(10,5,1,1,6) minus a class-0/class-1 edge still has
23 vertices, 121 edges, alpha=11 and compatible missing endpoints. Complete-cross
or unique-missing-edge information must supply the converse in each case.

Finite diagnostic enumeration is not a proof of the arbitrary-graph reduction.
Full source statements are in DECLARATION_STATEMENTS.md.
