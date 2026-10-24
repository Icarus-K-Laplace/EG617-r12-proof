# Offset Ledger — Uniform Low-Offset Family

Date: 2026-10-24  
Branch: workstream/general-r-asymptotic-20261024

## Exact parameters

For a contextual 5r+1 terminal, let T be the independent near-anchor triple, W its common target anti-neighbourhood, and j=2r-|W|. Then |W|=2r-j, |O'|=|V minus (T union W)|=3r+j-2, J_W=complement of F[W] is triangle-free, and alpha(J_W)=omega(F[W])<=r-1.

For 2<=j<=7, p_2(2r-j)=binom(2r-j,2)-floor((2r-j)^2/4), and p_r(2r-j)=r-j. Define delta_0=e(F[W])-p_2(|W|) and delta_i=e(C_i[W])-(r-j). Then

delta_0 + sum_i delta_i = g_r(j)
= floor((2r-j)^2/4)-(r-1)(r-j).

## Exact offset table

| Anchor branch | j | |W| | |O'| | anchor degree sum | k range | W-local total slack |
|---|---:|---:|---:|---|---:|---:|
| delta(F)=r | 2 | 2r-2 | 3r | 3r+k | 0..2 | r-1 |
| delta(F)=r | 3 | 2r-3 | 3r+1 | 3r+k | 0..2 | r-1 |
| delta(F)=r | 4 | 2r-4 | 3r+2 | 3r+k | 0..2 | r |
| delta(F)=r+1 | 2 | 2r-2 | 3r | 3r+3+k | 0..2 | r-1 |
| delta(F)=r+1 | 3 | 2r-3 | 3r+1 | 3r+3+k | 0..2 | r-1 |
| delta(F)=r+1 | 4 | 2r-4 | 3r+2 | 3r+3+k | 0..2 | r |
| delta(F)=r+1 | 5 | 2r-5 | 3r+3 | 3r+3+k | 0..2 | r+1 |
| delta(F)=r+1 | 6 | 2r-6 | 3r+4 | 3r+3+k | 0..2 | r+3 |
| delta(F)=r+1 | 7 | 2r-7 | 3r+5 | 3r+3+k | 0..2 | r+5 |

Low branch anchor degrees are r+epsilon_t, with epsilon_t in {0,1}, k=sum epsilon_t<=2. High branch degrees are r+1+epsilon_t, again k<=2.

## Duplicate-incidence ledger under the bounded-W hypothesis

If every o in O' has at least one target edge to T, let D be the number of anchor incidences beyond the first one per vertex. Then D=sum_t d_F(t)-|O'|.

| Branch | D | Lower bound on H=sum_t h_t | Upper bound |
|---|---:|---:|---:|
| delta(F)=r | k-j+2 | 6+k | H<=2D |
| delta(F)=r+1 | k-j+5 | 9+k | H<=2D |

Here h_t counts anchor neighbours of t that also see another anchor. Since H=2n_2+3n_3=2D-n_3, H<=2D.

Combining gives:
- low branch: 2j<=k-2, impossible for j>=2 and k<=2;
- high branch: 2j<=k+1<=3, impossible for j>=2.

This is exact integer arithmetic; no asymptotic term or rounding is hidden.

## Forced high-incidence kernel

If all d_F(o,W)<=B, the contradiction applies whenever r>=j+4B. Choosing B=floor((r-j)/4) yields the necessary condition for any surviving terminal:

max_{o in O'} d_F(o,W) >= floor((r-j)/4)+1.

Thus all nine branch-offset combinations reduce to the same high-incidence hub kernel. The identity is proved; excluding the hub under full colour ownership is OPEN.

## Threshold audit

The independent three-anchor AES inequality is

2r-9 > 5(3r-1)/8
iff 16r-72 > 15r-5
iff r>67.

Therefore its exact integer threshold is r>=68, not r>=67. This controls the K>=8 route only. The alternative direct near-anchor route has a cited threshold r>=67 and bypasses this inequality; neither route currently yields an unconditional theorem.
