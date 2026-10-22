# E406 d11 terminal: three star-complement blocks

Status: `PROVED` under `E406_D11_EXACT_SHELL.md` and `E406_D11_TWO_MAXIMA.md`. `E406` remains `OPEN`.

The d11 terminal has a q30 pivot p and two adjacent q31 pivots y,T. Let

- S be the common 11-point shell side anticomplete to y and T;
- D=N_C(y);
- E=N_C(T).

Previous results give

- `overline{R[S]} = K1,m_S + isolates`, `4<=m_S<=8`;
- `e_R(S,D)=0`;
- `e_R(S,E)<=1`;
- `|D intersect E|<=1`;
- `q_T=31`.

This note proves that the complement graphs on D and E are stars as well.

## 1. A general 11-block star lemma

Let X be an 11-vertex subset of a 47-core of minimum degree at least12. Put

- `K=overline{R[X]}`;
- `m=e(K)>0`;
- `rho_v=d_K(v)`;
- `epsilon_v=d_core(v)-12`;
- `epsilon_X=sum epsilon_v`.

Suppose every K-edge uv satisfies

`rho_u+rho_v+epsilon_u+epsilon_v>=9`.      (1)

### Case A: m+epsilon_X=9

If K contained two disjoint edges, the sum of `rho+epsilon` over their four endpoints would be at least18.

But over all eleven vertices

`sum_v(rho_v+epsilon_v)=2m+epsilon_X=m+9`.

For `m<=8` this is at most17, contradiction.

For `m=9`, equality would force all augmented weight onto those four endpoints. Here `epsilon_X=0`, so all graph degree lies on four vertices; nine edges cannot be supported on four vertices. Contradiction.

Hence K has matching number1. Such a simple graph is a star or a triangle.

The triangle alternative has `m=3`, `epsilon_X=6`. Since every triangle vertex has rho=2, (1) gives `epsilon_u+epsilon_v>=5` on all three edges. Summing gives `2 epsilon_X>=15`, i.e. `12>=15`, impossible.

Therefore K is a star.

### Case B: m+epsilon_X=8

The same two-disjoint-edge argument is even stronger, since

`sum(rho+epsilon)=m+8<18`.

Again K has matching number1. The triangle alternative has `m=3`, `epsilon_X=5`; summing the three edge inequalities gives `2 epsilon_X>=15`, i.e. `10>=15`, impossible.

Therefore K is a star here as well.

## 2. Apply the lemma to D

The exact d11 zero-slack identity gives

`m_D+epsilon_D=9`.

The core nonedge codegree bound gives (1) for every complement edge of D.

Therefore

`overline{C[D]} = K1,m_D + (10-m_D)K1`.

Since `epsilon_D<=6`, necessarily `3<=m_D<=9`.

## 3. Apply the lemma to E

Since `q_T=31`, the second-row formula gives

`m_E+epsilon_E+e_R(S,E)=9`,

with `e_R(S,E)<=1`.

If `e_R(S,E)=0`, then `m_E+epsilon_E=9` and Case A applies.

If `e_R(S,E)=1`, then `m_E+epsilon_E=8` and Case B applies.

Hence in either case

`overline{C[E]} = K1,m_E + (10-m_E)K1`.

## 4. Three-star-block normal form

Every surviving d11 final-rise state therefore has three 11-point near-cliques whose missing graphs are stars:

- S-star, with `4<=m_S<=8`;
- D-star, with `3<=m_D<=9`;
- E-star, with its size determined by `m_E+epsilon_E=8` or9.

The cross data are already tiny:

- `e(S,D)=0`;
- `e(S,E)<=1`;
- `|D intersect E|<=1`.

Thus the remaining d11 task is no longer graph classification. It is a finite compatibility theorem for three star-defect K11 blocks coupled to the two q31 pivot views.