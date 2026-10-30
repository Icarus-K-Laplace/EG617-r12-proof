# Strict 285-edge floor for the hereditary 47-point class

Date: 2026-10-30  
Status: **PROVED** for the exact hereditary-cap class R(4,47).

## 1. Theorem

Let R(4,47) be the class of simple 47-vertex graphs J satisfying
\[
\alpha(J)\le4,\qquad\omega(J)\le11,\qquad
e(J[U])\le D(|U|)\quad\forall U\subseteq V(J),
\]
where D(n)=binom(n,2)-11p_12(n) and p_12(12q+r)=12binom(q,2)+qr.

Then
\[
\boxed{J\in R(4,47)\Longrightarrow e(J)\ge285.}
\]

This strengthens the retained 284-edge floor by one.

## 2. Dependency 1: the 284-edge floor

The audited private-clique argument in the retained source CORE_FLOOR_284_PROOF.md establishes
\[
e(J)\ge284\quad\text{for every }J\in R(4,47).
\]
Its lower-order inputs are proved in MINDEG12_47_SOURCE_COMPLETE_AUDIT.md:
- R(2,24) is empty;
- delta(R(3,35))>=12, using the complete 121/122-edge triangle-free neighbourhood classification and D(14),D(23);
- delta(R(3,36))>=13;
- R(3,37) is empty;
- degree 10 in R(4,47) forces e>=289;
- degree 11 forces e>=287;
- the only remaining e=282,283 cases are excluded by the private-clique lemma.

The b=3,4 weighted-transversal part of that private-clique lemma uses the 127-row exact rational certificate. Both original Fraction verifiers and the source arithmetic supplement were rerun; see CLEAN_ROOM_REPLAY_20261030.md.

Thus e(J)>=284 is a proved input, not an assumed edge floor.

## 3. Dependency 2: equality e=284 is impossible

Assume e(J)=284. Then e(J)<=286, so the source-complete minimum-degree theorem gives
\[
\delta(J)\ge12.
\]
The universal 284-edge theorem independently proves that no 47-vertex graph can simultaneously satisfy
\[
e(J)=284,\quad\delta(J)\ge12,\quad
\alpha(J)\le4,\quad\omega(J)\le11.
\]
Every J in R(4,47) has the last two graph restrictions, so this is a contradiction.

Therefore equality in the 284-edge floor is impossible:
\[
e(J)\ne284.
\]

Combining with e(J)>=284 gives e(J)>=285.

## 4. E408/h13 parent consequence

For the exact E408/h13 parent F, every degree-13 pivot p gives an induced core
\[
H_p=F[V(F)\setminus(N_F(p)\cup\{p\})]\in R(4,47).
\]
The membership follows from alpha(F)<=5 (p is anticomplete to H_p), omega(F)<=11, and inheritance of all D-caps.

The exact pivot identity is
\[
408=91+q_p+e(H_p).
\]
By the strict floor just proved, e(H_p)>=285 for every legal degree-13 pivot. Consequently
\[
\boxed{q_p\le408-91-285=32}
\]
for every such pivot, and hence
\[
\boxed{Q_{\max}\le32.}
\]

This is stronger than merely ruling out a selected q_p=33 pivot. It closes the whole E408/Qmax=33 layer and removes the need for the 56-witness support-promotion route at that layer.

## 5. Exact dependency boundary

- 284-edge floor: PROVED; uses the retained private-clique proof and its 127-row rational certificate.
- Minimum-degree gate e<=286 => delta>=12: PROVED; independent of the 127-row certificate and independent of V11.
- Universal 284-edge nonexistence: PROVED; no hereditary density caps required by this local theorem.
- Strict 285-edge floor: PROVED for R(4,47), by combining the three preceding results.
- E408/h13 Qmax<=32: PROVED_CONDITIONAL under the exact T61 parent contract from the front-end bridge.
- E408/Qmax=32, E407/Q32, and the original K145-to-T61 parent bridge: OPEN / NOT CLOSED by this theorem.

No Q32 proof is imported or attempted in this workstream.
