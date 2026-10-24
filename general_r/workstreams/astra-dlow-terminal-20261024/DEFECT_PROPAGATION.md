# Robust joint kernel capacity, with unique edge ownership

Date: 2026-10-24. Status: **PROVED**.

This replaces an attempted per-defect propagation chain by a simultaneous
capacity inequality. It applies to arbitrary cover networks once the
actual five-clique / bounded-kernel reduction has been proved.

## 1. General statement

Let V have 5r+1 vertices and be partitioned as

    V = H disjoint-union C_1 ... disjoint-union C_5,

where |H|=m and each C_j is a clique in target color F.
All pairs have exactly one of r colors, and every non-target color G_i
has alpha(G_i)<=r. Assume delta(F)>=r+epsilon.

Then, writing h=e_F(H),

    r <= (3m^2+5m+2)/2 - epsilon m -3h.                 (KC)

There is no hypothesis on target cross edges between distinct C_j,
and no assumption that any non-target color is a clique partition.

## 2. A per-color cover inequality

Fix a non-target color i. Put e_i=e(G_i[H]).
Delete from H one endpoint of each color-i edge; duplicates in the
deletion list are counted only once. The remaining independent set
R_i has size at least m-e_i. If that number is negative, the empty set
still satisfies the stated lower bound.

Each C_j is independent in color i, by exclusive edge ownership.
Thus

    R_i union (C_j \ N_(G_i)(R_i))

is independent in color i. The independence cap implies

    |N_(G_i)(R_i) intersect C_j|
        >= |R_i|+|C_j|-r.

The number of edges from H to C_j is at least this neighborhood size.
Adding over the FIVE DISJOINT destination sets gives

    e_(G_i)(H,V\H)
       >= 5|R_i|+sum_j|C_j|-5r
        = 5|R_i|+1-m
       >= 4m+1-5e_i.                                   (1)

A negative individual right side is harmless: the inequality remains
valid, and no positive-part replacement in the wrong direction occurs.

This is a cover condition for all independent kernel selections. It is
valid even if the actual graph uses split covers, multiple blocks,
reused edges, or cyclic defect networks.

## 3. Sum across actual colors exactly once

Different colors own disjoint unordered pairs. Therefore

    sum_(i>0)e_i = binom(m,2)-h.                         (2)

Similarly the sum of (1) over all non-target colors is a lower bound
for the number of NON-TARGET pairs in the cut H : V\H:

    e_non(H,V\H)
      >= (r-1)(4m+1)-5[binom(m,2)-h].                   (3)

The target degree sum on H gives the independent cut bound

    e_F(H,V\H)=sum_(v in H)d_F(v)-2h
             >=m(r+epsilon)-2h.                       (4)

Every unordered pair across this cut occurs once, in either (3) or
(4). Hence the exact cut capacity m(5r+1-m) is at least their sum:

    m(5r+1-m)
      >= m(r+epsilon)-2h
          +(r-1)(4m+1)-5[binom(m,2)-h].

Rearrangement gives KC.

The factor 5 multiplying e_i is NOT five actual-edge charges.
It is a bound for how much removing a kernel vertex can reduce five
separate independent-set demands. The only edges charged to the
capacity are the color-owned cut edges in (3) and (4).
Edges internal to H enter (2) once; edges between C_j and C_k are not
charged at all.

## 4. Stronger exact instance inequality

One may choose R_i to be a maximum independent set of G_i[H].
With t_i=m-alpha(G_i[H]) (its minimum vertex-cover size), the stronger
necessary inequality is

    m(5r+1-m)
       >= m(r+epsilon)-2h
           +(r-1)(4m+1)-5 sum_(i>0)t_i.                 (5)

Since t_i<=e_i, (5) implies KC. Thus adjacent or cyclic kernel defects
which lower the minimum vertex-cover size below the number of their
edges only strengthen the obstruction. This records precisely where
closed defect chains can improve, rather than invalidate, the bound.

## 5. Scope relative to the requested robust theorem

The five C_j are actual target cliques obtained from the five-anchor
construction, not Furedi ideal groups. The kernel is bounded by twelve.
Consequently all original edge perturbations and all non-target cover
networks are included in (1)--(5), regardless of whether they meet an
ideal hub set. A hub may be the only representative of a label in a
block; no representative assumption occurs in the proof.

KC closes all requested offset windows for r>=221 after the kernel
reduction. For smaller r it is a necessary inequality; it is not
claimed to close the remaining incidence types.

