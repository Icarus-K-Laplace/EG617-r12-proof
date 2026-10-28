# E408-Q32 retraction firewall

Date: 2026-10-28
Status: **ACTIVE / FAIL-CLOSED**

This workstream may not use any theorem whose load-bearing proof depends on the withdrawn universal KP degree-nine exceptional vertex or the derived exceptional-point injectivity.

## 1. Primary source correction

The source-correct exact-129 Type-I graph is

`10 isolated K5 dot-union G11`.

For source parameter `a in {1,2,3,4}`, the two variable gadget degrees are

`4+a` and `9-a`,

i.e. `(5,8),(6,7),(7,6),(8,5)`.

Therefore there is **no universal degree-nine exceptional vertex**.

The valid consequences retained in this workstream are the factorization, twelve K5 partition after deleting x, the exact nine gadget edges, and arguments re-derived directly from those statements.

## 2. Forbidden historical claims

The following may be read only as historical artifacts and may not be cited as active closure lemmas:

- `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
- `Q32_EXACT_COLOR_COUNT_COLLAPSE.md`;
- the injectivity-dependent closure portion of `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md`;
- `E408_WHOLE_LAYER_EXACT_COUNT_CLOSURE.md` as a Q32 whole-layer theorem;
- any root promotion that cites those results as closing E408-Q32;
- old `Q32_V45_TWOPOINT_REDUCTION.md` conclusions such as “at most three 11-witness colors” or “at most one exceptional outside H” when their proof uses exceptional injectivity.

A verifier script attached to a retracted statement does not revive the statement.

## 3. Explicitly invalid root-promotion artifact

`R12_ROOT_CLOSURE_PROMOTION_AUDIT.md` predates the fail-close and contains the withdrawn Q32 closure route. It must not be used for current status.

The newer `ROOT_PROMOTION_RECEIPT.md` is the controlling branch-local root receipt. It explicitly withdraws the old promotion and sets

`EG617(r=12) = OPEN / NOT_CERTIFIED`.

## 4. Safe replacements already used here

The following deductions were re-derived from source-correct Type-I structure and current minimum-degree theorems:

1. corrected non-full-support multiplicity
   `n_w>=m-6`;
2. latest nonexact degree floors
   `L8=12`, `L9=7`, `L10=3`;
3. m=8 exact parameters satisfy `a in {2,3}` from the exact three-unit pointwise surplus ledger;
4. in m=8 all variable points `{x_C,y_C}` are pairwise distinct;
5. Case-II v=45,m=8 and v=46,m=8 are closed by weighted special-incidence capacity, not by historical injectivity;
6. v=47 exact-color H-edge normal forms and the 69/70 near-Turan analysis use only the true Type-I factorization.

## 5. E407 firewall

The E407 U-reserve contradiction is allowed because its load-bearing inputs are:

- V12 survivor exhaustiveness under retained screen assumptions;
- the common `|U|=29`, 49-block support contract;
- selected-component color identity;
- edge uniqueness;
- `alpha(D)<=12`;
- Turan.

It does **not** use universal degree9 or exceptional injectivity.

The fact that the frozen five-template compatibility file was still OPEN is not a defect in this later closure: the U-reserve theorem bypasses template-by-template incompatibility once the common support contract is available.

## 6. Q33 firewall

The Q33 global nonexact-U-reserve route is allowed. It depends on the 284-edge / 31-point / 56-witness contract and component/gadget distinction, not on the false degree-nine statement and not on the Q32 excess-six identities.

## 7. Fail-closed policy for new work

For every proposed Q32 lemma:

- identify whether x, y, or a generic G11 vertex is being used;
- if a degree is used, derive it from `(4+a,9-a)` or the fixed degree-five gadget vertices;
- never infer uniqueness merely from the label “exceptional”;
- distinguish residual degree from H-degree and shell degree;
- distinguish a chosen ten-witness family from all possible single-outside K5 witnesses;
- do not transfer an E407 excess-four identity to the E408 285-edge excess-six core;
- if a source statement cannot be matched exactly, mark the dependent result OPEN rather than interpolating it.

Root promotion stays disabled until this firewall is satisfied by every Q32 closure row.

## 8. Support-exhaustiveness audit gate (added 2026-10-28)

Local U-reserve arithmetic must be kept separate from the theorem that all parent completions enter the U-contract.

- **E407 Q32:** `E407_FOUR_COLOR_U_RESERVE_CLOSURE.md` validly excludes the frozen V12 `|U|=29`, 49-block contract by `294 + p_12(29)=316 > 310`. Its parent-level use remains conditional on V12 survivor exhaustiveness and the selected-component identity. The dedicated E407 branch still has a stale OPEN canonical/proof-audit snapshot; reconcile that branch state before treating the root gate as unconditional.
- **E408 Q33:** `Q33_NONEXACT_U_RESERVE_CLOSURE.md` validly excludes the frozen `|U|=31`, 56-witness contract by `26(11-m) <= delta+6h <= 41`, while m=8,9 require 78 or52. The inspected witness-packing source gives a support lower bound, not equality by itself. The root receipt asserts an upstream exhaustive reduction, but its exact source path was not identified in this pass. Until that source is linked and checked, Q33 parent-level exhaustion remains conditional.
- **E408 Q32:** the new pivot-neighborhood packing theorem is valid as a structural reduction. Its scalar slack system has feasible states and is not an UNSAT certificate.

Accordingly, the root DAG must preserve the exact conditional premises above and must not turn a support-boundary contradiction into a whole-parent closure without an exhaustive bridge.

## 9. New v47 high-support local lemmas — firewall check (2026-10-28)

The 2+8 two-block transversal blocker and the 3+7 double-track fiber cap use only:
- the source-correct 4,5,5 matching-switch classification;
- the already-proved zero-slack map alignment;
- `alpha(H)<=4`, `Delta(H[R])<=2`;
- the pointwise degree ledger `e_Q(q)+d_R(q)=3);
- the endpoint-load identity for small blocks.

They do not invoke the retracted universal KP degree-nine statement, exceptional-point injectivity, the E407 excess-four identity, or the Q33 284-edge identity. The singleton/triangle exception in the 2+8 double-track case is explicitly preserved. Root status remains OPEN / NOT_CERTIFIED.
