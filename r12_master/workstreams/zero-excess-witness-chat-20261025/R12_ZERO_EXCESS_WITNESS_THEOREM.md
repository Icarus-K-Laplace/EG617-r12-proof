# R12 zero-excess witness theorem and pairwise witness robustness

Date: 2026-10-25  
Branch: \`workstream/r12-zero-excess-witness-20261025\`  
Status: **PROVED_ANALYTIC** for the graph lemma; applications to exact-129 color components are **PROVED_CONDITIONAL** on the retained exact-129 factor theorem.

## 1. Scope and frozen contracts

This line attacks the common 284-edge core interface in E407 Q32 and E408 Q33, while also recording the limited extension to the 285-edge E408 Q32 core. It does not claim to eliminate any terminal.

Let \(H\) be the 47-vertex target core with
\[
\alpha(H)\le4,\qquad \delta(H)\ge12,\qquad e(H)\in\{284,285\}.
\]
Write
\[
\epsilon(v)=d_H(v)-12,\qquad E=\sum_{v\in V(H)}\epsilon(v)=2e(H)-564\in\{4,6\}.
\]
Let
\[
X=\{v:\epsilon(v)>0\},\quad k=|X|,\quad H_0=H-X.
\]
Every vertex of \(H_0\) has degree exactly 12 in \(H\). Since the parent T61 target graph \(F\) has minimum degree 13 and the pivot is anticomplete to \(H\), every \(x\in H_0\) has at least one target neighbour in the shell \(A\):
\[
d_F(x)=d_H(x)+d_F(x,A)=12+d_F(x,A)\ge13.
\]

For a shell vertex \(b\), write \(T_b=N_H(b)\cap H_0\). In the regular B-row regimes, \(|T_b|\le t_b\le3\).

## 2. Theorem

> **Robust zero-excess independent-four theorem.**
>
> - If \(e(H)=284\), then for every \(T\subseteq V(H_0)\) with \(|T|\le6\), \(\alpha(H_0-T)=4\).
> - If \(e(H)=285\), then for every \(T\subseteq V(H_0)\) with \(|T|\le4\), \(\alpha(H_0-T)=4\).

In particular, after deleting the full set of high-excess vertices, an independent 4-set remains after any allowed further deletion. All four vertices in that independent set have \(d_H=12\).

### Proof

The total excess is \(E\in\{4,6\}\), so \(1\le k\le E\), and
\[
\sum_{x\in X}d_H(x)=12k+E.
\]
Using \(e(H_0)=e(H)-e(H[X])-e_H(X,H_0)=e(H)-\sum_{x\in X}d_H(x)+e(H[X])\), we obtain
\[
e(H_0)\le 282-\frac E2-12k+\binom{k}{2}. \tag{1}
\]

Each \(v\in H_0\) has degree 12 in \(H\) and at most \(k\) neighbours in \(X\), hence \(d_{H_0}(v)\ge12-k\). For \(T\subseteq H_0\), \(|T|=t\), the number of edges deleted by removing \(T\) is
\[
e_{H_0}(T,H_0-T)+e(H_0[T])
=\sum_{v\in T}d_{H_0}(v)-e(H_0[T])
\ge t(12-k)-\binom t2.
\]
Together with (1),
\[
e(H_0-T)\le
U(E,k,t):=
282-\frac E2-12k+\binom{k}{2}
-t(12-k)+\binom t2. \tag{2}
\]

If \(\alpha(H_0-T)\le3\), then the complement is \(K_4\)-free. Turán's theorem gives
\[
e(H_0-T)\ge p_3(n),\qquad n=47-k-t,
\]
where
\[
p_3(n)=\binom n2-t_3(n)
=\sum_{j=1}^{3}\binom{n_j}{2}
\]
and the \(n_j\)'s are the three balanced part sizes (differing by at most one).

For the relevant \(k,t\), the gap \(p_3(47-k-t)-U(E,k,t)\) decreases as \(t\) increases: reducing \(n\) by one lowers \(p_3(n)\) by \(\lfloor(n-1)/3\rfloor\ge12\), whereas \(U(E,k,t)\) decreases by only \(12-k-t\le11\) per step. Thus the smallest gap occurs at the largest allowed \(t\).

The exact endpoint checks are:

| Core edges | \(E\) | \(k\) | \(t_{\max}\) | \(n=47-k-t_{\max}\) | \(p_3(n)\) | \(U(E,k,t_{\max})\) | Gap |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 284 | 4 | 1 | 6 | 40 | 247 | 217 | 30 |
| 284 | 4 | 2 | 6 | 39 | 234 | 212 | 22 |
| 284 | 4 | 3 | 6 | 38 | 222 | 208 | 14 |
| 284 | 4 | 4 | 6 | 37 | 210 | 205 | 5 |
| 285 | 6 | 1 | 4 | 42 | 273 | 229 | 44 |
| 285 | 6 | 2 | 4 | 41 | 260 | 222 | 38 |
| 285 | 6 | 3 | 4 | 40 | 247 | 216 | 31 |
| 285 | 6 | 4 | 4 | 39 | 234 | 211 | 23 |
| 285 | 6 | 5 | 4 | 38 | 222 | 207 | 15 |
| 285 | 6 | 6 | 4 | 37 | 210 | 204 | 6 |

Every gap is strictly positive. This contradicts \(\alpha(H_0-T)\le3\). Since \(\alpha(H_0-T)\le\alpha(H)\le4\), equality \(\alpha(H_0-T)=4\) follows. \(\square\)

## 3. Consequences for shell-row witnesses

### 3.1 One regular row

If \(t_b\le3\), then \(|T_b|\le3\). Applying the theorem with \(T=T_b\) gives an independent set
\[
Q_b\subseteq H_0\setminus T_b,\qquad |Q_b|=4.
\]
Thus \(Q_b\) is anticomplete to \(b\), independent in \(H\), and all four of its vertices have core degree exactly 12.

For each \(x\in Q_b\), the parent minimum-degree condition gives \(d_F(x,A)\ge1\). The existing universal shell-support theorem further gives that \(Q_b\) hits at least three distinct shell rows.

This applies to every regular B row in E407 Q32 and to every regular B row with \(t_b\le3\) in E408 Q32/Q33. It is an existence statement; it does **not** assert that a chosen \(Q_b\) is the particular K5-component witness in a non-target color.

### 3.2 Common witness for two regular rows in a 284-edge core

Suppose \(e(H)=284\) and \(b,c\) satisfy \(t_b,t_c\le3\). Then
\[
|T_b\cup T_c|\le6.
\]
The theorem applied to \(T=T_b\cup T_c\) yields an independent 4-set
\[
Q_{bc}\subseteq H_0\setminus(T_b\cup T_c)
\]
anticomplete to both \(b\) and \(c\).

Therefore every pair of regular B labels in E407 Q32 and every pair of regular B labels in E408 Q33 has a common zero-excess independent-four witness. The set \(Q_{bc}\) need not equal either of the individual witnesses \(Q_b,Q_c\).

For the 285-edge E408 Q32 core, the same conclusion follows whenever the actual union \(T_b\cup T_c\) has size at most four. The theorem does not imply it for every pair with only the separate bounds \(t_b,t_c\le3\).

### 3.3 Template A/C excess identity

For a zero-excess witness \(Q\subseteq H_0\), every vertex has \(d_H(x)=12\), so
\[
\sum_{x\in Q}(d_F(x)-13)
=\sum_{x\in Q}(d_F(x,A)-1)
=d_F(Q,A)-4. \tag{3}
\]
In E407 templates A/C, the retained row-count constraints imply that if \(Q\) misses any of the three hubs, then \(Q\) hits at least six B rows. Hence \(d_F(Q,A)\ge6\), and (3) gives
\[
\sum_{x\in Q}(d_F(x)-13)\ge2.
\]
This is a valid local cost for a non-hub-complete zero-excess witness. It must not be summed over overlapping witnesses without an explicit multiplicity argument.

## 4. Exact-129 color-component corollary for the 284-edge core

Assume the retained exact-129 factor theorem for a non-target color \(C\): its 61-point restriction has ten isolated K5 components and an 11-point exceptional gadget \(U\) with \(\alpha(C[U])=2\). In E407 Q32 and E408 Q33, \(e(H)=284\), so \(|X|\le4\).

The B set is a target clique and therefore independent in every non-target color. Thus \(|B\cap U|\le2\), and at least eight B vertices lie in isolated K5 components. No such component can contain two B vertices, since every pair in a K5 is C-colored but every pair of B vertices is target-colored. At most three components can contain an S vertex. Therefore at least five isolated K5 components have the form
\[
\{b\}\cup Q,\qquad b\in B,\quad Q\subset H,\quad |Q|=4.
\]
These five components are vertex-disjoint within color \(C\). At most four can contain a high-excess core vertex because \(|X|\le4\). Consequently **at least one of the five is a zero-excess witness**, with \(Q\subseteq H_0\).

The non-target edge excess over 129 is four in E407 (\(1830-407-11\cdot129=4\)), so there are at least seven exact-129 colors. In E408 the excess is three, so there are at least eight. Under the retained exact-129 factor theorem, this yields:
- E407 Q32: at least seven zero-excess K5-component witnesses across seven exact-129 colors;
- E408 Q33: at least eight zero-excess K5-component witnesses across eight exact-129 colors.

Across different colors, these K5 components still intersect in at most one vertex by unique edge ownership. This is conditional on the cited exact-129 factor theorem and does not apply automatically to E408 Q32, whose core has excess six.

## 5. What this does not close

The new theorem improves the witness supply but does not itself contradict E407 Q32 or E408 Q33:

- the common witness \(Q_{bc}\) is not necessarily a monochromatic K5 component;
- distinct witnesses may overlap in one, two, or three core vertices unless they are actual K5 components of different colors;
- the local cost in (3) can be reused by overlapping witnesses;
- no bound has yet been proved on the total multiplicity of shell-core edges across all witness sets;
- E408 Q32 has excess six and needs its separate four-deletion threshold.

The next mathematical target is to combine the common-witness property with the actual color-component packing, then classify overlaps of the 4-sets while charging each core vertex and each shell-core edge only once. No E407/E408 terminal exclusion is claimed here.
