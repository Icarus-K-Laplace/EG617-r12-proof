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
- `Q36_F2_2K1_A0_C7_ALLOWANCE3_REDUCTION.md`;
- `Q36_F2_2K1_A0_HIGH_C_SINGLE_CLASS_NORMAL_FORM.md`;
- `Q36_F2_2K1_A0_C9_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C10_FULL_CLOSURE.md`;
- `Q36_F2_2K1_A0_C10_MIXED_FULL_CLOSURE.md`.

General results:

- the two far 12-supports are disjoint and leave an 11-point remainder R with `alpha(H[R])<=2`;
- d2 rows have at most two distinct support classes;
- a repeated d2 class is the unique d2 class and is a zero-defect pure K2 repivoting to q35;
- if `n2>=3`, all d2 rows share that K2 and satisfy `3n2<=c+nu+2`, `2n2<=c+4`;
- the all-d2 branch has `c<=4`;
- d3 rows use at most two decorated missing-set classes;
- allowance-zero d3 class size<=2;
- allowance-one class has at most two distinct supports; if repeated, it is one pure q35 K3 class;
- allowance-two d3 class size<=6;
- all-d3 / two-missing-class sector has `c<=6`.

#### High-c all-d3 / single-class sector

The regular/decorated zero-gap theorem forces, for every `c>=7` single-class candidate,

- `nu=0`;
- distinguished decoration `g_x=3`;
- common-S allowance `A=c-4`;
- `Z=R\N_H(x)` has size `10-c`;
- every 3-support has exact form `D=Z union P`, `|P|=c-7`.

Consequences:

- c=7: EMPTY by common-three-point decoration overflow;
- c=8: EMPTY by common-two-point decoration overflow;
- c=9: EMPTY by the singleton-petal graph / saturated-edge argument in `Q36_F2_2K1_A0_C9_FULL_CLOSURE.md`;
- c=10 all-d3: EMPTY by the ten-row common-point theorem plus the K11/D14 incidence cap in `Q36_F2_2K1_A0_C10_FULL_CLOSURE.md`.

Thus the entire all-d3 / single-class high-c sector `c=7,8,9,10` is CLOSED.

#### c=10 mixed d2/d3 sector

`Q36_F2_2K1_A0_C10_MIXED_FULL_CLOSURE.md` closes every state with at least one d2 row.

A d2 support creates a regular target clique Q of size at least7 in the remainder. Every d3 support can then contain at most one Q-vertex, so at least two support incidences per d3 row lie in a set B of size at most4. The K11 `{p} union C` and inherited D14 cap give a universal three-vertex support-incidence bound. The resulting incidence mass on B is at least18, forcing three lambda-values to sum at least14, contradicting the D14 bound13.

Therefore the entire `2K1, a_F=0, c=10` layer is EMPTY.

The remaining `2K1, a_F=0` work lies at `c<=9`, with mixed d2/d3 states still open.

### Far topology K2

Retained from `Q36_F2_SHELL_LEDGER_REDUCTION.md`:

- at most3 d2 rows, with distinct disjoint pure K2 supports;
- d3 rows use at most two decorated missing-set classes;
- in the no-d2/two-class sector, total allowance<=1.

## Active assistant frontier

Highest priority:

1. reduce/close the remaining mixed `2K1, a_F=0, c<=9` states, beginning with c=9;
2. reduce the `2K1, a_F=1, c>=7` branch;
3. then return to the far-target-K2 f=2 branch.

The shell-poor five-one-spoke near-Mantel branch remains separate and OPEN.