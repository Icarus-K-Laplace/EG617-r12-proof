# E408 Q32 — source-pattern audit for the x-in-H two-double mode

Date: 2026-10-29  
Status: **Conditional source-incidence classification, independently checked on the 7-vertex residual graph.** This is not a full Q32 closure.

## 1. Contract and notation

Assume all ten isolated K5 components are single-outside, while both special K5 factors \(N_s,N_t\) are double-outside and the special point \(x_C\in H\). Then the seven H-vertices of the gadget are
\[
\{x\}\cup (N_s\cap H)\cup(N_t\cap H),
\]
where \(x\in T_0\), and each of \(N_s\cap H,N_t\cap H\) is a transversal triangle across \(T_1,T_2,T_3\).

Write
\[
a=|A_0\cap H|,\qquad A_0\subsetneq N_s,\quad A_0\ne\varnothing.
\]
The source gadget edges are \(yA_0\), \(x(N_s\setminus A_0)\), and \(x(N_t\setminus\{y\})\). The H-H edges among these, together with the two special K5 interiors, determine the seven-vertex residual color graph.

Every \(x\in T_0\) must have C-neighbors in all three large tracks, and pointwise balanced-coloring saturation gives \(d_C(x,H)\in\{3,4\}\). Since \(N_s\) has three H-vertices and \(N_t\) has three H-vertices,
\[
d_C(x,H)=(3-a)+
\begin{cases}
3,&y\in O,\\
2,&y\in H.
\end{cases}
\]
Thus \(y\in O\) forces \(a\in\{2,3\}\), while \(y\in H\) forces \(a\in\{1,2\}\).

## 2. Exact conditional case table

| Placement | \(a\) | \(d_C(x,H)\) | \(g_C=e_C(H)-69\) | \(t_C\) | Residual baseline | Source-forced surplus pattern |
|---|---:|---:|---:|---:|---|---|
| \(y\in O\) | 3 | 3 | 0 | 0 | Class A, \(\alpha=2\) | No extra edge |
| \(y\in O\) | 2 | 4 | 1 | 1 | Class A, \(\alpha=2\) | One T0--large edge \(x s_p\) |
| \(y\in H\) | 2 | 3 | 2 | 0 | Class B, \(\alpha=3\) | Two large-pair edges \(y s_j,y s_k\), a star centered at \(y\) |
| \(y\in H\) | 1 | 4 | 2 | 1 | Class B, \(\alpha=3\) | One large-pair edge \(y s_p\) and one T0--large edge from \(x\), with pair types disjoint |

Here \(t_C\) counts surplus edges on the three T0--\(T_i\) pairs. In the \(y\in H,a=2\) row, the track of \(y\) is the unique track containing the one H-vertex of \(N_s\setminus A_0\); the two H-vertices of \(A_0\) lie in the other two tracks. Hence the two \(yA_0\) edges are a star across the two large-pair types incident to \(y\).

In the \(y\in H,a=1\) row, let \(p\) be the track of the unique H-vertex of \(A_0\), and \(q\) the track of \(y\). Necessarily \(p\ne q\), because otherwise \(x\) would have no C-neighbor in one large track. The two H-vertices of \(N_s\setminus A_0\) occupy tracks other than \(p\), and the two H-vertices of \(N_t\setminus\{y\}\) occupy tracks other than \(q\). Their unique overlap is the third track \(r\). The extra T0 edge is on \(T_0T_r\), while \(yA_0\) is on \(T_pT_q\); these pair types are disjoint.

The \(y\in H,a=1\) row is a **conditional** complementary-pair law for this source mode only. It must not be generalized to every class-B \((g_C,t_C)=(2,1)\) residual: the source-correct \(x_C\in O\), \(N_s\) single-outside, \(N_t\) double-outside example in V47_Z01_SHARED_P_FACTOR_PACKING.md has a valid pair-sharing pattern because the selected Hall matching may use a gadget edge as baseline.

## 3. Exact local verifier

The companion script verify_v47_z01_two_double_source_pattern_audit.py enumerates all permutations of the three large-track labels and both baseline choices at the overlap track. It verifies:
- each baseline has nine edges;
- source completion adds exactly \(g_C=0,1,2,2\) edges in the four rows;
- the full residual graph has \(\alpha\le2\);
- the two class-B rows have baseline \(\alpha=3\) and completed \(\alpha=2\);
- the star and disjoint-pair signatures in the table hold for every relabeling.

This classification is limited to the x-in-H two-double source mode. The x-outside and triple-outside modes remain governed by their own source-placement constraints. No global Q32 closure is claimed.
