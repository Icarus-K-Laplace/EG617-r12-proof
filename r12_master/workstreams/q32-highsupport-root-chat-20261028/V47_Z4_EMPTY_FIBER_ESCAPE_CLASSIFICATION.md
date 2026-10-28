# E408 Q32 — z=4, 3+7 empty-fiber escape classification

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL necessary reduction; no Q32 closure claimed.**

## 1. Contract

Work in the full-support m=10 disconnected 3+7 light-block cell. The already-registered ledger gives:
- `e(H[R])=3+z), `x_T=3+z), `y=8-2z);
- `t_D+y_D=2) for each of the seven outer blocks D;
- `sum_D y_D=y), `sum_D t_D=2x_T);
- each small block A,B,C has endpoint loads `e_i(h)>=3-n_h), with total slack two;
- the three small-block zero-slack maps coincide, and every singleton common-track vertex q of label h meets all of F_h.

Suppose z=4. Then `e(H[R])=7), `x_T=7), and y=0, so `y_D=0) and `t_D=2) for every outer block. Every r in R has exactly one neighbor in each outer block.

## 2. Fiber partition with an empty label

The residual graph H[R] is either C7 or C3 dot-union C4. If the common zero-slack map has fiber sizes `(3,2,2,0)), the empty label is h=0 and
[
e_A(0),e_B(0),e_C(0)\ge3,
qquad E_0:=e_A(0)+e_B(0)+e_C(0)\ge9.
]
There are exactly 21 small-to-outer extra edges in total, three per outer block.

## 3. No all-aligned singleton completion

**Lemma 3.1.** It is impossible that all seven outer blocks are in the aligned normal form and every outer vertex has a singleton common-track intersection.

**Proof.** In each outer block D, the four common-track labels are then a permutation of 0,1,2,3. Let q_0(D) be the unique vertex with label0. Since F_0 is empty and every other singleton-track vertex q_h(D) is adjacent to all of F_h, while each r has exactly one neighbor in D (because y_D=0), the vertices q_h(D) for h=1,2,3 account for all seven R-neighbors. Hence q_0(D) has no R-neighbor and uses all three units of its degree surplus on extra Q-Q incidences.

An extra edge from small-block label0 cannot end at q_0(D), because the pair graph between that small block and D has exactly one extra edge beyond the base matching, and q_0(D) is already matched to label0. Therefore at most the (21-E_0\le12) extra edges whose small endpoint has nonzero label can land at the seven q_0(D). Let K_0 be this number and T_0 the total weight of heavy Q-Q pairs among outer blocks incident to track0. Since q_0(D) has no R-neighbor and has degree12,
[
K_0+T_0=7\cdot3=21.
]
Thus `T_0>=E_0>=9).

But the total heavy-pair weight among the outer blocks is `x_T=7). Every extra edge between two outer blocks is off the base matching, so an edge can contribute at most once to the track0 incidence sum. Hence `T_0<=x_T=7), contradiction. QED.

## 4. Every escape must involve the empty label

Therefore any valid z=4 completion with fiber sizes `(3,2,2,0)) must contain at least one nontrivial outer block.

- **Switch block:** all common-track intersections are singletons with one label s duplicated. The duplicate-fiber budget gives `n_s<=y_D=0), so the duplicated label must be the empty fiber 0. Thus the switch transposition must involve label0.
- **Aligned double-track block:** the two common tracks have fiber-size sum at most three. For sizes `(3,2,2,0)), the only possible pairs are `(3,0)) and `(2,0)). Thus every double-track block also involves the empty label.

Consequently the only surviving local escape mechanisms in this residual/fiber cell are switch or double-track configurations involving label0. This is a necessary reduction, not a proof that such configurations can or cannot coexist globally.
