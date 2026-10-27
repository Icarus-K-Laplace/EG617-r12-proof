# Contract firewall: Q33 versus Q32

Updated: 2026-10-27

## Q33: 284-edge core

All Q33 support-31 statements assume:
- |V(H)|=47, e(H)=284, alpha(H)<=4, delta(H)>=12;
- total degree excess sum_H(d_H-12)=4;
- the registered 61-point target residual and seven-block equality ledger;
- exact-129 Type-I/component factorization under its named external extremal input;
- the registered 31-point/56-witness terminal when the U-edge reserve theorem is invoked.

The local P_C=49 profile files use additional row/gadget contracts. The global theorem `Q33_NONEXACT_U_RESERVE_CLOSURE.md` does not need a colorwise P_C<=48 result and bypasses the two remaining local P_C=49 all-component-edge-present profiles.

The Q33 closure uses no 285-edge Q32 capacity identity.

## Q32: 285-edge core / E408 residual

All Q32-labelled support statements assume:
- |V(H)|=47, e(H)=285, alpha(H)<=4, delta(H)>=12;
- total degree excess sum_H(d_H-12)=6;
- q=32, equivalently e(M)+G_A=32, when shell/support statements are invoked;
- the registered E408 Q32 seven-block/exact-129 Type-I contract.

The support floor |U|>=44, nonfull-support closure U=H, and v=44/45 reductions are Q32-only and are not transferred to Q33.

### Stronger Q32 terminal theorem has a smaller load-bearing contract

`Q32_EXACT_COLOR_COUNT_COLLAPSE.md` closes the registered Q32 residual without using the 285-edge support-size split. Its load-bearing inputs are:

1. the E408 residual color ledger
   e_C(R)=129+s_C, s_C>=0, sum_C s_C=3;
2. exact-129 Type-I degree structure: one degree-nine exceptional vertex, every ordinary residual vertex degree at least four;
3. `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
4. full-color pointwise floors: s=1 gives degree at least3; s>=2 gives degree at least2;
5. alpha(C)<=12 and omega(C)<=5 for non-target residual colors;
6. the Brouwer/Kang--Pikhurko non-r-partite Turan bound in complement form;
7. target residual minimum degree13 and the 12-color partition of the 60 incident edges at every residual vertex.

It does **not** use:
- any Q33 284-edge formula;
- support-41;
- an M[B]=empty shell split;
- the Q32 capacity inequality;
- SAT/ILP nonexistence.

Therefore the Q32 contradiction is logically independent of the Q33 U-edge reserve contradiction.

## Outer incidence notation

For each non-target color C:
\[
e_C(R)=129+s_C,\quad s_C\ge0,\quad \sum_Cs_C=3.
\]
The registered duplicate identity is
\[
P_C+R_C+s_C=62.
\]
For an exact-129 color, s_C=0, so P_C+R_C=62. P_C is the block-block duplicate budget and R_C the block-to-residual duplicate budget. Baseline color edges are not added to P_C.

The seven entries r_i(C) are block-to-residual budgets summing to R_C; they are not the 21 block-pair duplicate incidences.

## Witness distinctions

Keep separate:
1. the 56 labelled independent four-set witnesses on the Q33 support-31 terminal;
2. the Q33 component versus gadget witness distinction used in U-edge reserve counting;
3. the Q32 ten-or-eleven core witnesses per exact color in the 285-edge support theorem;
4. the unified support-41 284-edge/ten-color witness family;
5. the size-five blocker occurrences M_C in the outer seven-block ledger.

A theorem for one family cannot be transferred to another without a proved map. The final Q32 exact-color-count contradiction does not require any witness-family transfer.

## Star-capacity rule

For a C-colored K12 Q and an outside vertex z, the valid consequence is
\[
d_C(z,Q)\le1.
\]
One external C-edge is permitted. A contradiction requires at least two C-edges from the same outside vertex into the same Q. The withdrawn stronger external-isolation claim is not used by either final E408 closure.

## External extremal theorem firewall

The Brouwer/Kang--Pikhurko input is used only after checking:
- the complement is K_{r+1}-free because the original graph has alpha<=r;
- it is non-r-partite because r-partiteness would create an independent set of size at least ceil(n/r)>5 in the complement, i.e. a clique of size at least6 in the original graph;
- the parameter range n>=2r+1 is satisfied in the uses (58,11), (57,11), and (53,10).

Under those conditions the complement bound is
\[
e(\bar G)\le t_r(n)-\lfloor n/r\rfloor+1,
\]
equivalently
\[
e(G)\ge p_r(n)+\lfloor n/r\rfloor-1.
\]

## Promotion rule

- PROVED: all hypotheses are stated and the proof is analytic.
- PROVED_CONDITIONAL: complete derivation under named retained inputs.
- COMPUTATION_CERTIFIED: exact verifier coverage/output only.
- OPEN: no complete exclusion.
- RETRACTED: a discovered invalid inference.

Current promotion:
- registered E408 Q33 terminal: PROVED_CONDITIONAL impossible;
- registered E408 Q32 terminal: PROVED_CONDITIONAL impossible;
- original EG617(r=12): OPEN / NOT_CERTIFIED, because E407 and upstream/backend bridge obligations remain outside this workstream.
