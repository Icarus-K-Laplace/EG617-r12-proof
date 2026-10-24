# Multicolor Moment and Triangle Identities

Status: **PROVED**.

Set `n=r^2+1`. For each vertex v and color i let

`x_i(v)=d_i(v)-r`.

Because the color neighborhoods partition `V\{v}`,

`sum_i d_i(v)=r^2`, hence `sum_i x_i(v)=0`.

## 1. Second moment / degree variance

Define

`V=sum_(v,i) x_i(v)^2`.

Then exactly

`sum_(v,i) d_i(v)^2 = n r^3+V`.

Thus the simultaneous degree second moment is minimized exactly by the pointwise regular profile `d_i(v)=r` for all `(v,i)`.

If

`mu=C(n,2)/r=r(r^2+1)/2`

and `Delta_i=e_i-mu`, then `sum_i Delta_i=0` and Cauchy gives

`V >= (4/n) sum_i Delta_i^2`.

Equivalently, color-edge imbalance forces color-degree variance.

## 2. Turan slack coordinates

Let

`p_r(n)=r(r^2-r+2)/2`

and define

`s_i=e_i-p_r(n)>=0`.

Since the color graphs partition all edges,

`sum_i s_i=r^2(r-1)/2`.

Moreover

`mu-p_r(n)=C(r,2)`,

so

`Delta_i=s_i-C(r,2)`.

Therefore

`V >= (4/n) sum_i (s_i-C(r,2))^2`.

This connects the global Turan-stability slack vector directly to the degree-variance variable in the non-rainbow theorem.

## 3. Same-color wedge identity

Let

`W=sum_(v,i) C(d_i(v),2)`.

Using the fixed pointwise degree sum,

`W=n r^2(r-1)/2 + V/2`.

If `T_2` denotes triangles using exactly two colors and `T_3` monochromatic triangles, then trianglewise counting gives the exact identity

`W=T_2+3T_3`.

Hence every deviation from simultaneous r-regularity creates additional same-color wedges and therefore additional non-rainbow triangle pressure.

## 4. Avoidance defect identity

For

`W_i(v)=V\({v} union N_i(v))`,

put

`Q(v)=C(r^2,2)-sum_i e_i(W_i(v))`.

Then

`sum_v Q(v)=2T_2+3T_3`.

Combining with the same-color wedge identity gives

`sum_v Q(v)-W=T_2>=0`.

This exact relation is the bridge between local `(r+1)`-set avoidance and the global degree second moment.

## 5. Convexity penalty

Define

`P(v)=sum_i p_(r-1)(r^2-d_i(v))-r^2(r-1)^2/2`,

and `P=sum_v P(v)`.

Discrete convexity gives `P(v)>=0`. The quadratic relaxation

`p_(r-1)(m)>=m^2/[2(r-1)]-m/2`

gives

`P>=V/[2(r-1)]`.

The global non-rainbow theorem therefore implies

`V+2P<=n r^2(r-1)`

and in particular

`V<=n r(r-1)^2`.

## 6. Edgewise rainbow-extension statistic

For an edge `xy`, let

`b(xy)=#{z notin{x,y}: triangle xyz is not rainbow}`.

Every non-rainbow triangle contributes to b on all three of its edges, so

`sum_(xy) b(xy)=3(T_2+T_3)`.

The global non-rainbow budget yields

`average_edge b(xy) <= 3(r-1)-3P/(n r^2)`.

Therefore the average edge has at least

`(r-1)(r-2)+3P/(n r^2)`

rainbow third-vertex extensions.

Since an edge has `n-2=r^2-1` possible third vertices, only `O(r)` of its `Theta(r^2)` extensions can fail to be rainbow on average.

## 7. Exact codegree form for an edge

Suppose `xy` has color i, and write

`c_j(x,y)=|N_j(x) intersect N_j(y)|`.

Then exactly

`b(xy)=d_i(x)+d_i(y)-2-c_i(x,y)+sum_(j!=i)c_j(x,y)`.

Indeed a third vertex is bad precisely when at least one incident edge from `{x,y}` repeats the edge color i, or when the two incident colors agree with each other in some `j!=i`.

Thus the average `O(r)` bad-extension theorem is an average multicolor codegree compatibility theorem: for most edges, two endpoint color-signature rows agree or collide in only a tiny fraction of the `r^2-1` remaining coordinates.
