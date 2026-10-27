# E408 Q32 — independent 285-edge terminal

Updated: 2026-10-27  
Status: **OPEN overall; every nonfull support v=44,45,46 is PROVED_CONDITIONAL impossible. Sole surviving support size: v=47.**

## 1. Frozen Q32 contract

\[
|V(H)|=47,\quad e(H)=285,\quad \alpha(H)\le4,\quad\delta(H)\ge12,
\quad\sum_{x\in H}(d_H(x)-12)=6.
\]
The shell parameter is \(q=32\), equivalently \(e(M)+G_A=32\). Under the registered seven-block equality and exact-129 Type-I factorization, \(m\in\{8,9,10\}\) non-target colors are exact-129.

No Q33 284-edge identity is imported.

## 2. Retained support floor

The read-only Q32 sibling workstream proves
\[
|U|\ge44
\]
for the union U of all exact-color single-outside K5 core K4 witnesses. The exact 285-edge capacity ledger is
\[
6N\le\binom v2-p_4(47-v)-12v+285-E_U.
\]

This scalar inequality is not itself the terminal closure.

## 3. Global exceptional-vertex injectivity

`Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md` proves that no residual vertex can be the Kang--Pikhurko Type-I exceptional vertex for two distinct exact-129 colors.

For any residual vertex v, exact colors contribute degree at least \(4m+5n_v\), where \(n_v\) is its exceptional multiplicity. A deletion-Turan argument forces the combined nonexact degree floor
\[
B_8=6,\qquad B_9=3,\qquad B_{10}=1.
\]
Together with target degree at least 13 and total degree 60, this gives \(n_v\le1\) for all \(m=8,9,10\).

This injectivity closes v=44 directly when combined with the sibling triple-pair theorem, but a stronger theorem below eliminates all three nonfull supports at once.

## 4. Uniform nonfull-support exclusion

`Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md` proves:
\[
\boxed{U=H.}
\]
Equivalently, no support size \(v=44,45,46\) is realizable.

### Proof interface

Fix \(w\in H\setminus U\). For every exact-129 color C, the Type-I factorization and shell-support classification are exhaustive. Since w is not contained in any selected single-outside K5 core witness, exactly one of the following holds:

1. \(w=x_C\), the exceptional degree-nine vertex of color C; or
2. w lies in the core part of the unique multi-outside K5 of color C.

By global exceptional injectivity, case 1 can occur for at most one exact color.

For every other exact color, w lies in a multi-outside K5. In the registered Q32 Type-I classification the additional outside-H vertices of that K5 are shell vertices in A; pivot p cannot co-occur with a shell vertex in a non-target K5 because all p--A edges have the target color. Therefore w has at least two distinct C-neighbors in the 13-point shell A.

Edges of two distinct non-target colors cannot coincide. Thus the shell-neighbor sets contributed by different exact colors are disjoint, and w would require at least
\[
2(m-1)\ge 14
\]
distinct neighbors in A. But \(|A|=13\). Contradiction.

Hence \(H\setminus U=\varnothing\), proving U=H.

This argument uses only the 285-edge Q32 Type-I/shell contract plus exceptional injectivity; no Q33 284-edge statement is imported.

## 5. Consequence: unique surviving terminal is full support v=47

The entire Q32 support frontier is now
\[
\boxed{|U|=47,\qquad W=\varnothing.}
\]

The former separate v=44 proof `Q32_V44_EXCEPTIONAL_DEGREE_CLOSURE.md` remains valid but is subsumed by the stronger nonfull-support theorem. The v=45 reduction is also superseded as a frontier description.

At full support,
\[
e(\overline H)=\binom{47}{2}-285=796.
\]
If exact colors are classified into shell-support types A/B/C with counts a,b,c, where A/C supply eleven single-outside K5 witnesses and B supplies ten, then
\[
a+b+c=m,
\]
and the selected component-witness count is
\[
N=11m-b.
\]
Their edge-disjoint K4s consume
\[
6N=66m-6b
\]
non-target core edges. The exact omitted-point incidence total across H is
\[
3a+7b+3c=3m+4b.
\]
These identities are the starting ledger for the remaining v=47 attack; they are not yet a contradiction.

## 6. Current full-support attack

The remaining proof must combine at least one genuinely global structural input with the full-support ledger. The present high-leverage interfaces are:

1. the exact 37-edge surplus over the eleven-color Turan floor on H:
   \[
   796-11p_{12}(47)=796-11\cdot69=37;
   \]
2. Type-I shell patterns: type B costs at least two extra H-edges above 69, type C at least three, while type A is at the 69-edge floor;
3. shell missing-edge budget \(e(M)+G_A=32\), including at least two shell missing edges per non-target color and at least three for each type-C exact color;
4. seven-block blocker coupling and good-component labels from the Q32 sibling workstream;
5. the exact per-vertex omission / leftover-complement degree identities induced by the full witness packing.

A scalar table satisfying these inequalities is not a graph realization and is not promoted to closure.

## 7. Scope firewall

Source Q32 branch: `workstream/r12-e408-q32-excess6-20261025` at `a0ba6db26c7e8b00a4217dcbcbf298895dff93ce`.

The Q33 31-point/56-witness closure and the unified 284-edge support-41 theorem are not used. EG617(r=12) remains **OPEN / NOT_CERTIFIED** until the v=47 Q32 terminal and the other upstream/backend branches are closed.