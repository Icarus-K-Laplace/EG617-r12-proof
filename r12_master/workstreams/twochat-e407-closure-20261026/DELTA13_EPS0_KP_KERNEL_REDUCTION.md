# E407 Q32 — delta=13, epsilon_U=0 four-partite-U KP kernel reduction

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the frozen core/support contract and the registered Brouwer/Kang–Pikhurko equality theorem. This is a strict finite reduction, not a terminal exclusion.**

## 1. Contract

Assume

\[
\delta=13,\qquad \epsilon_U=0,
\]

and assume

\[
L_U=\overline{H[U]}
\]

is four-partite. The 49 support K4s force the standard U-part structure

\[
|U|=29=7+7+7+8.
\]

As in the registered delta=13 four-partite analysis, the three small-part pair products are completely exhausted by the 49 support blocks, so H[U] has exactly eight cross-edges, all between the 8-part D and the three 7-parts. In particular every small-part vertex has at most one H[U]-neighbor in D.

The exact W ledger gives

\[
|W|=18,
\qquad e(H[W])=48-\epsilon_U-\delta=35,
\qquad \alpha(H[W])\le4.
\]

Put

\[
J=\overline{H[W]}.
\]

Then J is K5-free and

\[
e(J)=\binom{18}{2}-35=118.
\tag{1.1}
\]

## 2. J cannot be four-partite

If J were four-partite, H[W] would be the disjoint union of at most four cliques. Because alpha(H[W])=4 under the frozen feasible-profile theorem, all four parts are nonempty. Let their sizes be

\[
1\le n_1\le n_2\le n_3\le n_4,
\qquad n_1+n_2+n_3+n_4=18.
\]

Then

\[
35=e(H[W])=\sum_{i=1}^4\binom{n_i}{2}.
\tag{2.1}
\]

There is no positive integer solution to (2.1). Equivalently, the possible values nearest 35 are

\[
32,33,34,36,37,38,40,\ldots
\]

The exhaustive arithmetic is replayed in `verify_delta13_eps0_kp_kernel.py`.

Thus

\[
\boxed{J\text{ is not four-partite}.}
\tag{2.2}
\]

## 3. Exact Brouwer equality

For n=18 and r=4,

\[
t_4(18)=121,
\qquad
 t_4(18)-\left\lfloor\frac{18}{4}\right\rfloor+1
=121-4+1=118.
\]

By (1.1) and (2.2), J is a non-four-partite K5-free graph attaining equality in the Brouwer/Kang–Pikhurko bound.

The registered Kang–Pikhurko equality classification therefore applies. It starts from a complete four-partite graph on 17 vertices with ordered part sizes

\[
(n_1,n_2,n_3,n_4),\qquad \sum n_i=17,
\]

and adds an exceptional vertex x. Lemma 5's equality conditions in the regime r<= (n-1)/2 are

\[
n_1\ge2,\qquad n_2\le n_1+1,\qquad
n_4\le n_1+2,\qquad n_4\le n_3+1.
\]

For total 17 these conditions have exactly two ordered solutions:

\[
\boxed{(3,4,5,5),\qquad (4,4,4,5).}
\tag{3.1}
\]

Let N_1,...,N_4 be the base parts, let y in N_2, and choose a nonempty proper subset A_0 subset N_1 of size a. In J the equality construction:

- contains every base cross-edge except the edges yA_0;
- joins x to N_3 union N_4 union A_0 union {y};
- does not join x to (N_1\A_0) union (N_2\{y}).

Taking complements gives an explicit H[W] kernel.

## 4. The five target kernels

### Family I: base (3,4,5,5)

Here

\[
a\in\{1,2\}.
\]

The target graph H[W] consists of the four base cliques

\[
K_3\dot\cup K_4\dot\cup K_5\dot\cup K_5,
\]

plus:

- all a cross-edges from y to A_0;
- x adjacent to N_1\A_0 and N_2\{y};
- no other cross-edges involving x.

The H[W]-degree multiset is

\[
\boxed{3^3,\ 4^{14},\ 5^1.}
\tag{4.1}
\]

For a=1 the unique degree-5 vertex is x; for a=2 it is y.

### Family II: base (4,4,4,5)

Here

\[
a\in\{1,2,3\}.
\]

Again H[W] contains the four base cliques, the yA_0 edges, and x adjacent precisely to N_1\A_0 and N_2\{y} among the first two parts.

The degree multisets are

\[
\begin{array}{c|c}
a&\text{degree multiset in }H[W]\\\hline
1&3^4,4^{13},6^1\\
2&3^4,4^{12},5^2\\
3&3^4,4^{13},6^1.
\end{array}
\tag{4.2}
\]

The degree-6 vertex is x when a=1 and y when a=3.

Thus the entire delta=13, epsilon_U=0, four-partite-U branch is reduced on the W side to exactly five explicit kernels:

\[
(3,4,5,5;a=1),\ (3,4,5,5;a=2),
\]
\[
(4,4,4,5;a=1),\ (4,4,4,5;a=2),\ (4,4,4,5;a=3).
\tag{4.3}
\]

## 5. Coupling to the 49-block W-transversal theorem

Because epsilon_U=0 and delta=13,

\[
\sum_{w\in W}y_w=\epsilon_U+2\delta-2=24,
\]

where

\[
y_w=d_H(w,U)-7.
\]

Also every W vertex has d_H(w,U)>=7. Since

\[
d_H(w,U)=12+\epsilon_w-d_{H[W]}(w),
\]

we have

\[
\boxed{y_w=5+\epsilon_w-d_{H[W]}(w).}
\tag{5.1}
\]

All four units of core excess lie in W:

\[
\sum_{w\in W}\epsilon_w=4.
\tag{5.2}
\]

For the Family-II kernels with a=1 or a=3, the unique degree-6 vertex z must satisfy

\[
7\le d_H(z,U)=6+\epsilon_z,
\]

so

\[
\boxed{\epsilon_z\ge1.}
\tag{5.3}
\]

Hence those two kernels consume at least one of the four excess units at a prescribed exceptional vertex.

No stronger excess localization follows from the W-transversal degree floor alone for the other three kernels.

## 6. Dependency audit

This reduction uses:

1. the pure E407 core/support ledger and alpha(H[W])=4;
2. the delta=13 four-partite-U support-block transversal structure;
3. Brouwer's non-four-partite Turan bound at (n,r)=(18,4);
4. Kang–Pikhurko's equality classification and Lemma 5.

It does not use the Didin 2026 preprint, the delta=14 saturated branch, or any shell template A-E assumption.

The five-kernel enumeration and degree multisets are independently replayed by `verify_delta13_eps0_kp_kernel.py`. The verifier does not verify the external Kang–Pikhurko theorem.

## 7. Remaining terminal obligation

The formerly unclassified delta=13, epsilon_U=0, four-partite-U branch is no longer an arbitrary W-graph problem. It is enough to exclude the five kernels (4.3) against:

- the exact U degrees determined by the 7,7,7,8 support design and its eight D-to-small H[U] cross-edges;
- the four-unit W excess allocation;
- every W vertex hitting all 49 support blocks;
- the nonadjacent-pair common-U-neighbour inequality;
- the labelled shell/support constraints from the current five-template workstream.

No claim of terminal exclusion is made in this note.