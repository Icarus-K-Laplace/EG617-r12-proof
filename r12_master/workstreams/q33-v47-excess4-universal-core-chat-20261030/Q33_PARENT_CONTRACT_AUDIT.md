# Q33 parent-contract audit — source-complete minimum-degree promotion

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL contradiction for the E408 / Qmax=33 parent class**. The local 47/284 graph theorem and its minimum-degree source are PROVED.

## 1. Read-only parent freeze

- Global E408 root branch: workstream/r12-twochat-e408-global-20261026, HEAD b0459807acd4b7e386148056ddf77d7998918893.
- Q33 support-promotion sibling: workstream/r12-q33-support-promotion-20261030, HEAD ca088347124f4ea7706a63129d7ed63d4e4090d7.
- This isolated audit branch is workstream/r12-q33-v47-excess4-universal-core-attack-20261030.
- All parent and sibling sources are read-only. All writes remain under this workstream's directory.

## 2. Exact E408/Q33 parent contract

The E408 parent source is front_end/E408_Q33_CORE_ALMOST_REGULAR_NORMAL_FORM.md. Its target residual F is an induced 61-vertex h13 T61 residual with
\[
e(F)=408,\quad \delta(F)=13,\quad \alpha(F)\le5,\quad\omega(F)\le11.
\]
Because F is induced in the least-edge target color graph, it inherits every cap
\[
e(F[U])\le D(|U|).
\]
This follows from the front-end bridge's balanced-color argument: each of the other eleven colors has independence number at most12 on every vertex subset and hence at least p12(|U|) edges there.

The Q33 charge branch is the case
\[
Q=\max\{q_p:d_F(p)=13\}=33.
\]
Thus at least one degree-13 pivot p has q_p=33. This is the only pivot existence statement used here; no selected 31-point witness support is assumed.

## 3. Exact pivot-to-core identity

For a degree-13 pivot p, let A=N_F(p), |A|=13, and
\[
H=F[V(F)\setminus(A\cup\{p\})].
\]
Then |V(H)|=61-13-1=47.

Let M be the missing-edge graph of F[A], let z=e(M), let g_a=d_F(a)-13>=0, and let t_a=|N_F(a)\cap V(H)|. Since F[A] has 78-z edges,
\[
t_a=d_M(a)+g_a,\qquad
\sum_{a\in A}t_a=2z+\sum_{a\in A}g_a.
\]
The exact disjoint edge partition is
\[
e(F)=13+(78-z)+\sum_{a\in A}t_a+e(H)
=91+q_p+e(H),
\]
where q_p=z+sum_A g_a. At q_p=33,
\[
\boxed{e(H)=408-91-33=284.}
\]

## 4. All five 47-core hypotheses are now sourced

| Hypothesis | Derivation | Status |
|---|---|---|
| |V(H)|=47 | Delete p and its 13-neighbourhood | **PROVED** |
| e(H)=284 | Exact pivot identity at q_p=33 | **PROVED** |
| alpha(H)<=4 | An independent 5-set in H plus p would be independent 6 in F | **PROVED** |
| omega(H)<=11 | H is induced in F | **PROVED** |
| delta(H)>=12 | H belongs to R(4,47), e(H)=284<=286; apply MINDEG12_47_SOURCE_COMPLETE_AUDIT.md | **PROVED** |

The density caps required by R(4,47) are inherited because H is induced in F. This discharges the former V11 minimum-degree source gate without using V11.

## 5. Contradiction and promotion

The independent universal theorem Q33_UNIVERSAL_284_NONEXISTENCE.md proves that no simple graph H satisfies
\[
|H|=47,\quad e(H)=284,\quad\delta(H)\ge12,\quad
\alpha(H)\le4,\quad\omega(H)\le11.
\]
Sections 2–4 supply all five hypotheses. Therefore the assumed E408 Qmax=33 parent cannot exist.

\[
\boxed{\text{E408 / Qmax=33 is PROVED_CONDITIONAL impossible}}
\]
under the explicit E408 h13 parent contract and the front-end hereditary density caps.

This contradiction is independent of the exact 31-point / 56-witness support promotion. The Q33 support-promotion branch's larger-v scalar/profile frontier is bypassed: any q=33 pivot already yields the forbidden 47/284 core.

## 6. Firewall and global status

- No Q32 285-edge / excess-six result is used.
- No V11 theorem or V11 minimum-degree statement is used.
- No Kang–Pikhurko theorem is used by the minimum-degree or universal-core proofs.
- No degree-nine exceptional-vertex assertion is used.
- No global canonical file or sibling branch is modified.

This closes only the E408 Qmax=33 charge layer. The E408 Q31 and Q32 layers retain their own dependencies; the root problem EG617(r=12) remains OPEN / NOT_CERTIFIED until every other live branch and the global front-end dependency chain are closed.
