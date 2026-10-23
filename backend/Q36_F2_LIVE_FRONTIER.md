# q36 f=2 live frontier — 2026-10-23

Status: `LIVE REDUCTION MAP`. This file summarizes proved q36 f=2 assets only; it does not close E338.

## Far topology 2K1, a_F=0

This branch is almost completely eliminated.

All states with c>=3 are EMPTY, and c=2 with distinct d2 supports is EMPTY. No d3 row survives anywhere.

Only three explicit equality terminals remain:

1. c=2 repeated support:
   - `|X|=9`;
   - `M[X]=K1,4 disjoint_union 4K1`;
   - `nu=4`, `G=9`, all X decorations1;
   - the two low owners share one pure K2 support D;
   - both D endpoints are target-adjacent exactly to the missing-star centre;
   - the q35 repivot saturates D14 with `G'=13`.

2. c=1, nu=2:
   - `M[X]=K1,2 disjoint_union 7K1`;
   - both support endpoints are adjacent exactly to the centre.

3. c=1, nu=3:
   - `M[X]=K1,3 disjoint_union 6K1`;
   - both support endpoints are adjacent to the centre;
   - at most one additional D--X target edge exists.

Key closure assets include

- `Q36_F2_2K1_A0_C7_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C8_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C9_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_LOW_C_D3_ELIMINATION.md`;
- `Q36_F2_2K1_A0_C3_C4_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C2_DISTINCT_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C2_REPEATED_STAR_REDUCTION.md`;
- `Q36_F2_2K1_A0_C1_STAR_REDUCTION.md`.

## Far topology 2K1, a_F=1

`Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md` parameterizes every remaining c>=7 state.

Let x0 be the unique decorated vertex with a far target neighbour and Y the inactive decorated set. Then

`A+G_Y=6-e_M(Y)`,

`A>=2`, and for every core triple T

`lambda(T)+e(Y,T)+e_H(T)<=14+e_M(Y)`.

Every repeated support repivots to q<=35 and satisfies both

`G_Y+3(m-1)<=13`

and

`3m<=13+e_M(Y)`.

For c=7 the only possible allowances are A=2 or3. `Q36_F2_2K1_A1_C7_A2_FULL_CLOSURE.md` proves

> `c=7, A=2` is EMPTY.

Therefore the exact c=7 terminal is now

- `A=3`;
- `Y=K3`;
- inactive decorations `(1,1,1)`;
- `{p} union C union Y=K11`;
- seven common-S 3-support rows in the 12-point alpha-two remainder R;
- every repeated support has multiplicity at most4 and q<=35.

For c=8,9,10 the high-c normal form gives the finite allowance ranges recorded in that file; c=10 has exact `A=6`.

## Far target K2

Retained from `Q36_F2_SHELL_LEDGER_REDUCTION.md`:

- at most3 d2 rows, with distinct disjoint pure K2 supports;
- d3 rows use at most two decorated missing-set classes;
- in the no-d2/two-class sector, total allowance<=1.

## Active assistant frontier

Highest priority:

1. close the three a_F=0 missing-star equality terminals;
2. close `2K1,a_F=1,c=7,A=3` and lift its support-capacity mechanism to c=8..10;
3. return to the far-target-K2 branch.

The shell-poor five-one-spoke near-Mantel branch remains separate and OPEN.