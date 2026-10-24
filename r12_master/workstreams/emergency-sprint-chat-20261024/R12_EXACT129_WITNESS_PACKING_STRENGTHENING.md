# Exact-129 witness packing — audited corrected version

Date: 2026-10-25  
Status: **CORRECTED THEOREM PROVED UNDER THE STATED T61 / d3-SUPPORT CONTRACT.**  
Scope: E407 Q32 templates and E408 Q33/d3. Necessary structure only; no terminal exclusion.

## Audit correction to the initial version

The initial version at blob `af56a4720b4f3aa7e63c70089e812bc8a48d3a00` incorrectly claimed at least seven *B-labelled* witness sets per exact-129 color. Its proof said every component avoiding S lies in B∪H, but omitted the pivot p. A K5 component of C[V(F)] can contain p and four H vertices while avoiding S. At most one component can do this, but it cannot be silently ignored.

The valid lower bound is **six** B-labelled no-S components per exact-129 color. All counts below use this corrected bound.

## 1. Contract

Let F be a genuine 61-vertex T61 residual with
\[
\alpha(F)\le5,\quad \omega(F)\le11,\quad e(F)\in\{407,408\},
\]
and a legal degree-13 pivot p. Put
\[
A=N_F(p),\quad |A|=13,\qquad
H=V(F)\setminus(A\cup\{p\}),\quad |H|=47,
\]
with
\[
\alpha(H)\le4,\quad \omega(H)\le11,\quad \delta(H)\ge12.
\]

For the shell-support branch under study, split \(A=S\dot\cup B\), where \(|S|=3\), \(|B|=10\), and B is a target clique. Equivalently, for \(M=\overline{F[A]}\), \(M[B]\) is empty. This holds for E407 Q32 templates A/C and the retained E408 Q33/d3 contract; it is **not** assumed for arbitrary E408 Q32 states.

For a non-target color C, assume the registered constrained second-Turan/Kang–Pikhurko equality classification: if \(e(C[V(F)])=129\), then \(C[V(F)]\) has ten disjoint isolated \(K_5\) components and an 11-vertex exceptional gadget.

## 2. Corrected theorem: at least six B-labelled witness sets

**Theorem 2.1.** For every exact-129 non-target color C, at least six of its ten isolated \(K_5\) components have vertex set
\[
\{b\}\cup Q,\qquad b\in B,\quad Q\subseteq H,\quad |Q|=4,
\]
where Q is independent in H and b is target-anticomplete to Q.

**Proof.**

1. The ten \(K_5\) components are pairwise vertex-disjoint. Since \(|S|=3\), at most three of them meet S. Hence at least seven components avoid S.
2. Among those seven, at most one contains p, because the components are disjoint and p is a single vertex.
3. Every component avoiding both S and p lies in B∪H. Since B is a target clique, it is independent in the non-target color C, so a C-monochromatic clique contains at most one vertex of B.
4. Such a component cannot lie entirely in H: its five vertices would be target-independent in H, contradicting \(\alpha(H)\le4\). Therefore every component avoiding S and p has exactly one b∈B and four vertices Q⊂H.
5. The six edges within Q and the four bq edges all have color C, so Q is independent in target H and b is target-anticomplete to Q. \(\square\)

The six witness sets for a fixed color are pairwise disjoint in H. Across distinct color components, their Q sets intersect in at most one core vertex, because sharing two vertices would force their connecting edge to have two colors.

## 3. Corrected global counts

The total non-target excess on the 61-point residual is
\[
\sum_C(e_C(V(F))-129)=411-e(F).
\]
Therefore:
- E407: excess 4, so at least 7 exact-129 colors; at least **42** labelled witness 4-sets.
- E408: excess 3, so at least 8 exact-129 colors; under the d3 shell-support contract, at least **48** labelled witness 4-sets.

These are labelled components, not necessarily disjoint across colors; the proved intersection cap is one vertex. E408 Q32 is not covered unless its own reduction proves \(M[B]=\varnothing\).

## 4. Corrected E407 template A/C corollary

In templates A and C, each hub s∈S misses at least six B rows in M. Every b∈B is regular with \(t_b=|N_F(b)\cap H|=k_b=d_M(b)\le3\). Since \(M[S]=M[B]=\varnothing\),
\[
c_S:=e_M(S,B)=\sum_{b\in B}k_b\le30.
\]
The equality \(t_b=k_b\) makes \(c_S\) exactly the total target-edge budget between B and H.

Call Q hub-complete if it hits all three rows in S. If Q is not hub-complete, choose a hub s missed by Q. For every \(b'\in N_M(s)\cap B\), Q must hit b'; otherwise \(Q\cup\{s,b'\}\) is a target-independent 6-set. Hence this witness requires at least six distinct B–H target edges with core endpoint in Q.

For one fixed exact-129 color, its six witness sets are disjoint in H, so the required B–H edges are distinct across witnesses. Since \(c_S\le30\), at most five of the six witnesses can be non-hub-complete. Thus each exact-129 color in E407 template A/C has at least **one** hub-complete witness. Across at least seven exact-129 colors, this gives at least **seven** hub-complete witness occurrences.

The previous claims of seven witnesses per color and at least fourteen hub-complete occurrences are withdrawn; the corrected bounds are six and seven, respectively.

## 5. Exact limitations

This result does not prove that witness sets coincide, does not establish a legal parent graph from a local template, and does not eliminate E407 Q32 or E408 Q33/d3. It cannot be transferred to arbitrary E408 Q32 without its missing \(M[B]=\varnothing\) contract. The original K145-to-T61 bridge and all lower-order dependencies remain separate obligations.

The next theorem must use the corrected labelled overlap/capacity system on the 284-edge core, with the pivot component explicitly tracked rather than silently discarded.
