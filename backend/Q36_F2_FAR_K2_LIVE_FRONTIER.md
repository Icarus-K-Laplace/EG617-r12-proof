# q36 f=2 far-target-K2 live frontier

Status: `LIVE REDUCTION MAP`. This records proved assistant-owned far-K2 results only; it does not close the full q36 layer.

## 1. Global d2 reduction

`Q36_F2_FAR_K2_D2_GLOBAL_REDUCTION.md` proves:

- any d2 row forces `a_F=0` and has a pure target-K2 support of globally regular core vertices;
- for c>=3, at most one d2 row exists;
- d3 rows use at most two decorated missing-set classes;
- if two d3 classes occur with a d2 row, their total allowance is at most2;
- with no d2 row the known sharper two-class allowance sum is at most1.

## 2. c=8 with one d2 row

`Q36_F2_FAR_K2_C8_D2_REDUCTION.md` proves:

- the seven d3 owners form one missing-set class;
- allowance `A in {2,3,4}`.

`Q36_F2_FAR_K2_C8_D2_A2_FULL_CLOSURE.md` proves A=2 is EMPTY.

## 3. A=3 is fully CLOSED

The obsolete `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CLOSURE.md` remains `RETRACTED`; it incorrectly imported a fixed 12-point remainder from the far-2K1 topology.

The corrected chain is:

- `Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md`;
- `Q36_F2_FAR_K2_C8_D2_A3_ONEEDGE_FULL_CLOSURE.md`;
- `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CORRECT_REDUCTION.md`;
- `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_FULL_CLOSURE_V2.md`;
- `Q36_F2_FAR_K2_C8_D2_A3_FULL_CLOSURE.md`.

The full closure uses no fixed-remainder assumption. It eliminates multiplicity-three, multiplicity-two and all-singleton systems under the correct far-K2 contract.

Therefore

> `c=8, n2=1, A=3` is EMPTY.

## 4. A=4 high-multiplicity sector is fully CLOSED

`Q36_F2_FAR_K2_C8_D2_A4_HIGH_MULTIPLICITY_REDUCTION.md` proves:

- multiplicity4 is impossible;
- every multiplicity-three nonclique support is impossible;
- every multiplicity-three support is a target K3 with exact unit weights `(1,1,1)` and overlap charge `O_D in {0,1,2}`.

The three overlap-charge terminals are now all closed:

- `Q36_F2_FAR_K2_C8_D2_A4_UNIT_K3_O2_CLOSURE.md` closes `O_D=2`;
- `Q36_F2_FAR_K2_C8_D2_A4_UNIT_K3_O1_CLOSURE.md` closes `O_D=1`;
- `Q36_F2_FAR_K2_C8_D2_A4_UNIT_K3_O0_FULL_CLOSURE.md` closes `O_D=0`.

Hence

> every surviving A=4 support has multiplicity at most2.

## 5. Current c=8 one-d2 frontier

The allowance levels are now:

- `A=2`: CLOSED;
- `A=3`: CLOSED;
- `A=4`: OPEN only in the multiplicity-at-most-two support system.

Thus the complete `c=8, n2=1` problem has been reduced to one terminal layer:

> one d2 row, seven d3 owners in one common missing-set class, allowance4, and every d3 support class has multiplicity at most2.

## 6. Current far-K2 tasks

Highest priority:

1. close `c=8,n2=1,A=4` with support multiplicity<=2;
2. treat the no-d2 c=8 branch;
3. parameterize downward to c<=7.

The far-K2 topology is independent of the concurrent `2K1,a_F=1` work and of the Astra A/B frontiers.