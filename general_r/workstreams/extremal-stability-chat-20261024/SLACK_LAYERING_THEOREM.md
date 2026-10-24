# Slack Layering — F-004

## 1. Exact slack layers

For a hypothetical counterexample, s_i>=0 and sum_i s_i=m_0=r^2(r-1)/2. Thus the number of colors with s_i>lambda*r^2 is strictly less than (r-1)/(2lambda). Near the average layer lambda≈1/2 this gives little structure.

The mean slack is C=binom(r,2), so the budget alone does not guarantee a color with s_i<=r^2/100. The new linear neighborhood theorem therefore cannot be applied to a guaranteed color without extra information.

## 2. Low-slack layer

If s_i<=r^2/100, the weighted transversal theorem gives d_i>=31r/40. More generally, for s_i<r^2/4,
d_i >= L_i - 2s_i/L_i, where L_i=r-2sqrt(s_i).

## 3. Medium-slack layer and two smallest colors

The F-003 defect argument extends to s_i<=r^2/2. For 1<=d_i<r, the Turán deficit t of H_i[B_i] relative to T_(r-1)(r^2-d_i) satisfies
t<=s_i-r(r+1-2d_i)/2<=r(d_i-1/2)<=r d_i.
Füredi's partition lemma gives variance <5r d_i and missing cross-edge count b<=2r d_i. The same transversal-defect count rules out d_i<sqrt(r/1600). The d_i=0,1 cases are excluded by Brouwer bounds exceeding r^2/2. Hence
**s_i<=r^2/2 implies d_i>=max(2,ceil sqrt(r/1600))** for r>=4.

The second-smallest slack obeys s_(2)<=m_0/(r-1)=r^2/2, so at least two colors have neighborhoods this large.

## 4. High-slack layer

The budget permits up to r-2 colors with s_i>r^2/2 (integer strictness included). The current low/medium-slack estimates do not force enough exact partitions to invoke the frozen affine nonextension theorem.

## Status

- Slack-layer count: PROVED_ANALYTIC.
- Low-slack linear degree bound: PROVED_CONDITIONAL.
- Two smallest colors have degree at least Omega(sqrt(r)): PROVED_CONDITIONAL.
- Global contradiction from slack layering alone: DISPROVED as a strategy by d_i=r, s_i=C.
- Cross-color incidence closure: OPEN.
