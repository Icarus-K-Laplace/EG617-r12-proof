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

`Q36_F2_FAR_K2_C8_D2_A2_FULL_CLOSURE.md` proves:

- A=2 is EMPTY.

Thus only A=3,4 remain for c=8,n2=1.

## 3. c=8, one d2 row, A=3

`Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md` proves:

- support multiplicity at most3;
- every multiplicity-three support is either
  1. an exact one-edge q35 equality terminal, or
  2. a target-K3 terminal forcing disjoint target-K3 support incidences.

`Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CLOSURE.md` closes terminal (2) by a six-point vertex-cover / CORE211 w-mass contradiction.

`Q36_F2_FAR_K2_C8_D2_A3_ONEEDGE_FULL_CLOSURE.md` closes terminal (1) by repivoting to a D14-saturated q35 shell. The four external supports become pure K2 petal rows; their pairwise-intersection graph violates the D14 multiplicity inequality.

Therefore:

> every surviving c=8,n2=1,A=3 support class has multiplicity at most2.

A full closure of the multiplicity<=2 system is not yet claimed.

## 4. Additional reusable theorem

`Q36_F2_A1_A4_DISJOINT_REPEATED_K3_RIGIDITY.md` proves, in the separate `2K1,a_F=1,A=4` channels, that a disjoint pair of repeated target K3 supports is forced into an exact K1,3 cross graph and consumes the full CORE211 excess budget. This is not automatically imported into far-K2, but the proof architecture is reusable.

## 5. Current far-K2 tasks

Highest priority:

1. close `c=8,n2=1,A=3` with support multiplicity<=2;
2. close `c=8,n2=1,A=4`;
3. treat the no-d2 c=8 branch;
4. parameterize downward to c<=7.

The far-K2 topology is independent of the concurrent `2K1,a_F=1` repeated-K3 work.