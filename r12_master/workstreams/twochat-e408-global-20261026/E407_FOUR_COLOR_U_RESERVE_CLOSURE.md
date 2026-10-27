# E407 Q32 — U-edge reserve closure

Updated: 2026-10-27
Status: **PROVED_CONDITIONAL E407-Q32 CONTRADICTION** under the frozen V12 29-point/49-block support contract and its proved selected-component color identity.

This supersedes `E407_EXTRA_EXACT_U_RESERVE_CLOSURE.md` and the earlier four-color aggregate version. The contradiction already follows from **one** unselected non-target color.

## 1. Frozen V12 support object

Under the retained E407-Q32 V12 terminal contract, every surviving completion uses a target-color core H and support U with

\[
|H|=47,\qquad e(H)=284,\qquad |U|=29,
\]

and 49 independent four-set support blocks, seven in each of seven selected exact-129 non-target color classes. The blocks are disjoint within each selected color and pairwise linear across selected colors.

Put

\[
L_U=\overline{H[U]}.
\]

The exact support ledger is

\[
\boxed{e(L_U)=294+\delta,\qquad 3\le\delta\le16.}\tag{1}
\]

Thus

\[
\boxed{e(L_U)\le310.}\tag{2}
\]

## 2. The selected 49 blocks own 294 distinct non-target edges

`SUPPORT_BLOCK_ANCHOR_IDENTITY.md` on the active E407 sibling proves that every selected support block Q is exactly the H-four-set of a selected isolated monochromatic K5 component of its assigned exact-129 color.

Therefore all six pairs inside Q have that assigned non-target color.

Within one selected color the seven blocks are vertex-disjoint, so their pair sets are disjoint. Across different selected colors the 4-sets are pairwise linear, so two blocks share at most one vertex and hence share no pair. Consequently the 49 blocks own exactly

\[
49\binom42=49\cdot6=294
\]

distinct edges of L_U.

Call this selected edge set S. Then

\[
|S|=294.\tag{3}
\]

By (1), after the selected support edges only

\[
e(L_U)-|S|=\delta\le16\tag{4}
\]

non-target U-pairs remain available to every color outside the selected seven.

## 3. One unselected non-target color already exceeds the reserve

Relative to the target color, the balanced coloring has eleven non-target colors in total. The support system uses only seven distinct selected exact-129 color classes. Therefore at least one non-target color D is not among the selected seven (in fact there are four).

No hypothesis on whether D is exact is needed.

For every non-target color in the original balanced K145 coloring,

\[
\alpha(D)\le12,
\]

because every 13-set must contain an edge of every color. Hence

\[
\alpha(D[U])\le12.
\]

By Turan's theorem, a graph on29 vertices with independence number at most12 has at least

\[
p_{12}(29)
=5\binom32+7\binom22
=15+7
=22
\]

edges. Thus

\[
\boxed{e_D(U)\ge22.}\tag{5}
\]

Every D-edge in U lies in L_U. Since D is not one of the seven selected colors, unique edge ownership makes all these D-edges disjoint from S. Equations (3) and (5) therefore force

\[
e(L_U)\ge294+22=316.
\]

But (2) gives

\[
e(L_U)\le310.
\]

Hence

\[
\boxed{316>310},
\]

a contradiction with gap six.

Equivalently, the residual U-edge reserve after the 49 labelled support blocks is at most16, while **one** unselected non-target color needs at least22.

For reference, using all four unselected colors would give the stronger aggregate requirement `294+4*22=382`, but that extra counting is unnecessary.

## 4. Conclusion

Under the frozen V12 support contract and the proved selected-component color identity,

\[
\boxed{\text{no E407 Q32 V12 completion exists}.}
\]

This closes all five V12 shell templates simultaneously; their row types, high-k anchor counts and low-delta subdivisions are irrelevant once the selected support blocks are known to be genuinely color-labelled K5 components.

Status: **PROVED_CONDITIONAL**, because V12 exhaustiveness and its retained analytic/lower-order screen hypotheses remain parent dependencies.

## 5. Exhaustiveness interface

The active E407 sibling's `FIVE_TEMPLATE_GLOBAL_COMPATIBILITY.md` states that every legal completion of each of the five alternative V12 shell templates uses the same exact support contract above. The independently replayed V12 certificate records that all 554 finite-screen survivors are covered by these five templates.

Thus, relative to the retained V12 analytic/lower-order contracts, this contradiction covers the entire E407 maximum-Q32 survivor set, not only one low-delta or minimum-slack subcase.

## 6. Dependency firewall

Load-bearing inputs:

1. V12 survivor exhaustiveness under its retained analytic/lower-order hypotheses;
2. the frozen support contract |U|=29 with 49 blocks in seven distinct selected exact colors;
3. pairwise block linearity/disjointness;
4. `SUPPORT_BLOCK_ANCHOR_IDENTITY.md`, specifically that every selected block is the four-core part of a monochromatic selected-color K5;
5. the exact ledger e(L_U)=294+delta with delta<=16;
6. existence of at least one non-target color outside the selected seven (automatic since there are eleven non-target colors);
7. the balanced-coloring consequence alpha(D)<=12 for every non-target color;
8. Turan's theorem;
9. unique edge ownership.

Not used:

- `E407_SEVEN_EXACT_COLOR_EXCLUSION.md`;
- any exceptional-vertex degree argument;
- Brouwer/Kang--Pikhurko second-Turan bounds;
- the five individual shell template row structures;
- the repeated-anchor theorem;
- the Didin-dependent delta=14 branch;
- any E408 285-edge identity;
- any Q33 support-31 identity.

Therefore this is the shortest dependency-light E407 closure currently known in this project.
