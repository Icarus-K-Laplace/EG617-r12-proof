# Uniform Low-Offset Closure

Status: partial structural theorem; hub exclusion remains open.

## Exact contract

Let T be the independent near-anchor triple, W its common target anti-neighbourhood, j=2r-|W|, and O'=V(F) minus (T union W). Then |W|=2r-j and |O'|=3r+j-2. The unresolved rows are delta(F)=r with j=2,3,4 and anchor degrees r+epsilon_t, or delta(F)=r+1 with j=2,...,7 and anchor degrees r+1+epsilon_t; in both rows k=sum epsilon_t<=2.

## Bounded-incidence theorem

Assume d_F(o,W)<=B for all o in O' and r>=j+4B. An independent 4-set Q in O' would have at least |W|-4B>=r common target-nonneighbours in W. They cannot form a target clique, so two are nonadjacent and Q extends to an independent 6-set. Thus alpha(F[O'])<=3 and its complement is K4-free.

If o has no target edge to T, then N_F(o,W) must cover every edge of J_W=complement of F[W]. Therefore d_F(o,W)>=tau(J_W)=|W|-alpha(J_W)>=r-j+1>B, contradiction. Hence every o in O' sees an anchor.

For each anchor t, the vertices U_t adjacent only to t form a target clique: otherwise two nonadjacent vertices of U_t and the other two anchors form a K4 in the complement of F[O']. If h_t counts t-neighbours also adjacent to another anchor, then h_t>=d_F(t)-r+2.

Let n_2,n_3 count vertices adjacent to exactly two or three anchors. Then D=n_2+2n_3=sum_t d_F(t)-|O'| and H=sum_t h_t=2n_2+3n_3<=2D.

Low branch: D=k-j+2 and H>=6+k, giving 2j<=k-2, impossible for j>=2,k<=2.
High branch: D=k-j+5 and H>=9+k, giving 2j<=k+1<=3, also impossible.

Taking B=floor((r-j)/4) proves that every surviving terminal must have max_o d_F(o,W)>=floor((r-j)/4)+1. This forced-hub conclusion is proved; excluding the hub remains open.


## Local W extremizer

The local slack identity cannot force target excess above its minimum. Let q=r-1, m=2r-j, a=ceil(m/2), b=floor(m/2). Take J_W=K_{a,b} and F[W]=K_a union K_b. Colour each cross edge (u,v) by (u+v) mod q. Each colour class is a matching; restricting the q-by-q addition table leaves at least m-q=r-j+1 edges of each colour. Thus each non-target colour on W has independence number at most r-1, while alpha(F[W])=2, omega(F[W])<=r-1, and delta_0=0. This is only a W-local example, not a complete terminal.
