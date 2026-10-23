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
  2. a target-K3 terminal forcing at least two external owner incidences into disjoint target-K3 supports.

`Q36_F2_FAR_K2_C8_D2_A3_ONEEDGE_FULL_CLOSURE.md` closes terminal (1) by repivoting to a D14-saturated q35 shell. The external supports reduce to pairwise-intersecting pure K2 petal rows, contradicting D14 multiplicity.

`Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CLOSURE.md` is `RETRACTED`: its previous proof incorrectly imported a fixed 12-point remainder from the far-2K1 topology. The repeated-K3 terminal is therefore OPEN again.

The valid repeated-K3 interface is:

- D is a target K3 of multiplicity3 and defect<=2;
- at least two external owner incidences lie in supports disjoint from D;
- every support disjoint from D is itself a target K3;
- each such disjoint K3 E satisfies `e_H(D,E)<=2`;
- the d3-support union U satisfies `alpha(H[U])<=2` because the unique pure d2 block D0 is target-anticomplete to U.

No contradiction from these facts alone is currently certified.

## 4. Additional reusable theorem

`Q36_F2_A1_A4_DISJOINT_REPEATED_K3_RIGIDITY.md` applies only to the separate far-2K1,a_F=1,A=4 channels, where the fixed 12-point remainder contract is available. It must not be imported into far-K2 without a new global-capacity proof.

## 5. Current far-K2 tasks

Highest priority:

1. close the c=8,n2=1,A=3 repeated-K3 terminal under the correct far-K2 contract;
2. then close the remaining multiplicity<=2 A=3 support system;
3. close c=8,n2=1,A=4;
4. treat the no-d2 c=8 branch;
5. parameterize downward to c<=7.

The far-K2 topology is independent of the concurrent `2K1,a_F=1` repeated-K3 work.