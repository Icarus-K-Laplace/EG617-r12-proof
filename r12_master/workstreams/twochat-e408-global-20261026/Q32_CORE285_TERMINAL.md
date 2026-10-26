# E408 Q32 — independent 285-edge terminal

Updated: 2026-10-26  
Status: **OPEN / NOT_CERTIFIED**. This is the separate Q32 contract; no Q33 theorem is imported.

## 1. Frozen contract

\[
|V(H)|=47,\quad e(H)=285,\quad \alpha(H)\le4,\quad\delta(H)\ge12,
\quad\sum_{x\in H}(d_H(x)-12)=6.
\]
The shell parameter is \(q=32\), equivalently \(e(M)+G_A=32\). Under the registered seven-block equality and exact-129 Type-I factorization, the number \(m\) of exact-129 colors is 8, 9, or 10.

## 2. Retained strict reduction

The read-only Q32 workstream proves \(|U|\ge44\) for the union \(U\) of all ten-or-eleven exact-color four-set witnesses, uniformly over both \(M[B]=\varnothing\) and \(M[B]\ne\varnothing\) shell branches. Its capacity inequality is
\[
6N\le \binom v2-p_4(47-v)-12v+285-E_U,
\]
with total core excess six. This 285 constant and excess budget must be retained.

At \(v=44\), \(W=H\setminus U\) has three vertices. If \(O_C=U\setminus Q_C\) is the four-point omission set for an exact color \(C\), the two double-shell core triples and exceptional vertex \(x_C\) partition
\[
W\dot\cup O_C=T_{C,1}\dot\cup T_{C,2}\dot\cup\{x_C\}.
\]
Pair uniqueness says the pairs of \(W\)-vertices used within triples are globally edge-disjoint. Since \(W\) has only three pairs, at most three exact colors can have \(x_C\in O_C\). At least \(m-3\) colors have \(x_C\in W\), and for each such color the two triples split the other two vertices of \(W\), one per triple.

This is the exact remaining normal form, not a contradiction.

## 3. Required next attack

Do not stop at the scalar pair budget. Couple the \(v=44\) terminal to:
- the six-unit excess ledger on the 44-point support and three-point complement;
- the exact omission multiplicities \(O_C\) and exceptional vertices \(x_C\);
- the outer seven-block blocker labels and \(P_C+R_C+s_C=62\);
- the component triples' cross-color linearity.

For every exact color with \(x_C\in W\), each of the two triples contains one \(W\)-vertex and two points of \(O_C\). Across colors, a pair of vertices cannot be repeated in two triples. The next proof target is an incidence theorem that forces a repeated pair, forces an impossible degree/excess allocation, or creates a double-star violation in the outer blocks.

## 4. Scope firewall

The source workstream is workstream/r12-e408-q32-excess6-20261025 at HEAD a0ba6db26c7e8b00a4217dcbcbf298895dff93ce. Its theorem and verifier are read-only dependencies. The Q33 284-edge / excess-four support-41 theorem cannot be applied to this Q32 terminal. The original K145-to-T61 bridge and EG617(r=12) remain OPEN / NOT_CERTIFIED.
