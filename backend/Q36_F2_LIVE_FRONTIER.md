# q36 f=2 live frontier — 2026-10-23

Status: `LIVE REDUCTION MAP`. This file summarizes proved q36 f=2 assets only; it does not close E338.

## Closed / reduced sectors

### Far topology 2K1, a_F=1

Proof chain:

- `Q36_F2_2K1_A1_REDUCTION.md`;
- `Q36_F2_2K1_A1_C6_FULL_CLOSURE.md`.

Results:

- all low rows share one d3 missing set;
- c=4,5,6 are EMPTY;
- surviving branch has c>=7.

### Far topology 2K1, a_F=0

The proof chain now includes the structural reductions and full closures through c=3..10, including

- `Q36_F2_2K1_A0_C7_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C8_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C9_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C9_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C10_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C10_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_LOW_C_D3_ELIMINATION.md`;
- `Q36_F2_2K1_A0_C3_C4_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C2_DISTINCT_FULL_CLOSURE.md`.

The branch is now almost completely eliminated:

- every state with c>=3 is EMPTY;
- no d3 row survives anywhere;
- c=2 with distinct d2 supports is EMPTY.

Only three explicit equality terminals remain.

#### c=2 repeated-support terminal

`Q36_F2_2K1_A0_C2_REPEATED_STAR_REDUCTION.md` proves that the two low owners must share one pure K2 support D and

- `|X|=9`;
- `M[X]=K1,4 disjoint_union 4K1`;
- `nu=4`, `G=9`, every X-vertex has decoration1;
- both D-endpoints are target-adjacent exactly to the missing-star centre h inside X;
- the q35 repivot is D14-saturated with new decoration total13.

#### c=1 terminals

`Q36_F2_2K1_A0_C1_STAR_REDUCTION.md` leaves exactly two families:

1. `nu=2`: `M[X]=K1,2 disjoint_union 7K1`, with both support endpoints adjacent exactly to the star centre;
2. `nu=3`: `M[X]=K1,3 disjoint_union 6K1`, with both support endpoints adjacent to the star centre and at most one extra D--X target edge.

No other `2K1,a_F=0` state remains.

### Far topology K2

Retained from `Q36_F2_SHELL_LEDGER_REDUCTION.md`:

- at most3 d2 rows, with distinct disjoint pure K2 supports;
- d3 rows use at most two decorated missing-set classes;
- in the no-d2/two-class sector, total allowance<=1.

## Active assistant frontier

Highest priority:

1. close the three explicit `2K1,a_F=0` missing-star equality terminals;
2. reduce the `2K1,a_F=1,c>=7` branch;
3. return to the far-target-K2 f=2 branch.

The shell-poor five-one-spoke near-Mantel branch remains separate and OPEN.