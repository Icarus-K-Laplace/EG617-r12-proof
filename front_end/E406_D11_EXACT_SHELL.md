# E406 distance-11 final rise: exact zero-slack shell

Status: `PROVED` for the reduction below. `E406` remains `OPEN`.

This file refines Section 8 of `E406_FINAL_RISE_NORMAL_FORMS.md` and corrects one harmless off-by-one in the prose derivation there: for a missing edge inside an 11-set, the number of common target neighbours inside that 11-set is at least `11-rho_u-rho_v`, not `12-rho_u-rho_v`. The final edge inequality used there, `rho_u+rho_v+epsilon_u+epsilon_v>=9`, is the correct one.

Assume a q30->q31 final-rise edge of distance d=11. Let S be the 11-point missing neighbourhood of the new pivot y, D its 11-row in the old 285-edge core C, and T the unique old-shell vertex outside `S union {y}`.

Write

`h=g_T+e_R(S,D)`.

The exact final-rise identities give

`e_C(D)=46+epsilon_D+h`,

so if `K_D=overline{C[D]}` and `m_D=e(K_D)`, then

`m_D=9-(epsilon_D+h)`.

For every edge uv of K_D, with K_D-degrees rho_u,rho_v, the old-core nonedge codegree bound gives

`rho_u+rho_v+epsilon_u+epsilon_v>=9`.      (1)

Summing (1) gives `m_D+epsilon_D>=8`, hence `h<=1`.

## 1. The h=1 branch is impossible

Let `epsilon'_S` be the total excess of the inserted S vertices in the new 284-edge core C'. The exact exchange equation gives

`e_R(S)=47+h+epsilon'_S`.

Hence if `K_S=overline{R[S]}` and `m_S=e(K_S)`,

`m_S=8-h-epsilon'_S`.

Apply the same 11-block argument inside the new core C'. For a K_S-edge uv, the common target neighbours of u,v inside S are at least

`11-rho_u-rho_v`.

The core nonedge codegree bound is at most `2+epsilon'_u+epsilon'_v`, so again

`rho_u+rho_v+epsilon'_u+epsilon'_v>=9`.

Summing over K_S gives

`m_S+epsilon'_S>=8`.

But the exact formula above says

`m_S+epsilon'_S=8-h`.

Therefore `h=0`.

Thus the entire h=1 branch is empty, and necessarily

`g_T=0`,
`e_R(S,D)=0`.      (2)

## 2. The S-block complement is an exact star

With h=0,

`m_S+epsilon'_S=8`,

so every inequality in the summed 11-block argument is equality.

For every K_S-edge uv,

`rho_u+rho_v=m_S+1`,

and all new-core excess is supported on vertices of K_S-degree m_S. Hence K_S has matching number1. Since `epsilon'_S<=4`, we have `m_S>=4`, so the triangle alternative is impossible. Therefore

`K_S = K_{1,m} disjoint_union (10-m)K1`,

for some

`4<=m<=8`,

and

`epsilon'_S=8-m`.

All new-core excess on S is concentrated at the star centre.

## 3. Exact old row weights of the eleven S vertices

In C', the star centre has internal S-degree `10-m` and core excess `8-m`, hence total new-core degree `20-m`. Its old row into `C-D` therefore has size

`10`.

Each of the m star leaves has internal S-degree9 and zero excess, hence old row weight

`3`.

Each of the `10-m` K_S-isolates has internal S-degree10 and zero excess, hence old row weight

`2`.

So the old S-row multiset is exactly

`10, 3^m, 2^(10-m)`.      (3)

## 4. The last shell vertex T must miss all of S

By (2), T is undecorated, hence it is a legal degree-13 repivot. Put

`x=d_M(T)=|N_M(T) intersect S|`.

The q30 extreme-degree theorem gives

`x in {0,1,2,3,10,11}`.

If `x=1`, a missing edge from T to an S-vertex would have row-weight sum at most `1+10<13`, contradicting the strengthened E406 row-union theorem.

If `x=2`, the same contradiction is stronger: every missed S-vertex would need row weight at least11, but the maximum in (3) is10.

If `x=3`, every missed S-vertex must have row weight at least10. Only the unique star centre has weight10, so T cannot miss three vertices.

If `x=10`, every missed S-vertex needs row weight at least3. Thus T cannot miss any of the `10-m` weight-2 isolates. It can miss only the star centre and the m leaves, at most `m+1<=9` vertices. Contradiction.

If `x=0`, T is target-adjacent to all of S. From (3) and `t_s=d_M(s)+g_s`, the S decorations are then

- star centre: `9-m`;
- every leaf:1;
- every isolate:1.

Their total is `19-m>=11`, contradicting the q30 decoration budget `G<=8`.

Therefore the only possibility is

`x=11`.

So T is target-anticomplete to all eleven vertices of S.

## 5. Exact d11 shell normal form

Since y is also missing to all of S and yT is a target edge, the old missing shell is exactly

`M = K_{2,11} union K_{1,m}`

where the internal `K_{1,m}` lies on the 11-point side and `4<=m<=8`.

The decoration vector is zero except at the internal star centre, where

`g=8-m`.

Indeed, because T is missing to all S, the row weights (3) give

- centre decoration `10-(1+m+1)=8-m`;
- leaf decoration `3-(1+1+1)=0`;
- isolate decoration `2-(1+1)=0`.

Thus the distance-11 final-rise problem has been reduced to exactly five shell families, indexed by `m=4,5,6,7,8`.

## 6. Second 11-row and q-value of T

Let `E=N_C(T)`, so `|E|=11`. Repivoting T inserts the same S-block as repivoting y. A direct core-edge count gives

`q_T = 22 + m_E + epsilon_E + e_R(S,E)`,

where `m_E` is the number of complement edges in `C[E]` and `epsilon_E` is the old-core excess on E.

The E406 ceiling `q_T<=31` and the 11-block inequality imply

`8 <= m_E+epsilon_E <= 9-e_R(S,E)`.

Hence `e_R(S,E)<=1` and `q_T in {30,31}` whenever equality reaches the two boundary values. This turns the next step into a two-row compatibility problem for D and E over the same exact S-star shell, rather than a new shell classification problem.