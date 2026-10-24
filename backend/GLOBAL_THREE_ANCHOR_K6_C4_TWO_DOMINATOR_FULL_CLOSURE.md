# Three-Anchor K=6 / c=4 Exactly-Two-Dominator Full Closure

Status: **PROVED_ANALYTIC**.

This theorem completes `GLOBAL_THREE_ANCHOR_K6_C4_TWO_DOMINATOR_REDUCTION.md` and eliminates the entire exactly-two-dominator regime in the `(10,10,8)` four-connector partition.

Dependencies:

- `GLOBAL_THREE_ANCHOR_K6_C4_DOMINATOR_CAPACITY.md`;
- `GLOBAL_THREE_ANCHOR_K6_C4_TWO_DOMINATOR_REDUCTION.md`;
- hereditary 13-point cap `D(13)=67`;
- `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`.

No computation and no E-layer label are used.

---

## 1. Reduction to same-signature bad connectors

Assume the three-anchor contract, `K=6`, block sizes `(10,10,8)`, and exactly two K8-dominators.

The dominator-capacity theorem gives that the two dominators are target-adjacent and

`B3 = X3 union {a3,d1,d2}`

is a saturated K11.

The preceding two-dominator reduction proves that the two bad connectors cannot have different anchor signatures: their strengthened local defect costs are additive and would force `K>=8`.

Hence, after relabelling, the two dominators have signature `{a2,a3}` and the two bad connectors `b1,b2` both have signature `{a1,a3}`.

Let

`Pi = X1\N(bi)`, `Qi = X3\N(bi)`,

`pi=|Pi|>=1`, `qi=|Qi|>=1`,

`ki=kappa_bi`.

Let `e=1` if `b1b2` is a target edge and `0` otherwise.
Let `ri` be the number of dominators among `{d1,d2}` adjacent to `bi`.
Then the total connector adjacency entering the degree equation of `bi` is

`epsilon_i = ri+e`.

---

## 2. Two saturated K11 caps force large missed mass in both directions

### Private K10 side

`B1=X1 union {a1}` is always a K11.

The induced 13-set `B1 union {b1,b2}` has

`55 +(11-p1)+(11-p2)+e`

edges.  By `D(13)=67`,

> `p1+p2 >= 10+e`.                                          (P)

### Dominated K8 side

`B3=X3 union {a3,d1,d2}` is a K11.

Connector `bi` has exactly

`1 +(8-qi)+ri = 9-qi+ri`

edges into this K11.  Hence the induced 13-set `B3 union {b1,b2}` has

`55 +(9-q1+r1)+(9-q2+r2)+e`

edges.  Again using `D(13)=67`,

> `q1+q2 >= 6+r1+r2+e >=6`.                                (Q)

Thus the two bad connectors must jointly carry at least ten private missed vertices and at least six missed vertices in the dominated K8.

---

## 3. Single-bad capacity inside the saturated K11 background

For one bad connector `bi`, let `ni` be its number of neighbours in the opposite size-ten block `X2`.
The degree equation gives

`ni = ki+pi+qi-8-epsilon_i`,

so

> `pi+qi >= 8+epsilon_i-ki`.                                (D)

Because `bi` and the missed anchor `a2` are nonadjacent, `Pi union Qi` is a target clique.
Every point of `Qi` already has the ten-neighbour saturated-K11 base `X3 union {a3,d1,d2}` and is adjacent to every point of `Pi`; every point of `Pi` has the ten-neighbour base `X1 union {a1}` and is adjacent to every point of `Qi`.
Therefore the bad subsystem has local excess lower bound

> `Li = ki + qi(pi-2)_+ + pi(qi-2)_+`.                       (L)

Since the global excess is only six,

> `Li<=6` for each i.                                        (C)

We now extract two elementary consequences of (D)--(C).

### Consequence 1: if `pi,qi>=2`, then `pi+qi<=6`

If `pi,qi>=2`, then

`Li=ki+2pi qi-2pi-2qi`.

If `pi+qi>=7`, the smallest possible block term occurs at `{pi,qi}={2,pi+qi-2}`.
For sum seven it is six, while (D) still forces `ki>=1`; for larger sums the block term itself exceeds six.
Hence `Li>6`, contradiction.

Thus

> `pi,qi>=2 => pi+qi<=6`.                                   (S1)

### Consequence 2: if one side equals one, the other is at most eight

Suppose `qi=1`.  Then

`Li=ki+(pi-2)_+`.

For `pi>=9` the block term alone is at least seven, so `Li>6`.
Hence `pi<=8`.
The symmetric statement holds when `pi=1`.

Thus

> `min(pi,qi)=1 => max(pi,qi)<=8`.                           (S2)

---

## 4. Global missed-mass inequalities force a crossed one-small-side pattern

From (P),

`p1+p2>=10`.

From (Q),

`q1+q2>=6`.

If both bad connectors satisfied `pi,qi>=2`, then by (S1)

`(p1+q1)+(p2+q2)<=12`,

whereas (P)+(Q) gives

`(p1+p2)+(q1+q2)>=16`,

impossible.

Therefore at least one connector has a side of size one.

They cannot both have `qi=1`, because then `q1+q2=2<6`.
They cannot both have `pi=1`, because then `p1+p2=2<10`.

Suppose, without loss of generality, `q1=1`.
Then `q2>=5` by (Q).
If `p2>=2`, then `p2,q2>=2`, and (S1) gives

`p2+q2<=6`,

hence `p2<=1`, contradiction.
Therefore

`p2=1`.

Thus every possible survivor must have the crossed form

> `(p1,q1)=(p,1)`, `(p2,q2)=(1,q)`.                         (X)

But (P) now gives

`p+1>=10+e`,

so

`p>=9+e>=9`.

This contradicts (S2), which says that a bad connector with `q1=1` must satisfy `p<=8`.

Contradiction.

---

# 5. Conclusion

There is no `(10,10,8)` three-anchor K=6 core with exactly two K8-dominating connectors.

Combined with the dominator-capacity theorem:

- four dominators are impossible;
- three dominators are impossible;
- exactly two dominators are now impossible.

Hence any surviving `(10,10,8)`, `K=6` equality state would have at most one K8-dominator.

The remaining task in this partition is therefore a pure high-defect regime with at least three bad connectors; no mixed two-dominator equality window remains.

---

## Reusable mechanism

The proof isolates a general dense-base principle:

> two saturated K11 caps can force large missed mass in two orthogonal block directions, while the local bad-connector excess inequality bounds how much missed mass a single connector can carry.  Their incompatibility eliminates an entire equality regime without connector-graph enumeration.