# Q33 parent source map and root-import boundary

Date: 2026-10-30  
Read-only parent branch: workstream/r12-twochat-e408-global-20261026  
Read-only parent HEAD: b0459807acd4b7e386148056ddf77d7998918893

## 1. Parent source files actually checked

1. front_end/FRONTEND_BRIDGE_THEOREM.md, especially F7/F8 and the T61 terminal interface.
2. front_end/E408_Q33_CORE_ALMOST_REGULAR_NORMAL_FORM.md.
3. front_end/T61_H13_V11_SOURCE_AUDIT.md.
4. r12_master/workstreams/twochat-e408-global-20261026/ROOT_DEPENDENCY_DAG.md.

The root dependency DAG was read-only throughout. Its E408-33-PROMOTION row was OPEN at the audited parent HEAD because the 56-witness support route did not yet cover all support sizes. This workstream supplies a different route: the entire 47-point 284-edge core is forbidden, so no witness-support case split is needed once the Q33 parent contract is reached.

## 2. Exact parent contract from the front-end bridge

The T61 terminal interface in FRONTEND_BRIDGE_THEOREM.md gives an induced residual F with:
\[
|V(F)|=61,\quad \alpha(F)\le5,\quad\omega(F)\le11,
\]
all inherited induced-density caps
\[
e(F[U])\le D(|U|)\quad\text{for every }U\subseteq V(F),
\]
and actual minimum degree h=12 or13. The E408 / h13 branch fixes
\[
e(F)=408,\qquad \delta(F)=13.
\]

These are parent assumptions conditional on the front-end bridge's hypothetical balanced-colouring reduction. The present workstream does not promote that original K145 bridge to unconditional proof.

## 3. Exact pivot ledger

Choose any degree-13 pivot p in F and let A=N_F(p), |A|=13. Put
\[
H=F[V(F)\setminus(A\cup\{p\})].
\]
Then |V(H)|=61-13-1=47.

Let M be the missing-edge graph of F[A], z=e(M), g_a=d_F(a)-13>=0, and t_a=|N_F(a)\cap V(H)|. Since d_F(a)=13,
\[
t_a=d_M(a)+g_a.
\]
The disjoint edge partition is
\[
e(F)=13+(78-z)+\sum_{a\in A}t_a+e(H)
=91+z+\sum_{a\in A}g_a+e(H).
\]
Writing q_p=z+\sum_a g_a gives
\[
\boxed{408=91+q_p+e(H).}
\]
Thus, whenever a legal degree-13 pivot has q_p=33,
\[
\boxed{e(H)=284.}
\]

This is the exact identity recorded in E408_Q33_CORE_ALMOST_REGULAR_NORMAL_FORM.md; no Q32 identity is imported.

## 4. The five forbidden-core hypotheses

- |V(H)|=47: exact pivot deletion.
- e(H)=284: exact identity above at q_p=33.
- alpha(H)<=4: p is anticomplete to H; an independent 5-set in H plus p would violate alpha(F)<=5.
- omega(H)<=11: H is induced in F.
- inherited D-caps: H is induced in F, and every F[U] has the parent D-cap.

Therefore H belongs to the exact class R(4,47) defined in MINDEG12_47_SOURCE_COMPLETE_AUDIT.md. Since e(H)=284<=286, the source-complete minimum-degree theorem gives delta(H)>=12. The universal 284-edge theorem then gives a contradiction.

## 5. Logical status and precise conclusion

**PROVED:** no 47-vertex graph satisfies
\[
e(H)=284,\quad\delta(H)\ge12,\quad\alpha(H)\le4,\quad\omega(H)\le11.
\]

**PROVED:** every J in the explicitly defined hereditary-cap class R(4,47) with e(J)<=286 has delta(J)>=12.

**PROVED_CONDITIONAL:** under the actual E408/h13 T61 parent contract, no degree-13 pivot can have q_p=33. In particular, the E408 maximum-charge case Q_max=33 is impossible when Q_max is defined as the maximum q_p over the legal degree-13 pivots.

This argument bypasses the 56-witness support-promotion route entirely. It does not assume support size 31, 32, ..., 47; it does not use the m=8,9,10 nonexact-color reserve; it does not use exact-129 factorization; and it does not use the Q32 285-edge theorem.

## 6. Root import request — not applied here

At the read-only parent HEAD, ROOT_DEPENDENCY_DAG.md still records E408-33-PROMOTION as OPEN. A root maintainer should reconcile this branch's proof into that row and remove the now-redundant support-promotion obligation for the q_p=33 terminal, after checking the exact parent contract and this workstream's dependency receipt.

This workstream has not edited:
- ROOT_DEPENDENCY_DAG.md;
- ROOT_PROMOTION_RECEIPT.md;
- CANONICAL_STATE.md on the global root branch;
- any sibling Q32/Q33 workstream.

The global EG617(r=12) theorem remains OPEN / NOT_CERTIFIED because E408 Q32, E407 Q32, the R(4,49) front-end alternative, and their parent-coverage edges remain separate live obligations.
