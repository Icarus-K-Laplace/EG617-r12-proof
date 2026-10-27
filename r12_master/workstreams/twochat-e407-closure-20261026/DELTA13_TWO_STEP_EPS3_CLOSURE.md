# E407 Q32 — delta=13 two-step augmentation: epsilon_U=3 terminal closure

Date: 2026-10-27  
Status: **PROVED_CONDITIONAL strict closure** under the frozen E407-Q32 core/support contract and the registered Kang–Pikhurko equality structure. Together with `DELTA13_TWO_STEP_EPS1_EPS2_CLOSURE.md`, this closes the entire two-step augmentable non-four-partite delta=13 branch. E407 Q32 remains OPEN.

## 1. Frozen epsilon_U=3 terminal

After the previous reduction and the epsilon=1,2 closure, the only two-step augmentable terminal is

\[
H[W]=K_4\dot\cup K_4\dot\cup K_5\dot\cup K_5,
\]

with no W-cross edges. Write these four W-components as

\[
C_x,\ C_y,\ C_3,\ C_4,
\qquad |C_x|=|C_y|=4,\ |C_3|=|C_4|=5.
\]

The previous closure proves that

- `x` is complete to `C_x` and to no other W vertex;
- `y` is complete to `C_y` and to no other W vertex;
- `C_x != C_y`;
- `xy` is a target nonedge;
- the two augmentation edges avoid x and y.

In the balanced KP equality model on U, the base parts P1,P2,P3,P4 all have size seven. The complement H0=bar(L*) has P3 and P4 as target K7s, has no target edges between P3 and P4, and x,y are target-nonadjacent to every vertex of P3 union P4. Because the two added target edges avoid x,y and neither added edge has type P3-P4, all these relations remain true in the original H.

For z in P3 union P4 the exact U-degree formula gives

\[
d_H(z,W)=6-I_z\le6,
\]

where I_z is the number of the two added target edges incident with z.

Finally, alpha(H)<=4 implies the standard saturation rule: every U vertex is complete to at least one of the four W-components, because otherwise one can choose a non-neighbour from each W-component and obtain an independent five-set with that U vertex.

## 2. P3 and P4 cannot use either K4 as a saturation label

Take z in P3 union P4. Suppose z is complete to C_x.

The vertices x and z are nonadjacent in H. Vertex x has exactly the four neighbours of C_x in W and is anticomplete to the other three W-components. Since d_H(z,W)<=6 and z already uses four neighbours on C_x, z has at most two W-neighbours outside C_x.

Hence in each of the three other W-components there exists a vertex nonadjacent to z; those vertices are automatically nonadjacent to x as well. Choosing one such vertex from each component gives three pairwise nonadjacent W vertices. Together with the nonadjacent pair x,z they form an independent five-set, contradiction.

Therefore no z in P3 union P4 is complete to C_x. The same argument with y gives

\[
\boxed{\text{no vertex of }P_3\cup P_4\text{ can use either }C_x\text{ or }C_y\text{ as a saturation component}.}
\tag{2.1}
\]

By the saturation rule, every vertex of P3 union P4 must therefore be complete to C3 or C4.

Because d_H(z,W)<=6<10, no such vertex can be complete to both K5 components. Thus every vertex of P3 union P4 has a unique K5 saturation label in {C3,C4}.

## 3. Each of P3 and P4 must use both K5 labels

Each P_i, i=3,4, is a target K7 in H.

If all seven vertices of P3 were complete to the same K5, say C3, then

\[
H[P_3\cup C_3]\cong K_{12},
\]

contradicting omega(H)<=11. Hence both C3 and C4 occur as saturation labels on P3. The same argument applies to P4.

Therefore there exist

\[
u\in P_3,\qquad v\in P_4
\]

that share the same K5 saturation label, say C3.

## 4. A shared K5 label across P3 and P4 creates an independent five-set

The pair u,v is nonadjacent in H because H has no P3-P4 target edges.

Both u and v are complete to C3. Since each has W-degree at most six, each has at most one W-neighbour outside C3. Thus the union of their outside-C3 W-neighbour sets has size at most two.

The three remaining W-components are C_x,C_y,C4, of sizes 4,4,5. In each one choose a vertex outside the union of those at most two neighbours. The three chosen vertices are pairwise nonadjacent because distinct W-components have no target edges, and each is nonadjacent to both u and v.

Together with the nonadjacent pair u,v they form an independent five-set in H, contradicting alpha(H)<=4.

This contradiction proves

\[
\boxed{\epsilon_U=3\text{ is impossible in the two-step augmentable delta=13 branch}.}
\tag{4.1}
\]

## 5. Two-step augmentable branch closed

Combining this file with `DELTA13_TWO_STEP_EPS1_EPS2_CLOSURE.md` and the earlier universal three-neighbour reduction:

- epsilon_U=0: excluded by the degree-sum / three-neighbour inequality;
- epsilon_U=1: both W terminals excluded;
- epsilon_U=2: K3+3K5 excluded;
- epsilon_U=3: 2K4+2K5 excluded above.

Hence

\[
\boxed{\delta=13,\ L_U\text{ non-four-partite, two-step K5-safe augmentable }\Longrightarrow\bot.}
\]

The remaining delta=13 non-four-partite forks are strictly:

1. exactly one K5-safe augmentation edge, after which the 308-edge graph is K5-saturated;
2. the original 307-edge L_U is already K5-saturated.

No conclusion is claimed for those saturated forks here, and no E407-Q32 or EG617 closure is claimed.
