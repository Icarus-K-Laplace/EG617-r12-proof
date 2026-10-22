# E406 distance-11 final rise — FULL CLOSURE

Status: `PROVED EMPTY` for the entire d=11 q30->q31 final-rise class. `E406` itself remains `OPEN`.

Dependencies:

- `E406_D11_EXACT_SHELL.md`;
- `E406_D11_TWO_MAXIMA.md`;
- `E406_D11_THREE_STAR_BLOCKS.md`;
- Line-A theorem L4: every inherited R(4,47) core with at most286 edges has minimum degree at least12;
- `E406_NEAR284_ROW_UNION_LEMMAS.md` (PAIR-13).

Retain the d11 terminal notation:

- p is q30;
- y and T are adjacent q31 pivots;
- S is the common 11-point old-shell side anticomplete to y,T;
- D=N_C(y), E=N_C(T), each of size11;
- `|D intersect E|<=1`;
- the complement graphs on D and E are stars;
- `e(S,D)=0`, `e(S,E)<=1`.

Write d0,e0 for the complement-star centres of D,E.

## 1. The D-star centre must lie in E

The D-star complement has

`m_D+epsilon_D=9`,

and all D-core excess is supported at d0. Hence every D-star leaf has old-core excess0.

Since `m_D>=3` and `|D intersect E|<=1`, choose a D-star leaf l not belonging to E. In the q31 y-shell:

- l is undecorated;
- its missing neighbours are `{p,T,d0}`;
- its missing degree is3;
- the shell row weights of p,T,d0 are:
  - `t_p=11`;
  - `t_T=11-|D intersect E|`;
  - `t_d0=11`.

The subset charge on `{p,T,d0}` is therefore at most31, and the standard d=3 repivot lower bound gives

`q_l>=30`.

The global E406 ceiling gives `q_l<=31`. Thus the l-core has284 or285 edges, and L4 yields minimum degree at least12.

Repivoting l removes its 3-row and imports `{p,T,d0}` into the core. The imported centre d0 has old y-core row weight11.

- d0 is target-nonadjacent to p;
- d0 gains T as a new core neighbour if and only if `d0 in E`;
- deleting the l-row can only decrease its core degree.

Therefore, if `d0 notin E`, its degree in the l-core is at most11, contradicting L4.

Hence

`d0 in E`.

Since `|D intersect E|<=1`, this already gives

`D intersect E={d0}`.      (A)

## 2. The same vertex is the E-star centre

Apply the symmetric argument in the q31 T-view to an E-star leaf outside D. It forces

`e0 in D`.

Together with (A) and the one-point overlap,

`d0=e0=:x`,
`D intersect E={x}`.      (CENTER-OVERLAP)

Thus the two 11-block complement stars share exactly their centre and no other vertex.

## 3. PAIR-13 forbids every D-star isolate

Return to the q31 y-shell.

Because `D intersect E={x}`, the degree-13 shell vertex T is target-adjacent to exactly one D-vertex, namely x. Hence its missing degree and row weight are

`t_T=d_M(T)=10`.

Now suppose v is an isolate of the complement star on D. Then:

- v has old-core excess0;
- v is not the overlap centre x, hence `v notin E`;
- in the q31 y-shell, v is target-nonadjacent to p and T;
- internally on D it has no missing edge.

Therefore v is undecorated with

`t_v=d_M(v)=2`.

But Tv is a missing-shell edge. PAIR-13 gives

`|D_T union D_v|>=13`.

On the other hand

`|D_T union D_v|<=t_T+t_v=10+2=12`,

a contradiction.

Hence the D-star complement has no isolates.

An 11-vertex star with no isolates must have

`m_D=10`.

## 4. Final contradiction

The exact zero-slack d11 identity already gives

`m_D+epsilon_D=9`,

with nonnegative excess. Thus

`m_D<=9`.

This contradicts `m_D=10` from Section3.

Therefore no d=11 q30->q31 final-rise edge exists.

> **D11-CLOSURE. The complete E406 distance-11 final-rise class is empty.**