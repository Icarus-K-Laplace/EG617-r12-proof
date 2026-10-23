# q36 compensated d9 ceiling branch — full closure

Status: `PROVED` under the standard legal backend contract and `Q36_COMPENSATED_K49_NORMAL_FORM.md`.

This eliminates every q36 zero-defect d9 ceiling exchange. It does not yet eliminate the remaining compensated d4 family.

## 1. Compensated d9 setup

Use the normal form with

- S of size9;
- U={y} union T of size4;
- S and U both target cliques;
- y is regular and target-anticomplete to S;
- all target cross edges lie between S and the three vertices of T;
- every s in S is decorated;
- `g_s` equals its target cross-degree into T;
- total cross-edge count `G` satisfies `9<=G<=14`.

Every vertex of U is regular.

For `t in T`, let `a_t=e_F(t,S)`. Its missing degree in the shell is

`d_M(t)=9-a_t`.

At a q36 maximal pivot, regular missing degrees 5,6,7,8 are impossible. Hence

`a_t in {0,5,6,7,8,9}`.                                    (1)

Since all nine S-vertices have positive row degree, the nonzero T-columns cover S. By `G<=14` and (1), there are at most two nonzero T-columns.

Thus there are exactly two cases.

## 2. Case A: one active T-column

The unique nonzero column must meet all nine vertices of S, so it has degree9 and `G=9`.

Therefore y and the other two vertices of T are three zero columns. All three are regular d9 plateau pivots with the same missing set S.

For each zero column u let `D_u` be its 9-point core support. By the common-S theorem at q36:

- H[D_u]=K9;
- every vertex of D_u has H-degree12;
- two distinct supports are disjoint and target-anticomplete.

The active T-column has missing degree0, hence empty core row.

### A1. Three distinct supports

If the three zero columns have three distinct supports D1,D2,D3, then the three K9 blocks are pairwise anticomplete.

Each vertex in a Di has internal degree8 and total H-degree12, so it needs exactly four neighbours in the remaining 8-point set.

Hence the core has at least

`3*C(9,2) + 3*(9*4) = 108+108=216`

edges, contradicting `e(H)=211`.

### A2. One support used three times

If all three zero columns share one support D, each vertex of D is adjacent to all three zero shell columns. Since its H-degree is12, its global degree is at least15, so its decoration is at least2.

Repivoting at one of the zero columns inserts all nine vertices of D into the new shell. Thus the new q36 shell has decoration total at least

`9*2=18`.

But every q36 shell satisfies the inherited D14 bound `G<=14` from the normal-form theorem. Contradiction.

### A3. Multiplicity 2+1

Let D be the support shared by two zero columns and E the singleton support. D and E are disjoint and anticomplete.

Because the unique active T-column has empty core row, and S is anticomplete to E by zero-defect equality, every vertex of E has exactly one shell neighbour: its owner zero column. Hence every vertex of E is globally regular.

Repivot at the singleton owner. The new shell consists of

- a target K4 on the retained four-side;
- the pure regular K9 support E;
- no target cross edges between them;
- no decorated shell vertices.

So the new shell is the exact `K_(4,9)`, `G=0` plateau, already excluded by `K49_G2_SPLIT_FULL_CLOSURE.md`.

Thus Case A is impossible.

## 3. Case B: two active T-columns

Now y and the remaining T-vertex z are the two zero columns. Let the two active columns be t1,t2, with cross-degrees a1,a2>=5 and `a1+a2<=14`.

Their core-row sizes are

`|D_ti|=9-ai<=4`.                                          (2)

The zero supports `D_y,D_z` are K9s.

### B1. Distinct zero supports

Assume `D_y` and `D_z` are distinct. Then they are disjoint.

Repivot at y. In the new shell, `D_y` is the nine-side. The retained four-side vertices have target degrees into `D_y`:

- p: 0;
- z: 0, because `D_z` is disjoint from `D_y`;
- ti: at most `|D_ti|<=4` by (2).

The new shell is again a q36 d9 compensated configuration, with p as a regular d9 vertex missing all of `D_y`.

By the all-or-nothing theorem, if this new shell has positive decoration then every one of the nine vertices of `D_y` must be decorated. But the only possible decorating incidences come from `D_t1` and `D_t2`, whose total size is at most8. They cannot cover all nine vertices of `D_y`.

If there are no such incidences, the new shell is exact `K_(4,9)`, G=0, already closed.

Contradiction in either case.

### B2. Equal zero supports

Assume `D_y=D_z=D`.

Repivot at y. In the new shell, z is target-adjacent to every vertex of D, so z is a cross column of degree9.

For i=1,2, the target degree of ti into D is

`r_i=|D_ti intersect D|<=|D_ti|<=4`.

Again view the new shell through the regular vertex p, whose missing set is exactly the nine-side D. Every retained ti is regular. If `r_i>0`, its missing degree relative to D is

`9-r_i in {5,6,7,8}`,

which is forbidden at q36.

Therefore `r_1=r_2=0`.

The new shell consequently has exactly one active cross column, namely z, complete to the nine-side D. This is precisely Case A, already impossible.

Thus Case B is impossible.

## 4. Conclusion

Both possible compensated d9 topologies are impossible. Therefore

> no q36 lexicographically maximal CORE211 pivot admits a regular zero-defect d9 ceiling exchange.

Equivalently, the entire q36 d9 branch is empty.

## Boundary

The q36 d4 compensated family remains. It is reduced in `Q36_D4_COMPENSATED_DYNAMICS.md`.