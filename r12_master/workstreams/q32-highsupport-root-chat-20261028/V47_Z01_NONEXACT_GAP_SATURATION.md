# E408 Q32 — exact nonexact-gap saturation in the aligned z=0,1 cell

Date: 2026-10-29  
Status: **PROVED conditional structural theorem; not a full Q32 closure.**

## 1. Contract

Work in the aligned m=10, z in {0,1}, residual-fiber profile (2,2,2,1) established by V47_Z01_TRACK_ALIGNMENT.md. The target core H is partitioned into target-color cliques
\[
T_1,T_2,T_3\cong K_{12},\qquad T_0\cong K_{11},
\]
and O={p} union A has 14 vertices, with every pA edge target-colored.

Let D be the unique 132-edge nonexact color and write
\[
g_C=e_C(H)-69,\qquad g_D=e_D(H)-69.
\]
The balanced-coloring contract gives alpha(D)<=12. The source-mode audit for this aligned cell gives g_C<=3 for every exact Type-I color: the x in O case has only y-A0 gadget edges inside H, at most three; the two-double source modes have at most six gadget H-edges above the 66-edge K5-interior layer; the triple source mode must be a special factor and has at most five gadget H-edges above the 67-edge interior layer. A triple isolated factor and the two-isolated-double/single-special configuration are excluded by the target-track same-track edge prohibition. The isolated-double source cases are separately audited in V47_Z01_ISOLATED_DOUBLE_RESIDUAL_AUDIT.md.

The exact all-color core-gap identity is
\[
\sum_{C=1}^{11}g_C=37.
\]

## 2. At least 56 edges of D lie outside H

### 2.1 Three large-track contributions

For every o in O and i in {1,2,3}, the set T_i union {o} has 13 vertices. Since T_i is a target-color clique, the color D must occur on at least one edge from o to T_i. These are 14*3=42 distinct edges outside H.

### 2.2 A further 14-edge lower bound

Let
\[
Z=\{o\in O:d_D(o,T_0)=0\},\qquad k=|Z|.
\]
For any two distinct u,v in Z, if uv is not a D-edge, then T_0 union {u,v} is a D-independent 13-set. Therefore Z is a clique in D[O]. Since p has no D-edge to any vertex of A, if p is in Z then Z={p}.

Also D[A] has at least two edges: otherwise D[A] has a vertex cover of size at most one, so alpha(D[A])>=12; adjoining p, which has no D-edge to A, gives a D-independent 13-set. Hence e_D(A)>=2.

If p is in Z, then all 13 vertices of A have a D-neighbor in T_0, so
\[
e_D(O,T_0)+e_D(A)\ge13+2=15.
\]

Otherwise Z is a subset of A. Every o in O\Z has at least one D-edge to T_0, so
\[
e_D(O,T_0)\ge14-k.
\]
Since Z is a clique in D[A],
\[
e_D(A)\ge\max\{2,\binom{k}{2}\}.
\]
The exact lower bound is therefore
\[
e_D(O,T_0)+e_D(A)\ge14-k+\max\{2,\binom{k}{2}\}\ge14.
\]
Equality occurs only at k=2 or k=3.

Combining the disjoint edge classes gives
\[
e_D(K_{61}\setminus E(H))\ge42+14=56.
\]
As e(D)=132 and e_D(H)=69+g_D,
\[
63-g_D=132-(69+g_D)\ge56,
\]
so
\[
\boxed{g_D\le7.}
\]

## 3. The core-gap budget forces equality

Every exact color has g_C<=3, hence
\[
g_D=37-\sum_{C\text{ exact}}g_C\ge37-10*3=7.
\]
Together with Section 2 this gives
\[
\boxed{g_D=7,\qquad g_C=3\text{ for all ten exact colors}.}
\]
Thus the aligned z=0,1 branch has no low-gap exact colors: every exact color is at its source-correct three-unit cap, and the nonexact color is at its seven-unit core gap.

## 4. Equality characterization

Every inequality in Section 2 must be tight.

1. For every o in O and i in {1,2,3}, there is exactly one D-edge from o to T_i.
2. p is not in Z, and Z is a subset of A with size k=2 or k=3.
3. Every o in O\Z has exactly one D-edge to T_0, while each o in Z has none. In particular d_D(p,T_0)=1.
4. If k=2, then D[A] has exactly two edges: the edge on Z, plus one edge disjoint from it. The disjointness follows because two adjacent edges alone would give a vertex cover of size one in D[A], contradicting alpha(D[A])<=11.
5. If k=3, then Z is a triangle and D[A] consists exactly of that triangle.

Equivalently, the outside structure of D has only two possible forms:
- D[A] is 2K2, with two endpoints Z having no D-neighbor in T_0, and 12 D-edges from O to T_0;
- D[A] is K3, with its three vertices Z having no D-neighbor in T_0, and 11 D-edges from O to T_0.

The companion arithmetic checker enumerates all k=0,...,13 and the separate p in Z case, and verifies that the only equality cases are k=2,3.

## 5. Scope

This theorem closes no graph branch by itself. It sharply reduces the aligned m=10,z=0,1,(2,2,2,1) branch to the all-exact-gap-three regime and the two outside patterns above. It does not apply to the other m=10 light-block components, nor to m=8,9. E408/Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
