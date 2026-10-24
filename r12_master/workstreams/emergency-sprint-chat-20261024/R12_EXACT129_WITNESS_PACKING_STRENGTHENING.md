# Exact-129 witness-packing strengthening for the r=12 sprint

Date: 2026-10-25  
Status: **PROVED under the stated T61 / d3-support contract.**  
Scope: E407 Q32 templates and the E408 Q33/d3 support branch. This is a necessary-structure theorem, not a terminal exclusion.

## 1. Contract

Let \(F\) be a genuine 61-vertex T61 residual with
\[
\alpha(F)\le5,\quad \omega(F)\le11,\quad e(F)\in\{407,408\},
\]
and a legal degree-13 pivot \(p\). Put
\[
A=N_F(p),\quad |A|=13,\qquad H=V(F)\setminus(A\cup\{p\}),\quad |H|=47,
\]
and assume the retained core contract
\[
\alpha(H)\le4,\quad \omega(H)\le11,\quad \delta(H)\ge12.
\]

For the shell-support branch under study, split \(A=S\dot\cup B\), where \(|S|=3\), \(|B|=10\), and assume \(B\) is a target clique. Equivalently, for \(M=\overline{F[A]}\), \(M[B]\) is empty. This is part of the E407 Q32 template contract and the retained E408 Q33/d3 contract; it is **not** assumed for arbitrary E408 Q32 states.

For a non-target color \(C\), assume the retained constrained second-Turan/Kang–Pikhurko equality classification: if \(e(C[V(F)])=129\), then \(C[V(F)]\) has ten disjoint isolated \(K_5\) components and an 11-vertex exceptional gadget. The edge-coloring gives every edge exactly one color.

## 2. Theorem: at least seven no-\(S\) witness sets per exact-129 color

**Theorem 2.1.** For every exact-129 non-target color \(C\), at least seven of its ten \(K_5\) components have vertex set
\[
\{b\}\cup Q,\qquad b\in B,\quad Q\subseteq H,\quad |Q|=4,
\]
where \(Q\) is independent in \(H\) and \(b\) is target-anticomplete to \(Q\).

**Proof.**

1. The ten \(K_5\) components are pairwise vertex-disjoint. Since \(|S|=3\), at most three of them can contain any vertex of \(S\). Hence at least seven components avoid \(S\).
2. Every component avoiding \(S\) lies in \(B\cup H\). Since \(B\) is a target clique, it is independent in the non-target color \(C\); thus a \(C\)-colored clique contains at most one vertex of \(B\).
3. Such a component cannot lie entirely in \(H\): all its ten edges would be non-target edges, so its five vertices would form an independent 5-set in the target graph \(H\), contradicting \(\alpha(H)\le4\).
4. Therefore every \(K_5\) component avoiding \(S\) contains exactly one \(b\in B\) and four vertices \(Q\subset H\). Since all six pairs inside \(Q\) have color \(C\), \(Q\) is independent in \(H\); since the four \(bq\) edges also have color \(C\), \(b\) is target-anticomplete to \(Q\). Distinct components have distinct \(b\)-labels. \(\square\)

This strengthens the weaker five-witness count recorded in the earlier cross-cut note. It uses the same contract and no new extremal input.

## 3. Cross-color linearity and the number of witnesses

Two witness 4-sets from different color components intersect in at most one core vertex. If they shared two vertices \(x,y\), then edge \(xy\) would have two non-target colors. Within a single color, the witness sets are pairwise disjoint because they come from distinct \(K_5\) components.

Thus all witness sets form a linear 4-uniform family on the same 47-point core: distinct sets intersect in at most one vertex.

The total non-target excess on the 61-point residual is
\[
\sum_C(e(C)-129)=411-e(F).
\]
Therefore:
- for E407, the excess is \(4\), so at least \(11-4=7\) colors are exact-129; Theorem 2.1 gives **at least 49** labelled witness 4-sets;
- for E408, the excess is \(3\), so at least \(11-3=8\) colors are exact-129; under the d3 shell-support contract, Theorem 2.1 gives **at least 56** labelled witness 4-sets.

These are distinct labelled components, not necessarily disjoint across colors; the proved intersection cap is one vertex.

## 4. Corollary for E407 templates A and C

In templates A and C, the retained row-type screen gives
\[
|N_M(s)\cap B|\ge6\qquad\text{for each }s\in S.
\]
For each \(b\in B\), regularity gives \(t_b=|N_F(b)\cap H|=k_b=d_M(b)\le3\). Put
\[
c_S=e_M(S,B)=\sum_{b\in B}k_b=e(M)-e(M[S])\le30.
\]

Call a witness \(Q\) **hub-complete** if it hits all three shell rows in \(S\). If \(Q\) is not hub-complete, choose \(s\in S\) whose row it misses. For every \(b'\in N_M(s)\cap B\), the set \(Q\cup\{s,b'\}\) would be an independent 6-set unless \(Q\) hits row \(b'\). Therefore \(Q\) is target-adjacent to at least six distinct \(B\)-rows, requiring at least six distinct \(B\)-to-\(H\) target edges with core endpoint in \(Q\).

Fix one exact-129 color. Its at least seven witness sets are disjoint in \(H\), so their required \(B\)-to-\(H\) edges are distinct across witnesses. There are only \(c_S\le30\) such edges in total. Hence at most
\[
\left\lfloor\frac{c_S}{6}\right\rfloor\le5
\]
of the seven witnesses can be non-hub-complete.

**Conclusion.** Every exact-129 color in E407 template A or C has at least
\[
7-\left\lfloor c_S/6\right\rfloor\ge2
\]
hub-complete witness sets. Since there are at least seven exact-129 colors, these branches contain at least **14 hub-complete witness occurrences** across colors.

This does not yet contradict the 284-edge core: the same core vertex may occur in multiple witness sets across colors, subject to the one-vertex intersection rule and its non-target degree capacity.

## 5. Exact limitations and next theorem

This result does **not**:
- prove that witness sets coincide;
- infer that a local shell template has a legal parent graph;
- eliminate E407 Q32, E408 Q33/d3, or E408 Q32;
- transfer the d3-support contract to arbitrary E408 Q32 states;
- replace the original \(K_{145}\to T61\) bridge or any retained lower-order seed.

The next useful theorem must exploit the **labelled overlap graph** of the 49/56 witness sets together with the exact degree sequence of the same core \(H\), rather than summing their incidences as if witnesses were disjoint across colors.