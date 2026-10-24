# General-r Direct Near-Anchor Forcing

Status: **PROVED_SYMBOLIC conditional only on the general residual-core contract and inherited hereditary cap**.

This theorem is extracted from the r=12 direct Bridge A argument and parameterized exactly.

## Contract

Let `r>=2`. Let H be a graph on

`n=3r-1`

vertices satisfying

- `delta(H)>=r`;
- `omega(H)<=r-1`;
- inherited target hereditary cap

`e(H)<=D_r(3r-1)`, where

`D_r(n)=C(n,2)-(r-1)p_r(n)`

and `p_r(n)` is the minimum number of edges in an n-vertex graph with independence number at most r.

No common-S family is assumed. No shell/support extraction is used.

Define

`K_r(H)=sum_v(d_H(v)-r)=2e(H)-r(3r-1)`.

## 1. Exact cap arithmetic

For `3r-1=2r+(r-1)`, the balanced r-clique partition has one part of size2 and `r-1` parts of size3. Hence

`p_r(3r-1)=1+3(r-1)=3r-2`.

Therefore

`D_r(3r-1)=C(3r-1,2)-(r-1)(3r-2)`

and exact simplification gives

> `D_r(3r-1)=(3r^2+r-2)/2`.

Consequently

> **`K_r(H)<=2r-2`.**

For r=12 this is exactly `K<=22` and `e(H)<=221`.

## 2. Parameterized low-excess triple lemma

Use the following general graph lemma.

Let a graph on n vertices have minimum degree at least delta and clique number at most omega. Put

`t=n-1-delta-omega`.

Suppose

- `1<=t<=delta+2`;
- `2t<n`;
- `sum_v(d(v)-delta)<=2t`.

Then the graph contains an independent triple with degree pattern

`(delta, <=delta+1, <=delta+1)`.

Proof. Since total excess is smaller than n, there exists a degree-delta vertex a. Its open antineighbourhood has `n-1-delta` vertices. If there is no desired triple, then the vertices of excess at most1 in that antineighbourhood form a clique, hence at most omega in number. Therefore at least t vertices there have excess at least2. Since total excess is at most2t, equality holds everywhere: there are exactly t such high vertices, each of excess exactly2, all other vertices have zero excess. Repeating at every degree-delta vertex forces all t high vertices to be anticomplete to the degree-delta set. Their degrees are therefore at most t-1, but `t-1<=delta+1`, contradicting that each has degree delta+2. QED.

## 3. Residual-core specialization

Take

`n=3r-1`, `delta=r`, `omega=r-1`.

Then

`t=(3r-1)-1-r-(r-1)=r-1`.

The lemma hypotheses are automatic:

- `t=r-1>=1`;
- `t<=r+2`;
- `2t=2r-2<3r-1=n`;
- the hereditary cap gave `K_r<=2r-2=2t`.

Therefore:

> **General Direct Near-Anchor Forcing Theorem.**
>
> Every genuine residual core H satisfying the general residual-core contract and inherited hereditary cap contains an independent triple
>
> `a,b,c`
>
> with
>
> `d_H(a)=r`, `d_H(b)<=r+1`, `d_H(c)<=r+1`.
>
> Equivalently the anchor excess pattern is one of
>
> `(0,0,0)`, `(0,0,1)`, `(0,1,1)`.

Thus the total anchor excess is at most2.

## 4. Structural consequence

The common-S/signature machinery is not needed to *produce* the near-anchor alternative once a genuine core is available. It remains useful only for equality incompatibility, support concentration, and positive-loss branches.

Hence the general backend architecture should be reorganized as:

`residual-core extraction`
` -> direct near-anchor forcing`
` -> general near-anchor excess theorem`
` -> strengthened q ceiling`
` -> d<=3 / high-endpoint collapse`
` -> support equality incompatibility`.

## 5. Conditional strengthened envelope

If the general exact/near-anchor theorem is proved in the form

`independent triple of total excess <=3 => K_r(H)>=8`,

then the direct theorem applies to every genuine core and yields

`K_r(H)>=8`, hence

`e(H)>=[r(3r-1)+8]/2`.

At the maximum 4r+1 residual layer this strengthens the q ceiling from

`q<=3r+2`

to

> **`q<=3r-1`.**

Then for every r>=12, the repivot base eliminates every regular missing degree

`4<=d<=r-3`,

because

`d(r+1-d)>=4(r-3)>3r-1`.

Thus the scalable backend complexity reduces to d<=3 for the entire range r>=12, with the high endpoint d>=r-2 carrying at most three common-S owners.

## Boundary

This theorem does **not** prove the general residual-core extraction itself, and it does **not** prove the general exact three-anchor excess theorem. Those remain the two load-bearing upstream gaps.
