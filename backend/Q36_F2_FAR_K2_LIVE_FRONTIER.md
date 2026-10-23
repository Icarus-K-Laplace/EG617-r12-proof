# q36 f=2 far-target-K2 live frontier

Status: `LIVE REDUCTION MAP` under `Q36_F2_FAR_K2_POST_D14_AUDIT.md`.

The corrected contract is mandatory:

- valid D14 base: `B={p} union C union Y`, not `{p} union C union F`;
- `3m+O_D+e_F(Y,D)+e_H(D)<=14+nu_Y`;
- parent clique contract is `omega<=11`; there is no global target-K4 prohibition.

## 1. Safe global interfaces

Still canonical:

- exact f=2 shell ledger;
- d2/d3 repivot formulas;
- any d2 row forces `a_F=0` and a pure globally-regular K2 support;
- for c>=3, `n2<=1`;
- d3 rows use at most two decorated missing-set classes;
- no-d2 two-class allowance sum is at most1;
- common-S row closure / overlap identities;
- CORE211 excess `sum kappa=2`.

## 2. c=8 exactly one d2 row

Previous aggregate `Q36_F2_FAR_K2_C8_ONE_D2_FULL_CLOSURE.md` remains RETRACTED pending corrected-contract replay.

Canonical status:

> `c=8`, exactly one d2 row: OPEN_PENDING_REAUDIT.

Do not cite pre-audit D14 closures unless separately rebuilt against `Q36_F2_FAR_K2_D14_CONTRACT_CORRECTION.md`.

## 3. c=8 no-d2 shell reduction

`Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION_V2.md` proves under the corrected contract:

- all eight owners belong to one common d3 missing-set class;
- `A<=4`;
- if the inactive decorated pair Y is missing (`rho=1`), then `A<=3`;
- A=0 is EMPTY.

## 4. Corrected low-allowance closures

`Q36_F2_FAR_K2_C8_NO_D2_A1_FULL_CLOSURE_V2.md` proves

> no-d2 A=1 is EMPTY.

`Q36_F2_FAR_K2_C8_NO_D2_A2_FULL_CLOSURE_V2.md`, together with the dedicated multiplicity-four equality closure, rebuilds the next layer under the corrected D14/clique contract and proves

> no-d2 A=2 is EMPTY.

The V2 proof explicitly avoids the false F-based K11 base and any target-K4 prohibition.

Thus the corrected no-d2 c=8 frontier is now

> `A in {3,4}` only.

Since `A+rho<=4`, the A=4 layer automatically has `rho=0`.

## 5. New corrected multi-support tool

`Q36_F2_FAR_K2_C8_NO_D2_MULTISUPPORT_D17_CAPACITY.md` derives the genuine hereditary D17 interface from the correct 11-point base `B={p} union C union Y`.

For disjoint three-point support classes D,E with owner multiplicities r,s,

`3(r+s)+e_H(D)+e_H(E)+e_H(D,E)+e_F(Y,D union E)<=26+rho`.

In particular two disjoint target-K3 classes satisfy

- `r+s<=6` for rho=0;
- `r+s<=7` for rho=1.

This is intended to replace invalid K11-based owner-capacity shortcuts in the A=3/A=4 analysis.

## 6. Current far-K2 priority

1. close no-d2 A=3 under corrected D14+D17;
2. close no-d2 A=4 (necessarily rho=0);
3. re-audit the c=8 one-d2 branch under corrected D14;
4. only then parameterize to lower c.

This live file supersedes stronger far-K2 claims predating the D14/clique-contract audit.