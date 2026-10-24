# High-stop Round 2: excess concentration, critical windows, predecessor interface

Date: 2026-10-24  
Workstream: `general-r-residual-core-extraction-20261024`

Primary status: **partial progress; NO-HIGH-STOP remains OPEN**.

This file only attacks the high-stop obstruction. It does not revisit the residual-core minimum-degree theorem or fixed-r recurrence.

## 1. Exact simultaneous excess concentration

Let (R_a) be a first (K_r)-free canonical stop, (a\ge 6), with (n=ar+1). For the target color (0), let (x_0=e(G_0[R_a])-p_a(n)); for each non-target color (i\in\{1,\dots,r-1\}), let (x_i=e(G_i[R_a])-p_r(n)). The established ledger is

[
x_0+\sum_{i=1}^{r-1}x_i=S_a(r)
=\left(\binom a2-1\right)r+a.
]

All (x_i\ge0), so (\sum_{i=1}^{r-1}x_i\le S_a(r)).

### Theorem 1 — simultaneous near-Turán edge counts

Define

[
C_{a,r}:=\left\lceil\frac{2S_a(r)}{r-1}\right\rceil.
]

Then at least \(\lfloor r/2\rfloor\) non-target colors satisfy

[
x_i\le C_{a,r}\le a^2-1
qquad (r\ge a+1).
]

**Proof.** Let (m) be the number of non-target colors with (x_i>C_{a,r}). Since each such integer excess is at least (C_{a,r}+1>2S_a(r)/(r-1)),

[
m\frac{2S_a(r)}{r-1}<\sum_{i=1}^{r-1}x_i\le S_a(r),
]

so (m<(r-1)/2). Hence at least \(\lfloor r/2\rfloor\) colors lie below the threshold.

For the uniform bound, the inequality (C_{a,r}\le a^2-1) is equivalent to

[
(a+1)r\ge a^2+2a-1,
]

which holds strictly for (r\ge a+1). \(\square\)

For (a=6), (S_6(r)=14r+6), and

[
C_{6,r}=\left\lceil28+\frac{40}{r-1}\right\rceil.
]

Thus for (r\ge41), at least \(\lfloor r/2\rfloor\) non-target colors have (x_i\le29).

### Exact Turán interpretation

For each non-target color, (F_i:=\overline{G_i[R_a]}) is (K_{r+1})-free and

[
e(F_i)=t_r(ar+1)-x_i,
\qquad
t_r(n):=\binom n2-p_r(n).
]

Consequently at least half of the non-target complements are within (a^2-1) edges of the exact Turán maximum. This is a proved edge-count concentration theorem, not yet a partition/edit-distance stability theorem.

**Open stability issue.** The number of parts (r) grows with the parameter. A fixed-(r) stability statement cannot be applied with constants silently assumed uniform in (r). We still need a quantitative uniform lemma of the form

[
e(F)\ge t_r(ar+1)-C
\Longrightarrow
F\text{ is within }f(a,C)\text{ edits of }T_r(ar+1),
]

with an explicit (f) independent of (r). This implication is not claimed here.

## 2. Exact residue windows from the critical-core polynomial

Let (Q\subseteq R_a) be the induced ((r+1))-critical core, with

[
q=|Q|=\ell r+t,\qquad 0\le t<r.
]

The inherited cap and the Kostochka–Yancey lower bound require

[
P_{\ell,t}(r)\le0,
]

where

[
P_{\ell,t}(r)
=r^2(-\ell^2+3\ell+t-1)
+r(-2\ell t-2\ell-t^2+2t+1)-2t+2.
]

For \(\ell\ge2\), define

[
A_\ell=\ell^2-3\ell+1=(\ell-1)(\ell-2)-1,
\qquad
B_\ell=\ell^2-\ell-1=\ell(\ell-1)-1,
]

and

[
R_\ell:=\ell(\ell-1)^2(\ell-2)+2\ell+2.
]

### Theorem 2 — bounded residue windows

If (r\ge R_\ell) and (P_{\ell,t}(r)\le0), then

[
\boxed{t\le A_\ell
\quad\text{or}\quad
r-t\le B_\ell.}
]

When \(\ell=2\), the first alternative is impossible because (A_2=-1), so necessarily (r-t\le1).

**Proof sketch.** Put (u=r-t). Direct algebra gives the two equivalent forms

[
\frac{P_{\ell,t}(r)}r
=t(r-t)-2(\ell-1)t-A_\ell r-(2\ell-1)-\frac{2t-2}{r},
]

and

[
\frac{P_{\ell,r-u}(r)}r
=u(r-u)+2(\ell-1)u-B_\ell r-(2\ell+1)+\frac{2u+2}{r}.
]

Each right-hand side is a concave quadratic in its residue variable. For (r\ge R_\ell), it is positive at both endpoints of the interval from the proposed boundary (A_\ell+1) (respectively (B_\ell+1)) to (r/2). Concavity then makes it positive throughout that interval. Therefore (P\le0) forces one of the two stated boundary windows. All thresholds here are explicit. \(\square\)

For a fixed (a), (r\ge R_a) therefore confines (q\le ar+1) to bounded-width windows around multiples of (r). In particular,

[
R_6=614.
]

For (a=6), (r\ge614), and the already-proved (3r-1\le q\le6r+1), the only possible critical-core orders lie in

[
\boxed{
[3r-1,3r+1]
\;\cup\;
[4r-5,4r+5]
\;\cup\;
[5r-11,5r+11]
\;\cup\;
[6r-19,6r+1].
}
]

These are necessary windows, not existence claims. They eliminate every middle-residue regime but do **not** eliminate the surviving windows. In particular the current critical-core potential alone does not close (a=6).

## 3. First-stop predecessor interface

Suppose (R_a) is the first (K_r)-free state and (R_{a+1}) is its predecessor. Let (B\cong K_r) be the target-color clique deleted to obtain (R_a), and let (n=ar+1=|R_a|).

For each (v\in R_a), consider the (r) edges between (v) and (B). Since (B\cup\{v\}) has (r+1) vertices, the balanced-coloring condition requires every one of the (r) colors to occur among these edges or inside (B). The target color already occurs inside (B), so every non-target color must occur at least once among the (r) cross-edges.

Thus exactly one of the following happens for each (v):

1. (v) has exactly one target-color neighbor in (B), and each of the (r-1) non-target colors occurs exactly once on (vB);
2. (v) has no target-color neighbor in (B), and exactly one non-target color occurs twice on (vB), with all other non-target colors occurring once.

Let (q_0=e_0(B,R_a)), the number of vertices in case 1. For each non-target color (i), let (z_i) be the number of vertices in case 2 whose duplicated color is (i). Then

[
\sum_{i=1}^{r-1}z_i=n-q_0,
\qquad
e_i(B,R_a)=n+z_i.
]

The excesses of the predecessor and current states satisfy the exact identities

[
x_0(R_{a+1})=x_0(R_a)+q_0,
]

[
x_i(R_{a+1})=x_i(R_a)+z_i
\quad (i\ge1).
]

Consequently every color's excess is monotone nondecreasing when moving backward one canonical step, and the total increment is exactly

[
q_0+\sum_i z_i=n= S_{a+1}(r)-S_a(r).
]

This is a genuine first-stop constraint: the predecessor interface is a near-permutation matrix, with one target edge per column or one duplicated non-target color. It gives a precise starting point for the (K_r)-transversal / label-class route, but no transversal theorem has yet been derived from it.

## 4. Status ledger for this round

### PROVED

- At least \(\lfloor r/2\rfloor\) non-target colors are within (a^2-1) edges of the exact Turán maximum in the complement.
- The critical-core polynomial confines fixed-(a) residues to explicit bounded-width windows for (r\ge R_a).
- The predecessor-clique cross-color incidence and excess increments are exact.

### NOT PROVED

- (a=6) is impossible.
- Any (a\ge7) candidate contains a legal induced (R_{a-1}).
- Uniform quantitative edit-distance stability with growing part count (r).
- Pairwise approximate orthogonality / a resolvable-design skeleton.
- A design-trimming implication yielding an earlier (R_5) or (R_4).

### Current verdict

[
\boxed{\texttt{NO-HIGH-STOP = OPEN}.}
]

The critical-core potential has reduced the (a=6) case to four explicit residue windows, but no all-large-(r) contradiction has been established. The next highest-leverage step is to prove uniform Turán edit stability for fixed (a), (C=O(a^2)), and growing (r), then combine it with the exact predecessor-interface lemma.