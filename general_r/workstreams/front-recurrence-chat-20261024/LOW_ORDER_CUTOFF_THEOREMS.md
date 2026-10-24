# Low-Order Cutoff Theorems from the Inherited Cap

Date: 2026-10-24  
Status: **PROVED for r >= 6; explicit small-parameter obstructions recorded.**

## 1. State contract and notation

Let \(\mathcal C_r(a,n)\) denote the contextual class of graphs \(J\) on \(n\) vertices satisfying
\[
\alpha(J)\le a,\qquad \omega(J)\le r-1,
\]
and every inherited induced-subgraph cap
\[
e(J[Y])\le D_r(|Y|),\qquad
D_r(m)=\binom m2-(r-1)p_r(m).
\]
Here \(p_r(m)\) is the Turán-complement floor
\[
p_r(m)=\sum_{k=1}^{r}\binom{n_k}{2},
\quad m=qr+b,\quad
p_r(m)=r\binom q2+bq,\quad 0\le b<r,
\]
where the balanced r-partition has b parts of size q+1 and r-b parts of size q.

Write \(M_r(a)\) for the largest n for which the contextual class is not certified empty. These theorems concern the stated abstract state contract, not arbitrary graphs without the inherited cap.

For \(H=\overline J\), the contract gives
\[
\omega(H)=\alpha(J)\le a,\qquad
\alpha(H)=\omega(J)\le r-1,
\]
and
\[
e(H)=\binom n2-e(J)\ge (r-1)p_r(n).
\]

## 2. Theorem H.C2 — M_r(2) <= 2r-1 for r >= 6

**Theorem.** For every integer \(r\ge6\), no graph in \(\mathcal C_r(2,n)\) exists for any \(n\ge2r\). Hence
\[
\boxed{M_r(2)\le2r-1\qquad(r\ge6).}
\]

### Case n >= 2r+1

The complement H is triangle-free because \(\omega(H)\le2\). Every neighborhood in a triangle-free graph is independent, so \(\Delta(H)\le\alpha(H)\le r-1\). Therefore
\[
e(H)\le\frac{n(r-1)}2.
\]
For \(n\ge2r+1\), every part in the balanced r-partition defining \(p_r(n)\) has size at least 2 and at least one has size at least 3. Hence \(p_r(n)>n/2\), and the inherited cap requires
\[
e(H)\ge(r-1)p_r(n)>\frac{n(r-1)}2,
\]
a contradiction. Thus no state with \(n\ge2r+1\) exists for any \(r>3\).

### Boundary case n = 2r

Now \(p_r(2r)=r\). The cap and degree bound give
\[
r(r-1)\le e(H)\le\frac{2r(r-1)}2=r(r-1).
\]
Equality holds throughout, so H is \((r-1)\)-regular. For \(r\ge6\),
\[
\delta(H)=r-1>\frac{2(2r)}5=\frac{2n}5.
\]
The Andrásfai–Erdős–Sós theorem says that a triangle-free graph with minimum degree greater than \(2n/5\) is bipartite. A bipartite graph on 2r vertices has an independent part of size at least r, contradicting \(\alpha(H)\le r-1\).

**External theorem used:** B. Andrásfai, P. Erdős, V. T. Sós, “On the connection between chromatic number, maximal clique and minimal degree of a graph,” *Discrete Mathematics* 8 (1974), 205–218. The invoked special case is: triangle-free and \(\delta>2n/5\) implies bipartite.

## 3. Theorem H.C3 — M_r(3) <= 3r for r >= 6

**Theorem.** For every \(r\ge6\),
\[
\boxed{M_r(3)\le3r.}
\]

Suppose \(J\in\mathcal C_r(3,n)\) with \(n\ge3r+1\), and let v have minimum degree h. Its closed-neighborhood core
\[
J'=J-N_J[v]
\]
is an induced graph in \(\mathcal C_r(2,m)\), where \(m=n-h-1\): deleting the closed neighborhood reduces the independence cap from 3 to 2, while the clique and inherited caps are hereditary. Theorem H.C2 gives \(m\le2r-1\), so
\[
h\ge n-2r,\qquad
e(J)\ge\frac{nh}2\ge\frac{n(n-2r)}2.
\]
But the inherited cap says \(e(J)\le\binom n2-(r-1)p_r(n)\). These inequalities contradict one another whenever
\[
2(r-1)p_r(n)>n(2r-1),
\quad\text{equivalently}\quad
p_r(n)>\frac{n(2r-1)}{2(r-1)}.\tag{*}
\]

To verify (*), write \(n=ur+v\), \(0\le v<r\). If \(u\ge4\), then
\[
p_r(n)\ge\frac{n(u-1)}2\ge\frac{3n}2
>\frac{n(2r-1)}{2(r-1)}
\]
for \(r\ge6\). If \(u=3\), then \(n=3r+v\) with \(1\le v<r\), and
\[
p_r(n)=3r+3v.
\]
The difference between the two sides of (*) is
\[
2v-\frac{3r+v}{2r-2}
\ge 2-\frac{3r+1}{2r-2}
=\frac{r-5}{2r-2}>0.
\]
This proves the cutoff for every integer n in the full range, not merely at n=3r+1.

In particular, the outer state \((a,n)=(3,3r+1)\) is empty for \(r\ge6\). Directly at that boundary, \(h\ge r+1\) and
\[
e(J)\ge\frac{(3r+1)(r+1)}2,
\qquad
D_r(3r+1)=\frac{3r^2+3r+6}{2};
\]
the lower bound exceeds the cap by \((r-5)/2>0\).

## 4. Exact outer-state consequences

For the outer parameterization \(n=ar+t\), the t=1 states with a=2 and a=3 are now excluded for all \(r\ge6\):
- \((2,2r+1)\) is excluded by H.C2;
- \((3,3r+1)\) is excluded by H.C3.

The \((4,4r+1)\) coordinate is different: it is the intended extraction residual. It may be declared empty only under the contextual reductio that assumes no such residual exists. The \((5,5r+1)\) design-like terminal remains intentionally available.

## 5. Small-parameter audit: the cutoff is not all-r

The stronger cutoff \(M_r(2)\le2r-1\) is **false for r=4 and r=5 under the abstract state contract**. These are not full EG617 colorings; they show why the theorem must be thresholded and why the inherited-cap contract alone does not settle the small cases.

### r=4, n=8

Let H have vertices \(v,a,b,c,u_1,u_2,u_3,u_4\) and edges
\[
va,vb,vc,au_1,au_3,bu_1,bu_4,cu_2,cu_4,
u_1u_2,u_2u_3,u_3u_4.
\]
This is triangle-free with \(\alpha(H)=3\), \(\omega(H)=2\), and 12 edges. Its complement J has \(\alpha(J)=2\), \(\omega(J)=3\), and 16 edges, equal to \(D_4(8)\). Exact enumeration of all subsets gives the maximum induced edge count versus cap:

| m | max e(J[Y]) | D_4(m) |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 1 | 1 |
| 3 | 3 | 3 |
| 4 | 5 | 6 |
| 5 | 7 | 7 |
| 6 | 9 | 9 |
| 7 | 12 | 12 |
| 8 | 16 | 16 |

Thus \(J\in\mathcal C_4(2,8)\).

### r=5, n=10

Let H be the balanced blow-up of C5 with five parts of size 2, with all edges between consecutive parts. Then H is triangle-free, \(\alpha(H)=4\), \(\omega(H)=2\), and \(e(H)=20\). Its complement J satisfies \(\alpha(J)=2\), \(\omega(J)=4\), and \(e(J)=25=D_5(10)\). The maximum induced edge counts are:

| m | max e(J[Y]) | D_5(m) |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 1 | 1 |
| 3 | 3 | 3 |
| 4 | 6 | 6 |
| 5 | 8 | 10 |
| 6 | 11 | 11 |
| 7 | 13 | 13 |
| 8 | 16 | 16 |
| 9 | 20 | 20 |
| 10 | 25 | 25 |

These finite tables can be independently checked by enumerating all subsets; they are not used in the all-r proof. For r=5, the same graph can be described by part counts \(x_i\in\{0,1,2\}\), with
\[
e(J[Y])=\sum_i\binom{x_i}{2}+\sum_i x_i x_{i+2},
\quad \sum_i x_i=m,
\]
indices modulo 5, so only \(3^5=243\) count vectors need checking.

## 6. Status ledger

- \(M_r(2)\le2r-1\): **PROVED for r>=6**; abstract-contract counterexamples at r=4,5.
- \(M_r(3)\le3r\): **PROVED for r>=6**, by the preceding cutoff and minimum-degree pivot.
- General-r improvements to the five edge-floor seed coordinates: **OPEN**.
- All-state outer-budget dominance: **OPEN**.
- Explicit all-large-r EG617 contradiction: **NOT PROVED**.
