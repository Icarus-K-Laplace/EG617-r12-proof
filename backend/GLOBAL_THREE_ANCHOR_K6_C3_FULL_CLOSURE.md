# Three-Anchor K=6 / Three-Connector Full Closure

Status: **PROVED_ANALYTIC**.

This theorem eliminates the last `c=3` equality geometry from
`GLOBAL_THREE_ANCHOR_K6_C3_NORMAL_FORM.md` by an exact bad-connector excess ledger plus the common-nonneighbour clique lemma.

Dependencies:

- `GLOBAL_THREE_ANCHOR_K6_C3_NORMAL_FORM.md`;
- `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`;
- the common-nonneighbour clique lemma.

No solver and no E-layer label are used.

---

## 1. Equality normal form

Assume the three-anchor contract and total core excess

`K=sum_v(d_H(v)-12)=6`.

In the `c=3` partition the clique blocks have sizes `(10,10,9)`.
There is one three-anchor connector `t` and two pair-connectors `u,v`.
By the retained K=6 normal-form theorem exactly one pair-connector is bad and the other dominates the K9 block.

Relabel so that

- `u` is bad, with anchor signature `{a1,a3}` and missed anchor `a2`;
- `v` is good, with signature `{a2,a3}` and adjacent to every vertex of `X3`;
- `t` meets all three anchors.

Let

`P=X1\N(u)`, `Q=X3\N(u)`,

`p=|P|`, `q=|Q|>=1`,

`k=kappa_u`,

and let

`epsilon=e_H(u,{t,v}) in {0,1,2}`.

Since `u` and `a2` are target-nonadjacent, `P union Q` is a target clique.
Also `p>=1`: if `p=0`, then `u` dominates the K10 block `X1`, and `X1 union {a1,u}` is a forbidden K12.

Write `n2=|N(u) intersect X2|`.  The degree equation for `u` gives

`n2=k+p+q-9-epsilon`,

hence

> `p+q >= 9+epsilon-k`.                                      (1)

---

## 2. Exact local excess lower bound

Every `x in Q` has the nine fixed neighbours in `X3 union {a3}`, is adjacent to the good connector `v`, and is adjacent to every point of `P`.  Therefore

`kappa_x >= (p-2)_+`.

Every `y in P` has the ten fixed neighbours in `X1 union {a1}` and is adjacent to every point of `Q`.  Therefore

`kappa_y >= (q-2)_+`.

The sets `{u}`, `P`, and `Q` are disjoint, so the bad subsystem alone consumes at least

> `L = k + q(p-2)_+ + p(q-2)_+`.                             (2)

Since the global budget is six,

> `L<=6`.                                                     (3)

This lower bound is sharper than the retained coarse `>=5` bad-connector cost and is exact enough to classify the K=6 equality window.

---

## 3. Arithmetic classification of `L<=6`

We use only (1)--(3), `p,q>=1`, and integrality.

### 3.1 One of `p,q` equals one

Suppose first `min(p,q)=1`.

If `q=1`, then `p>=2` (the case `p=1` would require `k>=7+epsilon`) and

`L=k+p-2`.

Together with (1),

`L >= 6+epsilon`.

Thus `L<=6` forces

`epsilon=0`, `L=6`.

The same argument with `p=1` gives the identical conclusion.

### 3.2 Both `p,q` are at least two

For `p,q>=2`,

`L=k+2pq-2p-2q`.

For fixed `s=p+q`, the product `pq` is minimized at an endpoint, so with `p,q>=2`,

`L >= k+2(s-4)`.

From (1), `k>=9+epsilon-s`, hence

`L >= s+1+epsilon`.

Therefore `L<=6` implies `s<=5-epsilon`.

Consequently the only possibilities are:

- `epsilon=0`, `p+q=4 or 5`;
- `epsilon=1`, necessarily `p=q=2`, `k=6`;
- `epsilon>=2`: impossible.

More explicitly, the unique `L=5` cell is

> `(k,p,q,epsilon)=(5,2,2,0)`,                               (4)

while all other surviving cells have `L=6`.

In every `L=6, epsilon=0` cell the degree equation gives `n2<=1`.
In the unique `L=5` cell, `n2=0`.
In the unique `epsilon=1` cell `(6,2,2,1)`, again `n2=0`.

---

## 4. Eliminate every `L=6, epsilon=0` cell

Here the bad subsystem already consumes all six excess units.  Therefore

- `kappa_v=0`;
- `kappa_t=0`;
- every excess inequality used in (2) is tight;
- no edge outside the guaranteed base/clique edges may increase the excess of a vertex in `P union Q`.

Also `uv` and `ut` are both nonedges.

Because `v` dominates `X3` and has zero excess, it has eleven fixed neighbours (`X3` plus anchors `a2,a3`) and hence at most one further neighbour in `X1 union X2 union {t,u}`.

Let

`B = X2 \ (N(u) union N(v))`.

Since `n2<=1` and `v` has at most one neighbour in `X2`,

`|B|>=8`.                                                     (5)

Take any `y in P`.

If `vy` is a nonedge, then `y` and every point of `B` are common nonneighbours of the nonadjacent pair `u,v`.  The common-nonneighbour clique lemma forces `y` adjacent to every point of `B`.  That gives at least one target edge beyond the exact lower-bound degree used in (2), contradicting that the full excess budget is already saturated.

Hence `vy` must be an edge.

But this edge itself is again an extra target edge beyond the degree lower bound used in (2), so it increases `kappa_y` by at least one and again exceeds the saturated total excess six.

Contradiction.

Thus no `L=6,epsilon=0` cell exists.

---

## 5. Eliminate the unique `L=5` cell

Now (4) holds:

`k=5`, `p=q=2`, `epsilon=0`, `n2=0`.

Exactly one excess unit remains outside the bad subsystem.

Again `uv` is a nonedge.  The good connector `v` has eleven fixed neighbours, so with `kappa_v<=1` it has at most two further neighbours total.  Put

`B=X2 \ N(v)`.

Since `u` is anticomplete to `X2`,

`|B|>=8`.

For any `y in P`, if `vy` were a nonedge then the common-nonneighbour clique of `u,v` would force `y` adjacent to all of `B`, requiring at least eight excess units at `y`, impossible with only one global unit left.

Therefore `v` is adjacent to both vertices of `P`.

This already forces `kappa_v>=1`, and each of the two vertices of `P` receives one additional target edge beyond the lower bound in (2), so the total excess is at least

`5+1+1+1=8`,

contradicting `K=6`.

Thus the `L=5` cell is impossible.

---

## 6. Eliminate the unique `epsilon=1` cell

The only remaining arithmetic possibility is

`(k,p,q,epsilon)=(6,2,2,1)`.

The bad subsystem already consumes the entire excess budget, so all other vertices have zero excess and every lower bound in (2) is tight.

If `uv` is a nonedge, the argument of Section 4 applies verbatim and gives a contradiction.

Hence `uv` must be the unique edge counted by `epsilon`, so `ut` is a nonedge.

Since `n2=0`, `u` is anticomplete to `X2`.
The connector `t` has zero excess and already has the three anchor neighbours, so it has at most nine block neighbours (and fewer if it is adjacent to `v`).  Therefore there exists at least one vertex

`b in X2`

which is nonadjacent to both `u` and `t`.

Take any `y in P`.

- If `ty` is a nonedge, then `b,y` are common nonneighbours of the nonadjacent pair `u,t`; the common-nonneighbour clique lemma forces `by` to be an edge, adding an excess unit beyond the saturated lower bound.
- If `ty` is an edge, that edge itself adds an excess unit beyond the same saturated lower bound.

Either way the total excess exceeds six.

Contradiction.

Thus the `epsilon=1` cell is impossible.

---

# 7. Conclusion

Every arithmetic cell compatible with a K=6 bad pair-connector is impossible.

Therefore

> **there is no three-anchor K=6 core with connector count `c=3`.**

Combined with `GLOBAL_THREE_ANCHOR_K6_C2_FULL_CLOSURE.md`, the first surviving three-anchor equality layer, if it exists at all, is confined to the `c=4` connector regime.

---

## Reusable mechanism

The proof isolates a reusable equality principle:

> once a bad connector and its missed-set clique saturate all but at most one unit of the global excess budget, any large common-nonneighbour clique forces an additional target edge and therefore breaks equality.

This is a global compatibility obstruction, not an E-layer case split.