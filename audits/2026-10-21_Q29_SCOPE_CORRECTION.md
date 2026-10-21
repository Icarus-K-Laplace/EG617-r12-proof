# q29 theorem scope correction — 2026-10-21

Status: `PROVED` clarification.

The q29 good-repivot theorem must not be stated with an unnecessary hypothesis `e(H)=211`.

Correct scope:

- current pivot has `q=29`;
- the 35-core satisfies the inherited condition `delta(H)>=12`;
- the q29 shell identities / structural constraints hold.

Then there exists an undecorated shell vertex `y` with

`d_F(y)=13` and `q_y>29`.

Equivalently, since q is integral,

`q_y>=30`.

The proof uses the exact repivot identity plus the analytic three-case classification of the missing shell graph. The numerical edge count `e(H)=211` is not part of the existence theorem.

For the specific E331 closure, CORE211 is then invoked separately: every degree-13 pivot in a 331-edge graph satisfies

`q_y=331-91-e(H_y)<=29`,

which contradicts the q29 good-repivot theorem.

Canonical separation:

1. **Q29 Good-Repivot Lemma:** `q=29 + delta(H)>=12 -> exists degree-13 y with q_y>=30`.
2. **E331 Corollary:** fixed total edge count + CORE211 gives `q_y<=29`, hence contradiction.

Future manuscripts and agent prompts must preserve this separation so the q29 lemma remains reusable outside the 211-edge equality-core setting.
