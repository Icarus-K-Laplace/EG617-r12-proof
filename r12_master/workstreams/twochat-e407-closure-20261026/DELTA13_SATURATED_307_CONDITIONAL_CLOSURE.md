# E407 Q32 — delta=13 non-four-partite 307-edge K5-saturated fork

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL / EXCLUDED**, conditional on the same Didin 2026 independence-number Turan theorem and Brouwer second-Turan theorem already registered for the delta=14 saturated reduction. The Didin dependency remains unaudited. E407 Q32 remains OPEN.

## 1. Contract

Work in the delta=13 non-four-partite fork in which

\[
L:=L_U=\overline{H[U]}
\]

is already K5-saturated. Then

\[
|U|=29,\qquad e(L)=307,
\]

and with

\[
G:=H[U]=\overline L
\]

we have

\[
|V(G)|=29,\qquad e(G)=\binom{29}{2}-307=99,
\qquad \alpha(G)=4.
\]

The 49 selected support blocks are 49 pairwise edge-disjoint K4s in L, partitioned into seven classes of seven vertex-disjoint K4s.

Because L is K5-saturated, every edge uv of G is alpha-critical: adding uv to L creates a K5, so deleting uv from G creates an independent 5-set. Hence

\[
\alpha(G-uv)=5\quad\text{for every }uv\in E(G).
\]

Thus G is alpha-critical.

## 2. Component count under the registered Didin theorem

Use the same external theorem as in `DELTA14_SATURATED_ALPHA_CRITICAL_REDUCTION.md`:
if an alpha-critical graph on n vertices with independence number alpha has p connected components, put s=alpha-p; then

\[
e(G)\ge t(n+s,\alpha)-s,
\]

where t(N,alpha) denotes the minimum edge count of a graph on N vertices with independence number at most alpha, equivalently the balanced union of alpha cliques.

Here alpha=4.

- p=4 is impossible: every component then has independence number one, hence is a clique, so L is complete four-partite, contrary to the non-four-partite contract.
- p=1 gives
  \[
  e(G)\ge t(32,4)-3=109>99.
  \]
- p=2 gives
  \[
  e(G)\ge t(31,4)-2=103>99.
  \]

Therefore

\[
\boxed{p=3.}
\]

The component independence numbers are necessarily 1,1,2. Write

\[
G=K_a\dot\cup K_b\dot\cup C,
\qquad a+b+c=29,
\]

where C is connected, alpha(C)=2, and C is alpha-critical.

Let

\[
J:=\overline C=L[V(C)].
\]

Then J is triangle-free, non-bipartite, and triangle-saturated. By Brouwer's second-Turan theorem,

\[
e(J)\le \left\lfloor\frac{c^2}{4}\right\rfloor
-\left\lfloor\frac c2\right\rfloor+1,
\]

which is equivalent to the convenient lower bound

\[
\boxed{e(C)\ge \left\lfloor\frac{c^2}{4}\right\rfloor-1.}
\tag{2.1}
\]

## 3. The 49 support K4s force two capacities

Since L is the complete join of independent sets of sizes a,b and the triangle-free graph J, every K4 in L contains exactly

- one vertex from K_a,
- one vertex from K_b,
- two vertices forming an edge of J.

The 49 selected K4s are pairwise edge-disjoint. Therefore their A-B edges are all distinct and their J-edges are all distinct:

\[
\boxed{ab\ge49,\qquad e(J)\ge49.}
\tag{3.1}
\]

The exact edge identities are

\[
e(C)=99-\binom a2-\binom b2,
\qquad
e(J)=\binom c2-e(C).
\tag{3.2}
\]

Consequently any surviving integer kernel must satisfy

\[
\begin{gathered}
a+b+c=29,\qquad 1\le a\le b,\qquad c\ge5,\\
ab\ge49,\qquad e(J)\ge49,\\
e(C)=99-\binom a2-\binom b2,\\
e(C)\ge\left\lfloor c^2/4\right\rfloor-1.
\end{gathered}
\tag{3.3}
\]

## 4. Exact arithmetic terminal: no tuple exists

The finite replay in `verify_delta13_saturated_307.py` enumerates every integer triple satisfying the size/order constraints and checks (3.3). The survivor list is empty.

For comparison, replacing 99 by 98 is exactly the old delta=14 saturated arithmetic and has the unique tuple

\[
(a,b,c,e(C),e(J))=(7,7,15,56,49).
\]

The single additional target edge in the present 307-edge-L fork destroys that equality kernel: there is no corresponding 99-edge alpha-critical component decomposition compatible with the 49 support K4s and Brouwer bound.

Hence

\[
\boxed{\delta=13,\ L_U\text{ non-four-partite and already K5-saturated }\Longrightarrow\bot}
\]

**under the registered Didin+Brouwer external-theorem contract.**

## 5. Firewall and remaining branch

This is not promoted to an unconditional closure because the proof of the Didin 2026 preprint theorem has not been independently audited in this project.

After the unconditional two-step augmentation closure and this conditional 307-saturated closure, the only delta=13 non-four-partite fork still requiring a direct terminal proof is:

> there exists exactly one K5-safe augmentation edge e, and `L_U+e` is a non-four-partite 308-edge K5-saturated graph.

That branch is treated separately in `DELTA13_ONE_STEP_SATURATED_REDUCTION.md`.
