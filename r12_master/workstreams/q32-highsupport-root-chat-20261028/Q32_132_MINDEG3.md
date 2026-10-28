# E408 Q32: a 132-edge nonexact color has minimum degree at least three

Date: 2026-10-28
Status: PROVED_CONDITIONAL under the registered 61-point residual contract and Kang–Pikhurko Theorems 1 and 4.

## Statement

Let D be a graph on the 61-point E408 residual with

- e(D)=132;
- alpha(D)<=12;
- omega(D)<=5.

Then

> **delta(D)>=3.**

## Extremal values

For n in {58,59,60}, the Kang–Pikhurko second-Turan values at r=11 are:

- n=58: t_11(58)=1528, p_11(58)=1524, so e(D[N])>=1653-1524=129;
- n=59: t_11(59)=1581, p_11(59)=1577, so e(D[N])>=1711-1577=134;
- n=60: t_11(60)=1635, p_11(60)=1631, so e(D[N])>=1770-1631=139.

Here N is the non-neighborhood of a hypothesized low-degree vertex, and the complement of D[N] is K12-free and non-11-partite: an 11-partition would partition N into eleven D-cliques of size at most five, covering at most55 vertices, fewer than |N|.

## Proof

Suppose x has degree d in {0,1,2}. Let S=N_D(x) and N be its non-neighborhood. Then |N|=60-d. An independent 12-set in D[N], together with x, would be an independent 13-set in D, so alpha(D[N])<=11; also omega(D[N])<=5. The preceding second-Turan bounds apply.

- If d=0, then |N|=60 and e(D[N])>=139>132, impossible.
- If d=1, then |N|=59 and e(D[N])>=134>132, impossible.
- If d=2, then |N|=58 and e(D[N])>=129. Equality e(D[N])=129 is impossible: the complement would be an extremal K12-free non-11-partite graph at (58,11), so Kang–Pikhurko Theorem 4 gives the explicit construction with eleven old parts whose sizes sum to57. Each old part is a clique in D[N], hence has size at most five, so their total size is at most55, contradiction. Therefore e(D[N])>=130.

In the degree-two case, the 130 edges inside N and the two edges incident with x exhaust all132 edges of D. There can be no further edge inside S or between S and N. But degrees zero and one have already been excluded, so each of the two neighbors of x must have another D-edge besides its edge to x. Such an edge would have to lie inside S or between S and N, contradiction.

Thus no vertex has degree at most two and delta(D)>=3. QED.

## Q32 consequence

For m=10, the unique nonexact color has132 edges. The correct nonexact pointwise degree floor is therefore

> **L_10=3**, not2.

Together with L_8=12 and L_9=7, the pointwise special-surplus budgets become r_8=3, r_9=4, r_10=4. In every non-full-support branch, the source-correct zero-shell inequality gives n_w>=2m-14+t_w, so m=10 still has n_w>=6>4. Full support v=47 also gains the stronger gadget-membership bound q_z<=4 at every residual point.

No exceptional-vertex injectivity or universal degree-nine claim is used.
