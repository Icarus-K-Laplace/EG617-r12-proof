# E408 Q32 — 130-edge minimum degree four and Case-I v=46,m=8 closure

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL** under the registered E408 residual contract and Kang--Pikhurko Theorem 4.

## 1. External theorem scope

We use M. Kang and O. Pikhurko, *Maximum K_{r+1}-free graphs which are not r-partite*, Matematychni Studii 24 (2005), 12--20.

Theorem 1 gives, for `n>=r+3` and `r<=(n-1)/2`,

`p_r(n)=t_r(n)-floor(n/r)+1`,

where `p_r(n)` is the maximum edge count of an n-vertex K_{r+1}-free graph that is not r-partite.

Theorem 4 states that every extremal graph is one of the explicit constructions `G(n_1,...,n_r)` with

`sum_i n_i=n-1`.

In that construction every old part `N_i` is independent in the extremal graph and therefore becomes a clique after complementation.

For the application below, `r=11,n=57`, so `57>=14` and `11<=28=(57-1)/2`; the theorem is in range.

## 2. Theorem: a 130-edge color has minimum degree at least four

### Theorem 2.1

Let D be a non-target color graph on the 61-point E408 residual satisfying

`e(D)=130`, `alpha(D)<=12`, `omega(D)<=5`.

Then

> **`delta(D)>=4`.**

### Proof

The registered s=1 pointwise theorem already gives `delta(D)>=3`. Suppose for contradiction that a vertex v has `d_D(v)=3`.

Let

`S=N_D(v)`, `|S|=3`,

and let N be the 57 vertices different from v that are nonadjacent to v in color D.

As in the previously audited low-degree lemma, `alpha(D[N])<=11` and `omega(D[N])<=5`. The complement of `D[N]` is K12-free and is not 11-partite, because an 11-partition would partition N into eleven D-cliques, each of size at most5, covering at most55<57 vertices.

The Kang--Pikhurko extremal bound gives

`e(D[N])>=124`.

The 124 edges in N and the three v--S edges leave room for at most three further D-edges. Since every point of S has D-degree at least3, equality is forced: S spans a triangle and has no D-edge to N. Hence

> `K={v} union S` is an isolated D-colored K4,

and

`D' := D-K`

has

`|D'|=57`, `e(D')=124`, `alpha(D')<=11`, `omega(D')<=5`.

Now put `J=bar(D')`. Then

- J is K12-free;
- J is not 11-partite, by the same 55-vertex covering argument;
- `e(J)=C(57,2)-124=1596-124=1472`.

The balanced 11-partite Turan graph on57 vertices has part sizes `6,6,5^9`, so

`t_11(57)=1596-[2*C(6,2)+9*C(5,2)]`

`=1596-(30+90)=1476`.

Since `floor(57/11)=5`, Kang--Pikhurko Theorem 1 gives

`p_11(57)=1476-5+1=1472`.

Thus J is extremal. By Theorem 4, J is one of the explicit constructions `G(n_1,...,n_11)` with

`sum_i n_i=56`.

Every underlying part `N_i` is independent in J, hence a clique in D'. Because `omega(D')<=5`, every `n_i<=5`. Therefore

`56=sum_i n_i <=11*5=55`,

a contradiction.

Hence no degree-three vertex exists and `delta(D)>=4`. QED.

## 3. Consequences for E408 nonexact pointwise floors

The E408 excess partitions imply:

- `m=8`: the three nonexact colors all have130 edges, hence the corrected nonexact floor sum is
  
  > **`L_8=4+4+4=12`;**

- `m=9`: the nonexact colors have130 and131 edges, hence
  
  > **`L_9=4+3=7`;**

- `m=10`: the unique132-edge color retains the registered floor2.

The earlier values `L_8=9` and `L_9=6` are superseded.

## 4. Case-I v=46,m=8 is impossible

In Case I with `|U|=46`, the unique uncovered point w satisfies

`n_w>=m-3=5`

by the proved shell-matching theorem.

The eight exact colors contribute at least

`4m+n_w >=32+5=37`

to the non-target degree of w. The target contributes at least13, and the three 130-edge nonexact colors now contribute at least12.

Thus

`60 >= 13+37+12=62`,

impossible.

Therefore

> **Case I / v=46 / m=8 is CLOSED.**

Combined with the already proved m=9 and m=10 exclusions, **Case I has no v=46 realization at all.**

## 5. Stronger pointwise restriction for m=8

The same degree sum holds at every residual vertex z. With eight exact colors contributing baseline degree at least4 and three 130-edge colors contributing at least4 each,

`60 >= d_F(z)+32+12+E_z`,

where

`E_z=sum_{C: x_C=z}[(9-a_C)-4]=sum_{C:x_C=z}(5-a_C)`

is the total special-vertex excess over the exact-color baseline4.

Since `d_F(z)>=13`,

> **`E_z<=3` for every residual vertex z.**

In particular no residual vertex can be the Type-I special point of four exact colors, because each special incidence contributes at least one unit.

This immediately strengthens every non-full-support multiplicity argument in the m=8 branch.

## 6. Stronger pointwise restriction for v=44,m=9

For m=9, every W-point is special for exactly three exact colors. The corrected nonexact floor is `4+3=7`. Hence at a W-point w,

`60 >= 13 + 9*4 + 7 + E_w =56+E_w`,

so

`E_w<=4`.

Writing the three KP parameters as `a_1,a_2,a_3`,

`E_w=sum_i(5-a_i)=15-(a_1+a_2+a_3)<=4`,

therefore

> **`a_1+a_2+a_3>=11`.**

Up to order, only two parameter profiles remain:

> `(4,4,4)` and `(4,4,3)`.

This replaces the earlier four-profile list `(4,4,4),(4,4,3),(4,4,2),(4,3,3)`.

## 7. Firewall

This theorem uses:

- the 61-point E408 full-color contract;
- the already-proved s=1 floor `delta>=3` only to derive the isolated-K4 equality before the sharper step;
- Kang--Pikhurko Theorems 1 and4 at `(n,r)=(57,11)`;
- `omega(D)<=5`, `alpha(D)<=12`;
- the Q32 Case-I matching theorem only in Section4.

It does not use:

- Q33's 284-edge core;
- support-41;
- the retracted degree9 exceptional-vertex claim;
- exceptional-vertex injectivity;
- SAT/ILP nonexistence.

Q32 as a whole remains OPEN because Case II and full support v=47 remain.
