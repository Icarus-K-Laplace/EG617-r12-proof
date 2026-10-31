# Exact contextual recurrence certificate

## R0. Scope — PROVED

Fix the original target graph G and temporarily assume no induced `R(4,49)` occurs in it. All families below consist of INDUCED subgraphs of this one G with the stated alpha and omega bounds. Empty denotes a proved contextual impossibility, not solver UNSAT. This is a reductio hypothesis for extraction and cannot be exported as generic R449 emptiness.

Use `B(a,n)` as a lower bound for the edge count of every such subgraph. An empty entry remains empty at larger orders by taking induced subsets. Base cases: `B(a,0)=0`; `a=0` is empty at positive order; `a=1` is a clique on at most11 vertices. Initial order cutoffs are24 for a2,37 for a3,49 for a4. Edge seeds are131,210,234,284,308 at `(2,23),(3,35),(3,36),(4,47),(4,48)`.

## R1. Minimum-pivot identity — PROVED

In an admissible J of order n and `alpha<=a`, take a minimum-degree h vertex p, `A=N(p)`, and `C=J-N[p]`, of order `m=n-h-1`. Define `M=complement J[A]`, `z=e(M)`, `g_v=d_J(v)-h>=0`, `t_v=|N_C(v)|`. Then

    t_v=d_M(v)+g_v,
    q=z+sum g,
    e(J)=binom(h+1,2)+q+e(C),
    q=t(S)-e(M[S])+e(M[A\S])+sum_(A\S)g.

Because `omega(J)<=11`, `alpha(M)<=10`. Thus

    q>=z>=Z=max(p_10(h), binom(h+1,2)-D(h+1), binom(h,2)-D(h)).

## R2. Coverage and matching guarantee — PROVED

For `h>=11`, M has an edge. Let `M_b` denote the certified maximum possible order with `alpha<=b` in the contextual class. An M-edge's two core rows have union at least `beta=max(0,m-M_(a-2))`. Thus `q>=beta-1`; also `e(C)+beta<=D(m+2)`.

A maximum matching leaves an independent set, so its size is at least `ceil((h-10)/2)`. The 13/14-point caps additionally force two matching edges for `h>=12` and three for `h>=13`. Therefore one may use

    k(h)=max(ceil((h-10)/2), 1+[h>=12]+[h>=13]).

For t matching edges their 2t endpoints have weight sum at least `t*beta`; Turan and R1 give

    q>=t*beta-binom(2t,2)+p_a(2t), 1<=t<=k(h).

## R3. Exhaustive triangle split — PROVED

If M is triangle-free, the same endpoint sets give `q>=t*beta-t^2` by Mantel. If M has a triangle, its three rows have union at least `gamma=max(0,m-M_(a-3))`, so `q>=gamma-3` and `e(C)+gamma<=D(m+3)`. For a=2 the triangle alternative is impossible. If the latter density inequality fails, discard just that alternative. Take the MINIMUM of the two surviving alternative lower bounds, each including all common q floors.

## R4. Full induction — PROVED

Process `a=1..12` and, within each a, `n=1..145`. For each nonempty core row use R1–R3 and set

    L_h=max(ceil(n*h/2), B(a-1,m)+binom(h+1,2)+Q_h).

The node bound is the maximum of `min_h L_h`, `p_a(n)`, the applicable seed, and (for `n>2`) `ceil(n*B(a,n-1)/(n-2))`. The last inequality counts each edge in exactly `n-2` vertex deletions. An empty predecessor, no surviving h row, or a bound `>D(n)` makes the node empty.

Core and maximum-order inputs have smaller a; deletion averaging has smaller n. Thus this is a finite acyclic deduction. In particular the contextual49 exclusion never depends on a backend theorem: it is the explicit temporary hypothesis throughout.

## R5. Arithmetic certificate — COMPUTATION_CERTIFIED

The stored certificate was independently replayed by two integer implementations. The verifier checks all 1752 nodes, all 144 outer-stop comparisons, and the 192 S30 scalar entries.

Unique nonexcluded outer stop:

    (d,j,a,n)=(11,6,5,61), floor=397, budget=408.

The 73-point contextual bound is475. There is no dependence on E328/E329/E330 or a generic R449 lower bound.