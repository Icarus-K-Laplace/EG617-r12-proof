# Multicolor-to-Seed Interface — H+I Joint Audit

Date: 2026-10-24  
Status: **HEREDITARY TRANSFER LEMMA PROVED; TRANSFER TO A STRONGER SEED FLOOR OPEN.**

## 1. The induced-residual issue is resolvable

The original counterexample property says that every $(r+1)$-vertex subset contains every color. This property is hereditary under vertex restriction. Therefore it remains true on every induced residual $X$ with $m=|X|\ge r+1$; no claim is being transferred from the whole graph to a non-induced object.

Fix a color $c$, put $J=G_c[X]$, and suppose $\alpha(J)\le a$. For each $v\in X$ and each color $i$, define
`W_i(v)=X\setminus(\{v\}\cup N_i(v))` and `x_i(v)=m-1-d_i(v)`.

Then:
- for $i\ne c$, $\alpha(G_i[W_i(v)])\le r-1$;
- for $i=c$, $\alpha(J[W_c(v)])\le a-1$.

Both statements follow by adjoining $v$ to a forbidden independent set. Thus the target-color improvement is legitimate on the induced residual itself.

## 2. Exact transfer inequality

Let $p_k(s)$ be the minimum edge count in an $s$-vertex graph with independence number at most $k$. For $k,\ell\ge1$, define
[
\Pi_{k,\ell}(S)=\min_{y_1+\cdots+y_\ell=S,\ y_q\in\mathbb Z_{\ge0}}
\sum_{q=1}^{\ell}p_k(y_q).
]
Since $\sum_i x_i(v)=(r-1)(m-1)$, set
[
\Lambda_{r,a}(m)=\min_{0\le x\le m-1}
\left[p_{a-1}(x)+
\Pi_{r-1,r-1}((r-1)(m-1)-x)\right].
]
For triangle counts $T_2,T_3$ on $X$ (exactly two colors and monochromatic, respectively), the exact identity
[
\sum_{v\in X}\left[\binom{m-1}{2}-\sum_i e_i(W_i(v))\right]
=2T_2+3T_3
]
and the local Turán floors imply
[
\boxed{2T_2+3T_3\le
m\left[\binom{m-1}{2}-\Lambda_{r,a}(m)\right].}
]
This is a genuine multicolor-to-induced-residual theorem: it uses the edge partition, the inherited $(r+1)$-set property, and the stronger target-color independence cap $a$.

Also, with $W=\sum_{v,i}\binom{d_i(v)}2=T_2+3T_3$, Jensen gives
[
\frac{2e(J)^2}{m}-e(J)\le
m\left[\binom{m-1}{2}-\Lambda_{r,a}(m)\right].
]
The inequality is a consistency/upper-envelope constraint on $e(J)$, not an improved lower floor.

## 3. Why the five seed coordinates are not closed

The universal Turán floors are:
- $p_2(2r-1)=(r-1)^2$;
- $p_3(3r-1)=(r-1)(3r-2)/2$;
- $p_3(3r)=3r(r-1)/2$;
- $p_4(4r-1)=(r-1)(2r-1)$;
- $p_4(4r)=2r(r-1)$.

At $r=12$, the certified floors are respectively $131,210,234,284,308$, which exceed these baselines by $10,23,36,31,44$. The transfer inequality does not prove these excesses for general $r$.

For fixed $a\ge2$ and $m=ar+O(1)$, the degree-free relaxation has
[
\Lambda_{r,a}(m)=\left(\frac{a(a-1)}2+o(1)\right)r^2.
]
Consequently its right-hand side is $(a^2/2+o(1))r^3$, whereas the target-color wedge lower bound at $e(J)=p_a(m)$ is only $(a/2+o(1))r^3$. The resulting factor-$a$ scale gap means this relaxation cannot force a positive excess over $p_a(m)$.

A degree-profile refinement of the transfer inequality is still mathematically possible. It has not yet yielded an all-r lower floor, and the inequality's present direction must not be reversed.

## 4. Joint verdict

1. **Valid transfer lemma? Yes.** It applies to every relevant induced residual, with all quantifiers explicit.
2. **Five improved general-r seed floors? No.** Only the universal $p_a(n)$ floors are proved by this route.
3. **All nonterminal outer states eliminated? No.**
4. **Explicit $r_0$? No.**
5. **Unique blocker:** convert the transferred triangle/moment constraint into a lower bound using the target graph's simultaneous $\alpha\le a$, $\omega\le r-1$, and inherited caps; the current degree-free inequality is not directionally strong enough.
6. The transfer genuinely uses the multicolor edge partition, but that fact alone does not make it a seed-floor theorem.
