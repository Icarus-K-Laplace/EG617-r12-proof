# Backend interface — exact excess / focus / rectangle loads

## Status and scope

This is a reusable local accounting interface for the general-\(r\) backend. It does **not** assert repivot termination. It preserves the frozen theorem \(K\ge8\) and the Round-2 strengthening \(K\ge10\) for \(r\ge14\). The \(K=8\) equality layer remains open at \(r=12,13\).

## 1. Exact budget decomposition

Let \(C\) be the connector set and \(X_1,X_2,X_3\) the exclusive blocks. Every vertex is an anchor, a connector, or exclusive. The anchors have zero excess, so
\[
K=K_C+K_X,\qquad
K_C:=\sum_{z\in C}x_z,\quad
K_X:=\sum_{i=1}^3\sum_{v\in X_i}x_v.
\tag{1}
\]
All terms are nonnegative integers, and \(K\) is even.

For a connector \(z\), define \(\gamma_z=|N(z)\cap(C\setminus\{z\})|\). If \(z\) is a pair connector incident with anchors \(a_i,a_j\), missing \(a_k\), and \(a,b\) are its nonneighbour counts in \(X_i,X_j\), then
\[
a+b=r-2-d_i-d_j+\gamma_z+n_k-x_z,\qquad
n_k:=|N(z)\cap X_k|.
\tag{2}
\]
For a triple connector,
\[
\sum_i |N(z)\cap X_i|=r-3+x_z-\gamma_z.
\tag{3}
\]
These are exact equations, not inequalities. In particular, \(\gamma_z\), opposite-block neighbours \(n_k\), and connector excess \(x_z\) must not be silently discarded when an equality case is checked.

## 2. Per-vertex load accounting without double charging

For \(v\in X_i\), set \(b_i=2+d_i\). If the backend has established a set \(F_v\) of distinct external neighbours forced to be adjacent to \(v\), then
\[
x_v\ge (|F_v|-b_i)_+.
\tag{4}
\]
For a candidate skeleton, construct \(F_v\) as a **set union** of:
- connector neighbours whose incidence is part of the candidate;
- all opposite-side vertices forced by rectangle lemmas;
- focused connectors known to be complete to the block;
- any other independently forced external neighbours.

Then
\[
K\ge K_C+\sum_i\sum_{v\in X_i}(|F_v|-b_i)_+.
\tag{5}
\]
Equation (5) is a necessary condition and is safe under overlapping rectangles because a forced neighbour is included only once in \(F_v\). It may be weaker than a full graph constraint, but it never overstates the charge by summing the same vertex's excess twice.

The edge endpoint convention is important: an edge may legitimately constrain both endpoint excesses because \(K=\sum_vx_v\); this is not duplicate charging. Duplicate charging occurs only if the same vertex's required excess is added more than once in the budget sum.

## 3. Rectangle abstraction

For a pair connector \(z\), its two nonneighbour sets \(A\subset X_i\), \(B\subset X_j\) form a complete bipartite graph. If the effective capacities after known focus neighbours are \(p,q\), the local necessary charge is
\[
R_{pq}(|A|,|B|)
=|A|(|B|-p)_+ + |B|(|A|-q)_+.
\tag{6}
\]
For positive \(a,b\), use the certified threshold bounds:
\[
\begin{array}{ll}
R_{22}\ge a+b-4,&R_{22}\ge a+b-3\ (a+b\ge5),\\
R_{23}\ge a+b-5,&R_{23}\ge a+b-4\ (a+b\ge6),\\
R_{24}\ge a+b-6,&R_{24}\ge a+b-5\ (a+b\ge7),\\
R_{33}\ge a+b-6,&R_{33}\ge a+b-4\ (a+b\ge7).
\end{array}
\tag{7}
\]

A sum of two rectangle charges is justified when their opposite blocks are disjoint and the shared-block forced-neighbour sets are disjoint; same-missing-anchor nonadjacent connectors provide this latter disjointness. If two adjacent same-group connectors may have overlapping supports, do not sum their full charges. Use the pointwise union-load inequality (4), or the already proved safe pair bound \(k_1+k_2+\max(R_1,R_2)\) only when its hypotheses are satisfied.

## 4. Focus costs

If a connector is complete to \(X_i\), each \(v\in X_i\) has a known external neighbour consuming one unit of its baseline external capacity. Thus every rectangle incident with \(X_i\) must use the reduced effective capacity. This reduction is not an extra global charge to add on top of \(R_{pq}\): it changes the capacity used inside (6).

When several focused connectors meet a block, reduce capacity by the number of **distinct** focused neighbours actually forced on each vertex. If two focus owners cannot coexist by the clique/common-nonneighbour lemma, that pattern is rejected before charge arithmetic.

## 5. Equality-budget protocol

For \(K=8\), use the following exact protocol:
1. Partition \(K=K_C+K_X\).
2. Fix a connector adjacency/focus pattern and use the exact equations (2)–(3).
3. For each exclusive vertex, form the union \(F_v\) of all forced external neighbours and charge (4) once.
4. Sum only after checking the supports/union loads; record the residual budget \(8-\text{charged amount}\).
5. If the residual is zero, every uncharged vertex is exact. If the residual is one or two, do not use a saturation contradiction that requires those vertices to be exact unless the argument separately locates the residual excess.
6. Apply the independent-four, clique-cap, and common-nonneighbour-clique constraints to the remaining exact/saturated vertices.
7. Mark an integer/connector profile as a **necessary skeleton** until all graph constraints have been verified. Do not label it realizable without an explicit graph.

## 6. Proven theorem interface

The backend may currently call:
- \(K\ge8\) for all \(r\ge12\);
- \(K\ge10\) for all \(r\ge14\);
- if \(K=8\), then \(r\le13\), and the remaining geometries are exactly those indexed in EQUALITY_K8_CLASSIFICATION.md.

No further claim is available yet for \(r=12,13\). In particular, the current interface does not identify residual-pivot costs or repeated-colour incidence variables from sibling workstreams with specific graph vertices or edges. Such a mapping must be supplied and proved by the backend owner before these quantities can be added to (1)–(5).
