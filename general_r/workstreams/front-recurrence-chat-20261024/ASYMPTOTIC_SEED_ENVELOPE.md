# Asymptotic Seed Envelope — H+I Joint Audit

Date: 2026-10-24  
Status: **HEREDITARY MULTICOLOR TRANSFER PROVED; improved seed floors NOT PROVED.**

## 1. Required seed coordinates and cutoff package

The recurrence consumes the following edge-floor coordinates:

| Coordinate | Universal Turán floor $p_a(n)$ | r=12 certified floor | r=12 excess above $p_a(n)$ |
|---|---:|---:|---:|
| $(2,2r-1)$ | $(r-1)^2$ | 131 | 10 |
| $(3,3r-1)$ | $(r-1)(3r-2)/2$ | 210 | 23 |
| $(3,3r)$ | $3r(r-1)/2$ | 234 | 36 |
| $(4,4r-1)$ | $(r-1)(2r-1)$ | 284 | 31 |
| $(4,4r)$ | $2r(r-1)$ | 308 | 44 |

Here
$$
p_a(n)=a\binom q2+qb,\qquad n=aq+b,\quad 0\le b<a.
$$
The listed closed forms are exact for every integer $r$ in the stated coordinates. The r=12 excesses are observations from the certified recurrence inputs only; no all-r formula for those excesses is claimed.

The recurrence additionally needs cutoffs of the form $M_r(2)\le 2r-1$ and $M_r(3)\le 3r$. The contextual $a=4$ cutoff $M_r(4)\le4r$ is available only inside the reductio assuming no induced $(4r+1)$ residual. The two low-a cutoffs are not established for general $r$ by the present joint argument.

## 2. A genuine local-to-global transfer lemma

Let $X$ be an induced vertex subset of a hypothetical counterexample coloring, with $m=|X|\ge r+1$. The avoidance property is hereditary: every $(r+1)$-subset of $X$ still contains every color.

Fix a target color $c$ and put $J=G_c[X]$. Suppose $\alpha(J)\le a$. For every $v\in X$ and color $i$, define
$$
W_i(v)=X\setminus(\{v\}\cup N_i(v)),\qquad x_i(v)=|W_i(v)|=m-1-d_i(v).
$$
Then
$$
\alpha(G_i[W_i(v)])\le r-1\quad(i\ne c),
\qquad
\alpha(J[W_c(v)])\le a-1.
$$
The first statement follows by adjoining $v$ to a hypothetical color-$i$ independent $r$-set; the second follows by adjoining $v$ to a hypothetical independent $a$-set in $J$.

For $k,\ell\ge1$, define the balanced-sum floor
$$
\Pi_{k,\ell}(S)=
\min\left\{\sum_{q=1}^{\ell}p_k(y_q):
y_q\in\mathbb Z_{\ge0},\ \sum_q y_q=S\right\}.
$$
Since $\sum_i x_i(v)=(r-1)(m-1)$, for each $v$,
$$
\sum_i e_i(W_i(v))\ge
p_{a-1}(x_c(v))+
\Pi_{r-1,r-1}((r-1)(m-1)-x_c(v)).
$$
Set
$$
\Lambda_{r,a}(m)=\min_{0\le x\le m-1}
\left[p_{a-1}(x)+
\Pi_{r-1,r-1}((r-1)(m-1)-x)\right].
$$

Let $T_2,T_3$ count triangles using exactly two colors and one color, respectively. The exact identity
$$
\sum_{v\in X}\left[\binom{m-1}{2}
-\sum_i e_i(W_i(v))\right]=2T_2+3T_3
$$
therefore gives the valid induced-residual inequality
$$
\boxed{2T_2+3T_3\le
m\left[\binom{m-1}{2}-\Lambda_{r,a}(m)\right].}
\]
This is a real multicolor-to-residual transfer: it uses the edge partition and the stronger $a-1$ independence cap for the distinguished color.

## 3. Why this does not yet provide a seed floor

Let $W=\sum_{v,i}\binom{d_i(v)}2=T_2+3T_3$. For the distinguished color,
$$
\sum_v\binom{d_c(v)}2
\ge \frac{2e(J)^2}{m}-e(J).
$$
Since $W\le 2T_2+3T_3$, the transfer yields
$$
\boxed{\frac{2e(J)^2}{m}-e(J)
\le m\left[\binom{m-1}{2}-\Lambda_{r,a}(m)\right].}
$$
This is an **upper constraint** on $e(J)$, not the required improved lower floor $e(J)\ge p_a(m)+\text{excess}$.

For fixed $a\ge2$ and $m=ar+O(1)$, the degree-free relaxation has
$$
\Lambda_{r,a}(m)=\left(\frac{a(a-1)}2+o(1)\right)r^2,
$$
so the right-hand side is $(a^2/2+o(1))r^3$. At the basic Turán floor $e(J)=p_a(m)$, the distinguished-color wedge lower bound is only $(a/2+o(1))r^3$. The relaxation therefore leaves a factor-$a$ scale gap and does not force any positive excess above $p_a(m)$. A sharper degree-profile argument remains possible, but is not proved here.

## 4. Seed-envelope verdict

**Proved:** the multicolor avoidance inequality transfers to every relevant induced residual and can be strengthened using $\alpha(J)\le a$.

**Not proved:** any of the five r=12 seed excesses as an all-r lower bound; the general $M_r(2),M_r(3)$ cutoffs; or a seed envelope strong enough to close all outer budgets.

The safe universal envelope currently available from this route is only $B_r(a,n)\ge p_a(n)$, which is already part of H's recurrence and is quantitatively insufficient near $t=1$.
