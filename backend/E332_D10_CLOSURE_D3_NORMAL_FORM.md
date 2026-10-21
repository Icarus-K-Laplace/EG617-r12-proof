# E332 q30 equality: d10 branch closure and exact d3 terminal

Status: `PROVED` for every statement explicitly labelled proved below. The full E332 layer remains `OPEN`.

## Setup

Assume a legitimate residual `F in R(4,49)` with `e(F)=332` and a degree-13 pivot `p` whose 13-shell has charge `q=30` and whose 35-core `H` has `e(H)=211`.

The clean CORE211 equality state gives

- `delta(H)>=12`;
- degree multiset `14,12^34` or `13^2,12^33`.

For an undecorated shell vertex y, the exact repivot inequality plus the fixed E332 edge count implies that `d_M(y)=3` or `10` is a zero-slack equality channel. In either channel the complementary shell side is missing-edge-free and undecorated, and the core row of y is a clique of degree-12 core vertices.

---

## 1. Any d10 equality root forces a pure K3,10 shell — PROVED

Let y be an undecorated shell vertex with `d_M(y)=10`.

The d10 equality normal form splits the shell as

- `C`, size 3, containing y;
- `S`, size 10;

with M bipartite between C and S, no missing edges inside either side, every vertex of C undecorated, and for every `s in S`

`d_M(s)+g_s=3`.

All decorations are therefore supported on S. Since the 14-point shell cap gives `z=e(M)>=22` and `q=z+G=30`, we have `G<=8`. Hence among the ten vertices of S there is some `s` with `g_s=0`. For this s,

`d_M(s)=3`,

and its three missing neighbours are exactly C.

Apply the d3 zero-slack equality theorem to s. It forces every shell vertex outside `N_M(s)=C`, namely every vertex of S, to have zero decoration. Thus

`G=0`.

Consequently every `s in S` has missing degree 3, while `z=30`; hence every vertex of C has missing degree 10. Therefore

`M = K_{3,10}`

exactly, with no decoration anywhere.

Thus every C-vertex is a d10 equality root and every S-vertex is a d3 equality root.

---

## 2. Row geometry in the pure K3,10 state — PROVED

For `c in C`, let `D_c` be its 10-vertex core row. The d10 equality theorem gives

- `H[D_c]=K10`;
- every vertex of `D_c` has H-degree 12.

For `s in S`, let `P_s` be its 3-vertex core row. The d3 equality theorem gives

- `H[P_s]=K3`;
- every vertex of `P_s` has H-degree 12.

Moreover d10 equality says S is target-anticomplete to every `D_c`, hence

`P_s intersect D_c = empty`

for all c,s.

Let

`X = union_{c in C} D_c`,
`Y = union_{s in S} P_s`.

Then X and Y are disjoint.

Because every degree-12 core vertex must acquire at least one shell neighbour in the full graph F, while the exceptional degree-13/14 core vertices cannot lie in any equality row, we have the exact coverage:

- if `deg(H)=14,12^34`, then `|X|+|Y|=34` and one exceptional vertex lies outside X union Y;
- if `deg(H)=13^2,12^33`, then `|X|+|Y|=33` and two exceptional vertices lie outside X union Y.

### D-row intersections

For two distinct 10-rows D,D':

- equality is impossible, because the two adjacent shell roots together with a common K10 would form a forbidden K12;
- if they intersect, every common core vertex already sees all `|D union D'|-1=19-r` vertices of the union, where `r=|D intersect D'|`; degree 12 forces `r>=7`;
- hence `r in {0,7,8,9}`;
- if `r=0`, repeated d10 equality makes D and D' target-anticomplete in H.

The triple intersection of all three D-rows has size at most 8, because nine common core vertices together with the three shell roots would form a K12.

### P-row intersections

Repivot at a full d3 root s. For another full root t,

`d_{M_s}(t)=3-|P_s intersect P_t|`.

The new shell is again a q30 equality state. Once the d10 branch is excluded (proved below), missing degrees 1 and 2 on the undecorated 10-side are profitable and therefore impossible. Hence distinct P-rows are either equal or disjoint.

For disjoint rows, d3 equality makes them target-anticomplete in H.

A row-equivalence class has size at most 3: if c copies of the same triangle occur, repivoting at one copy makes each of its three core vertices carry new decoration at least `c-1`, so the new decoration total is at least `3(c-1)<=8`.

---

## 3. The d10 branch is impossible — PROVED

We now eliminate every possible geometry of the three D-rows.

### Case A: all three D-rows pairwise overlap

Each pair overlap is at least 7, and the triple overlap is at most 8. Therefore

`|X| <= 30-7-7-7+8 = 17`.

The exact coverage above gives `|Y|>=16`.

But after the P-row intersection analysis, distinct P-triangles are edge-disjoint and every H-edge inside Y lies in one of at most ten distinct row triangles. Hence

`e(H[Y]) <= 30`.

Since `alpha(H[Y])<=3`, Turan's K4 bound on the complement gives

`e(H[Y]) >= C(|Y|,2)-floor(|Y|^2/3)`.

For `|Y|>=16` the right side is at least 35, contradiction.

### Case B: all three D-rows pairwise disjoint

Then `|X|=30`, so exact coverage gives `|Y|=3` or 4.

There are ten P-rows and every row class has size at most 3, so at least four distinct P-triangles are required.

This is impossible on 3 vertices. On 4 vertices, any two distinct 3-subsets intersect in two vertices, but intersection size 2 is forbidden by the repivot pair-row coverage argument. Contradiction.

### Case C: exactly one D-pair overlaps

If two different pairs overlapped while the third pair were disjoint, one 10-set would contain two disjoint intersections of size at least 7, impossible. Thus the only remaining pattern is:

- `D1,D2` overlap in `r in {7,8,9}`;
- `D3` is disjoint from both and therefore anticomplete to `D1 union D2`.

Let

`A=D1\D2`, `B=D2\D1`, `c=e_H(A,B)`.

Then

`|X|=30-r`,
`e(H[X])=135-C(r,2)+c`.

Every X-vertex has H-degree 12, so if `O=H-X`,

`e_H(X,O)=12|X|-2e(H[X])`,

and therefore

`e(H[O]) = 211 + e(H[X]) - 12|X|`.

Explicitly:

- r=7: `e(O)=49+c`;
- r=8: `e(O)=54+c`;
- r=9: `e(O)=58+c`.

On the other hand O consists of Y plus one or two exceptional core vertices, and `e(H[Y])<=30`.

For r=8 or 9, even adding all possible edges incident to the exceptional vertices gives an upper bound below the displayed required value; hence both r=8 and r=9 are impossible.

For r=7 with core degree multiset `14,12^34`, `|Y|=11` and there is one exceptional vertex, so

`e(O)<=30+11=41<49+c`,

impossible.

The sole numerical residue is therefore:

- core degree multiset `13^2,12^33`;
- r=7;
- `|Y|=10`, two exceptional vertices;
- the crude edge bound forces `c<=2`.

But now A and B both have size 3, while `c<=2`, so there is a nonedge `ab` with `a in A`, `b in B`.

Choose any `d in D3`. Since D3 is anticomplete to `D1 union D2`, the triple `{a,b,d}` is independent in H.

Each of a and b has at most 3 neighbours in O (indeed `3-deg_B(a)` and `3-deg_A(b)`), and d has exactly 3 neighbours in O. Hence

`|N_O(a) union N_O(b) union N_O(d)| <= 9 < |O|=12`.

Some `o in O` is nonadjacent to all three, so `{a,b,d,o}` is an independent 4-set in H, contradicting `alpha(H)<=3`.

Thus Case C is impossible as well.

Therefore:

> **D10-CLOSURE. No E332 q30+211 survivor contains an undecorated shell vertex of missing degree 10.**

---

## 4. Surviving d3 shells collapse to two exact types — PROVED

Assume now that a q30 equality shell contains a d3 root y. Its zero-slack normal form is bipartite between

- a 3-vertex centre side T;
- a 10-vertex leaf side U;

with no internal missing edges, all U-vertices undecorated, and every centre having row weight exactly 10.

Because d10 roots are impossible, every centre must have positive decoration.

Let an undecorated leaf u have missing degree d. Since its missing neighbours lie in T and each centre has weight 10,

`q_u-q >= d(13-d)-10d = d(3-d)`.

Thus d=1 or 2 would be profitable, impossible in E332. Every leaf therefore has missing degree only 0 or 3.

Let k be the number of degree-3 leaves. Then each centre has missing degree k, hence decoration `10-k`. Therefore

`G=3(10-k)`.

Since `1<=10-k` and `G<=8`, only

`k=9` or `k=8`

are possible.

Hence every surviving d3 shell is exactly one of:

- **Type A:** `M=K_{3,9} disjoint_union K1`, with centre decorations `(1,1,1)`;
- **Type B:** `M=K_{3,8} disjoint_union 2K1`, with centre decorations `(2,2,2)`.

For every degree-3 leaf its core row is a degree-12 triangle.

---

## 5. Row-class dynamics of the two d3 types — PROVED

Take a full degree-3 leaf y with triangle row `P_y`, and repivot at y.

For another full leaf u,

`d_{M_y}(u)=3-|P_u intersect P_y|`.

The new q30 shell must again be Type A or B. Since degrees 1 and 2 are impossible, two distinct full-leaf rows are either equal or disjoint. Disjoint row triangles are target-anticomplete in the core.

Let c be the size of the row-equivalence class of `P_y`. The new full-leaf count is

`k' = 1 + (# old isolates) + (# old full leaves outside the class) = 11-c`.

Since `k'` must be 8 or 9,

`c in {2,3}`.

Distinct row classes are pairwise anticomplete triangles in H, so `alpha(H)<=3` allows at most three classes.

Therefore the class structure is forced:

- Type A (`k=9`): exactly `3+3+3`;
- Type B (`k=8`): exactly `3+3+2`.

Repivoting a size-3 class sends Type A to Type B; the inserted old centre triangle becomes the size-2 class. Repivoting the size-2 class in Type B returns to Type A. Thus the remaining equality dynamics is an explicit two-state triangle-switching system.

---

## 6. Exact 26-vertex core remainder — PROVED

In either Type A or Type B, the three distinct row triangles are pairwise disjoint, pairwise anticomplete, and every one of their nine vertices has H-degree 12.

Let J be the other 26 core vertices.

Each triangle contributes 3 internal edges and sends exactly 30 edges to J. Therefore

`e(H[J]) = 211 - 3*3 - 3*30 = 112`.

Every `x in J` must be complete to at least one of the three triangles; otherwise one may choose a non-neighbour of x from each triangle, producing an independent 4-set in H.

If `a(x)` is the number of H-edges from x to the three triangles, then

`a(x)>=3`,
`sum_{x in J} a(x)=90`.

Thus the total slack above the mandatory 3-per-vertex coverage is only

`90-26*3=12`.

Moreover all core degree excess (=2) lies inside J. Writing `h_x=d_H(x)-12`,

`d_{H[J]}(x)=12+h_x-a(x)`,

with `sum h_x=2`.

This 26-vertex, 112-edge near-Turan object together with the Type A/B triangle-switching rule is the new canonical Line C terminal.

## Current Line C frontier

E332 is not yet closed. The d10 branch is closed completely. Any survivor containing a d3 equality root must lie in the two-state system above:

`Type A: K3,9 + K1, decorations 1,1,1, row classes 3+3+3`

or

`Type B: K3,8 + 2K1, decorations 2,2,2, row classes 3+3+2`,

and the 211-core contains three pairwise anticomplete degree-12 triangles over a 26-vertex 112-edge remainder J with only 12 units of triangle-incidence slack.

The next target is to use the near-extremal complement of J (`K4`-free on 26 vertices with 213 edges), the 12-unit slack, and the triangle-switching dynamics to eliminate both Type A and Type B.
