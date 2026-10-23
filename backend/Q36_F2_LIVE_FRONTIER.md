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

The main proof chain now includes

- `Q36_F2_2K1_A0_REDUCTION.md`;
- `Q36_F2_2K1_A0_LOW_ALLOWANCE_D3.md`;
- `Q36_F2_2K1_A0_ALLOWANCE2_D3_CAPACITY.md`;
- `Q36_F2_2K1_A0_HIGH_C_SINGLE_CLASS_NORMAL_FORM.md`;
- `Q36_F2_2K1_A0_C7_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C8_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C9_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C9_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C10_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C10_MIXED_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_LOW_C_D3_ELIMINATION.md`;
- `Q36_F2_2K1_A0_PURE_D2_TERMINALS.md`.

General facts:

- the two far 12-supports are disjoint and leave an 11-point remainder R with `alpha(H[R])<=2`;
- d2 rows have at most two distinct support classes;
- a repeated d2 class is the unique d2 class and is a zero-defect pure K2 repivoting to q35;
- if `n2>=3`, all d2 rows share that K2 and satisfy `3n2<=c+nu+2`, `2n2<=c+4`;
- d3 rows use at most two decorated missing-set classes;
- allowance-zero d3 class size<=2;
- allowance-one d3 class has at most two distinct supports and any repeated support is the unique pure q35 K3 class;
- allowance-two d3 class size<=6.

#### High-c c=7,8,9,10

The all-d3 / single-class sector c=7,8,9,10 is CLOSED.

The mixed d2/d3 sectors c=7,8,9,10 are also CLOSED. Hence

> every `2K1,a_F=0` candidate has `c<=6`.

#### Low-c d3 elimination

`Q36_F2_2K1_A0_LOW_C_D3_ELIMINATION.md` proves that for every `c<=6` no d3 row can occur at all.

If two d3 classes were active, their exact allowance sum is

`A_x+A_z = 1_(xz in M) - e_M(Y) - G_Y - 1 <0`

because at least three inactive decorated vertices remain.

If one class were active,

`A_x+G_Y=6-e_M(Y)`

while at least four inactive decorated vertices give `G_Y>=4`, forcing `A_x<=2`; the regular/decorated zero-gap inequality requires `A_x>=3`.

Therefore

> `c<=6 => n3=0`.

The earlier all-d2 capacity gives `c<=4`. Consequently the entire `2K1,a_F=0` branch has collapsed to

> pure d2 only, with `c in {1,2,3,4}`.

#### Exact pure-d2 terminals

For c>=3 all d2 rows share one repeated pure K2 support D. `Q36_F2_2K1_A0_PURE_D2_TERMINALS.md` gives:

- c=4: `nu=e_M(X)=6`, `G=7`, every X-vertex has decoration1, and `e(D,X)=0`;
- c=3: `nu in {4,5}` and `e(D,X)<=nu-4`.

The c=1,2 pure-d2 terminals remain less rigid and are now the only other states in this branch.

### Far topology K2

Retained from `Q36_F2_SHELL_LEDGER_REDUCTION.md`:

- at most3 d2 rows, with distinct disjoint pure K2 supports;
- d3 rows use at most two decorated missing-set classes;
- in the no-d2/two-class sector, total allowance<=1.

## Active assistant frontier

Highest priority:

1. close the four pure-d2 `2K1,a_F=0` terminals c=1,2,3,4, starting with the exact c=4 equality shell;
2. reduce the `2K1,a_F=1,c>=7` branch;
3. then return to the far-target-K2 f=2 branch.

The shell-poor five-one-spoke near-Mantel branch remains separate and OPEN.