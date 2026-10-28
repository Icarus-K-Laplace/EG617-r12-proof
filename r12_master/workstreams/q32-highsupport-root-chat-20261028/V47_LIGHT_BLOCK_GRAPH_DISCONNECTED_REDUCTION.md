# E408 Q32 full support — disconnected light-block graph reduction (m=10)

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL structural reduction; no full-support closure claimed.**

## 1. Setup

Use the pivot-neighborhood blocks (Q_1,\ldots,Q_{10}), each an independent 4-set in H, and the residual (R), (|R|=7). For each pair of blocks write
[
k_{ij}=e_H(Q_i,Q_j)-4\ge0.
]
The lower bound 4 is the registered pivot-packing lemma. Call (ij) **light** if (k_{ij}=0), and **heavy** if (k_{ij}\ge1). Let (L) be the graph on the ten block labels whose edges are the light pairs.

For each block define
[
t_i=\sum_{j\ne i}k_{ij},\qquad
y_i=\sum_{r\in R}(|N_H(r)\cap Q_i|-1).
]
Then (x=\sum_{i<j}k_{ij}), (y=\sum_i y_i), and
[
\sum_i t_i=2x,\qquad \sum_i y_i=y.
]

Each vertex in (Q_i) has at least one H-neighbor in every other block, and the block has (7+y_i) edges to R. Thus
[
\sum_{q\in Q_i}d_H(q)=36+t_i+7+y_i=43+t_i+y_i.
]
Since every (q\in Q_i) has degree at least12, put
[
s_i=t_i+y_i-5=\sum_{q\in Q_i}(d_H(q)-12)\ge0.
]
The six-unit excess ledger gives
[
\sum_i s_i=2x+y-50\le6,
\qquad
(y+2z-8)+(2x+y-50)=6.
]
In particular (s_Q:=\sum_i s_i=14-y-2z\le6), while (s_R=y+2z-8\ge0).

## 2. Component lower bound

Let S be a connected component of L with (k\le5) vertices. Every pair between S and its complement T is heavy, so each (i\in S) has at least (10-k) units in (t_i). Hence
[
s_i=t_i+y_i-5\ge5-k+y_i,
]
and
[
\boxed{s_Q\ge k(5-k)+Y_S},\qquad Y_S=\sum_{i\in S}y_i.
	ag{2.1}
]

If L had at least three connected components, at least two components would have size at most4. Their lower bounds in (2.1) sum to at least (4+4=8), contradicting (s_Q\le6). Therefore **L has exactly two components**. Their sizes must be one of
[
\boxed{1+9,\quad2+8,\quad3+7,\quad4+6,\quad5+5.}
]

The following refinements are all necessary conditions.

## 3. Component sizes 1+9

For the singleton component S, its sole block has nine heavy partners, so (t_i\ge9) and
[
s_i=t_i+y_i-5\ge4.
]
Therefore (s_Q\ge4), (s_R\le2), and
[
y+2z\le10,qquad z\le5.
]
Moreover (s_i\le6) implies
[
(t_i-9)+y_i\le2.
]
So among the nine cross pairs, the total heavy-edge multiplicity beyond the mandatory one extra edge per pair is at most two; the singleton block has (y_i\le2).

## 4. Component sizes 2+8

Here (2.1) forces (s_Q=6) and (s_R=0). The two-vertex component is a light edge. Both of its blocks have (y_i=0), (s_i=3), and (t_i=8). Thus each of their eight cross pairs is heavy with **exactly one** extra edge, i.e. exactly five H-edges.

Every block in the eight-vertex component has (s_j=0), so its internal heavy-pair weight (t_j^{T}) satisfies
[
t_j^{T}+y_j=3.
]
Let (x_T) be the total (k_{ij})-weight over heavy pairs wholly inside T. Counting the 16 cross pairs and using (x+y+z=32) gives
[
x=16+x_T,qquad 2x_T+y=24,
]
hence
[
\boxed{x_T=8+z,\quad y=8-2z,\quad z\le4.}
]
Each block in T has weighted internal heavy degree at most3, so its degree in (L[T]) is at least4.

## 5. Component sizes 3+7

Now (s_Q=6), (s_R=0). The three-vertex component must be a **light triangle**: a path would create at least one internal heavy pair and exceed the entire six-unit budget. Its three blocks have (y_i=0), (s_i=2), and each cross pair to T is heavy with exactly one extra edge.

Each block (j\in T) satisfies
[
t_j^{T}+y_j=2.
]
Counting the 21 cross pairs gives
[
x=21+x_T,qquad 2x_T+y=14,
]
so
[
\boxed{x_T=3+z,\quad y=8-2z,\quad z\le4.}
]
Every block in T has weighted internal heavy degree at most2, and therefore degree at least4 in (L[T]).

In both the 2+8 and 3+7 cases,
[
s_R=0\implies d_{H[R]}(r)+b_r=2
]
for every (r\in R), where (b_r=\sum_i(|N_H(r)\cap Q_i|-1)). Hence (Delta(H[R])\le2), and (H[R]) is a disjoint union of paths, cycles and isolated vertices.

## 6. Component sizes 4+6

Equation (2.1) gives (s_Q\ge4), hence (s_R\le2) and
[
\boxed{y+2z\le10,\quad z\le5.}
]
Let (x_S) be the sum of (k_{ij}) over heavy pairs internal to S, and let (delta_{ST}=\sum_{i\in S,j\in T}(k_{ij}-1)) be the extra multiplicity beyond one on cross pairs. The 24 cross pairs are all heavy, and
[
s_S=4+2x_S+\delta_{ST}+Y_S\le6.
]
Therefore
[
\boxed{2x_S+\delta_{ST}+Y_S\le2.}
]
In particular, S has at most one unit of internal heavy-pair weight; its light graph is either (K_4) or (K_4) minus one edge. Across the 24 cross pairs, at most two extra multiplicity units are allowed beyond the mandatory one per pair.

## 7. Component sizes 5+5

There are 25 heavy cross pairs, so (x\ge25). Combining with (x+y+z=32) and (y+2z\ge8) gives
[
\boxed{y+z\le7,\quad z\ge1.}
]
Let (delta_{ST}) denote cross-pair multiplicity beyond one, and (x_S,x_T) the weighted heavy-pair sums internal to the two components. Then
[
x=25+\delta_{ST}+x_S+x_T,
]
and the six-unit budget yields
[
\boxed{2(\delta_{ST}+x_S+x_T)+y\le6.}
]
Thus there are at most three total heavy-edge multiplicity units beyond the 25 mandatory cross-pair units, and (y\le6).

## 8. Next mathematical target

The most rigid disconnected cases are 2+8 and 3+7: they spend the entire Q-excess budget, force (s_R=0), force all cross pairs to have exactly five edges, and reduce (H[R]) to a seven-vertex maximum-degree-two graph. The next step is to couple those path/cycle residual types to the unique-matching and independent-set-cover constraints across the pivot blocks.

This reduction does not close any full-support Q32 branch. The scalar slack relaxation remains feasible and is not treated as an UNSAT certificate.
