# E408 Q32 — K6 contradiction for the aligned m=10, z=0,1 cell

Date: 2026-10-29  
Status: **CLOSED under the registered E408/Q32 contract.** This closes only the aligned z=0,1, (2,2,2,1) cell, not all of full-support Q32.

## 1. Inputs

Use the established aligned cell:
- H is partitioned into target-color cliques T1,T2,T3 isomorphic to K12 and T0 isomorphic to K11;
- O={p} union A, |A|=13, with every pA edge target-colored;
- the nonexact color D has alpha(D)<=12 and omega(D)<=5;
- the exact nonexact-gap saturation theorem forces g_D=7 and g_C=3 for each of the ten exact colors;
- the only outside patterns are D[A]=2K2 or D[A]=K3, with a component Z having no D-edge to T0 and every vertex outside Z having exactly one D-edge to T0;
- every o in O has exactly one D-edge into each large track T1,T2,T3.

By V47_Z01_OUTSIDE_COMPONENT_BIJECTION.md, the components of D[O] map bijectively to each large track, and every component other than Z maps bijectively to T0. Each vertex in a component has D-neighbors in H exactly at the track vertices assigned to that component.

## 2. Same-component track vertices must be D-adjacent

Fix a component C of D[O] and two tracks T_i,T_j to which C maps, with corresponding vertices x_i(C), x_j(C). For a T0/large-track pair, only take C not equal to Z.

There are exactly 12 components of D[O]. Choose one representative from each of the 11 components other than C. These representatives form a D-independent 11-set: distinct connected components of D[O] have no D-edges between them. They are also nonadjacent in D to x_i(C) and x_j(C), because the latter have O-neighborhood exactly C.

If x_i(C)x_j(C) were not a D-edge, these 11 representatives together with x_i(C),x_j(C) would form a D-independent 13-set. This contradicts alpha(D)<=12. Hence
\[
\boxed{x_i(C)x_j(C)\in E(D)}
\]
for every pair of tracks to which C maps.

Therefore the three large-track vertices assigned to any component form a D-triangle. For every component C other than Z, its four assigned track vertices in T0,T1,T2,T3 form a D-colored K4.

## 3. Case D[A]=2K2

Let C={a,b} be the edge component other than Z. Both a and b have the same D-neighbor in each of T0,T1,T2,T3. By Section 2, these four track vertices form a D-colored K4. Both a and b are D-adjacent to all four vertices, and ab itself is a D-edge.

Thus the six vertices
\[
\{a,b,x_0(C),x_1(C),x_2(C),x_3(C)\}
\]
span a D-colored K6. This contradicts omega(D)<=5.

## 4. Case D[A]=K3

Let Z={a,b,c} be the triangle component with no T0-neighbors. The vertices a,b,c have the same D-neighbor in each large track. By Section 2, those three track vertices form a D-triangle. Each of a,b,c is D-adjacent to all three corresponding track vertices, and abc is itself a D-triangle.

Hence the six vertices
\[
\{a,b,c,x_1(Z),x_2(Z),x_3(Z)\}
\]
span a D-colored K6, again contradicting omega(D)<=5.

## 5. Conclusion and scope

Both equality patterns forced by the nonexact-gap saturation theorem are impossible. Therefore:

> **The aligned full-support Q32 cell with m=10, z in {0,1}, and residual-fiber profile (2,2,2,1) is CLOSED.**

This is an analytic contradiction; it does not depend on obtaining a solver UNSAT status. The remaining full-support frontier still includes m=8, m=9, and the other m=10 light-block/residual cells. The complete E408/Q32 terminal and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
