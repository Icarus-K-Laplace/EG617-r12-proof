# E406 low-charge promotion: q22--q26

Status: `PROVED` under the standard T61 h13 shell contract plus `delta(C)>=11` for the 47-core.

## Statement

Let p be a degree-13 pivot in an E406 T61 parent. Write A for its 13-shell, C for the 47-core, M for the shell missing graph, decorations g, row weights `t=d_M+g`, and shell charge q.

Assume the standard inherited facts:

- `z=e(M)>=22`;
- `alpha(M)<=10`;
- M contains a 3-matching;
- every M-edge has endpoint row-weight sum at least11;
- every M-triangle has row-weight sum at least24;
- every M-K4 has row-weight sum at least36;
- `delta(C)>=11`;
- exact subset and repivot identities.

Then:

1. `q<=23` is impossible;
2. every `q=24,25,26` pivot has a legal degree-13 repivot y with `q_y>=27`.

The repivot lower bound used below is the delta(C)>=11 form

`q_y-q >= d(12-d)-[t(S)-e_M(S)]`,

for an undecorated shell vertex y with `d=d_M(y)` and `S=N_M(y)`.

Because an M-K4 would give `q>=36-6=30`, every shell with q<=26 is K4-free.

---

## 1. q<=23 is impossible

If M is triangle-free, take the six endpoints S of a 3-matching. Pair coverage gives

`t(S)>=33`,

while Mantel gives `e_M(S)<=9`. Hence

`q>=t(S)-e_M(S)>=24`,

contradiction.

So M contains a triangle T. Put B=A\T, |B|=10, and `u=e_M(B)`.

The triangle subset identity gives

`q=t(T)-3+u+G_B`.

Since `t(T)>=24`,

`u+G_B<=q-21<=2`.      (1)

If rs were an M-edge inside B, K4-freeness gives at most four total T-incidences from r,s, while

`d_B(r)+d_B(s)<=u+1`.

Therefore

`t_r+t_s<=4+(u+1)+G_B<=7<11`,

contradicting pair coverage. Thus `u=0`.

### q=22

Now G=0, z=22, so the T--B cross count is19. Thus nine B-vertices have T-degree2 and one has T-degree1, all regular.

If all three triangle vertices meet a regular degree2 B-vertex, each has weight at least9, so `t(T)>=27`, while the identity gives `t(T)=25`. Contradiction.

Hence some triangle vertex meets no regular degree2 B-vertex. Its only possible B-neighbour is the unique degree1 point, but that edge would require triangle weight at least10, while the other two triangle vertices each require weight at least9; again `t(T)>25`. Therefore that triangle vertex has no B-neighbour, and B together with it is an independent11-set in M, contradicting `alpha(M)<=10`.

### q=23

Here G<=1. If G=0, all ten B-vertices have T-degree2 and `t(T)=26`; all three triangle vertices meet regular degree2 points and would each have weight at least9, contradiction.

If G=1, the T--B cross count is19. At least eight of the nine degree2 B-vertices are regular. If all triangle vertices meet one, again `t(T)>=27>26-G_B`.

Otherwise a triangle vertex has no regular degree2 neighbour. Its possible neighbours are only the unique decorated B-vertex and/or the unique degree1 point. The one-unit decoration budget makes its own row weight at most4, whereas either possible missing edge requires weight at least8 or9. Hence it has no B-neighbour, giving an independent11-set in M. Contradiction.

Thus q<=23 is impossible.

---

## 2. q=24 promotes to q>=27

### Triangle case

The same argument gives `u=0`. The T--B cross count is `21-G`, so G>=1.

If G=1, all ten B-vertices have missing degree2. The only viable placement has `G_B=0` and triangle weights `(9,9,9)`; any regular B-vertex y has a 2-point missing neighbourhood which is an M-edge, so

`t(S)-e_M(S)=9+9-1=17`.

Hence

`q_y-q>=20-17=3`,

so `q_y>=27`.

If G=2, the cross count is19. The same budget argument excludes a triangle vertex with no regular degree2 neighbour. Thus `G_B=0`, all three triangle weights are9, and a regular degree2 B-vertex again gives q_y>=27.

### Triangle-free case

For a 3-matching endpoint set S, equality in

`24>=33-e_M(S)`

forces

- `M[S]=K3,3`;
- `t(S)=33`;
- the seven outside vertices are M-independent and undecorated.

A 4-matching would force q>=28, so `nu(M)=3`. The graph is bipartite; Konig gives a size-3 cover X which is one side of the K3,3. All outside attachments meet X.

The opposite K3,3 side has no outside attachments. Summing the nine pair inequalities gives equality on every K3,3 edge, so the X-weights are all8 and the opposite-side weights all3.

The number of X--outside edges is `15-G`. Every nonisolated outside vertex is regular and, against weight8, must have missing degree3 and meet all of X. Hence `15-G` is divisible by3. With `G<=2`, this forces G=0.

Thus

`M=K3,8 disjoint_union 2K1`.

Any large-side nonisolated vertex y is regular of missing degree3, with

`t(X)-e_M(X)=24`.

Therefore

`q_y-q>=27-24=3`,

and q_y>=27.

---

## 3. q=25 promotes to q>=27

### Triangle case

The triangle identity gives `u+G_B<=4`; an edge inside B would have endpoint-weight sum at most9, so again `u=0`. The cross count is `22-G`, hence G is2 or3.

For G=2 all B-vertices have missing degree2. For G=3, nine have degree2 and one degree1. A triangle vertex with no regular degree2 neighbour is impossible by the same decoration-budget versus pair-coverage estimate used above.

Hence every triangle vertex meets a regular degree2 B-vertex and has weight at least9. For any regular degree2 y, if k is the triangle vertex it misses, then

`t(N_M(y)) = t(T)-t_k <= (28-G_B)-9 <=19`.

Since the two neighbours of y form an M-edge,

`t(N_M(y))-e_M(N_M(y))<=18`.

Thus

`q_y-q>=20-18>=2`,

so q_y>=27.

### Triangle-free case

A 4-matching gives q>=28, so `nu(M)=3`. A shortest-odd-cycle argument excludes nonbipartite M: a C7 already exceeds q25, while a C5 leaves outside charge at most2 and is incompatible with the matching-number3 / cross-incidence count. Hence M is bipartite.

Let X be a size-3 Konig cover and Y=A\X, |Y|=10, so Y is independent.

A regular y in Y of missing degree3 immediately gives

`t(X)-e_M(X)=25-G_Y<=25`

and therefore

`q_y-q>=27-(25-G_Y)>=2`.

Assume no such regular degree3 vertex exists.

If `e_M(X)>0`, no Y-vertex can have degree3 without forming a triangle. Then all ten Y-vertices have degree at most2. The required X--Y edge count is `25-G-e_M(X)`; for G<=2 this already exceeds20. For G=3 the only numerical equality is `e_M(X)=2` and 20 cross edges, which forces every Y-vertex to use the unique nonadjacent pair of X. The third X-vertex together with Y is then an M-independent11-set, impossible.

Thus `e_M(X)=0`. The cross count is `25-G`. If no regular degree3 vertex exists, every edge above the base capacity20 must be supplied by decorated degree3 Y-vertices. For G<=2 there is insufficient decoration budget. Hence G=3 and there are at least two decorated degree3 Y-vertices.

At least one such vertex has decoration1, hence row weight4; pair coverage forces all three X-weights to be at least7. Their total weight is at most23. Any regular degree2 Y-vertex whose two X-neighbours had weight sum at least19 would leave the third X-weight at most4, contradiction. Therefore some regular degree2 y has neighbour-weight sum at most18, giving

`q_y-q>=20-18=2`.

So q_y>=27.

---

## 4. q=26 promotes to q>=27

### Triangle case

Now `u+G_B<=5`, and an edge inside B would have endpoint row-weight sum at most10, contradicting pair coverage. Thus u=0.

The T--B cross count is `23-G`, so G is3 or4. A triangle vertex with no regular degree2 B-neighbour is again excluded by the decoration budget. Thus each triangle vertex has weight at least9.

For a regular degree2 B-vertex y,

`t(N_M(y)) <= (29-G_B)-9 <=20`.

Its two neighbours form an M-edge, so

`t(N_M(y))-e_M(N_M(y))<=19`,

and

`q_y-q>=20-19>=1`.

Hence q_y>=27.

### Triangle-free case

Again `nu(M)=3` and M is bipartite by the same odd-cycle argument. Let X be a size-3 cover and Y the independent10-set.

A regular degree3 y gives

`q_y-q>=27-(26-G_Y)>=1`.

Assume none exists.

If `e_M(X)>0`, no Y-vertex can have degree3. Hence the cross count is at most20. The only possible numerical equality is `G=4`, `e_M(X)=2`, cross count20; as above, this forces every Y-vertex onto the unique nonadjacent X-pair and creates an M-independent11-set. So `e_M(X)=0`.

Now the cross count is `26-G`. To exceed the base capacity20 without regular degree3 vertices requires at least `6-G` decorated degree3 vertices.

- G<=2 is impossible by decoration count.
- G=3 forces three decorated degree3 vertices, each with decoration1. Hence every X-weight is at least7, while their total is23. A regular degree2 vertex with nonprofitable pair sum >=20 would leave the third X-weight <=3, contradiction.
- G=4 requires at least two decorated degree3 vertices. One has decoration at most2, so every X-weight is at least6; their total is at most24. A nonprofitable regular degree2 pair would have sum at least20 and leave the third X-weight at most4, contradiction.

Thus a profitable regular degree2 or degree3 repivot always exists, and q_y>=27.

## Consequence

Within E406, once the independently recorded `delta(C)>=11` 47-core lemma is licensed, the low-charge bridge no longer needs the V7 q25/q26 black box:

- q22,q23: impossible;
- q24,q25,q26: promote to q>=27.

The remaining bridge work begins at q27.
