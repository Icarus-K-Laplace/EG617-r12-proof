# External extremal theorem scope audit: AES and Kang–Pikhurko

Date: 2026-11-03
Frozen integration: `c5f05f5868ed4d1347dc6d16f9d5b5be230ac7e2`.
Audit branch: `workstream/r12-astra-independent-audit-20261102`.

## Verdict

**NO HYPOTHESIS MISMATCH FOUND.** The two external extremal inputs used in the frozen proof are being applied in their exact parameter ranges. This check inspected the original AES paper and the Kang–Pikhurko paper, not only repository summaries.

## 1. Andrásfai–Erdős–Sós (AES), 1974

Original source: B. Andrásfai, P. Erdős and V. T. Sós, *On the connection between chromatic number, maximal clique and minimal degree of a graph*, Discrete Mathematics 8 (1974), 205–218, Theorem 1.1, printed p.207.

The theorem states, for integer (r\ge3), that at most two of the following can hold:
1. (K_r\not\subseteq G);
2. (delta(G)>\frac{3r-7}{3r-4}n);
3. (chi(G)\ge r).

Thus the first two hypotheses imply (chi(G)\le r-1).

### 1.1 The 35-point CORE211 application

The complement graph (L=\overline H) is (K_4)-free, has (n=35), and is 22-regular if the target core (H) has exactly210 edges. Set (r=4). The AES threshold is
[
\frac{3r-7}{3r-4}n=\frac58\cdot35=21.875.
]
Since (delta(L)=22>21.875), AES gives (chi(L)\le3), i.e. (L) is 3-partite. One part has at least (\lceil35/3\rceil=12) vertices; that part is independent in (L), hence a (K_{12}) in (H), contradicting (omega(H)\le11). Therefore (e(H)\ne210), and the prior lower bound (e(H)\ge210) improves to (e(H)\ge211).

### 1.2 The 23-point two-K10-completer strengthening

In the E286 strengthening, a 23-vertex induced graph (F) is triangle-free and has minimum degree at least10. Set (r=3). The AES threshold is
[
\frac{3r-7}{3r-4}n=\frac25\cdot23=9.2.
]
Thus (delta(F)=10>9.2) gives (chi(F)\le2), so (F) is bipartite. This is exactly the conclusion needed there. This strengthening is not a load-bearing premise of the frozen E286 theorem; the frozen proof only needs its weaker common-neighbor bound.

## 2. Kang–Pikhurko, 2005

Original source: M. Kang and O. Pikhurko, *Maximum (K_{r+1})-free graphs which are not (r)-partite*, Matematychni Studii 24 (2005), 12–20, Theorem 1, printed p.13.

Theorem 1 states that for (n\ge r+3), (r\ge2),
[
p_r(n)=
\begin{cases}
t_r(n)-2,&r>(n-1)/2,\\
t_r(n)-\lfloor n/r\rfloor+1,&r\le(n-1)/2,
\end{cases}
]
where (p_r(n)) is the maximum number of edges in an (n)-vertex (K_{r+1})-free graph that is not (r)-partite, and (t_r(n)=\operatorname{ex}(n,K_{r+1})).

For (n=49,r=12), both conditions hold:
[
49\ge15,qquad 12\le24.
]
Also (t_{12}(49)=1100) and (\lfloor49/12\rfloor=4), so every (K_{13})-free, non-12-partite graph (L) on49 vertices satisfies
[
e(L)\le1100-4+1=1097.
]
In the contextual (R(4,49)) argument, the complement of each non-target color graph is (K_{13})-free. It is not 12-partite because a 12-partition would give 12 cliques in the color graph, each of size at most4, covering at most48 vertices. Hence the theorem gives at least (1176-1097=79) edges in each of the eleven non-target colors, exactly as used in the source.

## 3. Disposition

- AES at ((n,r)=(35,4)): hypotheses and strict threshold verified.
- AES at ((n,r)=(23,3)): hypotheses and strict threshold verified.
- Kang–Pikhurko at ((n,r)=(49,12)): hypotheses and exact nonpartite bound verified.
- No external theorem statement needs correction for these applications.

This is an external-leaf scope audit only. It does not certify the analytic graph reductions, the complete root build, Lean kernel proof, or referee acceptance.
