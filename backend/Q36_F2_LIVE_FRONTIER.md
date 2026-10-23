# q36 f=2 live frontier — 2026-10-23

Status: `LIVE REDUCTION MAP`. This summarizes proved q36 f=2 assets only; it does not close E338.

## Far topology 2K1, a_F=0 — CLOSED

`Q36_F2_2K1_A0_STAR_TERMINALS_FULL_CLOSURE.md` closes the last c=2/c=1 missing-star equality terminals. Together with the earlier c>=3, c=2-distinct and low-c closures:

> the entire `2K1, a_F=0` branch is EMPTY.

The final uniform argument uses the E338 total degree-excess budget39: every remaining star terminal would force at least seven core-regular vertices to have global degree at least20, already contributing at least49 excess.

## Far topology 2K1, a_F=1

`Q36_F2_2K1_A1_HIGH_C_NORMAL_FORM.md` gives

`A+G_Y=6-e_M(Y)`, `A>=2`,

and the valid K11/D14 triple cap for this 2K1 topology

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
- A=4 remains OPEN, but the repeated-K3 residual has sharpened substantially. `Q36_F2_A1_A4_DISJOINT_REPEATED_K3_FULL_CLOSURE.md` proves that a multiplicity-three target-K3 support cannot coexist with any distinct disjoint repeated support class. Since the c=8 multiplicity reduction forces at least three outside owner incidences into supports disjoint from such a K3, all of those disjoint support classes are now singleton classes.

### c=9

- A=2 is EMPTY (`Q36_F2_2K1_A1_C9_A2_FULL_CLOSURE.md`).
- A=3 is EMPTY (`Q36_F2_2K1_A1_C9_A3_FULL_CLOSURE.md`).
- A=4 and A=5 remain OPEN.
- In A=4, the same new disjoint-repeated closure applies: if a multiplicity-three target-K3 support exists, the at-least-four outside owner incidences forced into supports disjoint from it must all lie in singleton support classes. Thus the former two-repeated-block residual is EMPTY.

### c=10

The high-c normal form has exact A=6. This layer remains OPEN.

## Far target K2 — corrected contract mandatory

`Q36_F2_FAR_K2_D14_CONTRACT_CORRECTION.md` and `Q36_F2_FAR_K2_POST_D14_AUDIT.md` are the canonical scope boundary.

The old assertion that `{p} union C union F` is a target K11 is false because every C--F pair is a shell missing edge. The valid c=8 D14 base is

`B={p} union C union Y`,

where `Y=X\{x}` and `e(B)=55-rho`, `rho=e_M(Y)`.

Thus the corrected support inequality is

`3m+O_D+e_F(Y,D)+e_H(D)<=14+rho`.

There is no global target-K4 prohibition.

### Safe global structure

- any d2 row forces `a_F=0` and a pure globally-regular K2 support;
- for c>=3, `n2<=1`;
- d3 rows use at most two decorated missing-set classes;
- in the no-d2/two-class sector the total allowance is at most1.

The old aggregate one-d2 closure remains RETRACTED pending corrected-contract replay.

### c=8 no-d2

`Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION_V2.md` proves that all eight owners belong to one d3 missing-set class and `A<=4`, with `A+rho<=4`.

Corrected closures now give

- A=0 EMPTY;
- A=1 EMPTY (`Q36_F2_FAR_K2_C8_NO_D2_A1_FULL_CLOSURE_V2.md`);
- A=2 EMPTY (`Q36_F2_FAR_K2_C8_NO_D2_A2_FULL_CLOSURE_V2.md`).

Therefore the actual corrected no-d2 frontier is

> `A in {3,4}`.

A=4 automatically has `rho=0`.

### New A=3 tools

`Q36_F2_FAR_K2_C8_NO_D2_MULTISUPPORT_D17_CAPACITY.md` gives the genuine D17 two-support inequality

`3(r+s)+e_H(D)+e_H(E)+e_H(D,E)+e_F(Y,D union E)<=26+rho`

for disjoint 3-support classes of owner multiplicities r,s. In particular two disjoint K3 classes satisfy

- `r+s<=6` if rho=0;
- `r+s<=7` if rho=1.

`Q36_F2_FAR_K2_C8_NO_D2_A3_MULT4_ONEEDGE_FULL_CLOSURE.md` proves

> every A=3 multiplicity-four one-edge support channel is EMPTY.

The proof uses a global common-S weight contradiction: a repeated one-edge support D has weight zero and a unique disjoint repeated K3 class E; among the other29 core vertices at most12 can have weight1 and at least17 have weight>=2, forcing total common-S weight at least46, while the exact A=3 budget is at most37.

`Q36_F2_FAR_K2_C8_NO_D2_A3_ALPHA2_DISJOINT_SUPPORT_LEMMA.md` proves that inside any alpha-two A=3 support union, two disjoint distinct support classes must both be target K3s. Any disjoint pair involving a nonclique support violates the common-S cross-edge allowance.

Thus the next A=3 targets are multiplicity-four two-edge/K3 channels and then multiplicity<=3 systems.

## Shell-poor branch — new simultaneous interface

`Q36_SHELL_POOR_SIMULTANEOUS_INTERFACE.md` couples the at-least-five one-spoke pivots.

For q36 shell-poor,

`11<=G<=14`,
`sum_(u in H) g_u =39-G in [25,28]`.

For every one-spoke v with unique shell label a, `D=N_H(v)` and `Z=H\(D union {v})`,

`g_a+g(D)<=14`,
`g(Z)>=25-G+g_a>=11+g_a`.

Writing `J=overline(H)`, every one-spoke is a degree22 vertex of the K4-free 35-point graph J and `Z=N_J(v)`. If two one-spokes are adjacent in J, then their two shell labels meet every triangle of the shell missing graph M.

This turns the five separate near-Mantel conditions into one joint core/shell system.

## Active assistant frontier

Highest current priorities:

1. finish the `2K1,a_F=1,A=4` singleton-only residual created by the disjoint-repeated-K3 closure (c=8 and c=9);
2. finish corrected far-K2 no-d2 A=3 (multiplicity-four two-edge/K3, then lower multiplicities);
3. close corrected far-K2 no-d2 A=4;
4. re-audit c=8 one-d2 under the corrected D14 base;
5. in parallel, exploit `Q36_SHELL_POOR_SIMULTANEOUS_INTERFACE.md` through either repeated two-label triangle covers or decoration-overlap counting.

The q36 layer remains OPEN.