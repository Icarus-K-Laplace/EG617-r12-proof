# Exact W-profile classification for \(\delta=14,\epsilon_U=1\)

Date: 2026-10-25  
Status: **PROVED_CONDITIONAL** on Brouwer's second-Turán theorem, with its \(K_5\)-free/non-four-partite hypotheses as stated below.

## 1. Contract

Let \(W\) have 18 vertices, \(\alpha(H[W])\le4\), and \(e(H[W])=33\). Let \(G=\overline{H[W]}\). Then \(G\) is \(K_5\)-free and
\[
e(G)=\binom{18}{2}-33=153-33=120.
\]
The Turán number is \(t_4(18)=121\), attained by the complete 4-partite graph with part sizes \((4,4,5,5)\).

## 2. Brouwer forces four-partiteness

Brouwer's second-Turán bound says that a \(K_5\)-free graph on \(n\) vertices that is not 4-partite has at most
\[
t_4(n)-\lfloor n/4\rfloor+1
\]
edges. At \(n=18\), this upper bound is
\[
121-\lfloor18/4\rfloor+1=121-4+1=118.
\]
Since \(e(G)=120>118\), \(G\) must be 4-partite. This is a direct application with the required \(K_5\)-free and non-four-partite hypotheses; no equality-case theorem beyond Brouwer's bound is used.

## 3. Enumerate the four-part sizes

Let \(a\le b\le c\le d\) be the part sizes of a 4-partition of \(G\), with \(a+b+c+d=18\). The complete 4-partite graph on these parts has
\[
\binom{18}{2}-\sum_{s\in\{a,b,c,d\}}\binom{s}{2}
\]
edges. It contains \(G\), so its edge count is at least 120; Turán's theorem says it is at most 121. Therefore
\[
\sum_s\binom{s}{2}\in\{32,33\}.
\]
The sorted positive integer partitions of 18 into four parts with these sums are exactly
\[
\begin{array}{c|c}
\sum_s\binom{s}{2}&(a,b,c,d)\\\hline
32&(4,4,5,5)\\
33&(3,5,5,5),\ (4,4,4,6).
\end{array}
\]

If the sum is 33, the complete 4-partite graph already has 120 edges, so \(G\) equals it. Taking complements, \(H[W]\) is respectively \(K_3\dot\cup K_5^3\) or \(K_4^3\dot\cup K_6\), with no W-cross-edge.

If the sum is 32, the complete 4-partite graph has 121 edges and \(G\) has 120, so exactly one cross-part edge is missing from \(G\). Its complement \(H[W]\) is \(K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5\) plus exactly one edge between two clique parts.

Therefore the three profiles handled by the three E407 \(\epsilon_U=1\) terminal theorems exhaust all possibilities under the stated contract.
