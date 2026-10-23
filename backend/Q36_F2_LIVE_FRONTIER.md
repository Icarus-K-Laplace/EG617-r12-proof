# q36 f=2 live frontier — 2026-10-23

Status: `LIVE REDUCTION MAP`. This summarizes proved q36 f=2 assets only; it does not close E338.

## Far topology 2K1, a_F=0 — CLOSED

`Q36_F2_2K1_A0_STAR_TERMINALS_FULL_CLOSURE.md` closes the last c=2/c=1 missing-star equality terminals. Together with the earlier c>=3, c=2-distinct and low-c closures:

> the entire `2K1, a_F=0` branch is EMPTY.

The final uniform argument uses the E338 total degree-excess budget39: every remaining star terminal would force at least seven core-regular vertices to have global degree at least20, already contributing at least49 excess.

## Far topology 2K1, a_F=1

`Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md` gives

`A+G_Y=6-e_M(Y)`, `A>=2`,

and the K11/D14 triple cap

`lambda(T)+e(Y,T)+e_H(T)<=14+e_M(Y)`.

Repeated supports repivot to q<=35 and satisfy

`G_Y+3(m-1)<=13`, `3m<=13+e_M(Y)`.

### c=7 — CLOSED

- A=2 is EMPTY (`Q36_F2_2K1_A1_C7_A2_FULL_CLOSURE.md`).
- A=3 is EMPTY. The proof chain eliminates multiplicity>=3, then all repeated supports, then the final seven-distinct-singleton 3-support system (`Q36_F2_2K1_A1_C7_A3_ALL_SINGLETON_FULL_CLOSURE.md`).

Hence

> `2K1, a_F=1, c=7` is EMPTY.

### c=8

Possible allowances are A=2,3,4.

- A=2 is EMPTY (`Q36_F2_2K1_A1_C8_A2_FULL_CLOSURE.md`).
- A=3 is EMPTY (`Q36_F2_2K1_A1_C8_A3_FULL_CLOSURE.md`).
- A=4 remains OPEN, but `Q36_F2_2K1_A1_C8_A4_MULTIPLICITY_REDUCTION.md` proves:
  - multiplicity4 is impossible;
  - every multiplicity-three support, if any, is a target K3;
  - such a K3 obeys `O_D+e(Y,D)<=2`, so at least three external owner incidences lie in supports disjoint from D.

Thus the exact c=8 frontier is only A=4.

### c=9

Possible allowances are A=2,3,4,5.

- A=2 is EMPTY (`Q36_F2_2K1_A1_C9_A2_FULL_CLOSURE.md`).
- A=3 is EMPTY (`Q36_F2_2K1_A1_C9_A3_FULL_CLOSURE.md`).
- A=4 remains OPEN, but `Q36_F2_2K1_A1_C9_A4_MULTIPLICITY_REDUCTION.md` proves:
  - multiplicity4 is impossible;
  - every multiplicity-three support is a target K3;
  - it satisfies `O_D+e(y,D)<=2`, forcing at least four external owner incidences into supports disjoint from D.
- A=5 remains OPEN.

### c=10

The high-c normal form has exact A=6. This layer remains OPEN.

## Far target K2

Retained from `Q36_F2_SHELL_LEDGER_REDUCTION.md`:

- at most3 d2 rows, with distinct disjoint pure K2 supports;
- d3 rows use at most two decorated missing-set classes;
- in the no-d2/two-class sector, total allowance<=1.

This topology remains OPEN.

## Active assistant frontier

Highest priority:

1. close the repeated-K3 / forced-disjoint-support geometry in `c=8,A=4`;
2. lift the same slack-three mechanism to `c=9,A=4`;
3. then treat `c=9,A=5` and exact `c=10,A=6`;
4. return to the far-target-K2 branch.

The shell-poor five-one-spoke near-Mantel branch remains separate and OPEN.