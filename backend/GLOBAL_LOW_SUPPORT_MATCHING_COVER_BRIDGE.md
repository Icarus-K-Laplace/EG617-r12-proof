# Global Low-Support Matching-Cover Bridge

Status: `PROVED_ANALYTIC`.

Dependencies:

- `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md`;
- `GLOBAL_D2_TRANSVERSAL_SHARP_CAPACITY_THEOREM.md`;
- `GLOBAL_SUPPORT_REPETITION_CHARGING_THEOREM.md`;
- the common-S row-closure cross-edge bound for disjoint supports.

Purpose: convert the remaining low-support extraction problem into a sharp dichotomy:

> either a large family contains too many pairwise-disjoint low-cross supports and is impossible immediately, or all support classes are hit by a bounded core transversal, forcing incidence / charge concentration.

This is independent of the labels `E333,...,E340`.

## 1. Abstract setup

Let `H` be a graph with

`alpha(H)<=3`.

Let `Y` be a family of `N` owner rows sharing one missing set `S`. Let the distinct support classes form a `d`-uniform hypergraph

`F={D^(1),...,D^(m)}`

on `V(H)`.

Assume that whenever two distinct support classes `D,E` are disjoint,

`e_H(D,E)<=c`.                                               (1)

Let

`nu(F)` be the matching number of the support hypergraph, i.e. the maximum number of pairwise-disjoint distinct support classes.

Let `T(d,c)` be any certified block-transversal capacity such that no `T(d,c)+1` pairwise-disjoint d-supports satisfying (1) can occur in a graph with independence number at most3.

The currently proved values needed in the r=12 backend are

- `T(2,1)=6` from `GLOBAL_D2_TRANSVERSAL_SHARP_CAPACITY_THEOREM.md`;
- `T(3,1)=3` from `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md`;
- `T(3,2)=6` from `GLOBAL_BLOCK_TRANSVERSAL_THEOREM.md`.

## 2. Matching bound

By definition of `T(d,c)`, any matching of size `T(d,c)+1` would be a family of pairwise-disjoint d-blocks with cross target-edge count at most c, contradicting the certified block-transversal capacity.

Therefore

> `nu(F)<=T(d,c)`.                                           (M1)

This is the extraction half of the bridge.

## 3. Small transversal theorem

Take a maximal matching

`M={D_1,...,D_k}`

in `F`. By (M1),

`k<=T(d,c)`.

Put

`C=D_1 union ... union D_k`.

If some support class `D` were disjoint from C, then `M union {D}` would be a larger matching, contradicting maximality.

Hence every support class meets C.

Therefore

> **Matching-cover conclusion**
>
> there exists a core set C meeting every support class with
>
> `|C|<=d T(d,c)`.                                          (M2)

Equivalently the support hypergraph transversal number satisfies

`tau(F)<=d T(d,c)`.                                         (M3)

This is purely structural and uses no owner multiplicities.

## 4. Owner-incidence concentration

Return to the owner rows. For each core vertex v write

`lambda_v=#{y in Y:v in D_y}`.

Because every owner support meets C,

`sum_(v in C) lambda_v >= N`.                               (M4)

Hence some vertex of C satisfies

> `lambda_v >= ceil(N/|C|) >= ceil(N/(dT(d,c)))`.            (M5)

More importantly, let

`J=sum_(lambda_v>=2 or w_v>=1) lambda_v`

be the forced-decorated incidence count from `GLOBAL_SUPPORT_REPETITION_CHARGING_THEOREM.md`.

An incidence lying in C but not counted by J must occur at a vertex with

`lambda_v=1, w_v=0`.

There are at most `|C|` such incidences. From (M4),

> `J >= max(0,N-|C|)`
>
> `  >= max(0,N-dT(d,c))`.                                  (M6)

Thus failure of the disjoint-support extraction forces a quantitative amount of repeated/charged incidence.

## 5. Matching-cover repivot-loss bound

Use the notation of `GLOBAL_SUPPORT_REPETITION_CHARGING_THEOREM.md`:

- support size d;
- `s=|S intersect X|`;
- `L=#{y:q_y<q}`.

When `d>s`, the repetition-loss theorem gives

`L >= ceil(max(0,J-Ns)/(d-s))`.

Combining with (M6) yields

> **Matching-cover loss inequality**
>
> `L >= ceil( max(0, N-dT(d,c)-Ns)/(d-s) )`.                 (M7)

Consequently, with

`Phi=sum_v lambda_v w_v + sum_y mu(D_y)`,

the exact support-gain identity gives the strengthened compatibility condition

> `Phi + ceil(max(0,N-dT(d,c)-Ns)/(d-s)) <= Na`.             (M8)

If (M8) fails, some legal repivot has `q_y>q`.

Thus both alternatives of the bridge are now quantitative:

1. large disjoint matching => impossible by block transversals;
2. small matching => bounded transversal => forced repetition/charge => mandatory total q-loss.

## 6. r=12 numerical corollaries

### 6.1 Two-point supports with cross allowance one

For `d=2,c=1`,

`T(2,1)=6`.

Hence every such support family satisfies

> `nu(F)<=6`,                                                (M9)
>
> `tau(F)<=12`.                                              (M10)

Therefore any D2/R9 forcing statement which produces seven pairwise-disjoint support classes is killed immediately by one theorem.

If it does not, every support class meets a 12-point core set, and all remaining work is incidence concentration on that set rather than an E-layer case split.

### 6.2 Three-point supports with cross allowance one

For `d=3,c=1`,

`T(3,1)=3`.

Hence

> `nu(F)<=3`,                                                (M11)
>
> `tau(F)<=9`.                                               (M12)

This is directly relevant to low-allowance pieces of the E334 d3 eleven-view system: either four disjoint triple supports exist and the state is impossible, or all eleven views are controlled by a nine-point core transversal.

### 6.3 Three-point supports with cross allowance two

For `d=3,c=2`,

`T(3,2)=6`.

Hence

> `nu(F)<=6`,                                                (M13)
>
> `tau(F)<=18`.                                              (M14)

In particular, any extraction of seven disjoint A2 triple supports closes the branch immediately. Failure of extraction is no longer an unstructured eleven-view problem: every support must meet one bounded 18-point core set.

## 7. Equality / near-equality geometry

The useful point is not only the numerical cover size.

Suppose a residual family is close to the matching threshold and close to equality in the repetition-charging inequality. Then simultaneously:

- a maximal support matching has size near T(d,c);
- its union C is a minimum or near-minimum transversal;
- almost all support rows meet C in exactly one point;
- almost all incidences in C not private-clean are forced decorated;
- repeated classes contribute strict q-loss unless the missing set is fully decorated;
- disjoint block pairs are near equality in the block-transversal density theorem;
- the hereditary support-packing inequality must also be near saturation if owner multiplicities are large.

Thus the surviving object is forced toward a bounded-hub equality geometry rather than an arbitrary support hypergraph.

This is the structural origin of the already observed common-pair, sunflower, two-clique-plus-matching and repeated-K3 terminals.

## 8. Minimal remaining bridge

After this theorem, the low-support part of the global bridge no longer needs a generic extraction lemma.

The remaining statement is the following bounded-transversal rigidity problem:

> **Low-Support Transversal Rigidity Lemma (OPEN).**
> In an r=12 maximal-pivot common-S family with d in {2,3}, if all support classes meet a transversal C of the sizes in (M10), (M12), or (M14), and the global repetition-charging inequality is non-strict, then the support-incidence system collapses to one of a finite list of hub geometries (common pair / sunflower / two-block matching / repeated clique support), each excluded by hereditary packing, core excess, or independence.

This is now the unique low-support bridge target.

It is strictly smaller than proving E334--E337 separately.

## 9. Generalization

Let H have `alpha(H)<=r`. Replace `T(d,c)` by any threshold certified from

`C(N,2)-ex(N,K_(r+1)) <= (c/d^2) C(N,2)`

plus any equality-rigidity strengthening at the boundary.

The maximal-matching proof of (M2), incidence concentration (M4)--(M6), and the coupling to the repetition-loss theorem are unchanged.

Therefore this matching-cover bridge is not specific to r=12. The r-specific input is only the block-transversal capacity threshold and the later equality-geometry exclusion.