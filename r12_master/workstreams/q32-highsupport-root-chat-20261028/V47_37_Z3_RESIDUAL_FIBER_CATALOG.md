# E408 Q32 — exact z=3 residual/fiber catalog in the 3+7 split

Date: 2026-10-29  
Status: **PROVED_CONDITIONAL local structural reduction.** This does not close the 3+7 cell or full-support Q32.

## 1. Contract

Work in the full-support \(m=10\), disconnected \(3+7\) light-block cell. The registered ledger gives
\[
x_T=3+z,\qquad y=8-2z,\qquad e(H[R])=3+z,\qquad
d_{H[R]}(r)+b_r=2,
\]
where \(b_r=\sum_i(|N(r)\cap Q_i|-1)\), \(\sum_r b_r=y\), and \(\Delta(H[R])\le2\). The residual small-block map \(F=(F_0,F_1,F_2,F_3)\) and the outer-track assignment \(G=(G_0,G_1,G_2,G_3)\) both partition \(R\) into cliques, with sorted fiber sizes in
\[
\mathcal P=\{(3,3,1,0),(3,2,2,0),(3,2,1,1),(2,2,2,1)\}.
\]
The two partitions are **not assumed equal**.

For \(z=3\), \(e(H[R])=6\) and \(y=2\). Hence
\[
\sum_{r\in R}(2-d_R(r))=14-2e(H[R])=2.
\]
Thus either one residual vertex has degree \(0\) and the other six have degree \(2\), or exactly two residual vertices have degree \(1\) and the other five have degree \(2\).

## 2. Exact residual graph types

Because \(|R|=7\), \(\Delta(H[R])\le2\), \(\alpha(H[R])\le4\), and the clique-cover number is at most four, the residual graph is one of exactly six disjoint unions of paths/cycles:
\[
C_6\dot\cup K_1,\quad 2C_3\dot\cup K_1,\quad
P_7,\quad C_3\dot\cup P_4,\quad C_4\dot\cup P_3,\quad C_5\dot\cup P_2.
\]
The companion pure-Python verifier independently enumerates all component multisets satisfying the numeric constraints and recovers exactly this list.

## 3. Exact compatibility of either clique partition with the residual graph

The table gives every sorted fiber profile compatible with each graph type. “Compatible” means every fiber is a clique; no alignment between \(F\) and \(G\) is presumed.

| \(H[R]\) type | Compatible profile(s) | Number of labelled 4-bin partitions checked |
|---|---|---:|
| \(2C_3\dot\cup K_1\) | \((3,3,1,0)\), \((3,2,1,1)\) | 168 |
| \(C_6\dot\cup K_1\) | \((2,2,2,1)\) | 48 |
| \(C_5\dot\cup P_2\) | \((2,2,2,1)\) | 120 |
| \(C_4\dot\cup P_3\) | \((2,2,2,1)\) | 96 |
| \(C_3\dot\cup P_4\) | \((3,2,2,0)\), \((3,2,1,1)\), \((2,2,2,1)\) | 168 |
| \(P_7\) | \((2,2,2,1)\) | 96 |

These counts include permutations of the four labels and are regression counts, not counts of non-isomorphic configurations.

The number of edges internal to the four fibers is respectively \(6,5,4,3\) for profiles \((3,3,1,0),(3,2,2,0),(3,2,1,1),(2,2,2,1)\). Since \(e(H[R])=6\), the required number of edges between distinct fibers is exactly \(0,1,2,3\).

## 4. Double-track vertices: a global and a small-fiber filter

A double-track outer vertex \(q\) has no residual neighbors. Therefore the global outer-track fiber \(G_g\) containing \(q\) must be empty: if \(G_g\) contained any \(r\), then by definition \(r\) is adjacent to all seven vertices of track \(T_g\), including \(q\).

Consequently, if any double-track vertex exists, the **global** track profile must be \((3,3,1,0)\) or \((3,2,2,0)\). By Section 3 this forces
- \(H[R]=2C_3\dot\cup K_1\) when the global profile is \((3,3,1,0)\); or
- \(H[R]=C_3\dot\cup P_4\) when the global profile is \((3,2,2,0)\).

In particular, no double-track vertex is possible for residual types \(C_6\dot\cup K_1\), \(P_7\), \(C_4\dot\cup P_3\), or \(C_5\dot\cup P_2\). For type \(C_3\dot\cup P_4\), double-track vertices require the global profile \((3,2,2,0)\); for type \(2C_3\dot\cup K_1\), they require global profile \((3,3,1,0)\).

Separately, if a double-track vertex has common small-block labels \(h,j\), the established double-track lemma forces
\[
n_h+n_j\le3,\qquad F_h\text{ is completely joined to }F_j.
\]
The exact \(z=3\) compatibility enumeration gives the only small-map profile/pair-size possibilities:

| Small-map profile \(F\) | Possible pair sizes \((n_h,n_j)\) for a double-track vertex | Residual type if the pair is present |
|---|---|---|
| \((3,3,1,0)\) | \((3,0)\), \((1,0)\) | \(2C_3\dot\cup K_1\) |
| \((3,2,2,0)\) | \((3,0)\), \((2,0)\) | \(C_3\dot\cup P_4\) |
| \((3,2,1,1)\) | \((2,1)\), \((1,1)\) | \((2,1)\): \(2C_3\dot\cup K_1\); \((1,1)\): \(C_3\dot\cup P_4\) |
| \((2,2,2,1)\) | \((2,1)\) | \(C_3\dot\cup P_4\) |

This table is a compatibility filter only. It does not assert that the listed double-track configurations extend to all seven outer blocks.

## 5. Switch-block budget and remaining target

For a switch block whose common-track labels duplicate a fiber \(F_h\), the two singleton-track vertices both meet every point of \(F_h\). Hence the block's residual incidence excess is at least \(n_h\). Since \(\sum_i y_i=2\), a switch cannot duplicate a size-three fiber; a size-two duplicated fiber can occur in at most one block, and size-one duplicates consume the total budget at unit cost.

The immediate remaining task is to couple this exact residual/fiber catalog to the seven blockwise source-label patterns, the at-most-two units of residual incidence excess, and the outer heavy-pair graph of total weight six. The catalog narrows the z=3 case but is **not** a contradiction or a Q32 closure.
