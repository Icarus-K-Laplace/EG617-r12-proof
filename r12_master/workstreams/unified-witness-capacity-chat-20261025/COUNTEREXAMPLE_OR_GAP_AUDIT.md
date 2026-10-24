# Counterexample / gap audit for the unified witness-capacity route

Date: 2026-10-25  
Status: **No graph counterexample found or claimed.** The integer relaxations below show that the present scalar ledgers are mutually consistent; they are not graph-realization certificates.

## 1. The edge-ownership identity is correct but not yet sharp enough

For \(N=7c\) linear independent four-sets, the exact crossing load is
\[
\sum_{xy\in E(H[U])}r_xr_y
=\sum_{i<j}e_H(Q_i\setminus Q_j,Q_j\setminus Q_i)
\ge4\binom N2-\sum_x\binom{r_x}{2}.
\]
At the two support boundaries, the lower bounds are 4122 (E407) and 5412 (E408 Q33) after the omission-capacity refinements. A valid generic upper bound is
\[
\sum_{xy\in E(H[U])}r_xr_y\le c^2e(H[U]).
\]
The current ledgers allow \(e(H[U])=112-\delta\) for E407 and \(129-\delta\) for E408 Q33; these upper bounds remain above the crossing lower bounds. Therefore the crossing inequality alone does not close either terminal.

## 2. Explicit integer omission relaxations that survive

### E407 Q32, \(S=\epsilon_U+2\delta=9\)

Take omission multiplicities
\[
(o_x)=(4,2,1,0^{26}).
\]
They sum to 7, each is at most 6, and \(\Omega=\sum_x\binom{o_x}{2}=6+1=7\). Hence \(r_x=7-o_x\) sums to 196 and the support has 29 points. The row-degree lower bound is
\[
5n_0+2n_1=5\cdot26+2=132\le e_H(U,W)=124+9=133.
\]
Choose the scalar core ledger \(\epsilon_U=3,\delta=3\): then \(\epsilon_U+2\delta=9\), \(\epsilon_U+\delta=6\le16\), \(e(H[U])=109\), \(e_H(U,W)=133\), and \(e(H[W])=42\ge p_4(18)=32\). The capacity bound is \(e(\overline{H[U]})=297\le307=310-\epsilon_U\). All stated scalar inequalities are consistent.

### E408 Q33, \(S_0=\epsilon_U+2\delta=12\)

Take
\[
(o_x)=(6,2,2,2,2,2,2,2,2,2,0^{21}).
\]
These 31 values sum to 24, with \(\Omega=15+9=24\). Thus \(r_x=8-o_x\) sums to 224. The row-degree lower bound is
\[
6n_0+3n_1=6\cdot21=126=e_H(U,W)=114+12.
\]
Choose \(\epsilon_U=4,\delta=4\): then \(S_0=12\), \(\epsilon_U+\delta=8\le17\), \(e(H[U])=125\), \(e_H(U,W)=126\), and \(e(H[W])=33\ge p_4(16)=24\). Also \(e(\overline{H[U]})=340\le349=353-\epsilon_U\). All scalar ledgers and the new omission-capacity inequality are consistent.

These profiles do **not** specify the 4-uniform witness blocks, the graph \(H\), shell rows, or color assignments. They are not counterexamples to EG617 and do not show that the terminal exists. They establish only that further work must use incidence geometry or labelled row structure, not these scalar inequalities alone.

## 3. Label-count relaxation is also feasible

For E408, the new pivot-label capacity forces at least 49 B-labelled witnesses among 56 selected witnesses. A 0–1 label-incidence matrix can have row sums \((7,6,6,6,6,6,6,6)\) and column sums
\[
(6,6,5,5,5,5,4,4,5,4),
\]
so each color uses six or seven distinct B labels, every label occurs at most seven times, and the total is 49. This meets the known label-count capacities. It does not construct witness blocks with the required intersections.

## 4. Exact missing proposition

The zero-excess theorem proves that every pair of regular B rows has some common independent four-set avoiding both rows. It does not make that set a component of any exact-129 non-target color. The exact-129 factor theorem certifies only its own monochromatic components.

A complete unified contradiction needs at least one of the following new results:

1. **Label-transfer/component-realization lemma:** a common zero-excess independent four-set for specified regular rows can be assigned to an exact-129 color component while preserving edge ownership; or
2. **Hub-capacity theorem:** an upper bound on the number of distinct shell rows/hubs that can be hit by the labelled zero-excess witnesses, counting each shell-core edge and each core vertex only once; or
3. **Incidence-design exclusion:** prove that the omission profiles and same-label disjointness constraints cannot be realized by a linear 4-uniform family whose blocks are transversals of every core vertex in \(W\).

No such proposition is established in this workstream yet. The smallest failure is the label-transfer gap: the graph-theoretic witness is unlabelled, while the colour-unique edge-ownership argument applies only to actual monochromatic \(K_5\) components.
