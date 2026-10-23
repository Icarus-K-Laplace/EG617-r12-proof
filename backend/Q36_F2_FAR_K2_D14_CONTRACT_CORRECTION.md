# q36 f=2 far-target-K2 — D14 contract correction

Status: `PROVED AUDIT / SCOPE CORRECTION`.

This file corrects a recurring D14-base error in several recently generated far-target-K2 c=8 proof assets.

## 1. Canonical inherited cap

`front_end/FRONTEND_BRIDGE_THEOREM.md` defines

`D(n)=C(n,2)-11*p_12(n)`.

For n=14, `p_12(14)=2`, hence

`D(14)=91-22=69`.

This is a valid inherited cap on **every** induced 14-set in the legal parent contract.

The issue is not the value 69. The issue is identifying the correct already-dense 11-point base inside a far-K2 c=8 shell.

## 2. Far-K2 shell geometry

In the f=2 far-target-K2 branch, the master ledger has

- low regular target clique `C`, here `|C|=8`;
- far regular target K2 `F={a,b}`;
- decorated set `X`, here `|X|=3`;
- every C--F pair is a shell missing edge.

Therefore

`{p} union C union F`

is **not** a target K11. Any D14 proof that counts 55 base edges on that set is invalid.

Now assume the seven d3 owners use one active decorated missing vertex `x`, and put

`Y=X\{x}`,  |Y|=2.

Every low vertex of C is missing exactly F plus x, so every C--Y pair is a target edge. Also p is target-adjacent to all shell vertices. Hence

`B={p} union C union Y`

is an 11-point target clique except possibly for the edge inside Y.

Let

`nu_Y=e_M(Y)` in {0,1}.

Then exactly

`e(B)=55-nu_Y`.                                             (1)

## 3. Correct D14 support inequality

Let D be a 3-point core support class of owner multiplicity m among the low clique C.

Let `O_D` denote the weighted incidences from the other low owners in C into D, so total C--D target incidence is

`3m+O_D`.

The induced 14-set `B union D` has edge count

`(55-nu_Y) + (3m+O_D) + e_F(Y,D) + e_H(D)`.

Applying `D(14)=69` gives the correct inequality

> `3m + O_D + e_F(Y,D) + e_H(D) <= 14 + nu_Y`.             (D14-K2)

This is the valid c=8 far-K2 D14 interface.

## 4. Invalid shortcut

Several recent far-K2 files instead state that

`{p} union C union F`

is a target K11 and use

`3m + O_D + e_F(F,D) + e_H(D) <=14`.

That base assertion contradicts the master shell ledger, which explicitly contains all `2|C|` C--F missing edges.

Therefore any proof step whose load-bearing estimate is the latter inequality must be re-audited or rebuilt from (D14-K2).

## 5. Unaffected interfaces

This correction does not affect results derived without the false K11 base, including:

- `Q36_F2_SHELL_LEDGER_REDUCTION.md`;
- the cluster/f=2 structural partition itself;
- exact d2/d3 repivot formulas from the master ledger;
- the far-K2 global fact that a d2 row forces `a_F=0` and a pure K2 support;
- row-closure and overlap identities;
- CORE211 `sum kappa=2`;
- inherited D(14)=69 itself.

Any stronger far-K2 c=8 closure must now cite this corrected D14 interface or avoid D14 entirely.

## 6. Clique-contract correction

The legal parent contract has `omega<=11`; it does **not** impose target K4-freeness. Any far-K2 proof using a target K4 as an immediate contradiction is invalid unless a separate local theorem forbids that particular K4.

This audit is the canonical scope boundary for further far-K2 work.