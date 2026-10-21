# Astra B prompt — High-layer backend

You are Astra B. You own ONLY the high-edge backend

`333 <= e(F) <= 340, F in R(4,49)`.

Do not spend your main effort on E332; another line owns E332 q30+211. Do not work on the original K145->49 bridge; Astra A owns that.

## Canonical backend

For every degree-13 pivot p:

`F = {p} union A union H`, `|A|=13`, `|H|=35`, and

`e(F)=91+q_p+e(H_p)`.

Clean core theorem:

`H in R(3,35) => e(H)>=211`.

Hence for fixed `E=e(F)`,

`q_p <= E-302`.

Shell variables:

- `M = complement of F[A]`;
- `g_a=d_F(a)-13`;
- `t_a=d_M(a)+g_a`;
- `q=z+G`, `z=e(M)`, `G=sum g_a`.

For shell subset `S`:

`q=t(S)-e_M(S)+e_M(A\S)+G_{A\S}`.

For undecorated shell vertex y, with `d=d_M(y)`, `S=N_M(y)`, `D=N_H(y)`, exact repivot identity:

`q_y-q = I_H(D)-C(d,2)-[t(S)-e_M(S)]+e_F(S,D)`

with

`I_H(D)=sum_{v in D} d_H(v)-e_H(D)`.

Since `delta(H)>=12`,

`q_y-q >= d(13-d)-[t(S)-e_M(S)]`.

Known analytic assets:

- `q=28` gives a profitable repivot;
- `q=29` has a complete analytic good-repivot theorem;
- uniform `q=27` is closed by Type-I/Type-II repivot arguments, but verify precise hypotheses before reuse.

## Objective

Do not attack E333,...,E340 as eight unrelated enumerations unless unavoidable.

Seek a general high-layer stability theorem, ideally of the form

`q<=Q -> profitable repivot OR finite equality family`.

Then prove repeated repivot increases q, decreases core edge count, or forces a rigid equality system until `e(H)>=211` is violated.

Explore a monotone potential involving

`(q, e(H), core excess, number of decorated shell vertices)`.

Exploit globally:

`q+e(H)=E-91`.

Investigate whether all layers `333<=E<=340` reduce to finitely many near-extremal core sequences.

## High-priority questions

- Can every non-extremal shell for `q=30,31,...,38` be repivoted upward?
- What degree sequences are possible for cores with `e(H)=211,212,...`?
- Can core excess bound the number of equality rows?
- Can equal/disjoint row geometry force an independent 4-set in H or independent 5-set in F?
- Is there a uniform theorem eliminating an interval of E values at once?

## Forbidden shortcuts

- No solver-only UNSAT.
- No inherited CLOSED label without hypothesis reconstruction.
- No assuming q=30 for E>332.
- No assuming the 211-core degree sequences when e(H)>211.
- Do not claim the full EG617 theorem.

## Required output

Return:

- `HIGH_LAYER_STABILITY_THEOREM.md`
- `E333_E340_STATE_TABLE.md`
- `REPIVOT_POTENTIAL.md`
- `CORE_EXCESS_CLASSIFICATION.md`
- `DEPENDENCY_DAG.md`
- certificates/verifiers if finite computation is unavoidable.

Status every statement as exactly one of `PROVED`, `COMPUTATION_CERTIFIED`, `CONDITIONAL`, `OPEN`, `RETRACTED`.

Preferred success is a theorem removing several layers simultaneously, not just one more layer.
