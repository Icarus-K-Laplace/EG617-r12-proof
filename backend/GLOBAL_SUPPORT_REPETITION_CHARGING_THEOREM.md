# Global Support Repetition-Charging Theorem

Status: `PROVED_ANALYTIC`.

Dependencies: the exact common-S repivot identity, all-pivot core minimum-degree baseline, exact decoration transport, and lexicographic maximality of `(q,tau)`.

This strengthens `GLOBAL_SUPPORT_COMPATIBILITY_THEOREM.md` by converting support-incidence repetition itself into a quantitative lower bound on the number of strict q-loss repivots.

## 1. Setup

Use the common-S notation of `GLOBAL_SUPPORT_COMPATIBILITY_THEOREM.md`:

- shell size `h`, core size `n`;
- `N` owner rows with the same missing set `S`, `|S|=d`;
- support of owner y is `D_y`, `|D_y|=d`;
- `lambda_v=#{y:v in D_y}`;
- `kappa_v=d_H(v)-(h-1)`;
- `w_v=kappa_v+e_F(v,S)`;
- support internal missing count `mu(D_y)`;
- row allowance `a`;
- globally decorated set X;
- `s=|S intersect X|`.

Put

`Phi=sum_v lambda_v w_v + sum_y mu(D_y)`.

The exact support-gain identity is

`sum_y(q-q_y)=Na-Phi`.                                      (1)

## 2. Incidence repetition forces decoration

A core vertex v with `lambda_v>=1` has

- core degree at least `(h-1)+kappa_v`;
- at least `lambda_v` target neighbours among the owners;
- at least `e_F(v,S)` further target neighbours in S.

The owner family is disjoint from S, so these degree contributions are disjoint. Therefore

`d_F(v)>=h-1+kappa_v+lambda_v+e_F(v,S)`.

Since `g_v=d_F(v)-h`, we obtain the sharpened bound

> `g_v >= w_v+lambda_v-1`.                                  (2)

Consequently every support-union vertex satisfying

`lambda_v>=2` or `w_v>=1`

is globally decorated.

The only support incidences not forced to be decorated by (2) occur at vertices with

`lambda_v=1` and `w_v=0`.                                   (3)

## 3. Forced-decorated incidence count

Define

`C=#{v:lambda_v=1 and w_v=0}`.

Every such vertex contributes exactly one support incidence. Define

> `J=Nd-C`.                                                   (4)

Thus J is the number of support incidences lying on vertices which are forced decorated by repetition/charge.

Equivalently

`J=sum_(lambda_v>=2 or w_v>=1) lambda_v`.

Let

`P=#{y:q_y=q}`

be the plateau rows and

`L=N-P`

the strict q-loss rows.

## 4. Repetition-to-loss inequality

For a plateau row y, exact tau transport and lexicographic maximality give

`|D_y intersect X|<=s`.

Every incidence counted by J lies on a decorated vertex. Hence a plateau row contains at most s incidences counted by J.

A strict row contains at most d such incidences.

Summing over all owners gives

`J<=Ps+Ld`
` =(N-L)s+Ld`
` =Ns+L(d-s)`.                                               (5)

Assume `d>s`. Then

> **Repetition-loss bound**
>
> `L >= ceil( max(0,J-Ns)/(d-s) )`.                          (6)

Every strict q-loss is an integer at least one. Combining (1) and (6) yields

> **Global repetition-charging inequality**
>
> `Phi + ceil(max(0,J-Ns)/(d-s)) <= Na`.                     (7)

Therefore, if a proposed support-incidence system satisfies

`Phi + ceil(max(0,J-Ns)/(d-s)) > Na`,                        (8)

then at least one legal repivot has `q_y>q`.

This is a direct improving-repivot criterion stated entirely in global support-incidence variables.

## 5. Pure repetition corollaries

Define the weighted repeated-incidence count

`Rstar=sum_(lambda_v>=2) lambda_v`.

Since all such incidences are counted by J,

`J>=Rstar`.

Hence

> `L >= ceil(max(0,Rstar-Ns)/(d-s))`.                         (9)

Thus sufficiently much support repetition alone forces strict q-loss rows even before using core charge.

Also define the total incidence repetition excess

`R0=sum_v max(lambda_v-1,0)=Nd-|U|`,

where `U=union D_y`.

Since `J>=R0`, a weaker but support-union-only bound is

> `L >= ceil(max(0,Nd-|U|-Ns)/(d-s))`.                       (10)

Using `|U|<=n` recovers the finite-core plateau-packing theorem as a corollary.

## 6. Equality rigidity

Suppose equality holds in (7). Then every inequality used above is saturated.

Consequently:

1. every strict row has exactly one unit of q-loss;
2. every plateau row contains exactly s forced-decorated incidences whenever `J>Ns`;
3. every strict row contains d forced-decorated incidences whenever the ceiling in (6) is exact without remainder;
4. every support incidence not counted by J lies on a private zero-charge vertex (`lambda=1,w=0`);
5. all remaining freedom is confined to the placement of the forced-decorated incidence hypergraph and the internal missing counts `mu(D_y)`.

This converts a non-strict charging argument into a finite equality-geometry problem.

In particular, equality forces the support hypergraph to use the minimum possible number of private clean vertices compatible with tau-maximality, while simultaneously saturating the charge budget `Phi=Na-sum(q-q_y)`.

This is the natural point at which the V5 two-clique-plus-matching geometry, the d3 common-pair/four-set/sunflower geometries, and the q36--q38 plateau geometries arise.

## 7. Relation to the requested global theorem

The desired high-backend contradiction can now be split into two conceptual steps rather than edge layers:

1. **charging step (proved here):**
   excessive support repetition/charge implies an improving repivot by (8);
2. **equality-rigidity bridge (open globally):**
   if (8) is not strict, classify the support hypergraphs attaining equality and exclude them by hereditary density caps, independence, or core-excess rigidity.

Thus the remaining hard theorem is no longer `E334`, `E335`, etc. It is the equality-rigidity bridge for a small list of support-hypergraph regimes.

## 8. Parameterized nature

The proof uses h,n,d,a,s symbolically. The r=12 values `h=13,n=35` are not intrinsic to the charging argument.

Accordingly this theorem is a candidate reusable component for r>=13, conditional on having the analogous pivot contract, all-pivot core degree baseline, and decoration transport identity.
