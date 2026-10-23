# q36 f=2 far-target-K2 — c=8, one d2 row, A=3 repeated-K3 closure

Status: `RETRACTED`.

## Retraction reason

The previous proof incorrectly imported a fixed 12-point remainder from the separate far-`2K1` topology. In the far-target-`K2` topology there is no canonical 12-point set `R` whose complement after two disjoint 3-supports has exactly six vertices.

The invalid step was the assertion

`L=R\(D union E), |L|=6`,

followed by a six-point `w=kappa+e(.,x)` mass bound.

That fixed-cardinality claim is not provided by `Q36_F2_FAR_K2_D2_GLOBAL_REDUCTION.md` or `Q36_F2_FAR_K2_C8_D2_REDUCTION.md`.

## What remains valid

The following precursor statements remain valid:

- the unique d2 support D0 is a pure globally-regular K2;
- D0 is target-anticomplete to every d3 support;
- therefore the union U of all d3 supports satisfies `alpha(H[U])<=2`;
- in the c=8,n2=1,A=3 branch, a multiplicity-three target-K3 support D has defect at most2;
- at least two external owner incidences lie in supports disjoint from D;
- every support disjoint from such a repeated K3 D must itself be a target K3;
- common-S row closure gives `e_H(D,E)<=2` for any such disjoint K3 support E.

These facts do not by themselves yield a contradiction without an additional global support-capacity argument.

## Current status

The multiplicity-three repeated-K3 terminal is `OPEN` again.

The separate one-edge multiplicity-three terminal is handled by `Q36_F2_FAR_K2_C8_D2_A3_ONEEDGE_FULL_CLOSURE.md`; that argument uses only the support-union independence consequence from D0 and does not require a fixed 12-point remainder.

This retraction is local and does not affect:

- `Q36_F2_FAR_K2_D2_GLOBAL_REDUCTION.md`;
- `Q36_F2_FAR_K2_C8_D2_REDUCTION.md`;
- `Q36_F2_FAR_K2_C8_D2_A2_FULL_CLOSURE.md`;
- `Q36_F2_FAR_K2_C8_D2_A3_MULTIPLICITY_REDUCTION.md`;
- `Q36_F2_FAR_K2_C8_D2_A3_ONEEDGE_FULL_CLOSURE.md`.