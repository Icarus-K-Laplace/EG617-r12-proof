# Three-Anchor K=6 / Three-Connector Normal Form

Status: **PROVED_ANALYTIC**.

This file advances the K=6 equality frontier in the `c=3` three-anchor partition.  It proves that the two pair-connectors cannot both fail, and cannot both succeed, at dominating the common size-nine block.  Hence exactly one of them is a size-nine dominator and the other is the unique high-cost exceptional connector.

Dependencies:

- `GLOBAL_THREE_ANCHOR_PARTITION_THEOREM.md`;
- the pair-connector cost estimate proved in `GLOBAL_THREE_ANCHOR_K4_EQUALITY_CLOSURE.md`;
- the common-nonneighbour clique lemma;
- `alpha(H)<=3`, `omega(H)<=11`, `delta(H)>=12`.

No E-layer labels or computation are used.

---

## 1. Setup

Let H satisfy the three-anchor residual-core contract and have total excess

`K=sum_v(d_H(v)-12)=6`.

Assume the connector count is `c=3`.

Then, after relabelling anchors, the partition theorem gives clique blocks

`|X1|=10, |X2|=10, |X3|=9`,

one three-anchor connector t, and two pair-connectors u,v with signatures

`u ~ {a1,a3}`,

`v ~ {a2,a3}`,

`t ~ {a1,a2,a3}`.

Thus both u and v meet anchor a3 and the size-nine block X3 is the common small block in their pair-connector analysis.

Call a pair-connector **good** if it dominates X3 and **bad** otherwise.

---

## 2. Retained one-connector cost bound

The proof of `GLOBAL_THREE_ANCHOR_K4_EQUALITY_CLOSURE.md` establishes the following local fact.

Take u, which misses anchor a2.  Let

- `P_u` be its missed set in the private size-ten block X1;
- `Q_u` be its missed set in the common size-nine block X3.

Because `u` and `a2` are nonadjacent, `P_u union Q_u` is a target clique.

If `Q_u` is nonempty, the degree/excess calculation implies that

> connector excess of u + forced excess on `P_u union Q_u` is at least 5.   (C1)

The same statement holds for v using its private block X2 and common block X3.

This was enough to exclude one bad connector under K=4.  At K=6 we additionally need to prove that two such lower bounds cannot hide in the same X3 excess.

---

## 3. Additivity of the two bad-connector costs

Assume for contradiction that both pair-connectors are bad.

Write

`P=P_u subset X1`, `Q=Q_u subset X3`,

`R=P_v subset X2`, `S=Q_v subset X3`.

The private-block contributions on P and R are disjoint, so only the excess on `Q intersect S` could conceivably be counted by both one-connector estimates.

Take `x in Q intersect S`.

From the common-nonneighbour clique for `(u,a2)`, x is adjacent to every point of P.

From the common-nonneighbour clique for `(v,a1)`, x is adjacent to every point of R.

The vertex x already has nine target neighbours in `X3 union {a3}`: eight inside the K9 block and its anchor a3.  Hence

`d_H(x) >= 9+|P|+|R|`,

so

> `kappa_x >= |P|+|R|-3`.                                  (C2)

The separate one-connector bounds on the same vertex are

`kappa_x >= max(0,|P|-3)`

and

`kappa_x >= max(0,|R|-3)`.

But for nonnegative integers a,b,

`max(0,a+b-3) >= max(0,a-3)+max(0,b-3)`.                   (C3)

Therefore the actual excess required at every shared X3 witness is at least the **sum** of the excess amounts charged to it by the two local bad-connector arguments.

Consequently the two lower bounds (C1) are additive even when Q and S overlap.

Thus two bad pair-connectors force total excess at least

`5+5=10`,

contradicting `K=6`.

Hence

> **at most one pair-connector is bad.**                    (C4)

---

## 4. Both pair-connectors cannot be good

Suppose now that both u and v dominate X3.

They both meet anchor a3.

If uv is a target edge, then

`X3 union {a3,u,v}`

is a K12, contradicting `omega(H)<=11`.

If uv is a target nonedge, then each connector already has eleven fixed neighbours: the nine vertices of X3 and its two anchor neighbours.

Thus u has at most `1+kappa_u` further neighbours and v has at most `1+kappa_v` further neighbours among the two size-ten blocks.

Since

`kappa_u+kappa_v<=K=6`,

they have at least

`20-(1+kappa_u)-(1+kappa_v) >=12`

common nonneighbours in `X1 union X2`.

Because u,v are nonadjacent, their common nonneighbours form a clique, contradicting `omega(H)<=11`.

Therefore

> **the two pair-connectors cannot both be good.**          (C5)

---

## 5. Exact macro normal form

Combining (C4) and (C5):

> **exactly one pair-connector is bad and exactly one pair-connector dominates X3.**   (C6)

Let u be the bad connector and v the good one.

By (C1), the subsystem consisting of u and the block vertices whose excess is forced by its missed-set clique consumes at least five of the six available excess units.

Hence every contribution outside that bad subsystem has total excess at most one.

In particular,

> `kappa_v<=1`,                                             (C7)
>
> `kappa_t<=1`.                                             (C8)

Moreover the sum of

- excess of the good pair-connector;
- excess of the three-anchor connector;
- all block excess not already required by the bad connector

is at most one.                                             (C9)

This is the K=6 three-connector normal form.

---

## 6. Interpretation

The c=3 K=6 equality frontier is therefore not a large family of connector patterns.  It has one canonical architecture:

1. one pair-connector is a full K9 dominator and is almost regular (`kappa<=1`);
2. the other pair-connector is the unique high-cost defect and consumes at least five excess units together with its forced missed-set witnesses;
3. the three-anchor connector is also almost regular (`kappa<=1`);
4. at most one excess unit in total remains outside the exceptional bad-connector subsystem.

This is precisely the kind of `one defect + rigid background` geometry expected from the Global Support-Compatibility programme.

---

## 7. Next step

The remaining c=3 problem is now an equality-rigidity question, not a case tree:

> classify the exact five- or six-unit bad-connector subsystem and test whether its almost-regular K9-dominator and three-anchor connector can coexist with it.

Together with `GLOBAL_THREE_ANCHOR_K6_C2_NORMAL_FORM.md`, this reduces two of the three K=6 connector regimes to finite global normal forms.