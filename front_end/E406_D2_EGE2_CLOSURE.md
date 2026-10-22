# E406 d=2: all retained-star layers e>=2 are impossible

Status: `PROVED`. The d=2 final-rise class is reduced to the unique retained-block case `e=1`. `E406` remains `OPEN`.

Inputs:

- `E406_D2_RETAINED_BLOCK.md`;
- Line-A ledger theorem L4: every inherited `R(4,47)` core with at most286 edges has minimum degree at least12.

Assume a d=2 q30->q31 final rise in the retained-star branch with

`e=e(M[T])>=2`.

By `E406_D2_RETAINED_BLOCK.md`:

- `M[T]=K_{1,e} +(9-e)K1`;
- the star centre is c and has decoration `8-e`;
- every star leaf l is undecorated;
- both exchanged S-vertices are missing-adjacent to c and to every star leaf;
- every star leaf has q-value exactly30;
- for each star leaf l, its old 3-row

  `U_l=N_C(l)`

  is a target K3 of old-core degree12 vertices;
- `U_l` is target-anticomplete to the common shell triple

  `{c,s1,s2}`.

Fix any star leaf l.

## 1. The l-core is a genuine 285-edge R(4,47) core

The pivot l has global degree13 and q_l=30. Hence its 47-core C_l satisfies

`e(C_l)=406-91-30=285`.

Because l is a degree13 pivot in the same T61 parent, C_l is an inherited `R(4,47)` object. L4 therefore gives

`delta(C_l)>=12`.      (L4)

## 2. The imported star centre has core degree exactly10

The star centre c has old p-shell row weight10:

- its internal retained-star missing degree is e;
- it is missing to both S-vertices;
- its decoration is `8-e`;

so

`t_c=e+2+(8-e)=10`.

Thus c has exactly10 neighbours in the old core C.

Repivoting at l replaces the old 3-row U_l by the three shell vertices

`{c,s1,s2}`.

The new core is

`C_l=(C\U_l) union {c,s1,s2}`.

By the retained-block theorem, U_l is target-anticomplete to c, so deleting U_l removes no old core neighbour of c.

Also c is target-nonadjacent to s1 and s2. Therefore importing s1,s2 creates no new core neighbour of c.

Consequently

`d_{C_l}(c)=10`.

This contradicts (L4).

Hence no retained-star d2 final-rise state with `e>=2` exists.

## 3. Remaining d2 terminal

The only d=2 final-rise state not covered by this argument is the exact `e=1` case from `E406_D2_RETAINED_BLOCK.md`:

- `M[T]=K2+8K1`;
- total T-decoration7 is supported on the two endpoints of the unique missing edge;
- both endpoints are target-anticomplete to S and D;
- the eight T-isolates are undecorated.

Thus d2 has collapsed from eight retained-block layers to one single decorated-edge terminal.