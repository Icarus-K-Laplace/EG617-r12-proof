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

Previous aggregate `Q36_F2_FAR_K2_C8_ONE_D2_FULL_CLOSURE.md` is RETRACTED pending corrected-contract replay.

Canonical status:

> `c=8`, exactly one d2 row: OPEN_PENDING_REAUDIT.

Do not cite the old aggregate as an emptiness theorem.

## 3. c=8 no-d2 safe shell reduction

`Q36_F2_FAR_K2_C8_NO_D2_CLASS_REDUCTION_V2.md` proves under the corrected contract:

- all eight owners belong to one common d3 missing-set class;
- `A<=4`;
- if the inactive decorated pair Y is missing (`rho=1`), then `A<=3`;
- A=0 is EMPTY.

The superseded V1 aggregate is RETRACTED.

## 4. c=8 no-d2 A=1

`Q36_F2_FAR_K2_C8_NO_D2_A1_FULL_CLOSURE_V2.md` closes A=1 under the corrected contract.

The corrected proof first reduces A=1 to the unique `rho=1`, `4+4` repeated defect-zero K3 equality terminal, then uses a low-weight-clique/global-weight contradiction:

- the two blocks are anticomplete to each other and to `F union X`;
- shell alpha forces `a_F=2`, `t_x=0`;
- outside core vertices with common-S weight <=1 form a target clique, hence at most11;
- at least18 outside vertices have weight>=2, forcing total weight>=36;
- exact global common-S weight is35.

Contradiction.

Therefore

> no-d2 A=1 is EMPTY.

## 5. c=8 no-d2 A=2

The old `Q36_F2_FAR_K2_C8_NO_D2_A2_FULL_CLOSURE.md` is RETRACTED.

Corrected D14 allows an omitted equality channel when `rho=1`: a repeated target-K3 support may have multiplicity4.

Canonical status:

> no-d2 A=2: OPEN_PENDING_REAUDIT.

## 6. c=8 no-d2 A=3/A=4

Both remain OPEN under the corrected contract.

## 7. Current far-K2 priority

1. rebuild and close no-d2 A=2, especially the `rho=1`, multiplicity4 equality channel;
2. then A=3 and A=4;
3. re-audit the c=8 one-d2 branch under corrected D14;
4. only then parameterize to lower c.

This live file supersedes stronger far-K2 claims predating the D14/clique-contract audit.