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

Proof chain:

- `Q36_F2_2K1_A0_REDUCTION.md`;
- `Q36_F2_2K1_A0_LOW_ALLOWANCE_D3.md`;
- `Q36_F2_2K1_A0_ALLOWANCE2_D3_CAPACITY.md`;
- `Q36_F2_2K1_A0_C7_ALLOWANCE3_REDUCTION.md`.

Results:

- the far 12-supports are disjoint and leave an 11-point remainder R with alpha(H[R])<=2;
- d2 rows have at most two distinct support classes;
- a repeated d2 class is the unique d2 class and is a zero-defect pure K2 repivoting to q35;
- if n2>=3, all d2 rows share that K2 and satisfy `3n2<=c+nu+2`, `2n2<=c+4`;
- the all-d2 branch has c<=4;
- d3 rows use at most two decorated missing-set classes;
- allowance-zero d3 class size<=2;
- allowance-one class has at most two distinct supports; if repeated, it is one pure q35 K3 class;
- allowance-two d3 class size<=6;
- all-d3 / two-missing-class sector has c<=6.

Therefore for c>=7 an all-d3 survivor must have one single decorated missing vertex.

For c=7 this single class is forced to allowance3. Its current exact terminal is

- `nu=0`;
- X is a target K4;
- decorations on X are `(3,1,1,1)`;
- the distinguished x has a 12-point core row;
- `|R\N_H(x)|` is exactly2 or3;
- every one of the seven 3-supports meets this 2/3-point non-neighbour set.

The nu=1 and nu=2 layers are empty, as are the cases where x has zero or one non-neighbour in R.

### Far topology K2

Retained from `Q36_F2_SHELL_LEDGER_REDUCTION.md`:

- at most3 d2 rows, with distinct disjoint pure K2 supports;
- d3 rows use at most two decorated missing-set classes;
- in the no-d2/two-class sector, total allowance<=1.

## Active assistant frontier

Highest priority:

1. close the two c=7 allowance3 terminals `|R\N(x)|=2` and3;
2. parameterize the resulting support-capacity mechanism to c>=8 single-class channels;
3. then return to the remaining mixed `a_F=0` and far-target-K2 branches.

The shell-poor five-one-spoke near-Mantel branch remains separate and OPEN.