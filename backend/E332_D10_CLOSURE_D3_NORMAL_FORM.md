# E332 q30 equality: d10 closure, d3 closure, and remaining extreme-degree shell

Status: `PROVED` for the d10 and d3 branches below. The full E332 layer remains `OPEN` only because the existence of a d3/d10 root has not yet been forced.

## Setup

Assume a legitimate residual `F in R(4,49)` with `e(F)=332` and a degree-13 pivot `p` whose 13-shell has charge `q=30` and whose 35-core `H` has `e(H)=211`.

CORE211 equality gives

- `delta(H)>=12`;
- degree multiset `14,12^34` or `13^2,12^33`.

For an undecorated shell vertex y, missing degrees 4..9 are automatically profitable. The equality channels d=3 and d=10 force every nonnegative repivot slack term to vanish.

---

## 1. Any d10 equality root forces a pure K3,10 shell — PROVED

Let y be undecorated with `d_M(y)=10`. The zero-slack normal form splits the shell as a 3-side C and 10-side S, with M bipartite, no internal missing edges, every C-vertex undecorated, and

`d_M(s)+g_s=3` for every `s in S`.

All decoration lies on S. Since `z>=22` and `q=z+G=30`, `G<=8`; therefore some `s in S` has `g_s=0`, hence `d_M(s)=3` and `N_M(s)=C`.

Applying d3 equality at s forces every vertex outside C, namely all of S, to have zero decoration. Thus `G=0`, every S-vertex has missing degree3, every C-vertex has missing degree10, and

`M=K_{3,10}`.

So all three C-vertices are d10 roots and all ten S-vertices are d3 roots.

---

## 2. Row geometry of the pure K3,10 state — PROVED

For `c in C`, let `D_c` be its 10-row. Then `H[D_c]=K10` and all row vertices have H-degree12.

For `s in S`, let `P_s` be its 3-row. Then `H[P_s]=K3` and all row vertices have H-degree12.

D10 equality makes S target-anticomplete to each D_c, hence

`P_s intersect D_c = empty`

for every c,s.

Let `X=union D_c`, `Y=union P_s`. Then X,Y are disjoint. Every degree12 core vertex must belong to X union Y in order to reach full degree at least13, while the exceptional degree13/14 core vertices cannot lie in an equality row. Hence

- in `14,12^34`: `|X|+|Y|=34`, one exceptional vertex outside;
- in `13^2,12^33`: `|X|+|Y|=33`, two exceptional vertices outside.

For two distinct D-rows, equality is impossible (two shell roots plus a common K10 would form K12). If they intersect in r vertices, degree12 of a common vertex forces `r>=7`. Thus

`r in {0,7,8,9}`.

Disjoint D-rows are target-anticomplete. The triple intersection of all three D-rows has size at most8, otherwise nine common core vertices plus the three shell roots form K12.

For P-rows, repivoting gives `d'(u)=3-|P_u intersect P_y|`. Once d10 is excluded, degrees1 and2 on the new undecorated 10-side are profitable, so distinct P-rows are either equal or disjoint. Disjoint P-rows are target-anticomplete. A row class has size at most3.

---

## 3. D10-CLOSURE — PROVED

All possible geometries of the three D-rows are impossible.

### All three overlap

Pair overlaps are at least7 and triple overlap at most8, so

`|X|<=30-7-7-7+8=17`.

Exact coverage gives `|Y|>=16`. Distinct P-triangles are edge-disjoint and supply all edges of H[Y], hence `e(H[Y])<=30`. But `alpha(H[Y])<=3` implies

`e(H[Y]) >= C(|Y|,2)-floor(|Y|^2/3) >=35`,

contradiction.

### All three disjoint

Then `|X|=30`, so `|Y|=3` or4. Ten P-rows with class size at most3 require at least four distinct triangles. Impossible on 3 vertices; on 4 vertices two distinct triples intersect in two vertices, which is forbidden.

### Exactly one overlap pair

The only feasible mixed pattern is `D1,D2` overlapping in `r=7,8,9`, with D3 disjoint from both. Put `A=D1\D2`, `B=D2\D1`, `c=e_H(A,B)`.

Then

`|X|=30-r`,
`e(H[X])=135-C(r,2)+c`.

Since every X-vertex has degree12, for `O=H-X`

`e(H[O])=211+e(H[X])-12|X|`,

namely

- r=7: `49+c`;
- r=8: `54+c`;
- r=9: `58+c`.

Because `e(H[Y])<=30` and O contains only one or two exceptional vertices beyond Y, r=8 and r=9 are numerically impossible. For r=7 the `14,12^34` core is also impossible.

The sole numerical residue is `13^2,12^33`, r=7, `|Y|=10`, two exceptional vertices, and `c<=2`.

Now A and B have size3 and c<=2, so choose a nonedge `ab` across A,B and any `d in D3`. The triple `{a,b,d}` is independent. Each of a,b,d has at most3 neighbours in the 12-vertex set O, so their O-neighbourhood union has size at most9. Some `o in O` is nonadjacent to all three, producing an independent4 in H. Contradiction.

Therefore:

> **No E332 q30+211 survivor contains an undecorated d10 shell vertex.**

---

## 4. Any d3 shell collapses to two exact states — PROVED

Assume a d3 root exists. Its zero-slack shell is bipartite between a 3-vertex centre side T and 10-vertex leaf side U. U is undecorated and every centre has row weight10.

Because d10 is impossible, every centre has positive decoration.

For an undecorated leaf of missing degree d,

`q_y-q >= d(13-d)-10d = d(3-d)`.

Thus d=1,2 are impossible. Leaves have degree only0 or3.

If k leaves have degree3, each centre has missing degree k and decoration `10-k`, so

`G=3(10-k)`.

With positive centre decoration and `G<=8`, only k=9 or8 remain. Hence exactly two shell types:

- **Type A:** `M=K_{3,9}+K1`, centre decorations `(1,1,1)`;
- **Type B:** `M=K_{3,8}+2K1`, centre decorations `(2,2,2)`.

For full leaves, row triangles are equal or disjoint; disjoint classes are target-anticomplete. Repivoting a class of size c gives new full-leaf count `11-c`, so `c in {2,3}`. Since alpha(H)<=3 permits at most three pairwise anticomplete classes:

- Type A has row classes `3+3+3`;
- Type B has row classes `3+3+2`.

A size3 repivot sends A to B; a size2 repivot sends B to A.

---

## 5. The 26-vertex remainder and triangle switching — PROVED

In either state there are three distinct row triangles `P1,P2,P3`, pairwise disjoint and pairwise anticomplete, all degree12 in the current 211-core.

Let J be the other26 core vertices. Each Pi sends30 edges to J, so

`e(H[J])=211-9-90=112`.

Every x in J is complete to at least one Pi; otherwise choosing one non-neighbour of x from each Pi gives an independent4 in H. The total Pi-J incidence is90, only12 above the mandatory baseline `26*3=78`.

All two units of 211-core degree excess lie in J.

---

## 6. D3-CLOSURE via four simultaneous pivot views — PROVED

It suffices to eliminate Type A, because every Type B state contains a size2 row class whose repivot produces Type A.

Work in Type A. Let T be the 3 shell centres and let `P1,P2,P3` be the three size3 row triangles.

The centres T form a target triangle. D3 equality makes T target-anticomplete to every Pi. Each T-vertex has core-row size10, and because it is anticomplete to all three Pi, all ten of those core neighbours lie in J. Hence T also sends exactly30 target edges to J.

Now use four legitimate degree13 pivot views of the SAME graph F:

1. the original pivot p has core triangles `P1,P2,P3` plus J;
2. repivot at a leaf from class P1: the new core triangles are `T,P2,P3` plus J;
3. repivot at a leaf from class P2: the new core triangles are `P1,T,P3` plus J;
4. repivot at a leaf from class P3: the new core triangles are `P1,P2,T` plus J.

In each view the pivot is target-anticomplete to its core, and the three displayed triangles are pairwise target-anticomplete.

Therefore, for every `x in J`, alpha(F)<=4 forces x to be complete to at least one of the three triangles in EACH of the four views. In Boolean form, if `C_T,C_1,C_2,C_3` mean “x is complete to that triangle”, then

- `C1 or C2 or C3`;
- `CT or C2 or C3`;
- `C1 or CT or C3`;
- `C1 or C2 or CT`.

These four conditions imply that x is complete to at least TWO of the four triangles `T,P1,P2,P3`.

Thus every x in J has at least6 target neighbours among the 12 vertices of those four triangles. Summing over `|J|=26` gives at least

`26*6=156`

triangle-to-J incidences.

But each of the four triangles sends exactly30 edges to J, so the actual total is only

`4*30=120`.

Contradiction.

Hence Type A is impossible, and therefore Type B is impossible as well.

> **D3-CLOSURE. No E332 q30+211 survivor contains an undecorated shell vertex of missing degree 3.**

---

## 7. Current E332 terminal — OPEN

Combining the generic profitable range with D10-CLOSURE and D3-CLOSURE, any remaining q30+211 shell must satisfy:

> every undecorated shell vertex has missing degree in `{0,1,2,11,12}`.

Degrees 3 through10 are now completely eliminated for undecorated shell vertices.

The next task is therefore no longer row-class geometry. It is an **extreme-degree shell theorem**: prove that a q30 shell with `z>=22`, `G<=8`, `alpha(M)<=10`, pair/triangle row-cover constraints, and regular degree set `{0,1,2,11,12}` cannot exist.

This is now the sole Line C obstruction to closing E332.
