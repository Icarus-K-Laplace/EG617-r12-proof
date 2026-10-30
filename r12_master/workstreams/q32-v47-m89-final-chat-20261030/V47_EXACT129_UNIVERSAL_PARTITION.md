# E408 Q32 — universal H-partition from an exact-129 color

Date: 2026-10-30  
Status: **PROVED_CONDITIONAL structural theorem** under the frozen Q32 core and the published Kang–Pikhurko equality classification.

## 1. Contract

Let the 61-point residual be partitioned as
\[
V=H\dot\cup O,\qquad |H|=47,\quad |O|=14.
\]
Assume the target-color core H has
\[
\alpha(H)\le4.
\]
Let C be any non-target color on V with
\[
e(C)=129,\qquad \alpha(C)\le12.
\]
The balanced-coloring hypothesis gives \(\alpha(C)\le12\): every 13-set must contain a C-edge.

No hypothesis \(\omega(C)\le5\), \(\omega(H)\le5\), or Type-I-only source mode is used.

## 2. Complement equality

Put \(G=\overline C\). Then
\[
e(G)=\binom{61}{2}-129=1830-129=1701,
\]
and
\[
\omega(G)=\alpha(C)\le12,
\]
so G is K13-free.

The balanced Turán graph \(T_{12}(61)\) has part sizes \(6,5^{11}\), hence
\[
t_{12}(61)=1830-\binom62-11\binom52=1705.
\]
Since \(12\le(61-1)/2\), Kang–Pikhurko Theorem 1 gives
\[
p_{12}(61)=t_{12}(61)-\lfloor61/12\rfloor+1
=1705-5+1=1701
\]
for the maximum edge count among K13-free, non-12-partite graphs.

There are two cases.

## 3. Case A: G is 12-partite

A 12-partition of G is a partition of V into at most twelve independent sets of G. Each part is therefore a clique in C. Its intersection with H is an independent set in H, so it has size at most four.

These at most twelve intersections partition H, which has 47 vertices. Since \(47=11\cdot4+3\), there must be exactly twelve nonempty parts, and their H-intersection sizes are
\[
4^{11},3.
\]
Thus H is partitioned into eleven independent 4-sets and one independent 3-set:
\[
\boxed{11K_4+K_3.}
\]

This case is important: balancedness does not rule out a 12-partite complement. No Kang–Pikhurko non-12-partite classification is invoked here.

## 4. Case B: G is not 12-partite

Now G lies in the class covered by Kang–Pikhurko Theorem 1 and attains the extremal value \(p_{12}(61)=1701\). Theorem 4 and Lemma 5 classify the equality constructions. Their twelve old part sizes are exactly
\[
(5^{12}),\qquad (4,5^{10},6),\qquad
(4,4,5^8,6,6).
\]
In each equality construction there is a special vertex x and twelve disjoint old parts
\[
N_1,\ldots,N_{12}
\]
partitioning \(V\setminus\{x\}\), with each \(N_i\) a clique in C. This is true for all three equality profiles; it does not assert that the full color graph is Type I or that the parts are all K5s.

Write \(n_i=|N_i|\), \(b_i=|N_i\cap O|\), and \(h_i=|N_i\cap H|=n_i-b_i\). Since \(N_i\cap H\) is independent in H,
\[
h_i\le4,\qquad b_i\ge n_i-4.
\]
For each of the three listed profiles,
\[
\sum_{i=1}^{12}(n_i-4)=60-48=12.
\]
Define the nonnegative integer excesses
\[
d_i=b_i-(n_i-4)=4-h_i\ge0.
\]

### B1. The special point x lies in O

Then
\[
\sum_i b_i=|O|-1=13,
\]
so \(\sum_i d_i=13-12=1\). Exactly one \(d_i\) is one and the others are zero. Hence the H-intersections have sizes \(3,4,\ldots,4\), giving
\[
\boxed{11K_4+K_3.}
\]

### B2. The special point x lies in H

Then
\[
\sum_i b_i=|O|=14,
\]
so \(\sum_i d_i=14-12=2\). There are exactly two possibilities:

- one \(d_i=2\), all others zero: H-intersection sizes \(2,4^{11}\), and the special point x adds a singleton;
- two \(d_i=1\), all others zero: H-intersection sizes \(3,3,4^{10}\), and x adds a singleton.

Thus the two partition shapes are
\[
\boxed{11K_4+K_2+K_1}
\qquad\text{or}\qquad
\boxed{10K_4+2K_3+K_1.}
\]

## 5. Universal conclusion

Combining Cases A and B:

> **Every exact-129 non-target color C on the 61-point Q32 residual induces one of exactly three partitions of H into independent parts:**
> \[
> 11K_4+K_3,\qquad
> 10K_4+2K_3+K_1,\qquad
> 11K_4+K_2+K_1.
> \]

This theorem covers:
- the 12-partite complement branch, which the earlier Type-I-only source gate omitted;
- all three non-12-partite Kang–Pikhurko equality profiles, including the two profiles with size-six parts.

It does not assume or conclude that C is Type I, that C has twelve K5 factors, or that \(\omega(C)\le5\).

## 6. Consequence of the tight-part lemma and remaining gap

The Hall/tight-part lemma in V47_TYPEI_PARTITION_OBSTRUCTION.md applies to all three partition shapes. Under
\[
|H|=47,\quad e(H)=285,\quad\delta(H)\ge12,\quad\alpha(H)\le4,
\]
it forces a clique of size at least six in H (or an independent 5-set, which is excluded by alpha(H)<=4).

This is a valid structural consequence for every exact-129 color, independent of its Type-I/II/III or 12-partite source mode. However, the actual Q32 core has only \(\omega(H)\le11\), so K6/K7 is allowed. This theorem therefore does **not** close Q32 by itself.

The missing mathematical task is now sharply isolated: exploit the forced K6/K7 structure, together with the 285-edge / excess-six core and the cross-color partition system, to obtain a contradiction under the genuine \(\omega(H)\le11\) cap. Do not reintroduce a K6-free assumption.
