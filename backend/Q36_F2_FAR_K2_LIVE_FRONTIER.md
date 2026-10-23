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

Thus only A=3,4 remain for c=8,n2=1.

## 3. c=8, one d2 row, A=3

`Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md` proves support multiplicity at most3 and isolates two multiplicity-three geometries.

### One-edge multiplicity-three geometry

`Q36_F2_FAR_K2_C8_D2_A3_ONEEDGE_FULL_CLOSURE.md` closes this terminal. Its proof uses only the d3-support union U with `alpha(H[U])<=2`, plus row closure, q35 saturation and D14. No fixed 12-point remainder is required.

### Repeated-K3 multiplicity-three geometry

The former `Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CLOSURE.md` is `RETRACTED` because it incorrectly imported a fixed 12-point remainder from the far-2K1 topology.

`Q36_F2_FAR_K2_C8_D2_A3_REPEATED_K3_CORRECT_REDUCTION.md` replaces it with a valid theorem:

- D is a target K3 of multiplicity3 and defect<=2;
- at least two external owner incidences lie in support classes disjoint from D;
- every support disjoint from D is itself a target K3;
- each such class E has `e_H(D,E)<=2`;
- any two distinct disjoint-from-D support classes intersect in exactly two points;
- therefore the distinct disjoint-class family is either
  1. Type P: all classes contain one fixed two-point set, or
  2. Type Q: all classes lie among the four triples of one four-point set;
- each such class has multiplicity at most3 and satisfies the D14 owner-incidence inequality.

This Type-P/Type-Q finite hypergraph system is the current repeated-K3 frontier.

The A=3 branch is not yet fully closed: repeated-K3 Type P/Q and the support-multiplicity<=2 sector remain OPEN.

## 4. Additional reusable theorem

`Q36_F2_A1_A4_DISJOINT_REPEATED_K3_RIGIDITY.md` applies only to the separate far-2K1,a_F=1,A=4 channels, where its fixed-remainder contract is available. It must not be imported into far-K2 without a new proof.

## 5. Current far-K2 tasks

Highest priority:

1. close A=3 repeated-K3 Type P and Type Q;
2. close the remaining multiplicity<=2 A=3 support system;
3. close c=8,n2=1,A=4;
4. treat the no-d2 c=8 branch;
5. parameterize downward to c<=7.

The far-K2 topology is independent of the concurrent `2K1,a_F=1` repeated-K3 work.