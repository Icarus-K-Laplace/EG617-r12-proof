# E408 Q32 — all exact-color counts are impossible

Updated: 2026-10-27  
Status: **PROVED_CONDITIONAL Q32 CONTRADICTION** under the registered E408/T61 residual contract, exact-129 Type-I classification, exceptional injectivity, full-color pointwise degree floors, and the cited Brouwer--Kang--Pikhurko second-Turan theorem.

## 1. Frozen residual contract

Let F be the 61-vertex E408 target residual. For the eleven non-target colors C,

\[
e_C(R)=129+s_C,\qquad s_C\ge0,\qquad \sum_C s_C=3.
\]

An exact color has s=0. Hence the number m of exact-129 colors lies in
\[
\boxed{m\in\{8,9,10\}}.
\]

For every exact color, the Type-I equality graph has one exceptional vertex of color-degree nine and all other residual vertices have color-degree at least four. `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md` proves that a residual vertex cannot be exceptional for two different exact colors, so the m exact colors have m distinct exceptional vertices.

We use the independently proved full-color pointwise floors:

- s=0: minimum color degree at least 4;
- s=1: minimum color degree at least 3;
- s>=2 in the E408 frontier: minimum color degree at least 2.

We also use the complement form of Brouwer's theorem. If a graph G has n vertices, alpha(G)<=r, omega(G)<=5, and n>5r, then \(\overline G\) is K_{r+1}-free and non-r-partite, so

\[
e(G)\ge p_r(n)+\left\lfloor\frac nr\right\rfloor-1.
\]

This is precisely the Brouwer / Kang--Pikhurko non-r-partite Turan bound applied to the complement.

## 2. Low-degree lemmas for nonexact colors

### Lemma 2.1 — a 131-edge color has minimum degree at least three

Let D have e(D)=131, alpha(D)<=12, omega(D)<=5. Suppose d_D(v)=2. Let N be the 58 non-neighbours of v, excluding v. Since v is anticomplete to N, alpha(D[N])<=11 and omega(D[N])<=5. Since 58>55,

\[
e(D[N])\ge p_{11}(58)+\lfloor58/11\rfloor-1=125+5-1=129.
\]

The two edges incident to v already use the remaining two edges of D. Therefore no further edge can touch either neighbour of v, so both would have degree one, contradicting the registered s>=2 degree floor two. Hence

\[
\boxed{\delta(D)\ge3\quad\text{for }e(D)=131.}
\]

### Lemma 2.2 — degree-three vertices of a 130-edge color form isolated K4 components

Let D have e(D)=130, alpha(D)<=12, omega(D)<=5, and d_D(v)=3. Let N be the 57 non-neighbours of v and S=N_D(v), |S|=3. Then alpha(D[N])<=11 and omega(D[N])<=5, so

\[
e(D[N])\ge p_{11}(57)+\lfloor57/11\rfloor-1=120+5-1=124.
\]

After the 124 edges in N and the three v--S edges, at most three edges remain. Every point of S has degree at least three, so after its edge to v the three vertices of S require at least six further degree incidences. Three edges can supply at most six incidences, with equality only when all three are internal to S. Thus S is a triangle, there are no S--N edges, and

\[
D[\{v\}\cup S]=K_4
\]

is an isolated component. All four of its vertices have degree exactly three.

Therefore all degree-three vertices of a 130-edge color are partitioned into isolated K4 components.

### Lemma 2.3 — a 130-edge color has at most four degree-three vertices

Two isolated K4 components are already impossible. If D contained two, delete their eight vertices. The remaining graph D' has

\[
|V(D')|=53,\qquad e(D')=130-2\cdot6=118.
\]

Every independent set of D' can be enlarged by one vertex from each deleted K4, so alpha(D')<=10. Also omega(D')<=5. Since 53>50,

\[
e(D')\ge p_{10}(53)+\lfloor53/10\rfloor-1
=115+5-1=119,
\]

contradicting e(D')=118. Hence D has at most one isolated K4. By Lemma 2.2,

\[
\boxed{\#\{v:d_D(v)=3\}\le4\quad\text{for every }130\text{-edge non-target color}.}
\]

### Lemma 2.4 — degree-two vertices of a 132-edge color lie in isolated triangles

Let D have e(D)=132 and d_D(v)=2. The same 58-point non-neighbourhood argument gives e(D[N])>=129. Beyond N and the two v-edges there is room for at most one additional edge. Both neighbours of v have degree at least two, so that edge must join them; no edge joins them to N. Thus v and its two neighbours form an isolated K3 and all three have degree two.

Therefore all degree-two vertices occur in disjoint isolated triangles.

Four such components are impossible: deleting four isolated K3s leaves 49 vertices, 120 edges, and independence number at most eight, whereas the elementary Turan lower bound gives

\[
p_8(49)=126>120.
\]

Hence a 132-edge non-target color has at most nine degree-two vertices.

## 3. Exclude m=10

If m=10, the unique nonexact color D has s=3 and e(D)=132.

At an exact exceptional vertex x:

- its own exact color contributes degree 9;
- the other nine exact colors contribute at least 4 each;
- the target color contributes at least 13.

Thus

\[
d_D(x)\le60-13-9-9\cdot4=2.
\]

The s>=2 pointwise floor gives equality d_D(x)=2. Exceptional injectivity provides ten distinct exact exceptional vertices, so D has at least ten degree-two vertices. Lemma 2.4 says degree-two vertices occur in isolated triangles, hence their number is a multiple of three; at least ten forces at least twelve, i.e. four isolated triangles. Lemma 2.4 excludes four. Contradiction.

Therefore
\[
\boxed{m\ne10.}
\]

## 4. Exclude m=9

If m=9, the two nonexact colors have positive excesses 1 and 2. Call them D_1 and D_2, with 130 and 131 edges.

At an exact exceptional vertex x,

\[
d_{D_1}(x)+d_{D_2}(x)
\le60-13-9-8\cdot4=6.
\]

Lemma 2.1 gives d_{D_2}(x)>=3, and the s=1 pointwise theorem gives d_{D_1}(x)>=3. Therefore both equal three at every exact exceptional vertex.

The nine exact exceptional vertices are distinct, so D_1 has at least nine degree-three vertices. Lemma 2.3 permits at most four. Contradiction.

Therefore
\[
\boxed{m\ne9.}
\]

## 5. Exclude m=8

If m=8, the three nonexact colors must all have s=1 and hence exactly 130 residual edges. Call them D_1,D_2,D_3.

At any exact exceptional vertex x, the eight exact colors contribute at least

\[
9+7\cdot4=37
\]
non-target degree and the target contributes at least 13. Therefore

\[
d_{D_1}(x)+d_{D_2}(x)+d_{D_3}(x)\le10.
\]

Each D_i has minimum degree at least three. If fewer than two of the three degrees were exactly three, their sum would be at least
\[
3+4+4=11,
\]
a contradiction. Hence **at least two of D_1,D_2,D_3 have degree exactly three at every exact exceptional vertex**.

Exceptional injectivity gives eight distinct exceptional vertices. Thus the three 130-edge colors together must supply at least
\[
2\cdot8=16
\]
degree-three incidences on those vertices.

But Lemma 2.3 gives at most four degree-three vertices per 130-edge color, hence at most
\[
3\cdot4=12
\]
such incidences in total. Contradiction.

Therefore
\[
\boxed{m\ne8.}
\]

## 6. Q32 contradiction

The outer equality system forces m in {8,9,10}. Sections 3--5 exclude all three possibilities. Therefore the registered E408 Q32 residual contract has no realization:

\[
\boxed{\text{E408 Q32 is PROVED_CONDITIONAL impossible}.}
\]

This argument is stronger than the earlier support analysis: it does **not** require the v>=44 theorem, the v=47 full-support reduction, the 285-edge witness-capacity inequality, or any Q33 284-edge statement. Those remain valid audits but are no longer load-bearing for Q32 closure.

## 7. Dependency firewall

Load-bearing inputs are only:

1. the E408 residual equality ledger \(\sum s_C=3\);
2. exact-129 Type-I degree structure: one degree-nine exceptional vertex, all ordinary residual vertices degree at least four;
3. `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md`;
4. the independently proved pointwise degree floors for s=1 and s>=2 colors;
5. alpha(C)<=12 and omega(C)<=5 for every non-target residual color;
6. Brouwer / Kang--Pikhurko non-r-partite Turan bound in the complement form used above;
7. target minimum degree thirteen and the fact that all twelve colors partition the 60 edges at every residual vertex.

No Q33 284-edge identity, support-41 theorem, shell split M[B]=empty, or speculative graph enumeration is used.

EG617(r=12) itself remains OPEN / NOT_CERTIFIED until the upstream reduction and all other registered terminal/backend obligations are reconciled.