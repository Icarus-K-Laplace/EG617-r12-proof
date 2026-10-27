# Progress log — E407 Q32 two-chat closure workstream

Date: 2026-10-27  
Branch: `workstream/r12-twochat-e407-closure-20261026`

Historical detailed Rounds 1–12 are preserved in commit `3b336b34b8540da89f4dac6589d056ac48bcfe10` and its ancestors. This file records the current canonical progress and the new Rounds 13–15 without claiming terminal closure.

## Historical state through Round 12

The workstream had already:

- rebuilt the exact low-delta frontier and corrected the feasible profile count to 56;
- proved the support omission-degree identity;
- repaired the A/C component-witness capacity proof through the registered row-transversal theorem;
- excluded the registered delta=13, epsilon_U=2 one-cross-edge (4,4,5,5) W profile;
- proved the W-side support-block transversal and common-neighbour inequalities;
- proved alpha(H[W])=4 universally;
- classified zero-slack U-neighborhood classes in the low-slack region;
- excluded single-vertex concentration of the seven minimum-slack units;
- reduced the slack-one minimum profiles to an exact (7,7,7,8) U-kernel;
- proved SUPPORT_BLOCK_ANCHOR_IDENTITY.md, identifying each of the 49 selected blocks with the H-four-set of a selected exact-color K5 component;
- proved SELECTED_COMPONENT_RESIDUAL_PARTITION.md, giving the exact per-color residual `3K5 + G11` after deletion of the seven selected components.

E407 Q32 remained OPEN.

## Round 13 — selected B-anchor floor five

**Commit:** `f2f991695a23b30c26a90070d7c2d1ab25b9d4f8`

Added `SELECTED_B_ANCHOR_FLOOR.md` and `verify_selected_b_anchor_floor.py`.

For one exact-129 color c, partition the ten B vertices among:

- selected K5 components: b_c vertices;
- three unselected K5 components: u_c vertices;
- exceptional G11: g_c vertices.

Because B is a target K10, each color-c K5 contains at most one B vertex, so u_c<=3. Since B cap G11 is independent in color c and alpha(G11)=2, g_c<=2. Hence

\[
b_c+u_c+g_c=10\Longrightarrow b_c\ge5.
\]

With seven selected components, b_c<=7, so
\[
\boxed{b_c\in\{5,6,7\}.}
\]

The live b_c=3 and b_c=4 residual branches are therefore empty.

If b_c=5, then (u_c,g_c)=(3,2). The pivot p must be selected: p cannot share an unselected K5 with B because p-B is target-colored, and p cannot lie in G11 with the two B vertices because that creates a color-c independent triple in a gadget of independence number two. Thus
\[
A_c^{sel}=\{p,s_c\}\cup B_c,\quad |B_c|=5.
\]
Consequently every exact color has at most one selected S-anchor.

Across seven exact colors:

- at least 35 selected support-block occurrences are B-anchored;
- at most seven are S-anchored.

Combining b_c>=5 with V12 high-k row floors gives actual selected-block floors:

- A: >=7 selected k=3 B-blocks globally;
- B: >=21 selected k>=2 B-blocks;
- C: >=7 selected k=3 B-blocks;
- D: >=14 selected high-k B-blocks;
- E: no positive floor from this cardinality intersection alone.

The verifier checks only finite arithmetic, not graph realization or the external exact-129 factor theorem.

## Round 14 — two residual shell edges per exact color

**Commit:** `d9478df06e1952e89f3a799dbed8ada41e441454`

Added `SHELL_COLOR_EDGE_LOAD.md` and `verify_shell_color_edge_load.py`.

For an exact color c, selected anchors lie in isolated selected K5 components, so any shell edge of color c has both endpoints among unselected shell labels.

The 26-vertex residual is three unselected K5 components plus G11. Every unselected K5 must contain an outside-core label, otherwise it would be a target-independent K5 inside H, contradicting alpha(H)<=4.

A three-case analysis by pivot location proves that, regardless of whether p is selected, lies in an unselected K5, or lies in G11,
\[
\boxed{e_c(M[A\setminus A_c^{sel}])\ge2.}
\]

The seven exact colors therefore use at least fourteen distinct shell missing edges. The important output is the per-color induced-subgraph list constraint, not the scalar fourteen.

The verifier independently checks the minimum edge count in all integer distribution cases.

## Round 15 — shell-only Hall/SDR route certified insufficient

**Commit:** `12ff5bfe8c631b7514f534bf0fbdfc1b0424aa92`

Added `SHELL_LIST_RELAXATION_AUDIT.md` and `verify_shell_list_relaxation.py`.

For any shell missing graph M with at least fourteen edges, choose fourteen distinct edges and pair them into seven colors. For each color, the two chosen edges use at most four B endpoints, so at least six of the ten B labels avoid both edges. Select those six B labels plus p as the abstract selected-anchor set.

Thus the coarse shell-label constraints

- b_c>=5;
- at most one selected S anchor;
- two unselected shell edges per exact color;
- shell edge uniqueness

are simultaneously feasible for every M with e(M)>=14. Since every V12 template has e(M)>=22, no shell-only Hall/list argument can close E407.

This is **not** a graph realization. It is a route audit proving that the next theorem must use the same U/H row/component geometry.

## Current mathematical gain

The global join has moved from a loose “selected support blocks versus auxiliary component witnesses” problem to a genuinely labelled selected-component system:

1. every selected block has an exact-color K5 anchor;
2. at least five of the seven anchors per exact color lie in B;
3. at most one lies in S;
4. every exact color still has three unselected K5 components plus G11 on the exact residual 26 vertices;
5. every exact color must own at least two shell edges completely outside its selected anchor set;
6. the shell-only relaxation is known to be insufficient.

## Current open contracts

- Five templates A–E: all OPEN against the common 284-edge core/support system.
- delta=13 four-partite epsilon_U=0: OPEN.
- delta=13 non-four-partite: OPEN.
- delta<=12: OPEN.
- delta=14 saturated branch: only PROVED_CONDITIONAL because of the unaudited Didin dependency.
- Minimum-slack complementary no-slack-one branch: OPEN.
- Original K145/T61/V12 dependency chain and full EG617 theorem: NOT_CERTIFIED.

## Highest-priority next theorem

Prove a same-core labelled support-row incompatibility for A–E using the actual selected B-anchor blocks, exact D_a row supports, same-anchor block disjointness, support linearity, residual 3K5+G11 structure, W-side transversal constraints, and the four-unit core excess.

No local profile or arithmetic verifier is treated as E407 closure.
