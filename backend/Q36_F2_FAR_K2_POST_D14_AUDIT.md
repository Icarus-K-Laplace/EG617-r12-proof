# q36 f=2 far-target-K2 — post-D14 canonical scope audit

Status: `PROVED AUDIT`.

This file records which far-target-K2 conclusions remain canonical after `Q36_F2_FAR_K2_D14_CONTRACT_CORRECTION.md`.

## 1. Mandatory corrected contract

For c=8 far-K2 with one active d3 missing vertex x and inactive pair Y:

- `{p} union C union F` is NOT a target K11;
- the valid 11-point D14 base is `B={p} union C union Y`;
- if `rho=e_M(Y)`, then `e(B)=55-rho`;
- for a support D of owner multiplicity m,

`3m+O_D+e_F(Y,D)+e_H(D)<=14+rho`.

The legal parent clique contract is `omega<=11`. There is no global target-K4 prohibition.

Any far-K2 proof using the false F-based K11 or treating a K4 as an automatic contradiction is noncanonical until rebuilt.

## 2. Safe global interfaces

The following are unaffected and remain canonical:

- `Q36_F2_SHELL_LEDGER_REDUCTION.md`;
- exact q36 d2/d3 repivot formulas;
- the global far-K2 d2 structural reduction (`a_F=0`, pure d2 support, `n2<=1` for c>=3);
- common-S row closure and overlap identities;
- CORE211 `sum kappa=2`;
- inherited D(14)=69;
- alpha(H)<=3 and parent alpha<=4 / omega<=11.

## 3. c=8 one-d2 status

`Q36_F2_FAR_K2_C8_ONE_D2_FULL_CLOSURE.md` is RETRACTED as an aggregate.

Reason: its underlying allowance closures were generated across the D14-scope transition, and several assets explicitly use the unavailable target-K4 prohibition or the false F-based K11 base.

Therefore the canonical status is

> c=8, exactly one d2 row: OPEN_PENDING_REAUDIT.

Individual underlying files may later be reinstated after corrected-contract replay; the aggregate is not proof of emptiness.

## 4. c=8 no-d2 safe reduction

The corrected V2 reduction proves:

- all eight owners lie in one common d3 missing-set class;
- `A<=4`, and `rho=1 => A<=3`;
- A=0 is EMPTY.

`Q36_F2_FAR_K2_C8_NO_D2_A1_FULL_CLOSURE_V2.md` further proves, under the corrected contract,

> A=1 is EMPTY.

The old A=1 proof in the retracted V1 aggregate must not be cited.

## 5. c=8 no-d2 A=2 status

The old `Q36_F2_FAR_K2_C8_NO_D2_A2_FULL_CLOSURE.md` is RETRACTED.

The corrected D14 inequality allows an equality channel omitted by the old proof:

- `rho=1`;
- repeated target-K3 support multiplicity4 can satisfy the corrected D14 cap.

Therefore

> no-d2 A=2 is OPEN_PENDING_REAUDIT.

## 6. c=8 no-d2 A=3/A=4

These layers remain OPEN. Any future proof must use the corrected D14 base and must not invoke global K4-freeness.

## 7. Current canonical far-K2 frontier

Safely certified:

- global d2/row-class reductions;
- c=8 no-d2 single-class reduction;
- no-d2 A=0 EMPTY;
- no-d2 A=1 EMPTY (corrected V2).

Open:

- c=8 one-d2: corrected-contract re-audit;
- c=8 no-d2 A=2;
- c=8 no-d2 A=3;
- c=8 no-d2 A=4;
- lower c after c=8 is resolved.

This audit supersedes any stronger far-K2 live-state claim that predates the corrected D14/clique contract.