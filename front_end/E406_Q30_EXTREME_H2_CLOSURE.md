# E406 q30 no-rise extreme shell: complete two-high closure

Status: `PROVED EMPTY` for the branch with exactly two undecorated high shell vertices.

Assume an E406 degree-13 pivot p with q=30 and no legal q31 repivot. The 47-core has e(C)=285 and delta(C)>=12. Assume the d3/d10 plateau branch has already been eliminated, so every undecorated shell missing degree lies in

`{0,1,2,11,12}`.

Let H be the set of undecorated high vertices (missing degree11 or12), L the undecorated low vertices (degree0,1,2), and D the decorated vertices. Put h=|H|, l=|L|, k=|D|, G=sum g, z=30-G.

The low set L is independent in M.

## 1. At most two high vertices

A high vertex has at most one M-nonneighbour among the other12 shell vertices. Hence

`e_M(H,L)>=hl-h`.

But the total missing degree on L is at most2l, so

`(h-2)l<=h`.

If h>=3 this forces l<=3 for h=3 and even smaller for h>3. Therefore k=13-h-l>=7 and G>=7, hence z<=23. On the other hand the number of M-edges incident with H is at least

`11h-C(h,2)>=30`

for h>=3, impossible. Thus h<=2.

We now exclude h=2.

Write H={a,b}.

## 2. Case ab notin E(M)

Then each of a,b has missing degree exactly11 and is adjacent in M to every vertex of L union D. Every low vertex therefore already has its maximum possible degree2, namely

`N_M(u)={a,b}`,

so there are no L-D edges.

Let J=M[D] and j=e(J). Since L union D has11 vertices and alpha(M)<=10, J is nonempty. Exact charge gives

`z=22+j`, `G=8-j`.

For an edge xy of J,

`t_x+t_y=4+d_J(x)+d_J(y)+g_x+g_y`.

The two endpoint degrees inside a j-edge graph satisfy

`d_J(x)+d_J(y)<=j+1`,

while positivity of all k decorations gives

`g_x+g_y<=G-(k-2)=10-j-k`.

PAIR-13 therefore gives

`13<=t_x+t_y<=15-k`,

so k<=2. Since J is nonempty, k=2, j=1 and G=7.

Thus the shell is exact:

- nine regular low vertices, each with neighbourhood {a,b};
- two decorated vertices x,y, adjacent to one another and to both a,b;
- g_x+g_y=7;
- ab is absent from M.

### 2.1 Pure K2 support classes

For every low u, the subset charge at S={a,b} is

`t_a+t_b=22=d(13-d)` for d=2.

No q31 rise is allowed, so the exact repivot formula is equality. Hence the core support U_u is a K2 on two degree-12 core vertices and is target-anticomplete to {a,b}; repivot at u again has q=30.

Two distinct supports cannot overlap in one vertex: repivot one support, and the retained vertex of the other loses its unique support neighbour and gains no edge to {a,b}, falling from core degree12 to11. Hence distinct supports are disjoint.

The same repivot argument shows two distinct support classes are target-anticomplete.

If the distinct support classes have multiplicities m_1,...,m_c, sum m_i=9, then their vertices contribute at least

`2 sum(m_i-1)=2(9-c)`

to the ambient excess above degree13. The shell already contributes G=7 and the total E406 ambient excess is19, so the core has only12 ambient excess units available. Therefore c>=3. Alpha(C)<=4 and pairwise anticompleteness give c<=4.

### 2.2 Four classes impossible

If c=4, let U be their eight vertices and K=C\U, |K|=39. Each support vertex has core degree12, one neighbour inside its K2, and no cross edges to the other support classes. Hence

`e(U)=4`, `e(U,K)=88`, `e(K)=193`,

and

`sum_{v in K}(d_C(v)-12)=6`.

Every v in K is complete to at least one support K2; otherwise choose one nonneighbour from each of the four pairwise anticomplete K2 classes and add v to obtain an independent5-set.

Repivoting the corresponding support replaces that K2 by {a,b}. The new core again has285 edges and minimum degree12. Thus a vertex v complete to the removed K2 obeys

`epsilon_v+r_ab(v)>=2`,

where r_ab counts its neighbours among {a,b}.

Summing over all39 vertices of K requires at least78. But the epsilon sum is6, and the two rows a,b have total size22 and are anticomplete to U, so

`sum_K r_ab=22`.

The left side is only28. Contradiction.

### 2.3 Three classes impossible

If c=3, the support contribution lower bound is12, exactly the entire core ambient-excess budget 19-G=12. Therefore equality holds everywhere:

- support vertices have no shell neighbours beyond their low-row multiplicities;
- every vertex v in K=C\U has ambient excess0.

Here |U|=6, |K|=41. Core counting gives again

`sum_K epsilon_v=6`.

For v in K, ambient excess0 means

`epsilon_v+r_shell(v)=1`.

In particular `epsilon_v in {0,1}`.

The decorated shell vertex x is target-anticomplete to every support class by the support equality above. If v is target-nonadjacent to x and is not complete to any of the three support K2s, then choose one v-nonneighbour from each K2; together with v and x these form an independent5-set. Hence every v outside the core row of x must be complete to some support K2.

For such a v, repivot that support class. Minimum degree12 in the new q30 core requires

`epsilon_v+r_ab(v)>=2`.

But v is not adjacent to x, and all low shell rows land entirely in U, so its shell neighbours can only be among a,b,y. Since `epsilon_v+r_shell(v)=1`, we have

`epsilon_v+r_ab(v)<=1`,

contradiction. Since x has row size at most13<41, such v certainly exists.

Thus the ab-nonedge branch is empty.

## 3. Case ab in E(M)

Let

`delta=(12-d_M(a))+(12-d_M(b)) in {0,1,2}`.

There are exactly delta missing high-to-(L union D) incidences. Let r_L be those falling on L, let s=e_M(L,D), and let j=e(M[D]). Since a low vertex has degree at most2,

`s<=r_L<=delta`.

Exact edge and charge counting gives

`G=7+delta-s-j`.                                      (A)

### 3.1 delta=2 is impossible

Both high vertices have weight11. Any ordinary low adjacent to both has d=2 and subset charge

`t_a+t_b-e_M(ab)=11+11-1=21<22=d(13-d)`.

Its repivot therefore has q>=31, forbidden.

But at most r_L+s<=4 low vertices can be exceptional, while k<=3 whenever j>0 (see below), and when j=0 the same low-D edge estimate forces k=1. Thus l=11-k>=8, leaving an ordinary low. Contradiction.

For completeness, when j>0 and xy is a D-edge,

- `d_J(x)+d_J(y)<=j+1`;
- `g_x+g_y<=G-(k-2)`;
- the two endpoints together have at most four high incidences and at most s low incidences.

PAIR-13 yields

`13<=t_x+t_y<=14+delta-k`,

so `k<=1+delta=3`.

If j=0, alpha(M)<=10 forces s>=1. A low-D edge requires its decorated endpoint to have weight at least11; using (A) gives k<=delta-1=1. Hence the preceding ordinary-low argument covers all delta=2 states.

### 3.2 delta=0 is impossible

Here s=0. If j=0, the 11 vertices L union D are independent in M, contradicting alpha(M)<=10.

If j>0, the preceding D-edge bound gives k<=1, impossible for an internal D-edge. Thus delta=0 is empty.

### 3.3 delta=1 is impossible

The D-edge bound gives k<=2. The j=0 alternative is impossible by the low-D edge estimate, so k=2 and j=1.

Equation (A) gives

`G=7-s`, with `s in {0,1}`.

The unique high deficit must fall on L; otherwise the two decorated endpoints of the unique J-edge have total row weight at most12, violating PAIR-13. Hence exactly one low misses one high.

There are eight ordinary lows with neighbourhood {a,b}. For each such low the d=2 repivot is an exact q30 plateau with a pure K2 degree-12 support anticomplete to {a,b}; distinct support classes are disjoint and pairwise anticomplete as above.

Let a support class have multiplicity m. After repivot, its two degree-12 support vertices enter the new shell with total decoration at least `2(m-1)`, while the old decorated vertices remain in the shell and still contribute `G=7-s`. Since any q30 shell has decoration at most8,

`7-s+2(m-1)<=8`.

If s=0 this forbids every repeated class, but eight rows and at most four pairwise-antocomplete K2 classes force repetition. Contradiction.

If s=1, every class has multiplicity at most2. Eight rows therefore force exactly four support classes of multiplicity2. The four-class summation argument of Section 2.2 applies verbatim; now the two high rows have total size23 rather than22, so its left side is at most `6+23=29`, still far below the required78. Contradiction.

Thus delta=1 is empty.

## 4. Conclusion

Every q30 no-q31 extreme shell with exactly two undecorated high vertices is impossible.

Together with the initial counting bound h<=2, any remaining extreme plateau must have

`h in {0,1}`.