# q36 f=2 far-target-K2 — c=8, exactly one d2 row: full closure

Status: `PROVED` under the established far-K2 c8 one-d2 contract and the certified allowance-layer closures listed below.

This file is an aggregate closure only. It introduces no new local lemma.

## 1. Reduction to A=2,3,4

`Q36_F2_FAR_K2_C8_D2_REDUCTION.md` proves that when c=8 and exactly one d2 row is present:

- the remaining seven low owners are d3 rows;
- all seven belong to one common decorated missing-set class;
- the class allowance is exactly one of

`A in {2,3,4}`.

## 2. Allowance two

`Q36_F2_FAR_K2_C8_D2_A2_FULL_CLOSURE.md` proves

> A=2 is EMPTY.

## 3. Allowance three

The corrected A=3 proof chain is

- `Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md`;
- `Q36_F2_FAR_K2_C8_D2_A3_ONEEDGE_FULL_CLOSURE.md`;
- `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CORRECT_REDUCTION.md`;
- `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_FULL_CLOSURE_V2.md`;
- `Q36_F2_FAR_K2_C8_D2_A3_FULL_CLOSURE.md`.

The obsolete fixed-remainder file `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CLOSURE.md` remains RETRACTED and is not used.

Therefore

> A=3 is EMPTY.

## 4. Allowance four

The A=4 chain first eliminates all multiplicity at least three, then all multiplicity-two support types:

- `Q36_F2_FAR_K2_C8_D2_A4_HIGH_MULTIPLICITY_REDUCTION.md`;
- the O=2/O=1/O=0 unit-K3 multiplicity-three closures;
- `Q36_F2_FAR_K2_C8_D2_A4_MULT2_K3_FULL_CLOSURE.md`;
- the repeated one-edge multiplicity-two closure;
- the repeated two-edge multiplicity-two reduction and final closure.

The final remaining all-singleton sector is closed by

`Q36_F2_FAR_K2_C8_D2_A4_ALL_SINGLETON_FULL_CLOSURE.md`.

That proof ends by forcing the seven singleton supports to be pairwise-intersecting target K3s, then linear, with every core point lying in at most two supports. A 3-set can then meet at most three other supports, contradicting the requirement to meet the other six.

Therefore

> A=4 is EMPTY.

## 5. Conclusion

All possible allowance levels are empty. Hence

> q36 f=2, far-target-K2, c=8, exactly one d2 row is EMPTY.

The remaining c=8 far-K2 task is the no-d2 branch.