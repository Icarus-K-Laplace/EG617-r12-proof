# Global d=3 q32 Nine-Owner Fully-Decorated Transversal Reduction

Status: `PROVED_ANALYTIC` under the retained r=12 backend contracts and the source-reported q32/CORE211 channel.

Dependencies:

- `GLOBAL_D3_Q32_NINE_OWNER_DECORATED_ESCAPE.md`;
- common-S exact exchange and row closure;
- `GLOBAL_ZERO_CHARGE_INCIDENCE_SIGNATURE_THEOREM.md`;
- inherited caps `D(14)=69`, `D(17)=81`;
- CORE211: `K=sum kappa=2`, `alpha(H)<=3`;
- the standard support-repetition decoration inequality.

Purpose: close two of the three fully-decorated slack layers and reduce the last layer to a bounded-transversal rigidity problem. This is the fully-decorated analogue of the global low-support matching-cover bridge.

## 1. Canonical nine-owner fully-decorated setup

By `GLOBAL_D3_Q32_NINE_OWNER_DECORATED_ESCAPE.md`, any surviving nine-owner q32 d3 system has

- nine regular owners `Y`, forming a target `K9`;
- one common missing triple `S`;
- `S` fully decorated;
- one remaining shell point `r`.

Thus

`A=Y disjoint_union S disjoint_union {r}`.

Every owner is target-adjacent to r, hence

> `B={p} union Y union {r}` is a target K11.                 (F1)

Put

`m=e_M(S)`,
`c=e_M(S,{r})`,
`G_S=sum_(s in S) g_s`.

Since every Y--S pair is a missing edge, there are exactly27 such shell missing edges. The q32 ledger is therefore

> `27+m+c+G_S+g_r=32`.                                      (F2)

Because S is fully decorated,

`G_S>=3`.

Hence

> `g_r+m+c<=2`.                                               (F3)

In particular

> `g_r in {0,1,2}`.                                          (F4)

For the common-S d3 rows the leftover shell block is `{r}`, so the exact row allowance is

> `a=2-g_r`.                                                  (F5)

The common-S total charge is

`W=sum_(v in H)(kappa_v+e_F(v,S))`.

Since `K=2`, direct shell--core incidence counting gives

> `W=34+m-g_r`.                                               (F6)

The total global decoration on the 35-core is

> `G_H=26+m+c`.                                               (F7)

Thus `G_H<=28`.

## 2. The K11 base gives multiplicity at most four

Let D be any 3-point support class with owner multiplicity M.

Every support row has defect at most a<=2, hence

`e_H(D)>=1`.

Inside the induced 14-set `B union D`, the certified target edges include

- 55 edges of the K11 base B;
- `3M` owner--support edges;
- `e_H(D)>=1` internal support edge;
- possibly further nonnegative r--D edges.

D(14)=69 gives

`55+3M+1<=69`.

Therefore

> every support class has multiplicity `M<=4`.               (F8)

Since there are nine owners, there are at least three distinct support classes.

## 3. The layer g_r=2 is impossible

Assume `g_r=2`.

Then (F3) forces

`m=c=0`, `G_S=3`,

and (F5) gives

`a=0`.

Thus every support D satisfies

`w(D)=0`, `mu(D)=0`.

Hence every support is a zero-charge target K3.

Proper overlap is impossible because every proper d3 overlap costs at least2 while the support defect is0. Distinct supports are therefore disjoint.

Row closure gives zero target cross-edges between distinct supports.

D14 with e_H(D)=3 sharpens (F8) to

`55+3M+3<=69`,

so

> `M<=3`.                                                     (F9)

Nine owners therefore force exactly three distinct support classes, each of multiplicity3.

These are three pairwise-disjoint pairwise-anticomplete zero-charge K3s.

Let z be any of the other 26 core vertices. If z were not target-complete to any one of the three K3s, choose one z-nonneighbour from each K3. Because the three K3s are pairwise target-anticomplete, together with z they form an independent4-set, contradicting `alpha(H)<=3`.

Hence z is target-complete to some support K3. Row closure against that zero-charge support yields

`w_z>=3`.

Thus

`W>=26*3=78`,

contradicting (F6), which gives W=32.

Therefore

> `g_r=2` is impossible.                                     (F10)

## 4. The layer g_r=1 is impossible

Assume `g_r=1`.

Then

`a=1`,
`W=33+m<=34`.

Every support has defect at most1. Hence proper overlap is impossible, so distinct supports are disjoint.

For disjoint supports D,E, common-S row closure gives

`e_H(D,E)<=1`.

Also every support has

`e_H(D)>=2`.

By the d3/cross-one block-transversal capacity theorem, at most three distinct support classes can occur.

By (F8) at least three are needed. Therefore there are exactly three distinct disjoint supports

`D_1,D_2,D_3`.

Let z be any of the other26 core vertices and suppose `w_z<=1`.

Row closure gives

`e_H(z,D_i)<=1`

for each i. Hence the z-nonneighbour set in every D_i has size at least2.

Between any two of these three 2-or-more point sets there is at most one target edge. The matching-transversal rigidity theorem for three parts then gives an independent transversal: if no independent transversal existed, all three parts would have size exactly2 and every pair would have to be joined by a perfect matching of size2, impossible because there is at most one target cross-edge per support pair.

Thus there are vertices

`u_i in D_i`, i=1,2,3,

which are pairwise target-nonadjacent and all target-nonadjacent to z.

This gives an independent4-set, contradiction.

Therefore every one of the26 outside core vertices satisfies

`w_z>=2`.

Hence

`W>=52`,

contradicting `W<=34`.

Therefore

> `g_r=1` is impossible.                                     (F11)

## 5. Only the allowance-two layer remains

By (F10)--(F11), every nine-owner fully-decorated survivor satisfies

> `g_r=0`, `a=2`.                                            (F12)

Then

`m+c<=2`,
`W=34+m<=36`,
`G_H=26+m+c<=28`.                                            (F13)

The remaining shell point r is regular.

## 6. Support union has at least seven vertices

Let U be the union of all support vertices.

The K11 base B contributes55 target edges, and the nine owners contribute exactly27 owner--core target incidences.

If `|U|<=6`, then `|B union U|<=17`, while the induced target-edge count is already at least

`55+27=82`.

But D(17)=81, and the retained cap is smaller for smaller orders in this range.

Contradiction.

Therefore

> `|U|>=7`.                                                   (F14)

## 7. Three pairwise-disjoint support classes are impossible

Assume for contradiction that there are three distinct pairwise-disjoint supports

`D_1,D_2,D_3`.

Put

`w_i=w(D_i)`.

Since each support has defect at most2,

`w_i+mu(D_i)<=2`.

Therefore

`w_i<=e_H(D_i)-1<=2`.                                       (F15)

For distinct disjoint supports row closure gives

`e_H(D_i,D_j)<=min(w_i,w_j)`.                               (F16)

Let

`R=H\(D_1 union D_2 union D_3)`, `|R|=26`.

### 7.1 Every outside vertex has positive charge

Suppose z in R has `w_z=0`.

Then row closure makes z target-anticomplete to every D_i.

Choose one uniformly random vertex from each D_i. The expected number of target cross-edges among the chosen triple is at most

`(2+2+2)/9=2/3<1`

by (F16).

Hence an independent transversal exists. Together with z it gives an independent4-set.

Thus

> every z in R has `w_z>=1`.                                (F17)

### 7.2 A charge-one outside vertex forces all three supports to have charge two

Let z in R satisfy `w_z=1`.

For each i let A_i be the set of z-nonneighbours in D_i. Row closure gives

`|A_i|>=2`.

If some support, say D_1, has `w_1=0`, then D_1 is target-anticomplete to both other supports. Since `e_H(D_2,D_3)<=2`, the two sets A_2,A_3, each of size at least2, contain a target-nonedge pair. Together with any point of A_1 this gives an independent transversal, contradiction.

If two support charges are at most1, then every support-pair cross graph contains at most one target edge. The three-part matching-transversal theorem again produces an independent transversal through A_1,A_2,A_3, contradiction.

Hence a charge-one outside vertex can exist only if, after sorting,

`(w_1,w_2,w_3)` is either `(1,2,2)` or `(2,2,2)`.             (F18)

The pattern `(1,2,2)` is also impossible.

Indeed the three pairwise cross-edge counts are at most

`1,1,2`.

If any A_i has size3, the four possible cross edges cannot cover all transversal triples: the union bound gives strictly fewer forbidden triples than `|A_1||A_2||A_3|`.

Thus all A_i would have size2. There are eight transversal triples. The maximum four cross edges would each cover two triples, so absence of an independent transversal would require the four covered-pair sets to be disjoint.

Let the unique D_1--D_2 edge be `a_0b_0` and the unique D_1--D_3 edge be `a_1c_0`. They must use different D_1 endpoints, otherwise their forbidden-transversal sets overlap. An edge of D_2--D_3 whose forbidden set is disjoint from both must then use simultaneously the endpoints different from b_0 and c_0. There is only one such edge, while two D_2--D_3 edges are required. Contradiction.

Therefore any charge-one outside vertex forces

> `w_1=w_2=w_3=2`.                                          (F19)

Then every D_i is a target K3.

### 7.3 Low total charge forces many charge-one outside vertices

If no outside vertex had charge1, (F17) would give

`W>=26*2=52`,

contradicting `W<=36`.

Hence charge-one outside vertices exist, and by (F19) all three support charges equal2.

Thus the support union itself contributes exactly6 charge units.

Since W<=36, among the26 outside vertices at most four can have charge at least2. Consequently

> at least22 outside vertices have charge exactly1.          (F20)

### 7.4 Zero-charge vertices inside the three K3s give the final contradiction

Because each K3 has total charge2 on three vertices, it contains at least one zero-charge vertex.

Call a support **Type A** if it has two zero-charge vertices (charge distribution 2,0,0), and **Type B** if it has one zero-charge vertex (charge distribution 1,1,0).

Zero-charge vertices belonging to different supports have different support-incidence signatures. By the zero-charge incidence-signature theorem they are pairwise target-nonadjacent across supports.

Take an outside charge-one vertex z.

If z failed to be target-adjacent to every zero-charge vertex of at least one support, then from each support choose a zero-charge z-nonneighbour. The three chosen vertices are pairwise target-nonadjacent and together with z form an independent4-set.

Thus z must be target-adjacent to all zero-charge vertices of some support.

But row closure gives at most one z-neighbour in each support. Therefore that support must be Type B, and z must be adjacent to its unique zero-charge vertex.

A zero-charge vertex in a Type-B K3 has

- core degree12;
- two internal K3 neighbours;
- no target cross-neighbours in the other supports.

Hence it has at most10 neighbours in R.

If at most two supports were Type B, their unique zero vertices could collectively serve at most20 charge-one outside vertices, contradicting (F20).

Therefore all three supports are Type B.

Let their unique zero vertices be `z_1,z_2,z_3`.

Suppose an outside charge-one vertex z were adjacent to only one of them, say z_1. That edge already consumes the row-closure allowance of z into D_1, so z is target-nonadjacent to the two positive-charge vertices of D_1. Choose one such vertex v.

The zero vertices z_2,z_3 are target-nonadjacent to v by zero-charge row closure, and are target-nonadjacent to each other by distinct signatures. By assumption z is also target-nonadjacent to z_2,z_3.

Hence

`{z,v,z_2,z_3}`

is an independent4-set, contradiction.

Thus every one of the at least22 charge-one outside vertices is adjacent to at least two of z_1,z_2,z_3.

The three zero vertices together have outside-neighbour capacity at most

`3*10=30`.

But the charge-one vertices demand at least

`2*22=44`

such incidences.

Contradiction.

Therefore

> no three distinct support classes can be pairwise disjoint. (F21)

## 8. Six-point transversal conclusion

Let F be the hypergraph of distinct 3-point support classes.

By (F21), its matching number satisfies

`nu(F)<=2`.

Take a maximal matching of size at most2. The union C of its support classes has size at most6.

By maximality, every support class meets C.

Therefore

> **Fully-decorated transversal reduction.**
> Every surviving q32/CORE211 nine-owner fully-decorated system satisfies
n
> `g_r=0`, `a=2`, and all distinct support classes are hit by a core transversal C with `|C|<=6`.   (F22)

Together with (F14), the total support union still has at least seven vertices.

Thus the final nine-owner equality problem is not an arbitrary support hypergraph. It is a bounded-transversal system with

- nine owners;
- support multiplicity at most4;
- support union size at least7;
- matching number at most2;
- total common-S charge at most36;
- total core decoration at most28.

## 9. Remaining bridge

The unique remaining statement for the N=9 fully-decorated escape is now:

> **A2 Six-Point Transversal Rigidity Lemma (OPEN).**
> Under the data in (F22), the 3-uniform support-incidence system cannot be realized in a 35-point core with alpha(H)<=3, CORE211 excess2, row closure, and the inherited hereditary caps.

This is strictly smaller than the original nine-view problem and is the fully-decorated equality analogue of `GLOBAL_LOW_SUPPORT_MATCHING_COVER_BRIDGE.md`.

A proof of this lemma would lower the q32 d3 simultaneous-owner capacity from nine to eight and remove the final owner-count equality escape in the E334 d3 bridge.

## 10. Generalization

Sections1--5 use only exact shell accounting and a hereditary K11 base. Section7 uses support size3, alpha(H)<=3, row closure and a low total charge bound. Section8 is pure hypergraph matching-cover.

Thus the architecture generalizes: a fully-decorated maximal-owner escape first descends through the leftover-shell slack, then either dies at low allowance or is forced into a bounded support transversal at the final allowance layer.
