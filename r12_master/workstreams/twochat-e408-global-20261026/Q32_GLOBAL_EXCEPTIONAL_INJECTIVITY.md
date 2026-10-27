# E408 Q32: global injectivity of exact-color exceptional vertices

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL** under the E408 Q32 residual contract and exact-129 Type-I classification.

## Theorem

Let \(m\in\{8,9,10\}\) be the number of exact-129 non-target colors on the 61-point residual \(R\). For each exact color \(C\), let \(x_C\) be the exceptional vertex of its KP Type-I factor. Then
\[
\boxed{x_C\ne x_D\quad\text{for distinct exact colors }C,D.}
\]
Equivalently, every residual vertex is exceptional for at most one exact-129 color.

## Proof

For a residual vertex \(v\), let \(n_v\) be the number of exact colors for which \(v=x_C\).

Every exact Type-I color has degree at least four at every residual vertex: ordinary vertices lie in a \(K_5\), while the exceptional vertex has degree nine. Hence the sum of exact-color degrees at \(v\) is at least
\[
4m+5n_v.\tag{1}
\]

For a nonexact color with residual edge count \(129+s\), the deletion-Turan argument gives minimum degree two for \(s=1\), and minimum degree one for \(s=2,3\). Since the positive nonexact excesses sum to three, the combined nonexact degree at every vertex is at least
\[
B_m=
\begin{cases}
6,&m=8,\\
3,&m=9,\\
1,&m=10.
\end{cases}\tag{2}
\]

The target residual graph has minimum degree thirteen. Since all twelve colors partition the 60 edges incident to \(v\),
\[
60\ge13+4m+5n_v+B_m.
\]
Thus
\[
5n_v\le
\begin{cases}
9,&m=8,\\
8,&m=9,\\
6,&m=10,
\end{cases}
\]
and therefore \(n_v\le1\) in every case.

## Consequences

1. The \(m\) exact-color exceptional vertices occupy \(m\) distinct vertices of the 61-point residual.
2. Any terminal that forces more than \(|X|\) exact exceptional vertices into a set \(X\subset R\) of size \(|X|\) is impossible.
3. The v=44 triple-pair terminal forces at least \(m-3\ge5\) exceptional vertices into its three-point complement \(W\), so injectivity immediately closes v=44.
4. For v=45,46,47 this theorem remains a load-bearing constraint, but those support sizes do not currently force enough exceptional vertices into the small complement; further structure is needed.

No Q33 284-edge identity is used.