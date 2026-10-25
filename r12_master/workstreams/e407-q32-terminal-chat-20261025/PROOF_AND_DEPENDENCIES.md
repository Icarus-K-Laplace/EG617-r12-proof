# E407 Q32 terminal — proof and dependency ledger

Date: 2026-10-25  
Status: **E407 Q32 OPEN / NOT_CERTIFIED; the \(\delta=16\) branch is excluded under the retained core/witness contract.**

## 1. Dependency chain currently supported

1. **T61 shell reduction** (inherited, conditional on the registered V12 retained-seed contract) gives a 61-vertex residual, pivot, shell, and 47-point core.
2. **Exact-129 factor theorem** (inherited Kang–Pikhurko equality-classification contract) gives seven disjoint independent 4-set witnesses per exact-129 color on the minimum-support boundary.
3. **Linearity** follows because two witnesses sharing two core vertices would assign their common edge two non-target colors; within a color, selected \(K_5\) components are disjoint.
4. **Support boundary** gives \(|U|=29, |W|=18\) in the unresolved \(129^7,130^4\) profile.
5. **Exact core ledger** gives
   \[
   e(H[U])=112-\delta,\quad e_H(U,W)=124+\epsilon_U+2\delta,\quad e(H[W])=48-\epsilon_U-\delta.
   \]
6. **Sibling transversal/excess theorem** gives \(\epsilon_U+2\delta\ge9\) and \(\delta\ge3\), under the same boundary contract.
7. **Four-partite reduction at \(\delta=16\)**: \(L=\overline{H[U]}\) has 310 edges, exceeding the non-four-partite Brouwer threshold 309, so it is four-partite. The 49 linear witnesses force \(U\)-part sizes \(7,7,7,8\); the exact ledger forces \(H[W]=K_5\cup K_5\cup K_4\cup K_4\).
8. **Reverse saturation**: under this structure, every \(w\in W\) is adjacent to all vertices of exactly one \(U\)-part. This is proved from \(\alpha(H)\le4\), the matching structure of the five \(U\)-cross-edges, and the total excess budget.
9. **Endpoint-split terminal exclusion**: the (4+1) and (3+2) allocations contradict the four-unit excess budget. In the (5+0) allocation, the endpoint (K_4) is forced complete to the 8-part, yielding a forbidden (K_{12}). Thus (delta=16) is excluded.

## 2. Exact external/input dependencies

- The V12 finite certificate is COMPUTATION_CERTIFIED / independently replayed, not an analytic proof of every screen rule and not a completed-core certificate.
- The exact-129 \(K_5\)-component structure is conditional on the registered constrained second-Turán/Kang–Pikhurko classification. This line does not reprove that extremal theorem.
- Brouwer's second-Turán bounds are used with the exact \(K_5\)-free/non-four-partite hypotheses stated at each application.
- The arithmetic verifier checks exact ledgers, partition profiles, and excess inequalities only. It is not a graph-realization certificate and does not independently verify the combinatorial lemmas.

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
\delta=16:\ \text{excluded by endpoint-split excess + forbidden }K_{12},\\
\delta=15,\ L\text{ non-four-partite}:\ \text{excluded by KP equality + incompatible }x,y\text{ degrees into }W,\\
\delta=15,\ L\text{ four-partite}:\ \text{only }H[W]=K_3\cup K_5^3\text{ remains, with }D\cup K_3=K_{11};\text{ shell compatibility OPEN},\\
\delta\le14:\ \text{four-partite and non-four-partite cases OPEN}.
\end{cases}\\
&\Downarrow\ \text{missing template-to-core incompatibility theorem for }\delta\le15\\
&\text{E407 Q32 excluded}\quad\text{(NOT YET PROVED).}
\end{aligned}
\]

There is no circular dependency in the \(\delta=16\) exclusion: it uses only the E407 core contract, 49-block linearity, the exact ledger, Turán/Brouwer bounds, \(\alpha(H)\le4\), and \(\omega(H)\le11\). The \(\delta=15\) non-four-partite exclusion additionally depends on the Kang–Pikhurko equality classification and W-side Brouwer bound. All remaining cases depend on the upstream validity of the 49-witness boundary.
