# Global Shell-Poor Decoration-Incidence Theorem

Status: `PROVED_ANALYTIC` under the q36 CORE211 shell-poor interface.

Dependencies:

- `Q36_CANDIDATE_COVERAGE_CLUSTER_REDUCTION.md`;
- `Q36_SHELL_POOR_SIMULTANEOUS_INTERFACE.md`.

Purpose: replace independent one-spoke analysis by a weighted multi-pivot incidence theorem. The theorem quantifies how the small global core-decoration budget must be reused across the large anti-neighbourhoods of all one-spoke pivots.

## 1. Setup

Let p be a q36 CORE211 pivot in the shell-poor regime.

Let

`P={v_1,...,v_k}`

be k nonadjacent-to-p one-spoke legal pivots in the old 35-core H. The candidate-coverage theorem gives

> `k>=5`.                                                     (I1)

For each i let

`Z_i=H\(N_H(v_i) union {v_i})`.

Then

`|Z_i|=22`.

Let core decoration weights be

`g_u=d_F(u)-13>=0`,

and write

`G_H=sum_(u in H) g_u`.

The simultaneous one-spoke interface proves

> `25<=G_H<=28`,                                             (I2)

and, for every i,

> `g(Z_i)>=11+g_(a_i)>=11`,                                 (I3)

where a_i is the unique old-shell target neighbour of v_i.

## 2. Decoration-incidence multiplicity

For each core vertex u define

`m_u=#{i:u in Z_i}`.                                         (I4)

Thus m_u is the number of one-spoke pivots to which u is target-nonadjacent inside the old core.

Double-count weighted incidences:

`I=sum_i g(Z_i)`
` =sum_u g_u m_u`.                                           (I5)

By (I3),

> `I>=11k`.                                                   (I6)

This is the exact global quantity coupling all one-spoke anti-neighbourhoods.

## 3. High-codegree decorated core vertex

Since

`sum_u g_u=G_H<=28`,

we have

`I<=G_H max_u m_u<=28 max_u m_u`.

Combining with (I6):

> **High-codegree decoration theorem**
>
> `max_(g_u>0) m_u >= ceil(11k/28)`.                         (I7)

Consequences:

- k=5: some decorated core vertex lies in at least2 anti-neighbourhoods;
- `k>=6`: some decorated core vertex lies in at least3 anti-neighbourhoods;
- `k>=8`: some decorated core vertex lies in at least4 anti-neighbourhoods;
- `k>=11`: some decorated core vertex lies in at least5 anti-neighbourhoods.

Thus increasing one-spoke abundance forces genuine multi-pivot correction concentration.

## 4. Repeated-decoration mass

Let

`R=sum_(u:m_u>=2) g_u`                                      (I8)

be the total core-decoration mass carried by vertices belonging to at least two anti-neighbourhoods.

Vertices outside this set contribute at most one weighted incidence each. Vertices inside it contribute at most k incidences per unit of decoration. Hence

`I<=G_H+(k-1)R`.                                             (I9)

Combining `I>=11k` and `G_H<=28` gives

> `R>=ceil((11k-28)/(k-1))`.                                (I10)

In particular:

- k=5: `R>=7`;
- k=6: `R>=8`;
- k=7: `R>=9`;
- every k>=5 forces at least seven units of core decoration onto vertices simultaneously anti-neighbouring at least two one-spoke pivots.

This is a strong global reuse constraint: a positive fraction of the entire 25--28 decoration budget cannot be private to one pivot.

## 5. Pairwise intersection mass

For every pair i<j define

`c_ij=g(Z_i intersect Z_j)`.                                (I11)

Then

`sum_(i<j)c_ij`
` =sum_u g_u C(m_u,2)`.                                     (I12)

To lower-bound this quantity, split each integer decoration weight g_u into g_u identical unit tokens, each inheriting the same multiplicity m_u. There are at most28 tokens and their total multiplicity is at least11k.

By convexity of `C(m,2)`, the pair-overlap sum is minimized by distributing the multiplicities as evenly as possible across 28 tokens.

Write

`11k=28q+r`, `0<=r<28`.                                     (I13)

Then

> **pair-overlap mass bound**
>
> `sum_(i<j)c_ij >= (28-r) C(q,2)+r C(q+1,2)`.              (I14)

For the first shell-poor value k=5,

`55=28*1+27`,

so

> `sum_(i<j)c_ij>=27`.                                      (I15)

There are ten pivot pairs, hence some pair satisfies

> `g(Z_i intersect Z_j)>=3`.                                (I16)

For k=6, the same calculation gives total pair-overlap mass at least48, so some pair has shared decoration mass at least4.

## 6. Interface with core adjacency and shell labels

The existing simultaneous interface gives a second kind of compatibility:

if two one-spoke pivots v_i,v_j are target-nonadjacent in H, then their two unique shell labels

`{a_i,a_j}`

meet every triangle of the shell missing graph M.

Therefore every pair of one-spoke pivots carries two simultaneous data:

1. a weighted common anti-neighbourhood mass `c_ij`;
2. when the pair is a core nonedge, a size-at-most-two shell-triangle cover `{a_i,a_j}`.

The shell-poor problem is consequently a coupled weighted graph system on P, not a collection of independent near-Mantel neighbourhoods.

## 7. New canonical shell-poor frontier

After this theorem, the shell-poor regime can be formulated as follows.

There is a set P of at least five ordinary degree-12 core vertices such that:

- each has a 22-point complement-core neighbourhood Z_i;
- `J=overline H` is K4-free and each `J[Z_i]` is triangle-free;
- total core decoration is at most28;
- each Z_i contains decoration mass at least11;
- at least seven decoration units have anti-neighbourhood multiplicity at least2;
- the total pairwise shared decoration mass is at least27 when k=5;
- core-nonedge pairs of P generate two-label covers of all shell-missing triangles.

Thus the remaining theorem is a **high-codegree / triangle-cover compatibility theorem** for this one weighted incidence graph.

It is strictly smaller than five separate near-Mantel stability arguments.

## 8. Equality geometry

At the lowest k=5 boundary, minimal overlap corresponds to distributing 55 incidences over28 decoration tokens as

- 27 tokens of multiplicity2;
- one token of multiplicity1.

Any departure from this distribution increases the pairwise overlap mass.

Hence a putative extremal survivor is forced toward an almost two-fold cover of the decoration budget by the five anti-neighbourhoods.

This is the shell-poor analogue of the equality geometries in the support-incidence theorem: a global average inequality leaves one rigid incidence design to classify.

## 9. General principle

The proof is a pure weighted-incidence argument:

if k local pivot neighbourhoods each demand mass at least L from a global nonnegative budget G, then high membership multiplicity and pairwise overlap are unavoidable.

The formulas

`max m >= ceil(kL/G)`

and the convex pair-overlap lower bound are parameterized and can be reused in higher-r multi-pivot compatibility problems.