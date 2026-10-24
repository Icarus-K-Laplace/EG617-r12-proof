# Audit of the high-multiplicity witness-star dichotomy

Date: 2026-10-25  
Source audited: sibling artifact R12_WITNESS_OVERLAP_STAR_LEMMA.md, emergency-sprint branch.  
Verdict: **basic star lemma valid; claimed edge dichotomy unsupported.**

## 1. Valid part

Suppose m witness sets have the form
\[
Q_i=\{x\}\cup P_i,\qquad |P_i|=3,
\]
where the Q_i are independent four-sets in H and pairwise intersect in at most one vertex.

Then the P_i are pairwise disjoint independent triples, x is anticomplete to their union U, and \(\alpha(H[U])\le3\). Turán's theorem gives
\[
e(H[U])\ge {3m\choose2}-t_3(3m)=3{m\choose2}.
\]
For m=10, |U|=30 and e(H[U])≥135. These statements are valid.

## 2. Gap in the claimed dichotomy

The sibling artifact argues that if e(H[U])≤143, then L=\(\overline{H[U]}\) has at least 292 edges. Brouwer's second-Turán bound gives at most 291 edges for a non-tripartite K4-free graph on 30 vertices, so L is tripartite.

That conclusion is only **tripartite**, not **complete tripartite**. The ten disjoint triangles P_i force each of the three parts to have size ten, but do not force every cross-part edge to be present. Hence H[U] may be three K10 cliques plus g cross-part edges, with \(0\le g\le8\), when e(H[U])≤143. The asserted dichotomy
\[
e(H[U])=135\quad\text{or}\quad e(H[U])\ge144
\]
does not follow.

## 3. Explicit local obstruction to the inference

Take three disjoint K10 cliques A,B,C in H[U], and add one cross-edge \(a_0b_1\) between A and B. Then
\[
e(H[U])=3{10\choose2}+1=136.
\]
The ten triples \(P_i=\{a_i,b_i,c_i\}\) remain independent provided the added edge uses different indices (for example a_0b_1). Also \(\alpha(H[U])=3\): each clique contributes at most one vertex to an independent set, and the single cross-edge can only reduce the choices. The complement is tripartite with one cross-part edge missing, not complete tripartite.

This is a local counterexample to the *inference*, not a counterexample to the full 47-core theorem. It is not asserted to extend to a 47-vertex graph satisfying every degree/excess condition.

## 4. What remains valid

The exact equality case e(H[U])=135 does force L to be the complete balanced tripartite graph, hence H[U]=3K10. The sibling proof that this exact equality case forces \(\epsilon_x\ge1\) may still be valid under its full global degree/excess contract. What fails is the jump from “L is tripartite” to “L is complete tripartite” for all e(H[U])≤143.

This workstream does not use the unsupported dichotomy. Any attempt to revive it must separately rule out g=1,...,8 using the full 47-core degree/excess and shell-row constraints.
