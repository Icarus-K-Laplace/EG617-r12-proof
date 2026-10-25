# E407 Q32: strict reduction of the \u03b4=14 K5-saturated branch

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL strict reduction**, not a contradiction. Dependencies: the retained T61/49-witness core contract; Brouwer's second-Turan bound for non-bipartite triangle-free graphs; and the stated theorem from Didin's 2026 author-prepared preprint, whose journal submission was under review as of 2026-09-18.

## 1. Frozen terminal contract

Let \(U\) have 29 vertices and let
\[
G=H[U],\qquad L=\overline G.
\]
Assume
\[
e(G)=98,\quad \alpha(G)=4,\quad \omega(L)=4,
\]
and that \(L\) is non-four-partite and \(K_5\)-saturated. The 49 selected witnesses are pairwise edge-disjoint \(K_4\)'s in \(L\).

This is the only remaining \(\delta=14\) non-four-partite branch after the augmentable-edge terminal was excluded in DELTA14_NONPARTITE_AUGMENTABLE_TERMINAL_CLOSURE.md.

## 2. Saturation makes \(G\) \(\alpha\)-critical

For every edge \(uv\in E(G)\), the pair \(uv\) is a nonedge of \(L\). Since \(L\) is \(K_5\)-saturated, adding \(uv\) to \(L\) creates a \(K_5\). In the complement, deleting \(uv\) from \(G\) therefore creates an independent 5-set. Since \(\alpha(G)=4\),
\[
\boxed{\alpha(G-uv)=5\quad\text{for every }uv\in E(G).}
\]
Thus \(G\) is \(\alpha\)-critical.

Moreover, every proper spanning subgraph of \(G\) has independence number at least five: if it omits an edge \(e\), it is a subgraph of \(G-e\). Consequently, the only spanning \(\alpha\)-critical subgraph of \(G\) with the same independence number is \(G\) itself. In the notation below, the maximum component count \(p\) equals the actual number of connected components of \(G\).

## 3. The number of components is exactly three

We use the following external result, stated here as an explicit dependency rather than reproved:

> **Didin's independence-number Turan bound (2026 preprint).** If a graph has \(n\) vertices, \(m\) edges, independence number \(\alpha\), and \(p\) is the maximum number of connected components among its spanning \(\alpha\)-critical subgraphs with the same independence number, then, with \(s=\alpha-p\),
> \[
> m\ge t(n+s,\alpha)-s,
> \]
> where \(t(N,\alpha)\) is the edge count of the balanced disjoint union of \(\alpha\) cliques on \(N\) vertices.

Source: Maksim Didin, *A Generalization of Turan's Theorem for Graphs with a Given Independence Number*, author-prepared preprint, Zenodo record 22831382, version 1 (2026-09-18; described there as submitted to the Journal of Graph Theory and under review). The proof of this external theorem has not been independently audited in this workstream.

Let \(p\) be the number of components of \(G\). We have \(p\le4\), since every component contributes at least one to \(\alpha(G)=4\). If \(p=4\), every component has independence number one and is therefore a clique; then \(L\) is complete four-partite, contrary to the contract. Hence \(p\le3\).

If \(p=1\), then \(s=3\) and
\[
e(G)\ge t(32,4)-3=4\binom82-3=109,
\]
contrary to \(e(G)=98\).

If \(p=2\), then \(s=2\) and
\[
e(G)\ge t(31,4)-2=
\left(\binom72+3\binom82\right)-2=103,
\]
again a contradiction.

Therefore
\[
\boxed{p=3.}
\]
The component independence numbers are consequently \(1,1,2\). Write
\[
G=K_a\ \dot\cup\ K_b\ \dot\cup\ C,
\qquad a+b+c=29,
\]
where \(C\) is connected, \(\alpha(C)=2\), and \(C\) is itself \(\alpha\)-critical.

## 4. A lower bound for the 2-independence component

Put \(J=\overline C=L[V(C)]\). Since \(\alpha(C)=2\), the graph \(J\) is triangle-free. Since \(C\) is \(\alpha\)-critical, adding any nonedge to \(J\) creates a triangle, so \(J\) is triangle-free saturated.

The graph \(J\) cannot be bipartite. Indeed, a bipartite triangle-free saturated graph must be complete bipartite: any missing cross-part edge could otherwise be added without creating a triangle. The complement of a complete bipartite graph is a disjoint union of two cliques, contradicting connectedness of \(C\).

Brouwer's second-Turan bound for a non-bipartite triangle-free graph gives
\[
e(J)\le \left\lfloor\frac{c^2}{4}\right\rfloor
-\left\lfloor\frac c2\right\rfloor+1.
\]
Consequently,
\[
\boxed{e(C)\ge \left\lfloor\frac{c^2}{4}\right\rfloor-1.} \tag{1}
\]
Also \(c\ge5\), because \(J\) is non-bipartite and triangle-free.

## 5. The 49 witnesses force two independent capacity constraints

Because \(G=K_a\dot\cup K_b\dot\cup C\), the graph \(L\) is the complete join of two independent sets of sizes \(a,b\) and the triangle-free graph \(J\).

Every \(K_4\) in \(L\) must contain exactly:
- one vertex from the independent set of size \(a\);
- one vertex from the independent set of size \(b\);
- two vertices forming an edge of \(J\).

It cannot use two vertices from either independent set, or three vertices from \(J\), since \(J\) is triangle-free. Thus each of the 49 edge-disjoint witness \(K_4\)'s uses a distinct \(A\)-to-\(B\) edge and a distinct edge of \(J\). Hence
\[
\boxed{ab\ge49,\qquad e(J)\ge49.} \tag{2}
\]

The exact edge ledger is
\[
98=\binom a2+\binom b2+e(C),\qquad
e(J)=\binom c2-e(C). \tag{3}
\]
Combining (1)--(3) yields the finite integer constraints
\[
\begin{gathered}
a+b+c=29,\quad 1\le a\le b,\quad 5\le c\le15,\quad ab\ge49,\\
e(C)=98-\binom a2-\binom b2,\\
\left\lfloor c^2/4\right\rfloor-1
\le e(C)\le\binom c2-49.
\end{gathered}
\]
The checked-in verifier exhausts these integer possibilities. There is exactly one:
\[
\boxed{(a,b,c,e(C),e(J))=(7,7,15,56,49).}
\]

## 6. The unique surviving kernel is highly rigid

Under the saturated-branch contract, the induced structure must be
\[
\boxed{H[U]=K_7\ \dot\cup\ K_7\ \dot\cup\ D},
\]
where \(D\) here denotes a connected 15-vertex \(\alpha\)-critical graph with \(\alpha(D)=2\) and 56 edges (not a claim that it is a 15-cycle). Its complement \(J\) is a triangle-free, non-bipartite, triangle-saturated graph on 15 vertices with exactly 49 edges.

Since \(|A||B|=e(J)=49\), every one of the 49 witnesses uses a different \(A\)-\(B\) pair and a different edge of \(J\); both sets of 49 objects are exhausted. For each fixed \(a_0\in A\), the seven witness edges in \(J\) paired with \(a_0\) form a matching: if two shared a vertex \(x\in V(J)\), their witness \(K_4\)'s would share the edge \(a_0x\). The same holds for each fixed \(b_0\in B\). Therefore:
- \(E(J)\) has a proper edge-coloring by the seven labels in \(A\), each color class a 7-edge matching;
- it has a second proper edge-coloring by the seven labels in \(B\), also with each color class a 7-edge matching;
- every ordered pair of colors \((a_0,b_0)\in A\times B\) labels exactly one edge.

In particular, \(\Delta(J)\le7\) and
\[
\sum_{v\in V(J)}(7-d_J(v))=105-2\cdot49=7.
\]

## 7. Status and next exact target

This is a **strict reduction**, not an exclusion. The saturated branch has been reduced to a single 15-vertex graph-realization problem. That graph-only target is now superseded: DELTA14_SATURATED_LOCAL_MODEL.md explicitly realizes a triangle-free, non-bipartite, triangle-saturated 15-vertex graph with 49 edges and the required orthogonal matching decompositions. The next target is the full W/core/shell extension, not a contradiction from the 15-vertex graph alone.

Dependencies and limitations:
- The component-count step uses Didin's 2026 author-prepared preprint theorem, which remains an external, not independently audited dependency here.
- The triangle-free bound uses Brouwer's second-Turan theorem.
- The integer verifier checks only the arithmetic enumeration, not graph realization or the external theorem.
- The five E407 shell templates, the low-\(\delta\) cases, the original \(K_{145}\)-to-T61 bridge, and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.


## 8. Correction: the 15-vertex local obstruction is realizable

The proposed target in Section 7—proving that no triangle-free, non-bipartite, triangle-saturated 15-vertex graph with 49 edges admits the matching structure—is now known to be false. DELTA14_SATURATED_LOCAL_MODEL.md gives an explicit blow-up of \(C_5\) with part sizes \((5,5,2,1,2)\), together with a verified cell-to-edge bijection and the third coloring \(\kappa=x+y\pmod7\). It realizes the 29-point saturated graph and all 49 witness sets, partitioned into seven classes of seven disjoint witnesses.

The correct next target is the extension problem: can this local \(H[U]\) be completed by \(W\) and the shell rows while satisfying the exact degree, clique, independence, and row-label constraints? The local model does not provide such a completion and is not a global counterexample.
