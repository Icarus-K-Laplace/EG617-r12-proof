# q36 f=3 K2+K1 terminal — support-class collapse

Status: `PROVED REDUCTION` under `Q36_F3_K21_TERMINAL_STRENGTHENING.md`, the standard row-closure theorem, CORE211, and inherited D14.

This reduces the surviving f=3 terminal from at least six arbitrary dense triples to exactly two disjoint 3-support classes with four possible multiplicity patterns.

## 1. Setup

Use the terminal notation from `Q36_F3_K21_TERMINAL_STRENGTHENING.md`.

The far regular shell is `F={a,b,z}` with `ab` a target edge and z target-nonadjacent to both.

Their core supports satisfy

- `|A|=|B|=11`, `|Z|=12`;
- `Z` is disjoint from A and B;
- `h=|A intersect B| in {10,11}`.

Let

`R=H\(A union B union Z)`.

Then `|R|=11` when h=10 and `|R|=12` when h=11.

The low regular shell clique C has size `c>=6`, and every low support `D_y`, y in C, satisfies

- `D_y subset R`;
- `|D_y|=3`;
- `e_F(F,D_y)=0`;
- `kappa(D_y)+m(D_y)<=1`, where `m(D)=3-e_H(D)`.

Hence every D_y induces either a target triangle or a target P3, with total captured core excess at most1.

## 2. Proper support overlap is impossible

Take two low rows D_i,D_j and put `r=|D_i intersect D_j|`.

The general row-closure overlap inequality for common missing set F gives

`r(3-r) <= kappa(D_j\D_i) + e_F(F,D_j\D_i) + m(D_j)`.

The shell-cross term vanishes, and the right side is at most

`kappa(D_j)+m(D_j)<=1`.

For a proper overlap r=1 or2, the left side equals2. Contradiction.

Therefore

> any two low supports are either equal or disjoint.          (1)

For distinct disjoint supports, the common-S theorem gives

`e_H(D_i,D_j)<=min(kappa(D_i),kappa(D_j))<=1`.              (2)

## 3. Four distinct support classes are impossible

Assume there are four distinct support blocks D1,D2,D3,D4.

They are disjoint 3-sets and every pair has at most one target cross edge by (2).

Choose one vertex uniformly and independently from each block. For each of the six block-pairs, the probability that the selected pair is a target edge is at most `1/9`. Hence the expected number of selected cross edges is at most

`6/9=2/3<1`.

Therefore some choice has zero target cross edges. The four chosen vertices form an independent4-set in H, contradicting `alpha(H)<=3`.

Thus there are at most three distinct support classes.

## 4. Three distinct support classes are impossible

Assume there are exactly three distinct disjoint support blocks D1,D2,D3.

Put

`L=H\(D1 union D2 union D3)`, so `|L|=26`.

For v in H define

`w_v=kappa_v+e_F(v,F)`.

The CORE211 excess is2, while the three far shell rows have sizes11,11,12. Hence

`sum_(v in H) w_v = 2+11+11+12 =36`.                       (3)

For v in L, row closure gives

`e_H(v,D_i)<=w_v`                                           (4)

for each i.

Suppose some v in L had `w_v<=1`. Then v has at most one neighbour in each D_i, so each

`D_i' = D_i\N_H(v)`

has size at least2.

Between any two D_i',D_j' there is at most one target edge, because the parent blocks have at most one. Choose one vertex uniformly from each D_i'. The expected number of target cross edges among the three selected vertices is at most

`3*(1/(2*2))=3/4<1`.

Thus there is a choice of one vertex from each block that is pairwise target-nonadjacent and also nonadjacent to v. Together with v they form an independent4-set in H, contradiction.

Hence every v in L has `w_v>=2`, so

`sum_L w_v>=26*2=52`,

contradicting (3).

Therefore there are at most two distinct support classes.

## 5. Every support class has multiplicity at most4

Let D be a support class of multiplicity m, and repivot at one of its owners y in C.

The strengthened terminal theorem gives

`q_y=34+kappa(D)+m(D)<=35`.

The repivot removes only the three regular far vertices F and retains all old decorated shell vertices X. Thus the old shell decoration total

`G=4-nu`

is retained.

A vertex v in D has core degree at least12 and is adjacent to all m shell owners in C. Therefore its global decoration satisfies

`g_v>=m-1`.

The new shell consequently has

`G_y>=G+3(m-1)`.                                           (5)

In the f=3 terminal, `nu=e_M(X)<=1`: if `nu>=2`, then `c>=6+nu>=8`, so `|X|=10-c<=2`, but a graph on at most2 vertices has at most one missing edge. Hence

`G=4-nu>=3`.                                                (6)

Every q_y<=35 shell satisfies the inherited D14 decoration bound

`G_y<=q_y-22<=13`.                                         (7)

Combining (5)--(7),

`3+3(m-1)<=13`,

so

> `m<=4`.                                                    (8)

## 6. Exactly two classes remain

There is at least one support class, and the low clique has `c>=6` owners.

- one class is impossible by (8), since it would have multiplicity c>=6;
- three or more classes were excluded above.

Therefore there are exactly two distinct support classes D1,D2.

Write their multiplicities as `m1>=m2`. Then

`m1+m2=c`, `2<=m_i<=4`.

Since `c>=6`, the only possibilities are

- c=6: `(m1,m2)=(4,2)` or `(3,3)`;
- c=7: `(4,3)`;
- c=8: `(4,4)`.

In particular

> `c in {6,7,8}`.                                           (9)

The shell parameters are correspondingly

- c=6: `|X|=4`, `nu=0`, `G=4`;
- c=7: `|X|=3`, `nu in {0,1}`, `G in {4,3}`;
- c=8: `|X|=2`, `nu in {0,1}`, `G in {4,3}`.

## 7. New exact f=3 frontier

The entire f=3 K2+K1 terminal is now reduced to two disjoint 3-support blocks D1,D2 contained in the 11/12-point remainder R, with

- multiplicities only `4+2`, `3+3`, `4+3`, or `4+4`;
- each support inducing K3 or P3;
- `kappa(D_i)+m(D_i)<=1`;
- `e_H(D1,D2)<=1`;
- every owner repivot has charge at most35.

This is a finite four-channel incidence problem. No q36 closure is claimed yet.