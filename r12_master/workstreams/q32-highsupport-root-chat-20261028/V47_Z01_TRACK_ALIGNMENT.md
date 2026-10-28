# E408 Q32 full support — z=0,1 small/outer track alignment

Date: 2026-10-28  
Status: **PROVED_CONDITIONAL structural theorem; does not close Q32.**

## 1. Contract

Work in the m=10, disconnected 3+7 cell. Let A,B,C be the small light triangle, T the seven outer blocks, and R the seven residual vertices. The registered identities are
`e(H[R])=3+z`, `y=8-2z`, `sum_D y_D=y`, and `d_R(r)+b_r=2`.

The common zero-slack map on A,B,C partitions R into four nonempty clique fibers `F_1,...,F_4`, with `n_s=|F_s|`. The globally aligned outer K7 tracks from `V47_37_OUTER_LIGHT_HOLONOMY.md` partition R into clique fibers `G_1,...,G_4`, with `m_g=|G_g|). Every outer vertex q in track g is adjacent to all of `G_g`; if q has singleton common-track label s across A,B,C, the singleton-track blocker also forces q adjacent to all of `F_s`.

For z=0,1, the residual-type/independence-number audit gives `alpha(H[R])=4`, so no double-track outer vertex can exist. Each outer block is therefore either aligned (its four common labels form a permutation) or a synchronized switch (one common label is duplicated and one label is missing).

## 2. Per-block fiber-mismatch inequality

For an outer block D, define
[
\eta_D=\sum_{q\in D}|F_{s(q)}\setminus G_{g(q)}|,
]
where s(q) is q's singleton common label and g(q) its globally aligned outer-track label.

For each q,
`d_R(q) >= |G_{g(q)} union F_{s(q)}| = |G_{g(q)}| + |F_{s(q)} minus G_{g(q)}|`.
The four q vertices of D occupy the four distinct outer tracks, so `sum_{q in D}|G_{g(q)}|=|R|=7`. On the other hand, the definition of y_D gives `sum_{q in D} d_R(q)=7+y_D`. Therefore
[
\boxed{y_D\ge\eta_D.}
	ag{2.1}
]

This is an exact incidence-slack inequality; it does not assume that the small and outer track partitions already agree.

## 3. z=0: the partitions coincide

Here `e(H[R])=3`. Each small-map fiber is a clique and the four fiber sizes sum to seven, so the only possible profile is `(2,2,2,1)`. Its three size-two fibers already account for all three edges of H[R]. Thus H[R] is exactly `3K_2 dot-union K_1`.

Every outer-map fiber is also a clique. Since H[R] has no triangles and exactly three edges, any partition into four clique fibers must use those same three edges and the remaining singleton. Consequently the two unlabelled partitions `{F_s}` and `{G_g}` coincide.

## 4. z=1: the partitions coincide by the seven-block slack budget

Here `e(H[R])=4). The small-map fiber profile is either `(3,2,1,1)` or `(2,2,2,1)`; in either case all four fibers are nonempty. The outer-map fibers are also all nonempty: a size profile `(3,3,1,0)` or `(3,2,2,0)` would already require at least six or five internal clique edges, respectively, exceeding `e(H[R])=4`.

Suppose the two unlabelled clique partitions differ. For any outer block D:
- If D is aligned, `eta_D=0` would imply every nonempty `F_s` is contained in its assigned `G_g`; since both are partitions into four nonempty sets, this forces the partitions to be identical. Therefore `eta_D>=1).
- If D is a switch, one nonempty `F_s` is assigned as the common label to two distinct, disjoint outer fibers. It cannot be contained in both, so again `eta_D>=1).

Equation (2.1) would then give
`y=sum_D y_D >= sum_D eta_D >=7`,
contradicting `y=8-2z=6`. Hence `{F_s}={G_g}` also for z=1.

## 5. No switch blocks when z=0 or z=1

Relabel the coincident partitions so that `F_h=G_h). All four fibers are nonempty. Suppose D is a synchronized switch with duplicated common label s and transposed partner j. In the canonical 4,5,5 switch normal form, the three extra small-to-outer edges all use small-side label s; the outer vertex q_{D,j} receives two of these edges.

By the singleton-track blocker, q_{D,j} is adjacent to all of `F_s); by outer-track completeness, it is adjacent to all of `G_j=F_j). The fibers are disjoint and nonempty, so
`d_R(q_{D,j}) >= n_s+n_j >=2`.
But q_{D,j} receives two extra Q-Q incidences, so the pointwise degree identity `e_Q(q)+d_R(q)=3` forces `d_R(q)<=1), a contradiction.

Thus every outer block is in the aligned singleton normal form for z=0 and z=1, and the small-block and outer-track fiber partitions coincide up to relabeling.

## 6. What remains open

This removes all switch and double-track escape mechanisms in the two lowest residual-excess cells of the 3+7 branch. It does **not** eliminate the fully aligned z=0 or z=1 completions. Those cells still require coupling the exact endpoint-load matrix, the weighted outer-heavy graph, and the all-color reserve / Type-I gadget constraints.

No retracted degree-nine claim or exceptional-vertex injectivity is used. Full-support E408/Q32 and EG617(r=12) remain **OPEN / NOT_CERTIFIED**.
