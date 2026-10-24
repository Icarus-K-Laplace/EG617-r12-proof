# General-r Repivot Potential Status

Status: PARTLY PROVED SYMBOLIC; global termination OPEN.

## 1. Proven symbolic two-coordinate potential

Under the general backend setup define

- `q_p=e(M_p)+G_(A_p)`;
- `X={v:d_F(v)>r+1}` globally;
- `tau_p=|A_p intersect X|`.

For a legal regular repivot p->y, direct set transport gives

> **`tau_y-tau_p=|D_y intersect X|-|S_y intersect X|`.**

Together with the symbolic q-exchange formula, this makes

> **`Psi_r^(2)(p)=(q_p,tau_p)`**

a genuine bounded lexicographic potential on the finite set of legal regular pivots.

Thus one may always choose a pivot maximal first in q and then in tau.

## 2. Proven strict-loss consequence

Suppose a support class D is repeated by at least two owners. Then every point of D is globally decorated by the owner incidences.

If the corresponding shell missing set S is not fully decorated, i.e.

`|S intersect X|<|D|`,

then a same-q repivot through D would satisfy

`tau_new-tau_old=|D|-|S intersect X|>0`.

Therefore tau-maximality forbids a repeated plateau support. Symbolically:

> **every repeated non-fully-decorated support has q-loss at least one.**

This is the all-r source of the r=12 repeated-support strict-loss bridge.

## 3. What is not proved

No theorem currently shows that every non-rigid configuration has a legal repivot which strictly increases `(q,tau)`.

Higher-slack equality states can preserve both coordinates while transporting defect between shell and core.

Thus `(q,tau)` is a real potential but not yet a complete termination potential.

## 4. Candidate extension

The natural third coordinate should be built from the exact nonnegative transport variables, for example a lexicographic refinement involving

- total positive transport slack `sum sigma_s`;
- zero-signature diversity;
- repeated-row energy `sum_C binom(mult(C),2)`;
- anchor deficit / low-excess concentration.

The desired theorem is not to guess a scalar formula but to prove:

> if q and tau are both unchanged under every legal repivot, then the transported defect system must collapse into the anchor or sunflower rigidity branch.

This is the precise symbolic termination gap.
