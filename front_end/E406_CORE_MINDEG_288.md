# E406 bridge lemma — 47-core minimum degree through 288 edges

Status: `PROVED` under the inherited T61 / R(4,47) density-cap contract.

## Theorem

Let `C in R(4,47)` be a genuine 47-point core arising in the T61 front end. If

`e(C) <= 288`,

then

`delta(C) >= 12`.

The previously registered generic lemma only covered `e(C)<=286`; this closes the 287- and 288-edge gaps needed by the E406 q28/q27 bridge.

## Proof

Assume for contradiction `delta(C)=11`, and choose a degree-11 pivot `x`.

Let

- `A=N_C(x)`, `|A|=11`;
- `H=C-N_C[x]`, `|H|=35`;
- `M=overline{C[A]}`;
- `g_a=d_C(a)-11`;
- `t_a=|N_H(a)|=d_M(a)+g_a`;
- `q11=e(M)+sum_A g_a`.

Because `x` is anticomplete to H and `alpha(C)<=4`, one has `H in R(3,35)`. Hence modern CORE211 gives

`e(H)>=211`.

Exact counting gives

`e(C)=66+q11+e(H)`.      (1)

Since `omega(C)<=11`, `M` is nonempty: otherwise `{x} union A` is a target K12.

Choose any missing-shell edge `uv in E(M)` and put

`D_u=N_H(u)`, `D_v=N_H(v)`.

If `|D_u union D_v|<=11`, then at least24 vertices remain in `H-(D_u union D_v)`. Since u,v are target-nonadjacent, an independent3-set in that remainder together with u,v would be an independent5-set in C, impossible. Thus that remainder would belong to `R(2,24)`, but `R(2,24)` is empty. Therefore

`|D_u union D_v|>=12`.

Consequently

`t_u+t_v>=12`.      (2)

The exact 11-shell subset identity for S={u,v} is

`q11 = t_u+t_v-1 + e_M(A\{u,v}) + G_{A\{u,v}}`.

Hence from (2)

`q11>=11`.      (3)

### 287 edges

If `e(C)=287`, (1) and CORE211 give

`q11<=287-66-211=10`,

contradicting (3).

Therefore no 287-edge core has minimum degree11.

### 288 edges

If `e(C)=288`, then (1)--(3) force equality everywhere:

`q11=11`, `e(H)=211`,

and for the chosen missing edge

- `t_u+t_v=12`;
- `D_u` and `D_v` are disjoint and `|D_u union D_v|=12`;
- all outside terms in the subset identity vanish.

Put `U=D_u union D_v`, `|U|=12`, and `W=H\U`, `|W|=23`.

Because u,v are target-nonadjacent and `alpha(C)<=4`, W has independence number at most2. Thus `W in R(2,23)` and the proved floor gives

`e(W)>=131`.      (4)

Every H-vertex has degree at least12. Therefore

`e(W)=e(H)-[sum_{a in U} d_H(a)-e_H(U)]`

`<=211-144+e_H(U)=67+e_H(U)`.

Combining with (4) yields

`e_H(U)>=64`.      (5)

Now inspect the induced 14-set

`U union {u,v}`.

It contains at least64 edges inside U, exactly `t_u+t_v=12` target edges from u,v into U, and uv itself is a target nonedge. Hence it has at least

`64+12=76`

target edges.

But the inherited hereditary cap is

`D(14)=69`.

Contradiction.

Thus no 288-edge core has minimum degree11 either.

Combining with the already registered `e(C)<=286 => delta(C)>=12` lemma proves the theorem.

## E406 consequence

For an E406 degree-13 pivot,

`e(C)=315-q`.

Therefore every pivot with

`q in {27,28,29,30,31}`

has a 47-core of minimum degree at least12.

In particular the q27/q28 states now satisfy the minimum-degree hypothesis required by the V6-style profitable-repivot machinery; the former S27 minimum-degree interface is no longer an E406 bridge gap.
