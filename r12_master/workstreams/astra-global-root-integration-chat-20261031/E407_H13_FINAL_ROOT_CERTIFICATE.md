# E407 / h13 final certificate

Status: PROVED for EVERY F with |F|=61, e(F)=407, delta(F)=13, alpha(F)<=5, omega(F)<=11, and all induced D caps. Original contextual parents satisfy these hypotheses by the independent frontend.

For each regular p (degree13), A=N_F(p) has13 points and C=F-N_F[p] has47. Let M=complement(F[A]), z=e(M), g_a=d_F(a)-13>=0 and q_p=z+sum_A g_a. Then |N_C(a)|=d_M(a)+g_a and disjoint edge counting gives

    407=13+(78-z)+(2z+sum g)+e(C)=91+q_p+e(C).

Here91=binom(14,2), not an assumed complete closed neighborhood. Independent five points in C would extend with p, so alpha(C)<=4; omega<=11 and ALL caps are inherited. The low-edge gate plus286 exclusion imply e(C)>=287, hence q_p<=29 for EVERY regular p.

The regular set is nonempty because delta=13. Its maximum Q thus satisfies Q<=29. The independently audited COVER theorem applies to the SAME fixed F and SAME full regular set and gives Q>=30. Contradiction.

This proves the complete h13 layer, including nonmaximum pivots, low charges, all support types and repivot overlaps. Graphs of minimum degree12 are covered separately; a merely degree13 vertex in such a graph is not used to invoke COVER.

Sources: low 783c72090205d4bd1a6eefce1dec09e15f78e319; equality c3d07b2ca5912b1b0c1c6998303c19c3c2911340; COVER 531e41c79e08dd2bb3892ca9ba8a491a56678565. Full local audited dependencies are frozen in this workstream.
