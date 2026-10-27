# E407 Q32 — exact-color shell-edge load after selected-anchor removal

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL on the exact-129 factor theorem and selected-support-component identity. Necessary global shell constraint; E407 Q32 remains OPEN.**

## 1. Setup

Fix an exact-129 non-target color c. Let A_c^sel be its seven selected outside-core anchors. By the support-component identity these anchors lie in {p} union A and belong to seven isolated color-c K5 components. Therefore no color-c edge joins a selected anchor to any vertex outside its own selected K5 component.

The complement of the seven selected components is the 26-vertex residual

R_c={u_c} union W union (({p} union A)\A_c^sel),

and the exact factor theorem decomposes R_c into three unselected isolated color-c K5 components plus the 11-vertex exceptional gadget G_c, with alpha(G_c)=2.

Let Z_c=({p} union A)\A_c^sel. Then |Z_c|=7. Every unselected K5 contains at least one vertex of Z_c: otherwise it would be a color-c K5 entirely inside H, hence a target-independent 5-set in H, contradicting alpha(H)<=4.

## 2. Localization of shell edges of color c

Any color-c edge inside the shell A has both endpoints in A\A_c^sel.

Indeed, a selected shell anchor belongs to an isolated selected K5 component and has no color-c edge to a different shell vertex. Thus

E_c(A) subset E(M[A\A_c^sel]).   (2.1)

Here M is the shell missing graph, so every non-target shell edge is an edge of M.

## 3. Each exact color needs at least two shell edges

We prove

|E_c(A)| >= 2.   (3.1)

There are three cases according to the position of the pivot p.

### Case I: p is selected

All seven vertices of Z_c lie in A. Let r_1,r_2,r_3>=1 be the numbers of shell vertices in the three unselected K5 components, and let t=7-r_1-r_2-r_3 be the number of shell vertices in G_c.

The K5 components force sum_i binom(r_i,2) color-c shell edges. Inside the t shell vertices of G_c, independence number at most two forces at least

binom(t,2)-floor(t^2/4)

color-c edges, because the complement on those t vertices is triangle-free. Hence

|E_c(A)| >= sum_i binom(r_i,2)+binom(t,2)-floor(t^2/4).

For r_i>=1 and r_1+r_2+r_3+t=7, the right side is at least two. The finite arithmetic is replayed by verify_shell_color_edge_load.py.

### Case II: p is residual and lies in an unselected K5

Because p is target-adjacent to every shell vertex, its color-c K5 contains no shell vertex. Thus that K5 uses p plus four core vertices. The other two unselected K5 components each contain at least one shell vertex. If their shell counts are r_1,r_2>=1 and the gadget contains t=6-r_1-r_2 shell vertices, then

|E_c(A)| >= binom(r_1,2)+binom(r_2,2)+binom(t,2)-floor(t^2/4) >=2.

### Case III: p lies in the exceptional gadget

The three unselected K5 components each contain at least one shell vertex, say r_1,r_2,r_3>=1, and the gadget contains t=6-r_1-r_2-r_3 shell vertices in addition to p.

Every edge from p to A is target-colored and therefore absent from color c. Since alpha(G_c)=2, any two shell vertices of G_c must be adjacent in color c; otherwise those two vertices together with p form an independent 3-set in G_c. Thus the t shell vertices in the gadget form a color-c clique and contribute binom(t,2) shell edges. Therefore

|E_c(A)| >= sum_i binom(r_i,2)+binom(t,2) >=2.

This proves (3.1) in all cases.

## 4. Seven-color global load

The seven exact-129 colors have pairwise disjoint shell-edge sets, because every shell edge has a unique color. Consequently

|E(M) colored by exact-129 colors| >= 14.   (4.1)

Each of the four 130-edge non-target colors must also occur on at least one shell edge: if a non-target color had no edge inside the 13-vertex shell A, then A would be an independent 13-set in that color, contradicting the balanced alpha<=12 condition. Hence the eleven non-target colors together give the weaker scalar consequence

e(M)>=14+4=18.

The V12 shell contract already has a stronger edge floor, so the value of this theorem is not the scalar 18. The new information is the **localized per-color list condition**

boxed:  e_c(M[A\A_c^sel]) >= 2 for each exact-129 color c.   (4.2)

Thus every exact color must leave at least two shell missing edges entirely among its six or seven unselected shell labels. Selected anchors cannot cover all but one edge of M.

## 5. Combine with the selected B-anchor theorem

By SELECTED_B_ANCHOR_FLOOR.md, every exact color has one of the following selected-anchor types:

- b_c=5: selected anchors are p, one S-vertex, and five B-vertices; hence A\A_c^sel has five B and two S vertices;
- b_c=6 with p selected: A\A_c^sel has four B and all three S vertices;
- b_c=6 with one S selected: A\A_c^sel has four B and two S vertices;
- b_c=7: A\A_c^sel has three B and all three S vertices.

In every one of these cases the induced shell missing graph on the displayed unselected labels must contain at least two edges of the corresponding exact color.

This is a direct global compatibility constraint between the 49 selected components and the five V12 shell templates. It is not implied by the earlier high-k hit counts.

## 6. Scope

The theorem uses the exact-129 factorization, alpha(G_c)=2, the selected-support-component identity, alpha(H)<=4, and the pivot/shell target adjacencies. It does not use the Didin preprint or any delta=13/14/15/16 W-profile theorem.

The finite verifier checks the integer lower bound in the three pivot-location cases only. It does not verify graph realization or the exact-129 factor theorem.

No template is closed yet: the next step is a finite/analytic Hall-type shell-edge assignment problem in which seven exact colors each require two distinct edges in M[A\A_c^sel], while their selected anchor sets obey b_c in {5,6,7}, at most one selected S anchor, same-anchor block disjointness, and the common-core row constraints.
