# R12 shell-to-core maximum-independent-set witness lemma

Date: 2026-10-24  
Status: **PROVED under the retained T61 contextual contract.**  
Scope: T61 residuals only; this does not eliminate E407 Q32 or E408 Q32/Q33.

## 1. Frozen contract

Let F be a 61-vertex T61 residual with

- alpha(F) <= 5, omega(F) <= 11;
- a legal degree-13 pivot p;
- shell A=N_F(p), |A|=13;
- core H=V(F)\(A union {p}), |H|=47;
- alpha(H) <= 4, omega(H) <= 11;
- every 49-vertex subset of F has independence number at least5 (the contextual no-R(4,49) contract).

For a in A, put

N_H(a)=N_F(a) intersect H, t_a=|N_H(a)|, and H_a=H\N_H(a).

Call a shell vertex **good** if alpha(H_a)=4, and **bad** otherwise. Since alpha(H)<=4, bad means alpha(H_a)<=3.

The hereditary target-edge cap on every induced n-vertex subset J of F is

e_F(J) <= D(n):=binom(n,2)-11 p_12(n),

where p_k(n) is the Turan minimum-edge count for independence number at most k. This follows because each of the eleven non-target color graphs has independence number at most12 and therefore at least p_12(n) edges on J.

## 2. Small-row lemma: t_a<=7 implies a is good

**Claim.** If t_a<=7, then alpha(H_a)=4.

**Proof.** Suppose instead alpha(H_a)<=3. Set n=|H_a|=47-t_a, so 40<=n<=47. The graph J=H_a has omega(J)<=11 and alpha(J)<=3. Its complement is K4-free and cannot be 3-partite: a 3-partite graph on n>=40 vertices has an independent part of size at least ceil(n/3)>=14, whereas alpha(bar J)=omega(J)<=11.

Brouwer's second-Turan bound therefore gives

e(J) >= p_3(n)+floor(n/3)-1.

The exact values on the only possible range are:

| n | lower bound p_3(n)+floor(n/3)-1 | cap D(n) |
|---:|---:|---:|
| 40 | 259 | 252 |
| 41 | 272 | 259 |
| 42 | 286 | 267 |
| 43 | 300 | 276 |
| 44 | 314 | 286 |
| 45 | 329 | 297 |
| 46 | 344 | 309 |
| 47 | 359 | 322 |

In every row the lower bound exceeds the hereditary cap, contradiction. Thus alpha(H_a) is not at most3; because alpha(H_a)<=alpha(H)<=4, it equals4. ∎

## 3. Pair-extension lemma: at least eight shell vertices are good

**Claim.** If ab is a target edge of F[A], then at least one of a,b is good. Consequently the bad vertices form an independent set in F[A], so there are at most five bad vertices and at least eight good vertices.

**Proof.** The 49-set H union {a,b} has independence number at least5 by the contextual no-R(4,49) contract. Since alpha(H)<=4 and ab is an edge, an independent 5-set cannot use both a and b. It must consist of one endpoint, say a, and four vertices of H anticomplete to a, or symmetrically b and four vertices anticomplete to b. Thus at least one endpoint has alpha(H_a)=4. Two bad vertices therefore cannot be adjacent in F[A]. Since alpha(F[A])<=alpha(F)<=5, at most five shell vertices are bad. ∎

This is a shell/core constraint, not a claim that every row is good. Rows with t_a>=8 may still be bad.

## 4. Consequence for the retained E408 Q33/d3 interface

Assume the exact Q33/d3 contract:

- A=S dot_union B, |S|=3, |B|=10;
- M=bar(F[A]), M[B] is empty;
- q=e(M)+G_A=33;
- the exact budget is beta+X+G_B=3;
- for each b in B, k_b=d_M(b)<=3 and t_b=k_b+g_b, with G_B=sum over b in B of g_b.

Then G_B<=3, so every b in B satisfies

t_b=k_b+g_b<=3+3=6<=7.

By the small-row lemma, **all ten B-vertices are good**, not merely the regular B-vertices.

For each b in B, choose an independent 4-set Q_b subset H_b. If ab is a missing target edge (ab in E(M)) with a in S, then Q_b must intersect N_H(a): otherwise Q_b union {a,b} would be an independent 6-set in F. Therefore

> Q_b hits every core row N_H(a) for a in N_M(b) intersect S.

The exact Q33 budget also gives sum over b in B of k_b=c_S>=22-beta. Since each k_b<=3, at least ceil((12-beta)/2) vertices of B have k_b>=2. In particular, **at least five B-vertices have a maximum independent 4-set in H that hits at least two of the three support rows**; in the beta=0,1 cases, at least six do.

## 5. What this does not prove

The lemma does not force two selected witness sets Q_b to coincide, nor does it establish that their row intersections are incompatible with the 284-edge core. The next genuine gap is a **witness-capacity theorem**: determine whether a 47-vertex core with excess4 can support ten independent 4-set witnesses satisfying these prescribed row-hit patterns and the seven-block color constraints.

No E407/E408 terminal contract is closed by this lemma alone.
