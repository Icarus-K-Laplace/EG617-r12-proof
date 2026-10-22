# E406 q30 no-rise platform: K3,r and five-block saturation

Status: `PROVED` for the branch containing a regular missing-degree3 or missing-degree10 pivot. The complementary extreme-degree-only q30 branch remains to be handled separately.

Assume an E406 degree-13 pivot p has q=30 and has no adjacent q31 pivot. Its 47-core C has e(C)=285 and delta(C)>=12.

For every undecorated shell vertex y, write d=d_M(y), S=N_M(y), and X=t(S)-e_M(S). Since q_y<=30,

`X>=d(13-d)`.

Hence every regular missing degree lies in

`{0,1,2,3,10,11,12}`.

## 1. Exact d3/d10 equality

For d=3 or10, `d(13-d)=30=q`, so equality is forced:

- `X=30`;
- `e_M(A\S)+G_{A\S}=0`;
- the exact repivot has `q_y=30`;
- the core row D=N_C(y) is a K_d consisting entirely of core-degree12 vertices;
- `e_R(S,D)=0`;
- the inserted set S has zero excess in the new 285-edge core;
- therefore `e_M(S)=0`.

Thus every d3/d10 repivot is a zero-slack q30 plateau exchange.

## 2. A d3 plateau forces K3,r

Assume y has d=3. Put B=S=N_M(y), |B|=3, and let T=A\(B union {y}), |T|=9.

The equality above gives:

- B is M-independent;
- `{y} union T` is M-independent;
- all decorations outside B vanish;
- `t(B)=30`.

PAIR-13 on the three edges y--b gives `t_b>=10` for every b in B. Since the three weights sum30,

`t_b=10` for all b in B.      (1)

Every t in T is regular. If t is nonisolated in M, PAIR-13 against a B-vertex and (1) gives

`d_M(t)+10>=13`,

so `d_M(t)>=3`. Since t has at most three B-neighbours, every nonisolated t has degree exactly3.

Hence the missing graph is

`M=K_{3,r} disjoint_union (10-r)K1`

for some r between1 and10, where the r-side includes y and the active T-vertices.

Each B-vertex has missing degree r and weight10, so its decoration is `10-r`. Therefore

`G=3(10-r)`.

Since q=30 and z>=22, G<=8, hence

`r in {8,9,10}`.

## 3. A d10 plateau forces r=10

Assume y has d=10. Equality gives a 10-side S and a three-point opposite side `{y,t1,t2}`.

All three opposite-side vertices are regular and their missing degrees are at most10. Since z>=22, the two extra degrees satisfy

`d_M(t1)+d_M(t2)>=12`.

The no-rise degree restriction leaves only possibilities `(10,10)`, `(10,3)`, `(10,2)` up to order.

- In the (10,3) case, the degree3 vertex has weight3. Its three B-neighbours must each have weight at least10 by PAIR-13. Those three already consume all `t(S)=30`, while the other seven S-vertices have missing degree at least2. Contradiction.
- In the (10,2) case, the degree2 vertex has weight2. Its two neighbours require weight at least11, while the remaining eight S-vertices again have missing degree at least2; the total exceeds30.

Thus only `(10,10)` survives, which is precisely

`M=K_{3,10}`, `G=0`.

So every d10 plateau lies in the r=10 member of the d3 family.

## 4. Equal-or-disjoint K3 support classes

Fix the K3,r platform. Let L be its r active large-side vertices. For every `s in L`, its old core row

`P_s=N_C(s)`

is a pure K3 of core-degree12 vertices, anticomplete to the three shell centres B.

Repivot at s. In the new q30 shell, the three vertices of P_s have weight exactly10: the reverse pivot p has missing degree3 and PAIR-13, while their total weight is30.

For another active `t in L`, its new missing degree is

`3-|P_s intersect P_t|`.

If the intersection had size1, the new missing degree would be2 and its neighbourhood charge would be `10+10=20<22`, forcing q>=32 by the delta>=12 repivot bound.

If the intersection had size2, the new missing degree would be1 and its neighbourhood charge would be10<12, again forcing q>=32.

Therefore

`P_s=P_t` or `P_s intersect P_t=empty`.

Thus the active rows split into classes of identical K3 supports; distinct classes are disjoint.

If a class has size m, its three core vertices have global degree `12+m`. After repivot at any member, they enter the shell with decoration `m-1` each. Since every q30 shell has G<=8,

`3(m-1)<=8`,

so

`m<=3`.

## 5. Plateau dynamics = swapping parts of a partition of 11

Let the active support-class sizes be

`m1,...,mc`, each in {1,2,3}, with sum r.

Let

`a=11-r`.

The quantity a is exactly the number of reverse/full vertices represented by the old pivot together with the old isolated large-side vertices after one plateau exchange.

Repivoting at a member of a class of size mi removes that class from the active list and inserts the old centre K3 as a new support class of size a. The new platform parameter is

`r'=11-mi`,

so its new distinguished deficit is mi.

Hence a plateau exchange merely swaps the distinguished part a with the chosen class size mi.

Therefore the multiset

`P={a,m1,...,mc}`

is invariant throughout the q30 plateau component. Every part belongs to {1,2,3} and

`sum P=11`.

## 6. The invariant parts are pairwise anticomplete K3 blocks

The c core K3 supports are pairwise target-anticomplete: if two distinct supports had a core edge, repivoting away one would lower the degree of a degree12 vertex in the other below12.

The shell-centre K3 B is target-anticomplete to every support K3 by the zero-slack equality `e_R(B,P_s)=0`.

Thus the `c+1` parts of P correspond to `c+1` pairwise target-anticomplete K3 blocks in R.

Choosing one vertex from each block gives an independent set, so `alpha(R)=5` implies

`c+1<=5`.

Since the parts are at most3 and sum11, at least four parts are required. Therefore the number of parts is four or five.

## 7. Four parts are impossible by the global E406 excess budget

A K3 block associated with a part of size s consists of three vertices of global degree

`12+s`,

hence contributes `3(s-1)` units of degree excess above13.

Summing over all invariant parts gives total contribution

`3*sum(s-1)=3(11-n)`,

where n is the number of parts.

For n=4 this equals21. But an E406 graph has total degree excess

`2*406-61*13=19`.

Contradiction.

Thus n=5 and c=4.

The only partitions of11 into five parts in {1,2,3} are

- `(3,2,2,2,2)`;
- `(3,3,2,2,1)`;
- `(3,3,3,1,1)`.

These five pairwise anticomplete K3 blocks consume exactly

`3(11-5)=18`

of the 19 global excess units.

## 8. Forced 35-point saturated remainder

In the current pivot view, four of the five K3 blocks are core supports and one is the shell-centre block.

Delete the four core K3 blocks from the 47-core C. Let H be the remaining 35-point induced graph.

Each support K3 consists of degree12 core vertices, has three internal edges, is anticomplete to the other support blocks, and every one of its three vertices has exactly10 neighbours in H. Thus each block sends exactly30 edges to H.

Therefore

`e(H)=285 - 4*3 - 4*30 =153`.

The shell-centre K3 also sends exactly30 target edges to H, because each centre has core-row size10 and is anticomplete to all four support blocks.

Hence the q30 no-rise branch containing d3/d10 has been compressed to:

- five pairwise target-anticomplete K3 blocks;
- invariant part multiset one of the three five-part partitions above;
- a 35-point remainder H with exactly153 edges;
- every one of the five K3 blocks sends exactly30 target edges to H;
- the five blocks consume18/19 global degree-excess units, leaving only one excess unit outside them.

This is the modern saturated q30 plateau terminal for this branch.

## Remaining q30 work

It remains to:

1. eliminate this five-block / H153 saturated terminal; and
2. exclude the complementary q30 no-rise shell in which no regular vertex has missing degree3 or10.

No already-closed q30->q31 distance class should be reopened.
