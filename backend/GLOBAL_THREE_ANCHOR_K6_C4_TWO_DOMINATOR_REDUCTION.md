# Three-Anchor K=6 / c=4 Two-Dominator Reduction

Status: **PROVED_ANALYTIC**.

This theorem treats the `(10,10,8)` four-connector equality regime under the hypothesis that exactly two connectors dominate the K8 block.  The retained dominator-capacity theorem already proves that those two dominators are target-adjacent and form a saturated K11 with the K8 block and its anchor.

The conclusion is that the two remaining bad connectors cannot have different anchor signatures.  Hence every such K=6 survivor is forced into one same-signature double-defect system.

Dependencies:

- `GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md`;
- the three-anchor partition theorem;
- `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`;
- the common-nonneighbour clique/missed-set-clique mechanism.

---

## 1. Setup

Let the exclusive clique blocks have sizes

`|X1|=|X2|=10`, `|X3|=8`,

with anchors `a1,a2,a3`.

All four connectors are pair-connectors and all meet `a3`; two have signature `{a1,a3}` and two have signature `{a2,a3}`.

Assume exactly two connectors `d1,d2` dominate `X3`.
The retained K=6 dominator-capacity theorem gives

- `d1d2` is a target edge;
- `X3 union {a3,d1,d2}` is a saturated K11.

Let `b` be a bad connector of signature `{a1,a3}`, so it misses anchor `a2` and does not dominate `X3`.
Put

`P=X1\N(b)`, `Q=X3\N(b)`,

`p=|P|>=1`, `q=|Q|>=1`,

and `k=kappa_b`.

The inequality `p>=1` is forced because `p=0` would make `X1 union {a1,b}` a K12.

Let `epsilon` be the number of connector neighbours of `b` among the other three connectors.
If `n2=|N(b) intersect X2|`, the degree equation is

`n2=k+p+q-8-epsilon`,

so

> `p+q>=8+epsilon-k`.                                       (1)

Because `b` and `a2` are nonadjacent, `P union Q` is a target clique.

---

## 2. Strengthened bad-connector cost in the two-dominator state

Every point `x in Q` has

- eight fixed neighbours in `X3 union {a3}`;
- the two dominators `d1,d2` as target neighbours;
- every point of `P` as a target neighbour.

Therefore

`kappa_x >= (p-2)_+`.

Every point `y in P` has the ten fixed neighbours in `X1 union {a1}` and all `q` neighbours in `Q`, so

`kappa_y >= (q-2)_+`.

Hence the bad subsystem has local cost

> `L(b)=k+q(p-2)_+ + p(q-2)_+`.                              (2)

### Lemma

`L(b)>=4`.

#### Proof

If `min(p,q)=1`, say `q=1`, then either `p=1`, in which case (1) gives `k>=6+epsilon`, or `p>=2`, in which case

`L=k+p-2 >= 5+epsilon`.

The case `p=1` is symmetric.  Thus the one-small-side regime has cost at least5 (and in the `(1,1)` corner at least6).

Now assume `p,q>=2` and put `s=p+q>=4`.
For fixed `s`, `pq>=2(s-2)`.  Hence

`L = k+2pq-2p-2q >= k+2s-8`.

By (1), `k>=8+epsilon-s`, so

`L>=s+epsilon>=4`.

This proves the lemma.

---

## 3. Different-signature bad costs are additive

Now suppose the two bad connectors have different signatures.

Write the second bad connector as `c`, of signature `{a2,a3}`, with missed sets

`R subset X2`, `S subset X3`,

and corresponding parameters `r=|R|`, `s=|S|`, `kappa_c`.

Its local cost is

`L(c)=kappa_c+s(r-2)_+ + r(s-2)_+ >=4`.

The private-block charge contributions on `P subset X1` and `R subset X2` are disjoint.
The only possible overlap of the two local cost ledgers occurs on `Q intersect S subset X3`.

Take `x in Q intersect S`.
Because `P union Q` and `R union S` are target cliques, `x` is adjacent to every point of `P union R`.
It already has the ten-neighbour K11 base

`X3 union {a3,d1,d2}`.

Therefore

`kappa_x >= p+r-2`.

For positive integers `p,r`,

`p+r-2 >= (p-2)_+ + (r-2)_+`.

Hence the actual excess at every shared X3 witness is at least the sum of the two amounts charged to it by the separate local ledgers.

Thus the two bad-connector costs are fully additive:

> `K >= L(b)+L(c) >= 4+4=8`.

This contradicts `K=6`.

---

# 4. Conclusion

In the `(10,10,8)`, `K=6`, exactly-two-dominator regime, the two bad connectors cannot have different anchor signatures.

Therefore every surviving two-dominator state has the unique macro architecture

> **same-signature double defect:** the two dominators have one common pair-signature and the two bad connectors have the opposite common pair-signature.

No other two-dominator connector assignment survives.

This reduces the remaining equality question to a single shared-defect problem rather than a connector case tree.

---

## Reusable principle

When a saturated dense base raises the guaranteed degree of a shared missed-set block, bad-connector excess charges belonging to different anchor signatures become additive even when their missed sets overlap.  This `dense-base -> additive defect cost` mechanism is independent of the E-layer label and should be reusable in later equality windows.