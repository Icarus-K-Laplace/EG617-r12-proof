# E408 Q32 — outside-component bijection in the aligned m=10, z=0,1 cell

Date: 2026-10-29  
Status: **PROVED conditional structural theorem; not a Q32 closure.**

## 1. Contract

Use the aligned (2,2,2,1) residual-fiber cell from V47_Z01_TRACK_ALIGNMENT.md, with target-color cliques T1,T2,T3 isomorphic to K12, T0 isomorphic to K11, and O={p} union A, |A|=13. Let D be the 132-edge nonexact color. Assume the saturation theorem V47_Z01_NONEXACT_GAP_SATURATION.md: D[A] is either 2K2 or K3, and its component Z has no D-edge to T0; every vertex of O\Z has exactly one D-edge to T0. Also, every o in O has exactly one D-edge into each Ti, i=1,2,3, and alpha(D)<=12.

## 2. Hitting maximum independent sets of O

Since p has no D-edge to A, the maximum independent sets of D[O] have size 12 and are exactly
\[
\{p\}\cup I,
\]
where I is a maximum independent set of D[A].

For every h in H, its D-neighborhood in O must intersect every such set. Otherwise {p} union I union {h} would be a D-independent 13-set, contrary to alpha(D)<=12.

### Case I: D[A]=2K2 union 9K1

Write the two edge components as E1,E2, and let Z be the edge component with no T0-neighbors. The maximum independent sets of A contain all nine isolated vertices and one endpoint from each Ei.

For a vertex h not adjacent to p, the condition of hitting every maximum independent set of A is therefore equivalent to:
- h has a D-neighbor among the nine isolated vertices; or
- h is adjacent in D to both endpoints of one of E1,E2.

Fix a large track Ti. Exactly one of its vertices is adjacent to p. The other 11 vertices must be hit by A-neighbors. The nine isolated vertices of A each have exactly one D-edge into Ti, so they can hit at most nine distinct track vertices. Hence at least two of the 11 non-p-neighbors have no isolated-A neighbor. Each must receive both endpoints of an edge component. There are exactly two such components, and every A-vertex has exactly one D-edge into Ti; therefore each edge component maps to its own track vertex, and the nine isolates map bijectively to the remaining nine non-p-neighbors. The unique p-neighbor is the twelfth vertex and has no A-neighbor.

The same argument applies to T0. There are ten vertices of T0 not adjacent to p, and the nine isolates can cover at most nine of them. The no-isolate vertex must receive both endpoints of the non-Z edge component, since Z has no T0-edges. The nine isolates map bijectively to the other nine non-p-neighbors, and p maps to the remaining T0-vertex. Thus T0 receives a bijection from the 11 components of D[O] other than Z.

Consequently the D-neighborhood-degree multisets from O are
\[
\begin{array}{c|c}
\text{track}&\{d_D(v,O):v\in T_i\}\\\hline
T_1,T_2,T_3& 1^{10},2^2\\
T_0&1^{10},2^1.
\end{array}
\]

### Case II: D[A]=K3 union 10K1

Let Z be the triangle. Every maximum independent set of A contains all ten isolated vertices and one triangle vertex. A vertex h not adjacent to p must therefore have a neighbor among the ten isolates or be adjacent to all three triangle vertices.

For each large track, there are 11 vertices not adjacent to p, but only ten isolated vertices. At least one track vertex has no isolated-A neighbor and must receive all three triangle vertices. The ten isolates then map bijectively to the other ten non-p-neighbors, and the unique p-neighbor has no A-neighbor. The resulting large-track multiset is 1^11,3^1.

For T0, the triangle Z has no T0-edges. The ten isolated vertices each have exactly one T0-edge, and the unique p-edge accounts for the eleventh edge. Since every T0-vertex must meet every maximum independent set of O, the ten isolates map bijectively to the ten non-p-neighbors and p maps to the remaining vertex. The T0 multiset is 1^11.

Thus
\[
\begin{array}{c|c}
\text{track}&\{d_D(v,O):v\in T_i\}\\\hline
T_1,T_2,T_3&1^{11},3^1\\
T_0&1^{11}.
\end{array}
\]

## 3. Component bijection and twin neighborhoods

In either case, every connected component of D[O] has all its vertices adjacent to the same unique vertex in each large track. Distinct components map to distinct vertices, and the map is a bijection from the 12 components of D[O] to each Ti, i=1,2,3.

For T0, the component Z is omitted and the remaining 11 components map bijectively to T0. In particular, for every edge ab in D[A],
\[
\boxed{N_D(a)\cap H=N_D(b)\cap H.}
\]
In the triangle case this holds pairwise for all three triangle vertices. The statement follows because each nontrivial component is assigned as a whole to one track vertex, and Z has no T0-neighbors.

This gives a strong necessary condition for the exact vertex-labelled CSP: in the 2K2 case, the O-degrees across (T1,T2,T3,T0) are (1^10,2^2) on each large track and (1^10,2) on T0; in the K3 case they are (1^11,3) on each large track and (1^11) on T0. The CSP and independent verifier encode/check these multiplicities and the twin-neighborhood condition.

## 4. Scope

This theorem is a structural reduction, not a contradiction. It does not eliminate either outside pattern, the aligned m=10,z=0,1 cell, or Q32 as a whole. The full-support Q32 terminal and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.


## 5. K6 contradiction corollary

The component-bijection theorem now has a decisive corollary, proved in V47_Z01_K6_CONTRADICTION.md. For any component C and two tracks to which it maps, the corresponding track vertices must be D-adjacent: otherwise one representative from each of the other 11 components of D[O], together with those two vertices, is an independent 13-set. Thus every non-Z component gives a D-K4 across T0,T1,T2,T3. In the 2K2 pattern, the non-Z edge component plus this K4 gives a D-K6; in the K3 pattern, the Z triangle plus its three large-track neighbors gives a D-K6. Since omega(D)<=5, both patterns are impossible. The aligned m=10,z=0,1,(2,2,2,1) cell is therefore CLOSED under the registered contract.
