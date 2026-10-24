# E408 global seven-block equality system

Status: **PROVED**, conditional only on the already-proved outer embedding ledger in `FRONTEND_BRIDGE_THEOREM.md` and the original balanced-coloring contract.

This theorem is independent of the retained lower-order seeds used by the V11/V12 Q31--Q33 shell analysis.

## 1. Outer equality forces an exact target decomposition

In the T61 embedding from F8 of `FRONTEND_BRIDGE_THEOREM.md`, the target residual edge count E satisfies

`E + sigma + z + g + x_6 + y_6 = 408`,

where every displayed charge is nonnegative.

At E=408 all of them vanish:

` sigma=z=g=x_6=y_6=0.`

Consequences:

- `sigma=870-m=0`, so the least-color graph G has exactly870 edges;
- `z=55-e(G[A])=0`, so the 11-neighbour set A of the anchor v is a target K11;
- `g=sum_(a in A)(d_G(a)-11)=0`, so every a in A has total target degree11; hence `N[v]` is a target K12 component anticomplete to the rest of G;
- `x_6=0`, so the six packed target K12 blocks are pairwise target-anticomplete;
- `y_6=0`, so those six blocks are target-anticomplete to the 61-point residual R.

Thus the 145 vertices split exactly as

> **`G = B_0 dot_union B_1 dot_union ... dot_union B_6 dot_union R`,**
>
> with every `B_i=K12`, `|R|=61`, `e_G(R)=408`, and no target edge between distinct pieces.

In particular the target graph consists of seven isolated K12 components together with the E408 T61 component R.

## 2. Every color has exactly870 edges

The complete graph K145 has

`C(145,2)=10440=12*870`

edges.

The target color G is a least-edge color and has870 edges. Therefore every one of the other eleven colors has at least870 edges. Their total together with G is exactly10440, so equality is forced:

> **every one of the twelve colors has exactly870 edges globally.**

## 3. One-or-two rule toward every target K12 block

Fix a non-target color C and one target block B_i.

The block B_i is an independent set of size12 in C. Since the original balanced condition gives `alpha(C)<=12`, every vertex x outside B_i must have at least one C-neighbour in B_i; otherwise `B_i union {x}` is C-independent of size13.

For a fixed x outside B_i, the twelve edges from x to B_i are all non-target edges and are partitioned among the eleven non-target colors. Every non-target color must occur at least once by the preceding paragraph. Hence the twelve edges have the exact multiplicity pattern

> **one non-target color occurs twice and each of the other ten colors occurs once.**

Equivalently, for every triple `(x,B_i,C)`,

`d_C(x,B_i) in {1,2}`, 

and for fixed `(x,B_i)` exactly one color has value2.

This is an exact near-Latin row condition.

## 4. Block-pair duplicate variables

For two distinct target K12 blocks B_i,B_j and a fixed non-target color C, every vertex of either block has C-degree one or two into the other block. Therefore

`e_C(B_i,B_j)=12+d_ij(C)`

for some integer `d_ij(C)>=0`.

Counting from either side shows that d_ij(C) is exactly the number of vertices on either side whose repeated color toward the opposite block is C.

For each fixed block pair,

> `sum_C d_ij(C)=12`,

because each of the twelve rows has exactly one repeated non-target color.

Define

`P_C=sum_(0<=i<j<=6) d_ij(C)`.

Then the total C-edge count among the seven target blocks is

> `e_C(B_0 union ... union B_6)=21*12+P_C=252+P_C`.

## 5. Block--R duplicate variables

For each block B_i and each vertex x in R, the same one-or-two rule holds. Hence

`e_C(B_i,R)=61+r_i(C)`

where `r_i(C)>=0` counts the R-vertices whose repeated color toward B_i is C.

For fixed i,

> `sum_C r_i(C)=61`.

Define

`R_C=sum_(i=0)^6 r_i(C)`.

Then

> `e_C((union_i B_i),R)=7*61+R_C=427+R_C`.

## 6. Exact 62-unit duplicate budget

On the 61-point residual, every non-target color obeys the contextual lower bound129. Write

`e_C(R)=129+s_C`, `s_C>=0`.

Since every non-target color has exactly870 edges globally, decomposing its edges into

- block--block,
- block--R,
- R-internal

parts gives

`870=(252+P_C)+(427+R_C)+(129+s_C)`.

Therefore

> **`P_C + R_C + s_C = 62`**
>
> for every non-target color C.

For E408, the eleven R-internal excesses satisfy

`sum_C s_C = C(61,2)-408-11*129 = 3`.

Thus the eleven global non-target colors form an exact family of 62-unit duplicate systems whose R-internal excess totals only3.

Summing the duplicate equations recovers

`sum_C P_C=21*12=252`,

`sum_C R_C=7*61=427`,

and `252+427+3=11*62`, as required.

## 7. Interface with Q32/Q33

Any E408 Q32/Q33 shell/core completion must therefore extend to this global seven-block near-Latin system.

In particular a local shell template is not realizable merely because its 61-point scalar/core equations are feasible: its eleven non-target color restrictions must simultaneously admit

- exact global edge count870 in every color;
- the one-or-two row condition toward each of seven target K12 blocks;
- per-color duplicate budget `P_C+R_C+s_C=62`;
- total residual excess `sum s_C=3`.

This provides a new completion obstruction independent of the retained-seed shell enumeration.
