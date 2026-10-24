# E407 Q32 terminal — proof and dependency ledger

Date: 2026-10-25  
Status: **E407 Q32 OPEN / NOT_CERTIFIED.**

## 1. Dependency chain currently supported

1. **T61 shell reduction** (inherited, conditional on the registered V12 retained-seed contract) gives a 61-vertex residual, pivot, shell, and 47-point core.
2. **Exact-129 factor theorem** (inherited Kang–Pikhurko equality-classification contract) gives seven disjoint independent 4-set witnesses per exact-129 color on the minimum-support boundary.
3. **Linearity** follows because two witnesses sharing two core vertices would assign their common edge two non-target colors; within a color the selected K5 components are disjoint.
4. **Support boundary** gives \(|U|=29, |W|=18\) in the unresolved \(129^7,130^4\) profile.
5. **Exact core ledger** gives
   \[
   e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,\quad e(H[W])=48-\epsilon_U-\delta.
   \]
6. **Sibling transversal/excess theorem** gives \(\epsilon_U+2\delta\ge9\) and \(\delta\ge3\), under the same boundary contract.
7. **This line's theorem**: if \(\delta=16\), Brouwer's second-Turán bound forces \(L=\overline{H[U]}\) four-partite; equality and degree accounting force the unique \(\delta=16\) structural kernel in FOUR_PARTITE_TERMINAL.md.
8. **Reverse saturation**: under the resulting (K_5cup K_5cup K_4cup K_4) structure, every (win W) is adjacent to all vertices of exactly one (U)-part. This is proved before the endpoint split and is not assumed as an input.

## 2. Exact external/input dependencies

- The V12 finite certificate is COMPUTATION_CERTIFIED / independently replayed, not an analytic proof of every screen rule and not a completed-core certificate.
- The exact-129 K5-component structure is conditional on the registered constrained second-Turán/Kang–Pikhurko classification. This line does not reprove that extremal theorem.
- Brouwer's second-Turán bounds are used with the exact \(K_5\)-free/non-four-partite hypotheses stated at each application.
- The arithmetic verifier checks edge ledgers, integer part-size profiles, and the finite endpoint-split inequalities only. It is not a graph-realization certificate and does not independently verify the combinatorial lemmas.

## 3. Open edges in the proof DAG

\[
\begin{aligned}
&\text{Original }K_{145}\text{ counterexample}\\
&\Downarrow\ \text{T61 reduction + retained lower-order inputs}\\
&\text{E407 Q32 shell template A/B/C/D/E}\\
&\Downarrow\ \text{49 linear independent }K_4\text{ witnesses}\\
&|U|=29,\ |W|=18,\ 3\le\delta\le16\\
&\Downarrow\\
&\begin{cases}
\delta\le15:\ \text{non-four-partite or near-Turán four-partite cases OPEN},\\
\delta=16:\ \text{forced }(7,7,7,8)\text{ / }K_5,K_5,K_4,K_4\text{ kernel OPEN}.
\end{cases}\\
&\Downarrow\ \text{missing template-to-core incompatibility theorem}\\
&\text{E407 Q32 excluded}\quad\text{(NOT YET PROVED).}
\end{aligned}
\]

There is no circular dependency in the new \(\delta=16\) reduction: it uses only the E407 core contract, the 49-block linearity, the exact ledger, Turán/Brouwer bounds, and \(\alpha(H)\le4\). The proof still depends on the upstream validity of the 49-witness boundary.
