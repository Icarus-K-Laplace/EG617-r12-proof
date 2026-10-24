# General-r Cell B Latin / Rainbow Extension Reduction

Status: **PROVED_SYMBOLIC** conditional on the Cell B normal form from `GENERAL_R_NEAR_ANCHOR_2R_MINUS1_NORMAL_FORM.md`.

## 1. Canonical Cell B model

Put

`q=r-1`.

Let A,B be the two q-vertex sides of `K_(q,q)`. Fix a 1-factorization

`M_1,...,M_q`.

Choose `uv in M_1` and subdivide it by w. The union of the non-target colors on W is

`S(K_(q,q))`.

Use the canonical color decomposition:

- for `j=2,...,q`, color j is `M_j` and w is isolated;
- color1 is `(M_1\{uv}) union {uw,wv}`.

The target color is the complement.

Let T be the three target-independent anchors, all target-nonadjacent to W.

## 2. Exact deletion formula for an ordinary color

Fix an ordinary color `j>=2`.

Then

`C_j[W]=M_j union {isolated w}`.

For any set `N subseteq W`, deleting N gives

`alpha(C_j[W\N])`

`= 1_(w notin N) + # {e in M_j : e is not fully contained in N}`

`= r - rho_j(N)`,

where

> **`rho_j(N)=1_(w in N)+# {e in M_j : e subseteq N}`.**

Now let `S subseteq T` be independent in color j and put

`N_j(S)=union_(t in S) N_(C_j)(t) intersect W`.

Any independent set in `C_j[W\N_j(S)]` can be adjoined to S. Since the global color-j independence number is at most r,

`|S|+alpha(C_j[W\N_j(S)])<=r`.

Hence the exact extension constraint is

> **`rho_j(N_j(S))>=|S|`.**

Equivalently,

> **`1_(w in N_j(S)) + # {e in M_j : e subseteq N_j(S)} >= |S|`.**

This is necessary and sufficient for the W-part of the color-j independence constraint for that anchor subset S.

## 3. Single-anchor consequence

Take `S={t}`.

Then t must satisfy one of two conditions in every ordinary color j:

1. `tw` has color j; or
2. t is color-j adjacent to both endpoints of at least one factor edge `e in M_j`.

Thus the cheapest ordinary-color certificate costs

- one T-W edge if it uses w;
- otherwise two T-W edges forming a complete factor pair.

Since the single edge tw has only one color, each anchor can use the one-edge certificate in at most one ordinary color.

## 4. Rainbow matching consequence

Suppose anchor t uses the two-edge certificate in distinct ordinary colors j and k.

The selected factor edge in `M_j` and the selected factor edge in `M_k` must be vertex-disjoint. Otherwise the shared W-vertex would require the same T-W edge to carry two colors.

Therefore the collection of factor edges selected by one anchor across its two-edge ordinary colors is a

> **rainbow matching in the 1-factorization `M_2,...,M_q`.**

Equivalently, in the Latin-square representation of the factorization it is a partial transversal.

At minimum incidence, an anchor uses such a rainbow matching in all but at most one ordinary factor.

## 5. Two- and three-anchor certificate diversity

Let two anchors s,t be independent in ordinary color j.

Then the exact constraint is

`rho_j(N_j({s,t}))>=2`.

Thus two anchors cannot rely only on the same single certificate:

- if both use only w, their mutual anchor edge must have color j so that they are not independent in color j;
- if both use the same factor edge and neither contributes w, their mutual anchor edge must again have color j;
- otherwise their union must contain at least two distinct certificates.

Similarly, if all three anchors are independent in ordinary color j, then

> **their union must contain at least three certificates.**

In a minimum-incidence configuration with no w certificate, this forces the three anchors to select three distinct edges of the same factor `M_j`.

Since there are only three anchor-anchor edges total, all but at most three colors see the full three-anchor independence constraint.

## 6. Exceptional color1

For color1, write

`Q=M_1\{uv}`

and let P be the path `u-w-v`.

Then

`C_1[W]=Q disjoint_union P`.

For `N subseteq W`,

`alpha(C_1[W\N])`

`= # {e in Q : e not fully contained in N} + alpha(P\N)`.

Define

> **`rho_1(N)=2-alpha(P\N)+# {e in Q:e subseteq N}`.**

Since the original alpha is `r`, the exact extension condition for a color1-independent anchor set S is

> **`rho_1(N_1(S))>=|S|`.**

For a single anchor, one color1 edge to u or v already gives one unit of reduction; alternatively it may fully cover one Q-edge.

## 7. Minimum-incidence anchor pattern

For one anchor t, the W-extension has `2r-1=2q+1` available edges.

The cheapest pattern is:

- one ordinary color uses the w-certificate, cost1;
- the other `q-2` ordinary colors use full factor-pair certificates, cost `2(q-2)`;
- color1 uses one unit certificate, cost1.

Total mandatory cost:

> **`2q-2=2r-4`.**

Thus only three T-W edges remain outside the minimum certificate skeleton.

The selected factor pairs form a rainbow matching of size `q-2`.

## 8. Three-anchor Latin reduction

For the three anchors, the Cell B local extension problem reduces to the existence of three large rainbow partial transversals of the factorization with the following compatibility:

- each anchor separately selects pairwise vertex-disjoint factor edges across its active ordinary colors;
- in every ordinary color not used on an anchor-anchor edge, the three anchors must provide three distinct certificates, hence in the minimum pair-only regime select three distinct factor edges;
- at most three colors can evade that full three-anchor condition through the three anchor-anchor edges;
- each anchor has only three T-W edges beyond its minimum certificate skeleton.

Therefore the correct downstream object is not an arbitrary graph-extension problem but a

> **three-fold near-complete Latin partial-transversal extension problem.**

Any final nonextension theorem for Cell B must exploit this factorization structure together with the remaining `3r-1` outside vertices; W-internal edge counts alone are already sharp.