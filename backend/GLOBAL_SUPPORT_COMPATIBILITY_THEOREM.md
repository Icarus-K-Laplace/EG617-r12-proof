# Global Support-Compatibility Theorem

Status: `PROVED_ANALYTIC` under the exact pivot/repivot identities, row closure, all-pivot core minimum-degree contract, and lexicographic maximality of `(q,tau)`.

Purpose: this theorem reorganizes the high-backend argument around common support structure rather than the individual edge layers `E333,...,E340`. It is parameterized and is not specific to one surviving shell family.

## 1. Abstract common-S setup

Let `p` be a lexicographically maximal pivot. Let its shell have size `h` and core `H` have size `n`. In the current r=12 backend,

- `h=13`,
- `n=35`,
- the core minimum-degree baseline is `h-1=12`.

Fix a family `Y` of `N` regular shell vertices having the same missing set

`S`, `|S|=d`.

For `y in Y`, let

`D_y=N_H(y)`, `|D_y|=d`.

Write

`kappa_v=d_H(v)-(h-1)`,

`w_v=kappa_v+e_F(v,S)`,

`mu(D)=binom(d,2)-e_H(D)`.

Let

`B=e_M(A\S)+G_(A\S)`

and define the common row allowance

`a=q-d(h-d)-B`.

The exact exchange formula is

`q_y=d(h-d)+B+w(D_y)+mu(D_y)`,

where

`w(D_y)=sum_(v in D_y) w_v`.

For each core vertex define its support-incidence multiplicity

`lambda_v=#{y in Y : v in D_y}`.

Let `X` be the globally decorated vertices and put

`s=|S intersect X|`.

## 2. Exact global repivot-loss identity

Summing the exact exchange formula over the whole common-S family gives

> **Support-gain identity**
>
> `sum_(y in Y) (q-q_y)`
> ` = N a - sum_(v in H) lambda_v w_v - sum_(y in Y) mu(D_y)`.      (G1)

This is an identity, not an inequality.

Because `p` has maximum q, every summand on the left is nonnegative. Hence

> **global compatibility inequality**
>
> `sum_v lambda_v w_v + sum_y mu(D_y) <= N a`.                    (G2)

Consequently, for every integer `t>=1`,

> `sum_(w_v>=t) lambda_v <= (N a-sum_y mu(D_y))/t`.                (G3)

In particular, since total support incidence is `Nd`, the number of zero-charge incidences satisfies

> `sum_(w_v=0) lambda_v >= N(d-a)+sum_y mu(D_y)`.                  (G4)

Thus a large common-S family at small allowance is forced to place a large fraction of its support incidences on zero- or low-charge core vertices. This is the common mechanism behind the V5/V6 repeated-pair capacity results.

## 3. Decoration created by support repetition

For every core vertex with `lambda_v>=1`, its global degree satisfies

`g_v=d_F(v)-h >= kappa_v+lambda_v-1`.                            (G5)

Hence

> `sum_(v in union D_y) g_v >= kappa(union D_y)+Nd-|union D_y|`.  (G6)

In particular every vertex used by at least two support rows is globally decorated.

This is the direct bridge from support repetition to secondary-pivot decoration.

## 4. Plateau packing theorem

The exact decoration transport under repivot is

`tau_y-tau_p=|D_y intersect X|-|S intersect X|`.

If `q_y=q`, lexicographic maximality of `(q,tau)` gives

`|D_y intersect X|<=s`.                                        (G7)

Every vertex with support multiplicity at least two is decorated by (G5). Therefore a plateau support contains at least

`d-s`

globally nondecorated vertices, and every such vertex occurs in exactly one support row.

Thus, if `P=#{y:q_y=q}` and `d>s`, then

> `P(d-s)<=n`.                                                 (G8)

Equivalently the number `L=N-P` of strict q-loss rows satisfies

> `L >= max(0, N-floor(n/(d-s)))`.                             (G9)

Since every strict loss is an integer at least one, combining (G1) and (G9) yields the strengthened compatibility bound

> `sum_v lambda_v w_v + sum_y mu(D_y)`
> ` <= N a - max(0,N-floor(n/(d-s)))`.                         (G10)

This is the first global inequality in the project that converts finite core size and support repetition directly into a mandatory total repivot loss.

### Repeated support corollary

If one support class `D` occurs for at least two owners, then every point of D is decorated. Hence, when `s<d`, none of those owners can be a q-plateau row. Every owner using that repeated support has

`q_y<=q-1`.                                                    (G11)

Thus repeated support classes create a strict loss penalty unless the entire missing set S is itself decorated.

## 5. Equality-case rigidity

If the left side of (G1) is zero, then every row is a q-plateau row. Therefore:

1. every row saturates its allowance:
   `w(D_y)+mu(D_y)=a`;
2. every support has at most s decorated vertices;
3. every support has at least `d-s` private globally clean vertices;
4. if `s<d`, no support class can repeat.

If additionally `a<d-1`, the common-S overlap theorem gives that two supports are equal or disjoint. Combining this with item 4 shows that, in a zero-loss equality state with `s<d`, all supports are pairwise disjoint. Hence

> `Nd<=n`.                                                     (G12)

If equality in (G8) also holds, the plateau supports partition exactly `P(d-s)` clean private vertices and every remaining support incidence is on decorated vertices. This is the canonical equality geometry that should be attacked rather than continuing layer-by-layer case enumeration.

## 6. Support-overlap and cross-edge constraints

The already-proved joint-row theorem gives, for two common-S supports with overlap `r=|D_i intersect D_j|`,

> `r(d-r)<=a`.                                                (G13)

Therefore if `a<d-1`, proper overlap is impossible.

For disjoint supports,

> `e_H(D_i,D_j)<=min(w(D_i),w(D_j))`
> `<=min(a-mu(D_i),a-mu(D_j))`.                               (G14)

Thus low allowance simultaneously limits support overlap and target cross-density.

## 7. Low-charge witness theorem

Let

`U=union_(y in Y) D_y`

and let `v in H\U` have charge `w_v=t`.

Row closure gives

`e_H(v,D_y)<=t`

for every support row. Because `alpha(H)<=3`, an independent triple in

`U\N_H(v)`

together with v would be an independent 4-set. Hence

> **Low-charge witness theorem**
>
> `alpha(H[U\N_H(v)])<=2`.                                   (G15)

Moreover each support loses at most t vertices to `N_H(v)`.

The V5 zero-charge concentration theorem is the special case `t=0`. The higher-layer strategy should use `t=1,2` witnesses rather than requiring an outside zero-charge vertex.

A low-charge witness exists automatically whenever

`H\U` is nonempty and its average charge is small. In particular,

`min_(v in H\U) w_v <= floor(W/(n-|U|))`,                    (G16)

where `W=sum_H w_v`.

This is the natural replacement for the V5 `W<=28` zero-charge threshold in higher layers.

## 8. Incidence-hypergraph interpretation

Associate to the common-S family the d-uniform support hypergraph

`I=(U,{D_y:y in Y})`.

Then

- `lambda_v` is the incidence degree of v;
- (G1) is the exact global gain/loss identity;
- (G4) is zero-charge incidence compression;
- (G5)--(G6) convert high incidence degree into global decoration;
- (G8)--(G10) convert finite core size into mandatory strict q-loss;
- (G13) bounds support codegrees;
- (G14) bounds target density between disjoint hyperedges;
- (G15) turns an outside low-charge point into a near-alpha-two theorem for the support union.

Thus the correct global object is the support-incidence hypergraph, not the list of edge layers E333,...,E340.

## 9. Existing backend results as corollaries / equality closures

### E333 five-family forcing

The V4 families `D2-A/B/C/D,R9` are all common two-point missing-set families. V5 supplies the low-charge concentration/capacity consequences and closes them simultaneously except for the unique allowance-two balanced equality geometry. That equality geometry is forced to two cliques joined by a perfect matching and is then excluded by the exact residual ledger.

Hence E333 is naturally interpreted as the first completed application of the global support-compatibility framework, not as five unrelated case proofs.

### Cores 211--213

V6 proves that for a repeated two-point missing set with `r=1`, allowance at most2 and `K in {2,4,6}`, multiplicity is at most6. The former scalar equality case is again forced to the two-clique-plus-perfect-matching geometry and is excluded analytically by intersecting-K11 rigidity.

This is a second application of the same framework beyond a single edge layer.

## 10. Current global closure target

The theorem above is fully analytic. What is not yet proved is that every local survivor in E334--E340 enters a support-hypergraph regime strong enough for (G1)--(G16) plus hereditary density caps to force a contradiction.

The remaining project should therefore be organized around one bridge statement, recorded separately in `GLOBAL_SUPPORT_BRIDGE_FRONTIER.md`, rather than eight edge-layer closures.

## 11. Generalization

Nothing in (G1)--(G16) uses the numerical values 35,12,211 except through:

- shell size h;
- core size n;
- the core baseline h-1;
- the exact exchange identity;
- the all-pivot minimum-degree contract;
- hereditary density caps used only in later capacity/equality closures.

Therefore the charging/packing part is parameterized and is a plausible reusable theorem for higher r once the analogous pivot reduction and all-pivot core lower-degree statement are available.
