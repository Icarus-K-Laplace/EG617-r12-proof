# E408 Q32 — exact-color count collapses to m=8

Updated: 2026-10-27  
Status: **PROVED_CONDITIONAL** under the registered E408/T61 residual contract and the cited Brouwer--Kang--Pikhurko second-Turan theorem.

## 1. Frozen residual contract

Let F be the 61-vertex E408 target residual. For the eleven non-target colors C,

\[
e_C(R)=129+s_C,\qquad s_C\ge0,\qquad \sum_C s_C=3.
\]

An exact color has s=0. Therefore the number m of exact-129 colors lies in \(\{8,9,10\}\).

For every exact color, the Type-I equality graph has one exceptional vertex of color-degree nine; all other residual vertices have color-degree at least four. `Q32_GLOBAL_EXCEPTIONAL_INJECTIVITY.md` proves that a residual vertex cannot be the exceptional vertex for two different exact colors. Hence the m exact colors have m distinct exceptional vertices.

We use the independently proved full-color pointwise floors:

- s=0: minimum color degree at least 4;
- s=1: minimum color degree at least 3;
- s>=2 in the E408 frontier: minimum color degree at least 2.

We also use the following form of Brouwer's theorem. If G has n vertices, independence number at most r, clique number at most five, and n>5r, then the complement is K_{r+1}-free and non-r-partite, so

\[
e(G)\ge p_r(n)+\left\lfloor\frac nr\right\rfloor-1.
\]

This is the complement form of the Brouwer / Kang--Pikhurko non-r-partite Turan bound.

## 2. Low-degree lemmas for nonexact colors

### Lemma 2.1 — an s=2 color has no degree-two vertex

Let D have e(D)=131, alpha(D)<=12, omega(D)<=5. Suppose d_D(v)=2. Let N be the 58 non-neighbours of v, excluding v. Since v is anticomplete to N, alpha(D[N])<=11; also omega(D[N])<=5. Because 58>55,

\[
e(D[N])\ge p_{11}(58)+\lfloor58/11\rfloor-1=125+5-1=129.
\]

The two edges at v already use the remaining two edges of D. Thus no edge can join the two neighbours of v to each other or to N. Both neighbours would have degree one, contradicting the registered s>=2 minimum-degree floor two. Hence

\[
\boxed{\delta(D)\ge3\quad\text{when }e(D)=131.}
\]

### Lemma 2.2 — degree-three vertices of an s=1 color form isolated K4 components

Let D have e(D)=130, alpha(D)<=12, omega(D)<=5, and let d_D(v)=3. Let N be the 57 non-neighbours of v and S=N_D(v), |S|=3. Again alpha(D[N])<=11 and omega(D[N])<=5. Since 57>55,

\[
e(D[N])\ge p_{11}(57)+\lfloor57/11\rfloor-1=120+5-1=124.
\]

After the 124 edges in N and the three edges from v to S, at most three edges remain. Every point of S has degree at least three, so after its edge to v the three vertices of S need at least six further degree incidences. Three remaining edges can supply at most six incidences, with equality only when all three edges lie inside S. Therefore S is a triangle, there are no S--N edges, and

\[
D[\{v\}\cup S]=K_4
\]

is an isolated component. Every vertex of that K4 has degree exactly three.

Thus all degree-three vertices of a 130-edge color are partitioned into isolated K4 components.

### Lemma 2.3 — an s=1 color has at most eight degree-three vertices

If D had at least nine degree-three vertices, Lemma 2.2 would give at least three isolated K4 components. Delete any three of them. The remaining graph D' has

\[
|V(D')|=49,\qquad e(D')=130-3\cdot6=112.
\]

Every independent set of D' can be enlarged by one vertex from each deleted K4, hence alpha(D')<=9. Also omega(D')<=5. Since 49>45,

\[
e(D')\ge p_9(49)+\lfloor49/9\rfloor-1=110+5-1=114,
\]

contradicting e(D')=112. Therefore

\[
\boxed{\#\{v:d_D(v)=3\}\le8\quad\text{for every }130\text{-edge non-target color}.}
\]

### Lemma 2.4 — degree-two vertices of a 132-edge color lie in isolated triangles

Let D have e(D)=132 and let d_D(v)=2. The same 58-point non-neighbourhood argument gives e(D[N])>=129. Beyond N and the two v-edges there is room for at most one further edge. Both neighbours of v have degree at least two, so that one edge must join them. No edge joins them to N. Hence v and its two neighbours form an isolated K3, and all three have degree two.

Consequently all degree-two vertices of D occur in disjoint isolated K3 components.

Four such components are impossible: deleting four isolated triangles leaves a 49-vertex graph with

\[
e=132-4\cdot3=120,
\]

and independence number at most 8. But Turan's elementary lower bound gives

\[
p_8(49)=126>120.
\]

Therefore a 132-edge non-target color has at most nine degree-two vertices.

## 3. Exclude m=10

If m=10, the unique nonexact color D has s=3 and e(D)=132.

Let x be an exceptional vertex of one exact color. At x:

- its own exact color contributes degree 9;
- the other nine exact colors contribute at least 4 each;
- the target color contributes at least 13.

Since the complete-graph degree is 60,

\[
d_D(x)\le60-13-9-9\cdot4=2.
\]

The s>=2 pointwise floor gives d_D(x)>=2, so every exact exceptional vertex has D-degree exactly two. Exceptional injectivity gives ten distinct such vertices.

By Lemma 2.4, degree-two vertices occur in isolated K3 components, hence their number is a multiple of three. Ten distinct degree-two vertices force at least twelve, i.e. at least four isolated triangles. Lemma 2.4 excludes four. Contradiction.

Thus

\[
\boxed{m\ne10.}
\]

## 4. Exclude m=9

If m=9, the two nonexact colors have positive excesses 1 and 2. Call them D_1 and D_2, with 130 and 131 edges respectively.

At an exact exceptional vertex x,

\[
d_{D_1}(x)+d_{D_2}(x)
\le60-13-9-8\cdot4=6.
\]

Lemma 2.1 gives d_{D_2}(x)>=3, while the s=1 pointwise theorem gives d_{D_1}(x)>=3. Hence both are exactly three at every exact exceptional vertex.

The nine exact exceptional vertices are distinct, so D_1 has at least nine degree-three vertices. Lemma 2.3 says a 130-edge non-target color has at most eight. Contradiction.

Thus

\[
\boxed{m\ne9.}
\]

## 5. Conclusion: exactly eight exact colors

The Q32 outer equality system already gives m in {8,9,10}. Sections 3 and 4 eliminate 9 and 10. Therefore

\[
\boxed{m=8.}
\]

The remaining three non-target colors all have s=1 and exactly 130 residual edges.

This conclusion is independent of the Q33 284-edge core. It applies to the Q32 residual before the full-support v=47 reduction and therefore may be combined with `Q32_NONFULL_SUPPORT_SHELL_CAPACITY.md`. In particular the sole surviving Q32 support terminal is now:

\[
\boxed{|U|=47,\quad m=8,\quad(s_1,s_2,s_3)=(1,1,1).}
\]

## 6. Immediate m=8 low-degree consequence

Let X be the eight distinct exact exceptional vertices. At x in X, the exact colors contribute at least

\[
9+7\cdot4=37
\]
non-target degree and the target color contributes at least 13. Hence the three 130-edge nonexact colors have degree sum at most ten at x. Each has minimum degree three, so at least two of the three have degree exactly three at every x.

By Lemma 2.2 those degree-three incidences come from isolated K4 components of the three nonexact colors, and by Lemma 2.3 each nonexact color has at most two such K4 components. This is the next finite structural kernel; no contradiction is claimed here.