# E406 d11 shell: forcing a second q31 maximum

Status: `PROVED` under the exact d11 shell theorem in `E406_D11_EXACT_SHELL.md`. `E406` remains `OPEN`.

Retain the exact d11 q30->q31 shell from that file. Thus

- p is q30;
- y is q31;
- S is the common 11-point missing side of y in the p-shell;
- T is the unique other shell vertex;
- y and T are target-adjacent;
- both y and T are target-anticomplete to S;
- `M[S]=K1,m + (10-m)K1`, `4<=m<=8`;
- the only p-shell decoration is `8-m` at the S-star centre;
- `D=N_C(y)` is an 11-row and `e_R(S,D)=0`;
- `E=N_C(T)` is another 11-row.

## 1. T has q-value 30 or31

A direct core exchange for the T-repivot gives

`q_T = 22 + m_E + epsilon_E + e_R(S,E)`,

where

- `m_E=C(11,2)-e_C(E)`;
- `epsilon_E=sum_{u in E}(d_C(u)-12)`.

The E406 ceiling gives `q_T<=31`.

The 11-block complement-edge inequality applied to E gives

`m_E+epsilon_E>=8`.

Hence

`8 <= m_E+epsilon_E <= 9-e_R(S,E)`

and therefore

`e_R(S,E)<=1`,
`q_T in {30,31}`.

## 2. The two 11-rows have overlap at most1

Put `k=|D intersect E|`.

Both D and E induce at least46 target edges: D has complement size at most9, and the inequality above gives the same lower edge floor for E.

In the induced set

`U=(D union E) union {y,T}`

we have at least

`e(D)+e(E)-C(k,2)+23`

edges. The final `23` is exact: y sends11 edges to D, T sends11 to E, and yT is an edge.

If k=10, then `|U|=14` and

`e(U)>=46+46-45+23=70>D(14)=69`.

If k=9, then `|U|=15` and

`e(U)>=46+46-36+23=79>D(15)=72`.

If k=8, then `|U|=16` and

`e(U)>=46+46-28+23=87>D(16)=76`.

Hence no overlap8,9,10 is possible.

Since the y--T distance in a degree-13 pivot shell is `11-k`, and both endpoint shells satisfy the q30/q31 extreme-degree restriction, the only remaining plateau/boundary possibilities have

`k in {0,1}`.

Therefore

`|D intersect E|<=1`.      (ROW-SEPARATION)

## 3. q_T=30 is impossible

Assume q_T=30.

Then the adjacent edge `T -> y` is another q30->q31 final rise. By ROW-SEPARATION its distance is11, so the exact d11 theorem applies again, now in the T-view.

In that view the 11-point shell side exchanged by the T->y move is E, while the support row of y is D. The zero-slack conclusion of `E406_D11_EXACT_SHELL.md` therefore gives

`e_R(D,E)=0`.      (A)

On the other hand, `q_T=30` in the formula of Section 1 means

`m_E+epsilon_E+e_R(S,E)=8`.

But the 11-block inequality already gives `m_E+epsilon_E>=8`; hence

`e_R(S,E)=0`,
`m_E+epsilon_E=8`.      (B)

The original d11 theorem already gives

`e_R(S,D)=0`.      (C)

Now each of the three 11-point target graphs R[S], C[D], C[E] has at least one internal nonedge:

- S has the complement star K1,m with m>=4;
- D cannot be K11 because y together with D would form a K12;
- E cannot be K11 because T together with E would form a K12.

Choose an independent pair in each of S,D,E. By (A)--(C), all cross pairs between the three chosen pairs are also target-nonedges. The six selected vertices form an independent6-set in the T61 parent, contradicting `alpha<=5`.

Therefore

`q_T !=30`.

Combining with Section 1:

`q_T=31`.      (SECOND-MAX)

## 4. Current d11 terminal

Every d11 q30->q31 final rise forces the following multipivot configuration:

- one q30 pivot p;
- two adjacent q31 pivots y,T;
- a common 11-point shell side S anticomplete to both y and T;
- `M[S]=K1,m+(10-m)K1`, `4<=m<=8`;
- two 11-row supports D,E with `|D intersect E|<=1`;
- `e_R(S,D)=0` and `e_R(S,E)<=1`;
- y,T are both global q-max pivots.

Thus d11 is no longer a one-edge final-rise problem. It has been converted into a rigid three-pivot compatibility problem with two almost-disjoint dense 11-row supports.