# Slack–Neighborhood Tradeoff — F-004

Status: PROVED_CONDITIONAL on Füredi's partition lemma, Brouwer's non-partite Turán bound, and the Kang–Pikhurko equality classification in the boundary case.

## 1. Notation and extension constraint

Delete x from a hypothetical balanced coloring of K_(r^2+1). Let G_i be color i on the remaining r^2 vertices, H_i=complement(G_i), A_i=N_i(x), d_i=|A_i|, C=binom(r,2), and m_0=rC. Then sum s_i=m_0, sum d_i=r^2, and A_i hits every K_r in H_i.

## 2. Explicit Brouwer tradeoff

For 0<=d<r, put m=r^2-d. The graph H_i[B_i], B_i=V\A_i, is K_r-free, has independence number at most r, and has more than r(r-1) vertices. It is not (r-1)-partite. Brouwer's bound yields
s_i >= p_(r-1)(m)-m_0+floor(m/(r-1))-1,
where p_q(m)=binom(m,2)-T_q(m).

Evaluating the quotient/remainder gives
F_Br(r,d)=
- binom(r+2,2), d=0;
- binom(r+1,2), d=1;
- max(0, r(r+3-2d)/2 - 1), 2<=d<r.

The d=2 equality case is excluded by the Kang–Pikhurko classification, strengthening it to s_i>=C+1.

## 3. Weighted transversal tradeoff

Füredi's partition lemma applied to H_i gives an r-partition V_1,...,V_r, at most s_i internal edges, and at most b<=2s_i missing cross-edges. If n_a=|V_a|, the partition identity gives
sum_a (n_a-r)^2 <= 4s_i.
Thus if s_i<r^2/4, all parts have size at least L=r-2sqrt(s_i)>0.

Every transversal either intersects A_i or contains a missing cross-edge, since A_i hits every K_r of H_i. A random transversal gives
1 <= d_i/L + b/L^2 <= d_i/L + 2s_i/L^2,
so
**d_i >= r-2sqrt(s_i)-2s_i/(r-2sqrt(s_i))** whenever s_i<r^2/4.

Invert this inequality. For d<r define
U_r(d)=(2r-d-sqrt(d^2-2rd+2r^2))/2.
Then s_i>=ceil(U_r(d_i)^2). If s_i>=r^2/4, the same lower bound is automatic because U_r(d)^2 <= (3/2-sqrt(2))r^2 < r^2/4.

## 4. Linear rigidity in the low-slack layer

If s_i<=r^2/100, then L>=4r/5 and b<=r^2/50. Hence
d_i >= L-b/L >= 4r/5-r/40 = **31r/40**.
So s_i<=r^2/100 implies d_i>=31r/40.

## 5. Medium-slack strengthening

The F-003 defect argument extends to s_i<=r^2/2 and gives
d_i>=max(2,ceil sqrt(r/1600)) for r>=4.
The two smallest slacks satisfy s_(2)<=m_0/(r-1)=r^2/2, so both corresponding neighborhoods obey this bound.

## 6. Combined F_r(d) and integer optimization

For d<r, define F_r(d) as the maximum of:
1. F_Br(r,d);
2. ceil(U_r(d)^2);
3. C+1 if d<max(3,ceil sqrt(r/1024));
4. floor(r^2/2)+1 if d<max(2,ceil sqrt(r/1600)).
For d>=r, set F_r(d)=0. Then s_i>=F_r(d_i).

The scalar integer program has minimum
min sum_i F_r(d_i)=0 subject to sum_i d_i=r^2, attained at d_i=r for every i. Choosing s_i=C for every color satisfies sum_i s_i=m_0 and all scalar bounds. For prime-power r this slack vector is realized by the old affine-skeleton K_(r^2) family after assigning exactly C leftover-class edges to each color.

This is not a K_(r^2+1) counterexample. It shows that scalar summation alone cannot finish the proof. The missing constraint is simultaneous incidence: the disjoint A_i must hit every K_r of their respective H_i while every old edge has exactly one color.

## Status

- Brouwer tradeoff: PROVED_CONDITIONAL.
- Weighted transversal tradeoff: PROVED_CONDITIONAL.
- Low-slack linear bound: PROVED_CONDITIONAL.
- Scalar contradiction: DISPROVED as a strategy by the feasible d_i=r, s_i=C witness.
- Full joint rigidity / all-r theorem: OPEN.
