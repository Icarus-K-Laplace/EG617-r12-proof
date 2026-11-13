# Odd-cycle bound

Module EG617.Core.OddCycleBound compiled in Linux run 43359045754 at
d97f9e7f3af79d21b1b28a2f0923e5ef66709cbd. That entire run failed later in
R23Reduction; this is a module PASS, not yet a whole-project or full-axiom PASS.

Paper mapping: frozen low M2 opening paragraph, independently reproduced in
LOWER_ORDER_M1_M6_INDEPENDENT_AUDIT_20261103.md, M2.

The public graph theorem is EG617.shortestOddCycle_edge_bound, with explicit
triangle-freeness, a shortest odd simple cycle p, and length p = 2*k+1.
Its conclusion is the standard unordered edgeFinset count <= B(card V,k).
See DECLARATION_STATEMENTS.md for verbatim source statements of every declaration.

The proof establishes, rather than assumes:

1. A globally shortest odd closed walk exists in a non-two-colorable graph.
2. Such a walk is a simple cycle and is chordless.
3. Its support has exactly length p vertices and exactly length p induced edges.
4. Its induced graph is two-regular. Independent subsets have at most half its
   vertices; triangle-freeness makes every vertex's cycle-neighborhood independent.
5. The circle, cross-cut, and exterior edge counts sum exactly to e(G).
6. The induced exterior satisfies Mathlib's kernel-proved Mantel bound.

IsShortestOddCycle minimizes over all simple odd cycles at all starting vertices;
shortestOddCycle_iff_shortestOddLoop proves equivalence to the working walk notion.
No unformalized capacity document is used as a premise.

Numerical theorems prove B(23,2)=122, B(23,3)=119, all feasible k>=3 give <=119,
and all feasible k>=2 at n=18 give <=73, with equality at k=2.
Feasibility means 2*k+1<=n. Omitting that domain gives a false unrestricted maximum
for the natural-subtraction formula, so the graph domain is written explicitly.
